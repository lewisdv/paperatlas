---
title: "Autism genes converge on asynchronous development of shared neuron classes."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41586-021-04358-6
pmid: 35110736
authors: Paulsen B et al.
journal: Nature (2022)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.pdf
pdf_status: downloaded
---

# Autism genes converge on asynchronous development of shared neuron classes.

## Source

- Authors: Paulsen B, Velasco S, Kedaigle AJ, Pigoni M, Quadrato G, Deo AJ, Adiconis X, Uzquiano A et al.
- Journal: Nature (2022)
- DOI: [10.1038/s41586-021-04358-6](https://doi.org/10.1038/s41586-021-04358-6)
- PMID: [35110736](https://pubmed.ncbi.nlm.nih.gov/35110736/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Genetic risk for autism spectrum disorder (ASD) is associated with hundreds of genes spanning a wide range of biological functions1-6. The alterations in the human brain resulting from mutations in these genes remain unclear. Furthermore, their phenotypic manifestation varies across individuals7,8. Here we used organoid models of the human cerebral cortex to identify cell-type-specific developmental abnormalities that result from haploinsufficiency in three ASD risk genes-SUV420H1 (also known as KMT5B), ARID1B and CHD8-in multiple cell lines from different donors, using single-cell RNA-sequencing (scRNA-seq) analysis of more than 745,000 cells and proteomic analysis of individual organoids, to identify phenotypic convergence. Each of the three mutations confers asynchronous development of two main cortical neuronal lineages-γ-aminobutyric-acid-releasing (GABAergic) neurons and deep-layer excitatory projection neurons-but acts through largely distinct molecular pathways. Although these phenotypes are consistent across cell lines, their expressivity is influenced by the individual genomic context, in a manner that is dependent on both the risk gene and the developmental defect. Calcium imaging in intact organoids shows that these early-stage developmental changes are followed by abnormal circuit activity. This research uncovers cell-type-specific neurodevelopmental abnormalities that are shared across ASD risk genes and are finely modulated by human genomic context, finding convergence in the neurobiological basis of how different risk genes contribute to ASD pathology.

## Key findings

**Headline claim.** Three unrelated ASD risk genes — `SUV420H1` (a.k.a. `KMT5B`), `ARID1B`, `CHD8` — when made heterozygous in human cortical organoids, **converge on a shared *phenotype* (asynchronous, mistimed development of two specific neuron classes) while *diverging* at the molecular level** (the dysregulated genes/proteins barely overlap across mutations). This is the paper's core "convergence-with-divergence" result.

**Genes perturbed (all heterozygous, protein-truncating indels → haploinsufficiency):**
- `SUV420H1` / `KMT5B` — H4K20 histone-lysine methyltransferase (chromatin writer). Edited in Mito210, Mito294, PGP1.
- `ARID1B` — BAF (SWI/SNF) chromatin-remodelling subunit; Coffin–Siris gene. Edited in Mito210, Mito294.
- `CHD8` — chromatin remodeller; one of the most penetrant ASD genes. Edited in HUES66 (AC2 clone), plus GM08330, H1, Mito210, Mito294 across experiments.
- All three are top recurrent ASD hits and are clinically associated with macro-/microcephaly; organoid size defects in mutants mirrored the patient direction (clinical-relevance check).

**Platform / scale.** Isogenic (CRISPR-edited mutant vs. parental control) **cortical organoids** from multiple iPSC/hESC donor lines, profiled by **single-cell readout**: scRNA-seq of **>745,000 cells** (749,370 cells across 112 QC-passing single organoids), plus **scATAC-seq** (45,988 nuclei, SUV420H1 only), **whole-organoid proteomics** (TMT mass spec), **bulk RNA-seq**, and functional **calcium imaging + MEA**. Note this is a *mutant-vs-isogenic-control comparison across lines*, **not** a pooled mosaic/multiplexed in-organoid CRISPR screen (contrast with [Li 2023](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md) and [Meng 2023](../sources/meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md), which do mosaic screening).

**The convergent phenotype — two shared neuron classes, mistimed:**
- **GABAergic (inhibitory interneuron) lineage** appears **prematurely / in excess** in all three mutants. Controls have few/no GABAergic neurons until ~3.5 months, but mutants show them at 1 month (SUV420H1, ARID1B) or strongly expanded at 3.5–6 months (CHD8). At 1 month these are broad-marker "GABAergic neurons"; by ≥3 months they express cortical-interneuron markers.
- **Deep-layer (DL) excitatory projection neurons** (the first-born cortical-plate neurons) are also mistimed — but the *direction differs by gene*: `SUV420H1+/−` **accelerates** their maturation; `ARID1B+/−` **delays/reduces** them. Same affected cell class, opposite developmental push.

**Timing / persistence (cell-class- and gene-specific):**
- Effects are early (detectable at 1 month) and can either **resolve** or **persist**. In milder backgrounds (e.g. Mito210 SUV420H1) the GABAergic and DL-PN phenotypes were rescued by 3 months; in Mito294 SUV420H1 the GABAergic excess persisted; for `CHD8+/−` the GABAergic-interneuron excess **persisted to 6 months**.
- Pseudotime/WGCNA module analyses support accelerated differentiation (SUV420H1: synapse/maturation module up; CHD8: interneuron-differentiation module up) vs. delayed differentiation (ARID1B: cell-cycle/DNA-replication module up in progenitors).

**Molecular divergence (the other half of the argument):**
- Across the three strong-phenotype lines, **DEGs barely overlap** between mutations even for identical cell types ([Fig. 4](../raw/sources/paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.pdf)); they share enriched GO categories but not individual genes.
- Proteomics: 233 DEPs (SUV420H1), 24 (ARID1B), 34 (CHD8); **only 5 proteins** dysregulated in ≥2 mutations. Protein–protein interaction networks show the distinct DEP sets nonetheless map onto **shared higher-order processes/subnetworks** — i.e. different molecules, convergent processes.

**Expressivity is modulated by genomic context.** The *same* mutation gives different severity in different donor lines, and — importantly — the *direction of context-modulation is gene- and phenotype-specific*: Mito294 showed the strongest SUV420H1 GABAergic phenotype but **no** significant ARID1B GABAergic phenotype; Mito210 showed a stronger DL-PN phenotype but milder GABAergic phenotype than PGP1. Different features of one mutant can be tuned independently by the same background.

**Functional consequence.** Calcium imaging (GCaMP) + MEA in intact ~4-month PGP1 organoids: network bursting is glutamatergic (NBQX-abolished); `SUV420H1+/−` organoids show **reduced spontaneous network burst frequency and duration** vs. controls, and after excitatory-synapse blockade only controls stayed active (controls more excitable/immature) — consistent with the accelerated-maturation molecular signature and with mouse KMT5B models.

## Methods

- **Organoid model.** Dorsally patterned **cortical organoids** generated by the directed Velasco/Arlotta protocol (ref. 9; Velasco 2019) from multiple human PS cell lines: iPSC lines Mito210, Mito294 (psychiatric controls), PGP1, GM08330; hESC lines HUES66, H1. Profiled at staged time points — **1 month** (mostly progenitors, neurogenesis beginning), **3 / 3.5 months** (progenitor + excitatory-neuron diversity), **6 months** (interneurons + astroglia). Karyotype/STR-authenticated; some lines carry documented CNVs (noted as a caveat by the authors).
- **Perturbation strategy.** **CRISPR-Cas9 knock-in of heterozygous protein-truncating indels** targeting patient-relevant protein domains (SUV420H1 N-terminal; ARID1B just before the ARID domain; CHD8 13-nt deletion → stop at aa1248). Delivery by nanoblades, Neon/Amaxa electroporation, or Cas9 RNP; clones picked, PCR/Sanger-confirmed, heterozygosity re-confirmed after expansion. **Isogenic design**: each mutant clone compared to its parental control line; key genes engineered in ≥2–4 independent donor backgrounds to test reproducibility vs. context.
- **Single-cell / transcriptomic analysis.** 10x Chromium 3′ **scRNA-seq** (Cell Ranger → Seurat v3; Louvain clustering, t-SNE; cell-type labels from marker genes). Cell-type proportion differences tested with **mixed-effect logistic regression** (organoid as random effect, BH-corrected) to handle organoid-to-organoid variation. **Pseudotime** via Monocle3 with one-sided Kolmogorov–Smirnov tests on mutant-vs-control pseudotime distributions; **WGCNA** gene-coexpression modules scored per cell with linear mixed models; **DESeq2** for per-cell-type and pseudobulk DEGs; clusterProfiler for GO enrichment.
- **Chromatin.** 10x **scATAC-seq** (SUV420H1, 1 + 3 months; Signac), co-embedded with matched scRNA-seq (label transfer); differentially accessible regions and HOMER TF-motif enrichment (links accessibility changes to maturation and GABAergic-lineage TFs — mechanistic, since SUV420H1 is a chromatin writer).
- **Proteomics.** Whole-organoid **TMT 16-plex LC–MS/MS** on individual mutant/control organoids; DEP detection with DEP/LIMMA (FDR < 0.1); GSEA; prize-collecting Steiner-forest PPI networks over STRING.
- **Function.** AAV-`SomaGCaMP6f` **calcium imaging** of intact organoids (confocal, Suite2p segmentation, custom MATLAB burst analysis) with TTX/NBQX pharmacology; **CMOS-HD multi-electrode array** for extracellular spikes.
- Data: Synapse (syn26346373) + Broad Single Cell Portal (SCP1129); code at github.com/AmandaKedaigle/mutated-brain-organoids.

## Relevance to the brain-organoid ASD review

Supports the manuscript *"Programmable Brain Organoids for Proactive Autism Genetics."*

- **Primary citation for "phenotypic convergence coexists with molecular divergence."** This is arguably the cleanest single-paper demonstration that diverse ASD genes converge on a *shared developmental/cellular vulnerability* (mistimed GABAergic + deep-layer projection neurons) while their *molecular targets stay largely gene-specific* (DEGs/DEPs barely overlap; only 5 shared proteins across mutations). Use it as the anchor reference whenever the review asserts convergence is at the level of process/cell class, not pathway.
- **Backs the CONVERGENCE argument** that *diverse ASD genes converge on shared developmental vulnerability stages*: here the vulnerable window is early neurogenesis (~1 month) and the shared targets are two specific cortical neuron classes — i.e. concrete support for "convergence on a developmental stage / shared neuron classes" rather than vague convergence.
- **Backs the isogenic-perturbation pillar.** Demonstrates that **CRISPR-engineered isogenic cortical organoids + single-cell readout** can resolve cell-type-specific, stage-specific ASD phenotypes reproducibly across donors — the methodological premise of "programmable" organoid autism genetics.
- **Supports "common Stage-3 readouts but gene-specific therapeutics."** Because convergence is phenotypic (shared affected neuron classes, shared higher-order processes, shared circuit dysfunction) while molecular mechanisms diverge, it directly motivates the review's claim that a **shared late/Stage-3 cellular-and-circuit readout** (interneuron/DL-PN proportions, pseudotime maturation, network bursting) can serve many genes, **but the upstream molecular correction must be gene-specific**. The authors themselves end by advocating therapeutics aimed at shared dysfunctional *circuit* properties in addition to shared molecular pathways.
- **Genomic-context / expressivity point.** Provides the review's evidence that human genetic background tunes expressivity per-gene and per-phenotype — relevant to any claim that proactive screening must test variants across multiple isogenic backgrounds. Complements [Fu 2023](fu_2023_autism_specific_pten_p_ile135leu_variant_autism.md) and [Kang 2024](../sources/kang_2024_germline_pten_genotype_dependent_phenotypic_divergence_during.md) (PTEN genotype × background) on context-dependent expressivity.

### Related pages
- [Villa 2022 — CHD8 haploinsufficiency links autism to transient alterations in excitatory/inhibitory neurons](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md) — independent CHD8 organoid study; Paulsen cites it as concordant for the CHD8 GABAergic-interneuron effect.
- [Birey 2022 — Dissecting the molecular basis of human interneuron migration in forebrain assembloids](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md) — GABAergic interneuron biology in organoid models.
- [Mariani 2015 — FOXG1-dependent dysregulation of GABA/glutamate neuron differentiation in ASD](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md) — earlier organoid evidence for excitatory/inhibitory imbalance in ASD.
- [Li 2023 — Single-cell brain-organoid screening identifies developmental defects in ASD](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md) and [Meng 2023 — Assembloid CRISPR screens of disease genes](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md) — *mosaic/multiplexed* perturbation complement to Paulsen's *one-gene-per-isogenic-line* design.

## Open questions / limitations

- **Generalizability beyond 3 genes.** Only `SUV420H1`/`KMT5B`, `ARID1B`, `CHD8` were tested. All three are chromatin/transcriptional regulators — whether the *same* two neuron classes are the convergent target for ASD genes in other functional classes (e.g. synaptic genes like SHANK3, signalling genes like PTEN) is not established here. The convergence claim is suggestive, not proven, for the broader ASD gene set.
- **Measurement / sampling bias.** When one lineage overgrows (e.g. GABAergic neurons reaching >50% of cells in severe SUV420H1/ARID1B organoids), proportions of *other* cell types are mechanically depressed, making it hard to call independent effects on those populations (the authors explicitly leaned on milder backgrounds to detect the DL-PN phenotype). Proportional scRNA-seq compositional data is inherently relative — convergence is inferred from cell-type *proportions* and pseudotime, not absolute counts.
- **Expressivity confounds.** Donor lines differ in baseline risk-protein expression and carry incidental CNVs (e.g. chr19 CNV in a Mito294 ARID1B control; chr20q duplication in GM08330); phenotype severity is line-dependent and can fully resolve over time, so a null in one background ≠ no effect, and snapshot time points may miss transient phenotypes.
- **Molecular convergence is statistical/network-level.** "Shared higher-order processes" rests on GO-term and PPI-network overlap of largely non-overlapping gene/protein lists; the actual converging mechanism is not directly demonstrated.
- **Functional data are narrow.** Circuit-activity (calcium/MEA) abnormalities were characterized mainly in `SUV420H1+/−` (PGP1); whether ARID1B and CHD8 produce the same circuit-level phenotype was not directly shown. Organoids also lack later-stage maturation, vascularization, and non-cortical inputs.
