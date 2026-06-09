---
title: "Dissecting the molecular basis of human interneuron migration in forebrain assembloids from Timothy syndrome."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1016/j.stem.2021.11.011
pmid: 34990580
authors: Birey F et al.
journal: Cell stem cell (2022)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# Dissecting the molecular basis of human interneuron migration in forebrain assembloids from Timothy syndrome.

## Source

- Authors: Birey F, Li M-Y, Gordon A, Thete MV, Valencia AM, Revah O, Paşca AM, Geschwind DH, Paşca SP (Stanford; UCLA)
- Journal: Cell Stem Cell 29, 248–264 (February 3, 2022)
- DOI: [10.1016/j.stem.2021.11.011](https://doi.org/10.1016/j.stem.2021.11.011)
- PMID: [34990580](https://pubmed.ncbi.nlm.nih.gov/34990580/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Defects in interneuron migration can disrupt the assembly of cortical circuits and lead to neuropsychiatric disease. Using forebrain assembloids derived by integration of cortical and ventral forebrain organoids, we have previously discovered a cortical interneuron migration defect in Timothy syndrome (TS), a severe neurodevelopmental disease caused by a mutation in the L-type calcium channel (LTCC) Cav1.2. Here, we find that acute pharmacological modulation of Cav1.2 can regulate the saltation length, but not the frequency, of interneuron migration in TS. Interestingly, the defect in saltation length is related to aberrant actomyosin and myosin light chain (MLC) phosphorylation, while the defect in saltation frequency is driven by enhanced γ-aminobutyric acid (GABA) sensitivity and can be restored by GABA-A receptor antagonism. Finally, we describe hypersynchronous hCS network activity in TS that is exacerbated by interneuron migration. Taken together, these studies reveal a complex role of LTCC function in human cortical interneuron migration and strategies to restore deficits in the context of disease.

## Key findings

Two mechanistically separable components of the TS interneuron migration defect (decreased saltation length + increased saltation frequency → inefficient migration, established in Birey et al. 2017):

- **Saltation length — LTCC/calcium/actomyosin axis.**
  - Soma rear lags behind soma front during nucleokinesis ("rear–front uncoupling") in TS interneurons (rear–front correlation: Mann-Whitney p < 0.001); TS somas and DAPI+ nuclei show reduced sphericity (p < 0.01 and p < 0.05).
  - LTCC blocker **nimodipine (Nim, 5 µM) increases saltation length but does not change frequency** in TS (length p < 0.0001) — the first dissociation of the two phenotypes.
  - The length phenotype is **calcium-dependent**: at 1 mM extracellular Ca²⁺ (vs 2 mM baseline), TS saltation length is partially restored while Ctrl length drops; fewer TS cells stop (27% TS vs 63% Ctrl arrest; χ² = 7.0, p < 0.01).
  - LTCC **activator FPL 64176 (5 µM)** *reduces* saltation length (no frequency effect) in ex vivo PCW18 primary human cortical slices (p < 0.0001) — tight LTCC tuning is required for normal length.
  - Downstream: TS hSS show **increased phospho-MLC2(Ser19)** by western blot (p < 0.05) and immunocytochemistry (p < 0.0001); FPL raises pMLC in Ctrl but not in (already saturated) TS. MLCK inhibitor **ML-7 (5 µM) rescues saltation length but not frequency** (length p < 0.0001).
- **Saltation frequency — GABA sensitivity axis.**
  - Bulk RNA-seq of TS hSS (early time points): upregulated GABA-receptor subunits **GABRA4 (logFC = 3.1, FDR = 0.0002), GABRA2 (logFC = 2.2, FDR = 0.007), GABRG1 (logFC = 4.0, FDR = 0.0006)**; GSEA enriched for GABAergic synaptic transmission, chloride-channel complex, and membrane-potential/ion-channel terms (hSS-specific; hCS instead showed glutamate-receptor changes).
  - WGCNA: 14 TS-associated modules (FDR < 0.05), 8 upregulated; several enriched for BD/MDD/SCZ GWAS SNP heritability (e.g., M8 BD enrichment = 2.4, FDR = 2.3×10⁻²; M8 SCZ = 2.4, FDR = 1.1×10⁻²) and NDD/ID gene sets (M13 NDD OR = 1.5, FDR = 3.7×10⁻⁴).
  - Functional confirmation: higher spontaneous Ca²⁺-transient rate in TS (p < 0.01); larger GABA-evoked Ca²⁺ rise (Fura-2, 100 µM GABA, p < 0.01) and larger GABA currents across puff durations (5–500 ms, p < 0.05–0.01) — **enhanced GABA sensitivity**; GABA is depolarizing at this stage. TS interneurons have a **relatively depolarized resting membrane potential** (hSS-specific, p < 0.0001; capacitance/input resistance unchanged); KCNC3/Kv3.3 robustly upregulated.
  - GABA-A blockers **picrotoxin (25 µM) and bicuculline (50 µM) restore saltation frequency but not length** in TS (frequency p < 0.001 / p < 0.05).
  - Elevated phospho-CREB(Ser133) in TS interneurons (p < 0.0001); depolarization (67 mM KCl, 6 h) over-induces activity genes FOS/NPAS4 in TS, blocked by Nim — linking Cav1.2 gain-of-function to activity-dependent transcriptional programs.
- **Network-level.** TS hCS show **hypersynchronous** network calcium activity that is **exacerbated after assembly** with hSS (interneuron infiltration), with larger transient amplitudes (two-way ANOVA p < 0.0001). LTCC blocker Nim (10 µM) reduces correlated transient amplitude in ex vivo PCW20 primary cortex.
- **No global maturation/identity shift.** No significant genotype differences in interneuron maturation scores (Mi 2018; Mayer 2018), SLC12A5/SLC12A2 (chloride reversal) ratio, or calbindin/calretinin/somatostatin subtype proportions — the defect is migratory/electrophysiological, not a fate change.

**Working model:** Cav1.2 gain of function (G406R) → (1) ↑Ca²⁺ → ↑pMLC → aberrant cell-rear actomyosin contractility / rear–front uncoupling → ↓saltation length; and (2) altered activity-dependent transcription → ↑GABA-receptor expression / depolarized RMP → enhanced GABA sensitivity → ↑saltation frequency.

## Methods

- **Model:** forebrain assembloids = fused human cortical spheroids (hCS, dorsal) + human subpallial spheroids (hSS, ventral) from hiPSCs. **8 control hiPSC lines (8 healthy individuals) and 3 TS hiPSC lines (3 individuals)**, all reprogrammed from fibroblasts; TS lines carry the gain-of-function **G406R mutation in alternatively spliced exon 8a of CACNA1C** (delayed Cav1.2 inactivation, ↑intracellular Ca²⁺). The TS-containing 8a isoform persists at later timepoints because the developmental 8a→8 switch is impaired.
- **Interneuron labeling/tracking:** lentiviral interneuron reporters (Dlxi1/2b-eGFP, -mScarlet, Dlx5/6-eGFP/-GCaMP6f). Migration quantified by long-term live imaging; subcellular soma rear/front tracked with a **DeepLabCut** transfer-learning pose-estimation pipeline (19 training frames).
- **Pharmacology:** nimodipine, isradipine, FPL 64176 (LTCC modulators), ML-7 (MLCK inhibitor), picrotoxin / bicuculline (GABA-A blockers); modified extracellular Ca²⁺ (0.5/1/2 mM).
- **Electrophysiology / imaging:** whole-cell patch clamp of migrating interneurons in flattened (transwell) assembloids; GABA puff currents; GCaMP and Fura-2 calcium imaging; Syn1-GCaMP6s for hCS network activity.
- **Transcriptomics:** bulk RNA-seq of hCS and hSS from 3 TS + 6 Ctrl individuals across early (days 40–75) and late (days 90–129) stages, plus 67 mM KCl-depolarized hSS; analyses include differential expression, GSEA, WGCNA, GWAS-heritability and NDD/ID gene-set enrichment, variance partitioning. Activity-dependent regulome compared to Boulting et al. (2021).
- **Ex vivo validation:** primary human cortical slices (PCW18, PCW20) for migration imaging and network calcium activity.

## Relevance to the brain-organoid ASD review

This is the manuscript's **Table-1 CACNA1C / Timothy-syndrome interneuron-migration entry** — the assembloid case study showing how a single ASD-associated channelopathy produces a dissectible, druggable cellular phenotype.

- **Assembloid migration phenotype, decomposed.** Directly supplies the "saltation length vs frequency" decomposition called out in the brief: length is LTCC/Ca²⁺/actomyosin-driven (rescued by Nim, low Ca²⁺, ML-7), frequency is GABA-sensitivity-driven (rescued by picrotoxin/bicuculline). This is a template for the manuscript's "Timothy-syndrome interneuron migration in assembloids" theme.
- **Programmable / proactive readouts.** Demonstrates that an ASD-relevant phenotype can be (a) quantified at subcellular resolution (DeepLabCut soma rear/front), (b) mechanistically partitioned, and (c) pharmacologically reversed in human tissue — the kind of actionable, perturbable assay a "programmable organoid for proactive autism genetics" platform aims to standardize.
- **E/I and network link.** Hypersynchronous TS cortical-network activity exacerbated by interneuron arrival ties the migration defect to circuit-level excitation/inhibition imbalance and candidate seizure mechanisms — complementing Villa's CHD8 E/I-trajectory result and Trevino's noncoding-variant hits at GABA-related motifs (NRF1→GABRB1).
- **Channel/calcium axis.** Establishes LTCC/Cav1.2 calcium signaling and activity-dependent transcription as a tractable node for ASD-relevant interneuron biology in human 3D models.

## Open questions / limitations

- Rescue with GABA-A blockers was **less robust** than the length rescue (Nim/ML-7), possibly due to compensatory metabotropic GABA-B receptors or other cell-non-autonomous effects (e.g., glutamate release in network activity); whether pharmacological rescue is *complete* is unresolved.
- Only **3 TS individuals**, all carrying the canonical G406R exon-8a mutation; atypical TS mutations and additional lines/timepoints are needed to generalize.
- No detectable change in transcriptional maturation programs of TS interneurons, but post-migration/integration electrophysiological "dysmaturation" was not exhaustively assayed.
- It remains **unconfirmed in post-mortem TS cortex** that interneuron numbers are actually reduced; absolute counts are hard because human interneuron migration is prolonged (into the second postnatal year), uses multiple subpallial niches, and is followed by selective apoptosis.
- Extrapolating in vitro hypersynchrony to seizures is explicitly cautioned against; direction of causality between KCNC3/Kv3.3 upregulation and depolarized RMP is unknown.
- Whether Cav1.2 gain of function upregulates GABA receptors *directly* (Ca²⁺-mediated transcription) or *indirectly* (homeostatic response to electrical changes) is open.

## Related

- [Birey 2017 — assembly of functionally integrated human forebrain spheroids](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md) — the foundational assembloid paper that first described the TS migration defect (decreased length + increased frequency); this 2022 paper dissects its molecular basis.
- [Villa 2022 — CHD8 haploinsufficiency links autism to transient E/I trajectory alterations](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md) — companion Table-1 ASD-gene organoid model; both converge on excitatory/inhibitory balance via different mechanisms.
- [Trevino 2021 — chromatin & gene-regulatory dynamics of developing human cortex](trevino_2021_chromatin_gene_regulatory_dynamics_developing_human_cerebral.md) — primary-tissue regulome reference; its disrupted NRF1→GABRB1 and interneuron-class variant hits connect to the GABA-sensitivity arm here.
- [Mariani 2015 — FOXG1-dependent dysregulation of GABA/glutamate neuron differentiation](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md) — another ASD organoid model centered on GABAergic/excitatory imbalance.
