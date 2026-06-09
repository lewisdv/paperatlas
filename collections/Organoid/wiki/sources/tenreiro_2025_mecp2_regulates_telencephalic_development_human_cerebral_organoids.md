---
title: "MeCP2 regulates telencephalic development in human cerebral organoids."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.celrep.2025.116670
pmid: 41391149
authors: Tenreiro MF et al.
journal: Cell reports (2025)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/tenreiro_2025_mecp2_regulates_telencephalic_development_human_cerebral_organoids.pdf
pdf_status: downloaded
---

# MeCP2 regulates telencephalic development in human cerebral organoids.

## Source

- Authors: Tenreiro MF, Mohana-Borges R, Sánchez-Sánchez SM, Dias ÂRM, Blanch R, Muotri AR
- Journal: Cell reports (2025)
- DOI: [10.1016/j.celrep.2025.116670](https://doi.org/10.1016/j.celrep.2025.116670)
- PMID: [41391149](https://pubmed.ncbi.nlm.nih.gov/41391149/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Loss-of-function variants in the X-linked gene MeCP2 cause a severe form of syndromic autism spectrum disorder known as Rett syndrome (RTT). Although traditionally considered a postnatal disorder, increasing evidence suggests that MeCP2 plays a crucial role during prenatal brain development. Here, we used human pluripotent stem cell-derived cerebral organoids and human telencephalic assembloids to model early cortical development in the context of MeCP2 deficiency. Loss of MeCP2 led to widespread dysregulation of transcriptional programs associated with cortical excitatory neuron development, accompanied by delayed morphological and functional maturation, despite preserved neuroepithelial architecture, dorsal telencephalic identity, and laminar organization. MeCP2 deficiency also led to an overproduction of cortical interneurons (cINs), with these cINs exhibiting hypermotile tangential migration dynamics and contributing to persistent hypersynchronous network activity in assembloids. These findings highlight the critical role of MeCP2 in early telencephalic neurodevelopment and underscore the prenatal origin of RTT-related dysfunction.

## Key findings

- **Core claim: MeCP2 has profound, lineage-specific prenatal roles in human telencephalic development — coordinating excitatory-neuron maturation tempo and restraining interneuron production and tangential migration — even though gross corticogenesis (architecture, dorsal identity, inside-out lamination) is preserved.** This is the Table-1 MeCP2/Rett organoid-ASD entry for the review and the strongest in-corpus evidence for a *prenatal* (not solely postnatal) origin of RTT dysfunction.
- **MeCP2 is expressed during human mid-fetal cortical development.** BrainSpan bulk + human fetal scRNA-seq (GW17–18) show broad MeCP2 across radial glia and infra-/supragranular neurons, with substantial second-trimester levels (coinciding with peak neurogenesis) rising further postnatally. In 8-week human cerebral organoids (hCOs), MeCP2 protein is broad but enriched in post-mitotic neurons — a developmentally regulated, neuron-intensifying pattern.
- **Isogenic + patient-derived MeCP2-loss models.** Female RTT iPSC lines were exploited as somatic mosaics: because X-inactivation is retained through reprogramming, clonal lines expressing *exclusively* WT or mutant (MUT) MeCP2 were isolated (Sanger-verified monoallelic expression; Xist RNA-FISH foci confirmed XCI; monoallelic status monitored for Xi erosion). Patient mutations: **2036 = p.R133C (c.397C>T, missense), 2042 = p.R255X (c.763C>T, nonsense), 2047 = p.R306C (c.916C>T, missense)** — 3 of the 8 recurrent RTT hotspots (~60% of cases). An isogenic homozygous MeCP2 deletion was also engineered in the H9 hESC line.
- **MeCP2 deficiency does NOT impair dorsal-telencephalic differentiation or lamination.** WT and MUT hCOs were morphologically/size-indistinguishable at week 3.5, expressed forebrain/dorsal markers (FOXG1, LHX2, PAX6), formed normal pseudostratified VZs, and progressed normally through TBR1 (LVI) → BCL11B/CTIP2 (LV) → SATB2 (LII–III) lamination to week 17, retaining the canonical inside-out pattern (no spatial-distribution difference). scRNA-seq of 55,478 cells (9 organoids, patients 2036+2042) gave 8 telencephalic clusters with strong concordance to fetal signatures and E15.5 mouse telencephalon; **no consistent cell-type-proportion shift** between genotypes.
- **Subtle but real: transient progenitor-over-neuron bias and modest VZ expansion.** MUT hCOs (esp. lines 2042, 2047) showed modestly larger/thicker VZs at weeks 5–6; bulk RNA-seq of week 5–6 organoids found MUT upregulation of progenitor-self-renewal genes (HEY2, NOTCH2, TP73), ECM (COL1A1, LAMA3), and WNT activators (RSPO1, WNT3A), with GO enrichment for epithelial morphogenesis; WT upregulated neuronal-differentiation genes. (Parallels mouse data of MeCP2 loss biasing progenitors toward proliferation — and the progenitor/neuron-balance theme of [Rash 2011](rash_2011_fgf_signaling_expands_embryonic_cortical_surface_area.md).)
- **MeCP2 regulates excitatory-neuron maturation tempo (delayed/protracted maturation).** Pseudotime showed increased density of intermediate states in MUT (protracted differentiation). MUT excitatory neurons upregulated axonogenesis/projection/synapse-assembly genes (shared across backgrounds: FRY, MIR137HG, TUBB3, STMN1, LRRTM4, ANK2, PCDH9) yet downregulated key differentiation TFs (NEUROD2, CREB5, POU3F2). Morphologically, MUT neurons were *more immature* — smaller soma, fewer primary neurite branches (consistent across backgrounds, pronounced in 2036). The authors interpret the apparent "accelerated projection programs + immature morphology" as a **temporal lag / decoupling of transcriptional and functional maturation**, not faster maturation.
- **Functional immaturity by calcium imaging (hCOs).** GCaMP imaging (week 17, patient 2042): MUT neurons had a markedly increased inter-event interval (reduced overall spontaneous activity) but increased burst duration, amplitude, and AUC of calcium transients (heightened excitability amid low baseline firing). scRNA-seq showed MUT downregulation of GRIA4 (AMPA subunit), KCNQ5 (K+ channel), and NNAT — consistent with altered intrinsic excitability.
- **MeCP2 deficiency overproduces cortical interneurons (cINs) — independent of DLX5 imprinting.** To get GABAergic cINs (under-represented in standard hCOs), the authors built human MGE organoids (hMGEOs) and fused them to hCOs into telencephalic assembloids (hTAs). MUT hMGEOs contained a higher proportion of **DLX2+ and DLX5+ cINs** (both backgrounds), with a modest ~1.5-fold DLX5 increase. They tested and **rejected** loss-of-imprinting as the cause: both WT and MUT showed biallelic DLX5 expression (c.*163dupC polymorphism), while bona fide imprinted controls (SNRPN, NDN, PEG10) stayed monoallelic. → cIN overproduction is not via DLX5 allelic relaxation.
- **Hypermotile cIN tangential migration.** Live imaging of Dlxi1/2b::eGFP+ cINs in intact hTAs: MUT cINs kept the normal saltatory/nucleokinesis motion but had **increased nucleokinesis displacement, higher event frequency, faster overall speed**, and straighter trajectories (greater path directness, fewer turns) than WT — i.e. MeCP2 normally *constrains* cIN motility. cIN invasion/coverage of cortical tissue itself was unchanged (chemoattraction intact). MUT cINs upregulated migration/guidance genes (ERBB4, NRG3, NRP2), K+ channels (KCNC2, KCNIP4), and GABA-A subunits (GABRA2, GABRB1).
- **Persistent network hypersynchrony + hyperexcitability in assembloids.** GCaMP imaging of hTAs ~2 months post-fusion: WT hTAs **decorrelated** (lost synchrony) after cIN integration, whereas **MUT hTAs maintained synchronous activity and increased firing frequency** (decreased IEI; higher mean pairwise Pearson correlation across fields). So MeCP2-deficient cINs fail to dampen synchrony in maturing circuits → sustained hypersynchrony/hyperexcitability (resembling RTT epileptiform activity), arising spontaneously without pharmacology.

## Methods

- **Cell lines:** controls = H9 (WA09) hESC + iPSC lines KOLF2.1J, WT83.06, WT.Fc02. RTT iPSCs from the Rett Syndrome Research Trust collection (Coriell), Sendai-reprogrammed: subjects 2036 (p.R133C), 2042 (p.R255X; severe — near-daily seizures, CGI-S 6), 2047 (p.R306C). Isogenic homozygous MeCP2-deletion hESC made in H9 by CRISPR/Cas9. Female lines used as WT/MUT clonal pairs via retained XCI; karyotype/CNV-array QC throughout.
- **hCO protocol (guided, dual-SMAD):** Aggrewell800 aggregates (~3×10^6 cells/well; 300–400 µm) → orbital shaking 90 rpm → **NIM1** (DMEM-F12, 15% KOSR, LDN-193189 100 nM + SB-431542 10 µM + XAV-939 2.5 µM) days 1–6 → **NIM2** (KOSR→N2) + low bFGF 4 ng/mL (no patterning factors) days 6–9 → **NDM1** (DMEM-F12:Neurobasal 1:1, N2/B27−vitA, insulin) with 20 ng/mL bFGF (7 d) then bFGF+EGF 20 ng/mL each (8 d), days 10–24 → **NDM2** (B27+vitA) from day 25, with 1% Matrigel added from weeks 4–5 to aid CP formation. ≥90%-success batches kept; quality criteria included >400 µm aggregates with clearing neuroepithelium.
- **hMGEO protocol (ventralized):** as hCO but on day 6 NIM2 + low bFGF + 1.25 µM XAV-939 (no dual-SMAD); days 10–17 NDM1 + **500 nM SAG** (smoothened agonist) + 1.25 µM XAV-939. SAG dose was optimized — 100 nM (prior reports) under-ventralized; **500 nM** needed for near-ubiquitous NKX2-1+ MGE identity (LGE marker GSX2 absent; DLX2+ IPs/cINs; GABA/GAD67+ by week 8).
- **Assembloids (hTAs):** controllable fusion of one hCO + one hMGEO in an Eppendorf tube (NDM2), transferred to plate day 7, long-term cultured on shaker (90 rpm) in NDM2 + 1% Matrigel. cIN reporter = mouse **Dlxi1/2b enhancer** via lentivirus.
- **Readouts:** bulk RNA-seq (week 5–6, patient 2042) and scRNA-seq (week 17 hCOs: 55,478 cells; week 17 hTAs: 31,991 cells, patient 2042); immunostaining + tissue clearing (CUBIC); morphology of hsyn::eGFP/NEUROD2+ neurons; live confocal imaging of cIN migration (nucleokinesis/path metrics); **GCaMP-based calcium imaging** of hCOs and hTAs (IEI, burst duration/amplitude/AUC, pairwise Pearson correlation across fields). Data: GEO **GSE297594**.

## Relevance to the brain-organoid ASD review

- **Primary Table-1 entry for MeCP2 / Rett-syndrome organoid modeling.** Provides the review's lineage-resolved, longitudinal demonstration that an X-linked syndromic-ASD gene perturbs *prenatal* human telencephalic development across both excitatory and inhibitory lineages — reframing RTT (and the "postnatal disorder" assumption) as having developmental-window origins amenable to proactive/early modeling.
- **Migration-vulnerability-stage support (interneuron axis).** The hypermotile, over-straight tangential migration of MeCP2-deficient cINs is a clean migration-stage phenotype complementing the excitatory/radial-migration deficits in [Urresti 2021](urresti_2021_cortical_organoids_model_early_brain_development_disrupted.md) and the assembloid migration screens ([Meng 2023](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md), [Birey 2022](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md)) — i.e. converging evidence that ASD genes hit a shared mid-fetal migration window, here on the GABAergic side.
- **cIN overproduction as a convergent ASD organoid phenotype.** Excess cINs recur across idiopathic-ASD and ASD-risk-gene organoid models; this paper adds MeCP2 to that set and rules out the long-assumed DLX5 loss-of-imprinting mechanism — a substantive correction the review can cite.
- **Maturation-tempo / asynchrony theme.** The decoupling of transcriptional from morphological/functional maturation aligns with the review's "asynchronous development" framing ([Paulsen 2022](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md), [Villa 2022](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md)) and with the FGF/Notch-set neurogenic-tempo logic of [Rash 2011](rash_2011_fgf_signaling_expands_embryonic_cortical_surface_area.md).
- **Circuit-level (E/I) readout via assembloids.** The WT-decorrelation vs MUT-hypersynchrony contrast after cIN integration showcases the assembloid + calcium-imaging pipeline the review advocates for measuring emergent network phenotypes — a functional layer beyond transcriptomics.
- **Complements the other MeCP2/RTT entry.** Sits alongside [Xiang 2020](xiang_2020_dysregulation_brd4_function_underlies_functional_abnormalities_mecp2.md) (BRD4 dysregulation in MeCP2-deficient organoids), giving the review two mechanistic angles on the same gene.
- **Same-lab platform continuity.** Muotri-lab cortical-organoid/assembloid platform shared with [Urresti 2021](urresti_2021_cortical_organoids_model_early_brain_development_disrupted.md), supporting methodological coherence across the review's ASD-gene table.

## Open questions / limitations

- **Severe-end variant + no XCI mosaicism.** Functional assays leaned on patient 2042 (p.R255X), a high-seizure-risk variant capturing the severe tail; fully WT or MUT organoids do **not** model the WT:MUT mosaicism of female RTT brains (XCI skewing modulates severity). Authors flag mosaic/chimeric organoids with controlled WT:MUT ratios as needed future work.
- **mCH-independent mechanism, prenatal only.** Mid-fetal cortex / organoids largely lack non-CG (mCH) methylation that accumulates postnatally and is central to MeCP2 function, so the transcriptional changes here are likely mCH-independent — leaving open how MeCP2 acts prenatally and how well phenotypes translate to postnatal stages.
- **Maturation ceiling of organoids.** RTT manifests postnatally; current models stop at mid-gestation, so whether the observed phenotypes are transient, compensated, or persistent into postnatal stages cannot be resolved here. Postmortem RTT single-cell data show limited overlap with these enrichment results.
- **Inter-line / inter-individual variability.** Cell-type proportions varied between individuals; some phenotypes (e.g. soma/branching) were strongest in one background; discrepancies with prior RTT organoid studies (altered vs unchanged excitatory abundance, IP/pre-plate changes) are attributed to protocol/patterning-fidelity differences but not fully reconciled.
- **oRG caveat.** A modest oRG-marker increase in MUT is flagged as unreliable given oRG under-representation in organoids.
- **Migration mechanism not nailed down.** cIN hypermotility is correlated with upregulated K+/GABA-A/guidance genes and a presumed prolonged depolarizing-GABA state (hTAs predominantly NKCC1+ regardless of genotype), but the causal driver — and possible non-cell-autonomous dorsal-compartment cues — is not established.
- **DLX5 increase mechanism open.** cIN/DLX5 overproduction is shown *not* to be loss-of-imprinting, but the actual mechanism is left for future work.

## Related

- [Urresti 2021 — 16p11.2 cortical organoids (neuronal migration deficits; same lab platform)](urresti_2021_cortical_organoids_model_early_brain_development_disrupted.md)
- [Xiang 2020 — BRD4 dysregulation underlies functional abnormalities in MeCP2-deficient organoids](xiang_2020_dysregulation_brd4_function_underlies_functional_abnormalities_mecp2.md)
- [Birey 2022 — Molecular basis of human interneuron tangential migration in forebrain assembloids](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md)
- [Birey 2017 — Assembly of functionally integrated human forebrain spheroids (MGE-cortex fusion)](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md)
- [Meng 2023 — Assembloid CRISPR screens reveal disease-gene impact on interneuron generation/migration](meng_2023_assembloid_crispr_screens_reveal_impact_disease_genes.md)
- [Mariani 2015 — FOXG1-dependent GABA/glutamate dysregulation in idiopathic-ASD organoids](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md)
- [Paulsen 2022 — Autism genes converge on asynchronous development of shared neuron classes](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md)
- [Villa 2022 — CHD8 haploinsufficiency alters excitatory neurons in organoids](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md)
- [Sȩt 2023 — Loss of CNTNAP2 alters human cortical excitatory neuron development](st_2023_loss_cntnap2_alters_human_cortical_excitatory_neuron.md)
- [Rash 2011 — FGF/Notch control of the cortical neurogenic window (progenitor/neuron balance)](rash_2011_fgf_signaling_expands_embryonic_cortical_surface_area.md)
- Concept: [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- Entity: [Assembloids and regional fusion](../entities/assembloids-and-regional-fusion.md)
- Entity: [Calcium imaging readouts](../entities/calcium-imaging-readouts.md)
