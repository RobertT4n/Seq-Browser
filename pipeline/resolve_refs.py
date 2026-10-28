#Date: 2026-10-26
#Purpose: Fill in missing citation fields (doi, year, journal, first/last author, pmid, pmcid) for masterlist entries
#  by looking up their DOI or reference title on Europe PMC. Never overwrites a field that is already set.
#Usage: python pipeline/resolve_refs.py            # resolve every entry with missing fields
#       python pipeline/resolve_refs.py rcmc       # just masterlist/methods/rcmc.yaml
#INPUT: masterlist/methods/*.yaml with at least reference.doi or reference.title

import re
import sys

import yaml

from common import BIORXIV, METHODS_DIR, epmc_lookup, get

FIELDS = ("doi", "year", "journal", "first_author", "last_author", "pmid", "pmcid", "title")  # preprint_doi etc. are kept as-is


def biorxiv_lookup(doi):
    """bioRxiv/medRxiv record shaped like a Europe PMC hit (title, authors, year, journal)."""
    for server in ("biorxiv", "medrxiv"):
        c = get(f"{BIORXIV}/details/{server}/{doi}").get("collection") or []
        if c:
            r = c[0]
            return {"doi": doi, "title": r["title"], "pubYear": r["date"][:4], "source": "PPR",
                    "journalTitle": "bioRxiv" if server == "biorxiv" else "medRxiv",
                    "authorString": ", ".join(a.strip() for a in r["authors"].split(";") if a.strip())}
    return None


def resolve(path, check_published=True):
    """Fill in a reference from Europe PMC. A preprint DOI is upgraded to its journal version FIRST (check_published):
    every new entry runs through here, so a method published since the preprint can never be filed as a preprint.
    (Origin: SAMPL-seq was written with its bioRxiv DOI although it was already in Nat Microbiol.)"""
    entry = yaml.safe_load(path.read_text())
    ref = entry.setdefault("reference", {})
    if check_published and (ref.get("doi") or "").startswith(("10.1101/", "10.64898/")) and not ref.get("preprint_doi"):
        from update_published import published_doi  # imported here: update_published imports this module
        pub = published_doi(ref["doi"])
        if pub:
            entry["reference"] = ref = {"doi": pub, "preprint_doi": ref["doi"]}  # re-resolve everything from the journal version
            path.write_text(yaml.safe_dump(entry, sort_keys=False, allow_unicode=True, width=120))
    if all(ref.get(f) for f in ("doi", "year", "journal", "first_author")):
        return "ok (already complete)"
    if ref.get("url") and not ref.get("doi") and not ref.get("title"):
        return "url-only reference (kit with no paper) - nothing to resolve"
    hit = epmc_lookup(doi=ref.get("doi"), title=None if ref.get("doi") else ref.get("title"))
    if not hit and (ref.get("doi") or "").startswith(("10.1101/", "10.64898/")):
        hit = biorxiv_lookup(ref["doi"])  # brand-new preprints reach Europe PMC days-weeks after bioRxiv
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
