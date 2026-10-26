#Date: 2026-10-26
#Purpose: Score the triage step (and later the classifier) against benchmark/benchmark.yaml: did each paper get
#  flagged, by which route, and were the expected method names extracted?
#Usage: python pipeline/benchmark.py
#INPUT: benchmark/benchmark.yaml (DOIs + expected outcomes); fetches each paper live from bioRxiv / Europe PMC

import yaml

from common import ROOT
from fetch import get_record
from triage import triage

cases = yaml.safe_load((ROOT / "benchmark" / "benchmark.yaml").read_text())
passed = 0
for c in cases:
    rec = get_record(c["doi"])
    if not rec:
        print(f"FAIL  {c['doi']}: record not found")
        continue
    t = triage(rec)
    want_flag, want_names = c["expect"]["triage"], [m.lower() for m in c["expect"]["methods"]]
    got_names = [n.lower() for n in t["names"]]
    missing = [m for m in want_names if not any(m == g or m in g.split(" (") for g in got_names)]
    ok = (want_flag is None or t["flag"] == want_flag) and not missing
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  {c['note'][:70]}\n      routes={t['routes']} names={t['names']}"
          + (f"  MISSING={missing}" if missing else ""))
print(f"\n{passed}/{len(cases)} benchmark cases pass triage")
