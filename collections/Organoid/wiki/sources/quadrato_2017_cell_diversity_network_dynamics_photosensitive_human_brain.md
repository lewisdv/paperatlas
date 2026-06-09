---
title: "Cell diversity and network dynamics in photosensitive human brain organoids."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1038/nature22047
pmid: 28445462
authors: Quadrato G et al.
journal: Nature (2017)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/quadrato_2017_cell_diversity_network_dynamics_photosensitive_human_brain.pdf
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# Cell diversity and network dynamics in photosensitive human brain organoids.

## Source

- Authors: Quadrato G, Nguyen T, Macosko EZ, Sherwood JL, Min Yang S, Berger DR, Maria N, Scholvin J et al. (senior author: Paola Arlotta; Harvard / Stanley Center, Broad Institute)
- Journal: Nature (2017), Vol 545:48-53.
- DOI: [10.1038/nature22047](https://doi.org/10.1038/nature22047)
- PMID: [28445462](https://pubmed.ncbi.nlm.nih.gov/28445462/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

In vitro models of the developing brain such as three-dimensional brain organoids offer an unprecedented opportunity to study aspects of human brain development and disease. However, the cells generated within organoids and the extent to which they recapitulate the regional complexity, cellular diversity and circuit functionality of the brain remain undefined. Here we analyse gene expression in over 80,000 individual cells isolated from 31 human brain organoids. We find that organoids can generate a broad diversity of cells, which are related to endogenous classes, including cells from the cerebral cortex and the retina. Organoids could be developed over extended periods (more than 9 months), allowing for the establishment of relatively mature features, including the formation of dendritic spines and spontaneously active neuronal networks. Finally, neuronal activity within organoids could be controlled using light stimulation of photosensitive cells, which may offer a way to probe the functionality of human neuronal circuits using physiological sensory stimuli.

## Key findings

### Long-term, low-stress culture
- Modified whole-brain (self-patterning) protocol for **progressive growth >9 months**: seed embryoid bodies from a **reduced 2,500 pluripotent cells**, optimized neural induction, transfer to **spinning bioreactors** at day 15, and add **BDNF** to the final differentiation medium from 1 month.
- Organoids did **not become hypoxic** and apoptosis stayed low out to 9 months. Yield from EBs improved to **>95% at 1 month (iPSC line 11a)** and **70% (ESC line HUES66)**.
- IHC time course: by 1 month, regional markers for forebrain (PAX6, NKX2.1), midbrain (OTX2), hindbrain (GBX2) and retina (VSX2, OTX2); progenitors first, then glutamatergic/GABAergic/dopaminergic neurons and GFAP+ astroglia.

### Large single-cell map of cell diversity (Drop-seq)
- **82,291 single cells from 31 organoids** (healthy-control iPSC line 11a), profiled at 3 and 6 months.
- 6-month dataset: **66,889 cells -> 10 transcriptionally distinct populations.** Seven largest clusters identified by comparison to endogenous reference signatures:
  - c1 mesodermal (3,027 cells; myogenin, MYH3/8, MYL1, MYLPF) — a minority non-neurectodermal population despite early neural patterning.
  - c2 astroglia (8,409; AQP4, GFAP); c9 neuroepithelial/OPC-like progenitors (17,103); c10 highly proliferative progenitors (13,428; TOP2A, MKI67); c3 dopaminergic-enriched neurons (971; TH, EBF1).
  - **c4 forebrain/cortical** (12,378) and **c5 retina** (9,919; photoreceptor markers CRX, RCVRN) — the two headline neural identities.
- **Subclustering matches endogenous diversity:** c4 -> radial glia, interneurons (DLX5/DLX2/GAD1), intermediate progenitors (EOMES/ELAVL4), corticofugal and callosal projection neurons; correlates with human fetal-cortex scRNA-seq. c5 contains **nearly all mouse-retina cell classes** — Muller glia, pigmented epithelium, photoreceptors (CRX/RCVRN/NRL), retinal ganglion cells, bipolar and amacrine cells.

### Reproducibility and bioreactor batch effects
- Some clusters reproducible (c1, c2, c5, c9, c10 each in **>89% of organoids**); others sporadic (c3 in 53%, c4 forebrain in only **32%**).
- **Organoids from the same bioreactor were more alike** (e.g., 100% of bioreactor-3 organoids contained the forebrain cluster) — i.e., growth environment / bioreactor is a key driver of which cell classes form. This variability is the paper's main reproducibility caveat.

### Maturation over extended culture
- Adding the **3-month dataset (15,402 cells)**: late-born types appear only by 6 months (callosal projection neurons; retinal Muller glia and bipolar cells), and mature signatures emerge with age (mature photoreceptor subcluster — 871 CRX+ cells, all but one from 6-month organoids; mature astrocyte markers GFAP/AQP4/AGT only at 6 months).
- Structural maturity: synapsin-1 (SYN1) absent at 1 month, present from 3 months and out to 9; VGAT+ and VGLUT1+ puncta (GABAergic + glutamatergic synapses). **Serial EM of an 8-month organoid:** reconstruction of ~16x16x5.4 um identified **129 synapses (0.088 synapses/um^3, ~human-fetal-cortex range)**; labelled dendrites bore **37 dendritic spines**, 30 of them innervated — dendritic spines are notoriously hard to obtain in vitro.

### Spontaneously active networks (electrophysiology)
- High-density silicon-probe extracellular recordings: spikes isolated in **6 of 7 organoids at 8 months** (median firing rate **0.66 Hz**, Q1-3 0.20-2.08), but **0 of 4 at 4 months** (Fisher's exact P = 0.015) — activity tracks the maturation seen in the transcriptome.
- Spikes are action potentials (abolished by 2 uM tetrodotoxin; typical waveforms/refractory periods). Spike-train cross-correlograms show short-lag positive peaks indicating **excitatory monosynaptic connections**; **20 uM NBQX reduced firing by 81%** -> majority of activity is non-NMDA (AMPA/kainate) glutamatergic synaptic transmission.
- Network-level: most units show network activity; 3 of 6 active organoids show **burst firing / population bursts** with reproducible temporal order of neuronal recruitment — self-organized network dynamics.

### Photosensitive cells respond to light (functional sensory readout)
- Long-term organoids make **photoreceptor-like cells with phototransduction machinery**. Testing **530 nm light** on 25 cells from 10 organoids (7-9 months): a subpopulation showed **attenuated firing after light**, with **4 of 10 organoids** containing light-responsive units; the activity-dependent gene **FOS was upregulated after light** in 8-month organoids (rhodopsin+ rod-like cells present).
- Authors are careful: they **could not determine whether light acts directly on photosensitive cells or via downstream network modulation.** Framed as a possible physiological-sensory route to probe human circuit function, alongside (not replacing) engineered optogenetics.

## Methods

- **Lines:** iPSC line 11a (healthy control; all Drop-seq/EM/ephys diversity data) and ESC line HUES66 (yield comparison).
- **Protocol:** modified Lancaster/Knoblich whole-brain organoid; 2,500 cells/EB; two-step neural induction; Matrigel embedding day 10; **spinning bioreactor** from day 15; BDNF from 1 month; cultured 1-9 months.
- **scRNA-seq:** droplet-based **Drop-seq** (Macosko et al.); PCA + t-SNE clustering; cluster identity by correlating differentially expressed signatures against published endogenous RNA-seq/scRNA-seq datasets (human fetal cortex via Fluidigm C1; mouse retina Drop-seq of 44,408 cells).
- **Structure:** IHC (PAX6, NKX2.1, OTX2, GBX2, VSX2, SYN1, VGAT, VGLUT1, rhodopsin); serial **electron microscopy** reconstruction and synapse/spine counting.
- **Function:** high-density silicon microelectrode extracellular recordings in intact organoids in aCSF at 36 C; pharmacology with TTX (2 uM) and NBQX (20 uM); spike sorting, cross-correlogram connectivity analysis, population-rate/burst analysis; **530 nm light stimulation** with paired firing-rate and FOS-induction readouts.

## Relevance to the brain-organoid ASD review

- **Primary use = the functional network / cell-diversity readout citation.** This is a foundational demonstration that long-term human brain organoids generate (i) endogenous-like cellular diversity at scale and (ii) **spontaneously active, synaptically connected neuronal networks** with maturation-dependent onset — exactly the "cell diversity & network dynamics (functional readouts)" theme of the review.
- Establishes the **functional-maturity timeline** the review needs: meaningful spontaneous activity appears around **8 months, not 4**, and depends on AMPA/kainate-mediated excitatory transmission — a benchmark for when functional ASD phenotypes (e.g., excitation/inhibition or network-synchrony differences) could be assayed.
- Supplies concrete **functional assay options** for a "programmable/proactive" platform: extracellular silicon-probe ephys, burst/population-dynamics analysis, and a **non-invasive sensory (light) stimulation** handle via intrinsically photosensitive cells — complementary to optogenetics.
- From the same Arlotta lab as the reproducibility paper (Velasco 2019); together they bracket two axes the review must address — **cell-type reproducibility** (Velasco) vs **functional network maturation** (this paper). The pronounced **bioreactor batch effects** here are an explicit caution for any organoid-based screening platform.
- Cross-cuts the ethics citation (Lovell-Badge 2021): demonstrates real but still-rudimentary functional maturity (spontaneous bursts, light-modulated activity), which is the empirical backdrop for the Guidelines' position that current organoids lack consciousness/sensory integration — useful for the review when discussing the provisional nature of the Category 1A exemption.

## Open questions / limitations

- **High organoid-to-organoid and bioreactor-driven variability** in which cell types form (forebrain cluster in only 32% of organoids); cell-type frequencies likely underestimated due to small per-organoid sampling and differential dissociation robustness.
- **Off-target / non-CNS cells:** retina and a mesodermal cluster arise — unguided protocol produces structures beyond the intended brain tissue.
- **Functional sampling is sparse:** spikes from only a few organoids/units; light responses in 4/10 organoids; the neuron types participating in the recorded networks were **not identified** (authors call for patch-clamp-to-transcriptome linkage).
- **Mechanism of light response unresolved** — direct photoreceptor effect vs downstream network modulation not distinguished.
- Single primary cell line (11a) for the functional/diversity claims; generalization across genetic backgrounds not tested here.
- 2017 droplet scRNA-seq depth/clustering is modest by current standards; identities rest on correlation to reference datasets rather than multi-omic confirmation.

## Related

- [Individual brain organoids reproducibly form cell diversity of the human cerebral cortex (Velasco 2019)](velasco_2019_individual_brain_organoids_reproducibly.md) — same lab; reproducibility counterpart to this functional/diversity paper.
- [Generation and long-term culture of ... organoids (Atamian 2024)](atamian_2024_generation_and_long-term_culture_of.md) — long-term-culture / extended-maturation methodology.
- [Cerebral organoids model human brain development and microcephaly (Lancaster 2013)](lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.md) — the unguided whole-brain protocol this work modifies.
- [Functional cortical neurons and astrocytes from human pluripotent stem cells (Pasca 2015)](paca_2015_functional_cortical_neurons_astrocytes_human_pluripotent_stem.md) — guided cortical-spheroid platform with complementary functional (synapse/ephys) readouts.
- [FOXG1-dependent dysregulation of GABA/glutamate neuron differentiation in ASD (Mariani 2015)](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md) — ASD organoid model on the excitatory/inhibitory axis these functional readouts could probe.
- Concept: [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- Entity: [MEA / electrophysiology readouts](../entities/mea-electrophysiology-readouts.md)
- Entity: [Calcium imaging readouts](../entities/calcium-imaging-readouts.md)
