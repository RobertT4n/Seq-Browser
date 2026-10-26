#Date: 2026-10-26
#Purpose: Collect website submissions - rows of the Google Sheet behind the Submit page (main route) plus any open GitHub
#  "submission" issues (backup route) - and turn each DOI into
#  a pipeline record marked submitted=True. Submitted records skip triage's discard rules and get a 3-pass check in the
#  classifier: they are only dropped if three independent passes all say "not a new sequencing method".
#Usage: python pipeline/submissions.py > data/submissions.jsonl
#  Or import: fetch_submissions() -> list of records (same shape as fetch.py, plus submitted/issue/submitter_notes)
#INPUT: published CSV of the submissions Google Sheet; open GitHub issues labelled "submission" (public API).
#  Rows already handled are remembered in <seen file> (default: next to step1 output) so none are processed twice.

import csv
import io
import json
import os
import re
import sys
import urllib.request

from common import get
from fetch import get_record

REPO = "RobertT4n/Seq-Browser"
DOI = re.compile(r"\b(10\.\d{4,9}/[^\s,;\"<>]+)", re.I)
VERIFY_PASSES = 3  # classifier passes required before a submission may be discarded
SHEET_CSV = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vRfsALodhvGCzpDrwHc7J-_I1CVmNATmKwtkXFh-AXbk3Q9s5L8lQkb4zmEFqYnMpUPmMgNFp4L1VI-"
             "/pub?output=csv")


def _issues():
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "Seq-Browser"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    url = f"https://api.github.com/repos/{REPO}/issues?labels=submission&state=open&per_page=100"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
        return json.load(r)


def _field(body, label):
    """Value under '### <label>' in an issue-form body."""
    m = re.search(rf"### {re.escape(label)}\s*\n+(.*?)(?=\n### |\Z)", body or "", re.S)
    v = m.group(1).strip() if m else ""
    return "" if v == "_No response_" else v


def _sheet_rows():
    """[(key, name, dois_text, notes)] from the Google Sheet behind the website form."""
    rows = list(csv.DictReader(io.StringIO(get(SHEET_CSV, as_json=False))))
    col = lambda r, start: next((v for k, v in r.items() if k and k.lower().startswith(start)), "") or ""
    return [(f"sheet|{r.get('Timestamp', '')}|{col(r, 'doi')}", col(r, "method name"), col(r, "doi"),
             "\n".join(filter(None, (f"Type: {col(r, 'type')}" if col(r, "type") else "", f"Measures: {col(r, 'what does it measure')}",
                                      f"Resolution: {col(r, 'resolution')}", f"Parents: {col(r, 'related')}", col(r, "notes")))))
            for r in rows]


def _issue_rows():
    return [(f"issue|{i['number']}", _field(i.get("body"), "Method name"), _field(i.get("body"), "DOI(s)") or i.get("body") or "",
             "\n".join(filter(None, (_field(i.get("body"), "Related / parent methods"), _field(i.get("body"), "Notes (optional)")))))
            for i in _issues()]


def fetch_submissions(seen_path=None):
    """New (not yet seen) submissions from the sheet and GitHub issues -> pipeline records marked submitted=True."""
    seen = set(json.loads(open(seen_path).read())) if seen_path and os.path.exists(seen_path) else set()
    out, problems, rows = [], [], []
    for label, fn in (("sheet", _sheet_rows), ("github issues", _issue_rows)):
        try:
            rows += fn()
        except Exception as e:
            problems.append(f"{label}: could not read ({type(e).__name__}: {e})")
    new = [r for r in rows if r[0] not in seen]
    for key, name, doi_text, notes in new:
        dois = [d.rstrip(".)") for d in DOI.findall(doi_text)]
        if not dois:
            problems.append(f"{key} ({name}): no DOI found in '{doi_text[:80]}'")
            continue
        for doi in dois:
            rec = get_record(doi)
            if rec:
                out.append(rec | {"submitted": True, "verify_passes": VERIFY_PASSES, "submission": key,
                                  "submitted_name": name, "submitter_notes": notes})
            else:
                problems.append(f"{key} ({name}): DOI {doi} not found on bioRxiv / Europe PMC")
    if seen_path:  # remember every row looked at, including problem rows (they are reported, not silently retried forever)
        with open(seen_path, "w") as fh:
            json.dump(sorted(seen | {r[0] for r in rows}), fh)
    for p in problems:
        print(f"submission problem: {p}", file=sys.stderr)
    return out


if __name__ == "__main__":
    recs = fetch_submissions()
    for r in recs:
        print(json.dumps(r))
    print(f"{len(recs)} submitted records", file=sys.stderr)
