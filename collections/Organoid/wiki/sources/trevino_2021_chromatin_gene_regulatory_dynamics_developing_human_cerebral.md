---
title: "Chromatin and gene-regulatory dynamics of the developing human cerebral cortex at single-cell resolution."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1016/j.cell.2021.07.039
pmid: 34390642
authors: Trevino AE et al.
journal: Cell (2021)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# Chromatin and gene-regulatory dynamics of the developing human cerebral cortex at single-cell resolution.

## Source

- Authors: Trevino AE, Müller F, Andersen J, Sundaram L, Kathiria A, Shcherbina A, Farh K, Chang HY, Pașca AM, Kundaje A, Pașca SP, Greenleaf WJ (Stanford; Saarland; Illumina AI Lab)
- Journal: Cell 184, 5053–5069 (September 16, 2021)
- DOI: [10.1016/j.cell.2021.07.039](https://doi.org/10.1016/j.cell.2021.07.039)
- PMID: [34390642](https://pubmed.ncbi.nlm.nih.gov/34390642/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Genetic perturbations of cortical development can lead to neurodevelopmental disease, including autism spectrum disorder (ASD). To identify genomic regions crucial to corticogenesis, we mapped the activity of gene-regulatory elements generating a single-cell atlas of gene expression and chromatin accessibility both independently and jointly. This revealed waves of gene regulation by key transcription factors (TFs) across a nearly continuous differentiation trajectory, distinguished the expression programs of glial lineages, and identified lineage-determining TFs that exhibited strong correlation between linked gene-regulatory elements and expression levels. These highly connected genes adopted an active chromatin state in early differentiating cells, consistent with lineage commitment. Base-pair-resolution neural network models identified strong cell-type-specific enrichment of noncoding mutations predicted to be disruptive in a cohort of ASD individuals and identified frequently disrupted TF binding sites. This approach illustrates how cell-type-specific mapping can provide insights into the programs governing human development and disease.

> Note: this is a study of **primary human fetal cortex** (mid-gestation), not of brain organoids. Its value for the organoid-ASD review is as a *ground-truth regulome / variant-to-cell-type reference* against which organoid fidelity and variant interpretation can be benchmarked.

## Key findings

- **Atlas scale.** Paired single-cell atlas from 4 primary samples at post-conceptional week (PCW) 16, 20, 21, 24: after QC, **57,868 single-cell transcriptomes** (scRNA-seq) and **31,304 single-cell epigenomes** (scATAC-seq). scATAC consensus set = **657,930 accessible peaks** (candidate cis-regulatory elements, CREs).
- **CRE–gene linkages.** Correlation-based linking of distal CRE accessibility to expression yielded **64,878 CRE–gene pairs** (median **5 CREs per gene**). Linked CREs were more evolutionarily conserved than unlinked elements (Wilcoxon rank-sum p < 2.2×10⁻¹⁶) and were enriched for support by cell-type-specific 3D promoter contacts.
- **Genes with predictive chromatin (GPCs).** Defined **185 GPCs** = top decile of gene-activity/expression correlation AND >10 linked CREs (e.g., SOX2, HES1). Strongly enriched for transcription-regulator / DNA-binding TF activity. Conceptually akin to "super-enhancers" / "super-interactive promoters."
- **Multiome validation.** Same-cell scATAC+scRNA on PCW21 cortex → **8,981 high-quality cells**. **40,181 of the in silico CRE–gene linkages (53%)** were recovered from this single joint timepoint, plus 23,849 new ones — confirming most inferred linkages.
- **Neuronal differentiation is a continuum.** RNA-velocity pseudotime over the glutamatergic-neuron (GluN) lineage gave **13,989 dynamic CRE–gene interactions** (5 k-means clusters). Early interactions → cell division/neural-precursor proliferation; late → morphogenesis, migration, maturation; **ASD-susceptibility genes were preferentially linked late in pseudotime**, TFs/DNA-binding genes intermediate.
- **Sequential TF motif waves.** 31 dynamic TFs paired to 24 disambiguated motif clusters. Order: early PAX6, SOX2/6/9, GLI3, ASCL1 → intermediate EOMES, NFIA, NFIB, NEUROD1 → late NEUROD2, BHLHE22, MEF2C. Motif coordination/synergy is higher early; late TFs act more independently. Differences across pseudotime exceeded differences across gestational stage.
- **Glial lineages.** Identified a multipotent glial progenitor (mGPC) co-expressing astroglial (GFAP, HOPX, EGFR, ASCL1) and oligodendrocyte-precursor (OLIG2, PDGFRA) markers; IHC confirmed ASCL1/OLIG2/EGFR and PDGFRA/SPARCL1 colocalization. Two astrocyte-precursor populations distinguished by chromatin: **A1-HES** (HES4, CAV2) vs **A2-OLIG** (SPARCL1, ID3, IGFBP7), separable by OLIG1- vs SOX21-motif accessibility.
- **GPCs prime cycling progenitors toward fate.** GPC-associated chromatin in cycling cells already carried signatures of more differentiated states; reprojecting cycling-cell branches using *only* GPC chromatin moved them forward in pseudotime toward distinct mature endpoints (random gene sets did not). Proposes enhancers act as a "ratchet" stabilizing lineage-determining TF expression.
- **Deep learning prioritizes noncoding ASD de novo mutations (central ASD result).**
  - Naive peak overlap gave **no** case/control enrichment (e.g., GluN6 OR = 1.02, Fisher p = 1.0) — peak-level annotation is insufficient.
  - Trained cell-type-specific **BPNet/ChromBPNet** convolutional models predicting base-resolution Tn5 coverage from sequence (GluN6 mean Spearman ρ = 0.58 on held-out chromosomes, 5-fold CV).
  - Scored **>200,000 de novo mutations from 1,902 Simons Simplex Collection families** by allelic fold-change ("local disruption score").
  - High-effect-size mutations enriched in ASD cases vs unaffected siblings for **GluN2/3/4/6/9 (>1.2-fold)**, plus IN2/3/4, nIPC, and radial glia. **Early radial glia = strongest enrichment: OR = 1.909, excess of ~20 mutations, Fisher p = 0.004.**
  - Specificity controls: BPNet trained on **fetal heart** enhancers gave no enrichment (OR = 1.01, p = 1.0); naive heart-enhancer overlap OR = 0.97, p = 1.0.
  - **1.4-fold** enrichment for case mutations whose nearest gene is in **SFARI** (24 case vs 17 control; OR = 1.24, p = 0.154 — not individually significant).
  - Most frequently disrupted motifs in cases vs controls: **CTCF** (loop boundaries), **NRF1** (regulates GABA receptor subunit GABRB1), E-box/bHLH (ASCL1, NEUROD6), homeobox (PAX5). Worked examples: a disruptive intronic mutation at **NFIA** (disrupts NFIA motif in a linked enhancer) and an intergenic mutation ~90 kb from **NPY** TSS predicted to break a CTCF loop anchor.

## Methods

- **Platform:** 10x Genomics Chromium scATAC-seq and scRNA-seq from 4 primary human fetal cortical samples (PCW16/20/21/24); separate **multiome** (joint ATAC+RNA same-cell) run on PCW21 cortex.
- **scATAC processing:** iterative LSI embedding/clustering (ArchR-style), gene-activity scores from aggregate local accessibility (Cicero-style), TF motif activity via chromVAR.
- **Integration:** canonical correlation analysis (CCA, Seurat) to match scRNA and scATAC cells; pseudo-bulk aggregation for CRE–gene correlation linking.
- **Trajectory:** RNA-velocity-derived diffusion pseudotime (scVelo); pseudotime transferred to nearest ATAC neighbors; adult cortical neurons (Hodge et al. 2019) projected to validate layer ordering.
- **Glial modules:** fuzzy c-means co-expression clustering (genes shared across modules) + reprojection embedding.
- **Motif disambiguation:** Vierstra et al. (2020) clustered motif archetypes to reduce sequence-similarity bias.
- **Deep learning:** BPNet/ChromBPNet CNNs predict base-resolution pseudo-bulk accessibility per scATAC cluster from DNA sequence; GC- and motif-density-matched backgrounds; variant effect = allelic fold-change in predicted counts; case vs control enrichment of high-effect mutations via Fisher's exact test.
- **Disease cohort:** Simons Simplex Collection (An et al. 2018) — >200,000 noncoding de novo mutations across 1,902 families (ASD probands vs unaffected siblings).
- **Validation:** IHC on PCW17/21 cortex for marker colocalization; cross-projection of independent fetal (Bhaduri 2020; Polioudakis 2019) and adult (Hodge 2019) scRNA-seq datasets.

## Relevance to the brain-organoid ASD review

This paper is the collection's **primary-tissue regulome and variant-interpretation reference** — the role flagged in the manuscript brief ("GRN/regulome reference for fidelity & variant-to-cell-type mapping").

- **Fidelity benchmark.** The 657,930-peak / 64,878-linkage primary-cortex atlas, the GPC set, and the ordered TF-motif waves (PAX6/SOX2→EOMES/NFI→NEUROD2/MEF2C) give a quantitative ground truth against which organoid GRNs (e.g., Fleck 2023 organoid regulome) and organoid corticogenesis fidelity (Cheroni 2022 benchmarking; Camp 2015; Amiri 2018) can be judged.
- **Variant-to-cell-type mapping.** The BPNet pipeline operationalizes "which cell type and developmental window does a noncoding ASD variant act in" — early radial glia and glutamatergic-neuron classes carry the strongest signal. This is exactly the proactive-genetics logic the manuscript proposes to run inside programmable organoids: map a variant to a cell type, then build/perturb that cell type in vitro.
- **Cross-link to Table-1 disease genes.** Frequently disrupted motifs include NRF1 (→ GABA receptor GABRB1) and worked examples at NFIA and NPY — connecting noncoding regulatory disruption to the same E/I-balance and interneuron themes that the Birey (CACNA1C/Timothy) and Villa (CHD8) Table-1 entries explore at the cellular level.
- **Why organoids, framed by primary data.** ASD-susceptibility genes link late in the GluN pseudotime and de novo mutation signal concentrates in radial glia / neuronal classes present in mid-gestation — developmental windows that human organoids can access experimentally but primary fetal tissue cannot perturb.

## Open questions / limitations

- Data span only **8 weeks of mid-gestation** (PCW16–24); earlier neurogenesis and later gliogenesis/maturation (and the link from astrocyte precursors to adult subtypes) are not captured.
- Most lineage relationships and singleome ATAC↔RNA matches rest on **data-integration inference** (CCA, pseudotime transfer), not measured same-cell data or lineage tracing; multiome validates many but not all inferences.
- Cell-type-specific BPNet models only score variant effects on peaks present in that cell type — trading statistical power (fewer overlapping mutations) for cell-type resolution.
- Prioritized noncoding de novo mutations are **computational predictions**; case-vs-control conservation and TSS distance were indistinguishable, and **molecular validation in the cognate cell types has not been done**.
- The SFARI-nearest-gene enrichment (OR = 1.24) is suggestive but not individually significant; motif-disruption "excess" bar plots are descriptive, not statistical tests.

## Related

- [Fleck 2023 — inferring and perturbing cell-fate regulomes in human brain organoids](fleck_2023_inferring_perturbing_cell_fate_regulomes_human_brain.md) — the organoid-side regulome counterpart; Trevino provides the primary-tissue GRN this can be benchmarked against.
- [Cheroni 2022 — benchmarking brain-organoid recapitulation of fetal corticogenesis](cheroni_2022_benchmarking_brain_organoid_recapitulation_fetal_corticogenesis.md) — fidelity framework that uses primary fetal references like this one.
- [Amiri 2018 — transcriptome & epigenome landscape of human cortical development modeled in organoids](amiri_2018_transcriptome_epigenome_landscape_human_cortical_development_modeled.md) — organoid chromatin/expression atlas; direct comparator.
- [Camp 2015 — human cerebral organoids recapitulate gene-expression programs](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md) — organoid-vs-fetal concordance baseline.
- [Pollen 2015 — molecular identity of human outer radial glia](pollen_2015_molecular_identity_human_outer_radial_glia_during.md) — radial-glia biology relevant to the strongest BPNet enrichment class.
- [Birey 2022 — molecular basis of human interneuron migration (Timothy syndrome)](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md) and [Villa 2022 — CHD8 haploinsufficiency](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md) — Table-1 ASD-gene organoid models; cellular complements to this regulatory atlas.
