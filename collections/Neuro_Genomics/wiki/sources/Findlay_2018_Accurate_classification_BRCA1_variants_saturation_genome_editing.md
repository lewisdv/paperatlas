---
title: "Accurate classification of BRCA1 variants with saturation genome editing."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41586-018-0461-z
pmid: 30209399
authors: Findlay GM et al.
journal: Nature (2018)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Findlay_2018_Accurate_classification_BRCA1_variants_saturation_genome_editing.pdf
pdf_status: downloaded
---

# Accurate classification of BRCA1 variants with saturation genome editing.

## Source

- Authors: Findlay GM, Daza RM, Martin B, Zhang MD, Leith AP, Gasperini M, Janizek JD, Huang X et al.
- Journal: Nature (2018)
- DOI: [10.1038/s41586-018-0461-z](https://doi.org/10.1038/s41586-018-0461-z)
- PMID: [30209399](https://pubmed.ncbi.nlm.nih.gov/30209399/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Variants of uncertain significance fundamentally limit the clinical utility of genetic information. The challenge they pose is epitomized by BRCA1, a tumour suppressor gene in which germline loss-of-function variants predispose women to breast and ovarian cancer. Although BRCA1 has been sequenced in millions of women, the risk associated with most newly observed variants cannot be definitively assigned. Here we use saturation genome editing to assay 96.5% of all possible single-nucleotide variants (SNVs) in 13 exons that encode functionally critical domains of BRCA1. Functional effects for nearly 4,000 SNVs are bimodally distributed and almost perfectly concordant with established assessments of pathogenicity. Over 400 non-functional missense SNVs are identified, as well as around 300 SNVs that disrupt expression. We predict that these results will be immediately useful for the clinical interpretation of BRCA1 variants, and that this approach can be extended to overcome the challenge of variants of uncertain significance in additional clinically actionable genes.

## Key findings

- **Scale of the assay.** Function scores obtained for **3,893 SNVs** = **96.5%** of all possible SNVs in (and immediately intronic to) **13 BRCA1 exons** encoding the RING (exons 2–5) and BRCT (exons 15–23) domains (transcript NM_007294.3). This is the "~4,000 variants" headline figure of the paper.
- **Bimodal score distribution.** Function scores split cleanly into two modes. All 138 nonsense SNVs scored below −1.25 (median −2.12); 98.7% of synonymous SNVs >3 bp from splice junctions scored above −1.25 (median 0.00). A two-component Gaussian mixture model classified SNVs as **functional (72.5%)**, **non-functional (21.1%)**, or **intermediate (6.4%)**.
- **Concordance with ClinVar (the accuracy claim).** Near-perfect agreement with expert clinical interpretations:
  - Of 169 ClinVar-"pathogenic" SNVs overlapping the assay, **162 scored non-functional**, 2 functional, 5 intermediate.
  - Of 22 ClinVar-"benign" SNVs, **20 scored functional**, 1 non-functional, 1 intermediate.
  - ROC over 375 one-star+ ClinVar SNVs: **sensitivity 96.7% at specificity 98.2%**, **AUC = 0.983** (treating likely-pathogenic/likely-benign as pathogenic/benign). High sensitivity/specificity held for the hardest classes (missense, splice-region).
  - 3 firmly discordant SNVs are argued to reflect *errors in the clinical databases*, not assay failure (Supplementary Note 1) — i.e. true accuracy may exceed the ClinVar-anchored estimate.
- **Resolving VUS (core clinical payoff).** Of variants that were *unclassifiable* by clinical data, SGE assigned a function to the large majority: **91.3% of the 378 VUS / conflicting-interpretation SNVs** were classified as functional or non-functional. Specifically **25.0% (64/256) of VUS** and **49.2% (60/122) of conflicting-interpretation SNVs** scored non-functional. Missense VUS were enriched for non-functional scores vs. missense SNVs absent from ClinVar (25.9% vs 17.2%, P = 0.002).
- **Variants never seen in a human.** Of **3,140 assayed SNVs absent from ClinVar**, 498 (15.9%) scored non-functional — pre-emptive functional evidence for variants not yet observed clinically.
- **Two functional layers captured at once.** Because the readout is at the endogenous locus, the assay integrates effects on protein activity *and* on RNA: **>400 non-functional missense SNVs** and **~300 SNVs disrupting expression** (depleted in mRNA relative to gDNA) were identified. SNVs at canonical splice sites were mostly non-functional (89.5%) or intermediate (5.5%).
- **Orthogonal validation.** Function scores tracked population allele frequency (rarer/singleton variants more often non-functional; gnomAD, Bravo, FLOSSIES) and out-performed computational predictors (CADD, phyloP, Align-GVGD) on the ClinVar pathogenic/benign missense set.

## Methods

- **Assay = saturation genome editing (SGE)** at the endogenous BRCA1 locus (method originally from Findlay et al. 2014, *Nature* 513:120). Each experiment targets a single exon; all possible SNVs across ~100 bp are introduced simultaneously by multiplex CRISPR-Cas9 + homology-directed repair (HDR) and concurrently assayed.
- **Cell line: HAP1** (near-haploid human CML-derived line; single-copy locus so one edited allele = one genotype). BRCA1 and other HDR-pathway genes (BRCA2, PALB2, BARD1, RAD51C) are **essential in HAP1**, so loss-of-function variants are depleted — this essentiality is what makes a survival readout possible.
- **Readout = cell survival (depletion/dropout).** Cells carrying function-compromising SNVs are selected against and lose genomic-DNA representation over time. Function is therefore a **binary-ish fitness/viability signal** read by deep sequencing, not a direct molecular phenotype.
- **Optimizations for signal.** A monoclonal **LIG4-knockout HAP1 line** (raises HDR rates ~3.6-fold by suppressing NHEJ) and **FACS sorting for 1n ploidy** before editing (HAP1 spontaneously diploidizes) improved reproducibility; final data came from 1n-sorted HAP1-LIG4KO cells.
- **Library design.** Array-synthesized oligo pools (Agilent), 3× region length + 1 wild-type template, cloned into plasmids with 600–1,000 bp homology arms. A fixed synonymous substitution at the Cas9 target site reduces re-cutting after successful HDR and acts as an "HDR marker" to distinguish true edits from sequencing error.
- **How function scores were derived.** 20M HAP1 cells co-transfected (day 0) with SNV library + Cas9/gRNA; puromycin selection; sampled **day 5 and day 11** for targeted gDNA sequencing; targeted RNA-seq on day 5 for expression scores. Pipeline: (1) log2 ratio of SNV frequency day 11 vs plasmid library; (2) subtract position-dependent editing bias (LOESS fit on day-5 frequencies); (3) normalize per-exon so median synonymous and median nonsense SNVs match global medians; (4) filter SNVs that couldn't be confidently scored. Class assignment via `normalmixEM` mixture model: non-functional distribution = nonsense SNVs, functional = synonymous SNVs away from splice sites; thresholds at posterior P(non-functional) of 0.01 / 0.99.
- Data/scores public at `https://sge.gs.washington.edu/BRCA1/`; pipeline at `github.com/shendurelab/saturationGenomeEditing_pipeline`.

## Relevance to the brain-organoid ASD review

- **The methodological template the review extends to 3D organoids.** Findlay 2018 is the canonical demonstration that SGE can functionally classify *every possible* SNV across a clinically actionable gene at its **endogenous locus** (not a cDNA transgene), capturing splicing/expression effects that overexpression assays miss. The review proposes porting this same "saturate every variant, read a phenotype, build a sequence-function map" logic into patient-relevant **brain organoids** for ASD genes.
- **The "~4,000 variants, >95% accuracy, binary survival assay" point — and why ASD is harder.** The power here comes from a **one-dimensional fitness readout** (survive or die) in a cell line where the target gene is *essential*. ~3,900 variants, ROC AUC 0.983, sensitivity 96.7%/specificity 98.2%. ASD risk genes generally are **not** essential-for-survival in a dish and their pathology is **not** captured by a binary survival signal — relevant phenotypes (neuronal differentiation, migration, synaptogenesis, network/electrophysiology, cell-type composition) are **multidimensional and developmental**. This is the central methodological gap the review must bridge: replacing a clean survival selection with rich, multi-modal organoid phenotyping (and the harder scoring/statistics that implies).
- **Why the cell line is "essential-gene" friendly.** HAP1 makes BRCA1 LoF lethal, giving the dropout signal. ASD genes would need an alternative SGE-compatible selection or phenotypic FACS/marker readout — exactly the kind of assay development the paper itself flags as a prerequisite for scaling SGE to other genes.
- **Link to PS3/BS3 clinical-evidence standards (the evidence-standards argument).** This dataset is a worked example of generating **functional evidence at clinical scale** for ACMG/AMP variant interpretation. Its near-perfect ClinVar concordance is the kind of assay validation that, per ClinGen SVI, can justify applying the strong functional codes **PS3 (abnormal function → pathogenic)** and **BS3 (normal function → benign)**. See [Brnich 2019 — PS3/BS3 framework](Brnich_2019_Recommendations_application_functional_evidence_PS3_BS3_criterion.md). The review's argument that organoid assays should aspire to PS3/BS3-grade evidence rests on precedents like this; the open challenge is whether a multidimensional organoid phenotype can be validated to the same statistical standard as a binary survival assay.
- **Sibling SGE / saturation-mapping precedents in this collection:** [Sahu 2025 — SGE of BRCA2](Sahu_2025_Saturation_genome_editing_based_clinical_classification_BRCA2.md) (same approach, humanized mouse ES cells, 6,551 SNVs, ACMG-integrated); [Hemker 2025 — SGE of MUTYH](Hemker_2025_Saturation_mapping_MUTYH_variant_effects_DNA_repair.md); [Kircher 2019 — saturation mutagenesis of regulatory elements](Kircher_2019_Saturation_mutagenesis_twenty_disease_associated_regulatory_elements.md); [Beltran 2025 — site-saturation mutagenesis of protein domains](Beltran_2025_Site_saturation_mutagenesis_500_human_protein_domains.md).

## Open questions / limitations

- **Cell-line survival ≠ physiological/3D context (the key caveat for the review).** The authors explicitly flag that a **HAP1 survival assay** is not a "more physiologically appropriate model"; validity rests on concordance with clinical data, not on biological fidelity. A dropout assay cannot capture tissue-specific, cell-type-specific, **developmental**, or **3D-architectural** phenotypes — precisely the dimensions that matter for neurodevelopmental/ASD genes and that brain organoids are meant to supply.
- **Requires an essential gene + a strong selection.** The method depends on BRCA1 (and HDR pathway) being essential in HAP1. Genes that aren't essential-for-viability — most ASD genes — need bespoke, validated alternative readouts (drug selection, FACS on phenotypic markers); the paper names this as an unsolved prerequisite for generalization.
- **Hypomorphs / intermediate alleles unresolved.** ~6% of SNVs (enriched for missense) had intermediate scores beyond definitive interpretation; these may be partial-function (hypomorphic) alleles whose risk the assay cannot quantify. ASD genes with dosage-sensitive, graded effects could produce many such ambiguous calls.
- **Scope limited to RING + BRCT domains.** Only 13 of BRCA1's exons were assayed; variants outside these critical domains, and most non-coding/regulatory variation, are not covered.
- **Single readout integrates but cannot dissect mechanism.** Survival folds splicing, translation, and protein activity into one score; targeted RNA-seq adds an expression axis, but the assay does not by itself separate *which* mechanism a given variant disrupts (follow-up mechanistic tests are needed, e.g. measuring mRNA in carriers for discordant SNVs).
- **Technical artifacts required curation.** Re-cutting biases near the CRISPR site, plasmid contamination (exon 22), and library bottlenecking (exon 18 RNA) forced filtering/exclusions — a reminder that scaling SGE to new loci/phenotypes carries non-trivial QC burden.
