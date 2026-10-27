#Date: 2026-10-27
#Purpose: Poll curated external method lists ("watchlists") that their maintainers keep updating, and turn every row not
#  seen before into a pipeline record marked watchlist=<list id>. Like website submissions, watchlist rows skip triage's
#  discard rules (a human already picked them), but they get the normal single classifier pass: these lists also carry
#  imaging-only, mass-spec, commercial-instrument and computational rows that the classifier should reject or route to dry.
#Usage: python pipeline/watchlists.py [--seen <seen.json>] > data/watchlist.jsonl
#  Or import: fetch_watchlists(seen_path) -> list of records (same shape as fetch.py, plus watchlist/watchlist_name/watchlist_url)
#INPUT: published CSV export of each list in WATCHLISTS (public, no login).
#  Rows already handled are remembered in <seen file> (default: next to step1 output) so none are processed twice.

import argparse
import csv
import io
import json
import os
import re
import sys

from common import epmc_search, get
from fetch import _journal, get_record

# id -> CSV export URL + which columns hold the method name / reference link / free-text type
WATCHLISTS = {
    "vilella-scellmarket": {
        "title": "#SingleCell #Omics market sheet (Albert Vilella, bit.ly/scellmarket)",
        "csv": "https://docs.google.com/spreadsheets/d/1IPe2ozb1Mny8sLvJaSE57RJr3oruiBoSudAVhSH-O8M/export?format=csv&gid=11468010",
        "name": "Method", "ref": "Reference", "type": "Type", "year": "Late Estimate",
    },
}
DOI = re.compile(r"10\.\d{4,9}/[^\s?#&]+", re.I)
PMID = re.compile(r"(?:pubmed/|pubmed\.ncbi\.nlm\.nih\.gov/|pmid=)(\d{6,9})", re.I)
PMCID = re.compile(r"\b(PMC\d{5,9})\b")
NATURE = re.compile(r"nature\.com/articles/([a-z0-9.\-]+)", re.I)  # article slug = DOI suffix under 10.1038


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower().replace("&", "and"))


def _rows(lst):
    """[(key, name, ref, type, year)] for one watchlist; key = list id + normalised name + reference (stable across re-sorts)."""
    c = WATCHLISTS[lst]
    out = []
    for r in csv.DictReader(io.StringIO(get(c["csv"], as_json=False))):
        name, ref = (r.get(c["name"]) or "").strip(), (r.get(c["ref"]) or "").strip()
        if name:
            out.append((f"{lst}|{_norm(name)}|{ref}", name, ref, (r.get(c["type"]) or "").strip(), (r.get(c["year"]) or "").strip()))
    return out


def resolve(ref):
    """Reference link -> pipeline record, or None. Tries DOI (incl. bioRxiv URLs), then PubMed ID, then PMC ID."""
    ref = ref.replace("%2F", "/").replace("%2f", "/")
    m = DOI.search(ref) or NATURE.search(ref)
    if m:
        doi = m.group(0) if m.re is DOI else f"10.1038/{m.group(1)}"
        doi = re.sub(r"(v\d+)?(\.full|\.abstract|\.pdf|\.epdf)?/?$", "", doi.rstrip(".)"))
        rec = get_record(doi)
        if rec:
            return rec
    for pat, field in ((PMID, "SRC:MED AND EXT_ID"), (PMCID, "PMCID")):
        m = pat.search(ref)
        if m:
            hits = epmc_search(f"{field}:{m.group(1)}", page_size=5, core=True).get("resultList", {}).get("result", [])
            if hits:
                return _journal(hits[0])
    return None


def fetch_watchlists(seen_path=None, lists=tuple(WATCHLISTS)):
    """New (not yet seen) rows of every watchlist -> pipeline records. Rows whose link is not a paper (vendor pages, review
    articles shared by many rows) become name-only stubs, so the classifier still sees them and can look them up."""
    seen = set(json.loads(open(seen_path).read())) if seen_path and os.path.exists(seen_path) else set()
    out, problems, rows = [], [], []
    for lst in lists:
        try:
            rows += [(lst,) + r for r in _rows(lst)]
        except Exception as e:
            problems.append(f"{lst}: could not read ({type(e).__name__}: {e})")
    for lst, key, name, ref, typ, year in (r for r in rows if r[1] not in seen):
        try:
            rec = resolve(ref)
        except Exception as e:
            rec = None
            problems.append(f"{key}: lookup failed ({type(e).__name__}: {e})")
        if not rec:  # stub: no paper behind the link (or lookup failed) - keep the row, flag it
            rec = {"id": f"{lst}:{_norm(name)}", "doi": None, "source": "watchlist", "title": name, "abstract": "",
                   "date": year, "category": typ, "jatsxml": None, "pmcid": None, "unresolved": True}
        out.append(rec | {"watchlist": lst, "watchlist_name": name, "watchlist_url": ref, "watchlist_type": typ})
    if seen_path:  # remember every row looked at, including stubs (they are reported, not silently retried forever)
        with open(seen_path, "w") as fh:
            json.dump(sorted(seen | {r[1] for r in rows}), fh)
    for p in problems:
        print(f"watchlist problem: {p}", file=sys.stderr)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seen", help="seen-rows JSON (omit to list every row)")
    a = ap.parse_args()
    recs = fetch_watchlists(a.seen)
    for r in recs:
        print(json.dumps(r))
    print(f"{len(recs)} watchlist records ({sum(bool(r.get('unresolved')) for r in recs)} name-only stubs)", file=sys.stderr)

# ---- Provenance ----
# Upstream:   pipeline/common.py (get, epmc_search), pipeline/fetch.py (get_record, _journal); the Google Sheets in WATCHLISTS
# Downstream: pipeline/step1.py (--week collects watchlists alongside preprints/journals/submissions) -> Proc_step2 classifier
# References: Albert Vilella's single-cell omics market sheet (bit.ly/scellmarket); bioRxiv API; Europe PMC REST API
# Notes:      seen-file pattern copied from submissions.py; watchlist rows bypass triage discard but get ONE classifier pass
#             (submissions get three). Initial backlog seeded 2026-10-27 into masterlist/queue/vilella_scellmarket.jsonl.
