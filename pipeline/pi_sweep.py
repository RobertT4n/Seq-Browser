#Date: 2026-10-27
#Purpose: Backfill by author: for every method-developer PI in masterlist/queue/pi_watchlist.yaml, find them on OpenAlex
#  Europe PMC (surname + initials, plus institution when only one initial), pull their papers, and keep those whose abstract introduces a method-like name that is
#  not in the masterlist yet. Output feeds Proc_step2 (classification in Claude Code), same record shape as step1.
#Usage: python3 pipeline/pi_sweep.py --since 2010-01-01 --out masterlist/queue/pi_sweep.jsonl
#       python3 pipeline/pi_sweep.py --since 2026-10-20 --out ...   (weekly top-up: only recent papers)
#INPUT: masterlist/queue/pi_watchlist.yaml (name + institution hint); Europe PMC REST API.
#OUTPUT: <out> candidates JSONL + <out>.resolution.tsv (query + paper count per PI - CHECK the GUESS rows)

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

from common import METHODS_DIR, ROOT, epmc_search
from fetch import _journal
from triage import triage



def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower().replace("&", "and"))


def query(pi):
    """Europe PMC author query. Full initials (Weissman JS) are specific enough on their own; a bare first initial
    (Cui A, Tay S) is narrowed by the institution hint. Returns (query, status): status GUESS = eyeball these papers."""
    toks = pi["name"].replace(".", "").split()
    last, first = toks[-1], toks[:-1]
    ini = "".join(t[0] for t in first if t[0].isalpha()).upper()
    if len(first) > 1:
        q = f'AUTH:"{last} {ini}"'
    else:
        at = pi.get("at") or []
        at = [at] if isinstance(at, str) else at  # PIs who moved: several institutions, OR'd
        q = f'AUTH:"{last} {ini}"' + (" AND (" + " OR ".join(f'AFF:"{x}"' for x in at if x) + ")" if any(at) else "")
    return q, ("GUESS" if pi.get("unsure") or (len(first) == 1 and not pi.get("at")) else "ok")


def works(q, since):
    out, cur = [], "*"
    while True:
        j = epmc_search(f"{q} AND FIRST_PDATE:[{since} TO 3000-01-01]", page_size=200, cursor=cur, core=True)
        hs = j.get("resultList", {}).get("result", [])
        out += [_journal(h) for h in hs if h.get("abstractText")]
        if not hs or j.get("nextCursorMark") in (None, cur):
            return out
        cur = j["nextCursorMark"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2010-01-01"); ap.add_argument("--out", required=True)
    ap.add_argument("--only", nargs="*", help="sweep just these PI names (e.g. after adding hints); output is merged into --out")
    a = ap.parse_args()
    pis = yaml.safe_load((ROOT / "masterlist/queue/pi_watchlist.yaml").read_text())
    if a.only:
        pis = [p for p in pis if p["name"] in a.only]
    known, dois = set(), set()
    for p in METHODS_DIR.glob("*.yaml"):
        e = yaml.safe_load(p.read_text())
        known |= {norm(x) for x in [e["name"]] + (e.get("aliases") or [])}
        dois.add(((e.get("reference") or {}).get("doi") or "").lower())
    recs, report = {}, []
    for pi in pis:
        q, status = query(pi)
        if len(pi["name"].replace(".", "").split()) == 2 and not any([pi.get("at")] if isinstance(pi.get("at"), str) else pi.get("at") or []):  # "Zhou J" alone = tens of thousands of namesakes
            report.append([pi["name"], "NEEDS-HINT", q, "single initial and no institution - add `at:` to pi_watchlist.yaml", ""])
            print(f"SKIP     {pi['name']}: needs an institution hint", flush=True); continue
        try:
            ws = works(q, a.since)
        except Exception as e:
            report.append([pi["name"], "ERROR", q, str(e), ""]); print(f"ERROR    {pi['name']}: {e}", flush=True); continue
        for w in ws:
            recs.setdefault(w["id"], w | {"pis": []})["pis"].append(pi["name"])
        report.append([pi["name"], status, q, "", str(len(ws))])
        print(f"{status:8} {pi['name'][:28]:28} {q[:60]:60} {len(ws)} papers", flush=True)
    kept = []
    for r in recs.values():
        if (r["doi"] or "").lower() in dois or not r["abstract"]:
            continue
        t = triage(r, fetch_fulltext=False)
        names = [n for n in t["names"] if norm(n) not in known]
        if t["flag"] and names:
            kept.append(r | {"triage": t | {"names": names}})
    out = Path(a.out)
    if a.only and out.exists():  # merge into the existing sweep, no duplicates
        old = [json.loads(l) for l in out.read_text().splitlines()]
        have = {r["id"] for r in old}
        kept = old + [r for r in kept if r["id"] not in have]
    out.write_text("".join(json.dumps(r) + "\n" for r in kept))
    Path(str(out) + ".resolution.tsv").write_text("pi\tstatus\tquery\terror\tpapers\n" + "".join("\t".join(r) + "\n" for r in report))
    print(f"{len(recs):,} papers from {len(pis)} PIs -> {len(kept)} name a method not in the masterlist -> {out}")
    flagged = [r for r in report if r[1] != "ok"]
    if flagged:
        print(f"CHECK {len(flagged)} PI resolutions marked GUESS/NO-MATCH/ERROR in {out}.resolution.tsv", file=sys.stderr)


if __name__ == "__main__":
    main()

# ---- Provenance ----
# Upstream:   masterlist/queue/pi_watchlist.yaml (user's PI lists, 2026-10-27); pipeline/common.py; pipeline/triage.py
# Downstream: Proc_step2 classification in Claude Code (pipeline/CLASSIFIER_INSTRUCTIONS.md) -> masterlist/methods/*.yaml
# References: Europe PMC REST API. OpenAlex was tried first but now needs an API key (401 without one, 2026-10-27)
# Notes:      abstract-only triage (no full text) - methods named only in Results are caught later by the weekly/backfill scans
