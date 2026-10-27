#Date: 2026-10-26
#Purpose: Shared helpers for the Seq-Browser pipeline: paths, slugs, polite HTTP, Europe PMC + bioRxiv API calls.
#Usage: imported by the other pipeline/*.py scripts; not run directly.

import json
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METHODS_DIR = ROOT / "masterlist" / "methods"
TAXONOMY = ROOT / "taxonomy.yaml"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
BIORXIV = "https://api.biorxiv.org"
UA = {"User-Agent": "Seq-Browser/0.1 (https://github.com/RobertT4n/Seq-Browser)"}
# Minimum seconds between requests to one host, shared by every thread of this process. bioRxiv's full-text server 429s
# hard when several threads (or several array tasks on one cluster IP) hit it at once - backfill 22440566 lost 78% of
# full texts that way. NCBI allows 3 req/s without an API key.
MIN_GAP = {"www.biorxiv.org": 1.0, "api.biorxiv.org": 0.5, "eutils.ncbi.nlm.nih.gov": 0.35, "www.ebi.ac.uk": 0.1, "api.openalex.org": 0.12, "api.crossref.org": 0.1}
_NEXT, _LOCK = {}, threading.Lock()


def _wait_turn(url):
    host = urllib.parse.urlsplit(url).hostname
    gap = MIN_GAP.get(host, 0)
    if not gap:
        return
    with _LOCK:
        now = time.time(); slot = max(now, _NEXT.get(host, 0)); _NEXT[host] = slot + gap
    time.sleep(slot - now)


def slug(name):
    """'CUT&Tag' -> 'cut-and-tag', 'in situ Hi-C' -> 'in-situ-hi-c'."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower().replace("&", "-and-").replace("+", "-plus")).strip("-")


def get(url, as_json=True, tries=3):
    tries_429 = 6  # rate limits clear given time: retry those longer than other errors
    i = 0
    while True:
        _wait_turn(url)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                body = r.read().decode("utf-8", "replace")
            return json.loads(body) if as_json else body
        except urllib.error.HTTPError as e:
            i += 1
            if e.code == 404 or i >= (tries_429 if e.code == 429 else tries):
                raise
            if e.code == 429:  # back off hard, honour Retry-After, and slow every thread on this host down
                wait = max(30 * i, int(e.headers.get("Retry-After") or 0))
                with _LOCK:
                    _NEXT[urllib.parse.urlsplit(url).hostname] = time.time() + wait
            time.sleep(30 * i if e.code == 429 else 5 * i)
        except Exception:
            i += 1
            if i >= tries:
                raise
            time.sleep(5 * i)


FT_STATS = {"fulltext_ok": 0, "not_open_access": 0, "fulltext_failed": 0, "gated_out": 0}  # reported in every step1 summary


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
    failed = False
    for url in (f"{EPMC}/{pmcid}/fullTextXML",
                f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid.removeprefix('PMC')}&rettype=xml"):
        try:
            xml = get(url, as_json=False, tries=3)
            if "<body" in xml:
                return xml
        except urllib.error.HTTPError as e:
            failed |= e.code != 404
        except Exception:
            failed = True
    if failed:
        raise RuntimeError(f"full text for {pmcid} could not be downloaded")
    return None


def jats_to_text(xml):
    """Crude JATS -> plain text: drop references, strip tags, collapse whitespace."""
    xml = re.sub(r"<ref-list.*?</ref-list>", " ", xml, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", xml))
