# Seq-Browser masterlist

Sequencing-based assays, one row per method. Updated 2026-10-26. 49 wet-lab methods.

**For LLMs / tools:** this file is the complete database. Columns use a fixed vocabulary (see `taxonomy.yaml`). `Variant of` gives the parent method's id (lowercase-hyphenated name). Machine-readable copies: `docs/methods.json`, `docs/methods.csv`. Raw URL: https://raw.githubusercontent.com/RobertT4n/Seq-Browser/main/METHODS.md

## Wet-lab methods

| Method | Aliases | Readouts | Resolution | Scope | Chemistry | Lineage | Ref | Cites | Summary |
|---|---|---|---|---|---|---|---|---|---|
| **2C-RT** |  | replication-timing | bulk | genome-wide | nucleotide-labeling; facs-sorting |  | Urien B 2026, bioRxiv, [doi:10.64898/2026.10.09.758048](https://doi.org/10.64898/2026.10.09.758048) |  | Replication timing from EdU-labelled S-phase cells sorted by a cell-cycle marker and DNA content, with multiplexed EdU-seq. |
| **3C** |  | 3d-genome | bulk | targeted | restriction-digest; proximity-ligation |  | Dekker J 2002, Science, [doi:10.1126/science.1067799](https://doi.org/10.1126/science.1067799) |  | Chromosome conformation capture: crosslink, digest and ligate, then quantify ligation between chosen loci. The ancestor of the C-family. |
| **4C-seq** |  | 3d-genome | bulk | targeted | restriction-digest; proximity-ligation | variant of 3c | van de Werken HJ 2012, Nat Methods, [doi:10.1038/nmeth.2173](https://doi.org/10.1038/nmeth.2173) | 390 | Inverse-PCR from a single viewpoint to sequence all of its ligation partners (one-vs-all). |
| **ATAC-seq** |  | chromatin-accessibility | bulk | genome-wide | tn5 | builds on dnase-seq; faire-seq | Buenrostro JD 2013, Nat Methods, [doi:10.1038/nmeth.2688](https://doi.org/10.1038/nmeth.2688) | 6415 | Tn5 transposase inserts sequencing adapters into accessible chromatin. |
| **Capture-C** |  | 3d-genome | bulk | targeted | restriction-digest; proximity-ligation; oligo-capture | variant of 3c | Hughes JR 2014, Nat Genet, [doi:10.1038/ng.2871](https://doi.org/10.1038/ng.2871) | 473 | 3C library enriched with capture oligonucleotides to profile one-vs-all contacts from many viewpoints at once. |
| **ChIA-PET** |  | 3d-genome; protein-dna-binding | bulk | genome-wide | antibody-pull-down; proximity-ligation | builds on 3c; chip-seq | Fullwood MJ 2009, Nature, [doi:10.1038/nature08497](https://doi.org/10.1038/nature08497) | 1726 | Chromatin interactions anchored at sites bound by a chosen protein, via ChIP plus paired-end-tag ligation. |
| **ChIP-seq** |  | protein-dna-binding; histone-modification | bulk | genome-wide | antibody-pull-down |  | Johnson DS 2007, Science, [doi:10.1126/science.1141319](https://doi.org/10.1126/science.1141319) |  | Chromatin immunoprecipitation followed by sequencing to map protein binding or histone marks genome-wide. |
| **ChIPmentation** |  | histone-modification; protein-dna-binding | bulk | genome-wide | antibody-pull-down; tn5 | variant of chip-seq; builds on atac-seq | Schmidl C 2015, Nat Methods, [doi:10.1038/nmeth.3542](https://doi.org/10.1038/nmeth.3542) | 509 | ChIP-seq with Tn5 tagmentation of bead-bound chromatin for fast, low-input library prep. |
| **CUT&RUN** |  | protein-dna-binding; histone-modification | bulk | genome-wide | antibody-tethered-enzyme; mnase | builds on chip-seq | Skene PJ 2017, Elife, [doi:10.7554/elife.21856](https://doi.org/10.7554/elife.21856) |  | Antibody-tethered pA-MNase cleaves around bound sites in permeabilised cells; low background, low input. |
| **CUT&Tag** |  | histone-modification; protein-dna-binding | bulk; single-cell | genome-wide | antibody-tethered-enzyme; tn5 | variant of cut-and-run; builds on atac-seq | Kaya-Okur HS 2019, Nat Commun, [doi:10.1038/s41467-019-09982-5](https://doi.org/10.1038/s41467-019-09982-5) | 2181 | Antibody-tethered pA-Tn5 tagments only at bound sites in permeabilised cells, giving low-background profiles from few cells. |
| **Dip-C** |  | 3d-genome | single-cell | genome-wide | restriction-digest; proximity-ligation; tn5; plate-based | variant of single-cell-hi-c | Tan L 2018, Science, [doi:10.1126/science.aat5641](https://doi.org/10.1126/science.aat5641) | 498 | Single-cell Hi-C with transposon-based whole-genome amplification and haplotype imputation for diploid 3D structures. |
| **DNase-seq** |  | chromatin-accessibility | bulk | genome-wide | dnase-digestion |  | Boyle AP 2008, Cell, [doi:10.1016/j.cell.2007.12.014](https://doi.org/10.1016/j.cell.2007.12.014) |  | DNase I hypersensitive sites sequenced genome-wide to map open chromatin. |
| **Drop-seq** |  | rna | single-cell | genome-wide | reverse-transcription; droplet-microfluidics | variant of single-cell-rna-seq | Macosko EZ 2015, Cell, [doi:10.1016/j.cell.2015.05.002](https://doi.org/10.1016/j.cell.2015.05.002) |  | Cells co-encapsulated with barcoded beads in droplets, giving thousands of single-cell transcriptomes per run. |
| **Droplet Hi-C** |  | 3d-genome | single-cell | genome-wide | restriction-digest; proximity-ligation; tn5; droplet-microfluidics; facs-sorting | variant of in-situ-hi-c; builds on snare-seq | Chang L 2025, Nat Biotechnol, [doi:10.1038/s41587-024-02447-1](https://doi.org/10.1038/s41587-024-02447-1) | 63 | In situ Hi-C followed by droplet barcoding on a commercial 10x scATAC kit for tens of thousands of cells per run. |
| **Droplet Paired-Tag** |  | histone-modification; rna | single-cell | genome-wide | antibody-tethered-enzyme; tn5; droplet-microfluidics; reverse-transcription | variant of paired-tag | Xie Y 2023, Nat Struct Mol Biol, [doi:10.1038/s41594-023-01060-1](https://doi.org/10.1038/s41594-023-01060-1) | 68 | Paired-Tag chemistry moved onto commercial droplet microfluidics for higher throughput and simpler workflow. |
| **ECHOS** | ECHOS+; Epigenetic CUT&Tag via High-resolution Optical Selection | histone-modification; protein-dna-binding | spatial; subcellular | genome-wide | antibody-tethered-enzyme; imaging-guided-selection | variant of cut-and-tag | Cao Q 2026, bioRxiv, [doi:10.64898/2026.03.26.714421](https://doi.org/10.64898/2026.03.26.714421) |  | CUT&Tag on optically selected regions of tissue or nuclei, giving spatially targeted epigenomic profiles down to sub-micron scale. |
| **FAIRE-seq** | FAIRE | chromatin-accessibility | bulk | genome-wide | organic-extraction |  | Giresi PG 2007, Genome Res, [doi:10.1101/gr.5533506](https://doi.org/10.1101/gr.5533506) |  | Nucleosome-depleted DNA partitions to the aqueous phase after crosslinking and phenol-chloroform extraction. |
| **GAGE-seq** |  | 3d-genome; rna | single-cell | genome-wide | restriction-digest; proximity-ligation; combinatorial-indexing; reverse-transcription | builds on sci-hi-c; sci-rna-seq | Zhou T 2024, Nat Genet, [doi:10.1038/s41588-024-01745-3](https://doi.org/10.1038/s41588-024-01745-3) | 70 | Combinatorial-indexing joint profiling of chromatin conformation and transcriptome in single cells. |
| **GAM** | Genome Architecture Mapping | 3d-genome | bulk | genome-wide | cryosectioning |  | Beagrie RA 2017, Nature, [doi:10.1038/nature21411](https://doi.org/10.1038/nature21411) | 715 | Ligation-free co-segregation mapping from sequencing thin nuclear cryosections. |
| **Hi-C** |  | 3d-genome | bulk | genome-wide | restriction-digest; proximity-ligation | variant of 3c | Lieberman-Aiden E 2009, Science, [doi:10.1126/science.1181369](https://doi.org/10.1126/science.1181369) | 8882 | Genome-wide all-vs-all chromatin contact mapping by restriction digest, biotin fill-in and proximity ligation. |
| **HiChIP** |  | 3d-genome; protein-dna-binding | bulk | genome-wide | restriction-digest; proximity-ligation; antibody-pull-down; tn5 | variant of in-situ-hi-c; builds on chia-pet; chip-seq | Mumbach MR 2016, Nat Methods, [doi:10.1038/nmeth.3999](https://doi.org/10.1038/nmeth.3999) | 1131 | In situ Hi-C followed by ChIP and Tn5 library prep to enrich protein-anchored contacts from low input. |
| **HiRES** |  | 3d-genome; rna | single-cell | genome-wide | restriction-digest; proximity-ligation; tn5; plate-based; reverse-transcription | builds on dip-c; single-cell-rna-seq | Liu Z 2023, Science, [doi:10.1126/science.adg3797](https://doi.org/10.1126/science.adg3797) | 172 | Simultaneous single-cell Hi-C and RNA-seq from the same cell. |
| **in situ Hi-C** |  | 3d-genome | bulk | genome-wide | restriction-digest; proximity-ligation | variant of hi-c | Rao SS 2014, Cell, [doi:10.1016/j.cell.2014.11.021](https://doi.org/10.1016/j.cell.2014.11.021) | 9199 | Hi-C with digestion and ligation performed in intact nuclei, giving kilobase-resolution maps and loop calls. |
| **Methyl-HiC** |  | 3d-genome; dna-methylation | bulk; single-cell | genome-wide | restriction-digest; proximity-ligation; bisulfite-or-enzymatic-conversion | builds on in-situ-hi-c | Li G 2019, Nat Methods, [doi:10.1038/s41592-019-0502-z](https://doi.org/10.1038/s41592-019-0502-z) | 229 | In situ Hi-C combined with bisulfite conversion to read contacts and methylation together. |
| **Micro-C** |  | 3d-genome | bulk | genome-wide | mnase; proximity-ligation | variant of hi-c | Hsieh TH 2015, Cell, [doi:10.1016/j.cell.2015.05.048](https://doi.org/10.1016/j.cell.2015.05.048) | 785 | Hi-C variant using MNase instead of restriction enzymes for nucleosome-resolution contact maps. |
| **Micro-Capture-C** | MCC | 3d-genome | bulk | targeted | mnase; proximity-ligation; oligo-capture | variant of capture-c; micro-c | Hua P 2021, Nature, [doi:10.1038/s41586-021-03639-4](https://doi.org/10.1038/s41586-021-03639-4) | 186 | MNase-based Capture-C with ligation junctions read directly, giving near base-pair resolution one-vs-all contact profiles. |
| **NG Capture-C** | Next-Generation Capture-C | 3d-genome | bulk | targeted | restriction-digest; proximity-ligation; oligo-capture | variant of capture-c | Davies JO 2016, Nat Methods, [doi:10.1038/nmeth.3664](https://doi.org/10.1038/nmeth.3664) | 267 | Capture-C with double capture and multiplexing for much higher sensitivity per viewpoint. |
| **Paired Hi-C** |  | 3d-genome; rna | single-cell | genome-wide | restriction-digest; proximity-ligation; tn5; droplet-microfluidics; facs-sorting; reverse-transcription | variant of droplet-hi-c; builds on drop-seq | Chang L 2025, Nat Biotechnol, [doi:10.1038/s41587-024-02447-1](https://doi.org/10.1038/s41587-024-02447-1) | 63 | Droplet Hi-C adapted to the 10x Multiome kit to profile chromatin conformation and transcriptome from the same nucleus. Introduced in the Results section, not the abstract. |
| **Paired-seq** |  | chromatin-accessibility; rna | single-cell | genome-wide | tn5; combinatorial-indexing; reverse-transcription | builds on sci-rna-seq; sci-atac-seq | Zhu C 2019, Nat Struct Mol Biol, [doi:10.1038/s41594-019-0323-x](https://doi.org/10.1038/s41594-019-0323-x) | 343 | Combinatorial-indexing joint profiling of chromatin accessibility and transcriptome in single nuclei. |
| **Paired-Tag** |  | histone-modification; rna | single-cell | genome-wide | antibody-tethered-enzyme; tn5; combinatorial-indexing; reverse-transcription | variant of paired-seq; builds on cut-and-tag | Zhu C 2021, Nat Methods, [doi:10.1038/s41592-021-01060-3](https://doi.org/10.1038/s41592-021-01060-3) | 300 | Antibody-guided Tn5 tagmentation plus combinatorial indexing for joint histone-mark and transcriptome profiles per nucleus. |
| **PLAC-seq** |  | 3d-genome; protein-dna-binding | bulk | genome-wide | restriction-digest; proximity-ligation; antibody-pull-down | variant of in-situ-hi-c; builds on chia-pet; chip-seq | Fang R 2016, Cell Res, [doi:10.1038/cr.2016.137](https://doi.org/10.1038/cr.2016.137) | 343 | Proximity ligation in nuclei followed by ChIP to capture contacts anchored at marked or bound regions. |
| **Pore-C** |  | 3d-genome | bulk | genome-wide | restriction-digest; proximity-ligation; long-read-sequencing | builds on hi-c | Deshpande AS 2022, Nat Biotechnol, [doi:10.1038/s41587-022-01289-z](https://doi.org/10.1038/s41587-022-01289-z) | 157 | Chromatin conformation capture with nanopore reads of full concatemers, capturing multi-way contacts. |
| **RCMC** | Region Capture Micro-C | 3d-genome | bulk | targeted | mnase; proximity-ligation; oligo-capture | variant of micro-c | Goel VY 2023, Nat Genet, [doi:10.1038/s41588-023-01391-1](https://doi.org/10.1038/s41588-023-01391-1) | 271 | Micro-C library enriched for selected regions, giving deep all-vs-all contact maps within them. |
| **RNA-seq** |  | rna | bulk | genome-wide | reverse-transcription |  | Mortazavi A 2008, Nat Methods, [doi:10.1038/nmeth.1226](https://doi.org/10.1038/nmeth.1226) |  | High-throughput sequencing of cDNA to quantify the transcriptome. |
| **scATAC-seq** | single-cell ATAC-seq | chromatin-accessibility | single-cell | genome-wide | tn5; microfluidic-chip | variant of atac-seq | Buenrostro JD 2015, Nature, [doi:10.1038/nature14590](https://doi.org/10.1038/nature14590) |  | ATAC-seq performed on individual cells captured in microfluidic chambers. |
| **sci-ATAC-seq** |  | chromatin-accessibility | single-cell | genome-wide | tn5; combinatorial-indexing | variant of atac-seq | Cusanovich DA 2015, Science, [doi:10.1126/science.aab1601](https://doi.org/10.1126/science.aab1601) |  | First combinatorial-indexing single-cell method: barcoded Tn5 plus PCR indexing across plates. |
| **sci-CAR** |  | chromatin-accessibility; rna | single-cell | genome-wide | tn5; reverse-transcription; combinatorial-indexing | builds on sci-rna-seq; sci-atac-seq | Cao J 2018, Science, [doi:10.1126/science.aau0730](https://doi.org/10.1126/science.aau0730) |  | Combinatorial indexing for joint chromatin accessibility and transcriptome from the same cells. |
| **sci-Hi-C** |  | 3d-genome | single-cell | genome-wide | restriction-digest; proximity-ligation; combinatorial-indexing | variant of single-cell-hi-c; builds on sci-atac-seq | Ramani V 2017, Nat Methods, [doi:10.1038/nmeth.4155](https://doi.org/10.1038/nmeth.4155) | 548 | Single-cell Hi-C scaled to thousands of cells by combinatorial cellular indexing. |
| **sci-RNA-seq** |  | rna | single-cell | genome-wide | reverse-transcription; combinatorial-indexing | variant of single-cell-rna-seq; builds on sci-atac-seq | Cao J 2017, Science, [doi:10.1126/science.aam8940](https://doi.org/10.1126/science.aam8940) |  | Single-cell transcriptomes by combinatorial cellular indexing, no physical isolation of cells. |
| **scNanoHi-C** |  | 3d-genome | single-cell | genome-wide | restriction-digest; proximity-ligation; long-read-sequencing; plate-based | builds on single-cell-hi-c; pore-c | Li W 2023, Nat Methods, [doi:10.1038/s41592-023-01978-w](https://doi.org/10.1038/s41592-023-01978-w) | 56 | Single-cell Hi-C read on nanopore so whole ligation concatemers (multi-way contacts) are sequenced. |
| **SeqTag** |  | rna; chromatin-accessibility; histone-modification | single-cell | genome-wide | antibody-tethered-enzyme; tn5; reverse-transcription |  | Fu B 2026, bioRxiv, [doi:10.64898/2026.06.02.729594](https://doi.org/10.64898/2026.06.02.729594) |  | Single-cell multiomics jointly profiling transcriptome, chromatin accessibility and histone modifications. Named in the abstract only, not the title. |
| **SHARE-seq** |  | chromatin-accessibility; rna | single-cell | genome-wide | tn5; reverse-transcription; split-pool-barcoding | builds on single-cell-rna-seq; scatac-seq | Ma S 2020, Cell, [doi:10.1016/j.cell.2020.09.056](https://doi.org/10.1016/j.cell.2020.09.056) |  | Split-pool ligation barcoding of accessibility and transcriptome from the same single cells. |
| **single-cell Hi-C** | scHi-C | 3d-genome | single-cell | genome-wide | restriction-digest; proximity-ligation; plate-based | variant of hi-c | Nagano T 2013, Nature, [doi:10.1038/nature12593](https://doi.org/10.1038/nature12593) | 1586 | Hi-C performed in individually isolated nuclei to measure contacts in single cells. |
| **single-cell RNA-seq** | scRNA-seq | rna | single-cell | genome-wide | reverse-transcription; plate-based | variant of rna-seq | Tang F 2009, Nat Methods, [doi:10.1038/nmeth.1315](https://doi.org/10.1038/nmeth.1315) |  | First whole-transcriptome sequencing of a single cell (manually picked cells, plate-based cDNA amplification). |
| **sn-m3C-seq** |  | 3d-genome; dna-methylation | single-cell | genome-wide | restriction-digest; proximity-ligation; bisulfite-or-enzymatic-conversion; plate-based; facs-sorting | builds on single-cell-hi-c | Lee DS 2019, Nat Methods, [doi:10.1038/s41592-019-0547-z](https://doi.org/10.1038/s41592-019-0547-z) | 338 | Joint chromatin conformation and DNA methylome from the same single nucleus via bisulfite conversion of 3C libraries. |
| **SNARE-seq** |  | chromatin-accessibility; rna | single-cell | genome-wide | tn5; reverse-transcription; droplet-microfluidics | builds on drop-seq; scatac-seq | Chen S 2019, Nat Biotechnol, [doi:10.1038/s41587-019-0290-0](https://doi.org/10.1038/s41587-019-0290-0) |  | Droplet-based joint profiling of accessibility and transcriptome by capturing tagmented DNA alongside mRNA. |
| **SPRITE** |  | 3d-genome | bulk | genome-wide | split-pool-barcoding |  | Quinodoz SA 2018, Cell, [doi:10.1016/j.cell.2018.05.024](https://doi.org/10.1016/j.cell.2018.05.024) | 890 | Ligation-free mapping of multi-way interactions by split-pool barcoding of crosslinked complexes. |
| **Tiled-MCC** | Tiled Micro-Capture-C | 3d-genome | bulk | targeted | mnase; proximity-ligation; oligo-capture | variant of micro-capture-c | Aljahani A 2022, Nat Commun, [doi:10.1038/s41467-022-29696-5](https://doi.org/10.1038/s41467-022-29696-5) | 120 | Micro-Capture-C with oligos tiled across a whole region, giving all-vs-all contacts within the captured locus. |
| **TOPmentation** | Transcription factor-OPtimized ChIPmentation | protein-dna-binding; histone-modification | bulk | genome-wide | antibody-pull-down; tn5 | variant of chipmentation | Crump NT 2023, Nat Commun, [doi:10.1038/s41467-023-40981-9](https://doi.org/10.1038/s41467-023-40981-9) | 27 | Optimised high-throughput ChIPmentation for weakly bound non-histone proteins from ~100,000 cells. Named only in the Results section. |

## Lineage (parent -> child)

`variant` = child is a direct modification of the parent; `builds on` = child combines or draws on the parent.

- 3c -> 4c-seq (variant)
- dnase-seq -> atac-seq (builds on)
- faire-seq -> atac-seq (builds on)
- 3c -> capture-c (variant)
- 3c -> chia-pet (builds on)
- chip-seq -> chia-pet (builds on)
- chip-seq -> chipmentation (variant)
- atac-seq -> chipmentation (builds on)
- chip-seq -> cut-and-run (builds on)
- cut-and-run -> cut-and-tag (variant)
- atac-seq -> cut-and-tag (builds on)
- single-cell-hi-c -> dip-c (variant)
- single-cell-rna-seq -> drop-seq (variant)
- in-situ-hi-c -> droplet-hi-c (variant)
- snare-seq -> droplet-hi-c (builds on)
- paired-tag -> droplet-paired-tag (variant)
- cut-and-tag -> echos (variant)
- sci-hi-c -> gage-seq (builds on)
- sci-rna-seq -> gage-seq (builds on)
- 3c -> hi-c (variant)
- in-situ-hi-c -> hichip (variant)
- chia-pet -> hichip (builds on)
- chip-seq -> hichip (builds on)
- dip-c -> hires (builds on)
- single-cell-rna-seq -> hires (builds on)
- hi-c -> in-situ-hi-c (variant)
- in-situ-hi-c -> methyl-hic (builds on)
- hi-c -> micro-c (variant)
- capture-c -> micro-capture-c (variant)
- micro-c -> micro-capture-c (variant)
- capture-c -> ng-capture-c (variant)
- droplet-hi-c -> paired-hi-c (variant)
- drop-seq -> paired-hi-c (builds on)
- sci-rna-seq -> paired-seq (builds on)
- sci-atac-seq -> paired-seq (builds on)
- paired-seq -> paired-tag (variant)
- cut-and-tag -> paired-tag (builds on)
- in-situ-hi-c -> plac-seq (variant)
- chia-pet -> plac-seq (builds on)
- chip-seq -> plac-seq (builds on)
- hi-c -> pore-c (builds on)
- micro-c -> rcmc (variant)
- atac-seq -> scatac-seq (variant)
- atac-seq -> sci-atac-seq (variant)
- sci-rna-seq -> sci-car (builds on)
- sci-atac-seq -> sci-car (builds on)
- single-cell-hi-c -> sci-hi-c (variant)
- sci-atac-seq -> sci-hi-c (builds on)
- single-cell-rna-seq -> sci-rna-seq (variant)
- sci-atac-seq -> sci-rna-seq (builds on)
- single-cell-hi-c -> scnanohi-c (builds on)
- pore-c -> scnanohi-c (builds on)
- single-cell-rna-seq -> share-seq (builds on)
- scatac-seq -> share-seq (builds on)
- hi-c -> single-cell-hi-c (variant)
- rna-seq -> single-cell-rna-seq (variant)
- single-cell-hi-c -> sn-m3c-seq (builds on)
- drop-seq -> snare-seq (builds on)
- scatac-seq -> snare-seq (builds on)
- micro-capture-c -> tiled-mcc (variant)
- chipmentation -> topmentation (variant)
