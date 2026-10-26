#Date: 2026-10-26
#Purpose: Validate every masterlist entry against taxonomy.yaml, then generate the published outputs:
#  METHODS.md (one LLM-readable table), docs/methods.json + docs/methods.csv (site + downloads), docs/llms.txt.
#  Fails loudly (exit 1) on any invalid entry so a bad push never reaches the site.
#Usage: python pipeline/build.py           # validate + write outputs
#       python pipeline/build.py --check   # validate only (CI)
#INPUT: masterlist/methods/*.yaml (one file per method), taxonomy.yaml

import csv
import json
import sys
from datetime import date

import yaml

from common import METHODS_DIR, ROOT, TAXONOMY, slug

LINK_FIELDS = ("variant_of", "builds_on")  # lineage: direct modification / combines-or-draws-on
REQUIRED = ("name", "category", "summary", "readouts", "resolution", "scope", "chemistry", "reference")
LIST_FIELDS = ("readouts", "resolution", "chemistry", "temporal", "perturbation")  # temporal is optional
REPO = "https://github.com/RobertT4n/Seq-Browser"
RAW = "https://raw.githubusercontent.com/RobertT4n/Seq-Browser/main"


def load():
    tax = yaml.safe_load(TAXONOMY.read_text())
    entries, errors = [], []
    for p in sorted(METHODS_DIR.glob("*.yaml")):
        e = yaml.safe_load(p.read_text())
        errs = [f"missing '{f}'" for f in REQUIRED if not e.get(f) and not (f == "chemistry" and e.get("category") == "dry")]
        if e.get("name") and slug(e["name"]) != p.stem:
            errs.append(f"file name should be {slug(e['name'])}.yaml")
        for f in LIST_FIELDS:
            errs += [f"{f}: unknown value '{v}'" for v in e.get(f) or [] if v not in tax[f]]
        for f in ("category", "scope"):
            if e.get(f) and e[f] not in tax[f]:
                errs.append(f"{f}: unknown value '{e[f]}'")
        errs += [f"introduces: '{v}' is not one of this entry's readouts" for v in e.get("introduces") or [] if v not in e.get("readouts", [])]
        if not (e.get("reference") or {}).get("doi") and not (e.get("reference") or {}).get("url"):
            errs.append("reference needs a doi (run pipeline/resolve_refs.py) or, for kits with no paper, a url")
        errors += [f"{p.name}: {x}" for x in errs]
        e["id"] = p.stem
        entries.append(e)
    errors += check_lineage(entries)
    check_inherited_readouts(entries)
    return entries, tax, errors


def parents(e):
    return [*(e.get("variant_of") or []), *(e.get("builds_on") or [])]


def check_lineage(entries):
    """Every link must point at an existing entry, with no self-links or cycles. Parent newer than child = warning."""
    by_id, errs = {e["id"]: e for e in entries}, []
    for e in entries:
        for f in LINK_FIELDS:
            for t in e.get(f) or []:
                if t == e["id"]:
                    errs.append(f"{e['id']}.yaml: {f} points at itself")
                elif t not in by_id:
                    errs.append(f"{e['id']}.yaml: {f} '{t}' has no entry - add masterlist/methods/{t}.yaml or fix the id")
                elif (by_id[t]["reference"].get("year") or 0) > (e["reference"].get("year") or 9999):
                    print(f"warning: {e['id']} ({e['reference'].get('year')}) lists newer parent {t} "
                          f"({by_id[t]['reference'].get('year')})", file=sys.stderr)
    state = {}  # cycle check: 1 = on current path, 2 = done

    def visit(i, path):
        state[i] = 1
        for t in parents(by_id[i]):
            if t in by_id and state.get(t) == 1:
                errs.append("lineage cycle: " + " -> ".join(path + [i, t]))
            elif t in by_id and not state.get(t):
                visit(t, path + [i])
        state[i] = 2
    for i in by_id:
        if not state.get(i):
            visit(i, [])
    return errs


def ancestors(i, by_id, seen=None):
    seen = set() if seen is None else seen
    for t in parents(by_id[i]):
        if t in by_id and t not in seen:
            seen.add(t)
            ancestors(t, by_id, seen)
    return seen


def check_inherited_readouts(entries):
    """A method with parents should inherit each readout from some ancestor, unless it says it introduces that readout
    (`introduces: [readout]`). Catches missing links, e.g. a Hi-C + methylation method with no methylation ancestor."""
    by_id = {e["id"]: e for e in entries}
    for e in entries:
        if not parents(e):
            continue  # roots introduce everything they measure
        inherited = {r for a in ancestors(e["id"], by_id) for r in by_id[a]["readouts"]}
        for r in e["readouts"]:
            if r not in inherited and r not in (e.get("introduces") or []):
                print(f"warning: {e['id']} measures '{r}' but no ancestor does - add a parent that measures it, "
                      f"or `introduces: [{r}]` if this method was first", file=sys.stderr)


