# Seq-Browser <img align="right" src="Seq-Browser_Logo1.png" style="height:100px;" />

A browser for sequencing assays: a curated, continuously updated catalogue of sequencing-based methods (single-cell, spatial, temporal and more), tagged by what they measure and how, and readable by both people and LLMs.

- **Full database, one file:** [`METHODS.md`](METHODS.md). Point an LLM here instead of making it search the web.
- **Machine-readable:** [`docs/methods.json`](docs/methods.json), [`docs/methods.csv`](docs/methods.csv), [`docs/llms.txt`](docs/llms.txt)
- **Website:** https://robertt4n.github.io/Seq-Browser/ (Table, Analysis, About)

![Seq-Browser flow](docs/flow.png)

## Rationale

Frederick Sanger's invention of DNA sequencing in the 1970s allowed scientists to "read" the genome. This method called Sanger sequencing utilized the concept of dideoxy chain termination to sequence DNA and lead to the sequencing of the entire human genome in 2003, costing $3B USD.

In the early 2000s, next-generation sequencing (NGS) methods were developed that quickly expanded the capabilities of genomics research, allowing scientists to sequence the genome of an organism at an unprecedented level of detail. Such technologies have led to the success of large-scale sequencing projects such as The Cancer Genome Atlas (TCGA) and Encyclopedia of DNA Elements (ENCODE), which greatly accelerate the rate of basic and translational biomedical research.

In recent years, there has been a remarkable explosion of different sequencing assays that can profile not just DNA, but also RNA, protein, and/or epigenetic modifications. In addition to utilising NGS platforms, some methods may also utilise microfluidic systems (to sort by single cells), or microscopy-based platforms (to preserve spatial information). Such emerging methods are being released to the scientific community at a blinding rate, and new ones are often only named deep inside a paper's Results.

Seq-Browser catalogues them and keeps the list up to date automatically.

## How it works

```
Fetch      bioRxiv/medRxiv + Europe PMC (PubMed journals), etc: new papers, full text when open access
   │
Triage     free rule-based filter (~1,200 papers/week -> ~100): abstract check + full-text naming scan
   │        to catch methods named only in Results
   │
classify    cheap language model reads each candidate -> structured labels + quoted evidence   [next phase]
   │
review        weekly pull request and review
              
   │
masterlist/methods/*.yaml   one file per method (continuously growing ground truth database) -> METHODS.md, docs/methods.json/.csv, llms.txt
```


## Labels

Each method is tagged on independent axes; allowed values live in [`taxonomy.yaml`](taxonomy.yaml):
**category** (wet / dry), **readouts** (3d-genome, rna, histone-modification, ...), **resolution** (bulk / single-cell / spatial / subcellular), **scope** (genome-wide / targeted), **chemistry** (proximity-ligation, mnase, tn5, droplet-microfluidics, ...), plus **variant_of** links to parent methods (e.g. RCMC -> Micro-C).

Computational (dry) methods are collected but kept "under construction" until curated.

## Submitting a method

Use the **[Submit page](https://robertt4n.github.io/Seq-Browser/submit.html)**, which opens a pre-filled submission issue. 
Submissions by this approach are added to the weekly trawl with priority.
