---
title: "CHD8 haploinsufficiency links autism to transient alterations in excitatory and inhibitory trajectories."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1016/j.celrep.2022.110615
pmid: 35385734
authors: Villa CE et al.
journal: Cell reports (2022)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# CHD8 haploinsufficiency links autism to transient alterations in excitatory and inhibitory trajectories.

## Source

- Authors: Villa CE, Cheroni C, Dotter CP, López-Tóbon A, Oliveira B, Sacco R, Yahya AÇ, Morandell J, Gabriele M, Tavakoli MR, Lyudchik J, Sommer C, Gabitto M, Danzl JG, Testa G, Novarino G (IEO/Human Technopole, Milan; IST Austria; Allen Institute)
- Journal: Cell Reports 39, 110615 (April 5, 2022) — open access (CC BY)
- DOI: [10.1016/j.celrep.2022.110615](https://doi.org/10.1016/j.celrep.2022.110615)
- PMID: [35385734](https://pubmed.ncbi.nlm.nih.gov/35385734/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Mutations in the chromodomain helicase DNA-binding 8 (CHD8) gene are a frequent cause of autism spectrum disorder (ASD). While its phenotypic spectrum often encompasses macrocephaly, implicating cortical abnormalities, how CHD8 haploinsufficiency affects neurodevelopmental is unclear. Here, employing human cerebral organoids, we find that CHD8 haploinsufficiency disrupted neurodevelopmental trajectories with an accelerated and delayed generation of, respectively, inhibitory and excitatory neurons that yields, at days 60 and 120, symmetrically opposite expansions in their proportions. This imbalance is consistent with an enlargement of cerebral organoids as an in vitro correlate of patients' macrocephaly. Through an isogenic design of patient-specific mutations and mosaic organoids, we define genotype-phenotype relationships and uncover their cell-autonomous nature. Our results define cell-type-specific CHD8-dependent molecular defects related to an abnormal program of proliferation and alternative splicing. By identifying cell-type-specific effects of CHD8 mutations, our study uncovers reproducible developmental alterations that may be employed for neurodevelopmental disease modeling.

## Key findings

- **Macrocephaly-like organoid overgrowth.** CHD8⁺/⁻ and CHD8⁺/E1114X organoids are indistinguishable from controls at day 0–20 but become **~50% larger than controls by day 120** (one-way ANOVA, p < 0.001; large per-genotype n, e.g., day 120 n(CHD8⁺/⁺)=85, n(CHD8⁺/⁻)=46). The patient mutation **S62X (no patient macrocephaly) produces essentially no size increase** — the assay tracks patient-specific phenotype.
- **Symmetrically opposite, transient E/I shift.** Time-course scRNA-seq (**75,060 cells**, 63 organoids, days 20/60/120) showed CHD8 haploinsufficiency **accelerates interneuron (IN) production and delays excitatory-neuron (EN) production**: more mutant cells in the IN branch at **day 60** and in the EN branch at **day 120**. The day-60 increase in interneurons (parvalbumin lineage) is the single most robust population change. Effects are largely **transient/stage-specific**, not a permanent rewiring.
- **Sustained, cell-autonomous over-proliferation.** EdU/Ki67 pulse-chase at day 10 and day 20: CHD8⁺/⁻ VZ-like structures have significantly more EdU⁺ and Ki67⁺ cells (p < 0.001 for EdU) with **unchanged EdU/Ki67 ratio** (cell-cycle length unchanged → larger progenitor pool, not faster cycling). By day 60: thicker Sox2⁺ (radial glia) layer, thinner Map2⁺ neuronal layer, fewer Tbr2⁺ IPs early. **S62X shows no proliferation increase**, matching its mild phenotype. **Mosaic 1:1 organoids** (CHD8⁺/⁺ + CHD8⁺/⁻;GFP) confirm cell-autonomy: GFP⁺ (mutant) cells over-represented among Sox2⁺ progenitors and under-represented among NeuN⁺ neurons at day 60.
- **Proliferation-vs-neurogenesis molecular dichotomy.** Bulk RNA-seq of day-10 organoids: **868 dysregulated genes**; upregulated → cell cycle, RNA splicing, transcription regulation; downregulated → neuronal differentiation/brain development. Significant enrichment of top **ASD-associated (SFARI)** genes among DEGs, including chromatin regulators ASH1L and direct CHD8 targets ARID1B and TBL1XR1. Of down-/up-regulated genes, **28% / 47% are CHD8-bound** (Sugathan 2014 ChIP-seq) — partly a direct effect.
- **ZEB2 as candidate mediator.** In day-20 radial glia, **ZEB2** is ~2.5-fold below control; ZEB2 ChIP-seq targets are enriched among cluster DEGs (up in cycling cells, down in differentiated cells). ZEB2 drives neuroepithelial→radial-glia transition and cortical expansion → plausible link from CHD8 dosage to the proliferative skew. Unbiased search added 3 more candidate TFs, including **RCOR1** (REST co-repressor; REST previously linked to CHD8).
- **Cell-type-specific lasting impact.** Most-affected clusters by DEG count are **early excitatory neurons (ENE)** and **interneuron intermediate progenitors (IN_IP)** — precisely the populations immediately upstream of the most-shifted frequencies (EN1 and IN). Net "bimodal" model: an **early switch accelerating interneuron fate (little lasting transcriptional legacy)** vs a **delayed excitatory fate that leaves a large lasting transcriptional legacy**, especially in lower-layer (corticofugal) neurons.
- **Altered mRNA processing / alternative splicing.** Pseudo-bulk dPSI and single-cell SpliZVD analyses found CHD8-dependent splicing changes concentrated in IN_IP, IN, and ENE/EN1; excitatory neurons (EN2) affected throughout. Top enriched pathway = **EIF2 signaling** (ribosome assembly / translation initiation), plus mitochondrial dysfunction — both previously associated with ASD; controls for physiological developmental splicing rule out a developmental-skew artifact.

## Methods

- **Model:** human cerebral organoids (Lancaster/Knoblich-style, with optimized hESC-seeding/EB conditions inspired by Camp 2015 for reproducibility; >90% successful differentiation per embedded EB).
- **Isogenic genetics (CRISPR/Cas9 in one hESC background):** two helicase-domain LoF lines (**CHD8⁺/⁻** and **CHD8⁺/⁻;GFP**, deletion in C-terminal helicase region, ~50% CHD8 protein reduction) plus two **patient-specific premature-stop** lines (**E1114X** macrocephaly-associated; **S62X** not macrocephaly-associated). Off-target screening performed. (Human CHD8 has long and short isoforms; short lacks the first 279 N-terminal aa.)
- **Single-cell:** droplet scRNA-seq across days 20/60/120 (3 control + 4 mutant samples per timepoint; each sample = pool of 3 organoids from ≥2 batches); Leiden clustering → 10 populations (RG1/2/3 by cell-cycle phase, IP, IN_IP, IN, ENE, EN1, EN2); annotation via markers + overlap with fetal cortex (Nowakowski 2017) + co-embedding with fetal primary cells (Pollen 2019). Trajectories via diffusion pseudotime (DPT) and tree-graph analysis; differential abundance and stage/cluster-wise differential expression.
- **Mosaic organoids:** 1:1 CHD8⁺/⁺ + CHD8⁺/⁻;GFP to test cell-autonomy (Sox2/NeuN vs GFP at day 60).
- **Imaging/proliferation:** EdU (1 h pulse, 16 h chase) + Ki67 at days 10/20; deep-learning semi-automatic cell counting (Cellpose) over large organoid regions; IHC for Sox2, Tbr2, Ctip2, Satb2, Map2, NeuN.
- **Bulk transcriptomics:** day-10 RNA-seq (proliferation-enriched stage, first CHD8⁺/⁺ vs CHD8⁺/⁻ divergence); GO enrichment; overlap with CHD8 (Sugathan 2014) and ZEB2 ChIP-seq targets and with prior CHD8 datasets (mouse + organoid).
- **Splicing:** pseudo-bulk delta-percent-spliced-in (dPSI) + single-cell SpliZVD; pathway enrichment (e.g., EIF2 signaling).

## Relevance to the brain-organoid ASD review

This is the manuscript's **Table-1 CHD8 entry** — the cerebral-organoid model of CHD8 haploinsufficiency linking a high-confidence ASD gene to macrocephaly and to transient excitatory/inhibitory imbalance.

- **CHD8 haploinsufficiency → organoid enlargement.** Provides the in-vitro macrocephaly correlate (~50% larger by day 120) and the mechanism (extended, cell-autonomous neural-progenitor proliferation; larger pool, not faster cycling) requested in the brief.
- **Transient E/I trajectory alterations.** Supplies the "accelerated inhibitory + delayed excitatory" trajectory result with concrete timing (IN excess at day 60, EN catch-up/excess at day 120) — a direct E/I-balance complement to Birey's Timothy-syndrome interneuron-migration phenotype.
- **Genotype–phenotype dissection / proactive-genetics fit.** The isogenic + mosaic design (helicase-LoF vs patient-specific E1114X vs S62X) shows the organoid assay can distinguish macrocephaly-causing from non-macrocephaly mutations and prove cell-autonomy — exactly the kind of patient-specific, programmable readout the "proactive autism genetics" manuscript is built around.
- **Convergence with the regulome reference.** ASD-gene (SFARI) and direct-CHD8-target enrichment among early DEGs, with ZEB2/RCOR1 as candidate downstream regulators, connects this cellular model to the gene-regulatory / variant-to-cell-type framework provided by Trevino 2021 and the organoid regulome work of Fleck 2023.
- **Reproducibility as a modeling asset.** Explicit emphasis on reproducible organoid generation and longitudinal sampling positions CHD8 organoids as a benchmarkable disease-modeling system.

## Open questions / limitations

- Phenotypes not recapitulated in organoids (specific brain areas, later cellular features) may be missed; organoids model early embryonic cortex only.
- E/I ratio changes were **not validated functionally** (no electrophysiology/circuit-activity readout of the inhibitory/excitatory imbalance).
- Candidate mediators (**ZEB2, RCOR1**, two others) were identified by expression + target-enrichment but **no rescue/perturbation experiments** were performed to prove their causal contribution.
- Alternative-splicing effects (dPSI + SpliZVD) are computational and **warrant functional validation** of isoform-ratio consequences.
- Genetic background is fixed to one isogenic hESC line; macrocephaly penetrance in patients is only ~½–⅔, so generalization across backgrounds/mutations is partial.

## Related

- [Birey 2022 — molecular basis of human interneuron migration (Timothy syndrome)](birey_2022_dissecting_molecular_basis_human_interneuron_migration_forebrain.md) — companion Table-1 ASD-gene model; both converge on excitatory/inhibitory balance via distinct mechanisms (channelopathy vs chromatin-remodeler dosage).
- [Trevino 2021 — chromatin & gene-regulatory dynamics of developing human cortex](trevino_2021_chromatin_gene_regulatory_dynamics_developing_human_cerebral.md) — primary-tissue regulome / SFARI variant reference framing the ASD-gene and TF-target enrichments seen here.
- [Cheroni 2022 — benchmarking brain-organoid recapitulation of fetal corticogenesis](cheroni_2022_benchmarking_brain_organoid_recapitulation_fetal_corticogenesis.md) — companion paper from the same lab/consortium on organoid fidelity, directly relevant to the reproducibility claims.
- [Mariani 2015 — FOXG1-dependent dysregulation of GABA/glutamate neuron differentiation](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md) — earlier ASD organoid model of E/I imbalance (over-production of GABAergic neurons), a conceptual precursor to this trajectory analysis.
- [Camp 2015 — human cerebral organoids recapitulate gene-expression programs](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md) — fetal-vs-organoid concordance work that informed this paper's optimized culture conditions.
