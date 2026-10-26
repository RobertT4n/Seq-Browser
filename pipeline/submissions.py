#Date: 2026-10-26
#Purpose: Collect open "submission" issues (filed via the website's Submit page / GitHub issue form) and turn each DOI into
#  a pipeline record marked submitted=True. Submitted records skip triage's discard rules and get a 3-pass check in the
#  classifier: they are only dropped if three independent passes all say "not a new sequencing method".
#Usage: python pipeline/submissions.py > data/submissions.jsonl
#  Or import: fetch_submissions() -> list of records (same shape as fetch.py, plus submitted/issue/submitter_notes)
#INPUT: open GitHub issues labelled "submission" on RobertT4n/Seq-Browser (public API; set GITHUB_TOKEN for higher limits)

import json
import os
import re
import sys
import urllib.request

from fetch import get_record

REPO = "RobertT4n/Seq-Browser"
DOI = re.compile(r"\b(10\.\d{4,9}/[^\s,;\"<>]+)", re.I)
VERIFY_PASSES = 3  # classifier passes required before a submission may be discarded


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


def fetch_submissions():
    out, problems = [], []
    for iss in _issues():
        body = iss.get("body") or ""
        dois = [d.rstrip(".)") for d in DOI.findall(_field(body, "DOI(s)") or body)]
        if not dois:
            problems.append(f"#{iss['number']}: no DOI found")
            continue
        for doi in dois:
            rec = get_record(doi)
            if not rec:
                problems.append(f"#{iss['number']}: DOI {doi} not found on bioRxiv / Europe PMC")
                continue
            out.append(rec | {"submitted": True, "verify_passes": VERIFY_PASSES, "issue": iss["number"],
                              "submitted_name": _field(body, "Method name"),
                              "submitter_notes": "\n".join(filter(None, (_field(body, "Related / parent methods"),
                                                                          _field(body, "Notes (optional)"))))})
    for p in problems:
        print(f"submission problem: {p}", file=sys.stderr)
    return out


if __name__ == "__main__":
    recs = fetch_submissions()
    for r in recs:
        print(json.dumps(r))
    print(f"{len(recs)} submitted records", file=sys.stderr)
