---
title: "Scalable production of human cortical organoids using a biocompatible polymer"
kind: paper
status: ingested
added: 2026-07-01
deep_ingested: 2026-07-01
doi: 10.1038/s41551-025-01427-3
pmid: 40579490
authors: Narazaki G et al.
journal: Nature Biomedical Engineering (2025)
source_ref: assembloid-technology-platform (Pașca lab batch)
raw_source: collections/Organoid/raw/sources/narazaki_2025_scalable_production_human_cortical_organoids_biocompatible_polymer.pdf
pdf_status: downloaded
---

# Scalable production of human cortical organoids using a biocompatible polymer

## Source
- Authors: Genta Narazaki, Yuki Miura (co-first), Sergey D. Pavlov, Mayuri Vijay Thete, Julien G. Roth, Merve Avar, Sungchul Shin, Ji-il Kim; Sarah C. Heilshorn (co-senior); senior/corresponding **Sergiu P. Pașca** (Stanford Brain Organogenesis, Wu Tsai Neuroscience Institute).
- Journal: Nature Biomedical Engineering, Volume 9, December 2025, pp. 2115–2123. Received 24 Jul 2023; accepted 12 May 2025; published online 27 Jun 2025.
- DOI: [10.1038/s41551-025-01427-3](https://doi.org/10.1038/s41551-025-01427-3)
- PMID: [40579490](https://pubmed.ncbi.nlm.nih.gov/40579490/)
- Data: scRNA-seq deposited GEO **GSE232581**; calcium-imaging code on Zenodo (doi:10.5281/zenodo.15092416).
- Added via: assembloid-technology-platform batch ingest.

## Abstract
Neural organoids from human pluripotent stem cells hold promise for disease modelling and drug screening but are hard to scale because organoids cultured in suspension spontaneously fuse. The authors screened biocompatible polymers added to culture medium to prevent fusion of suspension-cultured organoids and identified a cost-effective polysaccharide — **xanthan gum (XG)** — that raises medium viscosity and significantly increases the yield of cortical organoids while preserving regional patterning, neuronal morphology and functional activity. The platform enabled screening of **298 FDA-approved drugs and teratogens** for growth defects using **>2,400 cortical organoids**, uncovering agents (e.g., doxorubicin, AT9283) that disrupt organoid growth/development. The approach is positioned as a robust, scalable system for modelling human cortical development and for efficient compound screening of neuropsychiatric-disorder–associated phenotypes.

## Key findings
- **XG is the hit from a 23-polymer screen.** 23 candidate polymers (selected by molecular weight, chemical structure, electrostatic charge, biocompatibility; Supplementary Table 1) were added to differentiation medium from day 6; 5 hCO/well of a 24-well plate cultured to day 25, then remaining (unfused) organoids counted. Xanthan gum (a widely used food/pharma exo-polysaccharide) significantly reduced spontaneous fusion (untreated vs XG *P = 0.01; untreated vs carboxymethyl cellulose 700 *P = 0.03; Kruskal–Wallis).
- **Large, reproducible yield gain across lines.** In the primary yield comparison, n = 36 wells untreated vs 36 wells hCO+XG across **3 differentiations × 4 hiPS lines** showed markedly more remaining organoids with XG (two-tailed unpaired t-test ****P < 0.0001). Lines used: 1205-4, 1208-2, 8119-1, KOLF2.1J (+0524-1 for scRNA-seq/activity).
- **Enables one researcher to run thousands of organoids in parallel.** Because XG suppresses fusion, a single researcher differentiated and maintained **>2,000 organoids simultaneously**; the drug screen used **>2,400 cortical organoids**. Framed as reducing both maintenance time and media cost, enabling screens in budget-limited labs.
- **Uniform size / anti-fusion, not growth inhibition.** XG-hCO were smaller in bulk culture (cross-sectional area: NS at day 3 P = 0.99; ****P < 0.0001 at days 10 and 15; Ext. Data Fig. 3b) — but when organoids were cultured **individually** (one per low-attachment well), XG did **not** impair growth and slightly increased size (day 15; Ext. Data Fig. 3c), confirming the bulk size reduction reflects prevented fusion rather than stunted growth.
- **Dose and density dependence.** Anti-fusion effect present even at **0.01% (w/v)** XG (working stock 0.2% w/v = 2×; final ~0.1%). Effect attenuates at high organoid density: culturing **10 or 15** organoids per 24-well was less efficient than 5 (Ext. Data Fig. 1: 5 vs 10 ***P = 0.0003, 5 vs 15 **P = 0.0046, 10 vs 15 NS).
- **Beats a commercial anti-fusion medium.** XG prevented fusion more effectively than STEMdiff Neural Organoid Basal Medium 2 (NOBM): untreated vs XG ****P < 0.0001; XG vs NOBM **P = 0.002 (Ext. Data Fig. 2), with no differences in patterning/cytoarchitecture among conditions.
- **Mechanism is biophysical (viscosity/osmolarity), not merely MW.** XG raised medium viscosity (*P = 0.01) and osmolarity (****P < 0.0001). A different high-MW, negatively charged polymer — hyaluronic acid (MW 2.0–2.4×10⁶) — did **not** reduce fusion, arguing MW alone is insufficient. Extracellular-fluid ATTO-647 imaging showed XG medium still penetrates hCO (NS P = 0.08), i.e., no barrier to diffusion.
- **No cytotoxicity.** LDH assay NS (P = 0.48 main; P = 0.64 Ext. Data Fig. 4c, n = 39 vs 39 wells); no induction of cleaved caspase-3; comparable VZ-like structure density (Fig. 1k NS P = 0.75).
- **Progenitor identity preserved.** %SOX2⁺ (NS P = 0.46) and %PAX6⁺ (NS P = 0.35) at day 25 comparable to untreated (n = 15–16 organoids/condition). Day-25 RT-qPCR: no differences in FOXG1/EN1/EMX1/NKX2-1/FOXA2/RAX/HOXB4 (all NS); dorsal-forebrain identity maintained, off-target (midbrain/ventral/hindbrain) markers absent.
- **scRNA-seq confirms fidelity at day 65.** 11,763 cells (5,043 hCO; 6,720 hCO+XG). Both conditions contain cortical progenitors (PAX6⁺), glutamatergic neurons (TBR1⁺), cycling cells (MKI67⁺), intermediate progenitors, Cajal–Retzius, undefined and GABAergic neurons. Normalized-expression correlation between conditions **R² = 0.986 (****P < 0.001)**. VoxHunt mapping to Allen E15.5 mouse brain comparable across conditions. XG-hCO had slightly more GABAergic neurons, within previously reported hCO range; no DLX2/GSX2/NKX2-1 ventral contamination.
- **Later maturation & function intact.** CTIP2 (deep layer) at day 62; GFAP (glia) and SATB2 (upper layer) at day 100. Neuronal morphology (soma area, circularity, neurite number) unchanged (all NS). AAV-hSYN1::jGCaMP8s calcium imaging: Ca²⁺ events/min comparable (NS P = 0.19; n = 19 organoids/1,959 neurons hCO vs 18 organoids/2,491 neurons hCO+XG, 4 lines).
- **Screen hits — doxorubicin (Doxo).** In the 298-drug screen (1 µM, day 17→25, DMSO control), the breast-cancer topoisomerase-II drug / known teratogen doxorubicin reduced hCO area (day 4 *P = 0.02; days 6, 8 ****P < 0.0001). CUBIC 3D clearing showed lower SOX2⁺ density (****P < 0.0001); dose-dependent growth impairment (0 vs 1,000 nM *P = 0.02) and LDH cytotoxicity (0 vs 1,000 nM ****P < 0.0001); increased cleaved caspase-3 (**P = 0.006). Effect reproduced across a second Doxo batch and multiple lines.
- **Screen hits — AT9283.** JAK2/3 inhibitor reduced hCO area dose-dependently (0.01–1 µM, ****P < 0.0001 at 0.1 and 1 µM), increased cytotoxicity (0.1 µM ***P = 0.0009; 1 µM *P = 0.016) and reduced SOX2⁺ cell number (****P < 0.0001, CUBIC).

## Methods
- **Base organoid protocol:** Pașca-lab directed cortical organoid (hCO/hCS). hiPS cells (5 control lines incl. KOLF2.1J from Jackson Lab) maintained on vitronectin in Essential 8. Uniform spheroids formed in AggreWell-800 (300 microwells; ~2×10⁶ cells/well; ~6,666 cells/organoid at 24 h) with Y-27632; dual-SMAD inhibition (dorsomorphin 2.5 µM + SB-431542 10 µM) in Essential 6 to day 6; then Neurobasal-A + B-27 minus vit A + GlutaMAX + pen/strep + EGF 20 ng/ml + FGF2 20 ng/ml; BDNF+NT3 from day 25; B-27-only from day 45.
- **Material / polymer:** Xanthan gum powder pre-dissolved in 100% ethanol then diluted (0.5 g XG + 2 ml ethanol + 248 ml Neurobasal → 250 ml of 0.2% w/v XG = 2× stock; final working ~0.1%). Dedicated equipment/biosafety cabinet to avoid clumping and contamination. Comparators: 22 other polymers (Supplementary Table 1, incl. carboxymethyl cellulose, PEGs, alginate, gellan gum, hyaluronic acid), STEMdiff NOBM 2, and individual (single-well low-attachment) vs bulk (24-well) culture.
- **Scale / throughput assay:** 5 (vs 10, 15) hCO per 24-well; screening plate format scaled to run >2,000 organoids by one operator. Author-noted compatibility with bioreactors and automated bulk media changes (liquid handlers / robotic arms) for further scale.
- **Media biophysics:** viscosity by Rheosense m-VROC viscometer (high shear, steady state); osmolarity by 5010 OSMETTE III. Extracellular fluid imaging with 50 µM ATTO-647 (30 min), Leica SP8 confocal, ImageJ/Fiji.
- **Reproducibility / variance framing:** yield and phenotype metrics reported across **3–4 differentiation experiments and up to 4–5 hiPS lines**; organoid-level n typically 15–36 wells or ~100–500 organoids per comparison; fused organoids excluded and area normalized to day-1 to control baseline size.
- **Quality / fidelity assays:** RT-qPCR (day 25 regional-marker panel); scRNA-seq (10x Chromium 3′ v3.1, ~11,600 cells loaded/lane targeting 7,000; NovaSeq 6000, 2×150 bp; Cell Ranger v6.0.1; Seurat v4.1.2; filters >500 & <10,000 genes, <10% mito; top 15 PCs, res 0.4; VoxHunt v1.0.0 vs Allen E15.5 ISH). Immunocytochemistry (SOX2, PAX6, CTIP2, GFAP, MAP2, SATB2, cleaved caspase-3); CUBIC 3D clearing + SOX2/RedDot2 3D quantification (Imaris v9.6); LDH cytotoxicity (CyQUANT); AAV-DJ-hSYN1::eYFP morphology and hSYN1::jGCaMP8s calcium imaging (Suite2p, ΔF/F, custom event detection).
- **Drug screen:** 298 FDA-approved drugs / teratogens (Supplementary Table 4), 1 µM in DMSO/water, applied day 17→25 every other day; area imaged at days 1/4/6/8 (KEYENCE BZX-710, ×4); hits validated dose-response + CUBIC + LDH + caspase-3.
- **Timepoints:** fusion/yield day 25 (some day 5–12); size days 3/7/10/15; qPCR/ICC day 25; scRNA-seq day 65; layer markers day 62–100; up to 14 weeks.
- **Stats:** unpaired t-test (two-tailed), Mann–Whitney, one-/two-way ANOVA with Šidák/Tukey/Dunnett/Dunn multiple comparisons; GraphPad Prism v9.3.1.

## Relevance to the brain-organoid ASD review
- **Directly attacks the THROUGHPUT barrier.** A single anti-fusion additive lets one researcher run **>2,000 organoids in parallel** and screen 298 compounds — a concrete Build/Test scale-up for using cortical organoids as a screening platform, exactly the bottleneck the manuscript flags for deploying organoids at scale.
- **Attacks the COST/LABOR barrier.** XG is a cheap food-grade polysaccharide; the authors emphasize reduced maintenance time and media cost, making screens feasible "even in laboratories with a limited budget" — relevant to the review's argument that scalability enablers are prerequisites for organoid-based screening.
- **Supports REPRODUCIBILITY / size uniformity.** Uniform organoid size and prevented fusion reduce a major source of experimental variance and organoid loss; yield/phenotype validated across 3–4 differentiations and 4–5 lines — feeds the review's variance-partitioning and reproducibility requirements (complements Yoon 2019 and Velasco 2019).
- **Establishes assay operating characteristics for a growth readout.** Provides a quantitative, dose-dependent growth/size + cytotoxicity + caspase-3 assay cascade with defined n, controls (DMSO/H₂O, normalization to day 1) and multiple-comparison correction — a template for the assay-operating-characteristics the review demands of any screening endpoint.
- **Fidelity is preserved under scale-up (critical caveat handled).** scRNA-seq R² = 0.986, unchanged patterning, morphology and calcium activity show the scalability gain does **not** cost cellular fidelity — important because a screening platform must scale without distorting the disease-relevant phenotype.
- **Automation-ready / assembloid-compatible.** Explicitly compatible with bioreactors, liquid handlers and robotic arms, and the related anionic polysaccharide gellan gum enables assembloid CRISPR screens (Meng et al. 2023) — extends the enabler toward higher-throughput and circuit-level (assembloid) ASD phenotyping.

## Open questions / limitations
- **Density ceiling:** anti-fusion efficiency drops at ≥10 organoids per 24-well, capping per-well density; optimal density/format for very-large screens not fully defined.
- **Author-stated scope of "no effect":** authors caution that although no significant changes were detected in patterning, differentiation, morphology and activity, **other parameters at specific differentiation times may still be affected by XG** — not exhaustively excluded.
- **Line-dependent fusion:** degree of fusion still varies with hiPS line (early-stage growth-rate differences), so XG mitigates but does not fully eliminate line-to-line variance.
- **Early-development / short-window focus:** platform and screen emphasize early cortical development (day 17–25 growth readout); long-term (months), maturation-stage and functional/network phenotypes at scale are less validated.
- **Readout is largely morphometric:** primary screen endpoint is organoid area/growth; disease-relevant functional or molecular high-content readouts (calcium, transcriptomics) demonstrated but not yet run at full 298-compound scale.
- **Commercial-media opacity:** direct benchmarking against other commercial anti-fusion media is limited by undisclosed proprietary polymer compositions.
- **Mechanism partial:** viscosity/osmolarity implicated but the precise physical mechanism of fusion prevention (vs simple MW) is not fully resolved.
- **Competing interest:** Stanford holds a cortical-organoid patent (US 62/477,858) licensed to STEMCELL Technologies (S.P.P. inventor); one co-first author was a Daiichi-Sankyo employee during the study.

## Related
- [paca_2015_functional_cortical_neurons_astrocytes_human_pluripotent_stem.md](paca_2015_functional_cortical_neurons_astrocytes_human_pluripotent_stem.md) — the foundational suspension hCS/hCO protocol this work scales (Pașca lab, ref. 6).
- [yoon_2019_reliability_of_human_cortical.md](yoon_2019_reliability_of_human_cortical.md) — reliability/reproducibility of the same hCO protocol across lines (ref. 9); directly complements the reproducibility claims here.
- [velasco_2019_individual_brain_organoids_reproducibly.md](velasco_2019_individual_brain_organoids_reproducibly.md) — reproducible cortical cell-diversity benchmark (Arlotta); companion reproducibility reference.
- [cheroni_2022_benchmarking_brain_organoid_recapitulation_fetal_corticogenesis.md](cheroni_2022_benchmarking_brain_organoid_recapitulation_fetal_corticogenesis.md) — benchmarking organoid fidelity vs fetal corticogenesis; fidelity context for scaled organoids.
- [d_2026_from-organoid-culture-to-manufacturing-technologies-for-reproducible-and-scalable-organoid.md](d_2026_from-organoid-culture-to-manufacturing-technologies-for-reproducible-and-scalable-organoid.md) — review of scalable/reproducible organoid manufacturing (pruned as secondary review; thematic overlap on scalability).
- [birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md) — Pașca-lab assembloids; scalable polymers (gellan gum) extend to assembloid screens (ref. 26).
- [chen_2023_protocol_for_generating_reproducible_miniaturized.md](chen_2023_protocol_for_generating_reproducible_miniaturized.md) — reproducible miniaturized organoid protocol; adjacent scalability/reproducibility method.
