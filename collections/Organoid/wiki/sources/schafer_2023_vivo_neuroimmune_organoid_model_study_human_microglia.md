---
title: "An in vivo neuroimmune organoid model to study human microglia phenotypes."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.cell.2023.04.022
pmid: 37172564
authors: Schafer ST et al.
journal: Cell (2023)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# An in vivo neuroimmune organoid model to study human microglia phenotypes.

## Source

- Authors: Schafer ST, Mansour AA, Schlachetzki JCM, Pena M, Ghassemzadeh S, Mitchell L, Mar A, Quang D et al. (co-senior Glass, Nimmerjahn, Gage; Salk Institute / TU Munich / UC San Diego / Hebrew University)
- Journal: Cell (2023); 186(10):2111–2126; OPEN ACCESS
- DOI: [10.1016/j.cell.2023.04.022](https://doi.org/10.1016/j.cell.2023.04.022)
- PMID: [37172564](https://pubmed.ncbi.nlm.nih.gov/37172564/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Microglia are specialized brain-resident macrophages that play crucial roles in brain development, homeostasis, and disease. However, until now, the ability to model interactions between the human brain environment and microglia has been severely limited. To overcome these limitations, we developed an in vivo xenotransplantation approach that allows us to study functionally mature human microglia (hMGs) that operate within a physiologically relevant, vascularized immunocompetent human brain organoid (iHBO) model. Our data show that organoid-resident hMGs gain human-specific transcriptomic signatures that closely resemble their in vivo counterparts. In vivo two-photon imaging reveals that hMGs actively engage in surveilling the human brain environment, react to local injuries, and respond to systemic inflammatory cues. Finally, we demonstrate that the transplanted iHBOs developed here offer the unprecedented opportunity to study functional human microglia phenotypes in health and disease and provide experimental evidence for a brain-environment-induced immune response in a patient-specific model of autism with macrocephaly.

## Key findings

- **Platform (iHBO)**: hPSC-derived CD43+ erythromyeloid progenitors (EMPs) are integrated into hPSC forebrain organoids, then the organoid is xenotransplanted into the retrosplenial cortex of NOD/SCID mice (transplant ~day 38). Host vascularization infiltrates the graft, yielding an **immunocompetent, vascularized human brain organoid** with resident human microglia (hMGs). Dual labeling: organoids GFP+, microglia/EMPs tdTomato+.
- **Transplantation is required for maturation/survival**: in vitro, EMP-derived myeloid cells were IBA1+ at 6 wpi but largely lacked homeostatic markers (P2RY12/TMEM119 mRNA almost absent); few survived and those showed activated round morphology. After transplantation, tdT+ cells were IBA1+ at 8 wpt, co-expressed PU.1 and human-specific TMEM119, and (importantly) this occurred even though host mice were **not humanized for CSF-1** — the vascularized human organoid supplies the microglia-supportive niche. IL34 and CSF1 were detected in transplanted organoids but IL34 was undetectable in age-matched in vitro organoids.
- **Reproducible homeostatic identity**: iHBOs from 3 independent iPSC lines (plus hESC) yielded hMGs with characteristic ramified morphology and high IBA1; morphology matched IBA1+ microglia from human brain tissue. scRNA-seq of FACS-sorted tdT+/hCD45+ hMGs showed canonical microglia genes (AIF1, CX3CR1, CSF1R, CST3) and homeostatic markers (P2RY12, TMEM119, SALL1); P2RY12/hTMEM119 protein confirmed at 11 wpt.
- **Defined developmental trajectory toward in-vivo identity**: longitudinal scRNA-seq at 6/11/24 wpt — trajectory inference gave 3 trajectories (early→late); pseudo-temporal genes overlapped human fetal microglia developmental genes; integration with fetal microglia (GW9–18) showed correspondence. A highly proliferative endpoint cluster (matching fetal proliferative microglia) declined from 6→24 wpt. Mature/human-brain-environment-dependent hMG signatures were acquired between 11 and 24 wpt; 24-wpt hMGs mapped onto ex vivo adult human microglia.
- **Human-specific signature is environment-instructed** (hMG vs xMG): comparing hPSC-microglia in human-organoid grafts (hMGs) vs in mouse brain (xMGs) by WGCNA — the hMG module (MEturquoise) was exclusively enriched for human-specific microglia genes (hub genes SLC8A1, VSIG4, IRAK3, highly expressed in hMGs but few xMGs), whereas the xMG module (MEblue) contained mouse-specific genes (LY6E, TPI1). Implies the human-specific identity arises from hMG × human-brain-environment interaction.
- **Functional surveillance (in vivo 2-photon)**: ramified hMGs were highly motile — process motility 1.76 µm/min ± 0.43 at 12 wpt; baseline motility decreased significantly from 6 wpt (2.22 ± 0.59) to 24 wpt (1.702 ± 0.39); microglia density increased 6→24 wpt with no migratory cells by 24 wpt.
- **Injury response**: focal 2-photon laser lesions elicited immediate, directional process extension toward the injury (process polarity index shift at 10/30 min); distance traveled to the injury site was significantly greater at 12 wpt than 26 wpt (Mann-Whitney, p = 0.0056) — developmental-stage-dependent injury response.
- **Systemic inflammation response**: intraperitoneal LPS (1 or 5 mg/kg) produced a dose-dependent morphological shift in hMGs at 24 h (strong at high dose). No upregulation of TNF, IL6, or IL10 detected — i.e., a morphological/sensing response without a sustained acute-cytokine signature at the sampled point.
- **Patient-specific ASD finding (headline)**: isogenic GFP/tdT iPSCs from 3 ASD subjects (with macrocephaly) and 3 neurotypical controls. After 12 weeks in vivo, ASD-subject iHBOs showed hMGs with overabundant soma filopodia at the expense of resting states — significantly increased soma size, primary process thickness, and process filopodia number (primed/reactive phenotype); absent in all 3 control iHBOs.
- **The response is environment-driven, not microglia-intrinsic** (decisive swap experiment): when **neurotypical (control-iPSC) hMGs** were placed into ASD-subject vs control brain environments, the reactive phenotype appeared only in the ASD brain environment. This is the first experimental evidence for a cell-non-autonomous, brain-environment-induced microglial immune response in autism with macrocephaly.

## Methods

- **Cells**: hPSC-derived CD43+ EMPs (Mansour-lab protocol); constitutive tdTomato or GFP reporters; forebrain organoids.
- **Transplantation**: EMP-containing forebrain organoids grafted into retrosplenial cortex of NOD/SCID mice (not CSF-1-humanized); harvest 8–26 wpt; host-derived vascularization (builds on Mansour 2018 vascularized-transplant paradigm).
- **Profiling**: bulk RNA-seq of organoids before/after transplant (day 38, 4 & 24 wpt; Spearman correlation to BrainSpan); scRNA-seq of FACS-sorted tdT+/hCD45+ hMGs at 6/11/24 wpt; trajectory inference, Louvain clustering, WGCNA (hMG vs xMG); reference mapping to fetal (GW9–18) and adult ex vivo human microglia datasets.
- **Functional imaging**: in vivo 2-photon microscopy (process motility over 90-min intervals; focal laser-lesion injury at 12/26 wpt); systemic LPS challenge (1/5 mg/kg i.p.), morphological phenotyping at 24 h.
- **Disease model**: isogenic patient/control iPSC panels (3 ASD-macrocephaly + 3 neurotypical); reciprocal microglia × organoid combinations to separate intrinsic vs environmental contributions.

## Relevance to the brain-organoid ASD review

- **Fills the microglia / neuroimmune gap and is the advanced-platform anchor of the review.** Standard cortical organoids (e.g., the [Uzquiano 2022](uzquiano_2022_proper_acquisition_cell_class_identity_organoids_allows.md) atlas) explicitly lack microglia. This vascularized, immunocompetent xenotransplant (iHBO) delivers functionally mature, human-specific, surveilling hMGs inside a human brain environment — the missing neuroimmune dimension for ASD modeling.
- **Provides the strongest organoid evidence for a neuroimmune contribution to ASD**: the patient-specific reactive-microglia phenotype, and especially the swap experiment showing it is **driven by the ASD brain environment rather than intrinsic to the microglia**, recasts ASD microglial activation (long seen in postmortem/PET studies) as a cell-non-autonomous response to aberrant neurodevelopment.
- **Same disease subtype as the PTEN axis** (ASD with macrocephaly), linking it to [Fu 2023](fu_2023_autism_specific_pten_p_ile135leu_variant_autism.md): the neuronal/progenitor overgrowth phenotypes (Fu) and the environment-induced microglial priming (Schafer) are complementary readouts of the same overgrowth phenotype, suggesting a neuron→microglia signaling axis to probe proactively.
- **Demonstrates that maturation and human-specific identity require an in-vivo-like vascularized niche** — methodological context for why transplantation (cf. [Mansour 2018](mansour_2018_vivo_model_functional_vascularized_human_brain_organoids.md), [Revah 2022](revah_2022_maturation_circuit_integration_transplanted_human_cortical_organoids.md)) extends what purely in vitro organoids can model.
- Functional toolkit (in vivo 2-photon surveillance/injury/LPS assays) gives the review concrete neuroimmune phenotyping endpoints.

## Open questions / limitations

- Small group sizes for the disease analysis (3 ASD + 3 control lines); authors call for larger cohorts.
- Host-cell contribution to the graft is unresolved — whether graft vasculature is entirely host-derived or partly human is not established and could confound the "human" system.
- Sex/gender effects (relevant to ASD) were not dissected; flagged for future work.
- LPS elicited morphological change without detectable TNF/IL6/IL10 upregulation at the sampled timepoint — the molecular inflammatory response is incompletely characterized.
- Xenograft into immunodeficient (NOD/SCID) mouse — the systemic immune context is non-physiological; "immunocompetent" refers to the organoid's resident microglia, not the host.
- The ASD-environment signal is characterized morphologically; the specific neuronal-derived cues that prime microglia are not identified.

## Related

- [Mansour 2018 — vascularized human brain organoid transplantation](mansour_2018_vivo_model_functional_vascularized_human_brain_organoids.md) (the vascularized-transplant paradigm this builds on; shared senior author Gage)
- [Revah 2022 — maturation & circuit integration of transplanted human cortical organoids](revah_2022_maturation_circuit_integration_transplanted_human_cortical_organoids.md) (transplantation-driven maturation)
- [Uzquiano 2022 — cell-class identity atlas](uzquiano_2022_proper_acquisition_cell_class_identity_organoids_allows.md) (notes microglia absent from cortical organoids — the gap filled here)
- [Fu 2023 — PTEN p.Ile135Leu, ASD with macrocephaly](fu_2023_autism_specific_pten_p_ile135leu_variant_autism.md) (same disease subtype; neuronal/progenitor side)
- [Paulsen 2022 — ASD genes converge on neuron development](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md)
