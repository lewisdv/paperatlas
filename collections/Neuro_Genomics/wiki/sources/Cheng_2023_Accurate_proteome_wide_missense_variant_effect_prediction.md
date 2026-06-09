---
title: "Accurate proteome-wide missense variant effect prediction with AlphaMissense."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1126/science.adg7492
pmid: 37733863
authors: Cheng J et al.
journal: Science (New York, N.Y.) (2023)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Accurate proteome-wide missense variant effect prediction with AlphaMissense.

## Source

- Authors: Cheng J, Novati G, Pan J, Bycroft C, Žemgulytė A, Applebaum T, Pritzel A, Wong LH et al. (Google DeepMind).
- Journal: Science (New York, N.Y.) (2023); Science 381, eadg7492.
- DOI: [10.1126/science.adg7492](https://doi.org/10.1126/science.adg7492)
- PMID: [37733863](https://pubmed.ncbi.nlm.nih.gov/37733863/)
- Added via: manuscript_brain_organoid_v6 reference ingest
- Tool introduced: **AlphaMissense** — AlphaFold fine-tuned for missense pathogenicity; proteome-wide prediction database released as a community resource.

## Abstract

The vast majority of missense variants observed in the human genome are of unknown clinical significance. We present AlphaMissense, an adaptation of AlphaFold fine-tuned on human and primate variant population frequency databases to predict missense variant pathogenicity. By combining structural context and evolutionary conservation, our model achieves state-of-the-art results across a wide range of genetic and experimental benchmarks, all without explicitly training on such data. The average pathogenicity score of genes is also predictive for their cell essentiality, capable of identifying short essential genes that existing statistical approaches are underpowered to detect. As a resource to the community, we provide a database of predictions for all possible human single amino acid substitutions and classify 89% of missense variants as either likely benign or likely pathogenic.

## Key findings

**Problem.** Of >4 million observed human missense variants, only **~2%** have been clinically classified (pathogenic/benign); the rest are variants of unknown significance (VUS). AlphaMissense aims to close this gap.

**Architecture (AlphaFold-based).** Closely follows AlphaFold (AF2): inputs are the reference protein sequence (cropped to L = 256 residues), up to 50 sampled training variants, and an MSA (up to 2,048 sequences) processed by a **48-layer Evoformer** with recycling. It does **not** predict the mutated structure; it outputs a **scalar pathogenicity score** as the log-likelihood difference between the reference and alternate amino acid at the masked variant position. Two-stage training:
1. **AF pretraining** — single-chain structure prediction + masked protein-language-modeling (higher weight on masked-MSA reconstruction), retaining AF-level structure accuracy.
2. **Variant fine-tuning** — weak-label classification: **benign** = variants frequent in human/primate populations; **pathogenic** = variants absent from human/primate populations (the PrimateAI strategy). Avoids circularity by **never training on human-curated clinical labels (e.g. ClinVar)**. Adds self-distillation, matched trinucleotide-context sampling, MAF-weighted loss, weight decay toward pretrained values. Final score = average of 6 models (3 trained models × 2 MSA-diversity settings); calibrated via logistic regression on a balanced 2,526-variant ClinVar set so scores approximate P(pathogenic).

**Clinical benchmark accuracy (ClinVar AUC).**
- **ClinVar held-out test: auROC = 0.940** on 18,924 class-balanced variants (9,462 pathogenic / 9,462 benign, 999 proteins), vs **0.911 for EVE** (next-best model not trained on ClinVar; p = 0.001). Outperforms even models trained directly on ClinVar (which suffer data leakage).
- **Per-gene auROC = 0.950** (612 genes with ≥5 pathogenic + ≥5 benign) vs 0.921 EVE.
- **DDD de novo developmental-disorder variants: auROC = 0.809** (353 patient + 57 control variants, 215 genes), on par with PrimateAI (0.797, p = 0.31).
- **Cancer hotspots: auROC = 0.907** vs 0.885 (VARITY). State-of-the-art across all curated clinical benchmarks; no prior model ranks consistently high across all of them.

**Proteome-wide predictions + % variants classified.**
- Predicted all **216 million** possible single-amino-acid changes across **19,233 canonical human proteins** → **71 million missense variants** saturating the proteome.
- Using cutoffs at **90% precision on ClinVar**: **32% (22.8M) classified likely pathogenic, 57% (40.9M) likely benign → 89% confidently classified** (the headline; ~11% ambiguous). Cutoff is user-adjustable.
- This is a **+25.8 percentage-point** gain in confidently classifiable ClinVar test variants vs EVE (**67.1% → 92.9%** resolved at 90% precision).
- Of 69.5M variants unobserved in gnomAD, **88.8% (61.7M)** received a confident call.

**Agreement with experimental assays (MAVEs).** Without training on assay data:
- Highest mean Spearman correlation with **ProteinGym** (72 proteins, ~1.5M variants): **0.514** (0.474 on the 25-human-protein all-methods subset), beating ESM1b/ESM1v/EVE/GEMME; improves over next-best on 62/72 proteins.
- Recovers functional sub-structure (e.g. SHOC2 RVxF motif, GCK catalytic D205 = highest-pathogenicity residue; per-position Spearman 0.64 for SHOC2).

**Gene-level signal → cell essentiality.** A gene's *average* AlphaMissense pathogenicity correlates with LOEUF (Spearman −0.48) and **predicts essential genes that LOEUF cannot** — i.e. **short genes** underpowered for constraint metrics (~22% / ~4,000–4,252 protein-coding genes too small for LOEUF). Classifying cell-essential vs non-essential among LOEUF-underpowered genes: **auROC 0.88 vs 0.81 LOEUF** (p = 0.001); enrichment of essential genes in the most-pathogenic decile **5.9-fold** among small genes (e.g. correctly flags small spliceosome subunits PHF5A/SF3B5/SF3B6 that LOEUF misses).

**Complex-trait utility.** In UK Biobank (~4,000 traits), rare (MAF < 0.01) variants called likely-pathogenic carry **2× the trait associations of synonymous variants** and a rate statistically indistinguishable from pLoF variants (p = 0.43); combining AlphaMissense-pathogenic + pLoF expands candidate deleterious rare variants **3.2-fold** (~7,000 additional genes testable in gene-based association).

## Methods

- **Inputs:** reference sequence (crop L = 256), masked variant position(s), MSA (≤2,048). Inference one variant at a time.
- **Training labels (weak, no human curation):** benign from human/primate population frequency (MAF-stratified, downweighting rare variants); pathogenic from unobserved human variants, count-matched by trinucleotide context and gene to remove gene bias. Self-distillation filters likely-benign "pathogenic" labels and repeats fine-tuning.
- **Model selection:** small balanced ClinVar set (~1,263 pathogenic + 1,263 benign) used only for early stopping / hyperparameters and calibration — *not* as training signal.
- **Calibration:** univariate logistic regression on balanced ClinVar → scores in [0,1] ≈ probability of clinical pathogenicity. Three discrete classes (likely benign / ambiguous / likely pathogenic) at cutoffs giving 90% precision (ACMG-like).
- **Ablations:** both AF pretraining and fine-tuning are essential; masked-MSA pretraining *without* structure loss is insufficient — i.e. **structure prediction contributes materially**. Variant-count sampling reduces gene bias.
- **Released resources:** (1) 71M proteome-wide missense predictions; (2) gene-level mean pathogenicity; (3) all 216M amino-acid substitutions; (4) predictions across ~60,000 alternative transcript isoforms. Usable alongside the AlphaFold Structure Database.

## Relevance to the brain-organoid ASD review

AlphaMissense is a **named Stage-1 ("Design") computational tool** in the manuscript ("Programmable Brain Organoids for Proactive Autism Genetics"), **central to the Design stage** as the **missense** variant prioritizer. It is the structural/protein-coding counterpart to [SpliceAI](Jaganathan_2019_Predicting_Splicing_Primary_Sequence_Deep_Learning.md) (splicing). Why it fits proactive ASD organoid modeling:
- ASD risk is heavily driven by de novo coding (largely missense) variants; AlphaMissense converts ~89% of the proteome's VUS into confident calls, sharply shrinking the candidate set worth building into organoids.
- Strong on the most relevant clinical axis: **DDD de novo developmental-disorder variants (auROC 0.809)** and gene-level **essentiality including short genes** that population-constraint metrics (LOEUF) miss — useful for nominating dose-sensitive ASD genes.
- Editorial framing ("proactive" maps of variant effect via MAVEs) parallels the review's proactive-modeling thesis: AlphaMissense provides the in-silico prior, the organoid provides the in-context functional test.

**Stated limits the review flags / paper-acknowledged:**
- **Phenotype-agnostic:** predicts whether a missense variant is *pathogenic to protein function*, not the specific ASD/neurodevelopmental phenotype, affected cell type, or developmental window. A high score is a prioritization signal, not a mechanism — exactly the gap organoid functional readouts are meant to fill.
- **Non-coding blind spot:** AlphaMissense scores **only missense (single-amino-acid) coding changes** — it says nothing about regulatory/non-coding or splicing variants (hence the review pairs it with SpliceAI). This is the missense analogue of the review's "non-coding accuracy" concern.
- **Calibration weakest in the middle:** most scores sit near 0 or 1; calibration for scores **0.2–0.8 is explicitly less accurate**, and ~11% of variants remain "ambiguous."
- **Disordered regions:** reduced performance on residues AlphaFold predicts as intrinsically disordered (no structural context to exploit).
- **Gain-of-function / hyperactivating variants** are systematically under-called (e.g. GCK T65I causing hyperinsulinemic hypoglycemia tends to be classed ambiguous/benign) — the model is tuned to loss-of-function-style pathogenicity.

## Open questions / limitations

- **Weak-label noise:** "pathogenic" = "unobserved in populations," so many training "pathogenic" variants are actually benign; performance is validated on independent labels but the training signal is intrinsically noisy.
- **Does not predict mutant structure or molecular mechanism** — only a scalar score; it cannot tell you *how* a variant disrupts function (stability vs interface vs catalysis) beyond correlative structural context.
- **Isoform/context specificity:** predictions are largely on canonical isoforms (isoform-set released but evaluation limited); cell-type- and developmental-stage-specific effects relevant to ASD are out of scope.
- **Benchmarks carry human/clinical ascertainment bias** (ClinVar, DDD), which may not represent the true clinical-variant distribution.
- Gain-of-function, dominant-negative, and dosage-specific effects are not well modeled — a known ceiling for neurodevelopmental genes where these mechanisms matter.

## Cross-links

- [SpliceAI (Jaganathan 2019)](Jaganathan_2019_Predicting_Splicing_Primary_Sequence_Deep_Learning.md) — companion Stage-1 prioritizer for *splicing/noncoding* variants; together they cover the coding (this) + splice axes of the review's Design stage.
- [Gandal 2018 isoform-level dysregulation](Gandal_2018_Transcriptome_wide_isoform_level_dysregulation_ASD_schizophrenia.md) — downstream transcriptomic-convergence evidence; AlphaMissense prioritizes the *variants*, Gandal characterizes the *expression/isoform* consequences in patient brain.
