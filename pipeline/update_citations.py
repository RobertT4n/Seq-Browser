#Date: 2026-10-26
#Purpose: Refresh citation counts for every masterlist entry from OpenAlex (free; counts track Google Scholar far
#  better than Europe PMC's citedByCount). Kept in masterlist/citations.json, separate from the method files, so the
#  weekly refresh never rewrites curated entries.
#Usage: python pipeline/update_citations.py
#INPUT: masterlist/methods/*.yaml (reference.doi); OUTPUT: masterlist/citations.json {id: {"count", "checked"}}

import json
import sys
import urllib.parse
from datetime import date

import yaml

from common import METHODS_DIR, ROOT, get

OUT = ROOT / "masterlist" / "citations.json"
old = json.loads(OUT.read_text()) if OUT.exists() else {}
new, failed = {}, []
for p in sorted(METHODS_DIR.glob("*.yaml")):
    doi = (yaml.safe_load(p.read_text()).get("reference") or {}).get("doi")
    if not doi:
        continue
    try:
        w = get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}?select=cited_by_count&mailto=seqbrowser@users.noreply.github.com")
        new[p.stem] = {"count": w["cited_by_count"], "checked": date.today().isoformat()}
    except Exception as e:
        failed.append(f"{p.stem}: {type(e).__name__}")
        if p.stem in old:  # keep last known count rather than dropping it
            new[p.stem] = old[p.stem]
OUT.write_text(json.dumps(new, indent=1, sort_keys=True) + "\n")
print(f"{len(new)} citation counts written; {len(failed)} lookups failed" + (": " + ", ".join(failed) if failed else ""),
      file=sys.stderr)
