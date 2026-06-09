---
title: "Synaptic, transcriptional and chromatin genes disrupted in autism."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/nature13772
pmid: 25363760
authors: De Rubeis S et al.
journal: Nature (2014)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/De_2014_Synaptic_transcriptional_chromatin_genes_disrupted_autism.pdf
pdf_status: downloaded
---

# Synaptic, transcriptional and chromatin genes disrupted in autism.

## Source

- Authors: De Rubeis S, He X, Goldberg AP, Poultney CS, Samocha K, Cicek AE, Kou Y, Liu L et al.
- Journal: Nature (2014)
- DOI: [10.1038/nature13772](https://doi.org/10.1038/nature13772)
- PMID: [25363760](https://pubmed.ncbi.nlm.nih.gov/25363760/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

The genetic architecture of autism spectrum disorder involves the interplay of common and rare variants and their impact on hundreds of genes. Using exome sequencing, here we show that analysis of rare coding variation in 3,871 autism cases and 9,937 ancestry-matched or parental controls implicates 22 autosomal genes at a false discovery rate (FDR) < 0.05, plus a set of 107 autosomal genes strongly enriched for those likely to affect risk (FDR < 0.30). These 107 genes, which show unusual evolutionary constraint against mutations, incur de novo loss-of-function mutations in over 5% of autistic subjects. Many of the genes implicated encode proteins for synaptic formation, transcriptional regulation and chromatin-remodelling pathways. These include voltage-gated ion channels regulating the propagation of action potentials, pacemaking and excitability-transcription coupling, as well as histone-modifying enzymes and chromatin remodellers-most prominently those that mediate post-translational lysine methylation/demethylation modifications of histones.

## Key findings

- **Largest ASD whole-exome study at the time:** 16 sample sets, 15,480 DNA samples; primary rare-variant analysis of **3,871 ASD cases + 9,937 ancestry-matched or parental controls**. Restricted to high-quality alleles at frequency <0.1%, classed as loss-of-function (LoF: frameshift, stop-gain, splice donor/acceptor) or probably-damaging missense (Mis3 by PolyPhen-2).
- **De novo LoF excess:** **13.8%** of 2,270 ASD trios carried a de novo LoF mutation vs expected 8.6% (P < 10⁻¹⁴) and 7.1% in 510 control trios (P = 1.6 × 10⁻⁵). 18 genes had ≥2 de novo LoF mutations (vs ~2 expected by chance).
- **TADA gene discovery** (integrating de novo + transmitted + case-control LoF and de novo Mis3 in a Bayesian model): **22 autosomal genes at FDR < 0.05**, **33 at FDR < 0.1**, **107 at FDR < 0.3**. Of the 33: 15 (45.5%) were known ASD genes, 11 previously reported but unconfirmed, and **7 completely novel** (*ASH1L, KMT2C/MLL3, ETFB, NAA15, MYO9B, MIB1, VIL1*).
- **>5% of ASD subjects carry a de novo LoF mutation in the FDR < 0.3 gene set**; this set is strongly enriched for genes under evolutionary constraint (P = 3.0 × 10⁻¹¹), supporting heterozygous LoF as the risk mechanism.
- **Estimated ~1,150 ASD risk genes** total (from the ratio of genes with multiple vs single de novo LoF hits) — most with modest effect, confirming extreme locus heterogeneity.
- **Three converging functional classes:** (1) **synaptic** function — voltage-gated ion channels for action-potential propagation/pacemaking/excitability–transcription coupling: *SCN2A* (Naᵥ1.2; 4 LoF + 5 Mis3), *CACNA1D* (Caᵥ1.3; 3 Mis3), *CACNA2D3* (2 LoF), plus *SYNGAP1, SHANK3, NRXN1*; (2) **transcriptional regulation**; (3) **chromatin remodelling** — gene set enriched for histone-modifier genes (9/152, P = 2.2 × 10⁻⁷) and histone-lysine N-methyltransferase activity (5/41, FDR = 2.2 × 10⁻²); of 107 TADA genes, **5 SET methyltransferases, 4 jumonji demethylases, 2 readers** (incl. *CHD8, ARID1B, ASH1L, KMT2C, SETD5, SUV420H1, KDM5B/6B*).
- **Female protective effect (orthogonal validation):** FDR < 0.1 genes show profound female enrichment for de novo events (LoF P = 0.005, Mis3 P = 0.004), consistent with large liability impact (OR ≥ 20). FDR 0.1–0.3 genes show much weaker female enrichment (modest OR ~2–4 for LoF, little/no Mis3 effect), and their LoF variants are more often inherited than de novo.
- **RNA-binding-protein target enrichment:** FMRP targets (P = 1.20 × 10⁻¹⁷, 34 targets) and RBFOX targets (P = 0.0024, 20 targets, 12 overlapping FMRP) — extending ASD neurobiology to splicing and translation. Also enrichment for de novo SCZ mutations (P = 0.0085) and shared targets of RBFOX1 + H3K4me3 (P = 0.0166).
- **CNVs corroborate:** deletion CNVs in 10 supported FDR < 0.3 genes (incl. *NRXN1, SHANK3*), with risk OR comparable to LoF SNVs.

## Methods

- **Sequencing:** Illumina HiSeq 2000; SNV/indel calling in one large GATK v2.6 batch; de novo calls validated at very high rates.
- **TADA (Transmission and De novo Association):** Bayesian gene-based likelihood integrating per-gene mutation rates, allele frequencies, and class-specific relative risks; effective weighting de novo LoF > de novo Mis3 > transmitted LoF (inherited Mis3 dropped — no aggregate signal). Outputs per-gene Bayes factor + FDR q value; more powerful than de novo LoF counting alone.
- **Gene-number estimate:** from the relative-risk distribution over inferred ASD genes (balance of multi-hit vs single-hit de novo LoF genes).
- **Enrichment:** evolutionary constraint scores; FMRP (two datasets) and RBFOX target lists; Genes2Cognition synaptic/PSD orthologues; InterPro/SMART/Pfam domain over-representation (FYVE-PHD zinc fingers FDR = 7.6 × 10⁻⁴; SET domains FDR = 8.2 × 10⁻⁴); HIstome/HMG annotation; GO molecular function.
- **DAWN (Detecting Association With Networks):** hidden Markov random field integrating TADA scores + gene coexpression in **human mid-fetal prefrontal/motor-somatosensory neocortex** + constraint scores → 160 candidate risk genes (91 not in the 107). Seeded into a high-confidence protein–protein interactome → 4 network clusters (C1 cell junction/TGFβ; C2 neurodegeneration via *MAPT*; C3 synaptic transmission/cell communication; C4 transcriptional/chromatin regulation).
- **CHD8 follow-up:** trio sequencing of case-control *CHD8* variants identified 5 de novo, including 2 essential-splice-site LoF causing exon skipping/cryptic-splice activation in lymphoblastoid cells.

## Relevance to the brain-organoid ASD review

- **Theme 1 (ASD genetic architecture):** Foundational rare-variant / de novo reference. Establishes the **TADA** framework and the ~1,150-gene estimate, and defines the gene-class taxonomy (synaptic, transcriptional, chromatin) that recurs throughout the review and the collection (Iossifov 2014, Satterstrom 2020, Zhou 2022 build on it). Pair with Grove 2019 for the common-variant complement.
- **Theme 2 (convergence on developmental vulnerability stages):** Key. DAWN's use of **mid-fetal neocortex** coexpression to implicate risk genes (and the C3/C4 synaptic + chromatin clusters) is a primary statement that rare ASD risk converges on mid-fetal cortical development — directly parallel to Grove's corticogenesis Hi-C result and Litman's prenatal-expression timing. Defines the developmental epoch and cell context a programmable organoid should reproduce.
- **Theme 4 (saturation mutagenesis / variant-effect mapping):** Strong motivator. *SCN2A* and *CACNA1D* de novo Mis3 variants map to specific functional residues (ion-selectivity-filter P-loops, DEKA ring; NSCaTE, IQ, SHANK3-binding C-terminus), and homologous-residue mutations in *SCN5A/SCN1A* abolish current — exactly the per-residue functional questions saturation mutagenesis / variant-effect maps (Findlay, Beltran, Kircher, Sahu in the collection) resolve at scale. Many TADA missense variants need functional adjudication (VUS problem).
- **Theme 5 (sex differences):** Primary quantitative source for the **female protective effect** — higher de novo burden required for diagnosis in females (OR ≥ 20 for high-confidence genes), used here as an orthogonal validity check on gene lists. Anchors the review's sex-differences theme alongside DeCasien 2026 and Satterstrom 2026 (X chromosome).
- **Theme 6 (clinical variant interpretation, ACMG/ClinGen):** The de novo LoF / damaging-missense framing and constraint enrichment underpin PVS1/PS2/PM2-type evidence; the unresolved Mis3 variants are candidate substrates for PS3/BS3 functional evidence (Brnich 2019 in the collection).
- **Theme 7 (ASD subtypes / phenotypic heterogeneity):** Shows risk genes vary by effect size and inheritance mode (high-OR de novo vs modest inherited), foreshadowing Litman's class-specific de novo-vs-inherited partition.

## Open questions / limitations

- Discovery numbers are **threshold-dependent**: 22 genes (FDR < 0.05), 33 (FDR < 0.1), 107 (FDR < 0.3) — the FDR 0.1–0.3 tier may contain ~one-third false positives, so "107 genes" is a high-sensitivity, lower-specificity set.
- TADA assigns the **same relative risk to all variants within a class per gene** — it does not distinguish gain- vs loss-of-function or graded missense severity, leaving per-allele effects unmapped (the saturation-mutagenesis gap).
- The ~1,150-gene estimate is model-dependent (relies on de novo LoF multi-hit/single-hit balance) and individual-gene effect sizes are mostly modest and undetermined.
- Developmental/spatial convergence rests on **bulk mid-fetal neocortex coexpression** (DAWN), not single-cell or organoid functional data — cell-type and temporal resolution are coarse.
- 2014-era ancestry was predominantly European; X-linked and non-coding contributions not addressed; CNV analysis limited to deletions in the candidate set.
