---
title: "Saturation mutagenesis of twenty disease-associated regulatory elements at single base-pair resolution."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41467-019-11526-w
pmid: 31395865
authors: Kircher M et al.
journal: Nature communications (2019)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Kircher_2019_Saturation_mutagenesis_twenty_disease_associated_regulatory_elements.pdf
pdf_status: downloaded
---

# Saturation mutagenesis of twenty disease-associated regulatory elements at single base-pair resolution.

## Source

- Authors: Kircher M, Xiong C, Martin B, Schubach M, Inoue F, Bell RJA, Costello JF, Shendure J et al. (Ahituv N co-corresponding)
- Journal: Nature communications (2019) 10:3583
- DOI: [10.1038/s41467-019-11526-w](https://doi.org/10.1038/s41467-019-11526-w)
- PMID: [31395865](https://pubmed.ncbi.nlm.nih.gov/31395865/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

The majority of common variants associated with common diseases, as well as an unknown proportion of causal mutations for rare diseases, fall in noncoding regions of the genome. Although catalogs of noncoding regulatory elements are steadily improving, we have a limited understanding of the functional effects of mutations within them. Here, we perform saturation mutagenesis in conjunction with massively parallel reporter assays on 20 disease-associated gene promoters and enhancers, generating functional measurements for over 30,000 single nucleotide substitutions and deletions. We find that the density of putative transcription factor binding sites varies widely between regulatory elements, as does the extent to which evolutionary conservation or integrative scores predict functional effects. These data provide a powerful resource for interpreting the pathogenicity of clinically observed mutations in these disease-associated regulatory elements, and comprise a rich dataset for the further development of algorithms that aim to predict the regulatory effects of noncoding mutations.

## Key findings

- **Saturation MPRA of 21 elements (20 disease-associated + 1 ultraconserved).** 10 promoters: **TERT, LDLR, HBB, HBG, HNF4A, MSMB, PKLR, F9, FOXE1, GP1BB**; 10 enhancers: **SORT1, ZRS, BCL11A, IRF4, IRF6, MYC (×2), RET, TCF7L2, ZFAND3**; plus ultraconserved enhancer **UC88**. Elements span **187–601 bp** and **28–73% GC**. Wild-type luciferase activity ranged 2–200-fold over empty vector.
- **Scale of measurements.** **31,243** assayed mutations passing QC (min. 10 tags) at **9,834** unique positions — comprising ~28,937 SNVs and **2,306** single-bp deletions. (Abstract rounds to "over 30,000.") On average **99.9%** of all possible SNVs in each target were tag-associated; ~55% of possible 1-bp deletions.
- **Most regulatory variants are inert; effects skew repressive.** **4,830 (15%)** of unique mutations caused significant expression change (fit p < 1e-5). Of those, **37% (1,789) increased** expression (median +20%) and **63% (3,041) decreased** it (median −24%). Requiring ≥2-fold change: only **83 activating vs 559 repressing**. The repressive skew is highly significant (binomial p < 1e-42), consistent with most TFs being activators (binding more easily lost than gained by single substitutions). Per-element fraction of significant variants ranged **3–52%** (mean ~22%).
- **1-bp deletions and transversions hit harder.** 1-bp deletions had larger absolute effects than SNVs; transversions had larger effects than transitions (Wilcoxon p < 1e-16) — though the assay had more power for transitions (error-prone PCR bias), creating an artifactual enrichment that the authors correct for.
- **Significant positions cluster** (non-random for all but F9 and FOXE1), consistent with discrete TFBS. Worked examples:
  - **LDLR promoter** (familial hypercholesterolemia; HepG2): MPRA reproduces published luciferase effects, e.g. c.-152C>T → 32–39% residual activity; c.-217C>T → ~263–273% activation; c.-142C>T → 11–20% residual. Two full replicates correlate r=0.97.
  - **TERT promoter** (cancer; HEK293T + glioblastoma SF7996): canonical c.-124C>T and c.-146C>T are **activating**, creating de-novo ETS/GABP binding sites. siRNA knockdown of **GABPA** (−68% GABPA, −58% TERT activity) reduced activity of these variants; significant variants were 2.8-fold enriched for ETS-family motifs. Cell-type-specific effects seen at an E2F repressor site (c.-62 to c.-70) active in GBM but not HEK293T.
  - **SORT1 enhancer** (myocardial infarction; HepG2): GWAS SNP rs12740374 minor allele creates a C/EBP site → ~2.7–2.9 log2-fold expression increase; effects are orientation-independent (flip-library r≈0.96–0.97), confirming enhancer behavior.
- **Existing computational/conservation scores predict regulatory effects poorly** (the paper's headline cautionary result). Across 21 elements, mean Spearman of best methods: **DeepSEA 0.22**, then FunSeq2 / Eigen / top-decile JASPAR / FATHMM-MKL all ~0.14. Per-element values range widely (0.3–0.6 for some, ~0 or negative for others). Mean variance explained (Pearson R²) across elements was just **0.03** (max 0.41, mammalian PhastCons on LDLR). Conservation drives most integrative scores but is informative only for some elements. Crucially, **gain-of-binding (activating) variants are missed** by reference-genome scans; sequence-based models (deltaSVM) partly recover directionality.

## Methods

- **Saturation-mutagenesis MPRA.** Error-prone PCR (Mutazyme II) introduces <1 change/100 bp into each cloned element; high-complexity libraries (50k–2M constructs/target) capture nearly all SNVs plus many 1-bp deletions. Each construct carries a 15/20-bp random barcode in the reporter 3′ UTR. Variant→tag associations learned by deep sequencing (subassembly for long elements); luciferase reporter then inserted between element and tag.
- **Readout.** Libraries transfected into disease-relevant cell lines (≈5M cells, 3 replicates each; HepG2, HEK293T, glioblastoma SF7996, K562, etc.; mouse lines incl. Neuro-2a and NIH/3T3 also used for luciferase validation). RNA/DNA tag counts (UMI-based) → multiple linear regression for per-variant effect. QC threshold = min. 10 tags/variant (replicate r up to 0.97–0.98; coverage ~98% SNVs).
- **Comparators evaluated.** Conservation: PhyloP, PhastCons, GERP++. Integrative scores: CADD, DeepSEA, Eigen, FATHMM-MKL, FunSeq2, GWAVA, LINSIGHT, ReMM. Motif/TFBS: JASPAR 2018, ENCODE, Ensembl Regulatory Build. Sequence-based: deltaSVM (10/21 elements with cell-type model).
- **Resource.** Interactive browser: https://mpra.gs.washington.edu/satMutMPRA/

## Relevance to the brain-organoid ASD review

- **This is the non-coding / MPRA variant-prioritization study the review cites.** Where EVE ([Frazer_2021](Frazer_2021_Disease_variant_prediction_deep_generative_models_evolutionary.md)) handles coding/missense, Kircher supplies the regulatory-element counterpart: empirical, single-base-resolution functional maps of disease-associated promoters and enhancers — the most ASD-relevant variant class given that most common-disease GWAS signal is non-coding.
- **Motivates experimental Stage-2 over in silico Stage-1 for regulatory variants.** Its central negative result — that no current computational/conservation score reliably predicts regulatory effect (mean R²≈0.03; activating gain-of-motif variants systematically missed) — is the argument for direct functional assays of non-coding variants, which the review extends into a programmable brain-organoid setting.
- **Saturation-MPRA template for ASD enhancers.** The error-prone-PCR + barcoded-MPRA design, and the siGABPA knockdown demonstrating cis-element × trans-factor coupling, prototype how regulatory variants near ASD genes could be saturated and mapped.
- **Cross-links.** Non-coding/MPRA peers in this collection: [DeGroat_2026](DeGroat_2026_MPRA_enhancer_gene_modeling_NDD_regulatory.md) (MPRA-informed enhancer–gene modeling for NDD/ASD), [Boix_2020](Boix_2020_EpiMap_regulatory_circuitry_noncoding_disease.md) (EpiMap regulatory circuitry). Splicing analogue: [Jaganathan_2019](Jaganathan_2019_Predicting_Splicing_Primary_Sequence_Deep_Learning.md) (SpliceAI). ACMG functional-evidence framing: [Brnich_2019](Brnich_2019_Recommendations_application_functional_evidence_PS3_BS3_criterion.md). Note: Martin Kircher (lead author, also CADD co-author) was a peer reviewer of the Frazer/EVE paper.

## Open questions / limitations

- **Episomal, not native context.** Elements are tested on plasmids (up to 600 bp), outside native chromatin/locus context; some regulatory polymorphisms do not reflect in-vivo effects in culture, especially for developmental genes with temporal/tissue-specific expression (the authors flag IRF6 and ZRS).
- **Trans context limited to chosen cell lines.** Effects can be cell-type-specific (demonstrated for TERT between HEK293T and GBM); a variant's effect depends on the available trans-acting factors.
- **Reproducibility scales with basal activity.** Low-basal-activity elements (BCL11A, FOXE1, one MYC element) gave the noisiest data; suggested fixes include stronger minimal promoters or more complex libraries.
- **Element count too small for promoter-vs-enhancer generalizations.** Classification results are dominated by a few elements (promoters: LDLR, PKLR, TERT; enhancers: SORT1, IRF4, IRF6); the authors caution against over-interpreting promoter/enhancer differences.
- **Assay bias.** Error-prone PCR favors transitions and A/T transversions, requiring statistical correction; 1-bp deletion coverage is incomplete (~25–55%).
