---
title: "Rates, distribution and implications of postzygotic mosaic mutations in autism spectrum disorder."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/nn.4598
pmid: 28714951
authors: Lim ET et al.
journal: Nature neuroscience (2017)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Lim_2017_Rates_distribution_implications_postzygotic_mosaic_mutations_autism.pdf
pdf_status: downloaded
---

# Rates, distribution and implications of postzygotic mosaic mutations in autism spectrum disorder.

## Source

- Authors: Lim ET, Uddin M, De Rubeis S, Chan Y, Kamumbu AS, Zhang X, D'Gama AM, Kim SN et al.
- Journal: Nature neuroscience (2017)
- DOI: [10.1038/nn.4598](https://doi.org/10.1038/nn.4598)
- PMID: [28714951](https://pubmed.ncbi.nlm.nih.gov/28714951/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

We systematically analyzed postzygotic mutations (PZMs) in whole-exome sequences from the largest collection of trios (5,947) with autism spectrum disorder (ASD) available, including 282 unpublished trios, and performed resequencing using multiple independent technologies. We identified 7.5% of de novo mutations as PZMs, 83.3% of which were not described in previous studies. Damaging, nonsynonymous PZMs within critical exons of prenatally expressed genes were more common in ASD probands than controls (P < 1 × 10-6), and genes carrying these PZMs were enriched for expression in the amygdala (P = 5.4 × 10-3). Two genes (KLF16 and MSANTD2) were significantly enriched for PZMs genome-wide, and other PZMs involved genes (SCN2A, HNRNPU and SMARCA4) whose mutation is known to cause ASD or other neurodevelopmental disorders. PZMs constitute a significant proportion of de novo mutations and contribute importantly to ASD risk.

## Key findings

- **PZM rate ~7.5% of detectable de novo mutations.** Derived as 9.7% (high-confidence PZM share of DNMs) × 0.84 (fraction of Group C that are genuinely de novo) × 0.92 (fraction of Group C that are genuine PZMs) ≈ 7.5%. Authors stress this is a *floor* set by WES coverage; true rate would rise with deeper sequencing.
- **Cohort:** 5,947 families recalled (4,032 ASD trios + 1,918 quads with unaffected siblings); 282 trios newly sequenced (Autism Sequencing Consortium + Simons Simplex Collection). 96% whole-blood DNA, 3% lymphoblastoid, 1% saliva. Conservative recall = <1 DNM per exome; **4,846 total DNMs** after filtering variants seen in control exomes.
- **Allele-fraction (AAF) signature of mosaicism.** Modal AAF ~50% (germline heterozygous expectation). A 4.1-fold excess of DNMs at AAF ≤40% (23.7% of all DNMs) vs AAF ≥60% (5.8%); DNMs (not inherited variants) drive the low-AAF tail (OR = 1.67 at AAF ≤40% vs OR = 0.82 at AAF ≥60%). PZMs detectable by WES require roughly >25–30% of cells affected (≈15% AAF).
- **Three nested groups:** Group A = all 4,846 DNMs; Group B = 1,113 candidate PZMs (23%, AAF ≤80% of modal); Group C = 468 high-confidence PZMs (9.7%, statistically significant deviation from modal AAF).
- **Novelty:** 83.3% of Group C high-confidence PZMs (390/468) were *not* reported by prior calling pipelines; 55.4% of Group B (617/1,113) were new; 26.8% (1,297) of all Group A DNMs were new vs the source datasets. Prior pipelines tended to discard these as low-quality calls.
- **Validation across 3 orthogonal technologies** (CloneSeq subcloning+Sanger, Pyroseq, targeted-PCR+MiSeq). Group C confirmed as AAF ≤40% at 84.8–97.0% across phases; Group B (not C) only 13.7–38%; predicted germline DNMs 0–8.3%. CloneSeq vs targeted-PCR+MiSeq AAF correlation r = 0.85; Pyroseq correlated worse at low AAF (r = 0.64 vs 0.92 for MiSeq), so MiSeq is the recommended high-throughput substitute. ~84.1–89% of tested DNMs confirmed genuinely de novo (absent in parents).
- **Distinct mutational profile vs germline DNMs and cancer.** PZMs enriched on the antisense strand (OR = 1.30, 95% CI 1.07–1.58, Group C) — consistent with transcription-coupled repair bias. Enriched for A→C / T→G changes (OR = 2.23, 95% CI 1.64–2.99) tied to the nucleosome core, hinting at chromatin-remodeling relevance (a pathway already implicated in ASD). Trend toward late-replication timing (OR = 1.36, 95% CI 0.83–2.14) but **not significant** (Fisher P = 0.2) and weaker than in cancer.
- **Functional/anatomical enrichment.** Damaging nonsynonymous PZMs in critical exons of prenatally expressed genes were more common in probands than controls (P < 1 × 10⁻⁶); PZM-carrying genes enriched for amygdala expression (P = 5.4 × 10⁻³).
- **Implicated genes.** Genome-wide PZM enrichment for **KLF16** and **MSANTD2**; additional PZMs hit known NDD/ASD genes **SCN2A, HNRNPU, SMARCA4**.
- **CNV confounding ruled low:** TaqMan copy-number assays on 36 Group C PZMs found no co-occurring CNVs (PZM–CNV overlap likely <3%).

## Methods

- Joint re-calling of WES from 5,947 ASD families with current GATK best practices; filtered out DNMs present in control exomes to enrich for likely-pathogenic, large-effect variants.
- Custom pipeline to quantitatively classify candidate PZMs by deviation of AAF from the per-sample modal AAF (40–50%); Group B threshold = AAF ≤80% of modal, Group C = statistically significant deviation.
- Three-phase orthogonal resequencing (50, then 181, then 325 mutations) by CloneSeq, Pyroseq, and targeted-PCR + MiSeq to confirm AAF ≤40% and de novo status; Sanger used to confirm absence in parents.
- TaqMan copy-number assays to exclude CNV-driven false PZMs.
- Burden tests comparing proband vs sibling/control PZMs; tissue/developmental expression enrichment (prenatal expression, amygdala); strand/replication-timing/mutational-spectrum analyses vs germline DNMs and published cancer somatic catalogs.

## Relevance to the brain-organoid ASD review

- Supplies the **quantitative case for mosaicism in ASD**: ~7.5% of detectable DNMs (a conservative WES-limited floor) arise postzygotically, motivating models that can recapitulate cell-to-cell genetic heterogeneity rather than a single uniform genotype.
- Directly motivates **3D organoid modeling of mosaicism**: PZMs create distinct cell populations within one individual, and damaging PZMs concentrate in *prenatally expressed* genes with *amygdala* enrichment — i.e., developmental windows and regional identities an organoid system aims to reproduce. Genes flagged here (KLF16, MSANTD2, SCN2A, HNRNPU, SMARCA4) are candidate perturbation targets.
- Methodologically anchors **detection limits** any organoid/sequencing readout must respect: PZMs need ~15% AAF (>25–30% of cells) to be WES-visible; targeted deep sequencing (MiSeq) recovers far more, relevant for measuring induced or clonal mosaic edits in organoids.
- Cross-link: clinical-interpretation standard for functional evidence — [Brnich 2019 PS3/BS3](Brnich_2019_Recommendations_application_functional_evidence_PS3_BS3_criterion.md); targeted NDD gene-discovery panel overlapping SCN2A and other shared genes — [Stessman 2017](Stessman_2017_Targeted_sequencing_identifies_91_neurodevelopmental_disorder_risk.md).

## Open questions / limitations

- Rate is a **lower bound**: WES coverage misses low-AAF PZMs; deeper/targeted sequencing or single-cell data would raise the estimate. Quantitative true PZM burden remains unknown.
- Nearly all DNA was **whole blood** (96%); blood AAF need not match brain AAF, and brain-restricted PZMs would be invisible here.
- Late-replication-timing association did not reach significance (P = 0.2); the mechanistic origin of PZMs (vs cancer somatic mutations) is only partially resolved.
- Genome-wide significance limited to two novel genes (KLF16, MSANTD2); per-gene power for most PZM-carrying genes is low, so individual gene-level ASD causation is not established by this study alone.
- The study does not establish clinical pathogenicity of individual PZMs — it quantifies burden and distribution, not variant-level interpretation.
