---
title: "Predicting Splicing from Primary Sequence with Deep Learning."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.cell.2018.12.015
pmid: 30661751
authors: Jaganathan K et al.
journal: Cell (2019)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Predicting Splicing from Primary Sequence with Deep Learning.

## Source

- Authors: Jaganathan K, Kyriazopoulou Panagiotopoulou S, McRae JF, Darbandi SF, Knowles D, Li YI, Kosmicki JA, Arbelaez J et al.
- Journal: Cell (2019)
- DOI: [10.1016/j.cell.2018.12.015](https://doi.org/10.1016/j.cell.2018.12.015)
- PMID: [30661751](https://pubmed.ncbi.nlm.nih.gov/30661751/)
- Added via: manuscript_brain_organoid_v6 reference ingest
- Tool introduced: **SpliceAI** (open source, github.com/Illumina/SpliceAI; precomputed delta scores for all genome-wide SNVs released). From the Illumina AI Lab; lead contact Kyle Kai-How Farh; co-authors include Stephan J. Sanders (autism genetics).

## Abstract

The splicing of pre-mRNAs into mature transcripts is remarkable for its precision, but the mechanisms by which the cellular machinery achieves such specificity are incompletely understood. Here, we describe a deep neural network that accurately predicts splice junctions from an arbitrary pre-mRNA transcript sequence, enabling precise prediction of noncoding genetic variants that cause cryptic splicing. Synonymous and intronic mutations with predicted splice-altering consequence validate at a high rate on RNA-seq and are strongly deleterious in the human population. De novo mutations with predicted splice-altering consequence are significantly enriched in patients with autism and intellectual disability compared to healthy controls and validate against RNA-seq in 21 out of 28 of these patients. We estimate that 9%-11% of pathogenic mutations in patients with rare genetic disorders are caused by this previously underappreciated class of disease variation.

## Key findings

**Architecture.** SpliceAI is a 32-layer deep residual neural network (dilated convolutions, ResNet-style) that takes only the genomic pre-mRNA sequence as input and classifies each position as splice **donor**, **acceptor**, or **neither**. The flagship model, **SpliceAI-10k**, uses **10,000 nt of flanking context** (5,000 nt each side) per predicted position; this long context is what lets it resolve true junctions from the vast number of near-optimal but nonfunctional motifs. No human-engineered features; trained only on GENCODE reference transcripts + junction annotations on a subset of chromosomes, tested on held-out chromosomes (paralogs excluded). **Never saw variant data during training** — variant effect prediction is therefore an out-of-distribution generalization test.

**Splice-site prediction accuracy.**
- **95% top-k accuracy** on held-out protein-coding test transcripts (top-k = fraction correct at the threshold where #predicted sites = #actual sites). Large genes (e.g. CFTR, >100 kb) reconstructed to near-nucleotide precision.
- **84% top-k accuracy** on lincRNAs (free of protein-coding selective pressure), arguing the model approximates the spliceosome rather than exploiting exonic sequence bias.
- Exon prediction scores correlate with GTEx RNA-seq exon-inclusion rate (**Pearson r = 0.78**); constitutive exons score near 1 or 0, alternatively-spliced exons (10–90% inclusion) score intermediate.
- Context size matters: SpliceAI-80nt (local-motif model) underperforms; long-range determinants (exon/intron length, nucleosome positioning learned implicitly, Spearman 0.36 with nucleosome occupancy) confer specificity.

**Variant scoring (delta / "Δ score").** For a variant, SpliceAI scores the reference and alternate sequences and takes the largest change in donor/acceptor probability within 50 nt → Δ score in [0,1] for acceptor/donor gain or loss. Δ score thresholds 0.2 / 0.5 / 0.8 trade sensitivity for precision.

**Cryptic-splice validation on RNA-seq (GTEx, 149 individuals with WGS + RNA-seq).**
- Confidently predicted cryptic-splice variants (Δ ≥ 0.5) validate on RNA-seq at **~3/4 (75%) the rate of essential GT/AG dinucleotide disruptions**; validation rate and effect size track the Δ score.
- Sensitivity at Δ ≥ 0.5: **71% near exons** vs **41% deep intronic** (>50 nt from boundary) — deep intronic variants are the hard case.
- Substantially outperforms prior classifiers GeneSplicer, MaxEntScan, NNSplice (which lack specificity given the huge genome-wide search space because they model only local motifs).

**Population genetics (ExAC 60,706 exomes; gnomAD 15,496 genomes).**
- High-confidence (Δ ≥ 0.8) synonymous/intronic cryptic-splice variants are depleted **78%** at common allele frequency (≥0.1%) vs singletons (odds ratio 4.58, p < 10⁻¹²⁷) — i.e. ~78% are deleterious enough to be removed by selection, comparable to the **82%** depletion of frameshift/stop-gain/essential-splice variants.
- Deep intronic high-confidence variants depleted **56%** (consistent with harder prediction).
- Average human carries **~5 rare functional cryptic-splice mutations** vs **~11 rare protein-truncating variants**; cryptic-splice outnumber essential GT/AG disruptions ~2:1.

**Disease enrichment (de novo mutations).** Cohorts: 4,293 intellectual-disability (DDD), 3,953 ASD (Simons Simplex + Autism Sequencing Consortium), 2,073 unaffected sibling controls; ascertainment normalized by synonymous rate.
- Predicted splice-disrupting de novo mutations enriched **1.51-fold in intellectual disability** (p = 4.16×10⁻⁴) and **1.30-fold in ASD** (p = 0.0203) over controls (Δ ≥ 0.1); enrichment holds even when restricted to synonymous + intronic mutations.
- Estimated **~11% of pathogenic de novo mutations in ASD and ~9% in intellectual disability** are cryptic-splice (the "9%–11%" headline). Adding cryptic-splice to coding-variant gene-discovery yielded 5 extra ID genes and 2 extra ASD genes at FDR < 0.01.
- Functional cryptic-splice mutations have **~50% the clinical penetrance** of classic protein-truncating variants (their case-vs-control effect is ~38% as large), because many only partially shift splicing (hypomorphic; most disease de novos had Δ < 0.5).

**Experimental validation in ASD patients.** Deep mRNA-seq (~350M reads/sample, ~10× GTEx) of lymphoblastoid cell lines from 36 Simons Simplex probands carrying predicted de novo cryptic-splice variants. After excluding 8 with insufficient coverage, aberrant splicing matching the prediction was confirmed in **21/28 patients (75%)** — 9 novel-junction creation, 8 exon skipping, 4 intron retention, plus complex events.

## Methods

- **Training/testing:** GENCODE-annotated pre-mRNA transcripts; train on subset of chromosomes, test on the rest with paralogs excluded; lincRNAs as an annotation-light generalization test. An "augmented" model additionally trained on GENCODE + GTEx-derived junctions improves variant prediction by filling annotation gaps.
- **Variant scoring:** reference vs alternate sequence scored; Δ score = max change in splice probability within 50 nt of the variant.
- **Orthogonal validation (three independent axes, deliberately chosen because the model never trained on variants):** (1) GTEx RNA-seq validation/sensitivity of private variants; (2) negative-selection depletion in ExAC/gnomAD (singleton vs common AF); (3) case-vs-control de novo enrichment in DDD/ASD with RNA-seq confirmation in patient LCLs. Overfitting controls: private vs common variants, training vs test chromosomes, and motif-class splits all show no significant difference in validation rate/sensitivity.
- **Benchmarks:** GeneSplicer, MaxEntScan, NNSplice compared at matched prediction counts.
- **Resource:** precomputed Δ scores for all possible genome-wide single-nucleotide substitutions released to the community.

## Relevance to the brain-organoid ASD review

SpliceAI is a **named Stage-1 ("Design") computational tool** in the manuscript ("Programmable Brain Organoids for Proactive Autism Genetics") — specifically the **splicing-prediction** prioritizer used to nominate which candidate variants are worth building into organoid models. Its strengths map directly onto the review's Design rationale:
- It surfaces a class of variant (cryptic/noncoding splice) that exome-only pipelines miss but that accounts for **~9–11% of pathogenic mutations in ASD/ID** — a meaningful expansion of the candidate space for proactive modeling.
- It is **phenotype-agnostic and trained only on reference sequence**, so its predictions are de novo mutation calls that still require functional confirmation — exactly the role an organoid (with its developing-brain context) can play downstream.

**Stated limits the review flags / that the paper itself raises:**
- **Reduced accuracy on deep intronic variants** (41% sensitivity vs 71% near exons; only 56% population depletion deep-intronic) — the canonical "non-coding accuracy" caveat. The further a variant is from annotated exon boundaries, the weaker the prediction.
- **Phenotype- and cell-type-agnostic:** SpliceAI predicts *whether* splicing changes, not *which tissue/cell type* is affected or whether the consequence is pathogenic for ASD. Many validated variants are incompletely penetrant and produce a *mixture* of normal + aberrant transcripts, and cryptic-splice effects are frequently **tissue-specific** (35% of weak/intermediate Δ 0.35–0.8 variants vary across tissues). The relevant tissue (developing brain) is usually inaccessible — motivating organoid validation.
- It is a **predictor, not a mechanism for the disease phenotype**; cuts ~50% penetrance relative to protein-truncating variants mean a positive SpliceAI call is a hypothesis to be tested, not a diagnosis.

## Open questions / limitations

- **Deep intronic and trans-acting splicing** remain poorly predicted; the model captures local + long-range *cis* sequence but not variants that act through spliceosome proteins or distal regulators.
- **Black-box risk:** the authors explicitly note deep nets may learn features that inflate annotation accuracy without reflecting true spliceosome biology; they mitigate by three orthogonal variant validations, but this "does not fully preclude" irrelevant features.
- **Tissue/developmental specificity not modeled** in this version — a proposed future direction is training on RNA-seq junctions from the relevant tissue to obtain tissue-specific alternative-splicing models. Directly relevant to brain-specific ASD modeling.
- **Penetrance heterogeneity:** many predicted variants are hypomorphic; the framework does not quantify per-variant penetrance, only population-level deleteriousness.
- Validation tissue was LCLs, not brain; 7/28 patients showed no aberrant splicing in LCLs (some may be false positives, some tissue-specific) — an empirical false-positive/tissue-specificity ceiling on the predictions.

## Cross-links

- [AlphaMissense (Cheng 2023)](Cheng_2023_Accurate_proteome_wide_missense_variant_effect_prediction.md) — the companion Stage-1 *missense* prioritizer (this one covers *splicing*); both are phenotype-agnostic Design-stage tools in the review.
- [Gandal 2018 isoform-level dysregulation](Gandal_2018_Transcriptome_wide_isoform_level_dysregulation_ASD_schizophrenia.md) — independent evidence that splicing/isoform-level changes carry the largest disease effect in ASD/SCZ/BD brain, complementing SpliceAI's variant-level splicing focus.