def flat(e, cites, children, tax):
    r = e["reference"]
    return {"id": e["id"], "name": e["name"], "aliases": "; ".join(e.get("aliases") or []), "category": e["category"],
            "domains": "; ".join(dict.fromkeys(tax["readouts"][x] for x in e["readouts"])),
            "readouts": "; ".join(e["readouts"]), "resolution": "; ".join(e["resolution"]), "scope": e["scope"],
            "temporal": "; ".join(e.get("temporal") or []), "perturbation": "; ".join(e.get("perturbation") or []),
            "chemistry": "; ".join(e.get("chemistry") or []), "variant_of": "; ".join(e.get("variant_of") or []), "builds_on": "; ".join(e.get("builds_on") or []),
            "children": "; ".join(sorted(children.get(e["id"], []))),
            "year": r.get("year"), "first_author": r.get("first_author"), "last_author": r.get("last_author"),
            "journal": r.get("journal"), "title": r.get("title"), "doi": r.get("doi"), "url": r.get("url"), "citations": (cites.get(e["id"]) or {}).get("count"),
            "preprint": (r.get("journal") or "").lower() in ("biorxiv", "medrxiv"), "summary": e["summary"],
            "protocol": (e.get("links") or {}).get("protocol"), "code": (e.get("links") or {}).get("code"),
            "needs_review": e.get("needs_review")}


def md_table(rows):
    cols = ["Method", "Aliases", "Readouts", "Resolution", "Temporal", "Scope", "Chemistry", "Lineage", "Ref", "Cites", "Summary"]
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for f in rows:
        ref = (f"{f['first_author']} {f['year']}, {f['journal']}, [doi:{f['doi']}](https://doi.org/{f['doi']})" if f["doi"]
               else f"[{f['url']}]({f['url']})")
        cells = [f"**{f['name']}**", f["aliases"], f["readouts"], f["resolution"], f["temporal"], f["scope"], f["chemistry"],
                 "; ".join(x for x in (f["variant_of"] and f"variant of {f['variant_of']}",
                                       f["builds_on"] and f"builds on {f['builds_on']}") if x), ref, f["citations"], f["summary"]]
        out.append("| " + " | ".join(str(c or "").replace("|", "/") for c in cells) + " |")
    return "\n".join(out)


def write(entries, tax):
    cpath = ROOT / "masterlist" / "citations.json"
    cites = json.loads(cpath.read_text()) if cpath.exists() else {}
    children = {}
    for e in entries:
        for t in parents(e):
            children.setdefault(t, []).append(e["id"])
    rows = sorted((flat(e, cites, children, tax) for e in entries), key=lambda f: f["name"].lower())
    wet, dry = [f for f in rows if f["category"] == "wet"], [f for f in rows if f["category"] == "dry"]
    today = date.today().isoformat()
    md = [f"# Seq-Browser masterlist",
          f"",
          f"Sequencing-based assays, one row per method. Updated {today}. {len(wet)} wet-lab methods"
          + (f", {len(dry)} computational (under construction)." if dry else "."),
          f"",
          f"**For LLMs / tools:** this file is the complete database. Columns use a fixed vocabulary "
          f"(see `taxonomy.yaml`). `Variant of` gives the parent method's id (lowercase-hyphenated name). "
          f"Machine-readable copies: `docs/methods.json`, `docs/methods.csv`. Raw URL: {RAW}/METHODS.md",
          f"",
          f"## Wet-lab methods",
          f"",
          md_table(wet),
          f"",
          f"## Lineage (parent -> child)",
          f"",
          f"`variant` = child is a direct modification of the parent; `builds on` = child combines or draws on the parent.",
          f""] + [f"- {p} -> {f['id']} ({kind})" for f in wet for kind, key in (("variant", "variant_of"), ("builds on", "builds_on"))
                  for p in (f[key].split("; ") if f[key] else [])] + [
    ]
    if dry:
        md += ["", "## Computational methods (under construction - not yet curated)", "", md_table(dry)]
    (ROOT / "METHODS.md").write_text("\n".join(md) + "\n")
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    (docs / "taxonomy.json").write_text(json.dumps(tax, indent=1))
    (docs / "methods.json").write_text(json.dumps({"updated": today, "methods": rows}, indent=1))
    with (docs / "methods.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    (docs / "llms.txt").write_text(
        "# Seq-Browser\n\n> A curated, continuously updated table of sequencing-based assays (single-cell, spatial, temporal and more), "
        "tagged by readout, resolution, scope and chemistry, with variant-of links and primary references.\n\n"
        f"- [Full masterlist (Markdown table)]({RAW}/METHODS.md): the whole database in one file\n"
        f"- [methods.json]({RAW}/docs/methods.json): same data, machine-readable\n"
        f"- [Label vocabulary]({RAW}/taxonomy.yaml): allowed values for every tag\n"
        f"- [Repository]({REPO})\n")
    return len(wet), len(dry)


if __name__ == "__main__":
    entries, tax, errors = load()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(f"{len(errors)} problem(s) in masterlist - nothing written")
    if "--check" in sys.argv:
        print(f"{len(entries)} entries valid")
    else:
        print("wrote METHODS.md, docs/methods.json, docs/methods.csv, docs/llms.txt (%d wet, %d dry)" % write(entries, tax))
