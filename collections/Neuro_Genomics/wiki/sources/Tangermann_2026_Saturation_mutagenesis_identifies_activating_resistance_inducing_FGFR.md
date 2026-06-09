---
title: "Saturation mutagenesis identifies activating and resistance-inducing FGFR kinase domain mutations."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41588-025-02431-8
pmid: 41361008
authors: Tangermann C et al.
journal: Nature genetics (2026)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Tangermann_2026_Saturation_mutagenesis_identifies_activating_resistance_inducing_FGFR.pdf
pdf_status: downloaded
---

# Saturation mutagenesis identifies activating and resistance-inducing FGFR kinase domain mutations.

## Source

- Authors: Tangermann C, Ghosh A, Ziegler M, Facchinetti F, Stappenbeck J, Carus Sahin YO, Riester M, Viardot LC et al. (Diederichs S corresponding)
- Journal: Nature genetics (2026) 58:157–168
- DOI: [10.1038/s41588-025-02431-8](https://doi.org/10.1038/s41588-025-02431-8)
- PMID: [41361008](https://pubmed.ncbi.nlm.nih.gov/41361008/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Variants of uncertain significance represent the biggest challenge for genomics-based precision oncology. Activated fibroblast growth factor receptors (FGFRs) frequently drive tumorigenesis by different genetic aberrations. However, it remains unknown which of the many point mutations affecting FGFR1, FGFR2, FGFR3 or FGFR4 in cancer are druggable, that is, activating signaling while not mediating FGFR inhibitor resistance. Here we implemented a saturation mutational scanning platform to screen all 11,520 possible point mutations covering the kinase domains of FGFR1-4. Pooled positive selection screens identified 474 activating and 738 mutations mediating resistance to the FGFR inhibitors pemigatinib and futibatinib, together revealing 301 druggable FGFR mutations analogous to a strong PS3/BS3 evidence level. The screens also identified loss-of-function mutations and an association of gain-of-function mutations with hydrophobic changes. The functional screens identified 97% of acquired resistance mutations in clinical trials. Our comprehensive catalog of every druggable mutation in the FGFR kinase domains is readily available for clinical decision support.

## Key findings

- **Complete saturation of FGFR1-4 kinase domains.** Screened **all 11,520 possible single-nucleotide point mutations** (→ 7,524 amino-acid substitutions; 8,407 testable missense mutations) across the kinase domains of FGFR1, FGFR2, FGFR3, FGFR4. Motivation: COSMIC lists 1,749 FGFR kinase-domain mutations across these genes, but the Clinical Knowledge Base (CKB) has protein-effect annotation for only **1.3%** of possible mutations.
- **Two orthogonal positive-selection screens.**
  - **Activation** (growth-factor-independent proliferation, **MCF10A** cells under GF depletion): **474 activating** missense mutations = **5.6%** of 8,407 tested. Most in FGFR2 (58%), fewest in FGFR3 (5%). Binned by median enrichment: potentially activating (1.5–2.5×), weakly (>2.5–5×), activating (>5–10×), strongly (>10×). 8 mutations activate in all four FGFRs (e.g. I544V, N546S, N546K, V561L, K656Q/E/T, R675G in FGFR1 nomenclature).
  - **Resistance** (FGFRi-sensitive **NCI-H1581** lung cancer cells treated with 20 nM **pemigatinib** or 10 nM **futibatinib**): **738 resistance** mutations total — **635 pemigatinib-resistant (PemR)** and **407 futibatinib-resistant (FutR)**. Resistance was more evenly spread across the four FGFRs (FGFR4 had the most, 40%). For FGFR2: 32% dual-resistant, 58% pemigatinib-only, 10% futibatinib-only; FutR mutations cluster at Cys491 (futibatinib's covalent site), Phe492, Asp530.
- **301 druggable mutations.** Combining the two screens (activating AND not resistance-mediating) yields **301 druggable FGFR mutations** — i.e. activating variants still treatable by pemigatinib and/or futibatinib. Druggability is FGFR-specific: most FGFR1/FGFR2 activating mutations are treatable by one or both inhibitors, whereas most FGFR3/FGFR4 activating mutations mediate resistance to both.
- **Strong PS3/BS3 functional-evidence level.** Benchmarked against CKB/OncoKB labels, the screens gave an **odds-of-pathogenicity (OddsPath) of 45.4 / 52.0** for pathogenic and **0.010 / 0.015** for benign variants (CKB / OncoKB respectively) — meeting **strong** PS3 (pathogenic) and BS3 (benign) evidence under ACMG/AMP guidelines.
- **Clinically validated against acquired resistance.** From 27 patients (29 datapoints, 28 single-nucleotide mutations) at acquired resistance to FGFRis: **27/28 (96%)** mediated pemigatinib resistance and **22/28 (79%)** futibatinib resistance in the screens; only 1 (4%) did not. For the 14 "lead" resistance mutations, 13 (93%) showed resistance. For 19 cases of acquired resistance to pemigatinib+futibatinib, **all 19 (100%)** carried a screen-defined resistance mutation. Overall the functional data would have correctly indicated resistance in **28/29 (97%)** cases (the headline "97%"). The single miss had PIK3CA/TSC1 co-alterations (off-target PI3K-pathway resistance).
- **Mechanistic signal.** GoF mutations associate with **increased hydrophobicity** of the amino-acid change (LoF with decreased); the screen also recovered activating C-terminal **nonsense** mutations in FGFR2 and identified LoF mutations.
- **In silico predictors fail to stratify variant class.** REVEL, **EVE**, and **AlphaMissense** could not distinguish GoF from LoF: only weak positive correlation with enrichment for activating variants, and moderate/strong *negative* correlation for depleted ones (net negative overall, all FGFRs). COSMIC recurrence was only weakly predictive except for the rare highly recurrent (≥5) mutations. Exemplar discordant pairs (high-REVEL+COSMIC but low activation vs low-REVEL+absent-from-COSMIC but high activation) were individually confirmed — underscoring the need for experimental functional data.

## Methods

- **Saturation mutational scanning, pooled lentiviral format.** Library of 11,520 SNVs designed computationally, synthesized as pooled oligos, cloned into lentiviral expression plasmids; plasmid-pool NGS confirms per-mutation coverage. Each FGFR carries one distinct point mutation per construct after transduction.
- **Activation screen.** MCF10A (growth-factor-dependent) transduced, then selected under growth-factor depletion (no EGF/insulin, reduced horse serum) up to 3 weeks. Activating call = enrichment ≥1.5 in ≥3 of 4 biological replicates.
- **Resistance screen.** NCI-H1581 (FGFR1-amplified, FGFR2-dependent per DepMap) transduced, treated 8 days with pemigatinib (20 nM) or futibatinib (10 nM) — concentrations at/below clinically achievable serum levels — to positively select resistance. 3 replicates.
- **Readout & QC.** gDNA of selected cells → NGS enrichment; QC via replicate correlation, missense-vs-synonymous comparison, and concordance with CKB/OncoKB GoF/LoF/neutral/resistance labels. OddsPath computed per ACMG/AMP for PS3/BS3.
- **Orthogonal validation.** Individually cloned mutants in MCF10A and NIH-3T3 (viability, soft-agar colony formation, low-serum proliferation, FGFR/FRS2 phosphorylation by western); IC50 of 6 inhibitors for 7 FGFR2 mutants; structural mapping onto FGFR1; comparison to in silico scores (REVEL, EVE, AlphaMissense) and to COSMIC recurrence and clinical-trial resistance datasets.

## Relevance to the brain-organoid ASD review

- **Canonical variant-class stratification example.** This is the review's exemplar that a single saturation screen can resolve variants into distinct functional classes — **activating (GoF) vs loss-of-function vs resistance-conferring vs neutral** — rather than a single pathogenic/benign axis. That multi-class, mechanism-aware readout is the capability the review argues programmable brain organoids should bring to ASD variants (where GoF vs LoF distinctions carry different therapeutic implications).
- **Demonstrates strong PS3/BS3-grade functional evidence at scale.** Quantitative OddsPath (45–52 pathogenic; ~0.01 benign) shows a saturation functional assay reaching ACMG "strong" evidence, the bar the review wants organoid assays to clear; see [Brnich_2019](Brnich_2019_Recommendations_application_functional_evidence_PS3_BS3_criterion.md).
- **Independent confirmation that Stage-1 in silico tools cannot stand alone.** REVEL/EVE/AlphaMissense fail to separate GoF from LoF here — directly reinforcing, in a coding context, the same message Kircher makes for non-coding variants: computational prioritization ([Frazer_2021](Frazer_2021_Disease_variant_prediction_deep_generative_models_evolutionary.md), [Cheng_2023](Cheng_2023_Accurate_proteome_wide_missense_variant_effect_prediction.md)) must be paired with functional Stage-2 assays.
- **Note on disease domain.** This is an oncology (FGFR/precision-oncology) study, not autism genetics; its relevance to the ASD review is methodological (variant-class stratification, saturation-screen design, ACMG evidence calibration), not a direct ASD finding. FGFRs are flagged as central regulators of fetal development, but the paper does not address neurodevelopment.
- **Cross-links.** Saturation/DMS methodology peers: [Beltran_2025](Beltran_2025_Site_saturation_mutagenesis_500_human_protein_domains.md), [Findlay_2018](Findlay_2018_Accurate_classification_BRCA1_variants_saturation_genome_editing.md), [Sahu_2025](Sahu_2025_Saturation_genome_editing_based_clinical_classification_BRCA2.md), [Hemker_2025](Hemker_2025_Saturation_mapping_MUTYH_variant_effects_DNA_repair.md), [Herger_2025](Herger_2025_High_throughput_screening_human_genetic_variants_by.md). Regulatory-element counterpart: [Kircher_2019](Kircher_2019_Saturation_mutagenesis_twenty_disease_associated_regulatory_elements.md).

## Open questions / limitations

- **Cell-line / ectopic context.** Activation read in MCF10A and resistance in NCI-H1581; effects are measured by overexpression of mutant FGFR in selected lines, not in native tumor (or neural) context. Generalization across tumor types/contexts is assumed from cross-FGFR conservation, not exhaustively tested.
- **Kinase domain only.** Covers kinase-domain point mutations; extracellular-domain, fusion, amplification, and non-coding FGFR aberrations are out of scope, as are the four erdafitinib-relevant FGFR3 extracellular mutations.
- **Two inhibitors tested directly.** Resistance defined for pemigatinib and futibatinib; erdafitinib resistance was inferred from pemigatinib data (90%, 9/10 patients) rather than screened. IC50 panel extends to 6 inhibitors but only for 7 FGFR2 mutants.
- **Off-target resistance unmodeled.** The one clinical miss (PIK3CA/TSC1 co-alterations) shows resistance arising outside FGFR itself (PI3K/mTOR pathway) is not captured; direct causal link of PI3K-pathway mutations to resistance "remains to be proven in a clinical trial."
- **Threshold-dependent calls.** Activating/resistance categories depend on enrichment cutoffs (≥1.5-fold, replicate-count rules); near-threshold ("potentially activating/resistant") variants carry more uncertainty.
