---
title: "Assembloid CRISPR screens reveal impact of disease genes in human neurodevelopment."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41586-023-06564-w
pmid: 37758944
authors: Meng X et al.
journal: Nature (2023)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.pdf
pdf_status: downloaded
---

# Assembloid CRISPR screens reveal impact of disease genes in human neurodevelopment.

## Source

- Authors: Meng X, Yao D, Imaizumi K, Chen X, Kelley KW, Reis N, Thete MV, Arjun McKinney A et al. (senior author Sergiu P. Pașca; Stanford / UCSF / Bassik lab).
- Journal: Nature 622, 359–366 (12 October 2023). Open access.
- DOI: [10.1038/s41586-023-06564-w](https://doi.org/10.1038/s41586-023-06564-w)
- PMID: [37758944](https://pubmed.ncbi.nlm.nih.gov/37758944/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

The assembly of cortical circuits involves the generation and migration of interneurons from the ventral to the dorsal forebrain1-3, which has been challenging to study at inaccessible stages of late gestation and early postnatal human development4. Autism spectrum disorder and other neurodevelopmental disorders (NDDs) have been associated with abnormal cortical interneuron development5, but which of these NDD genes affect interneuron generation and migration, and how they mediate these effects remains unknown. We previously developed a platform to study interneuron development and migration in subpallial organoids and forebrain assembloids6. Here we integrate assembloids with CRISPR screening to investigate the involvement of 425 NDD genes in human interneuron development. The first screen aimed at interneuron generation revealed 13 candidate genes, including CSDE1 and SMAD4. We subsequently conducted an interneuron migration screen in more than 1,000 forebrain assembloids that identified 33 candidate genes, including cytoskeleton-related genes and the endoplasmic reticulum-related gene LNPK. We discovered that, during interneuron migration, the endoplasmic reticulum is displaced along the leading neuronal branch before nuclear translocation. LNPK deletion interfered with this endoplasmic reticulum displacement and resulted in abnormal migration. These results highlight the power of this CRISPR-assembloid platform to systematically map NDD genes onto human development and reveal disease mechanisms.

## Key findings

- **Pooled CRISPR loss-of-function screen of NDD genes in human forebrain assembloids.** Starting gene list = 611 ASD/NDD genes (from exome/GWAS studies and SFARI scores 1, 2, syndromic); after filtering for expression in human subpallial-organoid (hSO) interneuron-lineage cells (`Dlxi1/2b::eGFP+`) and human postconception week 8–9 ganglionic eminences, **425 genes** were screened (354 ASD + 71 other-NDD).
- **Overall hit rate: 46 of 425 NDD genes (~11%) perturb interneuron development** (13 generation + 33 migration candidates).
- **Interneuron generation screen → 13 candidate genes.** Read out by FACS of `Dlxi1/2b::eGFP+` vs eGFP– cells in hSO at day 44 of differentiation; hits called when ≥2 sgRNAs had effect ≤ −1.57 or ≥ +1.57 (≈2× s.d. of negative controls). Hits include **CSDE1, SMAD4, SYNCRIP, FOXG1**, cell-cycle genes **PPP2R1A and PPM1D**, NAA10, PPP2R1A.
- **Interneuron migration screen → 33 candidate genes**, run in **>1,000 forebrain assembloids (hFA)** at ~500-migrated-cell coverage per sgRNA; hits called at ≥2 sgRNAs with effect ≤ −2.5 or ≥ +2.5. Hits enriched for cytoskeleton/cell-migration genes — **NCKAP1, SEMA5A, PRKD1, RAC1** — plus telomere gene **TERF2** and ER-shaping gene **LNPK**.
- **SMAD4 and CSDE1 are required for subpallial (interneuron) differentiation.** KO hSO had reduced `Dlxi1/2b::eGFP+` fractions (****P < 0.0001), whereas SYNCRIP KO did not (P = 0.87); validated across three hiPS lines (1205-4, 2242-1, 1208-2) and in SMAD4 heterozygous lines. KO organoids were smaller (P < 0.01), showed strongly reduced DLX2, lost MGE markers (NKX2.1, LHX6, LHX8, SOX6) and gained caudal-ganglionic-eminence markers (NR2F1, NR2F2, PROX1); CSDE1 KO also upregulated the preoptic marker DBX1.
- **TERF2 and LNPK are required for interneuron migration, not generation.** LNPK/TERF2 KO did not change eGFP+ fraction or organoid size, but reduced mean `Dlxi1/2b::eGFP` intensity in the hCO compartment of hFA (LNPK KO *P = 0.0428; TERF2 KO *P = 0.0225), i.e. fewer interneurons reached the cortical side.
- **LNPK loss impairs saltatory migration** — reduced saltation length (****P < 0.0001) and speed (**P = 0.0021) of `Dlxi1/2b::eGFP+` cells. Confirmed acutely with an LNPK antisense oligonucleotide (ASO: −85% mRNA, −70% protein) and in mouse E13–14 ganglionic-eminence slices via Lnpk CRISPR (ruling out a purely developmental cause). LNPK has reported homozygous loss-of-function in patients with severe epilepsy.
- **New cell biology — ER displacement precedes nucleokinesis.** Using a SEC61B-mEGFP ER reporter, a large fraction of the ER moves forward (taking a linear then compact conformation) along the leading branch *before* nuclear translocation, seen in **75% of saltatory cells on the hSO side and 88% on the hCO side** (*P = 0.041). LNPK KO (and KO of a second ER-shaping gene, **ATL1/atlastin-1**) reduced the fraction of cells showing this ER displacement (LNPK **P = 0.004; ATL1 **P = 0.0029) and shortened saltation length — implicating ER dynamics as an essential, previously unappreciated step in human interneuron migration.

## Methods

- **Platform: subpallial organoids (hSO, MGE-like) fused with cortical organoids (hCO) into forebrain assembloids (hFA)** from hiPS cells, extending the Pașca-lab interneuron-migration model (Birey 2017; see also Sloan 2018, Miura 2022).
- **Engineered cell line:** clonal Tet-Off `CAG::Cas9` knock-in at the AAVS1 locus, further modified to express `Dlxi1/2b::eGFP` (validated MGE-lineage enhancer reporter). No Cas9-induced apoptosis detected (cleaved-Caspase3).
- **sgRNA library:** 5 sgRNAs/candidate + 13 known interneuron genes + safe-harbour negative controls (218 control sgRNAs; ~2,400 sgRNAs total), lentivirally delivered (mCherry marker) at 1,000× coverage; mCherry+ cells FACS-sorted then differentiated.
- **Hit calling:** casTLE effect size and score; candidates required ≥2 concordant sgRNAs beyond ~2× s.d. of negative-control distribution. Screens compare *proportional* sgRNA enrichment between cell populations of interest (eGFP+ vs eGFP–; migrated vs non-migrated), which suppresses survival/proliferation confounds.
- **Timing:** hSO collected day 44 for generation screen; for migration, day-60 hCO fused with day-45 perturbed hSO, 30-day migration window, then the two compartments separated and FACS-sorted.
- **Validation:** RNP-based KO pools (3 sgRNAs/gene; >96% amplicons with partial deletion) in multiple hiPS lines, including heterozygous SMAD4 lines; flow cytometry, RT–qPCR transcription-factor panels, CUBIC clearing + 3D reconstruction, confocal live imaging of saltatory migration, LNPK ASO, and mouse GE electroporation.

## Relevance to the brain-organoid ASD review

- **Canonical example of pooled perturbation in 3D / assembloid CRISPR screening** — directly supports the review's "assembloid CRISPR screens" and "perturbation in 3D" themes. Demonstrates that hundreds of NDD/ASD genes can be functionally mapped onto specific, late, otherwise-inaccessible stages of human interneuron development (generation and long-range migration into cortex) inside assembloids.
- Provides a concrete **methodological template** for the proposed "programmable" organoid pipeline: doxycycline-controllable Cas9 line + lineage reporter (`Dlxi1/2b::eGFP`) + pooled lentiviral library + compartment-resolved FACS readout + casTLE analysis.
- Companion protocol page: [Meng 2025, *CRISPR screens in human neural organoids and assembloids*](meng_2025_crispr_screens_in_human_neural.md) — step-by-step version of this platform.
- **Mechanistic ASD biology:** flags interneuron generation/migration regulators (SMAD4, CSDE1, FOXG1, NCKAP1, SEMA5A, PRKD1, RAC1) and uncovers ER dynamics (LNPK, ATL1) as a migration mechanism, expanding the cytoskeleton-centric view of NDD interneuronopathies.
- **Caveats for the review:** screen captures early generation/migration, not circuit integration or interneuron-subtype diversity, and uses MGE-like hSO only (see limitations below).

## Open questions / limitations

- Long-term assembloid culture caps the number of genes/stages testable; automation and faster interneuron maturation are needed to scale.
- hSO resemble the MGE only; cell-type-specific NDD effects in other GABAergic lineages (e.g. CGE-derived) are not captured.
- Non-cell-autonomous contributions to interneuron generation/migration from endothelial cells, oligodendrocytes, and other niches are not modeled.
- Hits rest on proportional enrichment vs negative controls; false positives/negatives from off-target or non-cell-autonomous effects cannot be excluded.
- Screens model generation and migration toward cortex (early development); post-migratory maturation, circuit assembly, and final laminar positioning of interneurons remain unscreened.

## Related

- [Meng 2025 — CRISPR screens in human neural organoids and assembloids](meng_2025_crispr_screens_in_human_neural.md)
- [Birey 2017 — Assembly of functionally integrated human forebrain spheroids](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md)
- [Birey 2022 — Molecular basis of human interneuron migration in Timothy-syndrome forebrain assembloids](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md)
- [Sloan 2018 — Generation and assembly of human brain region-specific 3D cultures](sloan_2018_generation_and_assembly_of_human.md)
- [Miura 2022 — Engineering brain assembloids to interrogate human neural circuits](miura_2022_engineering_brain_assembloids_to_interrogate.md)
- [Esk 2020 — Human tissue screen identifies an ER-secretion regulator as a brain-size determinant](esk_2020_human_tissue_screen_identifies_regulator_er_secretion.md)
- [Li 2023 — Single-cell brain-organoid screening of developmental genes](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md)
- [Fleck 2023 — Inferring and perturbing cell-fate regulomes in human brain organoids](fleck_2023_inferring_perturbing_cell_fate_regulomes_human_brain.md)
- [Paulsen 2022 — Autism genes converge on asynchronous development of shared neuron classes](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md)
- Concept: [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- Entity: [Assembloids and regional fusion](../entities/assembloids-and-regional-fusion.md), [CRISPR-Cas9 and next-generation CRISPR editing](../entities/crispr-cas9-and-next-generation-crispr-editing.md)
