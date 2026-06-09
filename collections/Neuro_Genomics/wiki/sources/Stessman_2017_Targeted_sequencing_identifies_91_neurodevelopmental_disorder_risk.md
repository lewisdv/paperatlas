---
title: "Targeted sequencing identifies 91 neurodevelopmental-disorder risk genes with autism and developmental-disability biases."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/ng.3792
pmid: 28191889
authors: Stessman HA et al.
journal: Nature genetics (2017)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Stessman_2017_Targeted_sequencing_identifies_91_neurodevelopmental_disorder_risk.pdf
pdf_status: downloaded
---

# Targeted sequencing identifies 91 neurodevelopmental-disorder risk genes with autism and developmental-disability biases.

## Source

- Authors: Stessman HA, Xiong B, Coe BP, Wang T, Hoekzema K, Fenckova M, Kvarnung M, Gerdts J et al. (senior author Eichler EE)
- Journal: Nature genetics (2017)
- DOI: [10.1038/ng.3792](https://doi.org/10.1038/ng.3792)
- PMID: [28191889](https://pubmed.ncbi.nlm.nih.gov/28191889/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Gene-disruptive mutations contribute to the biology of neurodevelopmental disorders (NDDs), but most of the related pathogenic genes are not known. We sequenced 208 candidate genes from >11,730 cases and >2,867 controls. We identified 91 genes, including 38 new NDD genes, with an excess of de novo mutations or private disruptive mutations in 5.7% of cases. Drosophila functional assays revealed a subset with increased involvement in NDDs. We identified 25 genes showing a bias for autism versus intellectual disability and highlighted a network associated with high-functioning autism (full-scale IQ >100). Clinical follow-up for NAA15, KMT5B, and ASH1L highlighted new syndromic and nonsyndromic forms of disease.

## Key findings

- **91 NDD risk genes, 38 new**, with an excess of de novo or private disruptive mutations accounting for **5.7% of cases**. (Header count = 91; see limitation note below on the two overlapping gene-set tallies the paper reports.)
- **Design:** single-molecule molecular inversion probes (smMIPs; 12,016 probes in 4 pools) targeting coding exons + 5 bp flanks of **208 candidate NDD genes**, screened across **>11,730 cases** (6,342 ASD + 7,065 ID/DD primary diagnoses; 13,407 probands total in the ASID network) and **>2,867 controls**, from 15 centers / 7 counters / 4 continents (Autism Spectrum/Intellectual Disability "ASID" network). Genes pre-selected via denovo-db by published de novo recurrences, CNV-morbidity-map overlap, pathway connectivity, and absence in 1,909 control sibling exomes.
- **Variant burden:** 61,315 QC-passing variants; 2,185 private + potentially deleterious (LGD or missense with CADD >30 = "MIS30"). Private high-impact events significantly exceeded unaffected siblings (FDR-corrected P = 1.44 × 10⁻⁹), driven by **LGD** events (P = 9.20 × 10⁻¹⁵), **not** MIS30 (P = 0.83). Sanger validation rate >97% (1,125 variants validated).
- **De novo signal:** of 286 private variants with inheritance assessed, 35% were sporadic → 91 private de novo mutations in cases (82 LGD + 9 MIS30) vs 9 in siblings (3 LGD + 6 MIS30). Allowing allele count ≤3 → 138 de novo proband events (114 LGD + 24 MIS30); probability of ≥114 LGD + ≥24 MIS30 across 208 genes = **P = 1.6 × 10⁻²² (OR 2.62, 95% CI 2.2–3.09)**.
- **Combined with published exomes:** 68 genes reached de novo significance for LGD and 23 for MIS30 (q <0.1, >1 event); 13 significant for both → **78 unique de novo-significant genes**. Of these 78, **32 were not previously associated with NDD** (most significant new ones: TRIP12, KMT5B, ASH1L, NAA15, DSCAM, all corrected P < 1 × 10⁻⁶). Most frequently de novo-mutated: SCN2A, ADNP, CHD8, DYRK1A, POGZ (NAA15 as frequent as DYRK1A/POGZ). No gene reached de novo LGD significance in controls (one MIS30 gene, TRRAP, likely a false positive).
- **Inheritance:** 65% of validated private LGD/MIS30 variants were inherited (33.2% maternal, 31.8% paternal); nominal maternal-transmission bias for LGD (not MIS30).
- **ASD-vs-ID/DD bias:** 25 genes biased by primary diagnosis (two one-tailed binomial tests, P <0.025). **8 ASD-biased** (CHD2, CTTNBP2, CHD8, LAMC3, DIP2A, RELN, UNC80, IQGAP3; only CHD8/CHD2/DIP2A previously known ASD loci); **17 ID/DD-biased** (incl. newly linked NAA15, ZMYM2, PHIP, STAG1). Most genes mutated in both → substantial genetic overlap between comorbid conditions.
- **High-functioning ASD network:** MAGI network-building on SSC probands with full-scale IQ >100 (n = 668; ~9:1 male bias) highlighted a gene-interaction network associated with high-functioning autism.
- **Drosophila functional validation:** pilot of 21 genes via UAS-Gal4 neuron-specific RNAi knockdown, assayed with the light-off jump habituation paradigm (an ASD/ID-relevant learning readout); used to nominate a subset (incl. NAA15, KMT5B, ASH1L, TCF4) with increased NDD involvement.
- **Clinical follow-up of 3 new genes:**
  - **NAA15** (N-terminal acetyltransferase complex component): 12 LGD + 1 MIS30 private variants; estimated LGD penetrance **35.3% (95% CI 15.7–63.6%)**; ID/DD-biased.
  - **KMT5B** and **ASH1L** (histone lysine N-methyltransferases): significant for both de novo LGD and MIS30; shared ID/DD + dysmorphism / macrocephaly-type features; define new syndromic and nonsyndromic NDD presentations.

## Methods

- smMIP-based targeted resequencing (highly sensitive/specific, low-cost) of 208 candidate genes across the ASID consortium; QC excluded common dbSNP variants; private = seen in only one family.
- Inheritance assigned by genotyping parental DNA where available; "de novo" vs inherited determined for 286 private variants.
- Per-gene burden tested with a one-tailed binomial model using a human–chimp-divergence mutation rate (~1.5 DNM/exome expected), FDR-corrected; private-variant burden vs ExAC and vs in-study siblings by Fisher's exact test with FDR.
- Phenotype-bias analysis using primary ascertainment diagnosis (ASD vs ID/DD per DSM-5) combined with prior NDD datasets; two one-tailed binomial tests per gene.
- Functional follow-up: Drosophila neuronal RNAi knockdown + light-off jump habituation behavioral assay (21 genes); clinical recontact and deep phenotyping for NAA15, KMT5B, ASH1L.

## Relevance to the brain-organoid ASD review

- Provides the **targeted NDD gene panel / candidate-gene catalog** the review can use to prioritize organoid perturbation targets: 91 risk genes (38 new), with explicit per-gene de novo counts and significance (Table 1) and ASD-vs-ID bias labels.
- The **ASD-biased genes** (esp. CHD8, CHD2, DIP2A and the high-functioning-ASD network) are the highest-value candidates for an ASD-focused organoid platform; the ID/DD-biased set helps distinguish ASD-without-ID biology from broader NDD — directly addressing the field's criticism that gene discovery conflates the two.
- Shares **SCN2A** (and the broader chromatin-/transcription-regulator theme: CHD8, ADNP, ARID1B, SMARCA4-family) with the mosaicism findings in [Lim 2017](Lim_2017_Rates_distribution_implications_postzygotic_mosaic_mutations_autism.md), reinforcing convergent target genes.
- The **Drosophila habituation assay** is a precedent for the kind of model-system functional validation an organoid review must contextualize — and exactly the class of evidence that must be calibrated against the [Brnich 2019 PS3/BS3 framework](Brnich_2019_Recommendations_application_functional_evidence_PS3_BS3_criterion.md) before it counts clinically (model-organism data warrant a nuanced strength adjustment per that guideline).
- Demonstrates the **genotype-first → phenotype follow-up** workflow (NAA15/KMT5B/ASH1L recontact, penetrance estimation) that organoid functional data could augment.

## Open questions / limitations

- **Two gene tallies coexist:** the title/abstract report **91 genes** (excess of de novo *or* private disruptive mutations, incl. burden hits) while the de novo-significance analysis yields **78 unique de novo-significant genes** (of which 32 novel). The "38 new" headline and the "32 not previously described" de-novo subset are computed over different gene sets — cite the specific set when quoting counts.
- Panel is **restricted to 208 pre-selected candidates**; novel genes outside the panel cannot be discovered, and selection was biased toward genes with prior de novo recurrences.
- MIS30 (missense, CADD >30) burden was **not** significant over siblings overall (P = 0.83); missense-level inferences are weaker than LGD.
- Penetrance estimates are wide (NAA15 LGD 35.3%, 95% CI 15.7–63.6%); small per-gene phenotype samples limit syndrome delineation.
- Drosophila knockdown is a **loss-of-function, invertebrate** proxy with limited behavioral readout — not a substitute for human neural-context functional evidence, and one MIS30 control gene (TRRAP) flagged as a likely statistical false positive shows the model's noise floor.
- ASD-vs-ID bias rests on **primary ascertainment diagnosis**, which is imperfect given frequent NDD co-occurrence; most genes were mutated in both phenotypes.
