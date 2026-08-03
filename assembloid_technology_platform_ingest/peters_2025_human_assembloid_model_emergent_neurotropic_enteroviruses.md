---
title: "Human Assembloid Model of Emergent Neurotropic Enteroviruses"
kind: paper
status: ingested
added: 2026-07-01
deep_ingested: 2026-07-01
doi: 10.1101/2025.11.18.689148
pmid: 41332624
authors: Peters CE et al.
journal: bioRxiv preprint (2025)
source_ref: assembloid-technology-platform (Pașca lab batch)
raw_source: collections/Organoid/raw/sources/peters_2025_human_assembloid_model_emergent_neurotropic_enteroviruses.pdf
pdf_status: downloaded
---

# Human Assembloid Model of Emergent Neurotropic Enteroviruses

## Source
- Authors (co-first, equal contribution): **Christine E. Peters, Jimena Andersen, Min-Yin Li**; then Lauren Varanese, Mayuri Vijay Thete, Se-Jin Yoon, Taylor Pio, Nicholas Thom, Xiaoyu Chen, Wenjie Qiao; senior/corresponding authors **Jan E. Carette** (Microbiology & Immunology, Stanford — virology) and **Sergiu P. Pașca** (Psychiatry & Behavioral Sciences / Stanford Brain Organogenesis Program — organoid/assembloid). J. Andersen now at Emory (Human Genetics). ~11 authors total.
- Journal: **bioRxiv preprint (2025)** — **not peer-reviewed** (posted 19 Nov 2025; CC-BY 4.0).
- DOI: [10.1101/2025.11.18.689148](https://doi.org/10.1101/2025.11.18.689148)
- PMID: [41332624](https://pubmed.ncbi.nlm.nih.gov/41332624/)
- Added via: assembloid-technology-platform batch ingest.

> **Preprint caveat:** All quantitative claims below are from a non-peer-reviewed preprint and should be treated as provisional.

## Abstract
Enteroviruses (EVs) are the leading cause of viral meningitis in children. Recent outbreaks of non-polio EVs — most notably EV-A71 and EV-D68 — have been associated with a polio-like paralysis, acute flaccid myelitis (AFM). The lack of models that mimic the cellular and functional responses of these human-restricted pathogens has hampered treatment development. The authors previously engineered human stem-cell-derived assembloids recapitulating neuromuscular connections underlying muscle contraction by integrating human spinal cord/hindbrain organoids (hSpO) with human skeletal muscle (hSkM). Here they used organoids and assembloids to investigate polio and non-polio EV pathogenesis. Infection of assembloids with poliovirus (PV), EV-D68, and EV-A71 caused loss of muscle contraction for all three viruses, preventable by antiviral treatment. Yet despite convergence on neuronal dysfunction, the cellular targets differed: single-cell transcriptomics uncovered divergent cell tropisms, and live imaging revealed different modes and kinetics of cell damage. The result is a multi-cellular model capturing viral pathogenesis in a human, circuit-relevant context.

## Key findings
*(All numbers from a bioRxiv preprint — provisional.)*

- **Three neurotropic enteroviruses modeled**: poliovirus type 1 (PV-1 Mahoney), EV-A71 (BrCr strain), and EV-D68 (2014 outbreak isolate US/IL/14-18952, "IL"). All three cause AFM but use different receptors and primary infection sites.
- **Assembloid platform = hSpO–hSkM** (human spinal cord/hindbrain organoid + 3D human skeletal muscle), a functional neuromuscular-circuit model from a prior Pașca-lab study (Andersen et al. 2020, *Cell*). Assembloids were integrated ~2 weeks (min. 10 d) before infection (defined as day 0).
- **All three EVs abolished spontaneous muscle contraction** over ~1 week (quantified at d0/d2/d8; readout = MUSCLEMOTION pixel-displacement events over a 2-min window; each 931×931 µm field split into 4 subfields). Effect reproduced across multiple hiPS lines (**n = 4 hiPS lines** total across experiments).
- **Antiviral rescue**: rupintrivir (1 µM; viral 3C protease inhibitor, broad anti-picornavirus) **prevented loss of contractions**, establishing that paralysis was virus-replication-dependent.
- **Viral antigen localized to the hSpO (neural) region**, not muscle — detected by immunostaining at 2 dpi (anti-dsRNA; anti-EV-D68 VP1; panEV antibody).
- **Productive replication in hSpO, but PV replicates most robustly.** By qRT-PCR (intracellular viral RNA vs rupintrivir-treated baseline): at **1 dpi already >2,000-fold** above baseline for **PV**, vs **~20-fold** for EV-D68 and EV-A71. **PV RNA peaked at >100-fold increase** from 1 dpi. Extracellular titer (plaque assay): EV-D68 and EV-A71 produced **>2 log lower** titer than PV; net progeny release above input appeared only later (PV early; EV-D68 ~8 d; EV-A71 ~2–4 d).
- **Divergent cell tropism (scRNA-seq, 10x, 2 dpi).** Fraction of cells with high viral RNA consistent with active replication: **PV 3.85%, EV-D68 5.87%, EV-A71 5.95%** (averaged across runs). **PV and EV-D68 preferentially infect motor neurons (MN, PHOX2B+/ISL1+) and other neuronal types; EV-A71 preferentially infects glial lineages (astroglia).** All three infect MNs; MN cluster carried the highest viral load across EVs (EV-A71 also high in cycling/astroglia clusters). Overall cell-type composition was unchanged by infection.
- **Reporter-virus live imaging confirms tropism.** Of hSyn1-mScarlet+ neurons: **~56% PV-mNeon+, ~28% EV-D68-GFP+, ~3% EV-A71-mNeon+**. Of EV-infected cells co-labeled with the glial reporter AdV-CMV-mCherry: **~54% for EV-A71** vs **~21% for PV** and **~3% for EV-D68** (AdV labels ~80% glial / <20% neuronal). EV-A71 also altered astroglial morphology (GFAP) at 4 dpi; PV/EV-D68 did not.
- **Distinct modes/kinetics of cell damage (48-h live imaging).** Damage binned as intact vs. fragmented vs. rounded-up. **PV: >50% of infected cell bodies remained intact.** **EV-D68: fragmented bodies >60%** of infected cells. **EV-A71: "rounded up" was the dominant phenotype.** MN (PHOX2B+) numbers dropped over 10 d for all EVs, most rapidly with PV.
- **Cytotoxicity (LDH release over 10 d) diverges from replication.** Peak cytotoxicity: **PV ~40% at 10 dpi**; **EV-A71 ~60% at 10 dpi (largest)**; **EV-D68 minimal (~1.7-fold over rupintrivir baseline at 10 dpi)** despite visible cell fragmentation.
- **Apoptosis: cell-autonomous (PV) vs. non-cell-autonomous (EV-A71).** Cleaved caspase-3 (clCASP3+) significantly increased at 2 dpi for PV and EV-A71 (not significant for EV-D68). For **PV**, apoptotic cells mostly co-localized with viral antigen (cell-autonomous). For **EV-A71**, clCASP3+ cells appeared in both infected *and* uninfected cells — suggesting **non-cell-autonomous killing** (authors speculate astrocyte infection may drive indirect neurotoxicity, cf. Guttenplan 2021 reactive astrocytes).
- **Innate immune response despite no immune cells.** A Luminex 80-plex panel showed increased proinflammatory cytokines (**IL-6, IL-8, CCL5/RANTES**) with all three EVs. Notably **no strong type I (IFN-α2), II (IFN-γ), or III (IFN-λ2) interferon** induction — consistent with EV IFN-antagonism and the absence of microglia/immune cells.
- **Overall model claim**: divergent tropism and damage modes **converge on neuronal dysfunction → paralysis**, recapitulating human AFM neuropathology in a human, circuit-relevant system that overcomes mouse refractoriness to human EVs.

## Methods
- **Models**: hSpO differentiated from hiPS cells (dual-SMAD + WNT/CHIR + RA + SHH/SAG patterning; DAPT for neurogenesis; standard Pașca-lab protocol, Andersen 2020 / Yoon 2019). 3D hSkM from commercial human skeletal myoblasts (Thermo A11440) in Geltrex, differentiated ≥14 d. **hSpO–hSkM assembloids**: hSpO (differentiation d28–32) placed in contact with 3D hSkM on transwell inserts, integrated ≥10 d; **only assembloids with baseline spontaneous contractions were used — 56/121 screened**. hSpO for organoid infections used at **differentiation d76–125** (4 hiPS lines from healthy subjects; Stanford IRB-approved).
- **Viruses/strains**: PV-1 Mahoney (gift, H. Ploegh; titred on H1-HeLa); EV-A71 BrCr (ATCC; titred on RD, 37 °C); EV-D68 US/IL/14-18952 (BEI NR-49131; titred on RD, 34 °C). **Fluorescent reporter viruses** built by inserting eGFP or mNeon after the 5′UTR + a 2A cleavage site upstream of the polyprotein (strategy from CV-B3, Lanke 2009): PV-mNeon-GPI, EV-D68-GFP, EV-A71-mNeon (from infectious clones; T7 in-vitro-transcribed RNA; electroporated into H1-HeLa+CDHR3 or RD cells).
- **Infection doses (per organoid/assembloid)**: **PV 10⁴ PFU, EV-A71 10⁴ PFU, EV-D68 10⁵ PFU**. Antiviral: 1 µM rupintrivir, re-dosed every 2 d.
- **Readouts**: (1) spontaneous-contraction live imaging (Leica SP8/Stellaris 5; 2 min at 14.7 fps; every 2 d for 8 d; MUSCLEMOTION + custom MATLAB event detection, >4 SD). (2) qRT-PCR of intracellular viral RNA (normalized to actin; 2 hSpO pooled/sample). (3) Plaque/FFU assays on supernatants (H1-HeLa for PV; RD for EV-A71/EV-D68). (4) Luminex 80-plex cytokine panel (Stanford HIMC). (5) IHC: anti-dsRNA (rJ2), EV-D68 VP1, panEV L66J, clCASP3, GFAP, PHOX2B, MAP2, SPARCL1. (6) LDH-Glo cytotoxicity (Triton-X = 100% max release). (7) Live imaging with reporter viruses + neuronal (AAV1-hSyn1-mScarlet) or glial (AdV-CMV-mCherry) labels; imaged 1 h intervals for 16–48 h.
- **scRNA-seq**: 10x Chromium 3′ v3; infected 2 dpi; **hSpO from 2 hiPS lines across 4 differentiations** (infected d62/d80/d98/d68; 5 organoids pooled/condition). Cell Ranger v6 aligned to a combined human GRCh38.98 + PV (NC_002058.3) + EV-A71 (U22521.1) + EV-D68 (KM851230.1) reference. Seurat v5 + SCTransform + Harmony (by hiPS line + run); label transfer from Andersen 2020 hSpO reference. **Cell counts after QC: 34,184 uninfected; 27,278 PV; 14,609 EV-D68; 29,596 EV-A71.** Virus-positive vs -negative cells set by kernel-density first-local-minimum thresholding of bimodal viral-read distributions.
- **Timepoints**: infection courses at 1, 2, 4, 6, 8, 10 dpi (organoids); d0/d2/d8 for assembloid contractions.
- **Stats**: one-/two-way ANOVA with Holm–Sidak or Benjamini–Hochberg correction; GraphPad Prism 10.
- **Funding/COI**: NIH R01AI169467 (Pașca + Carette) and others; Stanford holds patents on regionalized neural organoids/assembloids (Pașca, Andersen listed as inventors).

## Relevance to the brain-organoid ASD review
- **Primarily a disease-modeling / assembloid-application exemplar** — demonstrates region-specific human neural organoids + assembloids as a platform for human neural *pathology* (here viral neuropathogenesis / AFM), not ASD genetics.
- **Supports the manuscript's assembloid-platform framing**: shows the same hSpO–hSkM neuromuscular assembloid architecture (used elsewhere for circuit/perturbation studies) generalizes to a functional readout (muscle contraction) that reports on neuronal health — reinforcing assembloids as a perturbation-and-readout system for human neural circuits.
- **Tangential to ASD.** No ASD genes, risk variants, or neurodevelopmental-disorder phenotypes are studied. Relevance is methodological (Pașca-lab region-specific human neural models) rather than mechanistic.
- **Modest cross-utility**: illustrates that assembloids capture non-cell-autonomous effects and multi-cell-type interactions (e.g., glia→neuron), a theme relevant to ASD models that emphasize cell-type-specific and circuit-level contributions.

## Open questions / limitations
- **Preprint — not peer-reviewed** (bioRxiv, Nov 2025); all findings provisional.
- **Author-stated limitations**: (1) organoids/assembloids are a *developmental* model of neuromuscular connections — lacks mature cell types such as myelinating oligodendrocytes. (2) Neural organoids **lack microglia and infiltrating immune cells** — engraftment/transplantation approaches would be needed to study immune contributions (relevant to interpreting the muted IFN response). (3) **One strain per EV** was tested; non-polio EV neuropathogenesis may be strain-dependent (cf. Aguglia 2023, Dabilla 2025 showing EV-D68 strain-specific tropism).
- **Noted (ingest)**: mechanism linking cell-type tropism to circuit-level paralysis is correlative; the causal chain from astroglial EV-A71 infection to non-cell-autonomous neuronal death is proposed but not directly proven. Antiviral testing limited to a single agent (rupintrivir). Contraction "events" and damage-bin quantification rely on custom thresholds. Findings are in *developmental*-stage human neural tissue, not adult spinal cord.

## Related
- [Andersen 2020 (*Cell*), "Generation of Functional Human 3D Cortico-Motor Assembloids"] — foundational hSpO / hSpO–hSkM neuromuscular assembloid protocol this study builds on; **not yet ingested** into this collection (add if source becomes available).
- [Andersen 2023 — single-cell transcriptomic landscape of the developing human spinal cord](andersen_2023_singlecell_transcriptomic_landscape_developing_human_spinal_cord.md) — primary in-vivo fetal spinal-cord reference for the hSpO used here (same lab; batch sibling).
- [Assembloids and regional fusion (entity)](../entities/assembloids-and-regional-fusion.md)
- [Brain-organoid patterning and assembloids (concept)](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Birey 2017 — Assembly of functionally integrated human forebrain spheroids](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md) (founding assembloid paper, Pașca lab)
- [Miura 2022 — Engineering brain assembloids to interrogate...](miura_2022_engineering_brain_assembloids_to_interrogate.md)
- [Meng 2023 — Assembloid CRISPR screens reveal impact of disease genes](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md) (Pașca-lab assembloid perturbation platform)
- [Paca 2015 — Functional cortical neurons and astrocytes from human pluripotent stem cells](paca_2015_functional_cortical_neurons_astrocytes_human_pluripotent_stem.md)
- [Schafer 2023 — in vivo neuroimmune organoid model of human microglia](schafer_2023_vivo_neuroimmune_organoid_model_study_human_microglia.md) (relevant to the "no microglia" limitation)
