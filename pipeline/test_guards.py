#Date: 2026-10-28
#Purpose: Synthetic-data tests for the catalogue's data-quality guards. Every case here exists because a real mislabel got
#  through and the owner caught it, so each test names the entry that failed. Runs offline (no network, no real masterlist):
#  entries are built in a temp dir, so a bug here can never touch masterlist/.
#Usage: python3 pipeline/test_guards.py          # exits non-zero on the first failure
#INPUT: none. OUTPUT: PASS/FAIL per case on stdout.

import re
import shutil
import sys
import tempfile
from pathlib import Path

import yaml

import common

PASS, FAIL = [], []


def check(name, got, want):
    (PASS if got == want else FAIL).append(name)
    print(f"{'PASS' if got == want else 'FAIL'}  {name}" + ("" if got == want else f"\n        got {got!r}\n        want {want!r}"))


BASE = {"name": "Foo-seq", "category": "wet", "summary": "x", "readouts": ["rna"], "resolution": ["bulk"],
        "scope": "genome-wide", "chemistry": ["reverse-transcription"], "reference": {"doi": "10.1/x"}}


def errors_for(entry):
    """Run build.load() over a temp masterlist holding exactly this entry; return its error strings."""
    import build
    tmp = Path(tempfile.mkdtemp())
    (tmp / f"{common.slug(entry['name'])}.yaml").write_text(yaml.safe_dump(entry, sort_keys=False))
    old = build.METHODS_DIR
    build.METHODS_DIR = tmp
    try:
        _, _, errs = build.load()
    finally:
        build.METHODS_DIR = old
        shutil.rmtree(tmp)
    return errs


# --- guard 1: a single-cell assay must say how cells are kept apart (origin: SIMPLE-seq) -------------------------
sc = BASE | {"resolution": ["single-cell"]}
check("single-cell with no partitioning chemistry is an ERROR",
      any("cell-partitioning" in e for e in errors_for(sc)), True)
check("single-cell + combinatorial-indexing is accepted (SIMPLE-seq's real chemistry)",
      any("cell-partitioning" in e for e in errors_for(sc | {"chemistry": ["reverse-transcription", "combinatorial-indexing"]})), False)
check("single-cell + droplet-microfluidics is accepted",
      any("cell-partitioning" in e for e in errors_for(sc | {"chemistry": ["droplet-microfluidics"]})), False)
check("partition_unknown is an accepted, explicit opt-out",
      any("cell-partitioning" in e for e in errors_for(sc | {"partition_unknown": "full text paywalled"})), False)
check("bulk assay is never asked for a partitioning tag",
      any("cell-partitioning" in e for e in errors_for(BASE)), False)
check("dry entry is never asked for a partitioning tag",
      any("cell-partitioning" in e for e in errors_for({**sc, "category": "dry", "chemistry": None})), False)

# --- guard 2: rejected entries are skipped entirely (origin: sc-end5-seq, a category not a method) ---------------
check("a rejected entry raises no errors even when otherwise invalid",
      errors_for({"name": "Bad-seq", "rejected": "not a method"}), [])

# --- guard 3: author+year placeholder names (origin: Delley2021) -------------------------------------------------
check("'Delley2021'-style name is an ERROR",
      any("author+year" in e for e in errors_for(BASE | {"name": "Delley2021"})), True)
check("a real method name is fine", any("author+year" in e for e in errors_for(BASE)), False)

# --- guard 4: Europe PMC titles carry escaped markup (origin: m6A-ARTR-DBiT shown as 'm&lt;sup&gt;6&lt;/sup&gt;A') -
import build as _b
check("escaped markup is unescaped in titles", _b.clean("m&lt;sup&gt;6&lt;/sup&gt;A profiling"), "m6A profiling")
check("plain titles pass through", _b.clean("Simple title"), "Simple title")
check("empty title stays empty", _b.clean(""), None)

# --- guard 5: acronym expansion must match the name's CAPITAL letters AND its lowercase words ---------------------
#     (origin: ChAIR had none; mtscATAC-seq was given plain ATAC-seq's expansion; HT-recruit got "High-throughput method")
from acronym import matches, expansion

for nm, phrase, want in [
        ("ChAIR", "Chromatin Accessibility, Interaction and RNA", True),
        ("HiCAR", "Hi-C on accessible regulatory DNA", True),
        ("CPT-seq", "contiguity-preserving transposition sequencing", True),
        ("SHARE-seq", "simultaneous high-throughput ATAC and RNA expression with sequencing", True),
        ("microSPLiT", "Microbial split-pool ligation transcriptomics", True),
        ("mtscATAC-seq", "Assay for Transposase Accessible Chromatin with sequencing", False),
        ("HT-recruit", "High-throughput method", False),
        ("DR-seq", "genomic DNA and mRNA from the same cell", False)]:
    check(f"matches({nm!r}) is {want}", matches(nm, phrase), want)

check("expansion() pulls the authors' phrase out of a sentence",
      expansion("ChAIR", "we developed a protocol to capture Chromatin Accessibility, Interaction, and RNA profiles (ChAIR) in single cells"),
      "Chromatin Accessibility, Interaction, and RNA profiles")
check("expansion() reads the 'NAME (words)' form",
      expansion("HiCAR", "we report a new method HiCAR (Hi-C on accessible regulatory DNA), which uses Tn5"),
      "Hi-C on accessible regulatory DNA")
check("expansion() returns None when the text has no expansion",
      expansion("Foo-seq", "Foo-seq is a great assay that we used on brain tissue."), None)
check("expansion() refuses the wrong-method phrase",
      expansion("mtscATAC-seq", "the Assay for Transposase Accessible Chromatin with sequencing (mtscATAC-seq) was used"), None)

# --- guard 6: per-host pacing backs off on 429 and recovers on success (origin: bioRxiv throttling) --------------
common._GAP.clear()
host = "www.biorxiv.org"
url = f"https://{host}/x"
start = common.MIN_GAP[host]
common._paced(url, False)
after_429 = common._GAP[host]
check("a 429 doubles the gap", after_429 == min(common.MAX_GAP, start * 2), True)
for _ in range(50):
    common._paced(url, True)
check("successes shrink the gap back to the floor, never below", common._GAP[host] == start, True)
for _ in range(20):
    common._paced(url, False)
check("the gap is capped at MAX_GAP", common._GAP[host] == common.MAX_GAP, True)
check("an unlisted host is not paced at all", common._wait_turn("https://example.com/x"), None)

# --- guard 7: the full-text cache round-trips and survives a missing key -----------------------------------------
common.FT_CACHE = tempfile.mkdtemp()
common.cache_put("10.1/abc", "<article>body</article>")
check("cache round-trips", common.cache_get("10.1/abc"), "<article>body</article>")
check("cache miss returns None", common.cache_get("10.1/never-stored"), None)
check("no key, no crash", common.cache_get(None), None)
shutil.rmtree(common.FT_CACHE)

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
sys.exit(1 if FAIL else 0)

# ---- Provenance ----
# Upstream:   pipeline/build.py (load, clean, CELL_PARTITION), pipeline/common.py (_paced, _wait_turn, cache_*)
# Downstream: run before any push that touches the guards; pipeline/benchmark.py covers the real-entry regressions
# References: each case cites the real entry whose mislabel motivated it (SIMPLE-seq, sc-end5-seq, Delley2021,
#             m6A-ARTR-DBiT, ChAIR/mtscATAC-seq, bioRxiv 429s)
# Notes:      fully synthetic + offline: entries are built in a temp dir, so masterlist/ is never touched.
