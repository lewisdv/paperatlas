---
title: "Inferring and perturbing cell fate regulomes in human brain organoids."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1038/s41586-022-05279-8
pmid: 36198796
authors: Fleck JS et al.
journal: Nature (2023)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/fleck_2023_inferring_perturbing_cell_fate_regulomes_human_brain.pdf
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# Inferring and perturbing cell fate regulomes in human brain organoids.

## Source

- Authors: Fleck JS, Jansen SMJ, Wollny D, Zenk F, Seimiya M, Jain A, Okamoto R, Santel M et al. (corresponding: Zhisong He, J. Gray Camp, Barbara Treutlein)
- Journal: Nature (2023), Vol 621:365-372 (published online 5 Oct 2022; print 14 Sep 2023). Open access (CC BY 4.0).
- DOI: [10.1038/s41586-022-05279-8](https://doi.org/10.1038/s41586-022-05279-8)
- PMID: [36198796](https://pubmed.ncbi.nlm.nih.gov/36198796/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Self-organizing neural organoids grown from pluripotent stem cells1-3 combined with single-cell genomic technologies provide opportunities to examine gene regulatory networks underlying human brain development. Here we acquire single-cell transcriptome and accessible chromatin data over a dense time course in human organoids covering neuroepithelial formation, patterning, brain regionalization and neurogenesis, and identify temporally dynamic and brain-region-specific regulatory regions. We developed Pando-a flexible framework that incorporates multi-omic data and predictions of transcription-factor-binding sites to infer a global gene regulatory network describing organoid development. We use pooled genetic perturbation with single-cell transcriptome readout to assess transcription factor requirement for cell fate and state regulation in organoids. We find that certain factors regulate the abundance of cell fates, whereas other factors affect neuronal cell states after differentiation. We show that the transcription factor GLI3 is required for cortical fate establishment in humans, recapitulating previous research performed in mammalian model systems. We measure transcriptome and chromatin accessibility in normal or GLI3-perturbed cells and identify two distinct GLI3 regulomes that are central to telencephalic fate decisions: one regulating dorsoventral patterning with HES4/5 as direct GLI3 targets, and one controlling ganglionic eminence diversification later in development. Together, we provide a framework for how human model systems and single-cell technologies can be leveraged to reconstruct human developmental biology.

## Key findings

### Multi-omic developmental atlas
- Paired scRNA-seq + scATAC-seq over **11 time points** (days 4, 7, 9, 11, 12, 16, 18, 21, 26, 31, 61) spanning ~2 months of **unguided whole-brain organoid** development, from **3 iPS cell lines + 1 ES cell line** (H9, 409B2, Wibj2, Hoik1), demultiplexed by SNPs and integrated by CCA into "multi-omic metacells."
- Recovers a continuous trajectory: pluripotency (POU5F1) -> NPC (PAX6, VIM) -> dorsal telencephalon (EMX1, NEUROD6), ventral telencephalon (DLX5, ISL1, GAD1), non-telencephalon (TCF7L2, LHX9), plus a minor mesenchymal population (DCN, COL5A1).
- A separate multiome dataset across **9 lines** (iPS: 409B2, B7, HOIK1, KUCG2, WIBJ2, WTC; ES: H1, H9, HES3) at ~3 weeks shows that patterning-center marker **expression is consistent across lines, but cluster proportions vary substantially** — i.e., the GRN is preserved while self-patterning propensity differs between lines/batches.
- Branch inference (RNA velocity + CellRank) reveals an early anterior-telencephalon vs posterior-non-telencephalon bifurcation, then dorsal-excitatory vs ventral-inhibitory branching; the pre-bifurcation telencephalic progenitor state is marked by DCT, DIO3, SIX6.

### Pando — GRN inference framework
- **Pando** (released as an R package) infers a global gene regulatory network by combining: accessible peaks intersected with **conserved elements + known CRE annotations** to pick candidate regions, **TF-binding-site prediction** per region, and a **regression model** (offers GLM, regularized GLM, XGBoost, Bayesian regression) linking target-gene expression to TF expression x binding-site accessibility.
- Validation: **94% of accessible peaks overlapping H3K27ac (CUT&Tag) fell within Pando's candidate regions**, indicating strong enrichment for active regulatory regions.
- Output = per-TF positive/negative gene modules and regulatory-region modules; UMAP of the TF network recapitulates the pseudotemporal order (pluripotency TFs POU5F1/LIN28A -> neuroepithelial SOX2/HES1 -> regional NPC/neuron TFs), and the GRN can be partitioned into branch-specific subnetworks (e.g., NEUROD2/NFIA/SOX6 dorsal-specific; TFs that switch between activating and repressing across branches, e.g., HEY1, JUND, SOX2).

### Pooled CRISPR perturbation (CROP-seq) in mosaic organoids
- Lentiviral library targeting **20 TFs x 3 gRNAs each**, chosen to be expressed in cortical development but **silent in iPSCs/neuroectoderm** (to avoid disrupting early development). Delivered into an inducible-Cas9 (iCas9) iPSC line; mosaic organoids analyzed at **day 60**.
- **22,449 cells with an assigned gRNA** recovered (avg ~1 gRNA/cell). Effects sorted into two classes:
  - **Fate-abundance effects** — gRNAs for **8 TFs** consistently enriched cells in the ventral telencephalon with depletion elsewhere/cortex (e.g., **GLI3, TBR1**); an opposing set enriched in cortex / depleted ventrally (e.g., **HES1, HOPX**). GLI3 and HES1 act at the dorsoventral branchpoint with **antagonistic** effects on cortical commitment.
  - **Cell-state effects** — some perturbations changed the transcriptome without changing composition; notably **E2F2** (cell-cycle regulator) altered both dorsal and ventral neuronal transcriptomes, implicating cell-cycle-exit timing in neuronal state.

### GLI3 is required for human cortical fate (validation)
- Two independent **GLI3-knockout iPSC lines** + an edited WT control. scRNA-seq of KO vs WT organoids at **day 45**: KO cells are **depleted from dorsal telencephalon and enriched in ventral telencephalon**, with **MEIS2** (LGE/CGE marker) strongly downregulated and KO cells enriched in MGE-like neurons — confirming GLI3 promotes cortical fate and represses MGE program, consistent with mouse but now shown in human.

### Two distinct GLI3 regulomes (single-cell multiome + CUT&Tag)
- WT vs GLI3-KO **multiome at 3 weeks** (pre-dorsoventral patterning) and **6 weeks**: strong differential expression/accessibility concentrated in telencephalic progenitors.
- **Regulome 1 (early telencephalic progenitors, dorsoventral patterning):** GLI3 directly activates **HES4, HES5, PAX6, OTX2, CREB5**; **HES4 and HES5 are direct GLI3 targets** (confirmed by GLI3 CUT&Tag binding at HES4/HES5 plus matched differential accessibility); ~**76% of DEGs are indirect** GLI3 targets. NOTCH targets are not generally enriched, suggesting **NOTCH-independent** regulation of HES genes. HES1 is up, HES4/5 and EMX2 down in KO; SOX4/SOX11 (down in HES1-perturbed cells) go up in GLI3-KO — reinforcing GLI3/HES1 antagonism.
- **Regulome 2 (ventral telencephalon, ganglionic-eminence diversification, later):** GLI3 directly regulates **PAX6, LHX8, ID1, BCL11A**; dysregulation of PTCH1, NKX2-1, EMX2, GSX2, ID1. Some CREs (NKX2-1, ID1) become differentially accessible already in progenitors though the genes change expression only later — a possible **priming** effect.
- Module branch-activation scoring nominates **HES5, EMX2, PAX6** as drivers of dorsal fate and **FOXG1, DMRTA1** for ventral fate.
- **SHH link:** 3-day SHH treatment at the neuroepithelial stage downregulates GLI3 and produces DEGs **highly correlated with GLI3-KO DEGs (Pearson r = 0.5)**; shared/GLI3-specific DEGs are regionalization/differentiation genes, SHH-specific DEGs are lipid-metabolism. Interpretation: **SHH ventralizes mainly by preventing GLI3-driven dorsalization.**

## Methods

- **Stem cells / organoids:** 6 iPSC lines + 3 ESC lines; cultured in mTeSR1 on Matrigel. Whole-brain (unguided) organoid protocol (Lancaster-style): **4,500-5,000 cells** seeded per organoid in ultralow-attachment plates. Human ESC use approved by the ethics committee of northwest/central Switzerland (2019-01016).
- **Single-cell genomics:** 10x Genomics scRNA-seq (3' v3), scATAC v1, and Multiome ATAC+GEX (multiome from day 15 and day 19 organoids); pooled lines demultiplexed by SNPs; sequenced on Illumina NovaSeq. Integration via CCA, metacells via min-cost/max-flow bipartite matching, cross-sample integration via cluster similarity spectrum (CSS), visualization by UMAP.
- **Regulatory annotation:** H3K27ac and GLI3 CUT&Tag; GLI3-binding score = summed CUT&Tag intensity over gene body + 2 kb. Trajectories via RNA velocity + CellRank.
- **Perturbation:** doxycycline-inducible Cas9 (and a Cas9-nickase) line built in 409B2 via AAVS1 TALEN knock-in (M2rtTA + Puro-Cas9; D10A for nickase). CROP-seq protocol with eGFP swapped for the Puro marker; low-MOI transduction (<30% GFP+ to favor 1 vector/cell), FACS enrichment; mosaic organoids dissociated at 2 months, ~7,000 cells/lane; gRNA amplified from cDNA. (Note a karyotype caveat below.)
- **GLI3 loss-of-function:** two clonal GLI3-KO iPSC lines + edited WT control via CRISPR-Cas9 nickase; GLI3 protein confirmed absent by IHC; scRNA-seq at day 45 and WT/KO multiome at weeks 3 and 6; SHH treatment (3 days) at week 3 followed by multiome.
- **Computation:** Pando R package (candidate-region selection, motif matching, model fitting, module discovery). Composition effects tested with log-odds + Cochran-Mantel-Haenszel; significance generally reported at FDR < 0.01 (composition) and FDR < 1e-4 (CROP-seq DE).

## Relevance to the brain-organoid ASD review

- **Core "regulome inference + perturbation platform" citation.** Establishes the two-part toolkit the review's thesis depends on: (1) **Pando** to reconstruct a genome-scale, multi-omic GRN of human brain development, and (2) **pooled CRISPR (CROP-seq) in mosaic organoids** to test, at single-cell resolution, which TFs control cell-fate abundance vs cell state.
- Provides the conceptual distinction the review can borrow: perturbations split into **fate-abundance regulators vs cell-state regulators** — a useful framing for interpreting ASD-gene perturbation screens (e.g., Li 2023 CHOOSE, Meng 2023 assembloid screens in this corpus).
- The **GLI3 case study** is the worked example of "infer -> perturb -> validate -> resolve mechanism": a developmental TF whose human requirement for cortical fate is confirmed in organoids and dissected into stage-specific direct/indirect regulomes (HES4/5 direct targets; SHH-GLI3 axis). GLI3/SHH and HES signaling are relevant to dorsoventral balance and interneuron (GE-derived) production, a recurring ASD-relevant axis (cf. excitatory/inhibitory imbalance themes).
- Demonstrates that **multiregion unguided organoids are predictive of in vivo developmental programs**, supporting their use as an ASD-genetics discovery substrate, while also quantifying the **line-to-line variability in regional proportions** the review must account for.

## Open questions / limitations

- **GRN inference assumptions:** Pando links regions to genes largely by proximity and depends on TF-motif databases; the authors note missing comprehensive histone-modification and chromatin-conformation data and incomplete motif references. Edges are correlative predictions, validated for GLI3 but not genome-wide.
- **Unguided protocol variability:** strong between-line/batch variation in regional proportions; results aggregate across organoids and may obscure organoid-level heterogeneity.
- **Perturbation coverage:** only 20 TFs screened; chosen to be silent early, so effects on the earliest neuroepithelial decisions are not assayed. CROP-seq read out at a single time point (day 60).
- **Cell-line caveat:** the iCRISPR-Cas9 nuclease line acquired a common stem-cell abnormality over time (55% of cells carried a derivative chromosome 2 with chr1q11q44 attached) — a genomic-instability caveat for the mosaic-perturbation data.
- **Functional readout absent:** the paper measures transcriptome/chromatin/fate, not neuronal activity or circuit function — complementary to the functional-maturity work (Quadrato 2017) rather than overlapping it.
- GLI3 regulome model is built largely in one engineered background; generalization across genetic backgrounds and to bona fide human fetal tissue is inferred, not directly shown here.

## Related

- [Single-cell brain-organoid CRISPR screening identifies developmental defects (Li 2023)](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md) — the in-organoid pooled CRISPR (CHOOSE) screen of ASD genes; closest methodological sibling to Fleck's CROP-seq.
- [Assembloid CRISPR screens reveal impact of disease genes (Meng 2023)](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md) — complementary 3D pooled-perturbation screen (interneuron generation/migration).
- [Organoid single-cell genomic atlas (Kanton 2019)](kanton_2019_organoid_single-cell_genomic_atlas.md) — developmental single-cell atlas from the same Treutlein/Camp lineage that this multi-omic time course builds on.
- [An integrated transcriptomic cell atlas (He 2024)](he_2024_an_integrated_transcriptomic_cell_atlas.md) — cross-protocol atlas relevant to benchmarking organoid cell states.
- [Cerebral organoids model human brain development and microcephaly (Lancaster 2013)](lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.md) — the unguided whole-brain protocol used here.
- Concept: [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- Entity: [CRISPR-Cas9 and next-generation CRISPR editing](../entities/crispr-cas9-and-next-generation-crispr-editing.md)
- Entity: [Single-cell atlas benchmarking](../entities/single-cell-atlas-benchmarking.md)
