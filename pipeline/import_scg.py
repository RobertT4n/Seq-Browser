#Date: 2026-10-26
#Purpose: Build an import queue from Teichlab/scg_lib_structs (CC-BY 4.0): every method page's name, original-paper DOI,
#  and the other methods it cross-links (used as lineage hints). Marks methods already in the masterlist. The queue is
#  input for classification/curation; nothing here writes to masterlist/methods/.
#Usage: python pipeline/import_scg.py     # writes masterlist/queue/scg_lib_structs.jsonl and prints a summary
#INPUT: GitHub API + raw pages of Teichlab/scg_lib_structs; masterlist/methods/*.yaml (to flag duplicates)

import json
import re
import sys
import urllib.parse

import yaml

from common import METHODS_DIR, ROOT, get, slug

REPO, RAW = "Teichlab/scg_lib_structs", "https://raw.githubusercontent.com/Teichlab/scg_lib_structs/master/methods_html"
OUT = ROOT / "masterlist" / "queue" / "scg_lib_structs.jsonl"
SKIP = re.compile(r"archive|^index", re.I)


def url_to_doi(url):
    """Publisher URL -> DOI where the URL encodes it; Elsevier PIIs via Crossref."""
    u = urllib.parse.unquote(url)
    m = re.search(r"(10\.\d{4,9}/[^\s?#\"']+)", u)
    if m:
        return re.sub(r"(\.full|\.abstract|\.pdf|v\d+)+$", "", m.group(1).rstrip("/"))
    m = re.search(r"nature\.com/articles/([\w.-]+)", u)
    if m:
        return f"10.1038/{m.group(1)}"
    m = re.search(r"/pii/(S?[\dX]+)", u, re.I)
    if m:
        try:
            items = get(f"https://api.crossref.org/works?filter=alternative-id:{m.group(1)}&rows=1")["message"]["items"]
            return items[0]["DOI"] if items else None
        except Exception:
            return None
    m = re.search(r"pubmed/(\d+)|pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", u)
    if m:
        try:
            hit = get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:{m.group(1) or m.group(2)}&format=json")
            res = hit["resultList"]["result"]
            return res[0].get("doi") if res else None
        except Exception:
            return None
    return None


def known_names():
    names = {}
    for p in METHODS_DIR.glob("*.yaml"):
        e = yaml.safe_load(p.read_text())
        for n in [e["name"], *(e.get("aliases") or [])]:
            names[slug(n)] = p.stem
    return names


def main():
    pages = [f["name"] for f in get(f"https://api.github.com/repos/{REPO}/contents/methods_html") if f["name"].endswith(".html")]
    pages = [p for p in pages if not SKIP.search(p)]
    known, rows, unresolved = known_names(), [], []
    for page in sorted(pages):
        html = get(f"{RAW}/{page}", as_json=False)
        title = re.search(r"<title>(.*?)</title>", html, re.S)
        name = re.sub(r"\s+", " ", title.group(1)).strip() if title else page[:-5]
        h1 = re.search(r"<h1>\s*<a href=\"([^\"]+)\"", html)
        paper = h1.group(1) if h1 else None
        doi = url_to_doi(paper) if paper else None
        related = sorted({m for m in re.findall(r"methods_html/([\w.+-]+)\.html", html) if m != page[:-5]})
        dup = known.get(slug(name)) or known.get(slug(page[:-5]))
        rows.append({"name": name, "page": f"https://teichlab.github.io/scg_lib_structs/methods_html/{page}",
                     "paper_url": paper, "doi": doi, "related_pages": related, "already_in_masterlist": dup})
        if not doi:
            unresolved.append(name)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(json.dumps(r) + "\n" for r in rows))
    new = [r for r in rows if not r["already_in_masterlist"]]
    print(f"{len(rows)} method pages -> {OUT.relative_to(ROOT)}: {len(new)} new, {len(rows) - len(new)} already listed, "
          f"{len(unresolved)} without a resolvable DOI" + (f" ({', '.join(unresolved)})" if unresolved else ""), file=sys.stderr)


if __name__ == "__main__":
    main()
