---
title: "FOXG1-Dependent Dysregulation of GABA/Glutamate Neuron Differentiation in Autism Spectrum Disorders."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1016/j.cell.2015.06.034
pmid: 26186191
authors: Mariani J et al.
journal: Cell (2015)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.pdf
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# FOXG1-Dependent Dysregulation of GABA/Glutamate Neuron Differentiation in Autism Spectrum Disorders.

## Source

- Authors: Mariani J, Coppola G (co-first), Zhang P, Abyzov A, Provini L, Tomasini L, Amenduni M, Szekely A, Palejev D, Wilson M, Gerstein M, Grigorenko EL, Chawarska K, Pelphrey KA, Howe JR, Vaccarino FM (senior/corresponding; Yale Child Study Center).
- Journal: Cell (2015), Vol 162:375-390.
- DOI: [10.1016/j.cell.2015.06.034](https://doi.org/10.1016/j.cell.2015.06.034)
- PMID: [26186191](https://pubmed.ncbi.nlm.nih.gov/26186191/)
- Data: GEO GSE61476 (RNA-seq).
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Autism spectrum disorder (ASD) is a disorder of brain development. Most cases lack a clear etiology or genetic basis, and the difficulty of re-enacting human brain development has precluded understanding of ASD pathophysiology. Here we use three-dimensional neural cultures (organoids) derived from induced pluripotent stem cells (iPSCs) to investigate neurodevelopmental alterations in individuals with severe idiopathic ASD. While no known underlying genomic mutation could be identified, transcriptome and gene network analyses revealed upregulation of genes involved in cell proliferation, neuronal differentiation, and synaptic assembly. ASD-derived organoids exhibit an accelerated cell cycle and overproduction of GABAergic inhibitory neurons. Using RNA interference, we show that overexpression of the transcription factor FOXG1 is responsible for the overproduction of GABAergic neurons. Altered expression of gene network modules and FOXG1 are positively correlated with symptom severity. Our data suggest that a shift toward GABAergic neuron fate caused by FOXG1 is a developmental precursor of ASD.

## Key findings

This is the manuscript's **FOXG1 entry**: the first patient-derived telencephalic-organoid model of *idiopathic* ASD, showing that elevated **FOXG1** drives **overproduction of GABAergic (inhibitory) neurons** and an E/I imbalance correlated with clinical severity.

### Cohort and the "no known mutation" framing
- iPSCs from **four families**, each with an ASD proband selected for **macrocephaly / increased head circumference (HC)** plus 1-3 unaffected first-degree relatives; fathers used as **sex-matched controls**. 2-3 iPSC lines/person.
- **Whole-genome sequencing** (CNVnator for CNVs, GATK pipeline for SNVs) found **no de novo CNV or rare SNV causing a known deleterious loss-of-function** in any previously implicated ASD gene. Only one 4.8 kb non-genic deletion (proband 1123, ~30% copy decrease, possible somatic mosaic) validated; proband 07-03 carried a PTEN exon-2 deletion *also present in the unaffected father*. ~112,000 rare SNVs/proband on average. Thus the model probes **idiopathic (genetically heterogeneous, undefined-mutation) ASD**.

### Organoid model fidelity (telencephalic, mid-fetal)
- Free-floating 3D telencephalic-organoid protocol (modification of Mariani et al. 2012): manually isolated neural rosettes -> 1 wk growth -> 4-5 wk terminal differentiation. Time points = rosette (d0), **TD11**, **TD31**.
- Self-organized radial glia (BLBP/NESTIN/PAX6/BRN2/SOX1/2), apical mitoses, then DCX/TUBB3 immature and NeuN+ mature neurons basally.
- **BrainSpan correlation** (45 organoid samples vs 524 post-mortem brain samples): best match = **early fetal human brain ~9 wpc**, with TD31 extending to **13-16 wpc (2nd trimester)**; regional identity = **dorsal telencephalon** (DFC/MFC/OFC cortex + hippocampus), minor cerebellar/amygdala homology. Avg max correlation 0.86. **Low line-to-line and individual-to-individual variability** (intra < inter), attributed to the forebrain-selecting protocol.
- Both ASD and control organoids generate functional neurons: voltage-gated Na/K currents, action potentials (18/18 control, 12/14 proband neurons fired; thresholds -42.5 vs -37.9 mV, p=0.06), and rare AMPA-receptor EPSCs -> functional synapses form in both.

### Transcriptome / network dysregulation in probands
- Differential expression (proband vs father): **1,062 DEGs at TD11; 2,203 DEGs at TD31** (qPCR validation r=0.98, 100% directional concordance).
- **WGCNA -> 24 modules.** Probands show coordinated **down-regulation of non-neuronal modules** (yellow "vascular development," green "lipid metabolism") and **up-regulation of neuronal modules**: magenta ("regulation of transcription" + cell cycle), blue ("neuronal differentiation"/axon guidance), and (later, TD31) brown + tan ("synaptic transmission," "gated channel activity").
- Magenta hub TFs (up): **FOXG1, DLX6-AS1, EOMES, POU3F3/BRN1, SOX3, SOX5, GSX2, ETV1, DLX1, DLX6, E2F2**. Brown module = strongest **SFARI ASD-gene** enrichment (p=6.5E-5; hubs NRXN1, NRXN2, SCN2A, GRIN1, CAMK2B, SLITRK1...). Tan module = GABAergic machinery (**GAD1** + 3 GABA-receptor subunits).

### Cellular phenotypes: accelerated cycle, synaptic overgrowth, GABA bias
- **Shortened cell-cycle length** in undifferentiated ASD iPSCs and (trend) TD11 progenitors (Tc = Ts/(%BrdU/Ki67)); **no proliferation difference by TD31** -> early proliferative event with later compensation. Consistent with a transient TD11 organoid-size increase.
- **Synaptic overgrowth** at TD31: increased MAP2 density and **increased Synapsin-I+ puncta**; increased inhibitory **VGAT+** puncta with **no change in excitatory VGLUT1+** puncta.
- **GABAergic overproduction (the core result):** DLX1/2 and GAD1/GAD67 significantly up at both TD11 and TD31 (reproducible across lines/families/differentiations); also up ASCL1/MASH1, NKX2.1, GABA. **Excitatory markers unchanged at the protein level** (TBR2/EOMES, TBR1, CTIP2 proportions normal) despite mRNA up -> the imbalance is a **selective inhibitory-fate shift**, not a global increase. GABA precursors arose segregated from TBR1+ excitatory precursors.
- Electrophysiology corroboration: proband Na currents inactivated at more hyperpolarized potentials (Eh1/2 -72 to -65 mV in more proband cells), consistent with increased **Nav1.1**, an isoform enriched in GABAergic interneurons.

### FOXG1 is causal (RNAi rescue)
- **FOXG1 is among the top 10 up-regulated genes** at both time points (**8.5-fold at TD11, 13-fold at TD31**), a magenta hub.
- In proband line 07-P#9, **lentiviral shRNAs** (shRNA-2, shRNA-3) knocked FOXG1 down to ~unaffected-relative levels and **restored normal GABAergic differentiation** (DLX1, DLX2, GAD1 transcripts and DLX1-2+/GAD1+ cell numbers) at TD11 and TD31, **without** affecting dorsal markers (PAX6) or excitatory TFs (TBR1).
- Mechanism: BrdU pulse-chase shows the proband excess is **early increased proliferation of DLX1/2+ GABAergic progenitors** (not aberrant cycling of mature GAD1+ neurons), and **FOXG1 knockdown precludes both** the early proliferative excess and the later excess of mature GAD1+ interneurons. Effects on PAX6+/TBR1+ precursors were small/non-significant -> FOXG1 acts selectively on the GABAergic lineage.

### Correlation with clinical severity
- Across the 4 families, **upregulated modules and FOXG1 expression (esp. at TD31) correlate positively with HC Z-score and ASD symptom severity** in probands; downregulated modules correlate negatively. In an enriched n=9 sample, HC vs severity Spearman r=0.79 (p=0.01).
- Crucially, **module eigengenes do NOT correlate with HC in the unaffected fathers** despite equal macrocephaly -> the transcriptional program is a **maladaptive, ASD-specific trait**, not just a correlate of head size; authors propose FOXG1 / module dysregulation as candidate **biomarkers of severe ASD**.

## Methods

- **iPSCs:** retroviral or episomal (viral-free) reprogramming of fibroblasts from 4 families (lines 1123, 03 from Abyzov et al. 2012; 07, 1120 new). Deposited at RUCDR/NIMH.
- **Telencephalic organoids:** free-floating 3D aggregates of isolated neural rosettes; ~1 wk growth then 4-5 wk terminal differentiation; analyzed at rosette/TD11/TD31.
- **Genomics:** WGS of all fibroblasts + iPSCs; CNVnator (CNV), GATK (SNV); de novo prediction for trios; intersection with Willsey et al. 2013 and SFARI syndromic gene lists; qPCR validation of the one CNV.
- **Transcriptomics:** RNA-seq of **45 organoid samples** (Tophat/hg19, GencodeV7; RPKM via RSEQTools, counts via BEDTools; edgeR DEGs; **WGCNA** on log2(RPKM+1); DAVID + MSigDB v4.0 for GO/canonical pathways). Region/age classification by Spearman correlation to **BrainSpan** (524 samples, 95% CI of max correlation).
- **Cellular validation:** immunostaining + stereological quantification (SOX2, TUBB3, PAX6, SOX1, TBR2/EOMES, TBR1, CTIP2, DLX1-2, GAD1, ASCL1, NKX2.1, MAP2, SynI, VGAT, VGLUT1); BrdU/Ki67 cell-cycle and BrdU pulse-chase lineage; western blot (GAD1/2).
- **Perturbation:** lentiviral shRNA knockdown of FOXG1 (3 targeting + 1 non-targeting control) stably in proband iPSC line 07-P#9; qPCR + immunostaining readouts at TD11/TD31.
- **Electrophysiology:** whole-cell patch clamp (EPC9/PatchMaster) of organoid-edge neurons; n=99 neurons; voltage/current clamp, Na-current steady-state inactivation, spontaneous EPSCs.

## Relevance to the brain-organoid ASD review

- **This is the FOXG1 / E/I-imbalance anchor citation (a Table-1-adjacent monogenic-mechanism entry, though here the trigger is *idiopathic*).** It is the founding demonstration that **patient-derived brain organoids can reveal a convergent ASD mechanism without a known causal mutation** - directly motivating the review's thesis of using organoids "proactively" to read out autism genetics where the genotype is undefined.
- Supplies the review's **excitatory/inhibitory (E/I) imbalance** evidence on the *developmental* (fate-specification) axis: an inhibitory-neuron *overproduction* via FOXG1, complementing later monogenic models (e.g. Tenreiro 2025 MeCP2 cIN overproduction; St George-Hyslop 2023 CNTNAP2; Mariani-style E/I framing in CHD8/16p11.2 work).
- Establishes the **causality + rescue template** the review cites for organoid disease modeling: transcriptome -> WGCNA module -> hub TF -> **RNAi reversal of the cellular phenotype**, plus a **genotype-phenotype-severity correlation** (FOXG1 level vs HC/ADOS).
- Anchors the **macrocephaly/proliferation** strand: shortened early cell cycle + neuron overproduction as a developmental antecedent of ASD brain overgrowth, linking organoid readouts to neuropathology (increased neurons/minicolumns/synapses).
- Notes the **FOXG1 dose paradox** the review can use on the "deviation in either direction" point: FOXG1 *loss-of-function* causes congenital/atypical Rett with **small** brains, whereas the *excess* here associates with **large** brains - opposite size effects, convergent disability.

## Open questions / limitations

- **Very small cohort (n=4 families)**; all probands macrocephalic, so generalization to non-macrocephalic / normocephalic ASD is untested. Severity correlations rest on tiny n (supplemented to n=9 only for the HC-severity link).
- **Cause of FOXG1 over-expression is unknown** - no duplication or proximal-promoter mutation at the FOXG1 locus was found; distal regulatory SNVs or upstream network changes are speculated but unproven.
- Idiopathic design means the **shared mechanism is inferred from convergence**, not a defined variant; whether FOXG1 up-regulation is upstream cause vs downstream node is not fully resolved.
- Model captures only **early/mid-fetal (≈9-16 wpc) dorsal-telencephalon** development; later cortical maturation, microcircuit assembly, and in vivo context are absent. Functional synaptic transmission was detected but **network-level E/I activity was not compared** between proband and control organoids (authors flag this as the key follow-up).
- Excitatory markers were up at mRNA but not protein level - the mRNA/protein discordance is unexplained.
- FOXG1 RNAi rescue demonstrated in a **single proband line**; no cross-line/family causal replication of the knockdown.

## Related

- [Tenreiro 2025 — MeCP2 regulates telencephalic development in human cerebral organoids](tenreiro_2025_mecp2_regulates_telencephalic_development_human_cerebral_organoids.md) — Rett/MeCP2 organoids with convergent cortical-interneuron (cIN) overproduction + E/I dysregulation.
- [St George-Hyslop 2023 — Loss of CNTNAP2 alters human cortical excitatory neuron differentiation](st_2023_loss_cntnap2_alters_human_cortical_excitatory_neuron.md) — monogenic ASD model on the excitatory side / network hyperexcitability.
- [Urresti 2021 — Cortical organoids model early brain development disrupted by 16p11.2 CNV](urresti_2021_cortical_organoids_model_early_brain_development_disrupted.md) — patient-derived CNV organoids with size + neuron/progenitor-balance mirror phenotypes.
- [Paulsen 2022 — Autism genes converge on asynchronous development of shared neuron classes](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) — convergence framework across ASD risk genes in organoids.
- [Li 2023 — Single-cell brain-organoid CRISPR screen of ASD genes](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md) — scaled-up perturbation successor to this single-gene RNAi approach.
- [Quadrato 2017 — Cell diversity and network dynamics in photosensitive human brain organoids](quadrato_2017_cell_diversity_network_dynamics_photosensitive_human_brain.md) — functional-network readouts that could test the E/I imbalance Mariani identifies.
- [Paşca 2015 — Functional cortical neurons and astrocytes from human pluripotent stem cells](paca_2015_functional_cortical_neurons_astrocytes_human_pluripotent_stem.md) — contemporaneous guided cortical-spheroid platform.
- [Camp 2015 — Human cerebral organoids recapitulate gene expression programs of fetal neocortex](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md) — single-cell organoid-vs-fetal fidelity benchmark (cites Mariani as the bulk-transcriptome precedent).
- Concept: [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- Entity: [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)
- Entity: [MEA / electrophysiology readouts](../entities/mea-electrophysiology-readouts.md)
