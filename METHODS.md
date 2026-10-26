# Seq-Browser masterlist

Sequencing-based assays, one row per method. Updated 2026-10-26. 204 wet-lab methods.

**For LLMs / tools:** this file is the complete database. Columns use a fixed vocabulary (see `taxonomy.yaml`). `Variant of` gives the parent method's id (lowercase-hyphenated name). Machine-readable copies: `docs/methods.json`, `docs/methods.csv`. Raw URL: https://raw.githubusercontent.com/RobertT4n/Seq-Browser/main/METHODS.md

## Wet-lab methods

| Method | Aliases | Readouts | Resolution | Temporal | Scope | Chemistry | Lineage | Ref | Cites | Summary |
|---|---|---|---|---|---|---|---|---|---|---|
| **10x Chromium 5' Gene Expression** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | variant of 10x-chromium-single-cell-3-gene-expression; builds on strt-seq | [https://support.10xgenomics.com/single-cell-vdj](https://support.10xgenomics.com/single-cell-vdj) |  | 5' transcript profiling with a universal RT primer and barcoded template-switching oligos on the gel beads, so reads start at the transcript 5' end. |
| **10x Chromium 5' Immune Profiling Feature Barcoding** |  | rna; protein | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | variant of 10x-chromium-5-gene-expression; builds on 10x-chromium-single-cell-3-feature-barcoding | [https://support.10xgenomics.com/single-cell-vdj/overview/doc/getting-started-immune-profiling-feature-barcoding](https://support.10xgenomics.com/single-cell-vdj/overview/doc/getting-started-immune-profiling-feature-barcoding) |  | 5' gene expression plus antibody-oligo surface protein tags in one droplet workflow, with V(D)J receptor libraries from the same cells. |
| **10x Chromium Single Cell 3' Feature Barcoding** |  | rna; protein | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on 10x-chromium-single-cell-3-gene-expression; cite-seq | [https://support.10xgenomics.com/single-cell-gene-expression](https://support.10xgenomics.com/single-cell-gene-expression) |  | Antibody-oligo tags captured on the same gel beads as mRNA, giving surface-protein counts per droplet alongside transcriptomes. |
| **10x Chromium Single Cell 3' Gene Expression** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on drop-seq | [https://support.10xgenomics.com/single-cell-gene-expression](https://support.10xgenomics.com/single-cell-gene-expression) |  | Droplet 3' mRNA counting where gel beads carry cell-barcoded, UMI-tagged oligo-dT primers co-encapsulated with each cell. |
| **10x Chromium Single Cell 3' Solution v1** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on drop-seq | Zheng GX 2017, Nat Commun, [doi:10.1038/ncomms14049](https://doi.org/10.1038/ncomms14049) | 7329 | First commercial droplet 3' transcriptome kit, using barcoded gel beads and a microfluidic GemCode device to profile tens of thousands of cells per run. |
| **10x Chromium Single Cell ATAC** | Chromium scATAC | chromatin-accessibility | single-cell |  | genome-wide | tn5; droplet-microfluidics | variant of scatac-seq | Satpathy AT 2019, Nat Biotechnol, [doi:10.1038/s41587-019-0206-z](https://doi.org/10.1038/s41587-019-0206-z) | 979 | Droplet-based scATAC-seq in which nuclei are tagmented in bulk first, then each tagged nucleus is barcoded in a droplet. |
| **10x Chromium Single Cell Multiome ATAC + Gene Expression** |  | chromatin-accessibility; rna | single-cell |  | genome-wide | tn5; reverse-transcription; droplet-microfluidics | builds on 10x-chromium-single-cell-atac; 10x-chromium-single-cell-3-gene-expression | [https://support.10xgenomics.com/single-cell-multiome-atac-gex](https://support.10xgenomics.com/single-cell-multiome-atac-gex) |  | Tn5 tagmentation of nuclei followed by droplet capture of tagged open-chromatin DNA and mRNA on the same beads, giving accessibility and expression per nucleus. |
| **2C-RT** |  | replication-timing | bulk |  | genome-wide | nucleotide-labeling; facs-sorting |  | Urien B 2026, bioRxiv, [doi:10.64898/2026.10.09.758048](https://doi.org/10.64898/2026.10.09.758048) |  | Replication timing from EdU-labelled S-phase cells sorted by a cell-cycle marker and DNA content, with multiplexed EdU-seq. |
| **3C** |  | 3d-genome | bulk |  | targeted | restriction-digest; proximity-ligation |  | Dekker J 2002, Science, [doi:10.1126/science.1067799](https://doi.org/10.1126/science.1067799) | 3648 | Chromosome conformation capture: crosslink, digest and ligate, then quantify ligation between chosen loci. The ancestor of the C-family. |
| **4C-seq** |  | 3d-genome | bulk |  | targeted | restriction-digest; proximity-ligation | variant of 3c | van de Werken HJ 2012, Nat Methods, [doi:10.1038/nmeth.2173](https://doi.org/10.1038/nmeth.2173) | 390 | Inverse-PCR from a single viewpoint to sequence all of its ligation partners (one-vs-all). |
| **ASAP-seq** |  | chromatin-accessibility; protein | single-cell |  | genome-wide | tn5; droplet-microfluidics | builds on scatac-seq; cite-seq | Mimitou EP 2021, Nat Biotechnol, [doi:10.1038/s41587-021-00927-2](https://doi.org/10.1038/s41587-021-00927-2) | 528 | Droplet scATAC-seq combined with antibody-oligo bridging to read surface protein levels from the same single cells. |
| **ASTAR-seq** |  | rna; chromatin-accessibility | single-cell |  | genome-wide | tn5; reverse-transcription | builds on single-cell-rna-seq; scatac-seq | Xing QR 2020, Genome Res, [doi:10.1101/gr.257840.119](https://doi.org/10.1101/gr.257840.119) | 74 | Automated joint profiling of whole-cell transcriptome and chromatin accessibility from the same single cell. |
| **ATAC-seq** |  | chromatin-accessibility | bulk |  | genome-wide | tn5 | builds on dnase-seq; faire-seq | Buenrostro JD 2013, Nat Methods, [doi:10.1038/nmeth.2688](https://doi.org/10.1038/nmeth.2688) | 6415 | Tn5 transposase inserts sequencing adapters into accessible chromatin. |
| **BacDrop** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on drop-seq | Ma P 2023, Cell, [doi:10.1016/j.cell.2023.01.002](https://doi.org/10.1016/j.cell.2023.01.002) | 290 | Droplet-based single-cell RNA-seq for bacteria, using ribosomal RNA depletion and combinatorial barcodes. |
| **BuTT-seq** | Butt-seq | nascent-rna | bulk |  | genome-wide | reverse-transcription |  | Yu AD 2023, Genes Dev, [doi:10.1101/gad.350434.123](https://doi.org/10.1101/gad.350434.123) | 3 | Bulk nascent-transcript sequencing that uses thermostable group II intron reverse transcriptase to join adapter ligation and reverse transcription, giving libraries from as few as 10,000 cells. |
| **Capture-C** |  | 3d-genome | bulk |  | targeted | restriction-digest; proximity-ligation; oligo-capture | variant of 3c | Hughes JR 2014, Nat Genet, [doi:10.1038/ng.2871](https://doi.org/10.1038/ng.2871) | 473 | 3C library enriched with capture oligonucleotides to profile one-vs-all contacts from many viewpoints at once. |
| **CEL-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based | builds on single-cell-rna-seq | Hashimshony T 2012, Cell Rep, [doi:10.1016/j.celrep.2012.08.003](https://doi.org/10.1016/j.celrep.2012.08.003) | 1230 | Cells are barcoded and pooled before one round of in vitro transcription, giving linear rather than exponential mRNA amplification. |
| **CEL-seq2** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based; microfluidic-chip | variant of cel-seq | Hashimshony T 2016, Genome Biol, [doi:10.1186/s13059-016-0938-8](https://doi.org/10.1186/s13059-016-0938-8) | 1124 | Improved CEL-seq with UMIs and random-primed second-strand chemistry, with a Fluidigm C1 on-chip barcoding implementation. |
| **CH-ATAC-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; combinatorial-indexing | variant of sci-atac-seq | Zhang G 2024, Dev Cell, [doi:10.1016/j.devcel.2024.01.015](https://doi.org/10.1016/j.devcel.2024.01.015) | 11 | Combinatorial-indexing scATAC-seq in which the first barcode is added by barcoded Tn5 and later barcodes are added by hybridisation. |
| **ChAIR** |  | 3d-genome; chromatin-accessibility; rna | single-cell |  | genome-wide | restriction-digest; proximity-ligation; tn5; droplet-microfluidics; reverse-transcription | builds on single-cell-hi-c; scatac-seq; single-cell-rna-seq | Chai H 2025, Nat Methods, [doi:10.1038/s41592-025-02658-7](https://doi.org/10.1038/s41592-025-02658-7) | 32 | Droplet-based tri-omic method that captures chromatin accessibility, 3D chromatin contacts and RNA from the same cell by combining restriction digestion, proximity ligation, Tn5 tagmentation and the 10x Multiome system. |
| **ChIA-PET** |  | 3d-genome; protein-dna-binding | bulk |  | genome-wide | antibody-pull-down; proximity-ligation | builds on 3c; chip-seq | Fullwood MJ 2009, Nature, [doi:10.1038/nature08497](https://doi.org/10.1038/nature08497) | 1726 | Chromatin interactions anchored at sites bound by a chosen protein, via ChIP plus paired-end-tag ligation. |
| **ChIP-seq** |  | protein-dna-binding; histone-modification | bulk |  | genome-wide | antibody-pull-down |  | Johnson DS 2007, Science, [doi:10.1126/science.1141319](https://doi.org/10.1126/science.1141319) | 2920 | Chromatin immunoprecipitation followed by sequencing to map protein binding or histone marks genome-wide. |
| **ChIPmentation** |  | histone-modification; protein-dna-binding | bulk |  | genome-wide | antibody-pull-down; tn5 | variant of chip-seq; builds on atac-seq | Schmidl C 2015, Nat Methods, [doi:10.1038/nmeth.3542](https://doi.org/10.1038/nmeth.3542) | 509 | ChIP-seq with Tn5 tagmentation of bead-bound chromatin for fast, low-input library prep. |
| **CITE-seq** |  | protein; rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics |  | Stoeckius M 2017, Nat Methods, [doi:10.1038/nmeth.4380](https://doi.org/10.1038/nmeth.4380) | 3085 | Oligo-barcoded antibodies read out alongside the transcriptome, giving surface-protein and RNA levels per cell. |
| **CoBATCH** |  | histone-modification; protein-dna-binding | single-cell |  | genome-wide | antibody-tethered-enzyme; tn5; combinatorial-indexing | variant of sci-atac-seq; builds on cut-and-tag | Wang Q 2019, Mol Cell, [doi:10.1016/j.molcel.2019.07.015](https://doi.org/10.1016/j.molcel.2019.07.015) | 212 | Antibody-tethered protein A-Tn5 releases indexed chromatin fragments at target sites, then combinatorial barcoding profiles thousands of single cells. |
| **CoTECH** |  | histone-modification; rna | single-cell |  | genome-wide | antibody-tethered-enzyme; combinatorial-indexing; reverse-transcription | builds on cut-and-tag; sci-rna-seq | Xiong H 2021, Nat Methods, [doi:10.1038/s41592-021-01129-z](https://doi.org/10.1038/s41592-021-01129-z) | 100 | Combinatorial barcoding that jointly profiles histone-mark occupancy and transcriptome in the same single cells. |
| **COURIER** | engineered RNA export (Horns 2023); controlled output and uptake of RNA for interrogation, expression, and regulation | rna | bulk | longitudinal-sampling | genome-wide | reverse-transcription |  | Horns F 2023, Cell, [doi:10.1016/j.cell.2023.06.013](https://doi.org/10.1016/j.cell.2023.06.013) | 73 | Genetically encoded viral-inspired RNA exporters package barcoded RNA into nanoparticles that cells secrete, allowing non-destructive sampling of living cell populations over time. |
| **CRISPR-sciATAC** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; combinatorial-indexing | variant of sci-atac-seq; builds on crop-seq | Liscovitch-Brauer N 2021, Nat Biotechnol, [doi:10.1038/s41587-021-00902-x](https://doi.org/10.1038/s41587-021-00902-x) | 107 | Pooled CRISPR perturbations read out by combinatorial-indexing scATAC-seq, linking each guide to chromatin accessibility in the same cell. |
| **CROP-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on drop-seq | Datlinger P 2017, Nat Methods, [doi:10.1038/nmeth.4177](https://doi.org/10.1038/nmeth.4177) | 1093 | Pooled CRISPR screens read out by single-cell RNA-seq, with the guide RNA captured as a polyadenylated transcript. |
| **CUT&RUN** |  | protein-dna-binding; histone-modification | bulk |  | genome-wide | antibody-tethered-enzyme; mnase | builds on chip-seq | Skene PJ 2017, Elife, [doi:10.7554/elife.21856](https://doi.org/10.7554/elife.21856) | 1785 | Antibody-tethered pA-MNase cleaves around bound sites in permeabilised cells; low background, low input. |
| **CUT&Tag** |  | histone-modification; protein-dna-binding | bulk; single-cell |  | genome-wide | antibody-tethered-enzyme; tn5 | variant of cut-and-run; builds on atac-seq | Kaya-Okur HS 2019, Nat Commun, [doi:10.1038/s41467-019-09982-5](https://doi.org/10.1038/s41467-019-09982-5) | 2181 | Antibody-tethered pA-Tn5 tagments only at bound sites in permeabilised cells, giving low-background profiles from few cells. |
| **DamID** |  | protein-dna-binding | bulk |  | genome-wide | restriction-digest |  | van Steensel B 2000, Nat Biotechnol, [doi:10.1038/74487](https://doi.org/10.1038/74487) | 626 | A protein of interest fused to Dam methylase marks the DNA it contacts with adenine methylation, read out by methylation-sensitive digestion. |
| **DBiT-seq** |  | rna; protein | spatial |  | genome-wide | reverse-transcription; microfluidic-chip |  | Liu Y 2020, Cell, [doi:10.1016/j.cell.2020.10.026](https://doi.org/10.1016/j.cell.2020.10.026) | 964 | Spatial co-profiling of mRNAs and proteins in fixed tissue sections using microfluidic crossflow barcoding into a 2D grid of pixels. |
| **ddSEQ Single-Cell 3' RNA-Seq Kit** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics |  | [https://www.bio-rad.com/3scRNA-seq](https://www.bio-rad.com/3scRNA-seq) |  | Bio-Rad droplet 3' scRNA-seq kit for the ddSEQ instrument that uses deconvolution oligos to link beads that share a droplet. |
| **Delley2021** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on drop-seq | Delley CL 2021, Sci Rep, [doi:10.1038/s41598-021-90255-x](https://doi.org/10.1038/s41598-021-90255-x) | 31 | Modular recipe for making multifunctional barcode beads for droplet single-cell assays, with each bead functionalised for the target assay. |
| **Dip-C** |  | 3d-genome | single-cell |  | genome-wide | restriction-digest; proximity-ligation; tn5; plate-based | variant of single-cell-hi-c | Tan L 2018, Science, [doi:10.1126/science.aat5641](https://doi.org/10.1126/science.aat5641) | 498 | Single-cell Hi-C with transposon-based whole-genome amplification and haplotype imputation for diploid 3D structures. |
| **Direct-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription | builds on single-cell-rna-seq; crop-seq | Song Q 2020, Genome Biol, [doi:10.1186/s13059-020-02044-w](https://doi.org/10.1186/s13059-020-02044-w) | 26 | Adds an A/G mixed capture sequence to the gRNA scaffold so guide transcripts are reverse transcribed with mRNA, letting CRISPR perturbation and scRNA-seq readouts be profiled together. |
| **DNase-seq** |  | chromatin-accessibility | bulk |  | genome-wide | dnase-digestion |  | Boyle AP 2008, Cell, [doi:10.1016/j.cell.2007.12.014](https://doi.org/10.1016/j.cell.2007.12.014) | 1415 | DNase I hypersensitive sites sequenced genome-wide to map open chromatin. |
| **DOGMA-seq** |  | rna; chromatin-accessibility; protein | single-cell |  | genome-wide | tn5; reverse-transcription; droplet-microfluidics | variant of asap-seq; builds on cite-seq | Mimitou EP 2021, Nat Biotechnol, [doi:10.1038/s41587-021-00927-2](https://doi.org/10.1038/s41587-021-00927-2) | 528 | Trimodal single-cell profiling of chromatin accessibility, transcriptome and surface protein, extending ASAP-seq onto the 10x Multiome. |
| **DR-seq** |  | rna; dna-sequence | single-cell |  | genome-wide | reverse-transcription | builds on malbac; cel-seq | Dey SS 2015, Nat Biotechnol, [doi:10.1038/nbt.3129](https://doi.org/10.1038/nbt.3129) | 502 | Quasilinear amplification of genomic DNA and mRNA from the same cell, separated only after amplification into a DNA library and an mRNA library. |
| **Drop scChIP-seq** |  | histone-modification | single-cell |  | genome-wide | antibody-pull-down; droplet-microfluidics | builds on chip-seq | Grosselin K 2019, Nat Genet, [doi:10.1038/s41588-019-0424-9](https://doi.org/10.1038/s41588-019-0424-9) | 464 | Droplet microfluidics with DNA barcoding to profile histone-mark chromatin landscapes in thousands of single cells. |
| **Drop-BS** |  | dna-methylation | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion; droplet-microfluidics | variant of scbs-seq | Zhang Q 2023, Nat Commun, [doi:10.1038/s41467-023-40411-w](https://doi.org/10.1038/s41467-023-40411-w) | 28 | Droplet microfluidics encapsulates single cells for bisulfite library construction, profiling DNA methylomes of up to 10,000 cells within about two days. |
| **Drop-ChIP** |  | histone-modification | single-cell |  | genome-wide | antibody-pull-down; droplet-microfluidics | builds on chip-seq; drop-seq | Rotem A 2015, Nat Biotechnol, [doi:10.1038/nbt.3383](https://doi.org/10.1038/nbt.3383) | 853 | Microfluidic droplets barcode antibody-enriched chromatin from individual cells, giving per-cell chromatin state maps. |
| **Drop-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | variant of single-cell-rna-seq | Macosko EZ 2015, Cell, [doi:10.1016/j.cell.2015.05.002](https://doi.org/10.1016/j.cell.2015.05.002) | 7095 | Cells co-encapsulated with barcoded beads in droplets, giving thousands of single-cell transcriptomes per run. |
| **Droplet Hi-C** |  | 3d-genome | single-cell |  | genome-wide | restriction-digest; proximity-ligation; tn5; droplet-microfluidics; facs-sorting | variant of in-situ-hi-c; builds on snare-seq | Chang L 2025, Nat Biotechnol, [doi:10.1038/s41587-024-02447-1](https://doi.org/10.1038/s41587-024-02447-1) | 63 | In situ Hi-C followed by droplet barcoding on a commercial 10x scATAC kit for tens of thousands of cells per run. |
| **Droplet Paired-Tag** |  | histone-modification; rna | single-cell |  | genome-wide | antibody-tethered-enzyme; tn5; droplet-microfluidics; reverse-transcription | variant of paired-tag | Xie Y 2023, Nat Struct Mol Biol, [doi:10.1038/s41594-023-01060-1](https://doi.org/10.1038/s41594-023-01060-1) | 68 | Paired-Tag chemistry moved onto commercial droplet microfluidics for higher throughput and simpler workflow. |
| **dscATAC-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; droplet-microfluidics | builds on scatac-seq | Lareau CA 2019, Nat Biotechnol, [doi:10.1038/s41587-019-0147-6](https://doi.org/10.1038/s41587-019-0147-6) | 443 | Droplet microfluidics scATAC-seq in which Tn5-tagmented fragments from each nucleus are barcoded inside its droplet. |
| **dsciATAC-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; droplet-microfluidics; combinatorial-indexing | variant of dscatac-seq; builds on sci-atac-seq | Lareau CA 2019, Nat Biotechnol, [doi:10.1038/s41587-019-0147-6](https://doi.org/10.1038/s41587-019-0147-6) | 443 | dscATAC-seq combined with combinatorial indexing to scale single-cell chromatin accessibility profiling to very large cell numbers. |
| **easySHARE-seq** |  | chromatin-accessibility; rna | single-cell |  | genome-wide | tn5; reverse-transcription; split-pool-barcoding | variant of share-seq | Soltys V 2026, Elife, [doi:10.7554/elife.110034](https://doi.org/10.7554/elife.110034) |  | Streamlined SHARE-seq with an improved barcode that gives reads up to 300 bp and joint ATAC and RNA profiles per nucleus without a dedicated sequencing run. |
| **ECCITE-seq** |  | rna; protein | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on single-cell-rna-seq; cite-seq | Mimitou EP 2019, Nat Methods, [doi:10.1038/s41592-019-0392-0](https://doi.org/10.1038/s41592-019-0392-0) | 517 | CRISPR-compatible CITE-seq extension that adds guide RNA, TCR/BCR and surface-protein capture to scRNA-seq in the same cells. |
| **ECHOS** | ECHOS+; Epigenetic CUT&Tag via High-resolution Optical Selection | histone-modification; protein-dna-binding | spatial; subcellular |  | genome-wide | antibody-tethered-enzyme; imaging-guided-selection | variant of cut-and-tag | Cao Q 2026, bioRxiv, [doi:10.64898/2026.03.26.714421](https://doi.org/10.64898/2026.03.26.714421) |  | CUT&Tag on optically selected regions of tissue or nuclei, giving spatially targeted epigenomic profiles down to sub-micron scale. |
| **EpiDamID** |  | histone-modification; rna | single-cell |  | genome-wide | antibody-tethered-enzyme; reverse-transcription | builds on scdam-and-t-seq | Rang FJ 2022, Mol Cell, [doi:10.1016/j.molcel.2022.03.009](https://doi.org/10.1016/j.molcel.2022.03.009) | 66 | DamID fused to antibody or reader domains to map histone marks and transcription together in single cells. |
| **FAIRE-seq** | FAIRE | chromatin-accessibility | bulk |  | genome-wide | organic-extraction |  | Giresi PG 2007, Genome Res, [doi:10.1101/gr.5533506](https://doi.org/10.1101/gr.5533506) | 955 | Nucleosome-depleted DNA partitions to the aqueous phase after crosslinking and phenol-chloroform extraction. |
| **FIPRESCI** |  | rna | single-cell |  | genome-wide | reverse-transcription; combinatorial-indexing; droplet-microfluidics | builds on scifi-rna-seq | Li Y 2023, Genome Biol, [doi:10.1186/s13059-023-02893-1](https://doi.org/10.1186/s13059-023-02893-1) | 23 | Droplet-based 5'-end scRNA-seq that adds combinatorial sample indexing to the droplet system to multiplex very large numbers of cells. |
| **FLASH-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based | variant of smart-seq3 | Hahaut V 2022, Nat Biotechnol, [doi:10.1038/s41587-022-01312-3](https://doi.org/10.1038/s41587-022-01312-3) | 143 | Shortened full-length scRNA-seq protocol derived from Smart-seq3 that removes intermediate purifications for faster, more sensitive libraries. |
| **G&T-seq** |  | rna; dna-sequence | single-cell |  | genome-wide | reverse-transcription; oligo-capture | builds on smart-seq2; malbac | Macaulay IC 2015, Nat Methods, [doi:10.1038/nmeth.3370](https://doi.org/10.1038/nmeth.3370) | 750 | Physically separates mRNA from genomic DNA in each single cell so the genome and transcriptome of the same cell can be sequenced. |
| **GAGE-seq** |  | 3d-genome; rna | single-cell |  | genome-wide | restriction-digest; proximity-ligation; combinatorial-indexing; reverse-transcription | builds on sci-hi-c; sci-rna-seq | Zhou T 2024, Nat Genet, [doi:10.1038/s41588-024-01745-3](https://doi.org/10.1038/s41588-024-01745-3) | 70 | Combinatorial-indexing joint profiling of chromatin conformation and transcriptome in single cells. |
| **GAM** | Genome Architecture Mapping | 3d-genome | bulk |  | genome-wide | cryosectioning |  | Beagrie RA 2017, Nature, [doi:10.1038/nature21411](https://doi.org/10.1038/nature21411) | 715 | Ligation-free co-segregation mapping from sequencing thin nuclear cryosections. |
| **GoT** | Genotyping of Transcriptomes | rna; dna-sequence | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on drop-seq | Nam AS 2019, Nature, [doi:10.1038/s41586-019-1367-0](https://doi.org/10.1038/s41586-019-1367-0) | 330 | Targeted amplification of mutation sites from droplet scRNA-seq cDNA links somatic genotype to transcriptional state per cell. |
| **GoT-ChA** |  | chromatin-accessibility; dna-sequence | single-cell |  | targeted | tn5; droplet-microfluidics | builds on scatac-seq; got | Izzo F 2024, Nature, [doi:10.1038/s41586-024-07388-y](https://doi.org/10.1038/s41586-024-07388-y) | 61 | Genotyping of targeted loci alongside single-cell chromatin accessibility, linking somatic mutations to chromatin state. |
| **GRID-seq** |  | rna; 3d-genome | bulk |  | genome-wide | proximity-ligation; reverse-transcription | builds on rna-seq; hi-c | Li X 2017, Nat Biotechnol, [doi:10.1038/nbt.3968](https://doi.org/10.1038/nbt.3968) | 308 | In situ ligation of RNA to adjacent chromatin DNA followed by sequencing, mapping the genome-wide RNA-chromatin interactome. |
| **Hi-C** |  | 3d-genome | bulk |  | genome-wide | restriction-digest; proximity-ligation | variant of 3c | Lieberman-Aiden E 2009, Science, [doi:10.1126/science.1181369](https://doi.org/10.1126/science.1181369) | 8882 | Genome-wide all-vs-all chromatin contact mapping by restriction digest, biotin fill-in and proximity ligation. |
| **HiChIP** |  | 3d-genome; protein-dna-binding | bulk |  | genome-wide | restriction-digest; proximity-ligation; antibody-pull-down; tn5 | variant of in-situ-hi-c; builds on chia-pet; chip-seq | Mumbach MR 2016, Nat Methods, [doi:10.1038/nmeth.3999](https://doi.org/10.1038/nmeth.3999) | 1131 | In situ Hi-C followed by ChIP and Tn5 library prep to enrich protein-anchored contacts from low input. |
| **HiRES** |  | 3d-genome; rna | single-cell |  | genome-wide | restriction-digest; proximity-ligation; tn5; plate-based; reverse-transcription | builds on dip-c; single-cell-rna-seq | Liu Z 2023, Science, [doi:10.1126/science.adg3797](https://doi.org/10.1126/science.adg3797) | 172 | Simultaneous single-cell Hi-C and RNA-seq from the same cell. |
| **Hybrid BAG-seq** | BAG DNA RNA | dna-sequence; rna | single-cell |  | genome-wide | reverse-transcription |  | Li S 2025, Genome Biol, [doi:10.1186/s13059-025-03790-5](https://doi.org/10.1186/s13059-025-03790-5) | 2 | High-throughput multi-omic method that captures genomic DNA and transcripts from the same single nucleus, allowing genome-transcriptome correlation in tumours. |
| **HyDrop-ATAC** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; droplet-microfluidics | builds on indrop; scatac-seq | De Rop FV 2022, Elife, [doi:10.7554/eLife.73971](https://doi.org/10.7554/eLife.73971) | 69 | Low-cost droplet scATAC-seq in which custom-oligo hydrogel beads are released into droplets to barcode Tn5-tagged open chromatin. |
| **HyDrop-RNA** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on drop-seq; indrop | De Rop FV 2022, Elife, [doi:10.7554/eLife.73971](https://doi.org/10.7554/eLife.73971) | 69 | Droplet scRNA-seq that adapts the dissolvable hydrogel-bead chemistry and capture sequence to capture mRNA, improving on Drop-seq and inDrop. |
| **Illumina Bio-Rad SureCell 3' WTA for ddSEQ** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics |  | [https://support.illumina.com/sequencing/sequencing_kits/surecell-wta-3-kit.html](https://support.illumina.com/sequencing/sequencing_kits/surecell-wta-3-kit.html) |  | Commercial droplet-based 3' whole-transcriptome kit for the Bio-Rad ddSEQ instrument; discontinued by the vendor. |
| **in situ Hi-C** |  | 3d-genome | bulk |  | genome-wide | restriction-digest; proximity-ligation | variant of hi-c | Rao SS 2014, Cell, [doi:10.1016/j.cell.2014.11.021](https://doi.org/10.1016/j.cell.2014.11.021) | 9199 | Hi-C with digestion and ligation performed in intact nuclei, giving kilobase-resolution maps and loop calls. |
| **inDrop** |  | rna | single-cell |  | genome-wide | droplet-microfluidics; reverse-transcription |  | Klein AM 2015, Cell, [doi:10.1016/j.cell.2015.04.044](https://doi.org/10.1016/j.cell.2015.04.044) | 3354 | Barcoded beads co-encapsulated with single cells in droplets tag each cell's mRNA for transcriptome sequencing. |
| **inDrops-2** |  | rna | single-cell |  | genome-wide | droplet-microfluidics; reverse-transcription | variant of indrop | Juzenas S 2025, Nucleic Acids Res, [doi:10.1093/nar/gkae1312](https://doi.org/10.1093/nar/gkae1312) | 16 | Open-source, lower-cost version of inDrops that profiles fresh or preserved cells with exponential or linear amplification of barcoded cDNA. |
| **ISSAAC-seq** |  | chromatin-accessibility; rna | single-cell |  | genome-wide | tn5; reverse-transcription |  | Xu W 2022, Nat Methods, [doi:10.1038/s41592-022-01601-4](https://doi.org/10.1038/s41592-022-01601-4) | 114 | Joint single-cell chromatin accessibility and gene expression profiling in which Tn5 tags open chromatin and RNA-cDNA hybrids are sequenced in situ. |
| **itChIP-seq** |  | histone-modification; protein-dna-binding | single-cell |  | genome-wide | antibody-pull-down; tn5; combinatorial-indexing | builds on chipmentation; sci-atac-seq | Ai S 2019, Nat Cell Biol, [doi:10.1038/s41556-019-0383-5](https://doi.org/10.1038/s41556-019-0383-5) | 140 | Chromatin opening, cell indexing and tagmentation are done in one tube, so ChIP-seq can profile histone marks in single cells. |
| **LAST-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription |  | Lyu J 2023, Genome Biol, [doi:10.1186/s13059-023-03025-5](https://doi.org/10.1186/s13059-023-03025-5) | 11 | Single-cell RNA-seq that linearly amplifies single-stranded RNA by T7 in vitro transcription, skipping reverse transcription and second-strand synthesis before amplification. |
| **LIANTI** |  | dna-sequence | single-cell |  | genome-wide | tn5 |  | Chen C 2017, Science, [doi:10.1126/science.aak9787](https://doi.org/10.1126/science.aak9787) | 391 | Single-cell whole-genome amplification using transposon insertion and linear amplification, giving kilobase-resolution copy-number profiles. |
| **LiMCA** | Linking mRNA to Chromatin Architecture | 3d-genome; rna | single-cell |  | genome-wide | restriction-digest; proximity-ligation; reverse-transcription | builds on hires; smart-seq2 | Wu H 2024, Nat Methods, [doi:10.1038/s41592-024-02239-0](https://doi.org/10.1038/s41592-024-02239-0) | 81 | Joint single-cell 3D genome and transcriptome profiling from low input, combining a Hi-C style conformation capture with RNA capture from the same cell. |
| **Live-seq** |  | rna | single-cell | longitudinal-sampling | genome-wide | reverse-transcription | builds on single-cell-rna-seq | Chen W 2022, Nature, [doi:10.1038/s41586-022-05046-9](https://doi.org/10.1038/s41586-022-05046-9) | 247 | Fluidic force microscopy extracts cytoplasm from a living cell for RNA-seq while the cell survives, so the same cell can be sampled repeatedly over time. |
| **M3-seq** |  | rna | single-cell |  | genome-wide | combinatorial-indexing; plate-based; reverse-transcription | builds on sci-rna-seq | Wang B 2023, Nat Microbiol, [doi:10.1038/s41564-023-01462-3](https://doi.org/10.1038/s41564-023-01462-3) | 98 | Single-cell RNA-seq for bacteria that combines in situ reverse transcription with combinatorial plate indexing and post hoc rRNA depletion. |
| **MALBAC** |  | dna-sequence | single-cell |  | genome-wide | plate-based |  | Zong C 2012, Science, [doi:10.1126/science.1229164](https://doi.org/10.1126/science.1229164) | 1153 | Single-cell whole-genome amplification using multiple annealing and looping cycles to give uniform genome coverage from one cell. |
| **MALBAC-DT** |  | rna | single-cell |  | genome-wide | reverse-transcription | builds on malbac | Chapman AR 2022, Proc Natl Acad Sci U S A, [doi:10.1073/pnas.2206938119](https://doi.org/10.1073/pnas.2206938119) | 27 | High-precision single-cell RNA-seq used to measure gene-gene expression correlations from steady-state fluctuations within a population. |
| **MARS-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based; facs-sorting | builds on cel-seq | Jaitin DA 2014, Science, [doi:10.1126/science.1247651](https://doi.org/10.1126/science.1247651) | 1793 | Massively parallel scRNA-seq of FACS-sorted cells in barcoded plate wells, used to decompose tissues into cell types without markers. |
| **MARS-seq2.0** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based; facs-sorting | variant of mars-seq | Keren-Shaul H 2019, Nat Protoc, [doi:10.1038/s41596-019-0164-4](https://doi.org/10.1038/s41596-019-0164-4) | 291 | Indexed FACS sorting combined with an optimized MARS-seq chemistry using sub-microliter reactions and an error-correcting analysis pipeline. |
| **MATQ-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription | builds on single-cell-rna-seq | Sheng K 2017, Nat Methods, [doi:10.1038/nmeth.4145](https://doi.org/10.1038/nmeth.4145) | 255 | Multiple annealing and dC-tailing based single-cell RNA-seq of total RNA, designed for quantitative low-noise capture. |
| **mcSCRB-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based | variant of scrb-seq | Bagnoli JW 2018, Nat Commun, [doi:10.1038/s41467-018-05347-6](https://doi.org/10.1038/s41467-018-05347-6) | 255 | SCRB-seq with polyethylene glycol molecular crowding and Terra polymerase for higher sensitivity and more even cDNA amplification. |
| **Methyl-HiC** |  | 3d-genome; dna-methylation | bulk; single-cell |  | genome-wide | restriction-digest; proximity-ligation; bisulfite-or-enzymatic-conversion | builds on in-situ-hi-c; wgbs | Li G 2019, Nat Methods, [doi:10.1038/s41592-019-0502-z](https://doi.org/10.1038/s41592-019-0502-z) | 229 | In situ Hi-C combined with bisulfite conversion to read contacts and methylation together. |
| **Micro-C** |  | 3d-genome | bulk |  | genome-wide | mnase; proximity-ligation | variant of hi-c | Hsieh TH 2015, Cell, [doi:10.1016/j.cell.2015.05.048](https://doi.org/10.1016/j.cell.2015.05.048) | 785 | Hi-C variant using MNase instead of restriction enzymes for nucleosome-resolution contact maps. |
| **Micro-Capture-C** | MCC | 3d-genome | bulk |  | targeted | mnase; proximity-ligation; oligo-capture | variant of capture-c; micro-c | Hua P 2021, Nature, [doi:10.1038/s41586-021-03639-4](https://doi.org/10.1038/s41586-021-03639-4) | 186 | MNase-based Capture-C with ligation junctions read directly, giving near base-pair resolution one-vs-all contact profiles. |
| **Microbe-seq** |  | dna-sequence | single-cell |  | genome-wide | droplet-microfluidics |  | Zheng W 2022, Science, [doi:10.1126/science.abm1483](https://doi.org/10.1126/science.abm1483) | 283 | Single microbes are encapsulated in droplets, their genomes amplified and barcoded, then sequenced to recover strain-resolved genomes. |
| **microSPLiT** |  | rna | single-cell |  | genome-wide | reverse-transcription; split-pool-barcoding | variant of split-seq | Kuchina A 2021, Science, [doi:10.1126/science.aba5257](https://doi.org/10.1126/science.aba5257) | 340 | Bacterial version of SPLiT-seq that uses split-pool barcoding to profile transcriptional states of individual Gram-negative and Gram-positive bacteria. |
| **Microwell-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; microfluidic-chip |  | Han X 2018, Cell, [doi:10.1016/j.cell.2018.02.001](https://doi.org/10.1016/j.cell.2018.02.001) | 1597 | High-throughput, low-cost scRNA-seq that captures single-cell transcriptomes in simple microwell arrays, used to build a mouse cell atlas. |
| **MNase-seq** |  | chromatin-accessibility | bulk |  | genome-wide | mnase |  | Schones DE 2008, Cell, [doi:10.1016/j.cell.2008.02.022](https://doi.org/10.1016/j.cell.2008.02.022) | 1396 | Micrococcal nuclease digests linker DNA; sequencing protected fragments maps nucleosome positions genome-wide. |
| **Multi-CUT&Tag** |  | histone-modification; protein-dna-binding | bulk; single-cell |  | genome-wide | antibody-tethered-enzyme; tn5 | variant of cut-and-tag | Gopalan S 2021, Mol Cell, [doi:10.1016/j.molcel.2021.09.019](https://doi.org/10.1016/j.molcel.2021.09.019) | 111 | CUT&Tag with antibody-specific barcodes so several chromatin proteins are mapped in the same cells, in bulk or single-cell format. |
| **MulTI-Tag** |  | histone-modification | single-cell |  | genome-wide | antibody-tethered-enzyme; tn5 | builds on cut-and-tag | Meers MP 2023, Nat Biotechnol, [doi:10.1038/s41587-022-01522-9](https://doi.org/10.1038/s41587-022-01522-9) | 107 | Antibody-barcoding CUT&Tag-type assay that maps several histone marks simultaneously in single cells. |
| **NASC-seq** |  | rna | single-cell | metabolic-labeling | genome-wide | nucleotide-labeling; reverse-transcription | builds on single-cell-rna-seq | Hendriks GJ 2019, Nat Commun, [doi:10.1038/s41467-019-11028-9](https://doi.org/10.1038/s41467-019-11028-9) | 117 | Single-cell RNA-seq using alkylation of newly synthesized RNA to distinguish new from pre-existing transcripts in the same cell. |
| **NG Capture-C** | Next-Generation Capture-C | 3d-genome | bulk |  | targeted | restriction-digest; proximity-ligation; oligo-capture | variant of capture-c | Davies JO 2016, Nat Methods, [doi:10.1038/nmeth.3664](https://doi.org/10.1038/nmeth.3664) | 267 | Capture-C with double capture and multiplexing for much higher sensitivity per viewpoint. |
| **NOMe-seq** |  | chromatin-accessibility; dna-methylation | bulk |  | genome-wide | bisulfite-or-enzymatic-conversion | builds on wgbs | Kelly TK 2012, Genome Res, [doi:10.1101/gr.143008.112](https://doi.org/10.1101/gr.143008.112) | 453 | GpC methyltransferase footprints accessible DNA, then bisulfite sequencing reads accessibility and endogenous CpG methylation together. |
| **NTT-seq** |  | histone-modification; protein-dna-binding; protein | bulk; single-cell |  | genome-wide | tn5; antibody-tethered-enzyme | builds on cut-and-tag; cite-seq | Stuart T 2023, Nat Biotechnol, [doi:10.1038/s41587-022-01588-5](https://doi.org/10.1038/s41587-022-01588-5) | 93 | Nanobody-tethered Tn5 that binds primary antibodies against several histone marks or DNA-binding proteins, mapping multiple chromatin features in one assay, in bulk or single cells. |
| **Paired Hi-C** |  | 3d-genome; rna | single-cell |  | genome-wide | restriction-digest; proximity-ligation; tn5; droplet-microfluidics; facs-sorting; reverse-transcription | variant of droplet-hi-c; builds on drop-seq | Chang L 2025, Nat Biotechnol, [doi:10.1038/s41587-024-02447-1](https://doi.org/10.1038/s41587-024-02447-1) | 63 | Droplet Hi-C adapted to the 10x Multiome kit to profile chromatin conformation and transcriptome from the same nucleus. Introduced in the Results section, not the abstract. |
| **Paired-seq** |  | chromatin-accessibility; rna | single-cell |  | genome-wide | tn5; combinatorial-indexing; reverse-transcription | builds on sci-rna-seq; sci-atac-seq | Zhu C 2019, Nat Struct Mol Biol, [doi:10.1038/s41594-019-0323-x](https://doi.org/10.1038/s41594-019-0323-x) | 343 | Combinatorial-indexing joint profiling of chromatin accessibility and transcriptome in single nuclei. |
| **Paired-Tag** |  | histone-modification; rna | single-cell |  | genome-wide | antibody-tethered-enzyme; tn5; combinatorial-indexing; reverse-transcription | variant of paired-seq; builds on cut-and-tag | Zhu C 2021, Nat Methods, [doi:10.1038/s41592-021-01060-3](https://doi.org/10.1038/s41592-021-01060-3) | 300 | Antibody-guided Tn5 tagmentation plus combinatorial indexing for joint histone-mark and transcriptome profiles per nucleus. |
| **PETRI-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; combinatorial-indexing | builds on sci-rna-seq; split-seq | Blattman SB 2020, Nat Microbiol, [doi:10.1038/s41564-020-0729-6](https://doi.org/10.1038/s41564-020-0729-6) | 221 | Prokaryotic scRNA-seq that uses in situ combinatorial indexing to barcode transcripts from tens of thousands of bacterial cells in one experiment. |
| **PHAGE-ATAC** |  | chromatin-accessibility; protein | single-cell |  | genome-wide | tn5; droplet-microfluidics | builds on scatac-seq; cite-seq | Fiskin E 2022, Nat Biotechnol, [doi:10.1038/s41587-021-01065-5](https://doi.org/10.1038/s41587-021-01065-5) | 68 | Droplet scATAC-seq in which phage-displayed nanobodies carry barcodes to report surface or intracellular protein alongside accessibility. |
| **Phospho-seq** |  | protein; chromatin-accessibility | single-cell |  | genome-wide | tn5; droplet-microfluidics | builds on scatac-seq; cite-seq | Blair JD 2025, Nat Commun, [doi:10.1038/s41467-025-56590-7](https://doi.org/10.1038/s41467-025-56590-7) | 26 | Antibody-based profiling of intracellular and phosphorylated proteins alongside scATAC-seq in the same single cells, using DNA-conjugated antibodies. |
| **Pi-ATAC** | Protein-indexed ATAC-seq; piATAC-seq | chromatin-accessibility; protein | single-cell |  | genome-wide | tn5; facs-sorting | builds on scatac-seq | Chen X 2018, Nat Commun, [doi:10.1038/s41467-018-07115-y](https://doi.org/10.1038/s41467-018-07115-y) | 80 | Index flow cytometry records surface and intracellular protein levels per cell, which are then barcoded alongside chromatin accessibility. |
| **PIP-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based |  | Clark IC 2023, Nat Biotechnol, [doi:10.1038/s41587-023-01685-z](https://doi.org/10.1038/s41587-023-01685-z) | 223 | Particle-templated emulsification encapsulates single cells and barcodes cDNA in uniform droplets with only a vortexer, avoiding microfluidic hardware. |
| **PLAC-seq** |  | 3d-genome; protein-dna-binding | bulk |  | genome-wide | restriction-digest; proximity-ligation; antibody-pull-down | variant of in-situ-hi-c; builds on chia-pet; chip-seq | Fang R 2016, Cell Res, [doi:10.1038/cr.2016.137](https://doi.org/10.1038/cr.2016.137) | 343 | Proximity ligation in nuclei followed by ChIP to capture contacts anchored at marked or bound regions. |
| **plate-scATAC-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; facs-sorting; plate-based | builds on atac-seq | Chen X 2018, Nat Commun, [doi:10.1038/s41467-018-07771-0](https://doi.org/10.1038/s41467-018-07771-0) | 1147 | Tn5 tagmentation of a cell pool, then single nuclei are sorted into plates, giving scATAC-seq with no per-cell barcoding chemistry. |
| **Pore-C** |  | 3d-genome | bulk |  | genome-wide | restriction-digest; proximity-ligation; long-read-sequencing | builds on hi-c | Deshpande AS 2022, Nat Biotechnol, [doi:10.1038/s41587-022-01289-z](https://doi.org/10.1038/s41587-022-01289-z) | 157 | Chromatin conformation capture with nanopore reads of full concatemers, capturing multi-way contacts. |
| **ProBac-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; droplet-microfluidics | builds on single-cell-rna-seq | McNulty R 2023, Nat Microbiol, [doi:10.1038/s41564-023-01348-4](https://doi.org/10.1038/s41564-023-01348-4) | 117 | Hybridises mRNA-specific oligonucleotide probe libraries to bacterial cells, then encapsulates them in droplets for single-cell bacterial transcriptome sequencing. |
| **Quartz-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription |  | Sasagawa Y 2013, Genome Biol, [doi:10.1186/gb-2013-14-4-r31](https://doi.org/10.1186/gb-2013-14-4-r31) | 455 | Simpler, reproducible and sensitive single-cell RNA-seq method that reveals non-genetic gene-expression heterogeneity. |
| **Quartz-seq2** |  | rna | single-cell |  | genome-wide | reverse-transcription | variant of quartz-seq | Sasagawa Y 2018, Genome Biol, [doi:10.1186/s13059-018-1407-3](https://doi.org/10.1186/s13059-018-1407-3) | 135 | High-throughput version of Quartz-seq with improved reaction steps that convert a larger share of shallow reads into UMI counts. |
| **RamDA-seq** | random displacement amplification sequencing | rna | single-cell |  | genome-wide | reverse-transcription |  | Hayashi T 2018, Nat Commun, [doi:10.1038/s41467-018-02866-0](https://doi.org/10.1038/s41467-018-02866-0) | 292 | First full-length total RNA sequencing method for single cells, capturing non-poly(A) RNA with random-primed reverse transcription and displacement amplification. |
| **RCMC** | Region Capture Micro-C | 3d-genome | bulk |  | targeted | mnase; proximity-ligation; oligo-capture | variant of micro-c | Goel VY 2023, Nat Genet, [doi:10.1038/s41588-023-01391-1](https://doi.org/10.1038/s41588-023-01391-1) | 271 | Micro-C library enriched for selected regions, giving deep all-vs-all contact maps within them. |
| **RNA-seq** |  | rna | bulk |  | genome-wide | reverse-transcription |  | Mortazavi A 2008, Nat Methods, [doi:10.1038/nmeth.1226](https://doi.org/10.1038/nmeth.1226) | 13695 | High-throughput sequencing of cDNA to quantify the transcriptome. |
| **s3-ATAC** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; combinatorial-indexing | builds on sci-atac-seq | Mulqueen RM 2021, Nat Biotechnol, [doi:10.1038/s41587-021-00962-z](https://doi.org/10.1038/s41587-021-00962-z) | 98 | Uracil-based symmetrical-strand adapter switching makes combinatorial-indexed transposase libraries yield far more usable reads per cell. |
| **s3-WGS** |  | dna-sequence | single-cell |  | genome-wide | tn5; combinatorial-indexing | builds on s3-atac | Mulqueen RM 2021, Nat Biotechnol, [doi:10.1038/s41587-021-00962-z](https://doi.org/10.1038/s41587-021-00962-z) | 98 | Applies the s3 uracil-based adapter switching to single-cell whole-genome sequencing for copy-number and subclonal profiling. |
| **sc-end5-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription | builds on single-cell-rna-seq | Moody J 2021, bioRxiv, [doi:10.1101/2021.04.04.438388](https://doi.org/10.1101/2021.04.04.438388) | 3 | Single-cell RNA 5-prime-end sequencing that also detects transcribed enhancers and promoters from the same reads. |
| **scATAC-seq** | single-cell ATAC-seq | chromatin-accessibility | single-cell |  | genome-wide | tn5; microfluidic-chip | variant of atac-seq | Buenrostro JD 2015, Nature, [doi:10.1038/nature14590](https://doi.org/10.1038/nature14590) | 2303 | ATAC-seq performed on individual cells captured in microfluidic chambers. |
| **scBS-seq** | single-cell bisulfite sequencing | dna-methylation | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion; plate-based; facs-sorting | variant of wgbs | Smallwood SA 2014, Nat Methods, [doi:10.1038/nmeth.3035](https://doi.org/10.1038/nmeth.3035) | 1125 | Post-bisulfite adaptor tagging to profile genome-wide DNA methylation in single cells. |
| **scCARE-seq** |  | 3d-genome; rna | single-cell |  | genome-wide | restriction-digest; proximity-ligation; reverse-transcription |  | Qu J 2023, Nat Struct Mol Biol, [doi:10.1038/s41594-023-01066-9](https://doi.org/10.1038/s41594-023-01066-9) | 38 | Single-cell method that jointly captures chromatin conformation and mRNA from the same cell by sequencing. |
| **scCAT-seq** |  | chromatin-accessibility; rna | single-cell |  | genome-wide | tn5; reverse-transcription; facs-sorting; plate-based | builds on smart-seq2; scatac-seq | Liu L 2019, Nat Commun, [doi:10.1038/s41467-018-08205-7](https://doi.org/10.1038/s41467-018-08205-7) | 243 | Nuclei are tagmented for chromatin accessibility while the cytoplasm is amplified with Smart-seq2, giving both layers from one cell. |
| **scCOOL-seq** | single-cell COOL-seq | chromatin-accessibility; dna-methylation; dna-sequence | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion | builds on scnome-seq; scbs-seq | Guo F 2017, Cell Res, [doi:10.1038/cr.2017.82](https://doi.org/10.1038/cr.2017.82) | 374 | Measures chromatin state, DNA methylation and copy number from the same single cell, building on the NOMe and bisulfite single-cell approaches. |
| **scDam&T-seq** |  | protein-dna-binding; rna | single-cell |  | genome-wide | restriction-digest; reverse-transcription; facs-sorting; plate-based | variant of scdamid; builds on cel-seq2 | Rooijers K 2019, Nat Biotechnol, [doi:10.1038/s41587-019-0150-y](https://doi.org/10.1038/s41587-019-0150-y) | 110 | Adds mRNA sequencing to scDamID in the same sorted cell, so protein-DNA contacts and transcription are measured together. |
| **scDamID** |  | 3d-genome; protein-dna-binding | single-cell |  | genome-wide | restriction-digest; facs-sorting; plate-based | variant of damid | Kind J 2015, Cell, [doi:10.1016/j.cell.2015.08.040](https://doi.org/10.1016/j.cell.2015.08.040) | 482 | Dam methyltransferase fused to a lamina protein methylates GATC sites in sorted single cells, mapping nuclear-lamina contacts per cell. |
| **scDNase-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | dnase-digestion | variant of dnase-seq | Jin W 2015, Nature, [doi:10.1038/nature15740](https://doi.org/10.1038/nature15740) | 331 | DNase I digestion of single cells with carrier-DNA-assisted library prep maps genome-wide DNase hypersensitive sites in individual cells. |
| **scEU-seq** |  | rna | single-cell | metabolic-labeling | genome-wide | nucleotide-labeling; reverse-transcription | builds on single-cell-rna-seq | Battich N 2020, Science, [doi:10.1126/science.aax3072](https://doi.org/10.1126/science.aax3072) | 176 | Single-cell RNA-seq that labels nascent transcripts with 5-ethynyluridine and separates labeled from preexisting mRNA to measure synthesis and degradation. |
| **scGET-seq** |  | chromatin-accessibility; histone-modification; dna-sequence | single-cell |  | genome-wide | tn5 | variant of scatac-seq | Tedesco M 2022, Nat Biotechnol, [doi:10.1038/s41587-021-01031-1](https://doi.org/10.1038/s41587-021-01031-1) | 117 | Single-cell hybrid transposase (Tn5 fused to a H3K9me3-binding chromodomain) that profiles open and closed chromatin plus the genomic sequence in one assay. |
| **sci-ATAC-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; combinatorial-indexing | variant of atac-seq | Cusanovich DA 2015, Science, [doi:10.1126/science.aab1601](https://doi.org/10.1126/science.aab1601) | 1247 | First combinatorial-indexing single-cell method: barcoded Tn5 plus PCR indexing across plates. |
| **sci-ATAC-seq3** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; split-pool-barcoding; combinatorial-indexing | variant of sci-atac-seq | Domcke S 2020, Science, [doi:10.1126/science.aba7612](https://doi.org/10.1126/science.aba7612) | 405 | Three-level combinatorial indexing in which barcodes are added by split-pool ligation, so standard Tn5 can be used instead of indexed Tn5. |
| **sci-CAR** |  | chromatin-accessibility; rna | single-cell |  | genome-wide | tn5; reverse-transcription; combinatorial-indexing | builds on sci-rna-seq; sci-atac-seq | Cao J 2018, Science, [doi:10.1126/science.aau0730](https://doi.org/10.1126/science.aau0730) | 935 | Combinatorial indexing for joint chromatin accessibility and transcriptome from the same cells. |
| **sci-fate** |  | rna | single-cell | metabolic-labeling | genome-wide | nucleotide-labeling; combinatorial-indexing; reverse-transcription | variant of sci-rna-seq | Cao J 2020, Nat Biotechnol, [doi:10.1038/s41587-020-0480-9](https://doi.org/10.1038/s41587-020-0480-9) | 172 | Combinatorial-indexing single-cell RNA-seq combined with 4-thiouridine labeling to profile whole and newly synthesized transcriptomes in many cells. |
| **sci-Hi-C** |  | 3d-genome | single-cell |  | genome-wide | restriction-digest; proximity-ligation; combinatorial-indexing | variant of single-cell-hi-c; builds on sci-atac-seq | Ramani V 2017, Nat Methods, [doi:10.1038/nmeth.4155](https://doi.org/10.1038/nmeth.4155) | 548 | Single-cell Hi-C scaled to thousands of cells by combinatorial cellular indexing. |
| **sci-Plex** |  | rna | single-cell |  | genome-wide | reverse-transcription; combinatorial-indexing | variant of sci-rna-seq3 | Srivatsan SR 2020, Science, [doi:10.1126/science.aax6234](https://doi.org/10.1126/science.aax6234) | 398 | Nuclear hashing of sci-RNA-seq libraries to multiplex thousands of chemical perturbations in one single-cell experiment. |
| **sci-RNA-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; combinatorial-indexing | variant of single-cell-rna-seq; builds on sci-atac-seq | Cao J 2017, Science, [doi:10.1126/science.aam8940](https://doi.org/10.1126/science.aam8940) | 1402 | Single-cell transcriptomes by combinatorial cellular indexing, no physical isolation of cells. |
| **sci-RNA-seq3** |  | rna | single-cell |  | genome-wide | reverse-transcription; combinatorial-indexing | variant of sci-rna-seq | Cao J 2019, Nature, [doi:10.1038/s41586-019-0969-x](https://doi.org/10.1038/s41586-019-0969-x) | 4465 | Three-level combinatorial indexing (RT, ligation, PCR) scaling sci-RNA-seq to millions of cells. |
| **scifi-ATAC-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; combinatorial-indexing; droplet-microfluidics | builds on 10x-chromium-single-cell-atac; sci-atac-seq | Zhang X 2024, Genome Biol, [doi:10.1186/s13059-024-03235-5](https://doi.org/10.1186/s13059-024-03235-5) | 30 | Barcoded Tn5 pre-indexing of nuclei before 10x droplet capture, multiplying scATAC throughput about 20-fold. |
| **scifi-RNA-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; combinatorial-indexing; droplet-microfluidics | builds on sci-rna-seq; 10x-chromium-single-cell-3-gene-expression | Datlinger P 2021, Nat Methods, [doi:10.1038/s41592-021-01153-z](https://doi.org/10.1038/s41592-021-01153-z) | 270 | Combinatorial preindexing of permeabilized cells before droplet scRNA-seq, so several cells per droplet are demultiplexed computationally. |
| **sciPlex-ATAC-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; combinatorial-indexing | builds on sci-atac-seq | Booth GT 2023, BMC Genomics, [doi:10.1186/s12864-023-09832-1](https://doi.org/10.1186/s12864-023-09832-1) | 6 | Combinatorial-indexing scATAC-seq in which unmodified DNA oligo hashes label each sample's nuclei, allowing many specimens to be pooled in one run. |
| **SCITO-seq** |  | protein; rna | single-cell |  | genome-wide | droplet-microfluidics; combinatorial-indexing; reverse-transcription | builds on cite-seq | Hwang B 2021, Nat Methods, [doi:10.1038/s41592-021-01222-3](https://doi.org/10.1038/s41592-021-01222-3) | 63 | Splint-oligo combinatorial indexing of DNA-barcoded antibodies on commercial microfluidics, giving high-throughput protein profiles and optional transcriptome co-profiling. |
| **scMNase-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | mnase; facs-sorting | variant of mnase-seq | Gao W 2020, Nat Protoc, [doi:10.1038/s41596-019-0243-6](https://doi.org/10.1038/s41596-019-0243-6) | 26 | MNase digests FACS-sorted single cells; sub-nucleosome fragments report accessibility and mononucleosome fragments report nucleosome positions. |
| **scMT-seq** |  | rna; dna-methylation | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion; reverse-transcription | builds on smart-seq2; scrrbs | Hu Y 2016, Genome Biol, [doi:10.1186/s13059-016-0950-z](https://doi.org/10.1186/s13059-016-0950-z) | 300 | The cytoplasm is separated from the nucleus; Smart-seq2 profiles RNA and bisulfite-based scRRBS profiles methylation from one cell. |
| **scNanoHi-C** |  | 3d-genome | single-cell |  | genome-wide | restriction-digest; proximity-ligation; long-read-sequencing; plate-based | builds on single-cell-hi-c; pore-c | Li W 2023, Nat Methods, [doi:10.1038/s41592-023-01978-w](https://doi.org/10.1038/s41592-023-01978-w) | 56 | Single-cell Hi-C read on nanopore so whole ligation concatemers (multi-way contacts) are sequenced. |
| **scNMT-seq** |  | chromatin-accessibility; dna-methylation; rna | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion; reverse-transcription; plate-based | variant of scmt-seq; builds on scnome-seq; smart-seq2 | Clark SJ 2018, Nat Commun, [doi:10.1038/s41467-018-03149-4](https://doi.org/10.1038/s41467-018-03149-4) | 656 | A GpC methyltransferase marks open chromatin before bisulfite conversion, and RNA is split off, giving accessibility, methylation and transcriptome from one cell. |
| **scNOMe-seq** |  | chromatin-accessibility; dna-methylation | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion | builds on scbs-seq; nome-seq | Pott S 2017, Elife, [doi:10.7554/eLife.23203](https://doi.org/10.7554/eLife.23203) | 229 | NOMe-seq adapted to single cells: a GpC methyltransferase marks accessible DNA, and bisulfite sequencing reads accessibility and methylation together. |
| **scNT-seq** |  | rna | single-cell | metabolic-labeling | genome-wide | nucleotide-labeling; reverse-transcription; droplet-microfluidics | builds on single-cell-rna-seq | Qiu Q 2020, Nat Methods, [doi:10.1038/s41592-020-0935-4](https://doi.org/10.1038/s41592-020-0935-4) | 183 | Droplet-based single-cell RNA-seq that chemically marks newly transcribed mRNA with T-to-C substitutions on barcoded beads to profile new and old transcriptomes together. |
| **scONE-seq** |  | dna-sequence; rna | single-cell |  | genome-wide | reverse-transcription |  | Yu L 2023, Sci Adv, [doi:10.1126/sciadv.abp8901](https://doi.org/10.1126/sciadv.abp8901) | 76 | One-tube single-cell whole-genome DNA and RNA amplification that works on frozen tumour samples. |
| **SCRB-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based |  | Soumillon M 2014, bioRxiv, [doi:10.1101/003236](https://doi.org/10.1101/003236) | 216 | Plate-based digital gene-expression scRNA-seq protocol that surveys mRNA from thousands of single cells. |
| **scRCAT-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; tn5 | variant of smart-seq2 | Hu Y 2020, Nat Commun, [doi:10.1038/s41467-020-18976-7](https://doi.org/10.1038/s41467-020-18976-7) | 24 | Short-read single-cell method that tags both transcript ends during a modified Smart-seq2 protocol, then tagments and captures the 5' or 3' ends to demarcate isoform boundaries. |
| **scRRBS** |  | dna-methylation | single-cell |  | genome-wide | restriction-digest; bisulfite-or-enzymatic-conversion |  | Guo H 2013, Genome Res, [doi:10.1101/gr.161679.113](https://doi.org/10.1101/gr.161679.113) | 517 | Reduced representation bisulfite sequencing applied to single cells, enriching CpG-rich regions for a single-cell methylome. |
| **scSLAM-seq** |  | rna | single-cell | metabolic-labeling | genome-wide | nucleotide-labeling; reverse-transcription | variant of slam-seq; builds on single-cell-rna-seq | Erhard F 2019, Nature, [doi:10.1038/s41586-019-1369-y](https://doi.org/10.1038/s41586-019-1369-y) | 233 | Single-cell SLAM-seq that uses thiol alkylation of 4sU-labeled RNA to separate new from old transcripts in each cell. |
| **scSPLAT** |  | dna-methylation | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion; plate-based | builds on wgbs; scbs-seq | Raine A 2022, Sci Rep, [doi:10.1038/s41598-022-09798-2](https://doi.org/10.1038/s41598-022-09798-2) | 20 | Plate-based, pooled single-cell whole-genome bisulfite library preparation using splinted ligation adapter tagging. |
| **scSPRITE** |  | 3d-genome | single-cell |  | genome-wide | split-pool-barcoding | builds on sprite | Arrastia MV 2022, Nat Biotechnol, [doi:10.1038/s41587-021-00998-1](https://doi.org/10.1038/s41587-021-00998-1) | 127 | Split-pool barcoding of crosslinked DNA within single nuclei to map multiway 3D genome contacts. |
| **scTAPS** |  | dna-methylation | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion; plate-based |  | Chen X 2025, Genome Biol, [doi:10.1186/s13059-025-03708-1](https://doi.org/10.1186/s13059-025-03708-1) | 3 | Bisulfite-free, plate-based single-cell sequencing of 5mC and 5hmC at single-base resolution using enzymatic conversion. |
| **scTEM-seq** |  | dna-methylation; rna | single-cell |  | targeted | bisulfite-or-enzymatic-conversion; reverse-transcription | builds on scbs-seq; single-cell-rna-seq | Hunt KV 2022, Sci Rep, [doi:10.1038/s41598-022-09765-x](https://doi.org/10.1038/s41598-022-09765-x) | 21 | Single-cell amplicon bisulfite sequencing of SINE Alu elements to estimate global methylation, paired with the transcriptome of the same cell. |
| **scTHS-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5 | builds on scatac-seq | Lake BB 2018, Nat Biotechnol, [doi:10.1038/nbt.4038](https://doi.org/10.1038/nbt.4038) | 983 | Transposome hypersensitive-site profiling of single nuclei, run at high throughput alongside droplet snDrop-seq. |
| **scTrio-seq** |  | dna-sequence; dna-methylation; rna | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion; reverse-transcription | builds on scrrbs; smart-seq2 | Hou Y 2016, Cell Res, [doi:10.1038/cr.2016.23](https://doi.org/10.1038/cr.2016.23) | 647 | Separates each cell's RNA from its nuclear DNA so copy number, DNA methylome and transcriptome come from one cell. |
| **SEC-seq** |  | rna; protein | single-cell |  | genome-wide | reverse-transcription |  | Udani S 2024, Nat Nanotechnol, [doi:10.1038/s41565-023-01560-7](https://doi.org/10.1038/s41565-023-01560-7) | 52 | Hydrogel nanovials capture single cells with their secreted protein, which is tagged and linked to the cell transcriptome. |
| **Seq-Well** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based | variant of drop-seq | Gierahn TM 2017, Nat Methods, [doi:10.1038/nmeth.4179](https://doi.org/10.1038/nmeth.4179) | 868 | Portable scRNA-seq where barcoded capture beads and single cells are sealed in subnanoliter wells under a semipermeable membrane. |
| **Seq-Well S3** |  | rna | single-cell |  | genome-wide | reverse-transcription | variant of seq-well | Hughes TK 2020, Immunity, [doi:10.1016/j.immuni.2020.09.015](https://doi.org/10.1016/j.immuni.2020.09.015) | 271 | Seq-Well variant that uses randomly primed second-strand synthesis to recover cDNA that failed template switching, improving per-cell fidelity. |
| **SeqTag** |  | rna; chromatin-accessibility; histone-modification | single-cell |  | genome-wide | antibody-tethered-enzyme; tn5; reverse-transcription; combinatorial-indexing; plate-based | builds on paired-tag; cut-and-tag; atac-seq | Fu B 2026, bioRxiv, [doi:10.64898/2026.06.02.729594](https://doi.org/10.64898/2026.06.02.729594) |  | Single-cell multiomics: antibody-targeted CUT&Tag (histone marks) + ATAC (accessibility) + RNA from the same cell, with plate-based combinatorial barcoding. Named in the abstract only, not the title. |
| **SHARE-seq** |  | chromatin-accessibility; rna | single-cell |  | genome-wide | tn5; reverse-transcription; split-pool-barcoding | builds on single-cell-rna-seq; scatac-seq | Ma S 2020, Cell, [doi:10.1016/j.cell.2020.09.056](https://doi.org/10.1016/j.cell.2020.09.056) | 1140 | Split-pool ligation barcoding of accessibility and transcriptome from the same single cells. |
| **SIMPLE-seq** |  | dna-methylation | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion |  | Bai D 2025, Nat Biotechnol, [doi:10.1038/s41587-024-02148-9](https://doi.org/10.1038/s41587-024-02148-9) | 50 | Single-cell method that jointly maps 5mC and 5hmC at base resolution by labeling each modification and recording it as C-to-T signals. |
| **single-cell Hi-C** | scHi-C | 3d-genome | single-cell |  | genome-wide | restriction-digest; proximity-ligation; plate-based | variant of hi-c | Nagano T 2013, Nature, [doi:10.1038/nature12593](https://doi.org/10.1038/nature12593) | 1586 | Hi-C performed in individually isolated nuclei to measure contacts in single cells. |
| **single-cell RNA-seq** | scRNA-seq | rna | single-cell |  | genome-wide | reverse-transcription; plate-based | variant of rna-seq | Tang F 2009, Nat Methods, [doi:10.1038/nmeth.1315](https://doi.org/10.1038/nmeth.1315) | 3961 | First whole-transcriptome sequencing of a single cell (manually picked cells, plate-based cDNA amplification). |
| **SLAM-seq** | thiol(SH)-linked alkylation for metabolic sequencing of RNA | rna; nascent-rna | bulk | metabolic-labeling | genome-wide | nucleotide-labeling; reverse-transcription | builds on rna-seq | Herzog VA 2017, Nat Methods, [doi:10.1038/nmeth.4435](https://doi.org/10.1038/nmeth.4435) | 622 | Labels new RNA with 4-thiouridine, then alkylates the s4U so it is read as a T-to-C change in standard RNA-seq, giving transcript-level expression dynamics. |
| **Slide-DNA-seq** |  | dna-sequence | spatial |  | genome-wide | oligo-capture | variant of slide-seq | Zhao T 2022, Nature, [doi:10.1038/s41586-021-04217-4](https://doi.org/10.1038/s41586-021-04217-4) | 268 | Spatially barcoded DNA capture from tissue sections on bead arrays, used to map clonal copy-number populations in place. |
| **Slide-seq** |  | rna | spatial |  | genome-wide | oligo-capture; reverse-transcription |  | Rodriques SG 2019, Science, [doi:10.1126/science.aaw1219](https://doi.org/10.1126/science.aaw1219) | 2419 | RNA from a tissue section is transferred onto DNA-barcoded beads at known positions, giving spatially resolved transcriptomes. |
| **Slide-seqV2** |  | rna | spatial |  | genome-wide | oligo-capture; reverse-transcription | variant of slide-seq | Stickels RR 2021, Nat Biotechnol, [doi:10.1038/s41587-020-0739-1](https://doi.org/10.1038/s41587-020-0739-1) | 1292 | Improved Slide-seq with better library generation, bead synthesis and array indexing for much higher RNA capture efficiency. |
| **Slide-tags** |  | rna | single-cell; spatial |  | genome-wide | oligo-capture; reverse-transcription | builds on slide-seq | Russell AJC 2024, Nature, [doi:10.1038/s41586-023-06837-4](https://doi.org/10.1038/s41586-023-06837-4) | 221 | Nuclei in an intact tissue section are tagged with position barcodes from bead arrays, then profiled with standard single-nucleus assays. |
| **SMART-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based |  | Ramsköld D 2012, Nat Biotechnol, [doi:10.1038/nbt.2282](https://doi.org/10.1038/nbt.2282) | 1606 | Template-switching amplification of full-length cDNA from single cells, giving even coverage along transcripts. |
| **Smart-seq2** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based | variant of smart-seq | Picelli S 2013, Nat Methods, [doi:10.1038/nmeth.2639](https://doi.org/10.1038/nmeth.2639) | 2356 | Optimised SMART-seq with improved reverse transcription, template switching and preamplification for higher-yield full-length libraries. |
| **Smart-seq3** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based | variant of smart-seq2 | Hagemann-Jensen M 2020, Nat Biotechnol, [doi:10.1038/s41587-020-0497-0](https://doi.org/10.1038/s41587-020-0497-0) | 698 | Full-length single-cell RNA-seq with a 5' UMI in the template-switching oligo, so molecules can be counted and assigned to alleles and isoforms. |
| **Smart-seq3xpress** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based | variant of smart-seq3 | Hagemann-Jensen M 2022, Nat Biotechnol, [doi:10.1038/s41587-022-01311-4](https://doi.org/10.1038/s41587-022-01311-4) | 175 | Miniaturised, streamlined Smart-seq3 with lower reagent use for high-throughput full-length single-cell RNA-seq. |
| **sn-m3C-seq** |  | 3d-genome; dna-methylation | single-cell |  | genome-wide | restriction-digest; proximity-ligation; bisulfite-or-enzymatic-conversion; plate-based; facs-sorting | builds on single-cell-hi-c; snmc-seq | Lee DS 2019, Nat Methods, [doi:10.1038/s41592-019-0547-z](https://doi.org/10.1038/s41592-019-0547-z) | 338 | Joint chromatin conformation and DNA methylome from the same single nucleus via bisulfite conversion of 3C libraries. |
| **snapTotal-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription | builds on single-cell-rna-seq | Niu Y 2024, Nat Commun, [doi:10.1038/s41467-024-50291-3](https://doi.org/10.1038/s41467-024-50291-3) | 14 | One-step total-RNA single-cell RNA-seq that captures unspliced as well as spliced transcripts, enabling RNA-velocity kinetic analysis. |
| **SNARE-seq** |  | chromatin-accessibility; rna | single-cell |  | genome-wide | tn5; reverse-transcription; droplet-microfluidics | builds on drop-seq; scatac-seq | Chen S 2019, Nat Biotechnol, [doi:10.1038/s41587-019-0290-0](https://doi.org/10.1038/s41587-019-0290-0) | 807 | Droplet-based joint profiling of accessibility and transcriptome by capturing tagmented DNA alongside mRNA. |
| **snATAC-seq** | single-nucleus ATAC-seq | chromatin-accessibility | single-cell |  | genome-wide | tn5; combinatorial-indexing | variant of sci-atac-seq | Preissl S 2018, Nat Neurosci, [doi:10.1038/s41593-018-0079-3](https://doi.org/10.1038/s41593-018-0079-3) | 332 | Combinatorial barcoding of Tn5-tagmented nuclei from flash-frozen tissue, giving single-nucleus chromatin accessibility profiles. |
| **snmC-seq** | single-nucleus methylcytosine sequencing | dna-methylation | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion; plate-based; facs-sorting | variant of scbs-seq | Luo C 2017, Science, [doi:10.1126/science.aan3351](https://doi.org/10.1126/science.aan3351) | 545 | Single-nucleus methylome sequencing with improved throughput, used to classify neuronal subtypes. |
| **snmC2T-seq** |  | dna-methylation; chromatin-accessibility; rna | single-cell |  | genome-wide | bisulfite-or-enzymatic-conversion; tn5; reverse-transcription | builds on snmc-seq; single-cell-rna-seq; nome-seq | Luo C 2019, bioRxiv, [doi:10.1101/2019.12.11.873398](https://doi.org/10.1101/2019.12.11.873398) | 171 | Single-nucleus joint profiling of DNA methylation, chromatin accessibility and transcriptome from the same nucleus. |
| **snRandom-seq** |  | rna | single-cell |  | genome-wide | droplet-microfluidics; reverse-transcription |  | Xu Z 2023, Nat Commun, [doi:10.1038/s41467-023-38409-5](https://doi.org/10.1038/s41467-023-38409-5) | 99 | Droplet-based single-nucleus total RNA sequencing that uses random primers so that non-polyadenylated RNA and FFPE-archived material can be profiled. |
| **SNuBar-ATAC** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; droplet-microfluidics | variant of scatac-seq | Wang K 2021, Mol Cell, [doi:10.1016/j.molcel.2021.09.026](https://doi.org/10.1016/j.molcel.2021.09.026) | 35 | Single-oligo transposome barcoding during tagmentation lets scATAC-seq samples be multiplexed without a pre-labelling step. |
| **SPATAC-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; split-pool-barcoding | builds on sci-atac-seq | Sun K 2024, Nat Cell Biol, [doi:10.1038/s41556-024-01449-0](https://doi.org/10.1038/s41556-024-01449-0) | 19 | Split-pool ligation barcoding of Tn5-tagmented chromatin for single-nucleus ATAC profiling at atlas scale. |
| **Spatial-ATAC-seq** |  | chromatin-accessibility | spatial |  | genome-wide | tn5; microfluidic-chip | builds on atac-seq; dbit-seq | Deng Y 2022, Nature, [doi:10.1038/s41586-022-05094-1](https://doi.org/10.1038/s41586-022-05094-1) | 414 | Tissue-section chromatin accessibility profiling that combines in situ Tn5 tagmentation with microfluidic deterministic barcoding (DBiT-style). |
| **Spatial-CUT&Tag** | Spatial C&T | histone-modification | spatial |  | genome-wide | antibody-tethered-enzyme; tn5; microfluidic-chip | builds on cut-and-tag; dbit-seq | Deng Y 2022, Science, [doi:10.1126/science.abg7216](https://doi.org/10.1126/science.abg7216) | 391 | Tissue-section profiling of histone modifications by in situ CUT&Tag chemistry with microfluidic deterministic barcoding. |
| **Spear-ATAC** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; droplet-microfluidics | variant of 10x-chromium-single-cell-atac | Pierce SE 2021, Nat Commun, [doi:10.1038/s41467-021-23213-w](https://doi.org/10.1038/s41467-021-23213-w) | 145 | Droplet scATAC-seq modified to also capture sgRNA spacers, so chromatin accessibility can be read out for each CRISPR perturbation. |
| **spinDrop** |  | rna; nascent-rna | single-cell |  | genome-wide | droplet-microfluidics; facs-sorting; reverse-transcription | builds on drop-seq | De Jonghe J 2023, Nat Commun, [doi:10.1038/s41467-023-40322-w](https://doi.org/10.1038/s41467-023-40322-w) | 62 | Droplet platform that sorts droplets by fluorescence and uses picoinjection to add lysis and reverse transcription reagents, raising gene detection and cutting background. |
| **SPLiT-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; split-pool-barcoding |  | Rosenberg AB 2018, Science, [doi:10.1126/science.aam8999](https://doi.org/10.1126/science.aam8999) | 1422 | Split-pool ligation barcoding labels RNA from fixed cells or nuclei through successive rounds of barcoding, with no single-cell isolation. |
| **SPRITE** |  | 3d-genome | bulk |  | genome-wide | split-pool-barcoding |  | Quinodoz SA 2018, Cell, [doi:10.1016/j.cell.2018.05.024](https://doi.org/10.1016/j.cell.2018.05.024) | 890 | Ligation-free mapping of multi-way interactions by split-pool barcoding of crosslinked complexes. |
| **Strand-seq** |  | dna-sequence | single-cell |  | genome-wide | nucleotide-labeling; plate-based |  | Falconer E 2012, Nat Methods, [doi:10.1038/nmeth.2206](https://doi.org/10.1038/nmeth.2206) | 198 | BrdU-labels one parental DNA strand over a single replication round so each single cell's template strands are sequenced separately, mapping sister chromatid exchanges and inversions. |
| **STRT-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based |  | Islam S 2011, Genome Res, [doi:10.1101/gr.110882.110](https://doi.org/10.1101/gr.110882.110) | 948 | Single-cell tagged reverse transcription that barcodes cDNA at the mRNA 5' end, so cells are pooled and sequenced by their 5' ends. |
| **STRT-seq-2i** |  | rna | single-cell |  | genome-wide | reverse-transcription; facs-sorting | variant of strt-seq | Hochgerner H 2017, Sci Rep, [doi:10.1038/s41598-017-16546-4](https://doi.org/10.1038/s41598-017-16546-4) | 78 | STRT-seq on an addressable 9600-microwell array, with dual-index barcodes and cell sampling by limiting dilution or FACS. |
| **TEA-seq** |  | rna; protein; chromatin-accessibility | single-cell |  | genome-wide | reverse-transcription; tn5; droplet-microfluidics | builds on single-cell-rna-seq; scatac-seq; cite-seq | Swanson E 2021, Elife, [doi:10.7554/eLife.63632](https://doi.org/10.7554/eLife.63632) | 266 | Droplet-based trimodal assay that measures RNA, surface epitopes and chromatin accessibility from the same single cells. |
| **Tiled-MCC** | Tiled Micro-Capture-C | 3d-genome | bulk |  | targeted | mnase; proximity-ligation; oligo-capture | variant of micro-capture-c | Aljahani A 2022, Nat Commun, [doi:10.1038/s41467-022-29696-5](https://doi.org/10.1038/s41467-022-29696-5) | 120 | Micro-Capture-C with oligos tiled across a whole region, giving all-vs-all contacts within the captured locus. |
| **TIME-seq** |  | dna-methylation | bulk |  | targeted | bisulfite-or-enzymatic-conversion; tn5 |  | Griffin PT 2024, Nat Aging, [doi:10.1038/s43587-023-00555-2](https://doi.org/10.1038/s43587-023-00555-2) | 25 | Highly multiplexed tagmentation-based targeted methylation sequencing used to build low-cost epigenetic clocks. |
| **TimeLapse-seq** |  | rna | bulk | metabolic-labeling | genome-wide | nucleotide-labeling; reverse-transcription | builds on rna-seq | Schofield JA 2018, Nat Methods, [doi:10.1038/nmeth.4582](https://doi.org/10.1038/nmeth.4582) | 261 | Bulk RNA-seq that chemically recodes 4-thiouridine into cytidine analogs so newly transcribed RNA is marked by U-to-C mutations. |
| **TimeVault** |  | rna | bulk | molecular-recording | genome-wide | reverse-transcription |  | Chao YK 2026, Science, [doi:10.1126/science.adz9353](https://doi.org/10.1126/science.adz9353) | 21 | Genetically encoded vault particles capture polyadenylated mRNA inside living cells to store a transcriptome snapshot for later readout. |
| **TIP-seq** | Targeted Insertion of Promoters | histone-modification; protein-dna-binding | bulk; single-cell |  | genome-wide | antibody-tethered-enzyme; tn5 | builds on cut-and-tag | Bartlett DA 2021, J Cell Biol, [doi:10.1083/jcb.202103078](https://doi.org/10.1083/jcb.202103078) | 48 | Antibody-tethered Tn5 inserts a T7 promoter at target sites; in vitro transcription amplifies them linearly for single-cell chromatin profiling. |
| **TOPmentation** | Transcription factor-OPtimized ChIPmentation | protein-dna-binding; histone-modification | bulk |  | genome-wide | antibody-pull-down; tn5 | variant of chipmentation | Crump NT 2023, Nat Commun, [doi:10.1038/s41467-023-40981-9](https://doi.org/10.1038/s41467-023-40981-9) | 27 | Optimised high-throughput ChIPmentation for weakly bound non-histone proteins from ~100,000 cells. Named only in the Results section. |
| **Trac-looping** |  | 3d-genome; chromatin-accessibility | bulk |  | genome-wide | tn5 | builds on atac-seq; hi-c | Lai B 2018, Nat Methods, [doi:10.1038/s41592-018-0107-y](https://doi.org/10.1038/s41592-018-0107-y) | 92 | Transposase inserts a bivalent linker between interacting regions, capturing chromatin contacts and accessibility without fragmentation or ligation. |
| **txci-ATAC-seq** |  | chromatin-accessibility | single-cell |  | genome-wide | tn5; combinatorial-indexing; droplet-microfluidics | builds on sci-atac-seq; 10x-chromium-single-cell-atac | Zhang H 2024, Genome Biol, [doi:10.1186/s13059-023-03150-1](https://doi.org/10.1186/s13059-023-03150-1) | 25 | Tn5 pre-indexing of nuclei across samples followed by 10x barcoding, scaling scATAC to about 200,000 nuclei per reaction. |
| **VASA-seq** |  | rna | single-cell |  | genome-wide | reverse-transcription; plate-based; droplet-microfluidics |  | Salmen F 2022, Nat Biotechnol, [doi:10.1038/s41587-022-01361-8](https://doi.org/10.1038/s41587-022-01361-8) | 234 | Total-RNA single-cell sequencing that fragments and tails all RNA after lysis, so non-polyadenylated and non-coding transcripts are captured. |
| **wellDA-seq** |  | dna-sequence; chromatin-accessibility | single-cell |  | genome-wide | tn5; microfluidic-chip | builds on scatac-seq | Wang K 2024, bioRxiv, [doi:10.1101/2024.09.06.611519](https://doi.org/10.1101/2024.09.06.611519) | 1 | Dual-Tn5 tagmentation splits open and closed chromatin into ATAC and DNA libraries, with nanowell chip partitioning to co-profile copy number and accessibility in single cells. |
| **WGBS** | whole-genome bisulfite sequencing; BS-seq | dna-methylation | bulk |  | genome-wide | bisulfite-or-enzymatic-conversion |  | Lister R 2009, Nature, [doi:10.1038/nature08514](https://doi.org/10.1038/nature08514) | 4666 | Bisulfite conversion plus whole-genome sequencing to map DNA methylation at single-base resolution. |
| **ZipSeq** |  | rna | single-cell; spatial |  | genome-wide | reverse-transcription; imaging-guided-selection | builds on single-cell-rna-seq | Hu KH 2020, Nat Methods, [doi:10.1038/s41592-020-0880-2](https://doi.org/10.1038/s41592-020-0880-2) | 153 | Patterned illumination prints photocaged barcodes ("zipcodes") onto live cells in tissue, linking each transcriptome to its position. |

## Lineage (parent -> child)

`variant` = child is a direct modification of the parent; `builds on` = child combines or draws on the parent.

- 10x-chromium-single-cell-3-gene-expression -> 10x-chromium-5-gene-expression (variant)
- strt-seq -> 10x-chromium-5-gene-expression (builds on)
- 10x-chromium-5-gene-expression -> 10x-chromium-5-immune-profiling-feature-barcoding (variant)
- 10x-chromium-single-cell-3-feature-barcoding -> 10x-chromium-5-immune-profiling-feature-barcoding (builds on)
- 10x-chromium-single-cell-3-gene-expression -> 10x-chromium-single-cell-3-feature-barcoding (builds on)
- cite-seq -> 10x-chromium-single-cell-3-feature-barcoding (builds on)
- drop-seq -> 10x-chromium-single-cell-3-gene-expression (builds on)
- drop-seq -> 10x-chromium-single-cell-3-solution-v1 (builds on)
- scatac-seq -> 10x-chromium-single-cell-atac (variant)
- 10x-chromium-single-cell-atac -> 10x-chromium-single-cell-multiome-atac-plus-gene-expression (builds on)
- 10x-chromium-single-cell-3-gene-expression -> 10x-chromium-single-cell-multiome-atac-plus-gene-expression (builds on)
- 3c -> 4c-seq (variant)
- scatac-seq -> asap-seq (builds on)
- cite-seq -> asap-seq (builds on)
- single-cell-rna-seq -> astar-seq (builds on)
- scatac-seq -> astar-seq (builds on)
- dnase-seq -> atac-seq (builds on)
- faire-seq -> atac-seq (builds on)
- drop-seq -> bacdrop (builds on)
- 3c -> capture-c (variant)
- single-cell-rna-seq -> cel-seq (builds on)
- cel-seq -> cel-seq2 (variant)
- sci-atac-seq -> ch-atac-seq (variant)
- single-cell-hi-c -> chair (builds on)
- scatac-seq -> chair (builds on)
- single-cell-rna-seq -> chair (builds on)
- 3c -> chia-pet (builds on)
- chip-seq -> chia-pet (builds on)
- chip-seq -> chipmentation (variant)
- atac-seq -> chipmentation (builds on)
- sci-atac-seq -> cobatch (variant)
- cut-and-tag -> cobatch (builds on)
- cut-and-tag -> cotech (builds on)
- sci-rna-seq -> cotech (builds on)
- sci-atac-seq -> crispr-sciatac (variant)
- crop-seq -> crispr-sciatac (builds on)
- drop-seq -> crop-seq (builds on)
- chip-seq -> cut-and-run (builds on)
- cut-and-run -> cut-and-tag (variant)
- atac-seq -> cut-and-tag (builds on)
- drop-seq -> delley2021 (builds on)
- single-cell-hi-c -> dip-c (variant)
- single-cell-rna-seq -> direct-seq (builds on)
- crop-seq -> direct-seq (builds on)
- asap-seq -> dogma-seq (variant)
- cite-seq -> dogma-seq (builds on)
- malbac -> dr-seq (builds on)
- cel-seq -> dr-seq (builds on)
- chip-seq -> drop-scchip-seq (builds on)
- scbs-seq -> drop-bs (variant)
- chip-seq -> drop-chip (builds on)
- drop-seq -> drop-chip (builds on)
- single-cell-rna-seq -> drop-seq (variant)
- in-situ-hi-c -> droplet-hi-c (variant)
- snare-seq -> droplet-hi-c (builds on)
- paired-tag -> droplet-paired-tag (variant)
- scatac-seq -> dscatac-seq (builds on)
- dscatac-seq -> dsciatac-seq (variant)
- sci-atac-seq -> dsciatac-seq (builds on)
- share-seq -> easyshare-seq (variant)
- single-cell-rna-seq -> eccite-seq (builds on)
- cite-seq -> eccite-seq (builds on)
- cut-and-tag -> echos (variant)
- scdam-and-t-seq -> epidamid (builds on)
- scifi-rna-seq -> fipresci (builds on)
- smart-seq3 -> flash-seq (variant)
- smart-seq2 -> g-and-t-seq (builds on)
- malbac -> g-and-t-seq (builds on)
- sci-hi-c -> gage-seq (builds on)
- sci-rna-seq -> gage-seq (builds on)
- drop-seq -> got (builds on)
- scatac-seq -> got-cha (builds on)
- got -> got-cha (builds on)
- rna-seq -> grid-seq (builds on)
- hi-c -> grid-seq (builds on)
- 3c -> hi-c (variant)
- in-situ-hi-c -> hichip (variant)
- chia-pet -> hichip (builds on)
- chip-seq -> hichip (builds on)
- dip-c -> hires (builds on)
- single-cell-rna-seq -> hires (builds on)
- indrop -> hydrop-atac (builds on)
- scatac-seq -> hydrop-atac (builds on)
- drop-seq -> hydrop-rna (builds on)
- indrop -> hydrop-rna (builds on)
- hi-c -> in-situ-hi-c (variant)
- indrop -> indrops-2 (variant)
- chipmentation -> itchip-seq (builds on)
- sci-atac-seq -> itchip-seq (builds on)
- hires -> limca (builds on)
- smart-seq2 -> limca (builds on)
- single-cell-rna-seq -> live-seq (builds on)
- sci-rna-seq -> m3-seq (builds on)
- malbac -> malbac-dt (builds on)
- cel-seq -> mars-seq (builds on)
- mars-seq -> mars-seq2-0 (variant)
- single-cell-rna-seq -> matq-seq (builds on)
- scrb-seq -> mcscrb-seq (variant)
- in-situ-hi-c -> methyl-hic (builds on)
- wgbs -> methyl-hic (builds on)
- hi-c -> micro-c (variant)
- capture-c -> micro-capture-c (variant)
- micro-c -> micro-capture-c (variant)
- split-seq -> microsplit (variant)
- cut-and-tag -> multi-cut-and-tag (variant)
- cut-and-tag -> multi-tag (builds on)
- single-cell-rna-seq -> nasc-seq (builds on)
- capture-c -> ng-capture-c (variant)
- wgbs -> nome-seq (builds on)
- cut-and-tag -> ntt-seq (builds on)
- cite-seq -> ntt-seq (builds on)
- droplet-hi-c -> paired-hi-c (variant)
- drop-seq -> paired-hi-c (builds on)
- sci-rna-seq -> paired-seq (builds on)
- sci-atac-seq -> paired-seq (builds on)
- paired-seq -> paired-tag (variant)
- cut-and-tag -> paired-tag (builds on)
- sci-rna-seq -> petri-seq (builds on)
- split-seq -> petri-seq (builds on)
- scatac-seq -> phage-atac (builds on)
- cite-seq -> phage-atac (builds on)
- scatac-seq -> phospho-seq (builds on)
- cite-seq -> phospho-seq (builds on)
- scatac-seq -> pi-atac (builds on)
- in-situ-hi-c -> plac-seq (variant)
- chia-pet -> plac-seq (builds on)
- chip-seq -> plac-seq (builds on)
- atac-seq -> plate-scatac-seq (builds on)
- hi-c -> pore-c (builds on)
- single-cell-rna-seq -> probac-seq (builds on)
- quartz-seq -> quartz-seq2 (variant)
- micro-c -> rcmc (variant)
- sci-atac-seq -> s3-atac (builds on)
- s3-atac -> s3-wgs (builds on)
- single-cell-rna-seq -> sc-end5-seq (builds on)
- atac-seq -> scatac-seq (variant)
- wgbs -> scbs-seq (variant)
- smart-seq2 -> sccat-seq (builds on)
- scatac-seq -> sccat-seq (builds on)
- scnome-seq -> sccool-seq (builds on)
- scbs-seq -> sccool-seq (builds on)
- scdamid -> scdam-and-t-seq (variant)
- cel-seq2 -> scdam-and-t-seq (builds on)
- damid -> scdamid (variant)
- dnase-seq -> scdnase-seq (variant)
- single-cell-rna-seq -> sceu-seq (builds on)
- scatac-seq -> scget-seq (variant)
- atac-seq -> sci-atac-seq (variant)
- sci-atac-seq -> sci-atac-seq3 (variant)
- sci-rna-seq -> sci-car (builds on)
- sci-atac-seq -> sci-car (builds on)
- sci-rna-seq -> sci-fate (variant)
- single-cell-hi-c -> sci-hi-c (variant)
- sci-atac-seq -> sci-hi-c (builds on)
- sci-rna-seq3 -> sci-plex (variant)
- single-cell-rna-seq -> sci-rna-seq (variant)
- sci-atac-seq -> sci-rna-seq (builds on)
- sci-rna-seq -> sci-rna-seq3 (variant)
- 10x-chromium-single-cell-atac -> scifi-atac-seq (builds on)
- sci-atac-seq -> scifi-atac-seq (builds on)
- sci-rna-seq -> scifi-rna-seq (builds on)
- 10x-chromium-single-cell-3-gene-expression -> scifi-rna-seq (builds on)
- sci-atac-seq -> sciplex-atac-seq (builds on)
- cite-seq -> scito-seq (builds on)
- mnase-seq -> scmnase-seq (variant)
- smart-seq2 -> scmt-seq (builds on)
- scrrbs -> scmt-seq (builds on)
- single-cell-hi-c -> scnanohi-c (builds on)
- pore-c -> scnanohi-c (builds on)
- scmt-seq -> scnmt-seq (variant)
- scnome-seq -> scnmt-seq (builds on)
- smart-seq2 -> scnmt-seq (builds on)
- scbs-seq -> scnome-seq (builds on)
- nome-seq -> scnome-seq (builds on)
- single-cell-rna-seq -> scnt-seq (builds on)
- smart-seq2 -> scrcat-seq (variant)
- slam-seq -> scslam-seq (variant)
- single-cell-rna-seq -> scslam-seq (builds on)
- wgbs -> scsplat (builds on)
- scbs-seq -> scsplat (builds on)
- sprite -> scsprite (builds on)
- scbs-seq -> sctem-seq (builds on)
- single-cell-rna-seq -> sctem-seq (builds on)
- scatac-seq -> scths-seq (builds on)
- scrrbs -> sctrio-seq (builds on)
- smart-seq2 -> sctrio-seq (builds on)
- drop-seq -> seq-well (variant)
- seq-well -> seq-well-s3 (variant)
- paired-tag -> seqtag (builds on)
- cut-and-tag -> seqtag (builds on)
- atac-seq -> seqtag (builds on)
- single-cell-rna-seq -> share-seq (builds on)
- scatac-seq -> share-seq (builds on)
- hi-c -> single-cell-hi-c (variant)
- rna-seq -> single-cell-rna-seq (variant)
- rna-seq -> slam-seq (builds on)
- slide-seq -> slide-dna-seq (variant)
- slide-seq -> slide-seqv2 (variant)
- slide-seq -> slide-tags (builds on)
- smart-seq -> smart-seq2 (variant)
- smart-seq2 -> smart-seq3 (variant)
- smart-seq3 -> smart-seq3xpress (variant)
- single-cell-hi-c -> sn-m3c-seq (builds on)
- snmc-seq -> sn-m3c-seq (builds on)
- single-cell-rna-seq -> snaptotal-seq (builds on)
- drop-seq -> snare-seq (builds on)
- scatac-seq -> snare-seq (builds on)
- sci-atac-seq -> snatac-seq (variant)
- scbs-seq -> snmc-seq (variant)
- snmc-seq -> snmc2t-seq (builds on)
- single-cell-rna-seq -> snmc2t-seq (builds on)
- nome-seq -> snmc2t-seq (builds on)
- scatac-seq -> snubar-atac (variant)
- sci-atac-seq -> spatac-seq (builds on)
- atac-seq -> spatial-atac-seq (builds on)
- dbit-seq -> spatial-atac-seq (builds on)
- cut-and-tag -> spatial-cut-and-tag (builds on)
- dbit-seq -> spatial-cut-and-tag (builds on)
- 10x-chromium-single-cell-atac -> spear-atac (variant)
- drop-seq -> spindrop (builds on)
- strt-seq -> strt-seq-2i (variant)
- single-cell-rna-seq -> tea-seq (builds on)
- scatac-seq -> tea-seq (builds on)
- cite-seq -> tea-seq (builds on)
- micro-capture-c -> tiled-mcc (variant)
- rna-seq -> timelapse-seq (builds on)
- cut-and-tag -> tip-seq (builds on)
- chipmentation -> topmentation (variant)
- atac-seq -> trac-looping (builds on)
- hi-c -> trac-looping (builds on)
- sci-atac-seq -> txci-atac-seq (builds on)
- 10x-chromium-single-cell-atac -> txci-atac-seq (builds on)
- scatac-seq -> wellda-seq (builds on)
- single-cell-rna-seq -> zipseq (builds on)
