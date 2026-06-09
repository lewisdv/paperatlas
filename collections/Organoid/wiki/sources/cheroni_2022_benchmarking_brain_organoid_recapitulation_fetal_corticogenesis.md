---
title: "Benchmarking brain organoid recapitulation of fetal corticogenesis."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41398-022-02279-0
pmid: 36539399
authors: Cheroni C et al.
journal: Translational psychiatry (2022)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/cheroni_2022_benchmarking_brain_organoid_recapitulation_fetal_corticogenesis.pdf
pdf_status: downloaded
---

# Benchmarking brain organoid recapitulation of fetal corticogenesis.

## Source

- Authors: Cheroni C, Trattaro S (co-first), Caporale N, López-Tobón A, Tenderini E, Sebastiani S, Troglio F, Gabriele M, Bressan RB, Pollard SM, Gibson WT, Testa G (senior).
- Journal: Translational Psychiatry (2022) 12:520.
- DOI: [10.1038/s41398-022-02279-0](https://doi.org/10.1038/s41398-022-02279-0)
- PMID: [36539399](https://pubmed.ncbi.nlm.nih.gov/36539399/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Brain organoids are becoming increasingly relevant to dissect the molecular mechanisms underlying psychiatric and neurological conditions. The in vitro recapitulation of key features of human brain development affords the unique opportunity of investigating the developmental antecedents of neuropsychiatric conditions in the context of the actual patients' genetic backgrounds. Specifically, multiple strategies of brain organoid (BO) differentiation have enabled the investigation of human cerebral corticogenesis in vitro with increasing accuracy. However, the field lacks a systematic investigation of how closely the gene co-expression patterns seen in cultured BO from different protocols match those observed in fetal cortex, a paramount information for ensuring the sensitivity and accuracy of modeling disease trajectories. Here we benchmark BO against fetal corticogenesis by integrating transcriptomes from in-house differentiated cortical BO (CBO), other BO systems, human fetal brain samples processed in-house, and prenatal cortices from the BrainSpan Atlas. We identified co-expression patterns and prioritized hubs of human corticogenesis and CBO differentiation, highlighting both well-preserved and discordant trends across BO protocols. We evaluated the relevance of identified gene modules for neurodevelopmental disorders and psychiatric conditions finding significant enrichment of disease risk genes especially in modules related to neuronal maturation and synapsis development. The longitudinal transcriptomic analysis of CBO revealed a two-step differentiation composed of a fast-evolving phase, corresponding to the appearance of the main cell populations of the cortex, followed by a slow-evolving one characterized by milder transcriptional changes. Finally, we observed heterochronicity of differentiation across BO models compared to fetal cortex. Our approach provides a framework to directly compare the extent of in vivo/in vitro alignment of neurodevelopmentally relevant processes and their attending temporalities, structured as a resource to query for modeling human corticogenesis and the neuropsychiatric outcomes of its alterations.

## Key findings

A transcriptomic benchmarking study (WGCNA co-expression + differential expression + bulk deconvolution) that quantifies how closely brain-organoid protocols recapitulate human fetal corticogenesis, and where they diverge - in module content and especially in **timing (heterochronicity)**. The authors build an explicit fetal-cortex co-expression "knowledge base" and score four archetypal organoid protocols against it.

- **Reference + datasets compared.** Fetal reference = **BrainSpan Atlas, 162 bulk RNA-seq data points spanning post-conceptional weeks (PCW) 8-37**, plus in-house fetal CNS tissue (gestational weeks 13 and 15) and 2D fetal cultures (weeks 11, 19). In-house cortical BO (CBO): **39 single-organoid + 4 hiPSC samples from 4 control lines, profiled across 200 days**, in 2 batches. Three external protocols (time points 0-100+ days): **minimally-guided neural organoids (MGO; Luo et al. 2016), forebrain organoids (FO; Qian et al. 2016), telencephalic aggregates (TA; Mariani et al. 2015)**.
- **Two-step CBO differentiation.** Stage-wise DEA shows a **fast-evolving phase with large DEG numbers until ~day 100** (neuronal fate-commitment/maturation up; cell-cycle/transcription/translation down), then a **slow-evolving plateau** with milder changes. Cell fate regulators EOMES, LHX2, FEZF2 modulated early; astrocytic HEPACAM/AQP4/AGT/APOE and GABAergic-interneuron markers (CALB2, SCGN, SLC6A11) upregulated after day 100.
- **CBO converges toward fetal cortex.** In PCA, CBO move toward and cluster near fetal tissue with maturation, while 2D cultures stay apart. Deconvolution: in CBO progenitor:neuron proportions are comparable by ~day 50, neurons predominate from **day 100** onward; outer radial glia rise from day 100.
- **Fetal cortex structure.** WGCNA on BrainSpan gave **17 gene co-expression modules**; CBO gave **14 modules**. Monotonic up-with-development modules (BS_Turquoise/Pink/Midnightblue/Grey60) overlap CBO_Turquoise; cell-cycle down-with-development modules (BS_Yellow/Black) overlap CBO_Brown.
- **Divergence metric 1 - heterochronicity (the headline divergence).** The slow-evolving transition that begins ~**day 100-150 in CBO is anticipated to ~day 40-60 in MGO, FO, and TA**. Whole-transcriptome correlation to BrainSpan: **MGO and FO reach by ~day 60 a similarity to late PCW that CBO reaches only by ~day 100**. Deconvolution agrees: MGO/FO/TA accumulate neurons faster ("accelerated dynamic"). Net: external protocols compress/accelerate the corticogenesis timeline; CBO's prolonged EGF/bFGF use keeps cells immature longer but **aligns more faithfully with in-vivo developmental tempo**.
- **Divergence metric 2 - module preservation / discordance.** Monotonic neuron-specification and progenitor-proliferation programs are **shared between fetal cortex and CBO and largely recapitulated by all analyzed protocols**. In contrast, **non-monotonic (U-shaped) modules (BS_Red, BS_Blue; CBO_Red, CBO_Green; functionally enriched for ECM and cell adhesion) are well recapitulated in CBO but poorly/inconsistently in MGO, FO, TA** (MGO little variation, FO drop at day 100, TA opposite/absent trend). Outer-radial-glia signature onset also differs by protocol (CBO from day 100; FO from day 40; MGO/TA partial).
- **Reproducibility across genetic backgrounds.** CBO showed robust reproducibility across control individuals and batches; **TA were more sensitive to interindividual variability** (MGO/FO could not be tested - single line each).
- **Disease-gene relevance.** Overlap analysis (SFARI ASD genes; DD2P developmental-disorder genes; GWAS Catalog risk genes for ADHD, ASD, schizophrenia, unipolar depression; plus diabetes mellitus and IBD as non-psychiatric controls) found **significant enrichment of psychiatric/ASD risk genes specifically in modules tied to neuron commitment and maturation and synapse development** - in both fetal cortex (BS_Grey60/Midnightblue/Turquoise) and CBO (CBO_Turquoise/Black). These disease-relevant modules are **conserved from fetal brain to organoids**.
- **Metabolic stress.** No sustained increase of glycolytic/ER-stress signatures over BO differentiation - argues for a homeostatic metabolic state rather than progressive deleterious stress (contrasts with some scRNA-seq stress reports).

## Methods

- **iPSC/organoids.** hiPSCs reprogrammed (non-integrating self-replicating mRNA) from 4 healthy individuals; CBO differentiated per the authors' prior protocol; single organoids profiled to capture differentiation variability across 2 batches over 200 days.
- **Comparators.** External BO RNA-seq (MGO/FO/TA) re-analyzed; in-house fetal CNS tissue and 2D fetal cultures processed identically to CBO to allow direct comparison; BrainSpan (Miller et al.) as the principal prenatal reference (162 data points, PCW 8-37). Approximate in-vitro-day-to-PCW mapping used for visualization (e.g., day 25 = 3.6 wk, day 50 = 7.1 wk, day 100 = 14.3 wk, day 150 = 21.4 wk, day 200 = 28.6 wk).
- **Analyses.** Stage-wise differential expression (FDR < 0.05, |log2FC| > 1); WGCNA co-expression modules with module-eigengene-vs-stage Spearman correlation (P < 0.01); bulk deconvolution against a developing-human-cortex scRNA-seq reference; whole-transcriptome correlation of each BO data point to each BrainSpan PCW; cross-network module-overlap; GO enrichment; disease-gene overlap enrichment (SFARI, DD2P, GWAS Catalog).
- **Output.** Interactive supplementary tables (Supplementary Files 1-2) cataloguing module membership, behavior over development/differentiation, and prioritized known + novel transcriptional hubs - positioned as a reusable benchmarking framework.

## Relevance to the brain-organoid ASD review

- **Anchor citation for the "fidelity benchmarking vs fetal cortex" theme and for defining the usable benchmark/fidelity window.** It supplies the concrete claim the review needs: standard cortical organoids transcriptomically track human fetal corticogenesis through a **first-trimester-to-mid-fetal window**, with the maturation inflection around **day 100** in this CBO protocol; and divergence is dominated by **timing (heterochronicity), not just which programs appear**.
- **Protocol-choice guidance for ASD modeling.** Because ASD-relevant phenotypes frequently manifest as **delayed or accelerated neuronal differentiation**, a protocol that itself compresses developmental tempo can mask or distort the very phenotype under study. Cheroni gives an explicit ranking lesson: CBO best preserves in-vivo tempo; MGO/FO/TA are accelerated - a "proactive" ASD-genetics program should pick the differentiation method whose timing does not confound the disease timing signal.
- **ASD-gene targeting of conserved modules.** SFARI/ASD-GWAS risk genes concentrate in neuron-maturation and synapse modules that are **preserved from fetal cortex into organoids**, supporting the premise that organoids retain the developmental machinery in which ASD risk acts.
- **Practical benchmark resource.** The WGCNA knowledge base is a ready tool to QC any patient-derived ASD organoid line against fetal-cortex fidelity before interpreting disease effects.

## Open questions / limitations

- **Single genetic background for MGO and FO datasets** - observed differences could be partly line-specific; needs replication across backgrounds (and ideally multiple protocols from the same hiPSC lines at matched time points).
- Only **four archetypal protocols** examined; not the full BO landscape (though chosen as field-defining forerunners).
- External datasets had a **limited/short time window** (mostly 0-100+ days), constraining the heterochronicity comparison; CBO alone extended to very late (200-day) stages.
- Bulk transcriptomics + deconvolution, not single-cell - cell-type proportions are estimates; in-vitro-day-to-PCW conversion is approximate.
- **ECM-gene regulation differs between BO and fetal cortex**, a caveat for interpreting neuropsychiatric modeling datasets (ECM affects folding, progenitor proliferation, migration, synaptic plasticity).

## Related

- [Velasco 2019 - individual brain organoids reproducibly form cortical cell diversity](velasco_2019_individual_brain_organoids_reproducibly.md) - reproducibility / fidelity benchmark counterpart.
- [Paulsen 2022 - autism genes converge on asynchronous development](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) - ASD-as-developmental-timing convergence (directly motivates the heterochronicity concern).
- [Bhaduri 2020 - cell stress in cortical organoids](bhaduri_2020_cell_stress_in_cortical.md) - the metabolic-stress claim Cheroni qualifies.
- [Camp 2015 - organoids recapitulate gene-expression programs of fetal neocortex](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md); [Kanton 2019 single-cell genomic atlas](kanton_2019_organoid_single-cell_genomic_atlas.md); [Trevino 2021 developing-cortex regulatory dynamics](trevino_2021_chromatin_gene_regulatory_dynamics_developing_human_cerebral.md); [Amiri 2018 fetal cortex transcriptome/epigenome](amiri_2018_transcriptome_epigenome_landscape_human_cortical_development_modeled.md) - fetal/atlas references for benchmarking.
- [He 2024 - integrated transcriptomic cell atlas](he_2024_an_integrated_transcriptomic_cell_atlas.md) - newer atlas resource.
- [Mariani 2015 - FOXG1 / GABA-glutamate dysregulation in ASD](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md) - source of the TA dataset and ASD relevance.
- Concept: [brain organoid fidelity, reproducibility and atlases](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- Entity: [single-cell atlas benchmarking](../entities/single-cell-atlas-benchmarking.md)
