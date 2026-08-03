---
title: "Generating human neural diversity with a multiplexed morphogen screen in organoids"
kind: paper
status: ingested
added: 2026-07-01
deep_ingested: 2026-07-01
doi: 10.1016/j.stem.2024.10.016
pmid: 39642864
authors: Amin ND et al.
journal: Cell Stem Cell (2024)
source_ref: assembloid-technology-platform (Pașca lab batch)
raw_source: collections/Organoid/raw/sources/amin_2024_generating_human_neural_diversity_multiplexed_morphogen_screen_organoids.pdf
pdf_status: downloaded
---

# Generating human neural diversity with a multiplexed morphogen screen in organoids

## Source
- Authors: Neal D. Amin, Kevin W. Kelley (co-first), Konstantin Kaganovsky, Massimo Onesto, Jin Hao, Yuki Miura, James P. McQueen, Noah Reis, ... senior/lead contact **Sergiu P. Pașca** (Stanford, Dept. Psychiatry & Behavioral Sciences; Stanford Brain Organogenesis Program).
- Journal: Cell Stem Cell 31, 1831–1846 (December 5, 2024). "Resource" article.
- DOI: [10.1016/j.stem.2024.10.016](https://doi.org/10.1016/j.stem.2024.10.016)
- PMID: [39642864](https://pubmed.ncbi.nlm.nih.gov/39642864/)
- Data: scRNA-seq at GEO **GSE233574**; spatial (MERFISH) at Zenodo (10.5281/zenodo.13835782). No original code.
- Added via: assembloid-technology-platform batch ingest.

## Abstract
Morphogens choreograph cellular diversity in the developing nervous system, and in-vitro stem-cell differentiation relies on combinatorial modulation of these pathways — but the lack of a systematic approach has precluded generation of many neural populations, and general principles of regional specification and maturation remain incomplete. The authors developed an **arrayed screen of 14 morphogen modulators** (8 signaling pathways) in human hiPS-cell neural organoids cultured **>70 days**. Deconvolution of single-cell-multiplexed RNA sequencing revealed design principles of brain-region specification, including critical timing windows and morphogen combinatorics that yield rare neural subtypes. They tuned subtype diversity to generate a **TAC3-expressing striatal interneuron** type validated within assembloids by spatial transcriptomics, generated Cajal-Retzius (CR) cell and cerebellar organoid protocols, and — to circumvent in-vitro maturation limits — used **neonatal rat transplantation** to let human Purkinje neurons develop their hallmark complex dendritic branching. The platform yields insights into factors influencing stem-cell-derived neural diversification and maturation.

## Key findings
- **Arrayed morphogen screen scale.** Modulated **8 morphogen pathways using 14 molecules** across **46 unique conditions** (combinations × timing × concentration × duration), applied individually and combinatorially, in hiPS-derived organoids cultured **>70 days** (analyzed days 72–74). Included prior validated region protocols (spinal cord, choroid plexus) as positive controls.
- **14-molecule panel.** SAG (smoothened/SHH agonist), CHIR99021 (WNT agonist), IWP2 (WNT inhibitor), RA (retinoic acid), FGF2/FGF4/FGF8, EGF, BMP4, BMP7, LDN-193189 & dorsomorphin (DM) & SB-431542 (SMAD/dual-SMAD), SR11237 (RXR agonist), DAPT (Notch/γ-secretase inhibitor). LDN-193189 (continued SMAD inhibition) = **default comparison condition**, yielding telencephalic human cortical organoids (hCOs).
- **Massively parallel format.** 3D-printed **polylactic acid (PLA) grids** separated **~30 organoids per condition** in 6-well plates → panel of **nearly 1,500 individually spaced organoids**; multiplexed scRNA-seq via **split-pool combinatorial barcoding**.
- **scRNA-seq readout.** After filtering, **36,265 high-quality cells** captured across all conditions (avg **788 ± 57 SEM cells/condition**). Cells integrated with a high-resolution prenatal human brain atlas (ref 37) spanning stage-matched timepoints.
- **Coverage across the neural axis.** Organoid cells spanned neuronal, astroglial, and oligodendrocyte types from **telencephalon → diencephalon → midbrain → hindbrain/cerebellum**. Regional identity confirmed by label transfer + **VoxHunt** mapping to developing-mouse ISH data.
- **Broad recapitulation of in-vivo diversity.** Organoid clusters mapped to **358 / 550 (65.1%) CNS-derived fetal clusters** with ≥25% cluster overlap — capturing a large proportion of in-vivo brain regional diversity.
- **Condition→cell-type specificity.** On average each condition contributed ≥10% of its cells to only **3.37 ± 0.16 SEM neural clusters** (fairly specific), yet most clusters drew from >1 condition. Cell types generated: forebrain glutamatergic & GABAergic neurons, TP73+/RELN+ CR cells, cerebellar Purkinje + granule cells, thalamic VGLUT2+/CRH+ neurons, dopaminergic neurons, plus non-neuronal TTR+/CLIC2+ choroid plexus, MOG+ oligodendrocytes, cortical hem (CH).
- **Morphogen logic — dominance & synergy.** SHH (SAG) is **dominant over WNT and BMP** (SAG alone or +CHIR/+BMP7 → GABAergic INs + oligodendrocytes). Synergy: **SAG + CHIR + FGF4 or FGF8** greatly increased midbrain identity (absent with FGF4/FGF8 alone); **SAG + BMP4** yielded hypothalamic populations not seen with SAG alone. Combination-specific fates: **SAG+CHIR+FGF8 → dopaminergic neurons**; **BMP + CHIR → choroid plexus**.
- **Critical timing windows — switch-like vs graded.** **CR/CH fate = switch-like**: CHIR must be applied **early, before day 11** (WNT days 6–13 then inhibition days 13–21 still works; CHIR after day 13 → glutamatergic cortical neurons instead) — a "surprisingly narrow" window. **IN subtype = graded**: early 250 nM SAG → ventral NKX2-1+ INs; late 250 nM SAG → dorsal MEIS2+ INs; intermediate (day 11) → mixture.
- **Cerebellar organoids (hCbOs).** Dominant feature = **FGF2 with N2 supplement** (days 6–21; note: standard hCO uses FGF2 *without* N2). New FGF2 (50 ng/mL) differentiations in 3 hiPS lines → **13,040 cells** with PAX2+ INs, Purkinje (SKOR2+/CA8+/CALB1+), LMX1A+/EOMES+ unipolar brush cells, ATOH1+/BARHL1+ rhombic-lip progenitors, granule cells, cerebellar nuclei, choroid plexus, astrocytes.
- **Purkinje maturation is arrested in vitro but rescued by transplantation.** In vitro hCbO Purkinje neurons stall at **simple fusiform morphology** (≈ late first trimester / PCW12–16) even after **6–8 months** culture (day 185). After transplantation into neonatal athymic rat cerebellum (postnatal days 3–7; **8/9 rats** HNA+/CALB1+/SKOR2+), transplanted Purkinje neurons (t-hCbO, day 185 = 138 days post-transplant) developed **complex dendritic branching** resembling PCW32 human cerebellum, with significantly greater Sholl max-intersections and area-under-curve (**p < 0.0001**, Mann-Whitney; n = 39 vs 38 neurons).
- **Cajal-Retzius / medial pallium organoids (hMPOCR).** Protocol = **CHIR days 6–11**; validated by TP73+ IHC (4 hiPS lines) and scRNA-seq (2 lines, day 80, **12,500 cells**) showing CR (TP73+/RELN+) and cortical hem (WNT3A+/RSPO2+). In hMPOCR-hCO **assembloids** (AAV hSYN1::eYFP-labeled), CR cells (TP73+eYFP+) preferentially migrated into the hCO side (n = 9 assembloids, p = 0.0039), modeling CR migration.
- **TAC3+ striatal interneurons (hSOTAC3) — a primate innovation.** TAC3-INs (TAC3+/DLX1+/NKX2-1+, striatal-enriched, described in macaque/marmoset but absent in mouse/ferret) generated best with **CHIR 1.5 µM + SAG 1,000 nM**; refined to **CHIR 1.5 µM + SAG 2,000 nM** (= hSOTAC3). Validated against human PCW21 primary striatum (scRNA-seq + RNAscope). hSOTAC3-hStrO assembloids profiled by **MERFISH: 47,022 segmented cells** (14 cryosections, 6 assembloids, 48 days post-fusion); TAC3-INs localized to the hStrO side.
- **Neuropsychiatric disease-gene expression.** Disease genes broadly expressed but cluster-enriched: on average **81% of NDD genes (n=373)**, **84% of ASD genes (n=184)**, **60% of SCZ genes (n=244)** expressed per cluster. Some show restricted, condition-specific expression (e.g., **EBF3** in cerebellar Purkinje/midbrain-glutamatergic/CR; **GATA3** in midbrain GABAergic; **NR4A2** in dopaminergic).
- **Morphology quantification validated transcriptomics.** OLIG2+ nuclei (IHC) vs oligodendrocyte fraction (scRNA-seq) correlated across conditions (**r = 0.85, p < 0.0001**); RA + SAG → most oligodendrocytes. FGF8 (100 ng/mL) organoids were **2.82× larger** in diameter than RA (100 nM) (p < 0.0001) and rich in ventricular-like zones (VLZs). Telencephalic identity correlated with VLZs (not size); cerebellar identity correlated with size (not VLZs); organoid size was **not** associated with cCas3+ apoptosis.

## Methods
- **Cell lines:** 4 control hiPS lines (healthy subjects); TAC3 refinement/hCbO used up to 3–4 lines. E8/vitronectin maintenance.
- **Spheroid formation (day −1):** 3×10^6 hiPS cells per **AggreWell-800** well (+ Y-27632 10 µM) → ~**10,000-cell** spheroids by 24 h.
- **Neuralization:** dual-SMAD inhibition — **dorsomorphin 2.5 µM + SB-431542 10 µM** in Essential 6 (from day 0). ~200–300 spheroids/AggreWell split to ~30 spheroids/well.
- **Screen media/timing:** days 0–6 Essential 6 (daily change); **days 6–21 Neurobasal-A + B27 minus vitamin A + GlutaMAX** (morphogens applied here); day 21+ add N-2, BDNF/NT3 (20 ng/mL), cAMP (50 µM), ascorbic acid. Most morphogen manipulations occur in the **day 6–21** window (and select day 0–6 timings).
- **Arrayed grid:** custom 3D-printed **PLA grids** (Prusa i3 MK3S+), poly-HEMA hydrophobic coated, one organoid per chamber, ~30/condition in ULA 6-well plates; **~1,500 organoids** total.
- **Multiplexing/barcoding:** dissociation at days 72–74; multiplexed scRNA-seq via **split-pool combinatorial barcoding** (ref 36). 36,265 QC-passing cells across 46 conditions.
- **Fate annotation:** integration + **label transfer** from a high-resolution prenatal human brain atlas (ref 37); **VoxHunt** mapping to developing-mouse ISH; marker-gene confirmation; cluster-overlap scoring vs 550 primary CNS fetal clusters. Cerebellar cells re-mapped to a human fetal cerebellum dataset (ref 52).
- **Condition→cell-type deconvolution:** per-condition cell-composition heatmaps, similarity matrices, hierarchical clustering + PCA; **permutation testing** for morphogen↔neuronal-subcluster associations (morphogen map, Table S9).
- **Validation modalities:** IHC/immunocytochemistry, CUBIC tissue clearing + whole-mount SOX2/Ki67/cCas3, organoid silhouette/growth-rate/roundness imaging (Cellpose), qPCR (hypothalamic markers), RNAscope (TAC3 in PCW21 striatum), **MERFISH** (MERSCOPE/Vizgen) on assembloids, L7::GFP + CALB1 neurite tracing with **Sholl analysis**.
- **Transplantation:** stereotactic hCbO grafts (differentiation days 41–48) into cerebellar cortex of **postnatal-day 3–7 athymic (FOXN1−/−) rats**; longitudinal **T2-weighted MRI**; HNA/CALB1/SKOR2 IHC post-mortem.
- **Reference comparisons:** organoid Purkinje/CR transcriptomes vs stage-matched human fetal (PCW 9–17 cerebellum; PCW-matched CR) with GO-term enrichment — consistently showing lower in-vitro expression of dendritic-development / neuron-migration / cell-morphogenesis gene sets.

## Relevance to the brain-organoid ASD review
- **Directly addresses the AREALIZATION / regional-identity limitation.** Organoids are criticized for poor and variable areal/regional identity; this paper provides a *systematic, quantitative route to prescribed regional fates* — a morphogen→region map with defined timing windows (e.g., WNT before day 11 for medial pallium; graded SAG timing for dorsoventral IN identity) that can standardize which CNS region an organoid represents.
- **Expands the perturbation-platform repertoire (Stage 2/3 Build–Test).** An arrayed, multiplexed morphogen screen (46 conditions, split-pool scRNA-seq, atlas mapping) is a scalable Build–Test engine for prescribing and reading out cell-type composition — complementary to CRISPR screens in the same lab lineage (see meng 2023/2025).
- **Enables region-specific disease modeling.** Disease-gene enrichment analysis shows NDD/ASD/SCZ genes with cluster- and condition-restricted expression (e.g., EBF3, GATA3, NR4A2), arguing that phenotypes should be probed in the *correct regional cell type* — which this platform can now generate on demand.
- **New organoid/assembloid building blocks.** Provides validated protocols for hCbO (cerebellar), hMPOCR (medial pallium/CR), and hSOTAC3 (subpallial TAC3+ striatal IN) organoids, plus hMPOCR-hCO and hSOTAC3-hStrO assembloids — new regionalized parts for assembloid-based circuit and migration studies.
- **Maturation caveat reinforced.** Confirms a hard in-vitro maturation ceiling (Purkinje dendrites arrest at fusiform even at 6–8 months) that only in-vivo transplantation overcomes — relevant to review claims that organoid maturation limits ASD phenotype detection.
- **Primate/human-specific biology.** TAC3-INs are a striatal cell type present in primates but absent in mouse/ferret — an example of human/primate-specific neural diversity that organoids (not rodents) can access, strengthening the case for human organoid models.

## Open questions / limitations
- **Incomplete coverage:** with 46 conditions only a *fraction* of regional brain diversity was generated; a comprehensive human "morphogen map" needs many more conditions and larger cell numbers to detect rarer populations (authors state).
- **Missing in-vivo cues:** activity-dependent and other in-vivo processes shaping fate/maturation are absent in vitro; transplantation was required for Purkinje maturation.
- **Line/pluripotency dependence:** morphogen effects may depend on pluripotency state and cell line; broader cross-line validation is needed (only 2–4 lines per follow-up).
- **Reference-atlas dependence:** precise cell-type mapping is limited by the completeness/annotation of human neurodevelopmental atlases; only 65.1% of fetal clusters were matched.
- **In-vitro vs in-vivo transcriptomic gaps:** CR and Purkinje (and TAC3-IN) organoid cells show reduced expression of migration/morphogenesis/dendritic gene sets vs primary — organoid states are immature/imperfect copies.
- **No original code released;** reanalysis details available from lead contact on request.

## Related
- [Pașca 2015 — cortical spheroids (hCS foundation)](paca_2015_functional_cortical_neurons_astrocytes_human_pluripotent_stem.md)
- [Birey 2017 — forebrain assembloids / interneuron migration](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md)
- [Birey 2022 — molecular basis of human interneuron migration](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md)
- [Miura 2022 — engineering brain assembloids](miura_2022_engineering_brain_assembloids_to_interrogate.md)
- [Meng 2023 — assembloid CRISPR screens (disease genes)](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md)
- [Meng 2025 — CRISPR screens in human neural organoids/assembloids](meng_2025_crispr_screens_in_human_neural.md)
- [Velasco 2019 — reproducible individual brain organoids (regional identity)](velasco_2019_individual_brain_organoids_reproducibly.md)
- [Fleck 2021 — resolving organoid brain-region identities by mapping (VoxHunt)](fleck_2021_resolving_organoid_brain_region_identities_by_mapping.md)
- [Fleck 2023 — inferring/perturbing cell-fate regulomes](fleck_2023_inferring_perturbing_cell_fate_regulomes_human_brain.md)
- [Atamian 2024 — long-term organoid culture](atamian_2024_generation_and_long-term_culture_of.md)
- [Eura 2020 — brainstem organoids (regional)](eura_2020_brainstem_organoids_from_human_pluripotent.md)
- [Valiulahi 2021 — caudal-type serotonin neurons (rostrocaudal patterning)](valiulahi_2021_generation_of_caudal-type_serotonin_neurons.md)
- [Human 2026 — neuromodulatory (serotonin) assembloids](human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease.md)
- [Sloan 2018 — human assembly/oligodendrocyte spheroids](sloan_2018_generation_and_assembly_of_human.md)

- [Andersen 2023 — single-cell transcriptomic landscape of the developing human spinal cord](andersen_2023_singlecell_transcriptomic_landscape_developing_human_spinal_cord.md) — primary in-vivo fetal CNS reference (spinal cord) for benchmarking morphogen-guided regional organoids/assembloids (batch sibling).
