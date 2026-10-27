# Seq-Browser Proc_step2: classify candidate papers

(Canonical copy - workers get this file. Paths below are filled in per run.)

You decide, for each candidate paper, whether it introduces a NEW sequencing method. Most do not; rejecting is the
normal outcome. Accuracy beats coverage. Never guess: if unsure, decide `UNSURE` and explain.

Repo (working dir for commands): `<repo>` (given in your prompt)
Step2 dir: `<step2 dir>` (given in your prompt)

## Inputs
- Your batch (path in your prompt): JSON list of papers with title, abstract, doi, and `names_found` (method-like names the
  rule-based filter spotted, possibly noisy).
- `known_methods.tsv` (step2 dir): every method already in the database (id, name, aliases).
- `taxonomy.yaml` (repo): the ONLY allowed tag values. Example entries: `masterlist/methods/share-seq.yaml`, `masterlist/methods/scnt-seq.yaml`.

## Labels: measure what the method actually reads out
Readouts are defined one by one in `taxonomy.yaml` (read the comments). Choose by WHAT IS SEQUENCED / MEASURED, not by
the molecule that happens to be handled: ribosome-protected fragments are `translation`, not `rna`; m6A maps are
`rna-modification`; CLIP is `rna-protein-interaction`; RNA-virus genomes are `genome-sequence`. List the method's
PRIMARY readout first (it decides the graph lane).
**If no tag describes the measurement, do NOT pick the nearest one.** Decide `MISSING_TAG`, write the file anyway with your
best tags plus `needs_review: "MISSING_TAG: <what is missing>"`, and say so in your final message. A forced label is a
silent error; a flagged gap is a five-minute fix. (Origin: RAPPL-Seq, a ribosome-profiling method, was once labelled
`rna` because no translation readout existed.)

## Two lineage/scope rules (origin: direct-capture Perturb-seq was tagged `targeted`, DC-TAP-seq lineage flattened)
- `scope` describes the method's DEFAULT readout. An optional add-on demonstrated in the same paper (e.g. hybridization
  target enrichment of a whole-transcriptome library) does not make the method `targeted`.
- If the paper says it "improves on", "modifies", "extends" or "is a version of" X, that is `variant_of: [x]`. Use
  `builds_on` only for methods it borrows a component from (a vector, a capture chemistry, a barcoding scheme).

## Decide one of
- `NEW_WET`: the paper introduces a new sequencing-based wet-lab assay/protocol (a new library-prep / molecular method,
  or a substantial named modification of one). It must be the paper's own contribution ("we present/develop X").
- `NEW_DRY`: the paper introduces a new computational method/tool specifically for analysing sequencing data.
- `DUPLICATE`: the method it introduces is already in known_methods.tsv (same method under any name/alias) -> give the id.
- `USES_ONLY`: the paper applies existing methods (biology study, atlas, resource, benchmark) without a new method.
- `NOT_SEQ`: not about sequencing methods at all (imaging only, proteomics by mass spec, clinical, etc.).
- `UNSURE`: you cannot tell from the abstract. Say exactly what is unclear.
- `MISSING_TAG`: a real new method whose measurement has no fitting tag (see above).
If `submitted: true`, the paper was suggested by a user: be extra careful before rejecting, and explain the reason fully.
If `watchlist` is set, the row came from a curated external list (`watchlist_name`, `watchlist_url`): one normal pass,
but if `unresolved: true` there is no abstract - look the method up (name + link) before deciding; vendor platforms,
imaging-only, mass-spec and pure software rows are common there and should be NOT_SEQ / NEW_DRY as appropriate.
A paper can introduce two methods: give one decision row per method.

## For NEW_WET and NEW_DRY: write `masterlist/methods/<slug>.yaml`
Slug = method name lowercased, non-alphanumerics -> "-", "&" -> "-and-". Same format as the examples:
```yaml
name: X
aliases: [optional]
category: wet            # or dry
summary: One plain sentence in your own words.
readouts: [...]          # taxonomy keys
resolution: [...]
temporal: [...]          # only if the method captures time; else omit
scope: genome-wide       # or targeted
chemistry: [...]         # wet only; dry entries omit chemistry. Every RNA readout needs reverse-transcription.
variant_of: [id]         # ids from known_methods.tsv ONLY; omit if none
builds_on: [id, id]      # ids from known_methods.tsv ONLY; omit if none
reference:
  doi: <the paper's doi from the batch>
links: {}
source: weekly-2026-10-26
added: '2026-10-26'
needs_review: true
evidence: "Exact sentence from the abstract that shows the paper introduces this method."
```
Then run `python3 pipeline/resolve_refs.py <slug>`; it must print author/year/journal. Only touch your own new files.
No git, no other edits.

## Write your decisions
Save `decisions_<NN>.jsonl` in the step2 dir (NN = your batch number), one JSON object per line:
`{"doi": ..., "title": ..., "decision": "NEW_WET|NEW_DRY|DUPLICATE|USES_ONLY|NOT_SEQ|UNSURE|MISSING_TAG", "method": "name or null",
  "slug": "file written or null", "duplicate_of": "id or null", "reason": "one short sentence"}`
Every paper in your batch gets at least one line.

## Final message (concise)
Counts per decision, the list of files you created (slug - one line each, flag anything <80% sure), and the UNSURE items.
