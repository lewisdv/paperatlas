---
title: "Dysregulation of BRD4 Function Underlies the Functional Abnormalities of MeCP2 Mutant Neurons."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.molcel.2020.05.016
pmid: 32526163
authors: Xiang Y et al.
journal: Molecular cell (2020)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Dysregulation of BRD4 Function Underlies the Functional Abnormalities of MeCP2 Mutant Neurons.

## Source

- Authors: Yangfei Xiang, Yoshiaki Tanaka, Benjamin Patterson, Sung-Min Hwang, Eriona Hysolli, Bilal Cakir, Kun-Yong Kim, Wanshan Wang et al. (Sherman M. Weissman; lead/corresponding In-Hyun Park, Yale)
- Journal: Molecular Cell 79, 84–98 (July 2, 2020)
- DOI: [10.1016/j.molcel.2020.05.016](https://doi.org/10.1016/j.molcel.2020.05.016)
- PMID: [32526163](https://pubmed.ncbi.nlm.nih.gov/32526163/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Rett syndrome (RTT), mainly caused by mutations in methyl-CpG binding protein 2 (MeCP2), is one of the most prevalent intellectual disorders without effective therapies. Here, we used 2D and 3D human brain cultures to investigate MeCP2 function. We found that MeCP2 mutations cause severe abnormalities in human interneurons (INs). Surprisingly, treatment with a BET inhibitor, JQ1, rescued the molecular and functional phenotypes of MeCP2 mutant INs. We uncovered that abnormal increases in chromatin binding of BRD4 and enhancer-promoter interactions underlie the abnormal transcription in MeCP2 mutant INs, which were recovered to normal levels by JQ1. We revealed cell-type-specific transcriptome impairment in MeCP2 mutant region-specific human brain organoids that were rescued by JQ1. Finally, JQ1 ameliorated RTT-like phenotypes in mice. These data demonstrate that BRD4 dysregulation is a critical driver for RTT etiology and suggest that targeting BRD4 could be a potential therapeutic opportunity for RTT.

## Key findings

- **Isogenic male hESC RTT model.** CRISPR-Cas9 knock-in of the three most frequent clinical MeCP2 mutations into the male H1 hESC line — **R133C** (C397T, MBD/DNA-binding domain), **R270X** (C808T, NLS), **R306C** (C916T, TRD) — to avoid confounding X-inactivation. Cells stayed pluripotent; no off-targets at top predicted sites. R133C is the primary focus.
- **MeCP2 mutation severely impairs human interneurons (INs).** INs differentiated via an MGE protocol over ≥10 weeks. MeCP2-R133C INs showed decreased neurite growth, neurite coalescence, and soma size; failed to fire APs (or only small-amplitude onset spikes) by patch-clamp; calcium imaging showed individual firing and network synchronization in WT INs but rarely-detectable Ca²⁺ surges in R133C INs.
- **Broad transcriptional dysregulation.** RNA-seq across IN development (day 10→74); the most drastic deficits appeared in **mature INs (day 74)** — axon/dendrite growth, synapse development, ion channel activity. Proteomics (8,250 quantified proteins, day 76) correlated with transcriptome; calcium-related components strongly affected; depolarization-induced IEG transcription (c-FOS, FOSB, NPTX2) significantly reduced in R133C INs.
- **JQ1 (BET inhibitor) rescues RTT INs — the headline result.** Low-dose **JQ1 (75 nM)** shifted the R133C IN transcriptome to resemble WT, with minimal effect on WT INs; rescued ion-channel gene expression and IGF1, KCC2, mGlu7 (known RTT-downregulated); restored activity-dependent IEG induction. JQ1 rescued single-cell Ca²⁺ surges **and** network synchronization in R133C INs. Reproduced in an independent R133C clone.
- **Rescue is dosage- and time-dependent.** Effective window ~50–75 nM over prolonged (cumulative) treatment; up to 300 nM over ~10 days still rescued IEG induction, but too-high or too-low doses over prolonged treatment were not beneficial. **Acute 24 h JQ1 failed** (10-day treatment from the mature stage worked) → cumulative effect needed.
- **Generalizes across mutations and BET inhibitors.** R306C INs (milder, ↑Ca²⁺ spike frequency / ↓amplitude) and R270X INs (more impaired, ↓frequency + ↓amplitude) were both reversed by JQ1 (amplitude and network synchronization). Other BET inhibitors **CPI203 (50 nM)** and **I-BET762 (100 nM)** produced comparable rescue; IGF1 (20 ng/mL) did **not** rescue activity.
- **Cell-type / region specificity.** Cortical neurons (CNs) and cortical organoids (hCOs) were comparatively *less* sensitive to R133C than MGE INs/organoids — WT and R133C hCOs both showed area-scale Ca²⁺ synchronization; the MGE region was the vulnerable compartment. R133C CNs still showed reduced depolarization-induced c-FOS (FOSB intact); JQ1 improved c-FOS/FOSB induction in both WT and R133C CNs.
- **Mechanism — BRD4 hyperbinding.** ChIP-seq: KCl depolarization increases genome-wide BRD4 binding in WT INs (reduced by JQ1). **R133C INs show dramatically increased BRD4 binding even without stimulation, resembling activated WT** — and KCl barely adds further (a ceiling → loss of activity-dependent plasticity). JQ1 robustly lowered BRD4 occupancy in R133C INs and **restored** the KCl-inducible increase. Excess BRD4 binding correlated with transcriptional upregulation (including IEGs); reducing it via JQ1 attenuated that transcription.
- **MeCP2–BRD4 axis.** MeCP2 binding is dramatically reduced globally in R133C INs, specifically at highly-methylated CpG loci (mCpG levels themselves unchanged; no significant 5hmC change). MeCP2 and BRD4 occupy overlapping target genes; loss of MeCP2 binding at depolarization-induced genes coincides with BRD4 gain (e.g., FOSB, JUNB) and target upregulation. Model: MeCP2 loss → de-repression → BRD4 over-recruitment → hyperactive transcription.
- **3D genome / chromatin topology.** ATAC-seq: R133C open-chromatin profile distinct from WT, normalized by JQ1 (1,102/1,313 JQ1-rescued dOCRs were abnormally *open*; 211 abnormally *closed*); dOCRs enriched at distal enhancers of DE genes and enriched for BRD4 binding. Opened dOCRs enriched for IEG/AP-1 motifs (FOSL2, JUNB, AP-1); closed dOCRs enriched for neural-development TF motifs (ASCL1, OLIG2, SOX). Hi-C: enhancer–promoter interactions **markedly increased** in R133C INs and attenuated by JQ1; CTCF binding unaffected by mutation or JQ1.
- **Single-cell rescue in region-specific organoids.** hMGEOs and hCOs (cultured ~2.5 months; JQ1 75 nM from day 25); scRNA-seq, 30 clusters spanning RGCs, CNs, INs, glia, etc. 100–500 genes dysregulated per neuron/glia group in R133C; **JQ1 sharply reduced dysregulated-gene counts toward WT, more completely in hMGEO-derived cells than hCO-derived.** Cell-type/region-specific examples: TAC1, SMARCD3 down in R133C INs (rescued); MEF2C, NEUROD2 aberrantly up in R133C hCO neurons (rescued); OLIG2, MBP up in R133C hMGEO glia (rescued); EMX2, GLI3 dysregulated in R133C hCO glia (rescued); astrocyte genes (EAAT1, ALDH1L) unchanged.
- **In vivo rescue in mice.** Daily IP JQ1 **15 mg/kg** from 2 weeks of age into MeCP2−/Y mice: median survival **94 days (JQ1) vs 52 days (untreated)** — ~81% lifespan increase; significantly slowed symptom-score progression and delayed hindlimb clasping (more prominent at earlier stages); body weight unaffected.

## Methods

- **Cells / mutations:** male H1 hESC, CRISPR-Cas9 knock-in of MeCP2 R133C, R270X, R306C (isogenic to WT); GCaMP6s reporter knocked into AAVS1 for Ca²⁺ imaging.
- **2D differentiation:** MGE-protocol interneurons (cultured >10 weeks; functional readouts ~day 74–78), co-cultured with mouse astrocytes for electrophysiology; cortical neurons (CNs) as comparison.
- **3D models:** human MGE organoids (hMGEOs) and cortical organoids (hCOs) per Xiang et al. 2017; cultured ~2.5 months.
- **Drug:** JQ1 (BET/BRD4 inhibitor), low-dose 50–75 nM (up to 300 nM tested); comparators CPI203, I-BET762, IGF1.
- **Functional assays:** whole-cell patch-clamp; calcium imaging (single-cell + network synchronization, and area-scale in organoids); KCl-depolarization IEG induction (qPCR).
- **Genomics:** bulk RNA-seq (developmental series), proteomics, BRD4 & MeCP2 & CTCF ChIP-seq (± KCl, ± JQ1), RRBS/oxRRBS (mCpG/5hmC), ATAC-seq, Hi-C, and scRNA-seq of organoids.
- **In vivo:** MeCP2−/Y mice (Guy et al. 2001, exon 3–4 deletion); daily IP JQ1 15 mg/kg from 2 weeks; survival (Kaplan-Meier, n=16 treated / 14 untreated), symptom scoring, hindlimb clasping, body weight.

## Relevance to the brain-organoid ASD review

- **This is the Table-1 MeCP2 / Rett entry the manuscript builds on.** It supplies the **BRD4 dysregulation mechanism** and the **BET-inhibition (JQ1) rescue** that the review's MeCP2/Rett discussion cites: MeCP2 loss-of-function → loss of MeCP2 chromatin binding → excess BRD4 recruitment → increased enhancer–promoter contacts → hyperactive transcription → impaired neuronal development/activity/plasticity; JQ1 reverses it at molecular, functional, organoid (scRNA-seq), and whole-animal (survival) levels.
- **Human, isogenic, multi-scale evidence.** CRISPR-isogenic human hESC lines spanning three clinical mutations, plus region-specific organoids, plus an in vivo mouse rescue — exactly the kind of convergent, mechanism-to-therapy data a "programmable / proactive autism genetics" argument needs.
- **Cell-type and regional selectivity is a key takeaway for ASD organoid design.** MGE-derived **interneurons** are the vulnerable population; cortical neurons/organoids are relatively spared — arguing for **region-specific (MGE) organoids** when modeling MeCP2/RTT and, more broadly, that ASD phenotypes can be cell-type-restricted and missed by whole-cortex models.
- **Druggable epigenetic node.** Frames BET/BRD4 as a candidate therapeutic axis for an MeCP2-linked neurodevelopmental disorder, with explicit dose/timing constraints (low-dose, cumulative, mutation-dependent) that the review can cite as both promise and caution.
- **Methodological bridge:** uses the same hCO/hMGEO platform (Xiang 2017) central to the review's region-specific organoid toolkit, and demonstrates scRNA-seq as the readout for cell-type-resolved rescue.

## Open questions / limitations

- **Therapeutic window is narrow and mutation-dependent:** only low-dose (50–75 nM), prolonged/cumulative JQ1 rescued; high-dose JQ1 is known to impair memory (Korb 2015); acute 24 h dosing failed.
- **Pharmacology of JQ1 is unfavorable for translation:** short plasma half-life; needs more stable analogs and optimized delivery despite good BBB penetration.
- **Non-CNS effects of systemic JQ1 in MeCP2−/Y mice not excluded;** survival benefit could be partly peripheral.
- **In vivo readouts are survival/behavioral**, not the human-cell molecular endpoints — circuit-level rescue in vivo not directly shown.
- **CN/cortical sparing is incompletely explained** (organoid environment may be "more favorable," or cortex genuinely less MeCP2-sensitive); other (BRD4-independent) mechanisms contribute to IEG regulation (e.g., NPAS4).
- Generalization beyond the three tested mutations (and to female/mosaic RTT, the clinical norm) is untested in this isogenic male-line design.

## Related

- [birey_2017](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md) — MGE-derived interneuron generation and forebrain assembloids; context for the IN biology this paper probes.
- [birey_2022](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md) — molecular basis of human interneuron behavior in forebrain assembloids.
- [brain-subregion-specific-organoid-protocols](../concepts/brain-subregion-specific-organoid-protocols.md) — MGE vs cortical region-specific organoids (hMGEO/hCO), central to the cell-type-specific findings here.
- [crispr-cas9-and-next-generation-crispr-editing](../entities/crispr-cas9-and-next-generation-crispr-editing.md) — isogenic mutation knock-in approach used to build the RTT model.
- [calcium-imaging-readouts](../entities/calcium-imaging-readouts.md) — single-cell and network-synchronization Ca²⁺ assays used as the functional rescue readout.
