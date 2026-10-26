#Date: 2026-10-26
#Purpose: Fill in missing citation fields (doi, year, journal, first/last author, pmid, pmcid) for masterlist entries
#  by looking up their DOI or reference title on Europe PMC. Never overwrites a field that is already set.
#Usage: python pipeline/resolve_refs.py            # resolve every entry with missing fields
#       python pipeline/resolve_refs.py rcmc       # just masterlist/methods/rcmc.yaml
#INPUT: masterlist/methods/*.yaml with at least reference.doi or reference.title

import re
import sys

import yaml

from common import METHODS_DIR, epmc_lookup

FIELDS = ("doi", "year", "journal", "first_author", "last_author", "pmid", "pmcid", "title")


def resolve(path):
    entry = yaml.safe_load(path.read_text())
    ref = entry.setdefault("reference", {})
    if all(ref.get(f) for f in ("doi", "year", "journal", "first_author")):
        return "ok (already complete)"
    hit = epmc_lookup(doi=ref.get("doi"), title=None if ref.get("doi") else ref.get("title"))
    if not hit:
        return "NOT FOUND - check reference.title / reference.doi by hand"
    norm = lambda t: re.sub(r"[^a-z0-9]", "", re.sub(r"<[^>]+>", "", t or "").lower())
    if not ref.get("doi") and norm(hit.get("title")) != norm(ref.get("title")):
        return f"TITLE MISMATCH, nothing written - Europe PMC's best hit was '{hit.get('title')}' ({hit.get('pubYear')}); set reference.doi by hand"
    authors = [a.strip().rstrip(".") for a in hit.get("authorString", "").split(",") if a.strip()]
    found = {"doi": hit.get("doi"), "year": int(hit["pubYear"]) if hit.get("pubYear") else None,
             "journal": hit.get("journalTitle") or hit.get("bookOrReportDetails", {}).get("publisher") or
                        ("bioRxiv" if hit.get("source") == "PPR" else None),
             "first_author": authors[0] if authors else None, "last_author": authors[-1] if authors else None,
             "pmid": hit.get("pmid"), "pmcid": hit.get("pmcid"), "title": hit.get("title", "").rstrip(".")}
    for k in FIELDS:
        if not ref.get(k) and found.get(k):
            ref[k] = found[k]
    entry["reference"] = {k: ref[k] for k in FIELDS if ref.get(k)} | {k: v for k, v in ref.items() if k not in FIELDS}
    path.write_text(yaml.safe_dump(entry, sort_keys=False, allow_unicode=True, width=120))
    return f"{ref.get('first_author')} {ref.get('year')} {ref.get('journal')} doi:{ref.get('doi')}"


if __name__ == "__main__":
    targets = [METHODS_DIR / f"{s}.yaml" for s in sys.argv[1:]] or sorted(METHODS_DIR.glob("*.yaml"))
    for p in targets:
        print(f"{p.stem:<22} {resolve(p)}")
