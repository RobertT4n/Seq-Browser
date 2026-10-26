#Date: 2026-10-26
#Purpose: Upgrade preprint references to their published journal version. For every entry citing a bioRxiv/medRxiv DOI,
#  ask the bioRxiv API whether it has since been published; if so the journal DOI becomes reference.doi (and its
#  metadata is re-resolved from Europe PMC) while the preprint is kept as reference.preprint_doi. Run weekly.
#Usage: python pipeline/update_published.py            # all entries
#       python pipeline/update_published.py snmc2t-seq # one entry
#INPUT: masterlist/methods/*.yaml

import sys

import yaml

from common import BIORXIV, METHODS_DIR, get
from resolve_refs import resolve

PREPRINT = ("10.1101/", "10.64898/")


def published_doi(doi):
    for server in ("biorxiv", "medrxiv"):
        try:
            for r in get(f"{BIORXIV}/details/{server}/{doi}").get("collection") or []:
                if r.get("published") and r["published"] != "NA":
                    return r["published"]
        except Exception:
            pass
    return None


def upgrade(path):
    e = yaml.safe_load(path.read_text())
    ref = e.get("reference") or {}
    doi = ref.get("doi") or ""
    if not doi.startswith(PREPRINT) or (ref.get("journal") or "").lower() not in ("biorxiv", "medrxiv", ""):
        return None
    pub = published_doi(doi)
    if not pub:
        return f"{path.stem:<24} still a preprint ({doi})"
    e["reference"] = {"doi": pub, "preprint_doi": doi}
    path.write_text(yaml.safe_dump(e, sort_keys=False, allow_unicode=True, width=120))
    return f"{path.stem:<24} UPGRADED {doi} -> {pub}: {resolve(path)}"


if __name__ == "__main__":
    targets = [METHODS_DIR / f"{s}.yaml" for s in sys.argv[1:]] or sorted(METHODS_DIR.glob("*.yaml"))
    for p in targets:
        msg = upgrade(p)
        if msg:
            print(msg)
