---
title: "Cerebral organoids model human brain development and microcephaly."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/nature12517
pmid: 23995685
authors: Lancaster MA et al.
journal: Nature (2013)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.pdf
pdf_status: downloaded
---

# Cerebral organoids model human brain development and microcephaly.

## Source

- Authors: Lancaster MA, Renner M, Martin CA, Wenzel D, Bicknell LS, Hurles ME, Homfray T, Penninger JM et al.
- Journal: Nature (2013)
- DOI: [10.1038/nature12517](https://doi.org/10.1038/nature12517)
- PMID: [23995685](https://pubmed.ncbi.nlm.nih.gov/23995685/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

The complexity of the human brain has made it difficult to study many brain disorders in model organisms, highlighting the need for an in vitro model of human brain development. Here we have developed a human pluripotent stem cell-derived three-dimensional organoid culture system, termed cerebral organoids, that develop various discrete, although interdependent, brain regions. These include a cerebral cortex containing progenitor populations that organize and produce mature cortical neuron subtypes. Furthermore, cerebral organoids are shown to recapitulate features of human cortical development, namely characteristic progenitor zone organization with abundant outer radial glial stem cells. Finally, we use RNA interference and patient-specific induced pluripotent stem cells to model microcephaly, a disorder that has been difficult to recapitulate in mice. We demonstrate premature neuronal differentiation in patient organoids, a defect that could help to explain the disease phenotype. Together, these data show that three-dimensional organoids can recapitulate development and disease even in this most complex human tissue.

## Key findings

**Headline.** This is the **founding cerebral-organoid paper**: the first **unguided / intrinsic** 3D culture system that grows whole-brain-like tissue from human PSCs without patterning growth factors, and the first to (a) recapitulate human-specific outer-radial-glia (oRG) progenitor-zone organization in vitro and (b) model **microcephaly** — a disorder mouse models had failed to reproduce — via patient iPSCs and shRNA against `CDK5RAP2`.

**The unguided protocol (the core method this paper introduces).** EBs → neuroectoderm → **Matrigel droplet embedding** (provides scaffold for expanded neuroepithelium) → **spinning bioreactor** (nutrient/O₂ exchange). Deliberately **no patterning factors** — the design bets on intrinsic self-organization. Timeline: neural identity by **8–10 days**, defined brain regions by **20–30 days**, maximal size by ~2 months, organoids up to **4 mm** diameter, survivable to **~10 months**. Works from both hESCs (H9/WA09) and iPSCs.

**Self-patterned but heterogeneous regional identity.** Whole-organoid RT-PCR and IHC show forebrain (BF1, Six3, FoxG1, Emx1) and hindbrain (Krox20, Isl1, Gbx2, Pax2) identities arising as **discrete adjacent domains** (reminiscent of the mid-hindbrain boundary), with forebrain dominating over time. Quantified region frequencies across 35 organoids: **dorsal cortical morphology 35/35 (100%)**, choroid plexus **25/35 (71%)**, ventral forebrain (Nkx2.1⁺) **12/35 (34%)**, retina (RPE) **4/35 (11%)**. This per-organoid heterogeneity is the seed of the reproducibility problem later quantified by [Velasco 2019](velasco_2019_individual_brain_organoids_reproducibly.md) / [Quadrato 2017](quadrato_2017_cell_diversity_network_dynamics_photosensitive_human_brain.md).

**Cortical-progenitor-zone organization.** Dorsal cortical regions show a VZ-like layer (Sox2⁺ RG), adjacent Tbr2⁺ intermediate progenitors (IPs), and basal Tbr1⁺ neurons; interkinetic nuclear migration confirmed by live imaging of GFP-electroporated RG + BrdU pulse-chase; the neurogenic BAF→nBAF chromatin-remodeller switch is reproduced. RG spindle orientation: **41% horizontal, 37% oblique, 22% vertical** — more oblique/vertical than rodent, matching human-slice data.

**Human-specific oRG / OSVZ recapitulation (key evolutionary feature).** Sox2⁺ progenitors displaced basally from the VZ, separated by a Tuj1⁺ inner-fiber-layer-like band, with oRG morphology (**basal process, no apical process**) and **predominantly vertical** division. Control experiment: **mouse** organoids made by the same protocol have much smaller cortical tissue and only occasional, non-accumulating oRGs → OSVZ/IFL-like organization is **human-specific**, not an in-vitro artifact.

**Functional neurons.** Inside-out layering is only **modest** (deep-layer Ctip2⁺ internal, superficial Satb2⁺/Brn2⁺ external; clearer by 75 days) — explicitly **not** the full layer II–VI organization seen in vivo. Reelin⁺ Cajal-Retzius cells present. Neurons fire spontaneous **Ca²⁺ surges** (Fluo-4), increased by glutamate and **abolished by TTX** → activity-dependent, glutamatergic.

**Microcephaly model (`CDK5RAP2`).** Patient A3842: severe primary microcephaly (head circumference **−13.2 s.d.**), reduced stature (−6.7 s.d.), **compound-heterozygous truncating `CDK5RAP2` mutations** (exome-confirmed; fibroblasts show loss of protein). Patient iPSC organoids → **smaller neuroepithelia, premature neuronal outgrowth, fewer progenitor regions**. Mechanism = **premature neurogenic (non-proliferative) divisions at the expense of the RG founder pool** (↑ BrdU⁺/DCX⁺ cells; loss of the early-exclusive horizontal spindle orientation seen in 22-day controls). Two orthogonal confirmations: (1) **CDK5RAP2 re-expression rescue** — 54%±2 of low-GFP⁺ cells RG-morphology vs 19%±11 with GFP-only (P<0.05); (2) **two independent shRNAs** → loss of Sox2⁺ progenitors, gain of DCX⁺ neurons. Interpretation: a depleted founder RG population (an expansion step much larger in human than mouse) explains why mice don't phenocopy human microcephaly severity.

## Methods / Protocol

- **Cell lines.** hESC H9 (WA09, WiCell); commercial control iPSC (System Biosciences SC101A-1); patient iPSCs reprogrammed from skin fibroblasts via lentiviral OCT4/SOX2/KLF4/c-MYC. Mouse A9 ESCs for the cross-species control.
- **Organoid generation (the protocol).** Day 0: 4,500 single PSCs/well in low-bFGF hESC medium + 50 µM ROCK inhibitor (ultra-low-binding 96-well). Day 6: neural induction medium (DMEM/F12, N2, Glutamax, NEAA, 1 µg/ml heparin). **Day 11: embed in Matrigel droplets** (Parafilm dimple method). +4 days stationary in differentiation medium (DMEM/F12:Neurobasal, N2, B27 −vit A), then **transfer to spinning bioreactor** in differentiation medium with B27 **+vit A** (retinoic acid for neuronal differentiation). For microcephaly patient lines, **initial iPSC number was increased** to compensate for poor EB growth.
- **Perturbation tools introduced here.** (i) **Organoid electroporation** — plasmid injected into ventricle-like cavities, electroporated into apical RG (BTX ECM830, 5 pulses 80 V, 50 ms); used for GFP lineage tracing/live imaging, shRNA delivery, and CDK5RAP2 rescue. (ii) **shRNA knockdown** (pSuper, 4 targeting sequences). (iii) GFP+CDK5RAP2 co-electroporation rescue.
- **Readouts.** RT-PCR (pluripotency/regional markers); cryosection IHC (large antibody panel: Sox2, Pax6, Tbr1/2, Ctip2, Satb2, Brn2, FoxG1, Emx1, Nkx2.1, P-Vimentin, PH3, DCX, Reelin, etc.); BrdU pulse-chase for division mode; **GFP live imaging** of IKNM; **Fluo-4 calcium imaging** with glutamate/TTX pharmacology.
- **Genetics.** Patient exome (Agilent SureSelect 50 Mb, Illumina HiSeq, BWA/GATK, hg19), capillary-confirmed; western blot for CDK5RAP2 loss in fibroblasts.

## Relevance to the brain-organoid ASD review

Supports the manuscript *"Programmable Brain Organoids for Proactive Autism Genetics."*

- **The foundational platform citation — anchors the "unguided cerebral organoid" branch.** This is the origin point for the whole-brain, intrinsically patterned organoid. Use it wherever the review introduces the **platform taxonomy** (unguided cerebral organoids vs guided spheroids vs assembloids): Lancaster 2013 *is* the unguided pole, contrasting with the guided/dorsal-only [Paşca 2015 hCS](paca_2015_functional_cortical_neurons_astrocytes_human_pluripotent_stem.md) and downstream guided/fused protocols ([Birey 2017](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md), [Sloan 2018](sloan_2018_generation_and_assembly_of_human.md)).
- **Primary evidence for the human-specific-features pillar (oRG, OSVZ).** Establishes that organoids capture the **oRG/OSVZ expansion** unique to human cortex — the cellular substrate the review invokes for human-specific ASD vulnerability — with the mouse-organoid negative control as the clean cross-species demonstration. Pairs with primary-tissue oRG references [Hansen 2010](hansen_2010_neurogenic_radial_glia_outer_subventricular_zone_human.md) and [Pollen 2015](pollen_2015_molecular_identity_human_outer_radial_glia_during.md).
- **First proof that human neurodevelopmental disease modelling works in organoids.** The `CDK5RAP2` microcephaly result — *mouse-refractory* disorder, recapitulated via **patient iPSC + isogenic-style rescue + shRNA** with a concrete mechanism (premature neurogenesis depleting the founder progenitor pool) — is the template the review's "programmable autism genetics" argument is built on. Methodologically it foreshadows the perturbation-screen logic of [Li 2023](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md) (Li even cites it as ref. 9 for the disease-modelling premise).
- **Introduces the perturbation toolkit.** Organoid electroporation, shRNA knockdown, and rescue-by-re-expression are the in-organoid genetic-manipulation primitives that the review's CRISPR-perturbation theme later scales to pooled mosaic screens.
- **Honest fidelity caveat for the limits section.** The paper itself flags only **modest cortical lamination**, a **necrotic core** from lack of vasculature, and high organoid-to-organoid regional heterogeneity — concrete material for the review's "fidelity / limits" discussion.

### Related pages
- [Lancaster 2014 — Generation of cerebral organoids from human PSCs](lancaster_2014_generation_of_cerebral_organoids_from.md) — the step-by-step protocol write-up of this system.
- [Camp 2015 — Human cerebral organoids recapitulate gene-expression programs of fetal neocortex](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md) — transcriptomic fidelity benchmark of Lancaster-type organoids.
- [Hansen 2010](hansen_2010_neurogenic_radial_glia_outer_subventricular_zone_human.md), [Pollen 2015](pollen_2015_molecular_identity_human_outer_radial_glia_during.md) — primary-tissue basis for the oRG/OSVZ biology recapitulated here.
- [Quadrato 2017](quadrato_2017_cell_diversity_network_dynamics_photosensitive_human_brain.md), [Velasco 2019](velasco_2019_individual_brain_organoids_reproducibly.md) — later quantification of the cell-diversity / reproducibility this paper's heterogeneity foreshadows.
- Concept: [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md); [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md).

## Open questions / limitations

- **Lamination is incomplete.** Only modest deep/superficial separation; the authors explicitly state organoids do **not** reach mature layer II–VI inside-out organization — "further cues are needed." Later-born superficial layers and full cortical architecture are not faithfully built.
- **No vasculature → necrotic core.** Diffusion-limited; a size limit (~4 mm) with extensive central cell death. Constrains long-term maturation and the cell types that survive (addressed by later vascularization/transplant work).
- **Regional heterogeneity / low reproducibility.** Identity is self-patterned and stochastic — region frequencies vary widely organoid-to-organoid (e.g. ventral forebrain in only 34%), so any single organoid is not a controlled cortical sample. This is the explicit motivation for later *guided* protocols.
- **Microcephaly model is partial and n=1 patient.** A single `CDK5RAP2` compound-het patient; "at least some aspects" of microcephaly modelled. The rescue is indirect (high CDK5RAP2 over-expression was toxic, so only low-re-expressing cells were scored), and quantification rests on small cell counts.
- **Zygosity / dosage not controlled in perturbation.** shRNA knockdown and electroporation give variable, mosaic, non-isogenic perturbation — a limitation the field only resolves with inducible, barcoded CRISPR systems (cf. Li 2023 CHOOSE).
