---
title: "Autism-specific PTEN p.Ile135Leu variant and an autism genetic background combine to dysregulate cortical neurogenesis."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.ajhg.2023.03.015
pmid: 37098352
authors: Fu S et al.
journal: American journal of human genetics (2023)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Autism-specific PTEN p.Ile135Leu variant and an autism genetic background combine to dysregulate cortical neurogenesis.

## Source

- Authors: Fu S, Bury LAD, Eum J, Wynshaw-Boris A (Case Western Reserve University)
- Journal: The American Journal of Human Genetics (2023); 110(5):826–845
- DOI: [10.1016/j.ajhg.2023.03.015](https://doi.org/10.1016/j.ajhg.2023.03.015)
- PMID: [37098352](https://pubmed.ncbi.nlm.nih.gov/37098352/)
- Added via: manuscript_brain_organoid_v6 reference ingest
- Data: GEO GSE214323, GSE214422, GSE221882, GSE221923

## Abstract

Alterations in cortical neurogenesis are implicated in neurodevelopmental disorders including autism spectrum disorders (ASDs). The contribution of genetic backgrounds, in addition to ASD risk genes, on cortical neurogenesis remains understudied. Here, using isogenic induced pluripotent stem cell (iPSC)-derived neural progenitor cells (NPCs) and cortical organoid models, we report that a heterozygous PTEN c.403A>C (p.Ile135Leu) variant found in an ASD-affected individual with macrocephaly dysregulates cortical neurogenesis in an ASD-genetic-background-dependent fashion. Transcriptome analysis at both bulk and single-cell level revealed that the PTEN c.403A>C variant and ASD genetic background affected genes involved in neurogenesis, neural development, and synapse signaling. We also found that this PTEN p.Ile135Leu variant led to overproduction of NPC subtypes as well as neuronal subtypes including both deep and upper layer neurons in its ASD background, but not when introduced into a control genetic background. These findings provide experimental evidence that both the PTEN p.Ile135Leu variant and ASD genetic background contribute to cellular features consistent with ASD associated with macrocephaly.

## Key findings

- **The variant**: heterozygous PTEN c.403A>C [p.Ile135Leu] (GenBank NM_000314.8), identified by WES in 1 of 8 ASD individuals with early brain overgrowth (vs 5 matched controls) in the authors' prior work. Clinical framing: ~20% of ASD individuals show early brain overgrowth; ~15% of those carry PTEN variants. Most ASD-associated PTEN variants (unlike cancer variants) do not substantially disrupt lipid-phosphatase function.
- **Bidirectional isogenic design**: CRISPR-Cas9 used to create, in two backgrounds, three PTEN genotypes — WT/WT, WT/Ile135Leu, KO/KO. Primary ASD line "Apex" (carries the variant) and control line "Chap". The variant was both **installed** into controls and **corrected** in the ASD line. Replication backgrounds: second control "Clay" (variant installed); second ASD line "Arch" carrying a CTNNB1 c.226C>T [p.Gln76*] stop-gain, **corrected** by CRISPR.
- **NPC proliferation (2D)**: PTEN WT/Ile135Leu significantly decreased population doubling time (= faster proliferation) in BOTH backgrounds, comparable to PTEN KO/KO (point mutation suffices vs full knockout). Independently, ASD-background WT/WT (Apex) proliferated faster than control WT/WT (Chap) — background alone drives proliferation.
- **Biochemistry is background-dependent** (key surprise): in the ASD (Apex) background, WT/Ile135Leu mildly increased p-AKT-Thr308/Ser473 (partial loss of canonical PTEN activity); in the control (Chap) background the same variant had NO effect on p-AKT. So the variant impairs PTEN activity only on the ASD background.
- **Organoid size**: WT/Ile135Leu organoids were enlarged at week 4 in both backgrounds; by week 8, enlargement continued in the control background but was NOT sustained in the ASD background. ASD-background organoids were always larger than control regardless of PTEN genotype. Size enlargement replicated with the variant in second control line Clay (supports pathogenicity).
- **Cell-type overproduction is ASD-background-specific** (Table-1 phenotype): IHC showed increased IPCs (TBR2+, weeks 4 & 10) and oRGs (HOPX+, week 10), and overproduction of deep-layer (CTIP2+, TBR1+) and upper-layer (SATB2+) neurons — only in Apex WT/Ile135Leu vs Apex WT/WT (ASD background), NOT in Chap control background.
- **scRNA-seq**: 95,227 cells, 12 samples (week 10 & 21; 3 organoids pooled per genotype/timepoint), integrated with the Nowakowski/UCSC fetal cortex dataset. Recovered IPC, oRG, vRG, tRG, cycling progenitors, deep- and upper-layer excitatory neurons, interneurons (plus some non-brain "unknown" clusters from mis-differentiation).
- **Directionality flips with background** (recurring theme): GSEA neurogenesis/neuron-development GO terms were **downregulated** by the variant in the control background but **upregulated** in the ASD background; ASD background effects likewise reversed direction depending on PTEN genotype. PTEN KO/KO showed non-uniform/asynchronous effects. Variant also dysregulated gliogenesis ("glia cell differentiation", "regulation of gliogenesis").
- **Accelerated upper-layer maturation (ASD-specific)**: Monocle3 pseudotime — WT/Ile135Leu accelerated upper-layer neuron maturation only in the ASD background (and decelerated it in the control background at week 21). Deep-layer neuron maturation unaffected in both. Mechanism for overproduction = accelerated maturation + increased IPC/oRG proliferation.
- **Convergent PI3K/AKT modifier model**: ASD risk genes in the PI3K/AKT pathway (MET, FGF14, NTRK1, NTRK2, ITGB3, LAMB1, RELN, PRKCA) were dysregulated in the ASD line; correcting the PTEN variant rescued several (NTRK1, NTRK2, MET, ITGB3). The independent ASD background Arch (CTNNB1-corrected) showed 1,131 downregulated genes vs Chap and dysregulated similar PI3K/AKT ASD-risk genes — two ASD backgrounds converge on PI3K/AKT. Supports oligogenic inheritance: background variants act as modifiers of a key risk gene (PTEN).
- **Synaptic signaling**: WT/Ile135Leu downregulated synaptic-function GO terms (synaptic signaling, action-potential genes) in deep- and upper-layer neurons on the control background, but UPregulated them on the ASD background — again background-dependent direction.
- **Clinical parallel**: neuron overproduction echoes postmortem findings of 67% more prefrontal-cortex neurons in ASD individuals with brain overgrowth vs controls (Courchesne et al.).

## Methods

- **iPSC panels**: isogenic CRISPR-Cas9 editing for PTEN WT/WT, WT/Ile135Leu, KO/KO in Apex (ASD) and Chap (control); variant installed in Clay (control); CTNNB1 p.Gln76* corrected in Arch (ASD).
- **2D NPCs**: dorsal forebrain NPCs (PAX6+, FOXG1+); population-doubling-time proliferation assays (3 replicates, multiple passages); immunoblot for PTEN, p-AKT-Thr308/Ser473.
- **Bulk RNA-seq**: 54 NPC samples (3 replicates × 6 genotypes × 3 passages, ~30M paired-end reads/sample); GSEA + GO (ClusterProfiler 4.5.1, comparecluster).
- **Cortical organoids**: dual-SMAD + WNT inhibition protocol, cultured to week 21; bright-field size quantification (pixel-based) at day 14/18, week 4/8; IHC for TBR2, HOPX, CTIP2, TBR1, SATB2.
- **scRNA-seq**: 10X platform, week 10 & 21, Seurat (SCT, FindClusters res 1.5), integration with UCSC cortex-dev fetal reference, Monocle3 v1.2.9 pseudotime, GSEA per cell type.

## Relevance to the brain-organoid ASD review

- **The Table-1 PTEN entry and the cleanest demonstration of genetic-background dependence.** This is the load-bearing source for the claim that an ASD-associated PTEN missense variant produces ASD-relevant cellular phenotypes (NPC/IPC/oRG overproduction, deep- and upper-layer neuron overproduction, accelerated upper-layer maturation, brain/organoid overgrowth) **only on the ASD genetic background** — installing the same variant in control backgrounds does not reproduce them.
- **Directly motivates a "programmable" / proactive ASD-genetics strategy**: because the same risk variant flips direction and magnitude across backgrounds (even biochemically — p-AKT changes only on the ASD background), studying ASD risk genes in isolated control backgrounds can miss or invert the phenotype. Patient-derived (background-preserving) and isogenically engineered panels are both needed.
- **Convergence on PI3K/AKT** across two unrelated ASD backgrounds (PTEN-variant Apex and CTNNB1-corrected Arch) supports an oligogenic modifier model and a tractable convergent pathway for proactive screening/intervention.
- **Connects fidelity to disease readout**: the organoid recovers the correct progenitor (IPC/oRG) and neuronal (deep/upper-layer) classes whose dysregulation it then measures — consistent with the cell-class-identity validation of [Uzquiano 2022](uzquiano_2022_proper_acquisition_cell_class_identity_organoids_allows.md). The 67% postmortem neuron-overproduction parallel ties the organoid phenotype to human ASD-with-macrocephaly pathology.
- Complements [Paulsen 2022](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) (asynchronous neurogenesis convergence across ASD genes on multiple control backgrounds) and the broader PTEN/PI3K organoid literature ([Kang 2024](kang_2024_germline_pten_genotype_dependent_phenotypic_divergence_during.md), [Blair 2018 TSC/mTOR](blair_2018_genetically_engineered_human_cortical_spheroid_models_tuberous.md)).

## Open questions / limitations

- Small line numbers: 2 control + 2 ASD backgrounds; conclusions about "ASD genetic background" generality rest on few donors.
- Mechanism of background-dependent PTEN biochemistry is correlative — the specific modifier variants/epigenetic features that gate p-AKT response are inferred (PI3K/AKT ASD-risk genes), not causally dissected.
- The two ASD backgrounds carry different primary lesions (PTEN variant retained vs CTNNB1 corrected), complicating a clean "background-only" comparison.
- Direction-of-effect reversals (neurogenesis, synaptic GO terms up vs down by background) are striking but not mechanistically resolved.
- "Unknown"/non-brain clusters indicate residual mis-differentiation; maturation limited to ≤ week 21.
- Whether the neurogenesis→gliogenesis switch timing is altered is raised as future work (EGFR+ gliogenesis onset ~GW20 falls within the modeled window).

## Related

- [Uzquiano 2022 — proper acquisition of cell-class identity in organoids](uzquiano_2022_proper_acquisition_cell_class_identity_organoids_allows.md) (fidelity benchmark for the cell classes scored here)
- [Paulsen 2022 — ASD genes converge on asynchronous neuron development](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) (background/asynchrony, complementary design)
- [Kang 2024 — germline PTEN genotype-dependent phenotypic divergence](kang_2024_germline_pten_genotype_dependent_phenotypic_divergence_during.md)
- [Blair 2018 — engineered cortical spheroids, tuberous sclerosis (mTOR pathway)](blair_2018_genetically_engineered_human_cortical_spheroid_models_tuberous.md)
- [Schafer 2023 — neuroimmune organoid model of ASD with macrocephaly](schafer_2023_vivo_neuroimmune_organoid_model_study_human_microglia.md) (same disease subtype, neuroimmune axis)
