---
title: "Cerebral organoids at the air-liquid interface generate diverse nerve tracts with functional output."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41593-019-0350-2
pmid: 30886407
authors: Giandomenico SL et al.
journal: Nature neuroscience (2019)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/giandomenico_2019_cerebral_organoids_at_air_liquid_interface_generate.pdf
pdf_status: downloaded
---

# Cerebral organoids at the air-liquid interface generate diverse nerve tracts with functional output.

## Source

- Authors: Giandomenico SL, Mierau SB, Gibbons GM, Wenger LMD, Masullo L, Sit T, Sutcliffe M, Boulanger J et al.
- Journal: Nature neuroscience (2019)
- DOI: [10.1038/s41593-019-0350-2](https://doi.org/10.1038/s41593-019-0350-2)
- PMID: [30886407](https://pubmed.ncbi.nlm.nih.gov/30886407/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Neural organoids have the potential to improve our understanding of human brain development and neurological disorders. However, it remains to be seen whether these tissues can model circuit formation with functional neuronal output. Here we have adapted air-liquid interface culture to cerebral organoids, leading to improved neuronal survival and axon outgrowth. The resulting thick axon tracts display various morphologies, including long-range projection within and away from the organoid, growth-cone turning, and decussation. Single-cell RNA sequencing reveals various cortical neuronal identities, and retrograde tracing demonstrates tract morphologies that match proper molecular identities. These cultures exhibit active neuronal networks, and subcortical projecting tracts can innervate mouse spinal cord explants and evoke contractions of adjacent muscle in a manner dependent on intact organoid-derived innervating tracts. Overall, these results reveal a remarkable self-organization of corticofugal and callosal tracts with a functional output, providing new opportunities to examine relevant aspects of human CNS development and disease.

## Key findings

- **The advance is a culture-format change, not a new differentiation protocol: existing cerebral organoids are sliced (300 µm) and grown at the air-liquid interface (ALI-COs).** The starting tissue is the authors' guided enCOR organoid (forebrain-biased, with a proper cortical plate); slicing happens only *after* cortical-plate establishment (~day 55-60, in some cases up to day 90), so morphogenesis precedes ALI culture. The method is deliberately analogous to classic organotypic slice culture of mid-neurogenesis fetal cortex.
- **ALI culture markedly improves neuronal survival and morphology versus whole organoids.** TUNEL+ cell death is significantly lower in ALI-COs (**P = 0.0022, two-tailed Mann-Whitney, n = 6 vs 6). Whole organoids lose neurons and accumulate reactive astrocytes along the surface, whereas ALI-COs retain abundant healthy neurons and astrocytes with finer processes. Cultures stay healthy for **up to one year** (tested to ~365 d under ALI conditions).
- **Increased and better-aligned axons + more cortical neurons.** SMI312+ axon staining is higher in ALI-COs (**P = 0.0022) and more directionally aligned (OrientationJ energy x coherency, **P = 0.0022). Deep-layer CTIP2+ and upper-layer CUX2+ neuron counts are both higher (CTIP2 **P = 0.0022; CUX2 *P = 0.0411), with a particularly strong effect on deep-layer neurons.
- **Neurons reach mature morphology and are electrically active.** Sparse GFP labeling shows radially aligned cortical-plate pyramidal neurons with complex dendrites and dendritic spines (increasingly elaborate out to 1 year), plus pre/post-synaptic puncta and GABAergic interneurons/synapses. MEA recordings show spontaneous activity blocked by TTX; whole-cell patch-clamp shows trains of action potentials on current injection (F-I curve, n = 13 cells from 7 ALI-COs).
- **Axon tracts self-organize with diverse, in-vivo-like morphologies and respond to endogenous guidance cues.** Long-term live imaging captures pioneer-like dynamic outgrowth (with retractions) maturing into faster, directional, bundled growth; tracts project locally, across the organoid, and *away* from it, and show growth-cone turning and decussation. SMI312/NRP1 staining marks intracortical and developing-corpus-callosum (NRP1+) tracts; tracts associate with endogenous guidance foci — WNT5A (glial-wedge-like), RYK, EphrinB1, and Netrin-1 (tracts orient toward Netrin-1 signal).
- **scRNA-seq resolves the full cortical-neuron repertoire matched to projection behavior.** 13,280 cells from six slices of three ALI-COs (~4,427 cells/sample, 10x) gave 6 clusters: subcortical-projection neurons (C1: CTIP2, FEZF2), upper-layer/callosal IPC-overlapping neurons (C2: SATB2, EOMES), VZ/SVZ radial glia (C3: GFAP, FAM107A), more mature upper/deep neurons (C4: FOXP2, CUX2), interneurons (C5: DLX2), and actively dividing progenitors (C6: CENPE, EOMES). Axon-outgrowth genes (L1CAM, NRN1) enriched in C1-C2; maturity/synapse genes (VGLUT2, CNTNAP2, SYT4) in C4.
- **Tract morphology matches molecular identity (retrograde tracing).** CTB back-labeling: internal tracts trace to **91.1 ± 11.0%** callosal CUX2-single-positive neurons; "escaping" tracts trace mostly to subcortical identities (**65.4 ± 24.3%** CTIP2+; 20.6 ± 6.4% CTIP2-single-positive vs 1.1 ± 1.5% for internal tracts).
- **Functional output — the headline result.** 3D MEA recordings show network bursts and spatially structured connectivity (peak high-correlation at ~400 µm, beyond the 200 µm inter-electrode spacing, i.e. not mere nearest-neighbor). Co-culture of ALI-COs with embryonic-mouse spinal-cord-muscle explants: human tracts innervate the cord, form human-presynaptic (SYP)/mouse-postsynaptic (PSD95) synapses, and drive **coordinated, high-amplitude muscle contractions**. Contractions are intensity-graded, drivable at up to 1 Hz, abolished by TTX (restored on washout), and abolished by axotomy of the ALI-CO tract — demonstrating specificity. Stimulus-to-contraction latency ~37 ms (±17 ms frame interval), close to the developing human descending motor pathway and consistent with a polysynaptic circuit.

## Methods

- **System:** enCOR cerebral organoids from H9 (female; default) and H1 (male) human ESCs; 18,000 cells plated with PLGA microfilaments, Matrigel-supplemented from d35-40 to build the cortical plate; sparse/targeted labeling by ventricular injection + electroporation (fGFP/Sendai-emGFP/fFusionRed) between d40-60.
- **ALI-CO preparation:** mature organoids embedded in 3% low-gelling agarose, vibratome-cut to **300 µm**, placed on Millicell-CM inserts; equilibrated in serum-containing slice medium then switched to serum-free Neurobasal/B-27 medium; medium added only *below* the insert so slices sit at the air-liquid interface (daily media changes, 37 °C / 5% CO2).
- **Readouts:** confocal live imaging (10-min intervals, hours to days; OrientationJ for tract alignment, MTrackJ for growth cones, kymographs); IHC for SMI312/MAP2, layer markers (CTIP2, CUX2, FEZF2, BRN2, SATB2, SOX5), guidance cues (WNT5A, RYK, EphrinB1, Netrin-1), corpus-callosum marker NRP1; TUNEL; 10x scRNA-seq with tSNE/GO/pseudotime; CTB retrograde tracing; 3D/standard MEA (spike-time tiling coefficient for connectivity); whole-cell patch-clamp; ALI-CO + embryonic mouse spinal-cord-muscle explant co-culture with extracellular stimulation, axotomy, and TTX wash-in/washout; muscle contraction measured as displacement.
- **Statistics:** two-tailed Mann-Whitney for two-group comparisons; most key contrasts at n = 6 per group from ≥2 independent batches.

## Relevance to the brain-organoid ASD review

- **Primary citation for the "air-liquid interface (improved survival / axon outgrowth)" advanced-platform theme.** This is the originating ALI-CO paper: it concretely documents the survival gain (lower TUNEL, healthier glia, 1-year viability) and the extensive aligned axon-tract outgrowth that the review invokes as gap-filling for diffusion-limited whole organoids.
- **Connectivity + functional output is the unique selling point for an ASD circuit argument.** The review frames ASD partly as a connectivity/E-I-balance disorder; ALI-COs supply a human in-vitro system with self-organizing callosal (NRP1/CUX2) and corticofugal (CTIP2/FEZF2) tracts, active networks, and a measurable motor output (muscle contraction) — i.e. input *and* output on a tractable, scalable, fully in-vitro platform (contrast the "tedious, specialist" transplantation route the authors explicitly position against).
- **The authors themselves name the disease space:** they propose ALI-COs for modeling corpus-callosum neurodevelopmental conditions, epilepsy-type circuit imbalance, and explicitly **autism and schizophrenia**, plus axon-tract injury/degeneration — directly supporting the review's clinical-relevance framing.
- **Complements the other advanced platforms in the corpus:** ECM/microfluidic maturation ([Cho 2021](cho_2021_microfluidic_device_brain_extracellular_matrix_promotes_structural.md)) and in-vivo vascularization/transplantation ([Mansour 2018](mansour_2018_vivo_model_functional_vascularized_human_brain_organoids.md), [Revah 2022](revah_2022_maturation_circuit_integration_transplanted_human_cortical_organoids.md)) tackle the same survival/maturation bottleneck by different means; ALI is the slice-based, imaging- and circuit-friendly option.
- **Enables tract-level perturbation read-outs** (tractotomy, stimulation, retrograde tracing) that pair naturally with the review's programmable-perturbation thesis once disease genotypes are introduced.

## Open questions / limitations

- **Slicing sacrifices 3D whole-tissue and laminar context.** Because organoids are cut into 300 µm sections, the intact 3D architecture and full cortical-layer organization are not preserved — a caveat noted by [Cho 2021](cho_2021_microfluidic_device_brain_extracellular_matrix_promotes_structural.md) when contrasting ALI-COs with whole-organoid maturation approaches.
- **No vasculature; survival is improved but still diffusion-dependent.** ALI improves oxygen/nutrient access at the cut surface rather than providing perfusion or a blood supply; the approach is explicitly an in-vitro alternative to (not a replacement for) vascularization/transplantation.
- **Functional output is shown via a xenogeneic mouse spinal-cord-muscle co-culture, not an all-human motor circuit;** physiological fidelity of the human-to-mouse synapse and circuit is inferred from latency similarity, not proven to recapitulate human descending-pathway function.
- **Maturity is still developmental/fetal-stage** (e.g. upper-layer neurons overlap with progenitor identity, suggesting many are immature at the 69-75 d window sampled); long-term lamination, full glial/oligodendrocyte maturation, and disease-genotype phenotypes were not assayed here.
- **Throughput and quantitative rigor of live-tract analyses** rest on modest sample numbers (many n = 6, some imaging analyses on 2-7 organoids); batch/line generalization beyond H9/H1 enCOR organoids is not established in this paper.

## Related

- [Cho 2021 — Microfluidic device + brain ECM promotes structural/functional maturation](cho_2021_microfluidic_device_brain_extracellular_matrix_promotes_structural.md)
- [Eichmüller 2022 — Human cerebral organoids for clinical neurology (review; cites ALI-COs)](eichmller_2022_human_cerebral_organoids_new_tool_clinical_neurology.md)
- [Giandomenico 2021 — Generation and long-term culture of advanced (ALI) cerebral organoids (companion protocol)](giandomenico_2021_generation_and_long-term_culture_of.md)
- [Lancaster 2013 — Cerebral organoids model human brain development and microcephaly (founding protocol)](lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.md)
- [Lancaster 2014 — Generation of cerebral organoids from human PSCs](lancaster_2014_generation_of_cerebral_organoids_from.md)
- [Mansour 2018 — In vivo model of functional and vascularized human brain organoids](mansour_2018_vivo_model_functional_vascularized_human_brain_organoids.md)
- [Quadrato 2017 — Cell diversity and network dynamics in photosensitive human brain organoids](quadrato_2017_cell_diversity_network_dynamics_photosensitive_human_brain.md)
- Concept: [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- Concept: [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
