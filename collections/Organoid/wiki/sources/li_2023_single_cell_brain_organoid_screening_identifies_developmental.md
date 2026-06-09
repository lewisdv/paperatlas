---
title: "Single-cell brain organoid screening identifies developmental defects in autism."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41586-023-06473-y
pmid: 37704762
authors: Li C et al.
journal: Nature (2023)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/li_2023_single_cell_brain_organoid_screening_identifies_developmental.pdf
pdf_status: downloaded
---

# Single-cell brain organoid screening identifies developmental defects in autism.

## Source

- Authors: Li C, Fleck JS, Martins-Costa C, Burkard TR, Themann J, Stuempflen M, Peer AM, Vertesy Á et al. (Treutlein & Knoblich labs, IMBA / ETH Zürich)
- Journal: Nature (2023)
- DOI: [10.1038/s41586-023-06473-y](https://doi.org/10.1038/s41586-023-06473-y)
- PMID: [37704762](https://pubmed.ncbi.nlm.nih.gov/37704762/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

The development of the human brain involves unique processes (not observed in many other species) that can contribute to neurodevelopmental disorders1-4. Cerebral organoids enable the study of neurodevelopmental disorders in a human context. We have developed the CRISPR-human organoids-single-cell RNA sequencing (CHOOSE) system, which uses verified pairs of guide RNAs, inducible CRISPR-Cas9-based genetic disruption and single-cell transcriptomics for pooled loss-of-function screening in mosaic organoids. Here we show that perturbation of 36 high-risk autism spectrum disorder genes related to transcriptional regulation uncovers their effects on cell fate determination. We find that dorsal intermediate progenitors, ventral progenitors and upper-layer excitatory neurons are among the most vulnerable cell types. We construct a developmental gene regulatory network of cerebral organoids from single-cell transcriptomes and chromatin modalities and identify autism spectrum disorder-associated and perturbation-enriched regulatory modules. Perturbing members of the BRG1/BRM-associated factor (BAF) chromatin remodelling complex leads to enrichment of ventral telencephalon progenitors. Specifically, mutating the BAF subunit ARID1B affects the fate transition of progenitors to oligodendrocyte and interneuron precursor cells, a phenotype that we confirmed in patient-specific induced pluripotent stem cell-derived organoids. Our study paves the way for high-throughput phenotypic characterization of disease susceptibility genes in organoid models with cell state, molecular pathway and gene regulatory network readouts.

## Key findings

**Headline.** This is **THE in-organoid pooled CRISPR screen** for the review — the first system to run a **multiplexed, single-cell-resolved loss-of-function screen *inside* mosaic human cerebral organoids**. The **CHOOSE** system (CRISPR–Human Organoids–scRNA-seq) perturbs **36 high-confidence ASD genes** (all SFARI score-1 transcriptional/chromatin regulators) in parallel and reads out their effects on **cell-fate composition, gene expression, and a developmental gene-regulatory network (GRN)** at the level of dozens of telencephalic cell types.

**The CHOOSE platform (the methodological core).**
- Inducible, low-off-target **eCas9** under a **loxP-STOP** cassette; a lentivirus delivers **4-OHT-inducible CRE** + a **dual-sgRNA cassette (two gRNAs/gene)** placed in the **3′ LTR** (CROP-seq design) so the gRNA is **Pol-II-transcribed and captured by scRNA-seq**.
- **Verified guides:** a TagBFP flow-cytometry reporter assay screened **98 dual-sgRNA cassettes** to pick efficient pairs for all 36 genes (IHC confirmed protein loss for most).
- **Mosaicism by design:** lentiviral infection held at **2.5–<5%** (≈1 integration/cell); a **unique clone barcode (UCB, 1.4×10⁷ combinations)** tracks clonal lineage to separate true perturbation effects from clonal expansion. **~2,770 founder clones/perturbation**; mutant (GFP⁺/dTomato⁺) cells stay a minority (**avg 21.8% at day 120**), keeping each organoid a near-isogenic mosaic.
- **Telencephalon organoids** (Lancaster/Knoblich guided protocol); eCas9 induced in **day-5 EBs**; profiled at **4 months**. Total: **49,754 cells** (35,203 control/uninduced for annotation), 65 organoids, 14 pools, 3 batches; recapitulates dorsal **and** ventral trajectories (RGC, cycling-RGC, oRGC/HOPX, IPC/EOMES, L2/3–L6 excitatory + CThPN; v-RGC, INP/DLX2, LGE/CGE interneurons, OPC, astrocytes).

**Convergent vulnerable cell types.** Across perturbations the most affected populations are **dorsal intermediate progenitors (IPCs), ventral radial glia (v-RGCs), interneuron precursors (INPs), and upper-layer (L2/3) excitatory neurons**:
- **IPC depletion** = a strong convergent effect in **12 perturbations** (e.g. CHD2, KAT2B, KMT2C); validated by ↓EOMES⁺ IPCs in KMT2C/PHF3 individually-perturbed organoids (day 60).
- **v-RGC and/or ccv-RGC enrichment** in **10 perturbations** (e.g. ARID1B, BCL11A, DEAF1); **INP enrichment** in **10** (e.g. ILF2, MED13, TCF20; validated ↑DLX2⁺ INPs).
- **Dorsal→ventral shift:** 24 perturbations changed the dorsal:ventral ratio; **21 of 24 lowered it** (more ventral). 23 perturbations changed ≥1 cell-type abundance.
- **L2/3 excitatory neurons** depleted in the majority of perturbations — concordant with ASD coexpression networks enriched in upper-layer neurons. Implies ASD pathology can emerge **as early as the progenitor stage**.

**Molecular + GRN readouts.** **2,071 DEGs** total; recurrent hits include **CHCHD2 down** (7 perturbations; a mitochondrial gene down in ASD postmortem brain) and **CSMD1** (most frequent ventral DEG). Top-DEGs are **~2-fold enriched for SFARI ASD genes** (Fisher P<10⁻⁵) but **not** for intellectual-disability genes (sysID) → ASD-specific regulatory programs. A multiome (scRNA + scATAC) **GRN inferred with Pando** identifies an **ASD-associated sub-network** (40 SFARI-enriched TF modules; 14 encoded by ASD genes, e.g. NFIA, BCL11A, MEF2C). Perturbation DEGs concentrate in specific modules — ventral: **CREB5, MEIS2, NFIA, OLIG1**; dorsal: **SATB2, BACH2, MEF2C, EOMES**. The **OLIG1** and **EOMES** regulomes are highlighted as vulnerable fate-specification hubs.

**ARID1B → OPC/interneuron fate (the validated mechanism).** `ARID1B` (a **BAF/SWI-SNF** subunit) perturbation gives one of the strongest **v-RGC enrichments** and enriches the **OLIG1** module. CellRank trajectory analysis: ARID1B-perturbed v-RGCs have **significantly higher transition probability to early OPCs** (Wilcoxon P=7.7×10⁻⁸) and more **OLIG2⁺ v-RGCs** (OLIG2⁺ 19.6%→36.2%; OLIG2⁺DLX2⁺ 9.8%→30.6%, control vs ARID1B). **Patient validation:** two ARID1B⁺/⁻ patients (c.2201dupG truncation; 6q25.3 microdeletion) + a CRISPR-corrected isogenic control → **ventralized (SAG/IWP2) day-40 organoids show markedly increased OLIG2⁺, DLX2⁺ and OLIG2⁺DLX2⁺ cells** in both patients (ANOVA P<0.001). **In vivo corroboration:** intrauterine super-resolution MRI of patient 2 (GW22, GW31) shows an **enlarged ganglionic eminence** vs age-matched controls. All three BAF subunits tested (**ARID1B, BCL11A, SMARCC2**) enrich v-RGCs → BAF complex is a node for ventral-telencephalon fate control.

## Methods / Protocol

- **Cells.** H9 hESC (WiCell) carrying loxP-STOP-eCas9, STR/SNP-authenticated, mycoplasma-negative; ARID1B-patient iPSCs + isogenic corrected line.
- **Organoids.** Knoblich-lab guided telencephalon protocol (16,000 cells/EB; CHIR99021 d13–16; IDM−A from d14, IDM+A from d25; 1% Matrigel d40–90; BrainPhys + BDNF/GDNF/bucladesine from d60–70). **Ventralized organoids** = unembedded EBs + **SAG (100 nM) + IWP2 (2.5 µM)** d5–11. eCas9 induced with **0.3 µg/ml 4-OHT at day 5**.
- **CHOOSE construction.** sgRNAs picked by VBC score → TagBFP/3T3 reporter editing assay (BFP loss = efficient; 98 cassettes tested). Dual-sgRNA cassette (U6-sgRNA1-H1-sgRNA2) cloned into 3′ LTR of a CAG-ERT2-Cre-ERT2-P2A-EGFP lentivirus (CROP-seq style). **15-bp barcode (UCB)** added by PCR; ASD library = 36 paired guides, control = non-targeting pair; pooled **96:4 ASD:control**; infection <5%; GFP⁺ cells FACS-sorted, expanded to preserve complexity, then formed into EBs.
- **Readouts / analysis.** 10x scRNA-seq + **single-cell multiome (RNA+ATAC)** at 4 months; gRNA recovered from cDNA and bulk gDNA; cell typing via control-cell annotation + label transfer; **RNA velocity + CellRank** for trajectories/fate probabilities; **Cochran–Mantel–Haenszel** test (stratified by pool) for differential cell-type abundance; DESeq-style DEG calling; **Pando** GRN from multiome; SFARI/sysID Fisher enrichment. Individual-gene validation by FACS and **day-60 IHC** (EOMES, DLX2). Patient organoids validated by IHC (OLIG2/DLX2) + intrauterine MRI 3D-reconstruction of the ganglionic eminence.

## Relevance to the brain-organoid ASD review

Supports the manuscript *"Programmable Brain Organoids for Proactive Autism Genetics."*

- **THE flagship in-organoid pooled CRISPR screen — the central methods citation for the whole "programmable / proactive" thesis.** Wherever the review argues that brain organoids can move from *one-gene-at-a-time* modelling to **high-throughput, multiplexed functional genomics in a human context**, CHOOSE is the anchor: 36 ASD genes, perturbed and phenotyped **in parallel inside mosaic organoids** with single-cell resolution. This is the paper that operationalizes "proactive autism genetics."
- **Defines the modern CRISPR-perturbation toolkit for the review's perturbation theme.** Inducible eCas9 + loxP-STOP, **dual verified guides**, **3′-LTR/CROP-seq capture**, **clone barcoding to control clonal artifacts**, and **mosaicism for near-isogenic comparisons** are the methodological advances the review should foreground. Contrast it explicitly with the *one-gene-per-isogenic-line* approach of [Paulsen 2022](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) and the *assembloid* CRISPR screens of [Meng 2023](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md) — CHOOSE is the **dorsal+ventral mosaic cerebral-organoid** end of that spectrum.
- **Best single-paper evidence for "convergence on shared vulnerable cell types/stages."** Concrete, quantified convergence — IPCs, v-RGCs/INPs and L2/3 excitatory neurons hit across many unrelated ASD genes — directly supports the review's CONVERGENCE argument, complementing Paulsen 2022 (shared neuron classes) with a much wider gene panel. Note the symmetrical caveat the authors raise: GO/DEG analysis shows **both convergent and divergent** molecular mechanisms.
- **Functional-genomics readouts the review can cite as the "Stage-3"/network end-point.** Cell-state composition, cell-type-specific DEGs, and an **ASD-associated GRN with vulnerable TF hubs (OLIG1, EOMES, BAF modules)** are exactly the multi-layered readouts the review proposes for prioritizing variants — a template for reading many genes through shared molecular/network axes.
- **A fully worked gene→cell-fate→patient→in-vivo example (ARID1B).** The ARID1B → OPC/interneuron-fate result, validated in **two patient iPSC lines + isogenic control** and corroborated by **fetal MRI (enlarged ganglionic eminence)**, is the review's cleanest demonstration that an organoid-screen hit can be carried all the way to human-relevant pathology — and it implicates **oligodendrocyte-lineage / ventral-telencephalon** biology in ASD, broadening the usual excitatory-neuron focus.
- **Lineage / provenance.** Builds directly on the GRN-inference and perturbation methods of [Fleck 2023](fleck_2023_inferring_perturbing_cell_fate_regulomes_human_brain.md) (Pando; shared first/second authors) and the tissue-screen logic of [Esk 2020](esk_2020_human_tissue_screen_identifies_regulator_er_secretion.md) (the earlier low-content organoid CRISPR screen from the same lab). The ARID1B/ganglionic-eminence link connects to [Eichmüller 2022](eichmller_2022_human_cerebral_organoids_new_tool_clinical_neurology.md) on interneuron-progenitor amplification.

### Related pages
- [Esk 2020 — Human tissue screen identifies a regulator of ER secretion as a brain-size determinant](esk_2020_human_tissue_screen_identifies_regulator_er_secretion.md) — the precursor low-content (gRNA-count) organoid CRISPR screen CHOOSE upgrades to single-cell readout.
- [Fleck 2023 — Inferring and perturbing cell-fate regulomes in human brain organoids](fleck_2023_inferring_perturbing_cell_fate_regulomes_human_brain.md) — the Pando GRN / perturbation framework reused here (shared authorship).
- [Meng 2023 — Assembloid CRISPR screens reveal the impact of disease genes](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md) — the complementary *assembloid* mosaic-screen approach.
- [Paulsen 2022 — Autism genes converge on asynchronous development of shared neuron classes](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) — isogenic-line ASD-gene organoid study; convergence on shared cell types (contrast the screening strategy).
- [Mariani 2015 — FOXG1-dependent dysregulation of GABA/glutamate differentiation in ASD](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md), [Villa 2022 — CHD8 haploinsufficiency](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md) — earlier organoid ASD-gene phenotypes referenced for E/I and transient-defect themes.
- [Lancaster 2013](lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.md) — the organoid platform CHOOSE is built on (cited as the disease-modelling premise).
- Concept: [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md); entity: [CRISPR-Cas9 and next-generation CRISPR editing](../entities/crispr-cas9-and-next-generation-crispr-editing.md).

## Open questions / limitations

- **Missing cell types.** No microglia, **no MGE-derived interneurons**, no vasculature — so ASD effects on those lineages (and circuit-level consequences) are invisible here. The model is a *developing telencephalon snapshot*, not a mature circuit.
- **Zygosity unknown.** The reporter/editing strategy does **not** distinguish heterozygous from homozygous knockouts, so phenotypes may reflect biallelic loss rather than the haploinsufficiency typical of human ASD variants — a real interpretive gap for dosage-sensitive genes.
- **Gene class is narrow.** All 36 genes are **transcriptional/chromatin regulators (SFARI-1)**; whether the same vulnerable cell types converge for synaptic, signalling, or other ASD-gene classes is untested by this screen.
- **Transient phenotypes may be missed.** The authors note (citing Paulsen 2022) that cell-type-abundance effects can be **transient**; a single 4-month snapshot can miss earlier or later windows. Compositional scRNA-seq is also relative, so one population's expansion mechanically depresses others.
- **Mutant fraction is low.** Mutant cells average ~22% at day 120, limiting detection of **non-cell-autonomous** effects and mutant–mutant interactions; severe phenotypes might be under-sampled.
- **Validation breadth.** Deep patient/in-vivo validation was done for **ARID1B only**; most of the 35 other genes rest on the screen + limited individual IHC. The GRN is an inference (Pando) over organoid multiome data, not a directly measured network.
