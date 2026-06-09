---
title: "Comparison of induced neurons reveals slower structural and functional maturation in humans than in apes."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.7554/elife.59323
pmid: 33470930
authors: Schörnig M et al.
journal: eLife (2021)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Comparison of induced neurons reveals slower structural and functional maturation in humans than in apes.

## Source

- Authors: Schörnig M, Ju X (co-first), Fast L, Ebert S, Weigert A, Kanton S, Schaffer T, Nadif Kasri N, Treutlein B, Peter BM, Hevers W, Taverna E (corresponding).
- Journal: eLife (2021) 10:e59323. Received 26 May 2020; accepted 19 Jan 2021; published 20 Jan 2021.
- DOI: [10.7554/elife.59323](https://doi.org/10.7554/elife.59323)
- PMID: [33470930](https://pubmed.ncbi.nlm.nih.gov/33470930/)
- Lab: Elena Taverna, Max Planck Institute for Evolutionary Anthropology, Leipzig.
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

We generated induced excitatory neurons (iNeurons, iNs) from chimpanzee, bonobo, and human stem cells by expressing the transcription factor neurogenin-2 (NGN2). Single-cell RNA sequencing showed that genes involved in dendrite and synapse development are expressed earlier during iNs maturation in the chimpanzee and bonobo than the human cells. In accordance, during the first 2 weeks of differentiation, chimpanzee and bonobo iNs showed repetitive action potentials and more spontaneous excitatory activity than human iNs, and extended neurites of higher total length. However, the axons of human iNs were slightly longer at 5 weeks of differentiation. The timing of the establishment of neuronal polarity did not differ between the species. Chimpanzee, bonobo, and human neurites eventually reached the same level of structural complexity. Thus, human iNs develop slower than chimpanzee and bonobo iNs, and this difference in timing likely depends on functions downstream of NGN2.

## Key findings

Core claim: **human induced neurons mature slower than ape (chimpanzee + bonobo) iNs across transcriptional, morphological, and functional axes**, and the delay is a **cell-intrinsic** property of human neurons (the NGN2 direct-conversion system uncouples neuronal maturation from cell-cycle/progenitor dynamics). "Ape" = pooled chimpanzee + bonobo throughout.

- **Transcriptional heterochrony (scRNA-seq).** Genes for dendrite development (GO:0016358) and dendrite morphogenesis (GO:0048813) are enriched from **d5 in apes but not in humans** (*p* < 0.05, binomial). Synapse organization (GO:0050808) enriched from **d5 in apes vs only from d14 in humans**. Ion transmembrane transport (GO:0034220) enriched from d14 in apes but **not even by d35 in humans** (*p* > 0.33). SynGO analysis agrees: synaptic-organization / presynaptic / trans-synaptic genes start at d5 in apes vs d14–d28 in humans; most post-synaptic / trans-synaptic gene groups are not enriched in human iNs at any time point examined while enriched in apes from d14 on (core-synaptic genes become enriched in humans only at d35). Differences are largest at early time points.
- **Functional heterochrony — action potentials (patch clamp, n = 144 ape / 156 human iNs).** Single APs appear as early as d2 in both species. **Ape iNs sustain repetitive APs robustly already at d14–16; human iNs fire mainly single APs until ~d21**, acquiring repetitive firing only afterward (two-way ANOVA: *p*day = 1.98E-24, *p*spec = 2.96E-6). Sodium/potassium/calcium channel mRNAs are expressed in both species with no species-specific difference — so the AP delay is not explained by channel-gene expression.
- **Functional heterochrony — spontaneous synaptic activity (n = 132 ape / 135 human iNs).** Spontaneous excitatory postsynaptic currents (sEPSCs; verified glutamatergic with kynurenic acid) appear in **ape iNs after 2–3 weeks**; the **majority of human iNs are silent at those times**, becoming frequent only after **3–4 weeks** (two-way ANOVA *p*spec = 0.0035). No spontaneous activity before d14 in either species.
- **Morphological heterochrony.** At **d7 and d14, ape iNs have larger total neurite length** (multipolar: *p*d7 = 0.0098, *p*d14 = 0.0215; bipolar: *p*d7 = 0.0278, *p*d14 < 0.001) and more Sholl intersections at d14 (multipolar *p* = 0.0469; bipolar *p* < 0.001). By **d21 and d35 these differences vanish** — neurites reach the same structural complexity. Notably, **human multipolar axons are slightly LONGER than ape at d35** (*p* = 0.0094), a reversal consistent with protracted human growth.
- **What does NOT differ between species (controls for the heterochrony claim):** timing of axo-dendritic polarity establishment (~d7 in both); resting membrane potential; onset of voltage-gated-channel expression; overall final structural complexity. So the species difference is specifically in the *timing/dynamics* of maturation, not in the endpoint or in basic neuronal identity.
- **Passive electrical properties:** time constant τ = R·C stable at ~16 ms (ape 17.4 ms, human 15.3 ms); cell capacitance lower in humans (slightly but significantly, *p*spec = 0.02), with ape > human mainly at d14–16. Consistent with slightly less-mature human cells early on.
- **Unexpected fate result:** NGN2 induces **heterogeneous but cross-species-similar fates** — predominantly cortical neurons (90% CUX1⁺, 50–60% BRN2⁺; TBR1⁻) AND a large **sensory-neuron (nociceptive) population** (PRPH, NTRK2/TRKB, POU4F1/BRN3A, PHOX2B, ISL1, SCN9A/Nav1.7, FGF13). Authors conclude many iNs are "cortical sensory neurons." ~47% ape / 39% human iNs express VGLUT2 (glutamatergic); GABAergic markers absent. The same populations occur in both species, supporting that heterochrony is a general feature rather than a fate artifact. Forebrain marker FOXG1 was absent.

## Methods

- **Direct conversion (iNeuron) system:** forced expression of mouse **NGN2** (doxycycline-inducible, Tet-On) in PSCs converts them directly to excitatory neurons, **bypassing neural-progenitor proliferation/cell-cycle** — the key design choice that isolates cell-intrinsic maturation differences.
- **Cell lines:** 3 chimpanzee iPSC (SandraA, JoC, ciPS01), 1 bonobo iPSC (BmRNA), 3 human iPSC (409B2, SC102A-1, HmRNA), 1 human ESC (H9). scRNA-seq + morphology on a subset (2 chimp, 1 bonobo, 3 human); electrophysiology on all 8 lines.
- **Readouts & timeline (up to 8 weeks):** scRNA-seq (10x Genomics) at d5/d14/d28/d35 (10,111 ape + 25,923 human cells retained; 8 clusters: dividing NP, NP, intermediate, fibroblasts, and 4 neuronal subtypes incl. TAC1⁺, SSTR2⁺/GAL⁺, PIEZO2⁺/GAL⁺ sensory neurons); whole-cell patch-clamp current-clamp (APs) and voltage-clamp (sEPSCs); GFP sparse-labeling + Imaris tracing for morphology (Sholl, neurite/axon length) at d7/d14/d21/d35; IHC for cortical/sensory markers.
- **Statistics:** Mann–Whitney U (morphology), two-way ANOVA (electrophysiology, with *p*day / *p*spec / *p*day×spec), unpaired *t*-test (with Welch correction for sEPSCs), binomial test (GO enrichment), Fisher exact (SynGO). Significance: *p* < 0.05/0.01/0.001 = */**/***.
- **Resource:** "iNeuronExplorer" ShinyApp browser for the scRNA-seq data.

## Relevance to the brain-organoid ASD review

Supports the review theme **"human-specific protracted neuronal maturation" (maturation heterochrony)**. For "Programmable Brain Organoids for Proactive Autism Genetics":

- Provides **clean, reductionist evidence that protracted human neuronal maturation is cell-intrinsic** — it persists even when progenitor proliferation, migration, and tissue context are removed (NGN2 iNs). This strengthens the argument that organoid/iN models recapitulate a genuine human-specific developmental property rather than a culture artifact.
- Establishes **concrete quantitative timing anchors** (repetitive APs: ape d14–16 vs human ~d21; sEPSCs: ape 2–3 wk vs human 3–4 wk; synaptic-gene onset: ape d5 vs human d14+) that the review can cite for "how much slower" human neurons mature.
- Methodologically relevant: shows **iN direct conversion as a fast, controllable complement to organoids** for dissecting maturation phenotypes — useful for high-throughput readouts of ASD-gene effects on maturation tempo, a phenotype class poorly captured by proliferation-based organoid screens (cf. Esk 2020).
- Mechanistic pointer: authors propose the delay is driven by **functions downstream of NGN2**, with an early *transcriptional* driver and a later *post-transcriptional/translational* driver; they flag the human-specific **SRGAP2C** duplication as a candidate neoteny gene. Relevant to ASD because synaptic timing/SRGAP2 biology intersects ASD-risk pathways.
- Caveat for the review: the dominant readout cell type is **cortical/sensory excitatory neurons**, not a forebrain-circuit model, and there is **no autism-gene perturbation** here — the relevance is the *phenotype/heterochrony framework*, not direct ASD genetics.

## Open questions / limitations

- **No autism genes tested**; the paper characterizes baseline human-vs-ape maturation tempo only.
- **iNs are heterogeneous and largely sensory/cortical**, FOXG1⁻ — i.e. not a forebrain-specific or circuit-level model; generalization to disease-relevant forebrain neurons is by analogy.
- The proposed **early-transcriptional vs late-post-transcriptional two-driver mechanism is a hypothesis**, explicitly untested in this study; candidate genes (e.g. SRGAP2C) are suggested, not demonstrated here.
- **Limited cell lines per species** (one bonobo line; small per-species n for some assays); donor/line and reprogramming-method variation could contribute.
- mouse NGN2 over-expression imposes an artificial, synchronous differentiation that may not mirror endogenous human neurogenesis tempo; the system trades physiological context for the ability to isolate cell-intrinsic timing.
- Functional and transcriptional differences are largest **early** and partly converge by d21–d35; whether the early delay has lasting circuit consequences is left open (authors speculate longer human axons enable longer-range connectivity).

## Related

- [Benito-Kwiecinski 2021](benitokwiecinski_2021_early_cell_shape_transition_drives_evolutionary_expansion.md) — complementary human-specific developmental-timing story acting *earlier* (NE→RG progenitor transition) rather than at neuronal maturation; both ingested for this review.
- Kanton et al. 2019 (great-ape cerebral organoid scRNA-seq atlas; co-author Kanton) — organ-level counterpart showing slower human neuronal gene-expression maturation (cited; not yet a wiki page).
- See collection [index](../index.md) for other human-specific cortical-development sources (Pollen 2015 oRG identity, Camp 2015 organoid–fetal concordance).
