---
title: "Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the ACMG and AMP"
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/gim.2015.30
pmid: 25741868
authors: Richards S et al.
journal: Genetics in medicine : official journal of the American College of Medical Genetics (2015)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Richards_2015_Standards_guidelines_interpretation_sequence_variants_joint_consensus.pdf
pdf_status: downloaded
---

# Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the ACMG and AMP

## Source

- Authors: Richards S, Aziz N, Bale S, Bick D, Das S, Gastier-Foster J, Grody WW, Hegde M, Lyon E, Spector E, Voelkerding K, Rehm HL (on behalf of the ACMG Laboratory Quality Assurance Committee)
- Journal: Genetics in Medicine (2015), vol. 17, no. 5, 405–424
- DOI: [10.1038/gim.2015.30](https://doi.org/10.1038/gim.2015.30)
- PMID: [25741868](https://pubmed.ncbi.nlm.nih.gov/25741868/)
- Added via: manuscript_brain_organoid_v6 reference ingest (foundational gap-fill)

## Abstract

The American College of Medical Genetics and Genomics (ACMG) previously developed guidance for the interpretation of sequence variants. In the past decade, sequencing technology has evolved rapidly with the advent of high-throughput next-generation sequencing. By adopting and leveraging next-generation sequencing, clinical laboratories are now performing an ever-increasing catalogue of genetic testing spanning genotyping, single genes, gene panels, exomes, genomes, transcriptomes, and epigenetic assays for genetic disorders. By virtue of increased complexity, this shift in genetic testing has been accompanied by new challenges in sequence interpretation. In this context the ACMG convened a workgroup in 2013 comprising representatives from the ACMG, the Association for Molecular Pathology (AMP), and the College of American Pathologists to revisit and revise the standards and guidelines for the interpretation of sequence variants. This report recommends the use of specific standard terminology—"pathogenic," "likely pathogenic," "uncertain significance," "likely benign," and "benign"—to describe variants identified in genes that cause Mendelian disorders, and describes a process for classifying variants into these five categories based on criteria using typical types of variant evidence (population, computational, functional, and segregation data).

## Key findings

This is the **ACMG/AMP variant-interpretation standard** — the reference framework that defines what counts as evidence for or against a variant being disease-causing, and the **standard that functional assays (including organoid-based assays) must meet to qualify as PS3/BS3 functional evidence**.

- **Five-tier classification for Mendelian variants:** **Pathogenic**, **Likely pathogenic**, **Uncertain significance (VUS)**, **Likely benign**, **Benign**. "Likely" is defined as **>90% certainty** of being disease-causing (or benign).
- **Two evidence menus**, each criterion weighted by strength:
  - **Pathogenic evidence:** Very Strong **PVS1**; Strong **PS1–PS4**; Moderate **PM1–PM6**; Supporting **PP1–PP5**.
  - **Benign evidence:** Stand-alone **BA1**; Strong **BS1–BS4**; Supporting **BP1–BP7**.
- **Functional-evidence codes (load-bearing for organoid assays):**
  - **PS3 — "Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product."** Note: functional studies that are validated, reproducible, and robust in a clinical diagnostic setting are the most well-established; absent such validation the evidence may be downgraded (e.g., to moderate).
  - **BS3 — "Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing."** (The benign mirror of PS3.)
  - The guideline stresses that **not all functional assays are valid predictors** of effect on protein/gene function — the assay must be shown to interrogate the relevant biological mechanism and be reproducible.
- **Other key codes referenced by the review's themes:**
  - **PVS1** — null variant (nonsense, frameshift, canonical ±1/2 splice site, initiation codon, single/multi-exon deletion) in a gene where loss-of-function is a known disease mechanism. (Directly relevant to the de novo LoF variants central to ASD genetics.)
  - **PS2 / PM6** — de novo variant (PS2 = both maternity and paternity confirmed, no family history; PM6 = assumed de novo without confirmation). The de novo evidence codes that formalize the Sanders/Iossifov-style de novo signal at the single-variant clinical level.
  - **PS4** — variant significantly enriched in affected vs controls (relative risk/OR > 5.0, CI excluding 1.0).
  - **PM2** — absent/extremely rare in population databases (ESP, 1000 Genomes, ExAC); **BA1** — allele frequency > 5% (stand-alone benign); **BS1** — frequency greater than expected for the disorder.
  - **PP3 / BP4** — computational/in-silico predictions (deleterious / benign); each may be used only once and correlated predictors do not count independently.
- **Rules for combining criteria (Table 5) → classification:**
  - **Pathogenic** if e.g. (i) **1 PVS1 + ≥1 PS** (or +2 PM, or +1 PM & 1 PP, or +≥2 PP); OR (ii) **≥2 Strong (PS)**; OR (iii) **1 Strong + 3 Moderate**, etc.
  - **Likely pathogenic** if e.g. **1 Strong + 1–2 Moderate**, or **3 Moderate**, or **2 Moderate + 2 Supporting**, etc.
  - **Benign** if **1 Stand-alone (BA1)** OR **≥2 Strong (BS)**.
  - **Likely benign** if **1 Strong + 1 Supporting**, or **≥2 Supporting**.
  - **Uncertain significance** if criteria are unmet OR pathogenic and benign evidence conflict.
- **Flexibility:** criterion weights can be shifted up or down with documented justification (e.g., PM3 upgraded to strong with strong trans data; PS-level downgraded when data are weaker).

## Methods

- **Process:** ACMG/AMP/CAP workgroup convened 2013 (clinical lab directors + clinicians); built on the earlier ACMG 2008 guidance. Criteria and combining rules were refined through analysis of submitted lab protocols and community survey/feedback (including a two-system scoring exercise and a strength-weighting survey).
- **Scope:** Mendelian (and mitochondrial) germline sequence variants in clinical testing — genotyping, single genes, panels, exomes, genomes. Explicitly *not* a CNV/somatic/pharmacogenomic guideline (separate CNV guidance noted).
- **Output artifacts:** standardized five-tier terminology; pathogenic criteria table (PVS1, PS1–4, PM1–6, PP1–5); benign criteria table (BA1, BS1–4, BP1–7); rules table for combining criteria; recommendation that interpretation occur in a CLIA-approved lab by a board-certified clinical molecular geneticist/pathologist; HGVS nomenclature required.
- Supplemented by detailed per-criterion guidance and worked examples (e.g., BRCA, CFTR variants) and a single evidence-framework figure organizing all codes by type and strength.

## Relevance to the brain-organoid ASD review

- **Defines the regulatory/clinical bar the review invokes for functional assays:** for an organoid-based functional readout to count as clinical evidence of pathogenicity it must satisfy **PS3** ("well-established in vitro or in vivo functional studies supportive of a damaging effect") — and to support a benign call, **BS3**. This is the standard a "programmable brain organoid" functional platform must meet to feed variant interpretation, including the requirement that the assay be validated, reproducible, and mechanism-relevant.
- **Frames the proactive-genetics value proposition:** much of ASD rare-variant burden manifests clinically as **VUS** (uncertain significance) because functional and segregation evidence is lacking; scalable organoid functional assays are precisely the kind of PS3/BS3 evidence that can reclassify VUS → likely pathogenic / likely benign.
- **Connects to the de novo / LoF genetics** of the companion papers: **PVS1** (LoF mechanism) and **PS2/PM6** (de novo) are the clinical codes that operationalize the Sanders 2012 / Fu 2022 findings at the level of an individual patient's variant.
- Provides the **shared vocabulary** (pathogenic/likely pathogenic/VUS/likely benign/benign) the review uses when discussing how organoid evidence changes a variant's clinical classification.

## Open questions / limitations

- **Scope limited to Mendelian germline single-nucleotide/indel variants** — does not natively cover CNVs, somatic/mosaic variants, polygenic risk, or non-Mendelian/complex inheritance, which is precisely the architecture (moderate-penetrance, polygenic, CNV-heavy) that dominates ASD (see Fu 2022). Applying ACMG/AMP to ASD risk genes is therefore partial.
- The criteria are **qualitative and combinatorial**, not quantitative/probabilistic; inter-laboratory concordance was a known concern (later addressed by ClinGen specifications and Bayesian point systems, and by the **Brnich 2019** PS3/BS3 functional-evidence calibration framework already in this collection).
- **"Well-established" functional assay is not precisely defined** in the 2015 text — leaving the threshold an organoid assay must meet underspecified (the gap Brnich 2019 fills with OddsPath-based strength calibration).
- Designed for **highly penetrant, single-gene disorders**; weak for variants of intermediate effect (the bulk of ASD risk), where PS4-style case-control enrichment thresholds (OR > 5) rarely apply.
