#Date: 2026-10-26
#Purpose: Proc_step1 - everything that needs no language model: collect new papers (bioRxiv/medRxiv + PubMed journals via
#  Europe PMC), open website submissions and new rows of curated watchlists (pipeline/watchlists.py), then triage each with the abstract rules AND a full-text naming scan.
#  Writes the candidates for Proc_step2 (language-model classification, run in Claude Code) plus a summary.
#  Built for the cluster: full-text downloads run in parallel threads, so it can afford to scan every paper.
#Usage: python3 $SEQBROWSER_HOME/engine/pipeline/step1.py --week --out $SEQBROWSER_HOME/step1_out
#       python3 $SEQBROWSER_HOME/engine/pipeline/step1.py --from 2019-01-01 --to 2019-01-31 --out $SEQBROWSER_HOME/step1_out
#  (normally submitted via cluster/step1.sbatch, not run by hand)
#INPUT: none (public APIs). OUTPUT in --out:
#  step1_<from>_<to>.candidates.jsonl  one flagged paper per line (record + triage routes + extracted names)
#  step1_<from>_<to>.summary.json      counts per source, kept/dropped, and every failure (fail loud, nothing silent)

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta
from pathlib import Path

from common import BIORXIV, FT_STATS, get
from fetch import fetch_journals, fetch_preprints
from submissions import fetch_submissions
from watchlists import fetch_watchlists
from triage import triage


def log(msg):
    print(f"{datetime.now():%H:%M:%S}  {msg}", flush=True)


def check_network():
    """Compute nodes on some clusters have no internet; stop immediately with a clear message instead of finding 0 papers."""
    try:
        get(f"{BIORXIV}/details/biorxiv/2024-01-01/2024-01-01/0", tries=1)
    except Exception as e:
        sys.exit(f"NO INTERNET from this node ({type(e).__name__}: {e}). Run on a node with outbound access (or the login node for testing).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", action="store_true", help="the 7 days ending today, plus open website submissions and new watchlist rows")
    ap.add_argument("--from", dest="start"); ap.add_argument("--to", dest="end")
    ap.add_argument("--out", required=True)
    ap.add_argument("--threads", type=int, default=8, help="parallel full-text downloads (keep modest: public APIs)")
    ap.add_argument("--strict", action="store_true",
                    help="backfill mode: keep only papers where a method-like NAME was extracted (cuts Proc_step2 load ~6x)")
    a = ap.parse_args()
    if a.week:
        end = date.today(); start = end - timedelta(days=6)
        a.start, a.end = start.isoformat(), end.isoformat()
    if not (a.start and a.end):
        sys.exit("give --week or both --from and --to (YYYY-MM-DD)")
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    tag = f"step1_{a.start}_{a.end}" + ("_strict" if a.strict else "")
    log(f"Proc_step1 {a.start} -> {a.end} | out: {out} | threads: {a.threads}")
    check_network()
    log("internet OK")

    t0, failures, counts = time.time(), [], {}
    recs = []
    for label, fn in (("preprints", lambda: fetch_preprints(a.start, a.end)), ("journals", lambda: fetch_journals(a.start, a.end)),
                      ("submissions", (lambda: fetch_submissions(str(out / "submissions_seen.json"))) if a.week else lambda: []),
                      ("watchlists", (lambda: fetch_watchlists(str(out / "watchlists_seen.json"))) if a.week else lambda: [])):
        log(f"collecting {label} ...")
        try:
            got = fn()
        except Exception as e:
            got = []; failures.append(f"{label}: fetch failed: {type(e).__name__}: {e}")
        counts[label] = len(got); recs += got
        log(f"  {label}: {len(got):,} records")

    log(f"triage: {len(recs):,} papers (abstract rules + full-text naming scan)")
    kept, n_ft, last, t1 = [], 0, 0.0, time.time()
    with ThreadPoolExecutor(a.threads) as pool:
        futs = {pool.submit(triage, r): r for r in recs}
        for i, f in enumerate(as_completed(futs), 1):
            r = futs[f]
            try:
                t = f.result()
                # strict (backfill): keep only papers where the extractor found a method-shaped name (it already requires an
                # internal capital, digit, hyphen or &), plus all user submissions
                if t["flag"] and (not a.strict or r.get("submitted") or r.get("watchlist") or t["names"]):
                    kept.append(r | {"triage": t})
                    n_ft += "fulltext-naming" in t["routes"]
                    if "fulltext-naming" in t["routes"] and "abstract" not in t["routes"]:
                        log(f"  + full-text-only hit: {', '.join(t['names'][:3])}  <- {r.get('title', '')[:70]}")
            except Exception as e:
                failures.append(f"triage {r.get('id')}: {type(e).__name__}: {e}")
            now = time.time()
            if now - last > 30 or i == len(recs):  # heartbeat every ~30 s
                rate = i / max(now - t1, 1e-6); eta = (len(recs) - i) / max(rate, 1e-6)
                log(f"  {i:,}/{len(recs):,} ({100 * i / len(recs):.0f}%) | {rate * 60:.0f}/min | ETA {eta / 60:.0f} min | "
                    f"kept {len(kept)} (full-text {n_ft}) | failures {len(failures)} | full texts ok/not-OA/failed "
                    f"{FT_STATS['fulltext_ok']}/{FT_STATS['not_open_access']}/{FT_STATS['fulltext_failed']}")
                last = now

    (out / f"{tag}.candidates.jsonl").write_text("".join(json.dumps(r) + "\n" for r in kept))
    summary = {"range": [a.start, a.end], "fetched": counts, "total": len(recs), "kept": len(kept),
               "routes": {k: sum(k in r["triage"]["routes"] for r in kept) for k in ("abstract", "fulltext-naming", "submitted", "watchlist")},
               "fulltext": dict(FT_STATS), "failures": failures, "minutes": round((time.time() - t0) / 60, 1)}
    (out / f"{tag}.summary.json").write_text(json.dumps(summary, indent=1))
    log(f"DONE in {summary['minutes']} min: kept {len(kept)} of {len(recs):,} -> {tag}.candidates.jsonl")
    print(json.dumps(summary, indent=1))
    if failures:
        print(f"WARNING: {len(failures)} failures - see {tag}.summary.json", file=sys.stderr)
    if FT_STATS["fulltext_failed"] > 0.05 * max(1, sum(FT_STATS.values())):  # >5% of full texts lost: rerun this range
        sys.exit(f"FAIL LOUD: {FT_STATS['fulltext_failed']} full-text downloads failed (>5%) - rerun this range later")


if __name__ == "__main__":
    main()
