---
title: "Integrating de novo and inherited variants in 42,607 autism cases identifies mutations in new moderate-risk genes."
kind: paper
status: ingested
deep_ingested: 2026-06-09
added: 2026-06-09
doi: 10.1038/s41588-022-01148-2
pmid: 35982159
authors: Zhou X et al.
journal: Nature genetics (2022)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Zhou_2022_Integrating_de_novo_inherited_variants_42_607.pdf
pdf_status: downloaded
---

# Integrating de novo and inherited variants in 42,607 autism cases identifies mutations in new moderate-risk genes.

## Source

- Authors: Zhou X, Feliciano P, Shu C, Wang T, Astrovskaya I, Hall JB, Obiajulu JU, Wright JR et al.
- Journal: Nature genetics (2022)
- DOI: [10.1038/s41588-022-01148-2](https://doi.org/10.1038/s41588-022-01148-2)
- PMID: [35982159](https://pubmed.ncbi.nlm.nih.gov/35982159/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

To capture the full spectrum of genetic risk for autism, we performed a two-stage analysis of rare de novo and inherited coding variants in 42,607 autism cases, including 35,130 new cases recruited online by SPARK. We identified 60 genes with exome-wide significance (P < 2.5 × 10-6), including five new risk genes (NAV3, ITSN1, MARK2, SCAF1 and HNRNPUL2). The association of NAV3 with autism risk is primarily driven by rare inherited loss-of-function (LoF) variants, with an estimated relative risk of 4, consistent with moderate effect. Autistic individuals with LoF variants in the four moderate-risk genes (NAV3, ITSN1, SCAF1 and HNRNPUL2; n = 95) have less cognitive impairment than 129 autistic individuals with LoF variants in highly penetrant genes (CHD8, SCN2A, ADNP, FOXP1 and SHANK3) (59% vs 88%, P = 1.9 × 10-6). Power calculations suggest that much larger numbers of autism cases are needed to identify additional moderate-risk genes.

## Key findings

- **Cohort: 42,607 ASD cases** (35,130 new SPARK cases + 7,665 from ASC, MSSNG, SSC). Two-stage design integrating de novo variants (DNVs), transmission disequilibrium of inherited LoF, and case–control burden.
- **60 genes at exome-wide significance (P < 2.5 × 10⁻⁶); 72 genes at study-wide significance (P < 8.7 × 10⁻⁶)** across 5,754 constrained genes. **Five new risk genes not previously implicated in NDDs: NAV3, ITSN1, MARK2, SCAF1, HNRNPUL2.**
- **NAV3** association is **primarily driven by rare inherited LoF**, estimated **relative risk ~4** (point estimates of RR 3–6 for both NAV3 and ITSN1) — a *moderate*-effect gene, contrasting with high-penetrance de novo genes. NAV3 is highly expressed in the inner cortical plate of developing cortex and in pyramidal neurons/interneurons.
- **Mode of inheritance splits by penetrance:** known DNV-enriched genes carry more de novo than inherited LoF in ~16,000 unrelated trios (high penetrance, strong negative selection); genes significant only in meta-analysis carry more *inherited* LoF (lower penetrance). MARK2 is DNV-driven (also associated with other NDDs, Tourette, epilepsy; DeNovoWEST P = 2.7 × 10⁻⁵).
- **Inherited risk is largely in unknown genes:** known ASD/NDD genes explain ~two-thirds of the population-attributable risk (PAR) from damaging DNVs but only **~20% (one-fifth) of the overtransmission** of ultra-rare LoF to affected offspring → most inherited-risk genes remain undiscovered.
- **Burden concentrates in constrained genes:** excess damaging DNVs (de novo LoF + D-mis, REVEL ≥0.5) and inherited-LoF overtransmission both concentrate in LoF-intolerant genes (ExAC pLI ≥0.5; top 20% gnomAD LOEUF). Overall PAR from damaging DNVs ≈ 10%.
- **Phenotype / cognitive impairment (severity stratifier, theme 5/6):** individuals with high-confidence LoF in the **four novel moderate-risk genes (n = 87) had 56% cognitive impairment vs 88% for 129 individuals with LoF in well-established genes (CHD8, SCN2A, SHANK3, ADNP, FOXP1), P = 4.5 × 10⁻⁷**; the moderate-risk group did not differ from 8,731 general SPARK ASD cases (56% vs 50%, n.s.). *(The abstract reports the parallel figure as n=95, 59% vs 88%, P = 1.9 × 10⁻⁶; main text uses n=87 / 56% / P = 4.5 × 10⁻⁷.)*
- **Sex bias tracks penetrance:** moderate-risk-gene carriers had a male:female ratio ~4:1 (like the overall cohort), whereas well-established high-penetrance gene carriers showed *less* male bias (1.6:1, P = 0.009).
- **Inherited LoF in top-10% LOEUF genes are associated with cognitive impairment:** overtransmission to cognitively impaired cases ~2.7× that to unimpaired (P = 4.6 × 10⁻³), still ~2× after removing known genes (P = 0.04) — but A-risk-prioritized genes' inherited LoF were *not* ID-associated, indicating a subset of inherited risk acts independently of intellectual disability.
- **X chromosome:** maternal rare LoF significantly overtransmitted to affected sons but not daughters (remains significant after removing known genes).
- **Effect size ↔ IQ:** significant negative correlation (r = 0.78, P = 0.001) between estimated relative risk of rare LoF and average predicted IQ of carriers. **Power calc: substantially larger cohorts needed** to find more moderate-risk genes.

## Methods

- **Data:** exome/WGS from 35,130 new SPARK cases + ASC, MSSNG, SSC. Stage 1 (discovery): DNVs in 16,877 ASD trios (vs 5,764 unaffected trios) + transmission of rare LoF from 20,491 parents without ASD/ID to offspring (9,504 trios + 2,966 duos). Stage 2 (replication/meta): 22,764 additional cases; expanded family set (+6,174 new trios, +1,942 new duos) plus 15,780 unrelated cases of unknown inheritance.
- **Variant classes:** de novo LoF and damaging missense (D-mis = REVEL ≥0.5); ultra-rare (AF <1×10⁻⁵) high-confidence inherited LoF filtered by LOFTEE + proportion-expressed-across-transcripts (pExt ≥0.1).
- **Gene-level tests:** DeNovoWEST (DNV enrichment + missense clustering); transmission disequilibrium test (TDT) on inherited LoF; case–control burden vs two population references — gnomAD v2.1.1 non-neuro exomes (n = 104,068) and TOPMed freeze 8 WGS (n = 132,345); the *larger* (more conservative) P value used. 404 genes carried into stage-2 meta-analysis (159 de novo-enriched at P<0.001 + 260 TDT-prioritized; 15 overlap); final meta-analysis on **367 autosomal LoF-intolerant genes** combining three independent P values by Fisher's method.
- **Mega-analysis:** high-confidence LoF in all **31,976 unrelated cases** vs up to 132,000 controls to estimate per-gene effect sizes (cumulative allele frequency comparison) and selection coefficients (mutation–selection balance model, ŝ).
- **Gene prioritization aids:** 25 functional gene sets (transcriptome/proteome/regulome) + ML predictors **forecASD** and **A-risk** (A-risk ≥0.4 prioritized 1,464 constrained genes explaining 64% of inherited-LoF overtransmission, P = 2.6 × 10⁻⁵). Predicted full-scale IQ from parent-reported data via ML.

## Relevance to the brain-organoid ASD review

- **Core "ASD genetic architecture" citation (theme 1):** supplies the up-to-date risk-gene count (**60 exome-wide / 72 study-wide genes**) and the de novo vs inherited contribution split for the manuscript's architecture overview. Documents that combined DNVs explain only ~2% of liability variance / ~10% PAR — motivating the need to capture inherited and moderate-effect risk.
- **High- vs moderate-penetrance distinction → tiered organoid models:** the quantitative contrast (moderate-risk genes ~RR 4, 56% ID, 4:1 male bias vs high-penetrance genes 88% ID, 1.6:1) directly supports manuscript claims that organoid platforms must model a *spectrum* of effect sizes, not just syndromic high-penetrance genes (CHD8/SCN2A/SHANK3/ADNP/FOXP1).
- **Computational variant prioritization (theme 3):** the A-risk and forecASD machine-learning prioritizers — and the demonstration that A-risk captures inherited risk that constraint (LOEUF) alone misses — are concrete examples for the review's variant-prioritization section.
- **Sex differences (theme 5):** the penetrance-dependent male bias and X-linked maternal overtransmission to sons supply genetic-architecture evidence for the female-protective-effect discussion (complements Iossifov 2014 female de novo enrichment and Shaw 2025 epidemiologic 3.4:1 ratio).
- **Developmental-stage convergence (theme 2):** NAV3 expression in the inner cortical plate and new genes' neuronal expression reinforce arguments that risk genes converge on specific developing-cortex contexts that organoids recapitulate.
- **Names new candidate genes for functional/saturation follow-up:** NAV3, ITSN1, SCAF1, HNRNPUL2, MARK2 are concrete targets for the variant-effect-mapping (themes 4/6) the review proposes — moderate-effect genes where functional evidence (PS3/BS3) would most change interpretation.

## Open questions / limitations

- Most inherited-risk genes remain unidentified (known genes explain only ~20% of LoF overtransmission); explicit **power calculations indicate much larger cohorts are required** to detect additional moderate-risk genes — individual moderate-effect genes mostly fall short of exome-wide significance here.
- Effect-size estimates for new genes are point estimates with wide ranges (RR ~3–6) from case–control allele-frequency comparison against population references processed by different pipelines (mitigated by using the more conservative P value and ancestry checks, but residual confounding possible).
- Case–control controls (gnomAD non-neuro, TOPMed) are population references, not matched; relies on the assumption that demographic history does not confound cumulative allele frequencies of strongly selected alleles (selection coefficient >0.001).
- Cognitive-impairment phenotype is heterogeneous in source (self-reported in SPARK, Vineland <70 in SSC, ID flag in ASC) and ML-predicted IQ is an approximation.
- Analysis is coding-variant-focused (exome/WGS coding); non-coding/regulatory inherited risk and common-variant (polygenic) contribution are out of scope (see Grove 2019 for common variants).
- Discrepancy noted between abstract (moderate-risk n=95, 59% vs 88%, P=1.9×10⁻⁶) and main text (n=87, 56% vs 88%, P=4.5×10⁻⁷) for the cognitive-impairment comparison — use main-text figures as primary.
