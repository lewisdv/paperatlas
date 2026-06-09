---
title: "Cortical organoids model early brain development disrupted by 16p11.2 copy number variants in autism."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41380-021-01243-6
pmid: 34433918
authors: Urresti J et al.
journal: Molecular psychiatry (2021)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/urresti_2021_cortical_organoids_model_early_brain_development_disrupted.pdf
pdf_status: downloaded
---

# Cortical organoids model early brain development disrupted by 16p11.2 copy number variants in autism.

## Source

- Authors: Urresti J, Zhang P, Moran-Losada P, Yu NK, Negraes PD, Trujillo CA, Antaki D, Amar M et al.
- Journal: Molecular psychiatry (2021)
- DOI: [10.1038/s41380-021-01243-6](https://doi.org/10.1038/s41380-021-01243-6)
- PMID: [34433918](https://pubmed.ncbi.nlm.nih.gov/34433918/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Reciprocal deletion and duplication of the 16p11.2 region is the most common copy number variation (CNV) associated with autism spectrum disorders. We generated cortical organoids from skin fibroblasts of patients with 16p11.2 CNV to investigate impacted neurodevelopmental processes. We show that organoid size recapitulates macrocephaly and microcephaly phenotypes observed in the patients with 16p11.2 deletions and duplications. The CNV dosage affects neuronal maturation, proliferation, and synapse number, in addition to its effect on organoid size. We demonstrate that 16p11.2 CNV alters the ratio of neurons to neural progenitors in organoids during early neurogenesis, with a significant excess of neurons and depletion of neural progenitors observed in deletions. Transcriptomic and proteomic profiling revealed multiple pathways dysregulated by the 16p11.2 CNV, including neuron migration, actin cytoskeleton, ion channel activity, synaptic-related functions, and Wnt signaling. The level of the active form of small GTPase RhoA was increased in both, deletions and duplications. Inhibition of RhoA activity rescued migration deficits, but not neurite outgrowth. This study provides insights into potential neurobiological mechanisms behind the 16p11.2 CNV during neocortical development.

## Key findings

- **Core claim: patient-derived 16p11.2 deletion (DEL) and duplication (DUP) cortical organoids reproduce the human mirror brain-size phenotype and converge on dysregulated RhoA signaling and neuronal migration — and the migration deficit is pharmacologically rescuable by RhoA inhibition.** This is the Table-1 16p11.2 organoid-ASD entry for the review.
- **Cohort: 6 male 16p11.2 CNV carriers selected for extreme head size + 3 unrelated male controls.** DEL carriers had macrocephaly (head-circumference Z +2.51 to +4.32); DUP carriers had microcephaly (Z −0.69 to −1.63). Fibroblasts → episomally reprogrammed iPSCs → cortical organoids; 2 clones/individual. Genotypes throughout: 3 DEL, 3 DUP, 3 CTRL.
- **Organoid size mirrors patient head size.** DEL organoids skew large, DUP skew small (significant DEL vs CTRL at late maturation/3M; DUP vs CTRL at induction/proliferation). By 3 months DEL organoids were "completely devoid of small organoids" and DUP had very few large ones (>100 organoids/genotype measured).
- **Organoids map to human mid-fetal cortex.** By CoNTExT/TMAP transcriptomic alignment: iPSCs ≈ embryonic/early-fetal (4–10 PCW); 1-month organoids ≈ early-to-late mid-fetal (13–24 PCW); 3-month organoids ≈ late mid-fetal to neonatal/early-infancy (19 PCW–6 mo). Laminar matching showed proliferative-zone→upper-layer transitions, more advanced at 3M — i.e. they model the mid-fetal window implicated in ASD/SCZ.
- **DEL = excess neurons + progenitor depletion; DUP = the mirror (excess progenitors).** Flow cytometry on dissociated 1M organoids: NeuN+ (neurons) significantly higher in DEL than DUP; TBR2+ (intermediate progenitors) and SOX2+ (radial glia) significantly higher in DUP. Confirmed by immunohistochemistry in 1M slices: significant Pax6+ progenitor **depletion** and NeuN+ neuron **enrichment** in DEL vs CTRL, with a mirror DUP-vs-DEL phenotype (DUP vs CTRL did not reach significance). DEL organoids also showed *decreased* proliferation at 1M (Fig. S23) — interpreted as the progenitor pool already exhausted by 1M after earlier accelerated proliferation. (Echoes the in vivo "premature neurogenesis depletes progenitors" logic of [Rash 2011](rash_2011_fgf_signaling_expands_embryonic_cortical_surface_area.md).)
- **Accelerated neuronal maturation, altered morphology, and more synapses in DEL.** Total neurite length increased in DEL vs CTRL (p = 0.009) and DEL vs DUP (p = 0.025); soma size increased in DEL vs CTRL (p = 0.034); DUP showed a non-significant decreasing neurite trend. Synaptic puncta (Synapsin-I, normalized to cells) significantly increased in DEL vs CTRL (p = 0.008). The neuronal/synaptic transcriptomic module (1M 46brown4; hub gene SCN2A) was upregulated in DEL.
- **Severe neuronal migration deficits in BOTH genotypes.** In a Matrigel outgrowth assay, ~40% of CTRL neurons migrated >200 µm along RG fibers vs only ~20% from DEL or DUP (DEL vs CTRL p = 0.038; DUP vs CTRL p = 0.073); confirmed by live imaging and by an orthogonal Boyden-chamber assay (lower migrating fraction in both). Migrating cells were verified to be neurons, not progenitors.
- **Active RhoA (RhoA-GTP) is elevated in both DEL and DUP.** By Western blot of 1M organoids: KCTD13 protein decreased in DEL vs CTRL (p = 0.018) with the opposite DEL-vs-DUP trend (p = 0.0013), tracking CNV dosage; total RhoA changed in DEL vs DUP (p = 0.01); but **active RhoA-GTP was significantly UP in both genotypes** (DEL vs CTRL p = 0.005; DUP vs CTRL p = 0.01). Proposed route: 16p11.2 contains KCTD13, an adapter for the Cul3 ubiquitin ligase whose substrate is RhoA → altered KCTD13 dosage dysregulates RhoA. RhoA over-activation is known to stall cortical neuron migration.
- **RhoA inhibition rescues migration but NOT neurite length.** Constitutive treatment with the RhoA inhibitor **Rhosin (1 µM, from day 6 to day 30)** rescued migration in both DEL and DUP to levels indistinguishable from vehicle CTRL (DEL_Rh vs CTRL_Vh p = 0.85; DUP_Rh vs CTRL_Vh p = 0.73), replicated by Boyden chamber. The increased DEL neurite length was **not** rescued (Fig. S31) — attributed to Rhosin itself promoting neurite outgrowth, implying neurite length depends on other (e.g. Wnt) pathways. This dissociates migration (RhoA-dependent, rescuable) from neurite outgrowth (RhoA-independent).
- **Multi-omic convergence on migration / actin / synapse / ion-channel / Wnt pathways.** DEG counts (10% FDR): e.g. 1M organoids 132/35/118 (DEL-vs-CTRL / DUP-vs-CTRL / DUP-vs-DEL). DEPs by TMT-MS often equaled or exceeded DEGs (e.g. 1M DEL-vs-CTRL 517 DEPs). WGCNA/WPCNA modules for migration (1M 22darkgreen, down in DEL; 3M 32violet, up in DUP) and neuronal/synaptic (1M 46brown4, up in DEL; 3M 25orange, down in DUP) were anticorrelated by genotype and **preserved at the protein level**. Co-expression modules were enriched in high-confidence SFARI ASD genes, pLI>0.99 / constrained genes, and CHD8/FMRP targets; DEGs overlapped idiopathic-ASD and CHD8-KO organoid signatures but **not** 16p11.2-carrier lymphoblastoid lines (blood vs brain distinction).

## Methods

- **Cellular models:** skin fibroblasts from 16p11.2 DEL/DUP carriers + controls → iPSCs by episomal reprogramming (QC: immunofluorescence, RT-qPCR pluripotency, SNP-array to confirm CNV and rule out new CNVs); 2 clones/individual; cortical organoids by the Trujillo et al. protocol.
- **Cortical organoid protocol (key steps):** feeder-free iPSCs (mTeSR1) → Accutase single cells → spheres in mTeSR1 + 10 µM SB431542 + 1 µM dorsomorphin + 5 µM ROCK inhibitor (95 rpm rotation, 24 h) → mTeSR1 (48 h) → **Media1** (Neurobasal/Glutamax/Gem21/N2 + SB + dorso, 7 d) → **Media2 + 20 ng/mL FGF2** (7 d) → **Media2 + 20 ng/mL FGF2 + 20 ng/mL EGF** (7 d) → **Media3** (+BDNF/GDNF/NT-3 10 ng/mL each, ascorbic acid, dibutyryl-cAMP, 7 d) → maintained in Media2. Each plate held one DEL + one DUP + one CTRL ("batch") to control batch effects. (Note: FGF2/EGF in this protocol ties directly to the FGF neurogenic-window mechanism of [Rash 2011](rash_2011_fgf_signaling_expands_embryonic_cortical_surface_area.md).)
- **Time points / sampling:** D6 (induction), D16 (proliferation), 1M (early maturation), 3M (late maturation); 108 RNA-seq samples (iPSC/1M/3M × 36 each); paired TMT-MS proteomics (10-plex, Orbitrap; 6126 proteins at 1M, 5481 at 3M).
- **Cellular assays:** flow cytometry (NeuN/TBR2/SOX2; 50,000 events/sample); IHC on 20 µm cryosections (Pax6, NeuN, MAP2, Synapsin-I, βIII-tubulin, Ki67, SOX2; EdU); neurite/soma morphology (MAP2, dissociated neurons on poly-ornithine/laminin); proliferation via EdU/Ki67.
- **Migration assays (two orthogonal):** (1) intact organoids on Matrigel-coated plates, count + distance at 72 h, plus live imaging (15-min intervals); (2) Boyden chamber — ~3×10^5 dissociated cells on 8 µm inserts, FGF2 20 ng/mL + BDNF 10 ng/mL as chemoattractants, 24 h.
- **RhoA biology:** Western blot for KCTD13, total RhoA, active RhoA-GTP (actin loading control); pharmacological rescue with **Rhosin 1 µM from D6→D30** (vehicle = 0.1% DMSO).
- **Bioinformatics:** limma-voom with duplicateCorrelation (clones/replicates); WGCNA/WPCNA; GO enrichment; CoNTExT/TMAP developmental staging; curated ASD/synaptic gene-list enrichment. Investigators blinded for quantifiable experiments; one-way ANOVA (Tukey) / two-way ANOVA.
- **Limitations baked into design:** only male carriers (sample availability); patients selected for *extreme* head size (severe tail); unrelated (non-isogenic) controls.

## Relevance to the brain-organoid ASD review

- **Primary Table-1 entry for 16p11.2 CNV organoid modeling.** Supplies the canonical demonstration that the most common ASD-associated CNV produces *dosage-dependent, mirror-image* cellular phenotypes (DEL macrocephaly/excess neurons vs DUP microcephaly/excess progenitors) in patient-derived cortical organoids — i.e. a programmable CNV → cell-biology readout.
- **RhoA / migration as a convergent, druggable node.** The active-RhoA elevation in *both* genotypes plus the Rhosin rescue of migration gives the review a concrete perturbation-and-rescue example for the "migration vulnerability stage" and "proactive/programmable" thesis: a defined molecular target (RhoA, via KCTD13–Cul3) whose inhibition reverses a developmental phenotype.
- **Migration-vulnerability-stage support.** Directly evidences impaired tangential/radial-glia-guided neuronal migration during the modeled mid-fetal window — converging with assembloid CRISPR migration hits ([Meng 2023](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md)), oRG cytoskeletal/migration control ([Andrews 2020](andrews_2020_mtor_signaling_regulates_morphology_migration_outer_radial.md)), interneuron tangential migration ([Birey 2022](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md)), and the hypermotile-cIN migration phenotype in [Tenreiro 2025](tenreiro_2025_mecp2_regulates_telencephalic_development_human_cerebral_organoids.md).
- **Progenitor/neuron balance links to the FGF/Notch neurogenic window.** The DEL excess-neuron/progenitor-depletion phenotype is the human-organoid analogue of premature neurogenesis depleting the progenitor pool described in mouse by [Rash 2011](rash_2011_fgf_signaling_expands_embryonic_cortical_surface_area.md); the standard FGF2/EGF expansion step in this protocol is the experimentally tunable handle on that balance.
- **Cross-ASD convergence.** DEG/module overlap with idiopathic-ASD organoids ([Mariani 2015](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md), [Paulsen 2022](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md)) and CHD8 models ([Villa 2022](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md)) supports the review's argument that distinct ASD genetic subtypes converge on shared neuronal/synaptic/migration programs — and that organoids capture brain-specific (not blood) signatures.
- **Same-lab platform lineage.** Muotri-lab cortical-organoid platform (calcium/network and CNV modeling) shared with [Tenreiro 2025](tenreiro_2025_mecp2_regulates_telencephalic_development_human_cerebral_organoids.md), giving methodological continuity across the review's ASD-gene entries.

## Open questions / limitations

- **Male-only, extreme-phenotype, non-isogenic cohort.** Restricted to males; carriers chosen for extreme macro-/microcephaly (severe tail of the spectrum); controls are unrelated rather than isogenic/CRISPR-corrected, so background genetic variation is not excluded.
- **Proliferation timing inferred, not directly captured.** Decreased DEL proliferation at 1M is interpreted as the aftermath of earlier accelerated proliferation, but earlier time points (iPSC/NPC) were not assayed to demonstrate the acceleration → progenitor-depletion sequence directly.
- **Pathway attribution is correlative/polygenic.** With 29 genes in the locus plus hundreds of downstream DEGs, the specific causal gene(s) are not isolated; RhoA is implicated mechanistically and via rescue, but DUP shows elevated RhoA-GTP despite (trend) increased KCTD13, so the KCTD13→RhoA logic is not fully linear and other genes/pathways (MAPK/ERK via MAPK3/MVP/TAOK2, Wnt) likely contribute.
- **Neurite phenotype unexplained mechanistically.** Increased DEL neurite length is RhoA-independent (not rescued by Rhosin); the responsible pathway (Wnt cross-talk proposed) is not established.
- **Organoid maturation ceiling.** Models map only to mid-fetal/early-postnatal stages; later maturation, microcircuit function, and in vivo correspondence (e.g. the patchy cortical disorganization seen in postmortem ASD) are inferred, not measured.
- **DUP-vs-CTRL effects often sub-threshold.** Several DUP phenotypes are clearest only in the DUP-vs-DEL contrast, limiting interpretation of duplication-specific biology.

## Related

- [Tenreiro 2025 — MeCP2 telencephalic development (hypermotile cIN migration; same lab platform)](tenreiro_2025_mecp2_regulates_telencephalic_development_human_cerebral_organoids.md)
- [Rash 2011 — FGF/Notch control of the cortical neurogenic window (progenitor/neuron balance)](rash_2011_fgf_signaling_expands_embryonic_cortical_surface_area.md)
- [Andrews 2020 — mTOR/CDC42/actin control of oRG morphology and migration (rescue logic)](andrews_2020_mtor_signaling_regulates_morphology_migration_outer_radial.md)
- [Meng 2023 — Assembloid CRISPR screens reveal disease-gene impact on interneuron migration](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md)
- [Birey 2022 — Molecular basis of human interneuron migration in forebrain assembloids](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md)
- [Shcheglovitov 2013 — SHANK3/22q13.3 synaptic deficits and rescue (CNV perturbation-and-rescue)](shcheglovitov_2013_shank3_igf1_restore_synaptic_deficits_neurons_22q13.md)
- [Villa 2022 — CHD8 haploinsufficiency alters excitatory neurons in organoids](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md)
- [Paulsen 2022 — Autism genes converge on asynchronous development of shared neuron classes](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md)
- [Mariani 2015 — FOXG1-dependent GABA/glutamate dysregulation in idiopathic-ASD organoids](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md)
- [Li 2023 — Single-cell brain-organoid CRISPR screen of ASD genes](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md)
- Concept: [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- Entity: [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)
