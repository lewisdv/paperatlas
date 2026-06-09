---
title: "Xenotransplanted Human Cortical Neurons Reveal Species-Specific Development and Functional Integration into Mouse Visual Circuits."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.neuron.2019.10.002
pmid: 31761708
authors: Linaro D et al.
journal: Neuron (2019)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Xenotransplanted Human Cortical Neurons Reveal Species-Specific Development and Functional Integration into Mouse Visual Circuits.

## Source

- Authors: Linaro D, Vermaercke B, Iwata R, Ramaswamy A, Libé-Philippot B, Boubakar L, Davis BA, Wierda K et al. (senior authors Vincent Bonin, Pierre Vanderhaeghen)
- Journal: Neuron 104, 972–986 (December 4, 2019)
- DOI: [10.1016/j.neuron.2019.10.002](https://doi.org/10.1016/j.neuron.2019.10.002)
- PMID: [31761708](https://pubmed.ncbi.nlm.nih.gov/31761708/)
- Open access (CC BY-NC-ND)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

How neural circuits develop in the human brain has remained almost impossible to study at the neuronal level. Here, we investigate human cortical neuron development, plasticity, and function using a mouse/human chimera model in which xenotransplanted human cortical pyramidal neurons integrate as single cells into the mouse cortex. Combined neuronal tracing, electrophysiology, and in vivo structural and functional imaging of the transplanted cells reveal a coordinated developmental roadmap recapitulating key milestones of human cortical neuron development. The human neurons display a prolonged developmental timeline, indicating the neuron-intrinsic retention of juvenile properties as an important component of human brain neoteny. Following maturation, human neurons in the visual cortex display tuned, decorrelated responses to visual stimuli, like mouse neurons, demonstrating their capacity for physiological synaptic integration in host cortical circuits. These findings provide new insights into human neuronal development and open novel avenues for the study of human neuronal function and disease. VIDEO ABSTRACT.

## Key findings

- **Single-cell integration model.** Human ESC-derived cortical cells were injected intraventricularly into neonatal (P0/P1) mouse lateral ventricles in the presence of EGTA, yielding dispersed single-cell integration rather than the poorly integrated "lumps" of conventional compact grafts. Cells were tracked from 2 weeks to **11 months post-transplantation (MPT)**.
- **No fusion, no contamination.** 0/40 GFP/tdTomato double-positive cells (n=2 animals) → no transplant-to-host fusion; scRNA-seq found no detectable mouse reads in any human cell (n=10,698 cells, n=2 animals).
- **Pyramidal identity, layer position.** Transplanted cells were exclusively pyramidal: 0/19 glial-marker+, 0/27 GABAergic. >60% expressed deep-layer markers (FoxP2/CTIP2), located mainly in L5/6; a minority expressed upper-layer Cux1 (found only in L2/3). Only partial coupling between layer identity and position.
- **Host connectivity.** Monosynaptic rabies tracing at 4 MPT: TVA+/GFP+ human "starter" neurons surrounded by retrogradely labeled host mouse cortical neurons → significant host→graft connectivity.
- **Protracted physiological maturation (the central result).** Ex vivo patch-clamp from 1–11 MPT showed progressive maturation: at 1 MPT immature (low-amplitude APs, rapidly adapting firing); by 10 MPT sustained firing with mature-looking APs resembling adult human pyramidal neurons. Maturation included membrane hyperpolarization, decreased input resistance, increased max Na+ current, AP half-width shortening, decreased spontaneous firing (no spontaneously firing cells after 6 MPT), and rising rate of spontaneous EPSCs. **Contrast: mouse neurons transplanted into mouse cortex mature in only a few weeks**; host mouse L5 cells in transplanted animals were mature at 6 weeks (so the slow timeline is intrinsic to the human cells, not a delayed-host artifact).
- **Method-independent neoteny.** Prolonged maturation reproduced with an alternative in vitro corticogenesis protocol (Shi et al., 2012) → independent of differentiation/transplantation method.
- **Morphological maturation.** 28 biocytin-filled neurons reconstructed; pronounced increases in dendritic length/complexity (Sholl) and spine density over 1–7 MPT, with a marked separation between cells before 4 MPT and after 5 MPT; morphology strongly correlated with functional maturation (Spearman ρ reported, e.g., dendritic length vs resting Vm ρ = −0.731, p < 10⁻⁴; spine density vs Vm ρ = −0.445, p < 0.05).
- **Human-like spine morphology.** At 10 MPT, human spine head diameters and neck lengths exceeded host mouse (5-week) spines and fell in the range reported for human cortex (Benavides-Piccione 2002); spine density at 10 MPT still **lower** than adult mouse L5, consistent with incomplete (neotenic) maturation.
- **Juvenile-like spine dynamics in an adult host.** In vivo 2-photon imaging through a cranial window (n=5 animals, imaged at 1–2 week intervals up to ~12–15 weeks, cohorts starting at 3 or 7 MPT): spine density rose up to 10–12 MPT to values reported for human neurons at 1–2 years of age; spine turnover ratio high at 3–6 MPT then decreased at 7–10 MPT; spine survival lengthened from ~2 weeks (3–6 MPT) to ~8 weeks (7–11 MPT). Human spines stayed dynamic in an otherwise mature mouse brain → strong evidence neoteny is cell-intrinsic, not an artifact.
- **Functional synaptic plasticity.** Ex vivo LTP (pairing protocol) in human cells aged 3–6 MPT: ~two-thirds showed LTP lasting >30 min (n=7/10); mouse L5 cells in 3-month-old mice also showed LTP but smaller magnitude.
- **Sensory integration in visual cortex (in vivo Ca²⁺ imaging).** Human neurons engineered with doxycycline-inducible GCaMP6s + nuclear dTomato, imaged in L2/3 (100–300 µm) at 5–9 MPT; 155 human neurons across 5 animals. With drifting gratings, 35% (55/155) showed Ca²⁺ activity; visual stimulation raised transient rate and amplitude. **~25% (38/155) were clearly visually responsive**, i.e., 69% (38/55) of active cells. Activity was highly **decorrelated** across cell pairs (independent firing) — unlike the hypersynchronous activity of in vitro organoids.
- **Tuned responses resembling host neurons.** Human cells showed orientation/direction tuning (median OSI = 0.36, DSI = 0.25); 60%/78% of visually responsive cells tuned for orientation/direction (OSI/DSI > 0.2), similar to mouse neurons. Human cells showed weaker orientation selectivity than mouse (consistent with still-maturing circuitry) but comparable direction selectivity. Host mouse tuning in transplanted vs control animals was unchanged → transplantation did not overtly disrupt host circuitry.

## Methods

- **Model:** mouse/human chimera. Human ESC-derived cortical pyramidal neurons, lentivirally labeled (GFP, TVA-mCherry, GCaMP6s), injected intraventricularly into neonatal (P0/P1) mouse brain with EGTA to promote single-cell dispersal/integration.
- **Time course:** 6 h to 11 MPT.
- **Assays:** confocal immunostaining (layer markers); scRNA-seq of transplanted cells (purity/fusion check); ex vivo whole-cell patch-clamp (intrinsic properties, F-I curves, spontaneous activity, EPSCs); biocytin fills + 3D reconstruction + Sholl analysis (morphology); rabies-virus monosynaptic retrograde tracing (TVA + glycoprotein expressed in vitro 2 weeks pre-transplant to avoid host infection; GFP-rabies injected at 4 MPT); chronic in vivo 2-photon imaging of spine dynamics; ex vivo LTP (pairing paradigm); in vivo 2-photon Ca²⁺ imaging in awake head-fixed mice with drifting-grating visual stimulation.
- **Stats:** Welch's one-way ANOVA with Games-Howell post hoc; Kolmogorov-Smirnov for distributions; Spearman rank correlation for morphology-function relations.

## Relevance to the brain-organoid ASD review

- **Host-integration and species-specific maturation validation.** This is the manuscript's evidence that human cortical neurons retain a **months-to-years, cell-intrinsic maturation clock** even when placed in a fast-maturing mouse host — the cellular basis of human cortical *neoteny*. It anchors the review's argument that organoid/transplant "maturation timeline" reflects an intrinsic human program, not merely culture limitations.
- **Single-cell vs bulk transplantation matters.** Linaro shows that dispersed single-cell integration achieves far greater maturation and host connectivity than compact/bulk grafts (explicit contrast with Real et al. 2018: spine half-life <4 days and very limited connectivity in bulk grafts). Methodologically relevant when the review weighs xenotransplantation as a maturation/validation strategy for ASD organoid models.
- **Functional readout of host integration.** Decorrelated, tuned visual responses demonstrate that single human neurons can be physiologically recruited into an adult host circuit — a benchmark for what "functional integration" of human neurons looks like, contrasting with the hypersynchronous activity of standalone organoids (Trujillo 2019, Mansour 2018).
- **Caveats the review should carry forward:** only ~25% of cells were visually responsive; spine density still sub-adult at 10 MPT; authors concede xenotransplantation may itself be a suboptimal environment, and note chimpanzee neurons mature faster than human in the same assay (Marchetto et al., 2019) — i.e., the neotenic clock is species-graded.

## Open questions / limitations

- Only a **25% minority** of human neurons were visually responsive; cause unresolved (still-low connectivity/spine density, possible E/I imbalance, or improper wiring).
- Neurons had **not** reached adult human maturity (smaller somata/arbors, sub-adult spine density at 10 MPT; spine pruning, which lasts >a decade in vivo, not yet engaged).
- Authors explicitly allow that **part** of the prolonged timeline could reflect a suboptimal xenotransplant environment rather than pure intrinsic program (mitigated but not eliminated by the mature-host control).
- Host presynaptic partners driving human responses (thalamic vs cortical) not identified.
- Whether neurons given even longer in vivo time acquire further species-specific adult properties (e.g., enhanced information transmission) untested.
- Translational extrapolation to repair of *damaged/adult lesioned* cortex (vs neonatal transplantation here) remains to be demonstrated.

## Related

- [mansour_2018](mansour_2018_vivo_model_functional_vascularized_human_brain_organoids.md) — in vivo engraftment of whole human brain organoids into mouse (vascularization/integration); complementary transplantation approach with more synchronous activity.
- [host-context-transplantation-and-repair-validation](../concepts/host-context-transplantation-and-repair-validation.md)
- [host-circuit-engagement](../entities/host-circuit-engagement.md)
- [organoid-functional-assays-transplantation-and-coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [calcium-imaging-readouts](../entities/calcium-imaging-readouts.md)
