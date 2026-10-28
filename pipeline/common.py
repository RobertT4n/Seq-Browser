#Date: 2026-10-26
#Purpose: Shared helpers for the Seq-Browser pipeline: paths, slugs, polite HTTP, Europe PMC + bioRxiv API calls.
#Usage: imported by the other pipeline/*.py scripts; not run directly.

import gzip
import hashlib
import json
import os
import random
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
# Per-host request pacing, shared by every thread of this process, AIMD-style (as in TCP congestion control): the gap
# between requests starts at MIN_GAP, doubles on every HTTP 429 (up to MAX_GAP) and shrinks 10% after each success, with
# +-20% jitter so threads do not fire in lockstep. Retry-After is honoured. bioRxiv's full-text server throttles the cluster
# IP hard (backfill 22440566 lost 78% of full texts at fixed 1 req/s; 22475737 lost 32%); with --defer those requests are
# not retried inline but queued for pipeline/drain_fulltext.py. NCBI allows 3 req/s without an API key.
MAX_GAP = 120.0
MIN_GAP = {"www.biorxiv.org": 3.0, "api.biorxiv.org": 0.5, "eutils.ncbi.nlm.nih.gov": 0.35, "www.ebi.ac.uk": 0.1, "api.openalex.org": 0.12, "api.crossref.org": 0.1}
_NEXT, _GAP, _LOCK = {}, {}, threading.Lock()


def _wait_turn(url):
    host = urllib.parse.urlsplit(url).hostname
    if host not in MIN_GAP:
        return
    with _LOCK:
        gap = _GAP.setdefault(host, MIN_GAP[host]) * random.uniform(.8, 1.2)
        now = time.time(); slot = max(now, _NEXT.get(host, 0)); _NEXT[host] = slot + gap
    time.sleep(slot - now)


def _paced(url, ok, retry_after=0):
    """AIMD update after a response: success -> gap * 0.9 (not below MIN_GAP); 429 -> gap * 2 (not above MAX_GAP)."""
    host = urllib.parse.urlsplit(url).hostname
    if host not in MIN_GAP:
        return
    with _LOCK:
        g = _GAP.get(host, MIN_GAP[host])
        _GAP[host] = max(MIN_GAP[host], g * .9) if ok else min(MAX_GAP, g * 2)
        if not ok:
            _NEXT[host] = max(_NEXT.get(host, 0), time.time() + max(_GAP[host], retry_after))


def slug(name):
    """'CUT&Tag' -> 'cut-and-tag', 'in situ Hi-C' -> 'in-situ-hi-c'."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower().replace("&", "-and-").replace("+", "-plus")).strip("-")


def get(url, as_json=True, tries=3, tries_429=6):
    """GET with pacing. tries_429=1 makes a throttled request fail fast (callers that defer it to a queue)."""
    i = 0
    while True:
        _wait_turn(url)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                body = r.read().decode("utf-8", "replace")
            _paced(url, True)
            return json.loads(body) if as_json else body
        except urllib.error.HTTPError as e:
            i += 1
            if e.code == 429:  # slow every thread on this host down (AIMD), honouring Retry-After
                ra = e.headers.get("Retry-After") or "0"
                _paced(url, False, int(ra) if ra.isdigit() else 0)
            if e.code == 404 or i >= (tries_429 if e.code == 429 else tries):
                raise
            if e.code != 429:
                time.sleep(5 * i)
        except Exception:
            i += 1
            if i >= tries:
                raise
            time.sleep(5 * i)


FT_STATS = {"fulltext_ok": 0, "not_open_access": 0, "fulltext_failed": 0, "gated_out": 0, "skipped_published": 0,
            "deferred": 0, "cache_hit": 0}  # reported in every step1 summary


# Full-text cache: one gzipped XML per DOI, so retries and reruns never download a paper twice.
FT_CACHE = os.environ.get("SEQBROWSER_FT_CACHE")


def _cache_path(key):
    return os.path.join(FT_CACHE, hashlib.sha1(key.encode()).hexdigest()[:20] + ".xml.gz") if FT_CACHE and key else None


def cache_get(key):
    p = _cache_path(key)
    if p and os.path.exists(p):
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            return fh.read()
    return None


def cache_put(key, xml):
    p = _cache_path(key)
    if p and xml:
        os.makedirs(FT_CACHE, exist_ok=True)
        with gzip.open(p + ".tmp", "wt", encoding="utf-8") as fh:
            fh.write(xml)
        os.replace(p + ".tmp", p)  # atomic: a killed job never leaves a half-written cache file


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
