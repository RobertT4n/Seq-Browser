#Date: 2026-10-26
#Purpose: Pull new papers (title, abstract, full text when open access) from bioRxiv/medRxiv and Europe PMC (PubMed
#  journals) for a date range, as a uniform record list for triage.py.
#Usage: python pipeline/fetch.py 2026-10-12 2026-10-18 > data/raw_2026-10-12.jsonl   # one JSON record per line
#  Or import: fetch_preprints(start, end), fetch_journals(start, end), get_record(doi)
#INPUT: none (public APIs). Full text is NOT fetched here (slow); triage.py fetches it lazily for candidates only.

import json
import sys

from common import cache_get, cache_put, BIORXIV, FT_STATS, epmc_search, get, jats_to_text, epmc_fulltext

# Europe PMC query restricting PubMed-indexed journal papers to plausibly relevant ones (high recall, cheap)
JOURNAL_FILTER = ('(ABSTRACT:"sequencing" OR ABSTRACT:"seq" OR ABSTRACT:"single-cell" OR ABSTRACT:"single cell" '
                  'OR ABSTRACT:"chromatin" OR ABSTRACT:"transcriptom*" OR ABSTRACT:"epigenom*" OR ABSTRACT:"profiling")')


def _preprint(r, server):
    return {"id": r["doi"], "doi": r["doi"], "source": server, "title": r["title"], "abstract": r["abstract"],
            "date": r["date"], "category": r.get("category"), "jatsxml": r.get("jatsxml"), "pmcid": None,
            "published": None if r.get("published") in (None, "", "NA") else r["published"]}  # journal DOI once published


def fetch_preprints(start, end, servers=("biorxiv", "medrxiv")):
    """First versions only (later versions of the same preprint are not new methods)."""
    out = []
    for server in servers:
        cursor = 0
        while True:
            j = get(f"{BIORXIV}/details/{server}/{start}/{end}/{cursor}")
            batch = j.get("collection") or []
            out += [_preprint(r, server) for r in batch if str(r.get("version")) == "1"]
            cursor += len(batch)
            if not batch or cursor >= int(j["messages"][0].get("total", 0)):
                break
    return out


def _journal(h):
    return {"id": h.get("doi") or f"PMID:{h.get('pmid')}", "doi": h.get("doi"), "source": "journal",
            "title": h.get("title", ""), "abstract": h.get("abstractText", ""), "date": h.get("firstPublicationDate"),
            "category": h.get("journalInfo", {}).get("journal", {}).get("medlineAbbreviation"),
            "jatsxml": None, "pmcid": h.get("pmcid")}


def fetch_journals(start, end):
    q, cursor, out = f"FIRST_PDATE:[{start} TO {end}] AND SRC:MED AND HAS_ABSTRACT:y AND {JOURNAL_FILTER}", "*", []
    while True:
        j = epmc_search(q, page_size=1000, cursor=cursor, core=True)
        out += [_journal(h) for h in j.get("resultList", {}).get("result", [])]
        nxt = j.get("nextCursorMark")
        if not nxt or nxt == cursor:
            return out
        cursor = nxt


def get_record(doi):
    """One paper by DOI (used by the benchmark). bioRxiv first, then Europe PMC."""
    if doi.startswith(("10.1101/", "10.64898/")):
        for server in ("biorxiv", "medrxiv"):
            c = get(f"{BIORXIV}/details/{server}/{doi}").get("collection") or []
            if c:
                return _preprint(c[0], server)
    hits = epmc_search(f'DOI:"{doi}"', page_size=5, core=True).get("resultList", {}).get("result", [])
    hits = [h for h in hits if h.get("source") == "MED"] or hits
    return _journal(hits[0]) if hits else None


def full_text(rec, defer=None):
    """Plain full text if open access, else None. Every attempt is tallied in common.FT_STATS.
    Cached on disk per DOI (common.FT_CACHE). defer: a list -> a throttled bioRxiv download is not retried inline but the
    record is appended to `defer` (tallied as deferred, not failed) for pipeline/drain_fulltext.py to fetch later."""
    key = rec.get("doi") or rec.get("id")
    xml = cache_get(key)
    if xml:
        FT_STATS["cache_hit"] += 1
        return jats_to_text(xml)
    try:
        if rec.get("jatsxml"):
            xml = get(rec["jatsxml"], as_json=False, **({"tries": 1, "tries_429": 1} if defer is not None else {}))
        elif rec.get("pmcid"):
            xml = epmc_fulltext(rec["pmcid"])
        else:
            xml = None
    except Exception:
        if defer is not None and rec.get("jatsxml"):
            FT_STATS["deferred"] += 1
            defer.append(rec)
        else:
            FT_STATS["fulltext_failed"] += 1
        return None
    FT_STATS["fulltext_ok" if xml else "not_open_access"] += 1
    cache_put(key, xml)
    return jats_to_text(xml) if xml else None


if __name__ == "__main__":
    start, end = sys.argv[1:3]
    recs = fetch_preprints(start, end) + fetch_journals(start, end)
    for r in recs:
        print(json.dumps(r))
    print(f"{len(recs)} records", file=sys.stderr)
