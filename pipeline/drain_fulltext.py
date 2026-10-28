#Date: 2026-10-27
#Purpose: Work through the queue of bioRxiv full texts that step1 --defer could not download (HTTP 429 throttling), at
#  whatever rate bioRxiv tolerates (AIMD pacing in common.get), and run the full-text naming scan on each. Papers that
#  turn out to name a method are written as late candidates for Proc_step2. Idempotent and resumable: finished DOIs are
#  recorded in drain_done.json after every paper, downloads are cached, so killing and resubmitting loses nothing.
#Usage: python3 $SEQBROWSER_HOME/engine/pipeline/drain_fulltext.py --out $SEQBROWSER_HOME/step1_out --hours 70
#  (normally via cluster/drain_fulltext.sbatch, which resubmits itself while the queue is non-empty)
#INPUT: <out>/step1_*.deferred.jsonl (records step1 queued). OUTPUT: <out>/step1_*.late_candidates.jsonl, <out>/drain_done.json
#  Exit code 0 = queue empty, 3 = time budget used up with work left (the sbatch wrapper resubmits on 3).

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

import common
from common import FT_STATS
from fetch import full_text
from triage import names_in


def log(msg):
    print(f"{datetime.now():%H:%M:%S}  {msg}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True); ap.add_argument("--hours", type=float, default=70)
    a = ap.parse_args()
    out = Path(a.out); common.FT_CACHE = common.FT_CACHE or str(out / "ft_cache")
    done_p = out / "drain_done.json"
    done = set(json.loads(done_p.read_text())) if done_p.exists() else set()
    queue = [(f, json.loads(l)) for f in sorted(out.glob("step1_*.deferred.jsonl")) for l in f.read_text().splitlines() if l]
    todo = [(f, r) for f, r in queue if r["doi"] not in done]
    log(f"queue {len(queue)} | done {len(queue) - len(todo)} | to fetch {len(todo)} | budget {a.hours} h")
    stop, found, failed = time.time() + a.hours * 3600, 0, 0
    for i, (f, r) in enumerate(todo, 1):
        if time.time() > stop:
            log(f"time budget used: {len(todo) - i + 1} left"); sys.exit(3)
        before = FT_STATS["fulltext_failed"]
        body = full_text(r)  # normal path: paced + long 429 retries (no deferral here)
        if FT_STATS["fulltext_failed"] > before:
            failed += 1; continue  # stays queued for the next run
        names = [n for n in names_in(body or "") if n not in r.get("triage", {}).get("names", [])]
        if names:
            found += 1
            late = Path(str(f).replace(".deferred.jsonl", ".late_candidates.jsonl"))
            with late.open("a") as fh:
                fh.write(json.dumps(r | {"triage": {"flag": True, "routes": ["fulltext-naming", "late"], "names": names}}) + "\n")
            log(f"  + full-text hit: {', '.join(names[:3])}  <- {r.get('title', '')[:70]}")
        done.add(r["doi"])
        done_p.write_text(json.dumps(sorted(done)))  # checkpoint after every paper
        if i % 25 == 0:
            log(f"  {i}/{len(todo)} | hits {found} | still throttled {failed} | bioRxiv gap now "
                f"{common._GAP.get('www.biorxiv.org', 0):.1f} s")
    log(f"DONE: fetched {len(todo) - failed}, hits {found}, still queued {failed}")
    sys.exit(3 if failed else 0)


if __name__ == "__main__":
    main()

# ---- Provenance ----
# Upstream:   pipeline/step1.py --defer (writes step1_*.deferred.jsonl); common.py (AIMD pacing, full-text cache); triage.names_in
# Downstream: Proc_step2 reads step1_*.late_candidates.jsonl alongside step1_*.candidates.jsonl
# References: AIMD congestion control (Jacobson 1988 / TCP); bioRxiv API + JATS XML endpoints
# Notes:      bioRxiv throttles per IP; run ONE drain job at a time. Exit 3 = resubmit.
