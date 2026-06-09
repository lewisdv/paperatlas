---
title: "Decomposition of phenotypic heterogeneity in autism reveals underlying genetic programs."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41588-025-02224-z
pmid: 40634707
authors: Litman A et al.
journal: Nature genetics (2025)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Litman_2025_Decomposition_phenotypic_heterogeneity_autism_reveals_underlying_genetic.pdf
pdf_status: downloaded
---

# Decomposition of phenotypic heterogeneity in autism reveals underlying genetic programs.

## Source

- Authors: Litman A, Sauerwald N, Green Snyder L, Foss-Feig J, Park CY, Hao Y, Dinstein I, Theesfeld CL et al.
- Journal: Nature genetics (2025)
- DOI: [10.1038/s41588-025-02224-z](https://doi.org/10.1038/s41588-025-02224-z)
- PMID: [40634707](https://pubmed.ncbi.nlm.nih.gov/40634707/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Unraveling the phenotypic and genetic complexity of autism is extremely challenging yet critical for understanding the biology, inheritance, trajectory and clinical manifestations of the many forms of the condition. Using a generative mixture modeling approach, we leverage broad phenotypic data from a large cohort with matched genetics to identify robust, clinically relevant classes of autism and their patterns of core, associated and co-occurring traits, which we further validate and replicate in an independent cohort. We demonstrate that phenotypic and clinical outcomes correspond to genetic and molecular programs of common, de novo and inherited variation and further characterize distinct pathways disrupted by the sets of mutations in each class. Remarkably, we discover that class-specific differences in the developmental timing of affected genes align with clinical outcome differences. These analyses demonstrate the phenotypic complexity of children with autism, identify genetic programs underlying their heterogeneity, and suggest specific biological dysregulation patterns and mechanistic hypotheses.

## Key findings

- **Four data-driven autism classes** from a generative finite mixture model (GFMM) over **239 item-level/composite phenotype features in 5,392 SPARK probands** (SCQ, RBS-R, CBCL, developmental-milestone history). Four classes chosen by BIC + validation log-likelihood + clinical interpretability; robust to perturbation. Classes: **Social/behavioral (n = 1,976)**, **Mixed ASD with DD (n = 1,002)**, **Moderate challenges (n = 1,860)**, **Broadly affected (n = 554)**.
- **Person-centered, not a severity spectrum:** classes differ in *patterns* of co-occurring traits, not just severity. Broadly affected = high across nearly all domains; Social/behavioral = high disruptive/attention/anxiety but **no developmental delay**; Mixed ASD with DD = strong developmental-delay + restricted/repetitive enrichment; Moderate challenges = consistently lower difficulty.
- **External clinical validation** (medical-history diagnoses not used in the model): Mixed ASD with DD enriched for language delay, intellectual disability, motor disorders (vs siblings FDR < 0.01, 8.8 < FE < 20.0); Social/behavioral and Broadly affected enriched for ADHD/anxiety/major depression (1.65 < FE < 2.36). DD-heavy classes had much earlier age at diagnosis.
- **Replication in independent SSC cohort (n = 861)** using 108 shared features; strong correlation of class feature-enrichment profiles between SPARK and SSC (clinician-reported).
- **Common-variant (polygenic score) signals track phenotype:** Social/behavioral and Broadly affected had highest ADHD PGS; Social/behavioral had highest major-depression PGS (FDR = 0.00327). Broadly affected (most ID/cognitive impairment) had significantly **lower educational-attainment and IQ PGS** (Cohen's d > 0.17).
- **De novo vs inherited burden differs by class:** Broadly affected had greatest de novo LoF + de novo missense burden (vs siblings FDR = 0.01, FE = 1.66); Social/behavioral lowest (FE = 1.17). Rare **inherited** LoF/missense significant **only in Mixed ASD with DD** (FDR = 0.016, FE = 2.55) — i.e., a stronger inherited component. By constraint: in high-constraint genes (pLI ≥ 0.995) ORs were 3.69/6.31/2.87/3.25 across classes; intermediate-constraint (0.5 ≤ pLI < 0.995) dnLoF enrichment appeared specifically in **Moderate challenges** (OR 2.54) — a signal masked when classes are pooled.
- **Class-specific pathways (little/no overlap):** Social/behavioral → chromatin organization (FE 3.5), DNA-repair regulation (FE 5.3), microtubule activity (FE 34.2); Moderate challenges → histone modification (FE 3.56), chromatin organization (FE 3.5); Mixed ASD with DD → neuronal action potential (FE 19.0), membrane depolarization (FE 25.0), **voltage-gated sodium channel activity (FE 28.8)**.
- **FMRP-target de novo variants** strongly enriched in Broadly affected (vs other classes FDR = 0.04, FE = 2.2, OR = 12.8).
- **HEADLINE — developmental-timing alignment with clinical outcome:** using cell-type-specific human prefrontal-cortex developmental trajectories (Herring et al.), **Mixed ASD with DD** was enriched for dnLoF variants in genes expressed **prenatally (fetal/neonatal, "down"/"trans down" trajectories)** across all major PFC cell types — and this class had the **latest milestone attainment** (FDR < 1.9 × 10⁻¹⁹) and **earliest age at diagnosis** (FDR = 6.97 × 10⁻¹⁵⁰, Cohen's d = 0.99 vs Social/behavioral). Conversely, **Social/behavioral** was enriched for LoF in **postnatally** expressed genes ("up"/"trans up") in MGE inhibitory interneurons, with milestones and diagnosis ages near non-autistic siblings (Cohen's d < 0.07). Moderate challenges = mostly prenatal but lower-constraint genes (median pLI 0.75 vs 0.95 in Mixed ASD with DD, P = 0.026). Broadly affected = broad dysregulation across all stages/cell types.

## Methods

- **Cohort/phenotypes:** SPARK (n = 5,392 probands + 1,972 non-autistic siblings); 239 features from SCQ-Lifetime, RBS-R, CBCL 6–18, and developmental-milestone background form. Features manually mapped to 7 literature-defined categories (limited social communication, restricted/repetitive behavior, attention deficit, disruptive behavior, anxiety/mood, developmental delay, self-injury).
- **Modeling:** general finite mixture model (handles continuous/binary/categorical data, minimal assumptions); 2–10 classes trained; 4-class solution selected on 6 fit statistics + clinical interpretability + stability. Class differences tested by one-sided t-tests with Benjamini–Hochberg correction.
- **Replication:** GFMM trained on SPARK applied to SSC test set (n = 861) and independently retrained on SSC; feature enrichment/depletion profiles correlated (Pearson) across cohorts; label permutation as null.
- **Genetics:** polygenic scores (European-ancestry children) for ASD + 5 related GWAS traits; whole-exome de novo + rare-inherited variant calling via HAT, classified LoF/missense/synonymous; count-burden enrichment per class vs siblings; constraint stratification by pLI; ORs for ASD-risk gene sets and FMRP targets; GO biological-process/molecular-function enrichment of dnLoF/damaging-missense-hit genes.
- **Developmental transcriptomics:** cell-type-specific PFC gene-expression trajectories (Herring et al.) classified into up / trans-up / trans-down / down trends across 6 stages (fetal, neonatal, infancy, childhood, adolescence, adult); dnLoF burden enrichment computed per class × cell type × trend (genetics subset: n = 2,013 probands, 1,013 siblings).

## Relevance to the brain-organoid ASD review

- **Theme 7 (ASD subtypes / phenotypic heterogeneity):** This is the collection's primary **data-driven subtype** reference. Replaces DSM/ICD label-based subtyping (cf. Grove's registry subtypes) with replicated, person-centered latent classes, and crucially **maps each class to a distinct genetic program** (common vs de novo vs inherited; constraint tier; pathway). Defines the stratification an organoid platform could model class-by-class.
- **Theme 2 (convergence on developmental vulnerability stages) — strongest tie:** The headline result operationalizes "developmental timing" as a *discriminating* axis: prenatally-expressed-gene disruption (Mixed ASD with DD) → severe early-onset outcomes; postnatally-expressed-gene disruption (Social/behavioral) → near-typical milestones. This converts Grove's corticogenesis and De Rubeis's mid-fetal convergence into outcome-linked, class-specific windows — a direct rationale for *temporally programmable* organoids that model prenatal vs postnatal vulnerability and for choosing which developmental stage to perturb per subtype.
- **Theme 1 (ASD genetic architecture):** Demonstrates that common, de novo, and inherited variation contribute **unequally across phenotypic classes** — refining the whole-cohort architecture of Grove (common) and De Rubeis/Satterstrom/Zhou (rare) into class-resolved contributions (e.g., inherited burden concentrated in Mixed ASD with DD; high-constraint de novo in Broadly affected).
- **Theme 3 (computational variant prioritization):** Generative mixture modeling + per-class burden/pathway analysis is itself a computational stratification method; the cell-type × developmental-trend enrichment is a template for context-resolved variant prioritization that organoid functional readouts could validate.
- **Theme 5 (sex differences):** Class sex/age distributions reported (Extended Data); FMRP-target and high-constraint de novo enrichment in the severe classes intersects the female-protective-effect literature (De Rubeis, Satterstrom 2026), though sex is not the paper's primary axis.
- **Cross-links:** SCN-channel / membrane-depolarization pathway enrichment in Mixed ASD with DD echoes De Rubeis's *SCN2A/CACNA1D* ion-channel class; chromatin-organization/histone-modification enrichment in Social/behavioral + Moderate challenges echoes De Rubeis's chromatin gene class — the same gene classes partition across subtypes.

## Open questions / limitations

- **Self-reported SPARK phenotypes** (parent questionnaires) risk rater effects; intellectual disability is a known confounder of social-behavior assessment (authors note, but argue internal consistency + SSC clinician-reported replication mitigate).
- Genetic analyses run on a **subset** (PGS European-ancestry only; exome burden n ≈ 2,013 probands / 1,013 siblings) — smaller than the 5,392 phenotyped, limiting power for class-specific associations; many effects are single-cohort and need larger replication.
- Class boundaries are **probabilistic** (mixture-model assignments), and the 4-class solution is one defensible choice among 2–10; classes are statistical constructs, not discrete biological entities.
- Developmental-timing inference is **correlative**, built on an external bulk/cell-type PFC trajectory atlas (Herring et al.) intersected with variant-hit gene lists — not direct functional or organoid evidence of when/where the variant acts. Authors explicitly frame results as **mechanistic hypotheses** for follow-up.
- Whole-genome / regulatory variation, longitudinal trajectories, and digital phenotyping are absent; associations are "beyond single-gene" but still gene-set level, not causal at the variant level (the saturation-mutagenesis / organoid gap).
