---
title: "Genetically engineered human cortical spheroid models of tuberous sclerosis."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41591-018-0139-y
pmid: 30127391
authors: Blair JD et al.
journal: Nature medicine (2018)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/blair_2018_genetically_engineered_human_cortical_spheroid_models_tuberous.pdf
pdf_status: downloaded
---

# Genetically engineered human cortical spheroid models of tuberous sclerosis.

## Source

- Authors: Blair JD, Hockemeyer D, Bateup HS
- Journal: Nature medicine (2018)
- DOI: [10.1038/s41591-018-0139-y](https://doi.org/10.1038/s41591-018-0139-y)
- PMID: [30127391](https://pubmed.ncbi.nlm.nih.gov/30127391/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Tuberous sclerosis complex (TSC) is a multisystem developmental disorder caused by mutations in the TSC1 or TSC2 genes, whose protein products are negative regulators of mechanistic target of rapamycin complex 1 signaling. Hallmark pathologies of TSC are cortical tubers-regions of dysmorphic, disorganized neurons and glia in the cortex that are linked to epileptogenesis. To determine the developmental origin of tuber cells, we established human cellular models of TSC by CRISPR-Cas9-mediated gene editing of TSC1 or TSC2 in human pluripotent stem cells (hPSCs). Using heterozygous TSC2 hPSCs with a conditional mutation in the functional allele, we show that mosaic biallelic inactivation during neural progenitor expansion is necessary for the formation of dysplastic cells and increased glia production in three-dimensional cortical spheroids. Our findings provide support for the second-hit model of cortical tuber formation and suggest that variable developmental timing of somatic mutations could contribute to the heterogeneity in the neurological presentation of TSC.

## Key findings

Builds an **allelic series of `TSC1`/`TSC2` CRISPR-edited human cortical spheroids** to ask where tuber cells come from. Core results: only *biallelic* (homozygous, or mosaic "second-hit") loss disrupts development; mTORC1 hyperactivation biases progenitors toward glia and produces tuber-like dysplastic/giant cells; and rapamycin rescues — but only within a developmental window.

- **Allelic series (line WIBR3 hESC).** CRISPR–Cas9 deletion of `TSC1` exon 17 or `TSC2` exon 5 → heterozygous and homozygous lines. Homozygous loss degrades the partner protein (TSC1↓ in `TSC2^-/-`, TSC2↓ in `TSC1^-/-`) and the third complex member TBC1D7 (strongly ↓ in `TSC1^-/-`).
- **Heterozygous ≈ wild-type; homozygous = disease.** Heterozygous `TSC1^+/-` / `TSC2^+/-` hESCs, NPCs and spheroids showed **no** mTORC1 activation and a normal neuron/glia developmental profile. Only homozygous `-/-` cells activated mTORC1 (↑p-S6 Ser240/244, ↑p-4E-BP1 Ser65) with reciprocal feedback ↓p-AKT(Ser473). `TSC2` loss raised p-S6 more than `TSC1` loss.
- **mTORC1 is normally suppressed during neurogenesis; that suppression is required.** In WT spheroids p-S6 and p-4E-BP1 fall sharply as cells go from pluripotent (day 0, highest) to differentiating. `TSC1^-/-` / `TSC2^-/-` spheroids keep a stem-cell-like phospho/total ratio throughout — they cannot down-regulate mTORC1 during differentiation.
- **mTORC1 hyperactivation biases progenitors to glia at the expense of neurons.** Homozygous spheroids showed reduced/delayed neuronal markers (MAP2, RBFOX3/NeuN) and increased glial markers (GFAP, S100B) from ~day 100–150 (e.g. `TSC2^-/-` MAP2 d100 p = 0.0003; GFAP d150 p = 0.0028). Early forebrain-progenitor specification was normal (no difference in PAX6+, SOX2+, or Ki-67+ fractions at day 20; WT ~49.7 ± 5.5% Ki-67+), so the defect is in the neuron-vs-glia fate balance, not initial induction. The bias reflects biased differentiation, not extra glial proliferation (no increase in Ki-67/S100B double-positive cells).
- **Mechanism — STAT3.** mTORC1 hyperactivation increased gliogenic p-STAT3(Tyr705) (most in `TSC2^-/-`), rising in WT only when astrocytes appear (d100–150). Rapamycin (20 nM from d12) reduced p-STAT3(Tyr705) to ~50% of control and GFAP to ~4% of control while boosting neuronal proteins (DCX ~348%, CAMK2A ~194%, GLUA1 ~153% of control) → mTORC1 is gliogenic.
- **Second-hit model proven with a conditional allele.** Engineered `TSC2^-/c` (one constitutive null + one Cre-inducible conditional null) plus a Cre-reporter (`TSC2^-/c; LSL-tdTom`). Sparse Cre during NPC expansion created **mosaic** biallelic-null cells in an otherwise heterozygous spheroid. Only the tdTomato+ (biallelic-null) cells became dysplastic — enlarged, multinucleated "giant cells," high p-S6, diffuse nestin/vimentin, some co-expressing neuronal (MAP2) + glial (S100B) markers — exactly mirroring patient tuber cells. Heterozygous (`TSC2^+/c` + Cre) cells did **not** form cytomegalic cells. NPCs: p-S6 and soma size both significantly larger in Cre+ vs neighboring GFP+ cells; neurons showed dendritic hypertrophy (Sholl).
- **Confirmed in a TSC-patient background.** Patient hiPSC line (`4520`, heterozygous `TSC2` exon 1–14 deletion; childhood seizures + mild ID) engineered with a conditional second allele → only Cre+ (biallelic) cells became dysmorphic/high-p-S6/vimentin+, so a second hit is *necessary* for dysplastic cells in patient-derived spheroids. Phenotypes also reproduced in an independent BJ `TSC2^-/-` hiPSC line.
- **Biallelic loss generates glia >> neurons.** In `TSC2^-/c; LSL-tdTom` spheroids, tdTomato+ biallelic-null cells differentiated to glia:neurons ≈ **7.3:1** (72.6% S100B+ vs 9.9% HuC/HuD+; astrocyte identity confirmed by EAAT1, CD44), vs heterozygous GFP+ cells (15.8% neurons, 34.2% glia).
- **Rapamycin rescue is window-dependent (drug-screening proof-of-concept).** Chronic rapamycin (20 nM) starting day 12 (during progenitor expansion) **completely reversed** the glial bias (biallelic cells → 70.4% neurons / 9.9% glia) and tripled neuron output from heterozygous cells (15.8% → 46.5%), and prevented cytomegaly. Starting at day 80 reduced mTORC1 and reversed hypertrophy but only modestly improved neuronal differentiation (9.9% → 22.3%) — most fate decisions are made before day 80 and can't be reversed late. A transient d12–80 pulse improved differentiation (→30.3%) but mTORC1 hyperactivity re-emerged once rapamycin was withdrawn, so sustained inhibition is needed to keep it suppressed.

## Methods

- **Lines / editing:** CRISPR–Cas9 in WIBR3 hESCs — `TSC1` exon-17 and `TSC2` exon-5 deletions (frameshift/premature stop), heterozygous and homozygous. Conditional `TSC2^-/c` (constitutive null + floxed conditional null) and AAVS1 `CAGGS-LSL-tdTomato` Cre reporter. Validation in BJ-fibroblast `TSC2^-/-` hiPSC and patient `4520^-/c` hiPSC. Pluripotency, karyotype, teratoma assays for QC.
- **Cultures:** 2D forebrain NPCs/neurons; 3D cortical spheroids by an established dual-SMAD (dorsomorphin + SB431542) protocol (based on Pasça et al.), FGF2/EGF expansion → BDNF/NT3 maturation; analyzed days 0–205.
- **Second-hit modeling:** subsaturating Cre-GFP vs GFP lentivirus at day 12 (progenitor-expansion phase) for mosaic biallelic inactivation; tdTomato fate-mapping of biallelic-null cells.
- **Readouts:** Western blot + qPCR time courses (p-S6 Ser240/244, p-4E-BP1 Ser65, p-AKT Ser473, p-STAT3 Ser727/Tyr705, TBC1D7, MAP2, GFAP, RBFOX3/NeuN, S100B); IF/confocal (PAX6, SOX2, Ki-67, TUJ1, NeuN, MAP2, GFAP, S100B, nestin, vimentin, p-S6, HuC/HuD, EAAT1, CD44); per-cell p-S6 and soma-area quantification; Sholl analysis of dendrites.
- **Drug:** rapamycin 20 nM, started day 12, 80, or pulsed d12–80; vehicle control. Stats: one-/two-way ANOVA with Bonferroni/Dunnett/Sidak/Tukey; Kolmogorov–Smirnov for per-cell distributions.

## Relevance to the brain-organoid ASD review

This is the **TSC (TSC1/TSC2) entry in the review's Table 1** and the paper that provides the **drug-screening / therapeutic proof-of-concept** for mTOR-pathway organoid disease modeling (ASD + intellectual disability occur in ~half of TSC patients).

- **Gene × developmental-timing disease model:** demonstrates that *when* (and in how many alleles) a mutation hits a cortical progenitor determines the phenotype — biallelic loss during NPC expansion is necessary and sufficient for tuber-like dysplastic cells. This validates the second-hit model of tuber formation in a human system (rodent models lack bona fide tubers) and supplies the review's "progenitor-proliferation vulnerability stage" with a concrete mechanism (mosaic second hit during expansion).
- **mTOR axis counterpart to PTEN:** TSC1/2→mTORC1 here is the upstream/parallel arm of the same PI3K–AKT–mTOR network disrupted by PTEN in [Kang 2024](kang_2024_germline_pten_genotype_dependent_phenotypic_divergence_during.md); the two together anchor the review's mTОR/PI3K-AKT theme, both showing progenitor-stage damage and both rescued by targeting the pathway.
- **Drug-screening proof-of-concept:** the window-dependent rapamycin rescue (full rescue if given during progenitor expansion, only partial if given late, re-activation on withdrawal) is exactly the kind of programmable, stage-specific pharmacological readout the review's "proactive" thesis advocates — it argues for *when* to intervene, not just *whether*.
- **Human-specific motivation:** the introduction explicitly grounds the need for human models in the longer human neurogenic window (~140 days vs ~8 days in mouse) and human-specific progenitor zones — the same OSVZ/oRG expansion documented in [Hansen 2010](hansen_2010_neurogenic_radial_glia_outer_subventricular_zone_human.md).

## Open questions / limitations

- **Tuber architecture not modeled.** Spheroids reproduce tuber *cells* (dysplastic neurons, giant cells, glial bias) but not the macroscopic, organized tuber lesion or its circuitry/epileptogenesis.
- **Haploinsufficiency contribution unresolved.** Heterozygous cells were essentially normal here, yet second-hit mutations are found in only a minority of resected human tubers; whether haploinsufficiency contributes to milder neurological/cognitive aspects of TSC in vivo is not settled by this model.
- **Mosaicism is engineered, not endogenous.** Second hits are introduced by exogenous Cre at a chosen timepoint (day 12); the timing/frequency of true somatic second hits in patients — and how that maps to clinical heterogeneity — remains inferential.
- **Late-stage / functional gaps.** Cultures extend to ~205 days but no electrophysiology, network/seizure readouts, or in-vivo validation; many late panels are n = 1 / performed once (e.g. day-205 imaging, some IF).
- **`TSC1` vs `TSC2` asymmetry** (TSC2 loss → stronger mTORC1 activation and more severe phenotype) is observed but its mechanistic basis and clinical relevance are not fully explored.

## Related

- [Germline PTEN genotype-dependent phenotypic divergence during the early neural developmental process of forebrain organoids](kang_2024_germline_pten_genotype_dependent_phenotypic_divergence_during.md) - sibling PI3K-AKT-mTOR ASD organoid model (PTEN), with AKT-inhibitor rescue.
- [mTOR signaling regulates the morphology and migration of outer radial glia in developing human cortex](andrews_2020_mtor_signaling_regulates_morphology_migration_outer_radial.md) - mTORC1 biology in human radial glia, the pathway hyperactivated by TSC1/2 loss.
- [Cerebral organoids model human brain development and microcephaly](lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.md) - founding template for organoid-based monogenic neurodevelopmental disease modeling.
- [Single-cell brain organoid screening identifies developmental defects in autism](li_2023_single_cell_brain_organoid_screening_identifies_developmental.md) - organoid ASD-gene screen sharing the progenitor-stage vulnerability framing.
