#Date: 2026-10-26
#Purpose: Shared helpers for the Seq-Browser pipeline: paths, slugs, polite HTTP, Europe PMC + bioRxiv API calls.
#Usage: imported by the other pipeline/*.py scripts; not run directly.

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METHODS_DIR = ROOT / "masterlist" / "methods"
TAXONOMY = ROOT / "taxonomy.yaml"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
BIORXIV = "https://api.biorxiv.org"
UA = {"User-Agent": "Seq-Browser/0.1 (https://github.com/RobertT4n/Seq-Browser)"}


def slug(name):
    """'CUT&Tag' -> 'cut-and-tag', 'in situ Hi-C' -> 'in-situ-hi-c'."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower().replace("&", "-and-").replace("+", "-plus")).strip("-")


def get(url, as_json=True, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                body = r.read().decode("utf-8", "replace")
            return json.loads(body) if as_json else body
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(5 * (i + 1))


def epmc_search(query, page_size=25, cursor="*", core=False):
    params = {"query": query, "format": "json", "pageSize": page_size, "cursorMark": cursor,
              "resultType": "core" if core else "lite"}
    return get(f"{EPMC}/search?{urllib.parse.urlencode(params)}")


def epmc_lookup(doi=None, title=None):
    """Best Europe PMC record for a DOI or exact-ish title, or None."""
    q = f'DOI:"{doi}"' if doi else f'TITLE:"{title}"'
    hits = epmc_search(q, page_size=5).get("resultList", {}).get("result", [])
    if not hits:
        return None
    notice = ("author correction", "publisher correction", "correction", "erratum", "retraction")
    hits = [h for h in hits if not h.get("title", "").lower().startswith(notice)] or hits
    if title:  # prefer the journal version over its preprint when both exist
        hits.sort(key=lambda h: h.get("source") == "PPR")
    return hits[0]


def epmc_fulltext(pmcid):
    """JATS XML full text for an open-access PMC article, or None. Europe PMC first; NCBI PMC as fallback
    (Europe PMC's fullTextXML intermittently 500s on articles that are open access)."""
    for url in (f"{EPMC}/{pmcid}/fullTextXML",
                f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid.removeprefix('PMC')}&rettype=xml"):
        try:
            xml = get(url, as_json=False, tries=2)
            if "<body" in xml:
                return xml
        except Exception:
            pass
    return None


def jats_to_text(xml):
    """Crude JATS -> plain text: drop references, strip tags, collapse whitespace."""
    xml = re.sub(r"<ref-list.*?</ref-list>", " ", xml, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", xml))
