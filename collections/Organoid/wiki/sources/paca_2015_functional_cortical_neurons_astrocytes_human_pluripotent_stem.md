---
title: "Functional cortical neurons and astrocytes from human pluripotent stem cells in 3D culture."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/nmeth.3415
pmid: 26005811
authors: Paşca AM et al.
journal: Nature methods (2015)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/paca_2015_functional_cortical_neurons_astrocytes_human_pluripotent_stem.pdf
pdf_status: downloaded
---

# Functional cortical neurons and astrocytes from human pluripotent stem cells in 3D culture.

## Source

- Authors: Paşca AM, Sloan SA, Clarke LE, Tian Y, Makinson CD, Huber N, Kim CH, Park JY et al.
- Journal: Nature methods (2015)
- DOI: [10.1038/nmeth.3415](https://doi.org/10.1038/nmeth.3415)
- PMID: [26005811](https://pubmed.ncbi.nlm.nih.gov/26005811/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

The human cerebral cortex develops through an elaborate succession of cellular events that, when disrupted, can lead to neuropsychiatric disease. The ability to reprogram somatic cells into pluripotent cells that can be differentiated in vitro provides a unique opportunity to study normal and abnormal corticogenesis. Here, we present a simple and reproducible 3D culture approach for generating a laminated cerebral cortex-like structure, named human cortical spheroids (hCSs), from pluripotent stem cells. hCSs contain neurons from both deep and superficial cortical layers and map transcriptionally to in vivo fetal development. These neurons are electrophysiologically mature, display spontaneous activity, are surrounded by nonreactive astrocytes and form functional synapses. Experiments in acute hCS slices demonstrate that cortical neurons participate in network activity and produce complex synaptic events. These 3D cultures should allow a detailed interrogation of human cortical development, function and disease, and may prove a versatile platform for generating other neuronal and glial subtypes in vitro.

## Key findings

**Headline.** Introduces **human cortical spheroids (hCSs)** — the founding **guided / region-specified 3D protocol** from the Paşca lab. Unlike unguided cerebral organoids ([Lancaster 2013](lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.md)), hCSs use **dual SMAD inhibition** to drive a single, reproducible **dorsal-telencephalon (excitatory-only) cortical** fate, and are the first 3D system to generate, in one preparation, **deep + superficial cortical neurons, spontaneously arising non-reactive astrocytes, and functional glutamatergic synapses** amenable to **acute-slice electrophysiology**.

**Defined, scaffold-free, reproducible.** Generated from **intact hiPSC colonies** (not single cells), in **floating low-attachment** culture, **no Matrigel/extracellular scaffold, no bioreactor**. **7 hiPSC lines from 5 subjects**, all worked. Patterning efficiency: by **day 18, >85% PAX6⁺**, of which **>80% FOXG1⁺** (dorsal forebrain). Reproducible within and across differentiations and across lines (Supplementary Fig. 4) — a deliberate answer to the variability of unguided organoids. Size: >300 µm by 2 weeks, up to **4.2 ± 0.3 mm by 2.5 months** (n=16, 4 lines).

**Cytoarchitecture recapitulates corticogenesis.** VZ-like proliferative zones of PAX6⁺ RG around an **N-cadherin⁺ lumen**, surrounded by **TBR2⁺ IP** (SVZ-like) zones; PH3⁺/p-VIM⁺ mitoses restricted to the luminal surface; **interkinetic nuclear migration** shown by live imaging (Lenti-GFAP::EGFP); RELN⁺ horizontal cells (marginal-zone-like) on the surface.

**Inside-out layering with correct birth order.** Layer-marker proportions tracked at days 52/76/137: deep-layer **TBR1 peaks at day 76 (40.7%±0.3)**, CTIP2 high early then declines; superficial markers (SATB2, BRN2, CUX1/2) rise **up to ~7-fold from day 52→137**; by ~day 137 deep and superficial neurons are roughly equal and **concentrically organized** (deep internal, superficial outer). **EdU birthdating** (48 h pulse at day 55, chased 3 wk): SATB2⁺ superficial neurons are EdU⁺ but TBR1⁺ deep neurons are not → superficial neurons born **later**, matching the in-vivo inside-out program. Mutually exclusive CTIP2/SATB2 co-expressed in **<3%** of cells (correct fate segregation).

**Transcriptional fidelity to mid-fetal cortex.** CoNTExT machine-learning mapping (trained on 1,340 primary samples) places **2.5-month hCSs at ~19–24 post-conception weeks (late mid-fetal)** — later/more mature than monolayer or other 3D methods of the time. Transition mapping: day 52→76 transition overlaps VZ/SVZ→IZ/SP/inner-CP transitions (−log₁₀P > 83). Up-regulated genes enriched for synaptic transmission; down-regulated for cell cycle/division.

**Spontaneous astrogenesis (no induction needed).** A neurogenesis→gliogenesis switch yields astrocytes **without** CNTF/LIF/serum: GFAP⁺ cells **2.7%±0.7 (≤day 35) → ~8% (day 76) → ~20% (day 180)**. Astrocytes are **non-reactive** in serum-free culture (thin processes, glycogen granules by EM, MAP2/GFAP intertwined by array tomography) but adopt a **reactive** polygonal phenotype + GFAP/VIM/LCN2 up-regulation when serum is added — i.e. a controllable astrocyte-reactivity readout from an isogenic background.

**Electrophysiological maturity + functional synapses.** Whole-cell patch (cells dissociated from ~130-day hCSs): **all recorded neurons (n=28, 2 clones)** show TTX-sensitive Na⁺ currents + sustained K⁺ currents; **all (n=9)** fire action potentials. Array tomography reveals **SYN1/VGLUT1 apposed to PSD-95** (glutamatergic synapses, sometimes NR2B⁺). **88.8% of neurons** show spontaneous synaptic activity, **abolished by NBQX+D-AP5** → purely glutamatergic; TTX cuts EPSC amplitude/frequency ~50% (mix of evoked + spontaneous release). **Acute hCS slices (250 µm):** 80% fire APs to current steps, 86% show spontaneous synaptic activity (reduced by kynurenic acid), and electrical stimulation evokes large EPSPs/EPSCs and spikes — i.e. an **intact, recordable human cortical micro-network**.

## Methods / Protocol

- **Cell input.** Intact hiPSC colonies enzymatically detached from feeders (Dispase), transferred to low-attachment plates in KnockOut-serum medium **without FGF2** → fold into spheres within hours. 7 hiPSC lines / 5 subjects.
- **Patterning (the key differentiator vs unguided organoids).** **Dual SMAD inhibition** from day 0 — **dorsomorphin (compound C, BMP inhibition) + SB-431542 (TGF-β inhibition)**. Day 6: switch to Neurobasal/B-27 + **FGF2 + EGF** (proliferative expansion). **Day 25:** FGF2/EGF → **BDNF + NT3** (neuronal differentiation). **Day 43 onward:** growth-factor-free Neurobasal/B-27, fed every 4 days. **No Matrigel, no spinning bioreactor.** Maintainable up to **9 months**.
- **Characterization.** Flow cytometry + cryosection IHC for staged layer markers (PAX6, FOXG1, TBR1, TBR2, CTIP2, SATB2, BRN2, CUX1/2, RELN, GFAP, NEUN, p-VIM, PH3); EdU birthdating; Lenti-GFAP::EGFP live imaging of IKNM.
- **Transcriptomics.** Bulk profiling at days 52 + 76 mapped to fetal/adult human brain with **CoNTExT** and **transition mapping** (Stein 2014 framework); RRHO against laser-capture-microdissected fetal cortical laminae. GEO: **GSE68917**.
- **Astrocyte assays.** Developmental GFAP⁺ time course (3 wk–6 mo); monolayer morphology in defined serum-free medium; serum-challenge reactivity test; **array tomography** (70 nm serial sections) and TEM (glycogen granules).
- **Electrophysiology.** Fura-2 / Fluo-4 calcium imaging; whole-cell patch clamp (voltage- and current-clamp) on dissociated neurons; **acute 250-µm hCS slice** recordings with extracellular stimulation; pharmacology = TTX, NBQX, D-AP5, kynurenic acid; biocytin fills for morphology.

## Relevance to the brain-organoid ASD review

Supports the manuscript *"Programmable Brain Organoids for Proactive Autism Genetics."*

- **Anchors the "guided cortical spheroid" platform branch.** This is the canonical reference for **region-specified, reproducible, scaffold-free dorsal-cortical 3D culture** — the methodological counterpoint to unguided cerebral organoids in the review's platform taxonomy (unguided / guided / assembloid). It is also the **direct precursor to the assembloid program**: hCSs (dorsal) + ventral spheroids are later fused into forebrain assembloids in [Birey 2017](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md) and [Sloan 2018](sloan_2018_generation_and_assembly_of_human.md) from the same lab.
- **Backs the reproducibility advantage that makes "proactive/programmable" screening feasible.** Because hCSs reproducibly produce a defined cortical fate across lines and differentiations (>85% PAX6⁺/>80% FOXG1⁺), they are a controlled substrate for isogenic disease modelling — exactly the property [Velasco 2019](velasco_2019_individual_brain_organoids_reproducibly.md) and [Yoon 2019](yoon_2019_reliability_of_human_cortical.md) later formalize as a prerequisite for detecting genotype-specific phenotypes. Cite for "guided protocols trade some regional diversity for the reproducibility needed to read out subtle ASD effects."
- **Establishes the functional-readout toolkit the review depends on.** hCSs are the system that made **human cortical electrophysiology in 3D** routine: spontaneous activity (calcium imaging), patch-clamp maturity, glutamatergic synapses, and **acute-slice network recordings**. These are precisely the late-stage **functional readouts** the review proposes as shared end-point assays — e.g. the calcium-imaging / network-burst phenotypes used in ASD-gene organoid studies like [Paulsen 2022](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md).
- **Provides isogenic human astrocytes inside the cortical model.** Astrocytes arise spontaneously from the same genetic background and can be pushed to a reactive state — relevant to any ASD mechanism (or screen readout) involving glia / neuron-glia interactions, and to the review's argument that organoids capture non-neuronal contributions.
- **Defines the maturation ceiling.** Mapping to ~19–24 PCW sets the realistic developmental window organoids occupy — useful for the review's "fidelity / limits" framing of *when* in development organoid ASD phenotypes are read.

### Related pages
- [Birey 2017](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md), [Sloan 2018](sloan_2018_generation_and_assembly_of_human.md) — hCS-derived forebrain assembloids and astrocyte maturation; the direct lineage of this protocol.
- [Lancaster 2013](lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.md) — the unguided counterpart; contrast guided-vs-unguided.
- [Paulsen 2022](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) — uses guided cortical organoids + calcium imaging/MEA for ASD-gene phenotyping (the functional-readout lineage).
- [Yoon 2019](yoon_2019_reliability_of_human_cortical.md), [Velasco 2019](velasco_2019_individual_brain_organoids_reproducibly.md) — reproducibility/reliability benchmarks for guided cortical organoids.
- Concept: [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md); entity: [Calcium imaging readouts](../entities/calcium-imaging-readouts.md).

## Open questions / limitations

- **Dorsal-only by design.** hCSs generate **excitatory neurons of the dorsal telencephalon** exclusively — **no interneurons, no ventral/GABAergic populations** in a single spheroid. Interrogating excitatory-inhibitory balance (central to ASD) requires fusing with separately patterned ventral spheroids (the later assembloid work), so this paper alone cannot model E/I circuits.
- **Maturation plateau (~mid-fetal).** Transcriptionally caps at ~19–24 PCW; later cortical maturation, full layer II–VI architecture, and adult-like circuitry are not reached on these timescales.
- **No vasculature, no microglia, limited cell-type breadth.** As an iPSC-intrinsic system it lacks mesodermal/immune lineages; long-term metabolic support is unaddressed here.
- **Functional data from few lines.** Electrophysiology/synapse quantification rests on neurons from **two hiPSC clones**; network-level claims, while strong, are not yet line-broad.
- **Method paper, not a disease study.** Demonstrates the platform's capabilities (development, function) but does not itself apply a disease genotype — its ASD-relevance is as the enabling guided platform + readout suite, realized in later studies.
