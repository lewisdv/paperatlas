---
title: "Transcriptome-wide isoform-level dysregulation in ASD, schizophrenia, and bipolar disorder."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1126/science.aat8127
pmid: 30545856
authors: Gandal MJ et al.
journal: Science (New York, N.Y.) (2018)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Transcriptome-wide isoform-level dysregulation in ASD, schizophrenia, and bipolar disorder.

## Source

- Authors: Gandal MJ, Zhang P, Hadjimichael E, Walker RL, Chen C, Liu S, Won H, van Bakel H et al.; PsychENCODE Consortium. Senior/corresponding: Daniel H. Geschwind, Dalila Pinto, Lilia M. Iakoucheva, Chunyu Liu.
- Journal: Science (New York, N.Y.) (2018); Science 362, eaat8127.
- DOI: [10.1126/science.aat8127](https://doi.org/10.1126/science.aat8127)
- PMID: [30545856](https://pubmed.ncbi.nlm.nih.gov/30545856/)
- Added via: manuscript_brain_organoid_v6 reference ingest
- Resource: interactive data at Resource.PsychENCODE.org.

## Abstract

Most genetic risk for psychiatric disease lies in regulatory regions, implicating pathogenic dysregulation of gene expression and splicing. However, comprehensive assessments of transcriptomic organization in diseased brains are limited. In this work, we integrated genotypes and RNA sequencing in brain samples from 1695 individuals with autism spectrum disorder (ASD), schizophrenia, and bipolar disorder, as well as controls. More than 25% of the transcriptome exhibits differential splicing or expression, with isoform-level changes capturing the largest disease effects and genetic enrichments. Coexpression networks isolate disease-specific neuronal alterations, as well as microglial, astrocyte, and interferon-response modules defining previously unidentified neural-immune mechanisms. We integrated genetic and genomic data to perform a transcriptome-wide association study, prioritizing disease loci likely mediated by cis effects on brain expression. This transcriptome-wide characterization of the molecular pathology across three major psychiatric disorders provides a comprehensive resource for mechanistic insight and therapeutic development.

## Key findings

**Cohort.** PsychENCODE postmortem frontal/temporal cortex RNA-seq across 8 uniformly-processed studies: **2,188 samples passing QC from 1,695 individuals** (+279 technical replicates). Diagnostic n (per graphical abstract): ASD = 51, SCZ = 559, BD = 222, controls = 936. Detected 16,541 protein-coding + 9,233 noncoding genes (Gencode v19). 28 surrogate variables + sequencing metrics as covariates; DE not driven by RNA-degradation confounds.

**Pervasive differential expression — >25% of the transcriptome.**
- **Differential gene expression (DGE), FDR < 0.05:** ASD 1,611 genes; SCZ 4,821; BD 1,119. >1/4 of the brain transcriptome affected in ≥1 disorder.
- **Transcriptomic-severity gradient ASD > SCZ > BD:** ASD mean |log2FC| 0.26 vs SCZ 0.10 and BD 0.15 (both p < 2×10⁻¹⁶).
- Strong concordance with prior microarray meta-analysis (Spearman ⍴ of log2FC: ASD 0.80, SCZ 0.78, BD 0.64) and prior RNA-seq (ASD 0.96, SCZ 0.78–0.80, BD 0.85).

**Isoform level carries the largest effect and most disease specificity (core thesis).**
- **Differential transcript expression (DTE), FDR < 0.05:** ASD 767, SCZ 3,803, BD 248 isoforms.
- Isoform-level effect sizes **larger** than gene-level: mean |log2FC| **0.25 (isoform) vs 0.14 (gene)**, p < 2×10⁻¹⁶ (esp. protein-coding).
- **Cross-disorder overlap is significantly attenuated at the DTE level** vs DGE → alternative transcript usage/splicing confers disease specificity.
- Isoform-only DE (no DGE signal): 811 SCZ, 294 ASD, 60 BD; biased to down-regulation, enriched in excitatory neurons (OR > 4), neuron-projection/mRNA-metabolism/synaptic pathways. PCR-validated.

**Local splicing dysregulation (LeafCutter).** 515 DS intron clusters in 472 genes (FDR < 0.1); 25% contain previously unidentified exons. Most common event = exon skipping (41–60%). Cross-disorder PSI correlation Spearman ⍴ = 0.59 (SCZ-BD), 0.52 (SCZ-ASD); only 2 genes (DTNA, AHCYL1) differentially spliced in all three. RT-PCR validated for 9 genes.

**Noncoding transcriptome.** 944 "neuropsychiatric ncRNAs" (NPncRNAs) DE in ≥1 disorder (693 SCZ, 178 ASD, 174 BD); under greater selective constraint than ncRNAs overall; 74 (~8%) under purifying selection (exon CDTS < 10th percentile). Examples: LINC00996 (microglia-restricted, down in SCZ/BD), LINC00634 (brain-enriched, down SCZ, genome-wide-significant SCZ TWAS hit).

**Cross-disorder convergence vs specificity.** Shared (often glial/immune) signal at the gene/module level, increasing specificity as analysis moves gene → isoform → network. Quantified cross-disorder PSI/expression correlations above; the ASD>SCZ>BD severity gradient recurs for down-regulated neuronal/synaptic pathways.

**Genetic-driver integration.**
- **Polygenic risk score (PRS):** 18 genes/isoforms with expression significantly associated with PRS (16 ASD — mostly 17q21.31; 2 SCZ — including the established risk gene **C4A**, up-regulated, correlated with imputed C4A copy number R = 0.36).
- **TWAS** (14,750 genes with heritable cis-regulated brain expression): BD 17 genes / 14 loci; ASD 12 genes / 3 loci (conditional analysis → **LRRC37A** at 17q21.31, supported by SMR + fetal-brain Hi-C); SCZ 193 genes (107 after conditioning). Validated with summary-data Mendelian randomization (SMR) + HEIDI.
- **Consistently prioritized across methods: 5 candidate genes in ASD, 11 in BD, 64 in SCZ** (incl. 10 ncRNAs). Most disease-specific; only 4 shared SCZ↔BD (MCHR1, VPS45, SNAP91, DCLK3), none shared with ASD. 60 SCZ TWAS genes overlap the 321 high-confidence SCZ risk genes from the companion deep-learning/regulatory-network manuscript (OR = 34.7, p < 10⁻⁶⁰).

**Networks (WGCNA).** Combined 90 modules (34 gene-level + 56 isoform-level); 61 (68%) associated with ≥1 disorder. **Isoform-level networks captured more disease GWAS signal than gene-level (61% vs 41% nominal GWAS enrichment).** 5 modules shared across all three disorders (3 up, 2 down) — including an up-regulated **NFkB inflammatory** module and a shared down-regulated **endothelial/blood-brain-barrier** module (hubs ITIH5, SLC38A5, ABCB1, GPR124). 41 of 61 disease modules show cell-type enrichment → neural-immune mechanisms (microglia, astrocyte, interferon-response) plus a medication-exposure module enriched for activity-dependent immediate-early genes.

## Methods

- **Data:** PsychENCODE postmortem cortex RNA-seq, 8 studies, consolidated pipeline; Gencode v19. QC + 28 surrogate variables.
- **Levels analyzed:** gene (DGE), transcript isoform (DTE, RSEM-quantified), local splicing (DS, LeafCutter de novo), and coexpression networks — for both protein-coding and noncoding biotypes.
- **Validation:** PCR/RT-PCR for selected DTE and DS events; concordance vs prior microarray and RNA-seq datasets.
- **Genetic integration:** PRS association; TWAS (FUSION-style cis-expression weights); SMR + HEIDI; stratified LD-score regression for module GWAS heritability enrichment; Hi-C for locus fine-mapping.

## Relevance to the brain-organoid ASD review

Supports the manuscript's **transcriptomic dysregulation / cross-disorder convergence** theme (not a Stage-1 Design tool — it is the downstream phenotype evidence the Design tools are trying to predict). Key alignments:
- **Isoform/splicing-level changes carry the largest disease effect and most genetic enrichment** in patient brain — independent validation of *why* the review pairs a splicing prioritizer ([SpliceAI](Jaganathan_2019_Predicting_Splicing_Primary_Sequence_Deep_Learning.md)) with a missense prioritizer ([AlphaMissense](Cheng_2023_Accurate_proteome_wide_missense_variant_effect_prediction.md)) at the Design stage. Gene-level analysis alone misses ~294 ASD isoform-only DE transcripts.
- **Cross-disorder convergence** (shared NFkB/inflammatory, blood-brain-barrier, neuronal/synaptic modules across ASD/SCZ/BD) provides the molecular-convergence backbone the review invokes: ASD-prioritized variants are expected to funnel onto shared dysregulated programs that an organoid can read out transcriptomically.
- Provides a **patient-brain reference transcriptome** against which organoid models of prioritized ASD variants can be benchmarked for convergent dysregulation.

## Open questions / limitations

- **ASD is the smallest arm (n ≈ 51 cases)** — ASD-specific DTE/DS/TWAS power is limited (BD splicing "likely still underpowered"); many ASD findings concentrate at 17q21.31, a structurally complex locus where common variants tag an inversion (interpretation caveat).
- **Postmortem adult/postnatal cortex, bulk tissue** — captures end-state, not the developmental window or single-cell resolution most relevant to ASD onset; cell-type signals are computationally deconvolved, not directly measured. (Directly motivates organoid + single-cell follow-up.)
- **Correlative / cis-regulatory:** TWAS and SMR prioritize candidate genes but remain influenced by LD and pleiotropy; associations are not mechanistic proof.
- **TWAS weights partly derived from non-CNS tissue** (limited brain eQTL data at the time), and ncRNA functions are largely unannotated.
- Convergence vs specificity is quantified but the *causal direction* (cause vs consequence vs medication effect — note the explicit medication-exposure module) is not resolved.

## Cross-links

- [SpliceAI (Jaganathan 2019)](Jaganathan_2019_Predicting_Splicing_Primary_Sequence_Deep_Learning.md) — variant-level splicing prediction; Gandal supplies the brain-level evidence that splicing/isoform changes dominate disease effect.
- [AlphaMissense (Cheng 2023)](Cheng_2023_Accurate_proteome_wide_missense_variant_effect_prediction.md) — coding-variant prioritization upstream of the expression/isoform consequences mapped here.
