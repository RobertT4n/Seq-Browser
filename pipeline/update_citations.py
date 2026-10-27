#Date: 2026-10-26 (updated 2026-10-27: Crossref by default - OpenAlex now returns 401 without an API key)
#Purpose: Refresh citation counts for every masterlist entry. Kept in masterlist/citations.json, separate from the method
#  files, so the weekly refresh never rewrites curated entries.
#  Source: Crossref is-referenced-by-count (free, no key). If OPENALEX_API_KEY is set, OpenAlex cited_by_count is used
#  instead for ALL entries (tracks Google Scholar a little closer). One source at a time so counts stay comparable.
#Usage: python pipeline/update_citations.py
#       OPENALEX_API_KEY=... python pipeline/update_citations.py
#INPUT: masterlist/methods/*.yaml (reference.doi); OUTPUT: masterlist/citations.json {id: {"count", "checked", "source"}}

import json
import os
import sys
import urllib.parse
from datetime import date

import yaml

from common import METHODS_DIR, ROOT, get

OUT = ROOT / "masterlist" / "citations.json"
KEY = os.environ.get("OPENALEX_API_KEY")
SOURCE = "openalex" if KEY else "crossref"


def count(doi):
    q = urllib.parse.quote(doi)
    if KEY:
        return get(f"https://api.openalex.org/works/doi:{q}?select=cited_by_count&api_key={KEY}")["cited_by_count"]
    return get(f"https://api.crossref.org/works/{q}?mailto=seqbrowser@users.noreply.github.com")["message"]["is-referenced-by-count"]


old = json.loads(OUT.read_text()) if OUT.exists() else {}
new, failed, n = {}, [], 0
for p in sorted(METHODS_DIR.glob("*.yaml")):
    doi = (yaml.safe_load(p.read_text()).get("reference") or {}).get("doi")
    if not doi:
        continue
    n += 1
    try:
        new[p.stem] = {"count": count(doi), "checked": date.today().isoformat(), "source": SOURCE}
    except Exception as e:
        failed.append(f"{p.stem}: {type(e).__name__}")
        if p.stem in old:  # keep last known count rather than dropping it
            new[p.stem] = old[p.stem]
OUT.write_text(json.dumps(new, indent=1, sort_keys=True) + "\n")
print(f"{len(new)} citation counts written ({SOURCE}); {len(failed)} lookups failed" + (": " + ", ".join(failed) if failed else ""),
      file=sys.stderr)
if len(failed) > 0.1 * max(n, 1):
    sys.exit(f"FAIL LOUD: {len(failed)}/{n} citation lookups failed")

# ---- Provenance ----
# Upstream:   masterlist/methods/*.yaml
# Downstream: pipeline/build.py (citations column, Family circle sizes, Analysis "Most cited"); weekly GitHub Action
# References: Crossref REST API (is-referenced-by-count); OpenAlex API (cited_by_count, key required since 2026)
# Notes:      counts differ by source (TAPS 2019: Crossref 476); never mix sources within one refresh
