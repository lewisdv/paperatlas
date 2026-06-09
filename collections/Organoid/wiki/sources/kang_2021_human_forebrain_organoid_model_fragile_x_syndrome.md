---
title: "A human forebrain organoid model of fragile X syndrome exhibits altered neurogenesis and highlights new treatment strategies."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41593-021-00913-6
pmid: 34413513
authors: Kang Y et al.
journal: Nature neuroscience (2021)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/kang_2021_human_forebrain_organoid_model_fragile_x_syndrome.pdf
pdf_status: downloaded
---

# A human forebrain organoid model of fragile X syndrome exhibits altered neurogenesis and highlights new treatment strategies.

## Source

- Authors: Kang Y, Zhou Y, Li Y, Han Y, Xu J, Niu W, Li Z, Liu S et al. (co-corresponding: Peng Jin & Zhexing Wen, Emory University School of Medicine).
- Journal: Nature Neuroscience 2021;24:1377–1391 (published online 19 Aug 2021).
- DOI: [10.1038/s41593-021-00913-6](https://doi.org/10.1038/s41593-021-00913-6)
- PMID: [34413513](https://pubmed.ncbi.nlm.nih.gov/34413513/)
- Data: GEO **GSE146878** (scRNA-seq, bulk RNA-seq, eCLIP-seq).
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Fragile X syndrome (FXS) is caused by the loss of fragile X mental retardation protein (FMRP), an RNA-binding protein that can regulate the translation of specific mRNAs. In this study, we developed an FXS human forebrain organoid model and observed that the loss of FMRP led to dysregulated neurogenesis, neuronal maturation and neuronal excitability. Bulk and single-cell gene expression analyses of FXS forebrain organoids revealed that the loss of FMRP altered gene expression in a cell-type-specific manner. The developmental deficits in FXS forebrain organoids could be rescued by inhibiting the phosphoinositide 3-kinase pathway but not the metabotropic glutamate pathway disrupted in the FXS mouse model. We identified a large number of human-specific mRNAs bound by FMRP. One of these human-specific FMRP targets, CHD2, contributed to the altered gene expression in FXS organoids. Collectively, our study revealed molecular, cellular and electrophysiological abnormalities associated with the loss of FMRP during human brain development.

## Key findings

- **Patient-derived FXS forebrain organoid model.** Dorsal-forebrain organoids were grown from iPSCs of **3 male FXS patients** (CGG full mutation, FMR1 silenced) + **3 age/sex-matched controls**, plus a **CRISPR–Cas9 isogenic correction** line (FXS1R, expanded CGG excised). FMRP confirmed absent in FXS iPSCs, EBs, and D28/D56 organoids. Most phenotyping at **Day 56** (~mid-fetal stage, peak human cortical neurogenesis and the period of FMRP depletion in patients).
- **Loss of FMRP reduces NPC proliferation and accelerates premature differentiation at D56.** Fewer Ki67+ proliferating cells among SOX2+/PAX6+ NPCs and fewer EdU+ S-phase cells (****P < 0.0001); increased Ki67−EdU+ cells = accelerated cell-cycle exit. Birth-dating (retro-GFP at D49, scored D56): most control GFP+ cells stayed SOX2+ NPCs, whereas many FXS GFP+ cells became MAP2+ neurons (****P < 0.0001). Note the effect is **stage-dependent** — at the earlier D28 timepoint FXS organoids instead show *increased* Ki67+/SOX2+ NPCs; the authors' model is that FMRP loss accelerates differentiation overall (more proliferation early, depletion later).
- **Disrupted cortical layering and reduced organization.** More TBR2+ intermediate progenitors (IPCs), abnormally mislocated into the CTIP2+/MAP2+ cortical-plate (CP) layer; abnormally strong DCX in PAX6+ NPCs; SOX2+/PAX6+ NPCs detached from the apical VZ and dispersed. VZ thickness reduced and CP thickness increased; deeper-layer markers (POU3F2, SATB2, BCL11B/CTIP2) increased → shift toward deep-layer predominance.
- **Reduced GABAergic fate.** Percentage/number of GABA+ inhibitory neurons dramatically decreased in FXS (CaMKIIα+ glutamatergic vs GABA+ co-stain); RNAscope showed depletion of DLX2+ ventral (ganglionic-eminence) NPCs at both D28 and D56; DLX1/DLX2 down by RNA-seq. (Control organoids are ~10% GABAergic, matching other groups.)
- **Increased synapse formation + neuronal hyperexcitability.** SYN1+PSD95+ synaptic puncta density significantly increased (****P < 0.0001). Whole-cell patch of CTIP2+ glutamatergic neurons in acute organoid slices: passive properties unchanged, but **increased action-potential firing frequency** (P = 0.0336), shorter AP decay time (P = 0.0421), and **larger voltage-activated K+ currents** (peak current density P = 0.0173) with normal Na+ currents; **Kv4.2 expression increased** → proposed driver of hyperexcitability.
- **Human-specific, pervasive transcriptional dysregulation vs near-silent mouse.** Bulk RNA-seq DEGs (FDR < 0.20): **810 (D28), 1,194 (D56), 3,839 (D84)** in organoids and **2,723** in two FXS fetal cortex samples (23- and 24-wk post-conception), with significant same-direction overlap (P < 2.2 × 10⁻¹⁶), strongest at D84 (~18–23 wk). By contrast, **only 3 genes** were differentially expressed in *Fmr1*-KO mouse forebrain at the matched stage (E13.5) — one being *Fmr1* itself. DEGs enriched for neurogenesis, neuronal migration, axonogenesis, membrane-potential regulation.
- **Altered single-cell developmental trajectory.** scRNA-seq of 3 control/FXS pairs (30,550 cells, 14 clusters). Down-DEGs enriched for neurogenesis/differentiation/neuron-projection; up-DEGs for translation, protein targeting to membrane, and oxidative phosphorylation. Neural-stem/radial-glia clusters expanded; CCND2 (proliferation promoter) decreased in NPC/inhibitory clusters; Monocle 3 pseudotime (22 clusters) showed a distinct FXS trajectory with branches/bypasses, with inhibitory-neuron maturation (cluster C7) most perturbed.
- **PI3K inhibition rescues, mGluR5 antagonism does not.** D42→D56 (2-week) treatment: **MPEP** (mGluR5 antagonist, 10 µM) **failed** to normalize Ki67+ NPCs or synaptic puncta — concordant with failed human mGluR5 clinical trials. **LY294002** (pan-PI3K, 10 µM) and **GSK2636771** (PI3Kβ-selective, 1 µM) **largely normalized** both NPC proliferation and synaptic density to control levels. → PI3K, not mGluR5, is the actionable node in this human model.
- **eCLIP identifies human-specific FMRP mRNA targets enriched for ASD genes.** eCLIP-seq (≥8-fold IP/input) on D56 organoids vs E13.5 mouse cortex found **3,726 FMRP-bound mRNAs in human** (1,651 shared with mouse; ~80% of shared overlap Darnell et al. targets). Binding mostly in CDS/introns. Shared targets = neurodevelopment/synaptic plasticity; **human-specific targets = synaptic signaling + Wnt pathway**; mouse-specific = glutamate-receptor signaling. Human FMRP targets significantly enriched among ASD risk genes (50.1% overlap, P < 2.2 × 10⁻¹⁶) but not random gene sets.
- **CHD2 is a human-specific FMRP target with downstream consequences.** Only human (not mouse) FMRP IP pulled down CHD2 mRNA (P = 0.0024). CHD2 **mRNA unchanged** but **protein increased** in FXS organoids (P = 0.0016) — consistent with FMRP normally repressing CHD2 translation. DEGs from FXS organoids overlapped E13.5 *Chd2⁺/⁻* mouse DEGs (408/1,004, P < 2.2 × 10⁻¹⁶), and 255/408 are ENCODE CHD2-bound → CHD2 (an ID/ASD risk gene) is positioned as a convergent, potentially druggable node.

## Methods

- **Organoid protocol:** dorsal-forebrain (cortical) organoids via the Qian/Ming–Song **miniature spinning bioreactor (SpinΩ)** route. EB in dorsomorphin + A-83-01; neural induction with **WNT-3A (4 ng/mL) + CHIR99021 (1 µM, GSK3 inhibitor → WNT activation) + SB-431542**; Matrigel embedding D7; bioreactor differentiation from D14; maturation medium (BDNF/GDNF/TGFβ/cAMP) from D71. Analyses focused on D56 (with D28/D84 for time course).
- **Cellular assays:** Ki67/EdU proliferation & cell-cycle-exit; retroviral GFP birth-dating (infect D49, score D56); immunostaining panel (SOX2, PAX6, TBR1, TBR2/EOMES, CTIP2/BCL11B, DCX, MAP2, CaMKIIα, GABA, SYN1, PSD95); 5-bin neuroepithelial distribution analysis; VZ/CP thickness; RNAscope (SOX2, DLX2, PAX6). Quantification blinded in ImageJ.
- **Electrophysiology:** whole-cell patch on 225-µm acute organoid slices; current-clamp AP trains and voltage-clamp Na+/K+ currents; recorded neurons dye-filled (Alexa 594) and CTIP2-confirmed.
- **Genomics:** bulk RNA-seq (STAR/DESeq2, hg19/mm9; FXS fetal cortex from full-mutation terminations + control brain bank tissue, ethics-approved); 10x scRNA-seq (30,550 cells, Seurat 3.1, Monocle 3); FMRP **eCLIP-seq** (CLIPper peaks; human organoids vs E13.5 mouse cortex); Western blot (FMRP, CHD2) and qRT–PCR; GO via PANTHER.
- **Pharmacology:** MPEP 10 µM; LY294002 10 µM; GSK2636771 1 µM; D42–D56 dosing.

## Relevance to the brain-organoid ASD review

- **Table-1 monogenic disease-model entry — FMR1 / Fragile X.** This is the FMR1/FXS exemplar for the review's catalogue of monogenic organoid ASD models: a complete-loss, patient-iPSC + isogenic-corrected human forebrain-organoid model with convergent cellular, electrophysiological, and transcriptomic phenotypes.
- **Strongest "human organoids beat mouse" argument in the corpus.** ~1,000–3,800 organoid DEGs and 2,723 fetal-cortex DEGs (overlapping) vs essentially **3** in *Fmr1*-KO mouse directly motivates the review's thesis that human 3D models capture disease biology that rodent models miss — and that human-specific FMRP targets (incl. CHD2, Wnt-pathway genes) are missable in mouse.
- **Mechanism-guided, programmable rescue.** The PI3K-yes / mGluR5-no dissociation (with the mGluR5 result mirroring failed human trials) is a clean proof-of-concept for the review's "proactive/programmable" framing: use the human organoid to triage druggable pathways before the clinic.
- **Phenotype themes shared across the review:** accelerated/premature neurogenesis and altered cortical layering (cf. mTOR/oRG biology in [Andrews 2020](andrews_2020_mtor_signaling_regulates_morphology_migration_outer_radial.md)); GABAergic-fate reduction and excitatory/inhibitory imbalance (contrast with GABA *overproduction* in idiopathic-ASD [Mariani 2015](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md)); neuronal hyperexcitability (parallels [St George-Hyslop 2023](st_2023_loss_cntnap2_alters_human_cortical_excitatory_neuron.md) CNTNAP2).
- **WNT/SHH patterning connection.** Human-specific FMRP targets are enriched in the **Wnt pathway**, and the protocol itself uses WNT-3A/CHIR for dorsal-telencephalic patterning — linking this disease model to the patterning-gradient background reviewed in [Hébert 2008](hbert_2008_genetics_early_telencephalon_patterning_some_assembly_required.md).
- **Convergent risk gene (CHD2).** Positions CHD2 as an FMRP-downstream, ASD/ID-convergent node, complementing other convergence-themed corpus papers ([Paulsen 2022](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md), [Li 2023 CHOOSE screen](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md)).

## Open questions / limitations

- **Few lines, male-only.** 3 FXS + 3 control (1 isogenic) male donors; CGG full mutation only — does not cover mosaics, premutation, or females; isogenic control exists for just one line.
- **Stage-dependent, opposite proliferation effects** (D28 increase vs D56 decrease) complicate interpretation and any rescue timing; the authors infer "accelerated differentiation" but the switch mechanism is unresolved.
- **mGluR5 caveat:** the negative mGluR5 result (and the human trials it echoes) used adults/adolescents, not early development — the developmental-window question for mGluR5 is not closed here.
- **PI3K rescue is short-term and partial-readout** (Ki67, synaptic puncta at D56); long-term functional/electrophysiological rescue and in-vivo translation are untested.
- **Dorsal-biased model under-samples GABAergic biology.** Reduced GABAergic neurons are inferred in a dorsal-forebrain organoid; ventral organoids or assembloids would be needed to study interneuron generation directly (authors note this).
- **Proposed m6A explanation** for the human/mouse divergence in FMRP-dependent gene regulation is a hypothesis, not demonstrated in this study.

## Related

- [St George-Hyslop 2023 — Loss of CNTNAP2 alters human cortical excitatory neuron differentiation](st_2023_loss_cntnap2_alters_human_cortical_excitatory_neuron.md) — sibling Table-1 monogenic model (CNTNAP2); shared hyperexcitability theme.
- [Hébert 2008 — Genetics of early telencephalon patterning](hbert_2008_genetics_early_telencephalon_patterning_some_assembly_required.md) — WNT/SHH patterning background for the dorsal-forebrain protocol and FMRP Wnt-target enrichment.
- [Mariani 2015 — FOXG1-dependent GABA/glutamate dysregulation in ASD](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md) — contrasting GABAergic phenotype in idiopathic ASD organoids.
- [Li 2023 — Single-cell brain-organoid CRISPR screen (CHOOSE) in autism](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md) — convergent ASD vulnerability and screening logic.
- [Paulsen 2022 — Autism genes converge on asynchronous development of shared neuron classes](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) — convergence framing for FMRP/CHD2.
- [Andrews 2020 — mTOR regulates oRG morphology/migration](andrews_2020_mtor_signaling_regulates_morphology_migration_outer_radial.md) — parallel kinase-pathway (PI3K/mTOR) progenitor vulnerability.
- [Paşca 2015 — Functional cortical neurons and astrocytes from hPSCs in 3D](paca_2015_functional_cortical_neurons_astrocytes_human_pluripotent_stem.md) — guided cortical-organoid platform precedent.
- Concept: [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
