---
title: "Rare coding variation provides insight into the genetic architecture and phenotypic context of autism"
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41588-022-01104-0
pmid: 35982160
authors: Fu JM et al.
journal: Nature genetics (2022)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Fu_2022_Rare_coding_variation_provides_insight_into_genetic.pdf
pdf_status: downloaded
---

# Rare coding variation provides insight into the genetic architecture and phenotypic context of autism

## Source

- Authors: Fu JM, Satterstrom FK, Peng M, Brand H, Collins RL, Dong S, Wamsley B, Klei L (+ Autism Sequencing Consortium [ASC], Broad-CCDG, iPSYCH-BROAD; senior authors Buxbaum, Daly, Devlin, Roeder, Sanders, Talkowski)
- Journal: Nature genetics (2022), vol. 54, 1320–1331
- DOI: [10.1038/s41588-022-01104-0](https://doi.org/10.1038/s41588-022-01104-0)
- PMID: [35982160](https://pubmed.ncbi.nlm.nih.gov/35982160/)
- Added via: manuscript_brain_organoid_v6 reference ingest (foundational gap-fill)

## Abstract

Some individuals with autism spectrum disorder (ASD) carry functional mutations rarely observed in the general population. We explored the genes disrupted by these variants from joint analysis of protein-truncating variants (PTVs), missense variants and copy number variants (CNVs) in a cohort of 63,237 individuals. We discovered 72 genes associated with ASD at false discovery rate (FDR) ≤ 0.001 (185 at FDR ≤ 0.05). De novo PTVs, damaging missense variants and CNVs represented 57.5%, 21.1% and 8.44% of association evidence, while CNVs conferred greatest relative risk. Meta-analysis with cohorts ascertained for developmental delay (DD) (n = 91,605) yielded 373 genes associated with ASD/DD at FDR ≤ 0.001 (664 at FDR ≤ 0.05), some of which differed in relative frequency of mutation between ASD and DD cohorts. The DD-associated genes were enriched in transcriptomes of progenitor and immature neuronal cells, whereas genes showing stronger evidence in ASD were more enriched in maturing neurons and overlapped with schizophrenia-associated genes, emphasizing that these neuropsychiatric disorders may share common pathways to risk.

## Key findings

**This paper is the true primary source of the "185 genes at FDR ≤ 0.05" and "72 genes at FDR ≤ 0.001" figures (across ~63,000 samples) often cited in the brain-organoid ASD review.** Exact gene counts at each threshold, verified against the paper text:

- **ASD-only analysis (TADA-ASD, n = 63,237):**
  - **72 genes** associated with ASD at **FDR ≤ 0.001** (Fig. 3b; ≈ exome-wide Bonferroni, back-calculated `P < 2.8 × 10⁻⁶` across 18,128 autosomal genes).
  - **185 genes** associated with ASD at **FDR ≤ 0.05** (Supplementary Table 11).
- **ASD + DD meta-analysis (TADA-NDD, DD cohorts n = 91,605; 31,058 DD-affected individuals):**
  - **373 genes** associated with ASD/DD at **FDR ≤ 0.001**; of these, **54 genes were unique to the joint analysis** (not reaching FDR ≤ 0.001 in either dataset alone).
  - **664 genes** at **FDR ≤ 0.05**.
- **Allelic architecture / share of association evidence:** de novo PTVs = **57.5%**, damaging missense = **21.1%**, CNVs = **8.44%** of the association signal. Among the 72 FDR ≤ 0.001 genes, de novo PTV/MisB/MisA variants were carried by **4.0% of cases vs 0.5% of controls** (combined OR **8.44**, `P = 3.4 × 10⁻⁵¹`, Fisher's exact).
- **CNVs confer the greatest relative risk per event**, even though they contribute the smallest share of total evidence; de novo CNVs were enriched in cases (3.95% of ASD cases vs 1.39% of unaffected siblings carried ≥1 de novo coding CNV; OR 2.91, `P = 2.2 × 10⁻²¹`). De novo deletions of constrained genes conferred relative risk ~3× that of de novo PTVs in the same constraint decile.
- **Missense stratification by MPC score:** MisB (MPC ≥ 2) strongly enriched in cases; MisA (1 ≤ MPC < 2) only modestly enriched. PTVs and MisB confer similar relative risk; MisA much less.
- **Moderate-penetrance / ascertainment gradient (architecture point the review leans on):** de novo PTV burden varies by ascertainment — highest in DD/ID/multisystem-congenital cohorts, **moderate in ASD or isolated developmental anomalies, lowest in schizophrenia**. Most ASD heritability is common-variant/polygenic; rare high-impact coding variants explain risk in ≥ ~10% of cases. → Rare ASD risk variants are individually penetrant but the disorder as a whole is genetically heterogeneous and largely polygenic.
- **Cell-type enrichment:** DD-predominant genes enriched in progenitor and immature neuronal transcriptomes (earlier, less-differentiated cells); ASD-predominant genes enriched in maturing/post-mitotic neurons (excitatory + interneurons). Ratio of maturing-to-progenitor enrichment 1.29 (ASD) vs 0.7 (DD).
- **Schizophrenia overlap:** SCHEMA identified 244 schizophrenia genes (`P < 0.01`); 234 are in this TADA model. Of the 72 FDR ≤ 0.001 ASD genes, 61 also DD-associated and 8 schizophrenia-associated. ASD-predominant genes were significantly enriched for schizophrenia overlap (6/36; `P = 8.4 × 10⁻⁶`) including ANK2, ASH1L, BRSK2, CGREF1, DSCAM, NRXN1; DD-predominant overlap was not enriched (3/82). Suggests distinct ASD subsets overlap DD vs schizophrenia.
- **Recessive signal (exploratory):** 10 genes had ≥2 offspring with biallelic (homozygous/compound-het) PTV/MisB and none in unaffected siblings — B3GALT6, BTN2A2, DNAAF3, EIF3I, FEV, KCP, RDH11, RNF39, RNF175, SSPO. Most not previously tied to recessive ASD; flagged for follow-up.
- **Sex / female protective effect:** more female than male cases carried de novo CNVs (6.0% vs lower in males). Logistic regression over the 185 genes + GD loci: damaging-variant carriers more likely female AND more severely affected (lower FSIQ, n = 2,095; higher ADOS, n = 5,280), combining additively with **no interaction** — favoring a female protective effect over ascertainment bias.

## Methods

- **Cohort:** 33 ASD cohorts, 63,237 individuals — 15,036 affected probands, 28,522 parents, 5,492 unaffected siblings (family/trio data) + 5,591 cases and 8,597 controls (case-control). Family-based n = 49,049; case-control n = 14,188.
- **Variant classes jointly modeled:** PTVs; deleterious missense split by MPC (MisB ≥ 2; MisA 1–2); and CNVs (deletions/duplications), discovered from exomes using **GATK-gCNV** (benchmarked vs WGS: 86% sensitivity / 90% PPV for rare CNVs spanning >2 captured exons; 83% sens / 97% PPV for de novo CNVs). Genomic-disorder (GD)/recurrent loci distinguished from non-GD individual-gene CNVs.
- **Statistical framework:** extended **Transmission And De novo Association (TADA)** Bayesian model integrating de novo, case-control, and rare-inherited modules for each variant type (PTV, MisB, MisA, deletion, duplication), incorporating gnomAD constraint (**LOEUF**) and per-class relative-risk priors; per-gene Bayes factors → FDR. Cross-validation used to refine variant-class-specific risk.
- **Meta-analysis:** same TADA framework applied jointly to ASD + DD cohorts (DD n = 91,605) to produce TADA-NDD gene lists.
- **Downstream:** single-cell fetal-cortex RNA-seq for cell-type enrichment; comparison to SCHEMA schizophrenia genes; phenotype regressions on FSIQ/ADOS.

## Relevance to the brain-organoid ASD review

- **This is the real, citable source of the "185-gene" headline figure** (185 at FDR ≤ 0.05; 72 at FDR ≤ 0.001) — distinct from the companion Satterstrom 2020 (102 genes) study. Any review statement attributing "185 ASD genes" should point here, with the threshold (FDR ≤ 0.05) stated.
- **Establishes the moderate-penetrance, heterogeneous architecture** that motivates a programmable-organoid "proactive" strategy: hundreds of genes, each individually high-impact but collectively heterogeneous, with risk graded by ascertainment severity. Organoid platforms that can model many genes in parallel match this many-genes problem.
- **Cell-type and developmental-timing results** (ASD genes enriched in maturing neurons; DD genes in progenitors) give a concrete benchmark for which organoid stages/cell types a model must capture to be relevant to ASD vs broader NDD biology.
- **Provides the prioritized gene set** (72 / 185 / 373) from which organoid experiments can draw load-bearing targets, plus the SCN2A/CHD8/ANK2/NRXN1-type high-confidence genes shared with schizophrenia.

## Open questions / limitations

- TADA-ASD discovery is still **dominated by de novo loss-of-function**; subtler missense and intragenic/single-exon duplication effects remain under-powered — true effect sizes for MisA and duplications uncertain.
- **ASD vs DD separation is imperfect** due to comorbidity; only ~13.4% of TADA-ASD signal could be cleanly attributed to ASD-specific (vs general-NDD) risk. Many "ASD genes" are really broad NDD genes.
- The **recessive analysis (10 genes)** is exploratory; the framework was not designed for autosomal-recessive risk and these need replication.
- Gene-level FDR thresholds depend on constraint priors and mutation-rate models; gene counts are threshold-dependent (185 vs 72 differ only by FDR cutoff), so citations must state the FDR used.
- Cohort is predominantly European-ancestry; generalizability across ancestries is not established here.
