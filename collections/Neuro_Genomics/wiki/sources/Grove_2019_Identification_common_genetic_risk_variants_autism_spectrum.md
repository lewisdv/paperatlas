---
title: "Identification of common genetic risk variants for autism spectrum disorder."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41588-019-0344-8
pmid: 30804558
authors: Grove J et al.
journal: Nature genetics (2019)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Grove_2019_Identification_common_genetic_risk_variants_autism_spectrum.pdf
pdf_status: downloaded
---

# Identification of common genetic risk variants for autism spectrum disorder.

## Source

- Authors: Grove J, Ripke S, Als TD, Mattheisen M, Walters RK, Won H, Pallesen J, Agerbo E et al.
- Journal: Nature genetics (2019)
- DOI: [10.1038/s41588-019-0344-8](https://doi.org/10.1038/s41588-019-0344-8)
- PMID: [30804558](https://pubmed.ncbi.nlm.nih.gov/30804558/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Autism spectrum disorder (ASD) is a highly heritable and heterogeneous group of neurodevelopmental phenotypes diagnosed in more than 1% of children. Common genetic variants contribute substantially to ASD susceptibility, but to date no individual variants have been robustly associated with ASD. With a marked sample-size increase from a unique Danish population resource, we report a genome-wide association meta-analysis of 18,381 individuals with ASD and 27,969 controls that identified five genome-wide-significant loci. Leveraging GWAS results from three phenotypes with significantly overlapping genetic architectures (schizophrenia, major depression, and educational attainment), we identified seven additional loci shared with other traits at equally strict significance levels. Dissecting the polygenic architecture, we found both quantitative and qualitative polygenic heterogeneity across ASD subtypes. These results highlight biological insights, particularly relating to neuronal function and corticogenesis, and establish that GWAS performed at scale will be much more productive in the near term in ASD.

## Key findings

- **First robust common-variant ASD loci.** GWAS meta-analysis of **18,381 ASD cases + 27,969 controls** (iPSYCH Danish case–cohort 13,076 cases/22,664 controls + 5 PGC family-based trio samples, 5,305 cases/5,305 pseudocontrols) over 9,112,387 autosomal markers yielded **3 genome-wide-significant loci** in the primary scan; adding a follow-up sample (2,119 cases, 142,379 controls) brought **5 loci** to genome-wide significance in ASD alone. Lead loci near *MACROD2* (rs71190156), *KIZ/XRN2/NKX2-2/NKX2-4* (rs910805, P = 2.04 × 10⁻⁹), *SOX7/PINX1* region (rs10099100), *PTBP2* (rs201910565), and *KMT2E/SRPK2* (rs111931861).
- **SNP-based heritability h²_SNP = 0.118 (s.e.m. 0.010)** at assumed population prevalence 0.012 — confirming common variants explain a major fraction of ASD liability. By contrast (cited background), de novo mutations have larger individual effects but collectively explain <5% of overall liability.
- **+7 additional loci via MTAG** leveraging genetically correlated traits (schizophrenia, major depression, educational attainment) at a stricter threshold P < 1.67 × 10⁻⁸ (maxFDR 0.021): 3 shared with educational attainment, 4 with major depression. Effect sizes were stronger in ASD than the secondary trait; 3 of 7 were not significant in the secondary trait.
- **Genetic correlations (bivariate LDSC)** with: major depression r_G = 0.412 (P = 1.40 × 10⁻²⁵), ADHD r_G = 0.360 (novel, P = 1.24 × 10⁻¹²), schizophrenia r_G = 0.211 (P = 1.03 × 10⁻⁵), educational attainment r_G = 0.199 (P = 2.56 × 10⁻⁹), childhood social-communication difficulties r_G = 0.375. iPSYCH vs PGC cross-design r_G = 0.779.
- **Gene-based MAGMA** found 15 significant genes; 7 lay in 4 loci beyond the GWAS-significant regions, notably ***KCNN2*** (P = 1.02 × 10⁻⁹, a Ca²⁺-activated K⁺ channel), *MMP12*, *NTM*, and a chr17 cluster (*KANSL1, WNT3, MAPT, CRHR1*).
- **Quantitative polygenic heterogeneity across subtypes:** h²_SNP of Asperger's syndrome (0.097) was ~2× that of childhood autism (0.049, P = 0.001) and other/unspecified PDD (0.045, P = 0.001); ASD **without** ID (0.086) was ~3× ASD **with** ID (0.029, P = 0.015). Pairwise genetic correlations among subtypes were uniformly high (95% CIs included 1).
- **Qualitative heterogeneity:** of 8 PRS phenotypes tested across ASD subgroups, only cognitive scores (educational attainment P = 1.8 × 10⁻⁸; IQ P = 3.7 × 10⁻⁹) showed strong differential loading. Excess education-associated alleles were confined to Asperger's (P = 2.0 × 10⁻¹⁷) and childhood autism (P = 1.5 × 10⁻⁵), not atypical autism or other/unspecified PDD. Hypothesis of homogeneity across subphenotypes strongly rejected (P = 1.6 × 10⁻¹¹).
- **PRS prediction:** ASD PRS explained mean **Nagelkerke's R² = 2.45%** (pooled OR = 1.33; highest-vs-lowest decile OR = 2.80, 95% CI 2.53–3.10). A multi-phenotype PRS raised R² to **3.77%** (top-decile OR = 3.57). Risk scaled dose-dependently with polygenic burden.
- **Spatiotemporal convergence on corticogenesis:** 380 credible SNPs (28 loci) assigned via fetal-brain Hi-C (cortical plate CP + germinal zone GZ) to 95 genes (40 protein-coding); 34 genes interacted in both CP and GZ (high-confidence set). Credible SNPs were enriched in fetal-brain enhancer marks, and ASD-candidate genes showed **peak expression during fetal corticogenesis**. Authors note both common and rare ASD risk preferentially affect genes expressed during corticogenesis.

## Methods

- **Discovery:** iPSYCH Danish nationwide population-based case–cohort (births 1981–2005, ICD-10 ASD diagnosed before 2014), genotyped from neonatal dried blood spots; QC/imputation via Ricopili with 1000 Genomes phase 3 panel. Meta-analyzed with 5 PGC European trio cohorts using inverse-variance-weighted fixed-effects on markers with MAF ≥ 0.01 and INFO ≥ 0.7. Inflation λ = 1.12 (λ₁₀₀₀ = 1.006); LDSC attributed >96% to polygenicity, not confounding.
- **Replication/follow-up:** top loci (P < 1 × 10⁻⁵) in 5 cohorts (2,119 cases, 142,379 controls); combined analysis.
- **Cross-trait:** bivariate LDSC against 234 LD Hub traits; **MTAG** (multi-trait analysis of GWAS) run as 3 pairwise scans with schizophrenia, major depression, educational attainment (height/BMI as negative controls — added no ASD loci). Largest MTAG weights: SCZ 0.27, MD 0.24, EduAttain 0.11.
- **Gene/gene-set:** MAGMA gene-based test; enrichment vs neocortical coexpression modules (Parikshak M13/M16/M17), pLI > 0.9 LoF-intolerant genes, SPARK/Sanders ASD gene lists, MSigDB GO sets.
- **Polygenic architecture:** GCTA h²_SNP partitioned across ICD-10 subtypes (childhood autism F84.0 n = 3,310; atypical F84.1 n = 1,607; Asperger's F84.5 n = 4,622; other/unspecified PDD F84.8-9 n = 5,795) and ID status (with ID n = 1,873); PRS distributions regressed on subgroups; 5-way PRS train/target splits within iPSYCH-PGC.
- **Functional:** credible-set fine-mapping; integration with fetal-brain Hi-C (CP and GZ), eQTL, and brain expression trajectories.

## Relevance to the brain-organoid ASD review

- **Theme 1 (ASD genetic architecture):** This is the anchor common-variant / GWAS heritability reference. Establishes h²_SNP ≈ 0.12 from common SNPs and the dose-dependent polygenic PRS model, complementing the rare-variant exome papers (De Rubeis, Iossifov, Satterstrom, Zhou) in the collection — common + rare jointly define the architecture an organoid platform must model.
- **Theme 2 (convergence on developmental vulnerability stages):** Strongest tie. Fetal-brain Hi-C maps common-variant credible SNPs onto genes peaking in expression during **fetal corticogenesis (CP + GZ)**, and the paper explicitly argues common AND rare ASD risk converge on corticogenesis despite heterogeneity. This is the common-variant counterpart to De Rubeis/Willsey mid-fetal neocortex convergence and Litman's prenatal-expression timing — the developmental window programmable organoids should target.
- **Theme 3 (computational variant prioritization):** Demonstrates MTAG cross-trait borrowing, MAGMA gene-based testing, LDSC partitioning, and Hi-C–based SNP-to-gene assignment — methods for prioritizing/interpreting non-coding GWAS signal before functional follow-up.
- **Theme 5 (sex differences):** Indirect; this GWAS does not center sex, but its common-variant liability framework is the backdrop against which the female-protective-effect (rare-variant) literature operates.
- **Theme 7 (ASD subtypes / phenotypic heterogeneity):** Provides genetic evidence that DSM/ICD subtypes differ **quantitatively** (Asperger's h² ≈ 2× childhood autism; no-ID ≈ 3× ID) and **qualitatively** (cognitive PRS loading confined to Asperger's + childhood autism). Directly motivates Litman's data-driven decomposition and any organoid effort stratified by subtype.

## Open questions / limitations

- Only **5 genome-wide-significant ASD-alone loci** despite >18k cases — power-limited; effect sizes per common variant are tiny and most heritability remains in undiscovered polygenic background. PRS explains only ~2.5% (3.8% multi-trait) of variance — far from clinically predictive.
- **MTAG loci are provisional:** they borrow signal from correlated traits, so precise ASD-specific phenotypic consequences "await expansion of all these trait GWAS." Genetic correlations were modest, so cross-trait weights were small.
- Subtype heritability differences rest on ICD-10 registry diagnoses (validated but susceptible to diagnostic drift over 1981–2005); pairwise subtype r_G CIs all included 1, so subtypes are not genetically distinct in correlation, only in magnitude/qualitative PRS loading.
- Functional gene assignment via Hi-C is correlative (physical contact, not causal regulation); credible-set genes are candidates, not validated effectors — exactly the gap a saturation-mutagenesis / organoid functional platform is meant to close.
- Ancestry restricted to European; X-chromosome best signal only P = 7.8 × 10⁻⁵ (no GW-significant X locus), leaving sex-chromosome contribution unresolved here.
