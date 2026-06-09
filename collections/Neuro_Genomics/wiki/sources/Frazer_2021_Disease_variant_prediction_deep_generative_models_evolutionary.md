---
title: "Disease variant prediction with deep generative models of evolutionary data."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41586-021-04043-8
pmid: 34707284
authors: Frazer J et al.
journal: Nature (2021)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Frazer_2021_Disease_variant_prediction_deep_generative_models_evolutionary.pdf
pdf_status: downloaded
---

# Disease variant prediction with deep generative models of evolutionary data.

## Source

- Authors: Frazer J, Notin P, Dias M, Gomez A, Min JK, Brock K, Gal Y, Marks DS
- Journal: Nature (2021)
- DOI: [10.1038/s41586-021-04043-8](https://doi.org/10.1038/s41586-021-04043-8)
- PMID: [34707284](https://pubmed.ncbi.nlm.nih.gov/34707284/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Quantifying the pathogenicity of protein variants in human disease-related genes would have a marked effect on clinical decisions, yet the overwhelming majority (over 98%) of these variants still have unknown consequences1-3. In principle, computational methods could support the large-scale interpretation of genetic variants. However, state-of-the-art methods4-10 have relied on training machine learning models on known disease labels. As these labels are sparse, biased and of variable quality, the resulting models have been considered insufficiently reliable11. Here we propose an approach that leverages deep generative models to predict variant pathogenicity without relying on labels. By modelling the distribution of sequence variation across organisms, we implicitly capture constraints on the protein sequences that maintain fitness. Our model EVE (evolutionary model of variant effect) not only outperforms computational approaches that rely on labelled data but also performs on par with, if not better than, predictions from high-throughput experiments, which are increasingly used as evidence for variant classification12-16. We predict the pathogenicity of more than 36 million variants across 3,219 disease genes and provide evidence for the classification of more than 256,000 variants of unknown significance. Our work suggests that models of evolutionary information can provide valuable independent evidence for variant interpretation that will be widely useful in research and clinical settings.

## Key findings

- **EVE = unsupervised deep generative model.** EVE (Evolutionary model of Variant Effect) predicts missense pathogenicity **without any disease labels**, learning only from the distribution of natural sequence variation across species. This sidesteps the label bias, label sparsity, label noise, and data-leakage circularity that inflate the apparent accuracy of supervised predictors (the paper's central methodological argument; ACMG/AMP guidelines currently treat computational predictors as only "weak evidence").
- **Accuracy vs ClinVar.** Average **AUC = 0.91** against known ClinVar clinical labels across all **3,219** disease genes; **AUC = 0.92** on the subset of 60 ACMG "clinically actionable" genes. Performance is robust to the number of labels per gene (supporting generalization to poorly annotated / unlabelled genes).
- **Beats all benchmarked predictors.** EVE outperforms **all 7 unsupervised and 8 supervised** state-of-the-art variant-effect predictors on ClinVar AUC, and also on a second, less-biased benchmark of ~40,000 experimentally measured variants across 10 proteins (Spearman correlation vs deep mutational scans). Named comparators include CADD, PolyPhen-2 (HVAR/HDIV), SIFT, PROVEAN, PrimateAI, MPC, REVEL, M-CAP, DEOGEN2, MutationAssessor, MutationTaster, FATHMM, LRT, DANN, LIST-S2. EVE also beats supervised meta-predictors.
- **On par with / better than experimental MAVEs.** For the 5 genes with abundant high-quality ClinVar labels (**BRCA1, TP53, PTEN, MSH2, SCN5A**), EVE matches or beats the purpose-built deep mutational scans. Per-gene EVE-vs-experiment AUCs reported: e.g. **0.95, 1.0, 0.99, 0.97, 0.85, 0.82** across panels (Fig. 3); for TP53, EVE separated benign/pathogenic across the whole protein where the experiment was weak in the tetramerization domain (positions ~300+). For SCN5A, EVE called R814Q pathogenic even though it is a gain-of-function in the assay — suggesting evolutionary data carry GoF as well as LoF signal.
- **Discordance analysis favours EVE.** Across MSH2, PTEN, TP53, in **23 of 27 (85%)** variants where EVE disagrees with ClinVar, the MAVE experimental data side with EVE rather than ClinVar.
- **Genome-scale predictions.** EVE provides continuous scores [0,1] and benign/uncertain/pathogenic class calls for **>36 million** single–amino-acid variants across the 3,219 genes. Of these, ~1.3M have been observed in ≥1 human (UK Biobank + gnomAD) but only ~3% have any ClinVar interpretation. After dropping the **25% most uncertain** variants (holding accuracy at ~90%), EVE interprets ~27M variants total, including ~64% (>800,000) of the variants seen to date in humans.
- **Reclassification evidence.** Combining EVE with population data and other evidence yields **>256,000** previously uninterpreted variants flagged for potential reclassification, plus **539** variants whose EVE-supported call contradicts current ClinVar status (e.g. TP53 R337Q).

## Methods

- **Two-stage model, per protein.** (1) A **Bayesian variational autoencoder (VAE)** is trained on a multiple-sequence alignment (MSA) for each protein, learning a distribution over amino-acid sequences that captures position-specific constraints and inter-position dependencies. Architecture: symmetric 3-layer encoder/decoder (2000–1000–300 units), latent dimension 50, one-hot sequence input, 1-D convolution on decoder output, softmax over amino acids; trained by maximizing the ELBO. (2) The **"evolutionary index"** of each variant ≈ the negative log-likelihood ratio of mutant vs wild-type, estimated by sampling 2,000× from the approximate posterior and ensembling over 5 independently trained VAEs.
- **Unsupervised class assignment.** A two-component **global–local Gaussian mixture model** is fit to the distribution of evolutionary indices across all variants (the benign/pathogenic separating value is consistent across proteins). Output = continuous EVE score + benign/uncertain/pathogenic class, with predictive entropy of the GMM used as a per-variant **uncertainty** measure, enabling an accuracy-vs-coverage trade-off (e.g. set aside 25% most uncertain → ~90% accuracy).
- **Data.** MSAs built with HMMER 3.1b2 by searching ~250M sequences in UniRef; the models draw on sequences from >140,000 organisms. Validation against ClinVar labels and against published DMS/MAVE datasets (BRCA1, TP53, PTEN, MSH2, SCN5A). Implemented in Python 3.7 / PyTorch 1.4.
- **Availability.** Code at github.com/OATML-Markslab/EVE; scores/MSAs at evemodel.org.

## Relevance to the brain-organoid ASD review

- **EVE is one of the review's named Stage-1 (in silico Design) variant-prioritization tools.** It exemplifies the unsupervised, evolution-based predictor class that the review positions as the first computational filter for nominating candidate variants before functional follow-up.
- **Frames the computation→experiment pipeline the review extends to organoids.** Frazer's own thesis is that an in silico predictor can match purpose-built MAVEs and is best used to *prioritize which variants/genes are most informative to test experimentally* (Supplementary Table 7) — exactly the Stage-1 → Stage-2 logic the review applies to programmable brain organoids.
- **Calibrated uncertainty + gene-by-gene evidence weighting** maps onto the ACMG/AMP PS3/BS3 functional-evidence framework that this collection tracks (see [Brnich_2019](Brnich_2019_Recommendations_application_functional_evidence_PS3_BS3_criterion.md)). EVE provides an independent, orthogonal evidence stream to combine with experimental functional data.
- **Cross-links.** Saturation/DMS counterparts to EVE's protein-level scope in this collection: [Beltran_2025](Beltran_2025_Site_saturation_mutagenesis_500_human_protein_domains.md) (500 protein domains), [Findlay_2018](Findlay_2018_Accurate_classification_BRCA1_variants_saturation_genome_editing.md) (BRCA1 SGE — a Frazer benchmark gene), [Sahu_2025](Sahu_2025_Saturation_genome_editing_based_clinical_classification_BRCA2.md) (BRCA2). Related missense predictor: [Cheng_2023](Cheng_2023_Accurate_proteome_wide_missense_variant_effect_prediction.md) (AlphaMissense).

## Open questions / limitations

- **Mechanism opaque.** The authors state they do not know precisely how the sequence-derived constraints relate to disease; pathogenicity is inferred, not mechanistic.
- **Coding/missense only.** EVE covers single–amino-acid substitutions in protein-coding regions; it does not address non-coding/regulatory variants (the gap covered by MPRA work such as [Kircher_2019](Kircher_2019_Saturation_mutagenesis_twenty_disease_associated_regulatory_elements.md)). The authors flag functional RNA / splice variation (e.g. in MSH2) as a case where EVE–experiment concordance can be misleading.
- **No combinations / epistasis.** The model scores single variants; it does not address combinations of variants, despite ~12% of genes per person carrying ≥2 variants vs reference (≈21,000 distinct in-gene variant pairs across ACMG actionable genes, occurring ~1.5M times in UK Biobank).
- **Discrete pathology categories mask heterogeneity.** Same-gene (and even same-variant) differences in severity or distinct disease presentations are not captured by binary benign/pathogenic calls; whether the continuous EVE score predicts severity is explicitly called speculative.
- **MSA dependence.** Requires a sufficiently informative alignment; however, the paper notes no strong correlation between alignment depth (N/Lcov) and AUC — even some shallow alignments perform near-perfectly.
- **Coverage caveat.** Headline interpretive counts depend on discarding the 25% most-uncertain variants to hold accuracy near 90%; the accuracy/coverage trade-off is meant to be set per gene and per use case.
