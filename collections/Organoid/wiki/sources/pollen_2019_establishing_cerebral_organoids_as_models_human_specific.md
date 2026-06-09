---
title: "Establishing Cerebral Organoids as Models of Human-Specific Brain Evolution."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1016/j.cell.2019.01.017
pmid: 30735633
authors: Pollen AA et al.
journal: Cell (2019)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/pollen_2019_establishing_cerebral_organoids_as_models_human_specific.pdf
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# Establishing Cerebral Organoids as Models of Human-Specific Brain Evolution.

## Source

- Authors: Alex A. Pollen1,2,* (co-first, lead contact), Aparna Bhaduri (co-first), Madeline G. Andrews, Tomasz J. Nowakowski, Olivia S. Meyerson, Mohammed A. Mostajo-Radji, Elizabeth Di Lullo, Beatriz Alvarado, Melanie Bedolli, Max L. Dougherty, Ian T. Fiddes, Zev N. Kronenberg, Joe Shuga, Anne A. Leyrat, Jay A. West, Marina Bershteyn, Craig B. Lowe, Bryan J. Pavlovic, Sofie R. Salama, David Haussler, Evan E. Eichler, Arnold R. Kriegstein* (corresponding). (UCSF; UC Santa Cruz; Univ. Washington; Fluidigm; Stanford.)
- Journal: Cell (2019), Vol 176(4):743-756 (7 Feb 2019).
- DOI: [10.1016/j.cell.2019.01.017](https://doi.org/10.1016/j.cell.2019.01.017)
- PMID: [30735633](https://pubmed.ncbi.nlm.nih.gov/30735633/)
- Data: RNA-seq GEO **GSE124299** and phs000989.v3.
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Direct comparisons of human and non-human primate brains can reveal molecular pathways underlying remarkable specializations of the human brain. However, chimpanzee tissue is inaccessible during neocortical neurogenesis when differences in brain size first appear. To identify human-specific features of cortical development, we leveraged recent innovations that permit generating pluripotent stem cell-derived cerebral organoids from chimpanzee. Despite metabolic differences, organoid models preserve gene regulatory networks related to primary cell types and developmental processes. We further identified 261 differentially expressed genes in human compared to both chimpanzee organoids and macaque cortex, enriched for recent gene duplications, and including multiple regulators of PI3K-AKT-mTOR signaling. We observed increased activation of this pathway in human radial glia, dependent on two receptors upregulated specifically in human: INSR and ITGB8. Our findings establish a platform for systematic analysis of molecular changes contributing to human brain development and evolution.

## Key findings

The manuscript's **human-specific brain-evolution anchor**: a single-cell, cross-species (human / chimpanzee / macaque) **primary + organoid** comparison that (1) validates organoids as faithful models of primate cortical *gene regulation*, then (2) uses **chimpanzee organoids** - an otherwise-inaccessible window onto ape prenatal corticogenesis - to isolate **261 human-derived gene-expression changes**, converging on **increased PI3K-AKT-mTOR activation in human outer-subventricular-zone radial glia**.

### Cross-species design (the "cellular anthropology" platform)
- Single-cell RNA-seq across: **48 human + 6 macaque primary** cortical samples and **56 organoids from 10 human + 8 chimpanzee** individuals, spanning cortical neurogenesis (Fig 1B). Primary human data from Nowakowski et al. 2017.
- **Three nested comparisons** (Fig 1A): (i) human primary vs human organoid = organoid "report card"; (ii) human vs macaque **primary** = developmental divergence across ~25 My; (iii) human vs chimpanzee **organoid** = changes derived on the human lineage in the **last ~6 My**. The chimp organoid is the key enabling reagent (no prenatal chimp tissue).
- Organoids: **Sasai/Kadoshima 2013** guided cortical protocol; two further published protocols (Camp/Lancaster unguided; Sloan/Pasca cortical spheroid) reanalyzed as a guided→unguided continuum. Cross-species alignment used the **Comparative Annotation Toolkit (Fiddes 2018)** + a de novo chimp genome assembly (Kronenberg 2018) → **49,360 orthologous genes** aligned to each species' native genome.

### Organoid fidelity to primary tissue (report card)
- Organoids contain telencephalic excitatory-lineage cells (RG across cell-cycle phases, **TBR2/EOMES+ IPCs**, excitatory neurons) + some ventral-telencephalic interneurons, with **VZ/SVZ-like germinal zones** by IHC (SOX2, TBR2/EOMES, CTIP2/BCL11B, SATB2) - but a **greatly compressed** ventricle-to-pia distance and a much smaller intermediate zone / cortical plate than primary cortex.
- **Gene co-expression modules are highly preserved and conserved:** independently derived WGCNA modules correlate across datasets (Pearson R > 0.5); **>70% of human primary modules** correlate >0.7 with a human organoid module. Cell-type/state modules (RG subtypes incl. **HOPX+ OSVZ-RG**, IPC, interneuron LGE/CGE/MGE subtypes, G1/S & G2/M, neuronal maturation) emerge across species and systems. Modules for cell types **rare in organoids** (microglia, OPCs) appear only in primary data.
- Developmental trajectories (RG→neuron differentiation; RG maturation; areal V1-vs-PFC identity) arise **spontaneously** in organoids, but with **heterochronic / variable timing**: the RG-maturation signature correlates better with *primary* age than *organoid* age. Composition varies by individual/protocol (2 of 10 human iPSC lines made mostly off-target hindbrain: 8/9 organoids).

### Organoid metabolic-stress signature (the fidelity caveat)
- Across **all three protocols**, organoids over-express the same modules vs primary tissue: **glycolysis** (strongest), **endoplasmic-reticulum stress / unfolded-protein response**, and **electron transport**. These are normal pathways pathologically **over-activated** in vitro (glycolysis modules also exist in primary cells but are higher/more pervasive in organoids) - flagged as optimization targets (media/perfusion).

### 261 human-specific expression changes
- **1,258 DEGs** human-vs-macaque (primary) and **738 DEGs** human-vs-chimp (organoid); **261 overlap** (p < 1e-16) = candidate **human-derived** cortical-development changes, supported independently by primary and organoid data. Direction/fold-change correlated across comparisons.
- **85% are cortex-specific** (distinct from human-chimp fibroblast/iPSC DEGs; Gallego Romero 2015) yet **shared across cortical cell types** - consistent with hierarchical regulatory pleiotropy.
- **Enriched for recent gene duplications** (Sudmant 2013; p < 1e-7): e.g. SMN1, ARL17A loci up in human; NPIPB5 (single derived paralog of expanded NPIP family); SLC29A4 (human-chimp-ancestral duplication, higher in human IZ/CP). Modest enrichment for older ape duplications too (p < 0.005).
- **ASD overlap:** of 78 high-confidence ASD de-novo-mutation genes (Stessman 2017), **5** overlap the strict 261 and **4** more the broader 668-gene set (incl. **SRCAP**) - moderately significant (hypergeometric p < 0.005).
- **Human-derived co-expression networks:** the two strongest human-gained modules are enriched for **negative regulation of transcription at G1/S** and **neuronal apoptosis** (p < 1e-6) - both able to tune progenitor/neuron number; a human-RG module's gain is partly driven by **NBPF** gene duplication.

### PI3K-AKT-mTOR in human outer RG (the mechanistic result)
- mTOR-pathway genes top the (uncorrected) GO ranking among DEGs; both **activators (INSR, ITGB8, IFNAR1)** and a repressor (**PTEN**) are up in human organoids + primary cells.
- **Phospho-S6 (pS6, mTOR effector) is strongly elevated in human OSVZ radial glia** vs macaque (primary) and chimp (organoid) - cortical-plate neurons show comparable pS6 across species, so the change is **progenitor/OSVZ-RG-specific** (aggregate Welch p < 1e-6). Western blots confirm higher pS6, p4EBP1, pNDRG1 and INSR protein in human.
- **Causal test:** macaque RG can be driven to higher pS6 by BDNF/3BDO (so primate RG are *poised* to activate mTOR); **shRNA knockdown of INSR or ITGB8 in human organotypic slices reduces pS6** in the OSVZ (Welch p < 0.05/0.01) → INSR + ITGB8 are candidate human-lineage upstream drivers of elevated mTOR in human outer RG.
- Distinguished from the earlier **LIFR-STAT3** OSVZ-RG self-renewal signature (Pollen 2015), which was **conserved in macaque** and thus *not* a recent human change - whereas the mTOR change is human-derived.

## Methods

- **Organoid differentiation:** Kadoshima/Sasai 2013 guided cortical protocol (primary new dataset, 10 human + 8 chimpanzee lines); plus reanalysis of unguided whole-brain (Lancaster/Camp 2015) and cortical-spheroid (Sloan/Pasca 2017) protocols.
- **scRNA-seq:** standardized capture across primary (48 human, 6 macaque) and organoid cells; some chimeric/multiplexed organoids de-multiplexed computationally; "report card" pipeline benchmarking organoid cells against primary tissue.
- **Cross-species genomics:** Comparative Annotation Toolkit (Fiddes 2018) re-annotation of chimp + macaque; de novo chimp assembly (Kronenberg 2018); reads aligned to native genomes; 49,360 orthologs. (Authors caution residual bias toward the higher-quality human assembly, especially for macaque.)
- **Clustering / networks:** canonical correlation analysis (Seurat/Butler 2018) to co-cluster homologous cell types across systems/species; **WGCNA** modules computed independently per dataset then correlated; GLM linking modules to cell type/individual/species/system.
- **Differential expression:** likelihood-ratio test + GLM (variancePartition) accounting for biological/technical replicates; gene-set/duplication/ASD overlap by hypergeometric tests.
- **Protein / functional validation:** IHC for pS6 across species; western blots (INSR, pS6, p4EBP1, pNDRG1) on progenitor-enriched cultures + 5-week organoids; mTOR activation in macaque cells with BDNF + 3BDO; **shRNA-lentiviral knockdown of INSR / ITGB8** in primary human organotypic slice culture; in situ hybridization (e.g. SRCAP, SLC29A4).

## Relevance to the brain-organoid ASD review

**The human-specific-evolution / heterochrony anchor** for the review's "organoids as models of human-specific brain evolution" theme.

- **Establishes the cross-species organoid paradigm.** Because prenatal chimpanzee tissue is inaccessible during neurogenesis, **chimp (and human) organoids are the only window** onto when/how human cortical-development differences arose - the explicit justification for using organoids to study **human-specific** brain evolution. The 3-way (human/chimp/macaque, primary+organoid) design lets the review claim organoids can polarize changes to the **~6-My human lineage**.
- **Supplies the fidelity precondition.** Demonstrates organoids **preserve and conserve gene-regulatory networks, cell types (incl. TBR2/EOMES IPCs and HOPX+ OSVZ-RG), and developmental trajectories** across species and protocols - reinforcing the [Camp 2015](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md)/[Amiri 2018](amiri_2018_transcriptome_epigenome_landscape_human_cortical_development_modeled.md) fidelity argument, while quantifying the limits (compressed architecture, variable composition, glycolysis/ER-stress over-activation).
- **Names heterochrony explicitly.** RG maturation tracks primary age better than organoid age (variable in-vitro tempo) - the developmental-timing/heterochrony point the review can cite for both evolution (human neoteny) and disease modeling.
- **Direct ASD-mechanism convergence on mTOR.** Human-derived elevation of **PI3K-AKT-mTOR (INSR/ITGB8-dependent) in outer RG** is the same pathway repeatedly tied to ASD, focal cortical dysplasia, and macrocephaly - linking *human-specific* RG biology to the *ASD-overgrowth* phenotypes the review targets, and dovetailing with the lab's mTOR-oRG morphology work ([Andrews 2020](andrews_2020_mtor_signaling_regulates_morphology_migration_outer_radial.md)). Also flags ASD genes (SRCAP +others) among human-derived changes.
- **Connects to the expansion-gene literature.** Human-derived DEGs enriched for **recent duplications** (NBPF/NPIP/SMN1/ARL17A) frame the broader human-cortical-expansion story carried by the **NOTCH2NL** ([Fiddes 2018](fiddes_2018_human_specific_notch2nl_genes_affect_notch_signaling.md), [Suzuki 2018](suzuki_2018_human_specific_notch2nl_genes_expand_cortical_neurogenesis.md)) and oRG ([Pollen 2015](pollen_2015_molecular_identity_human_outer_radial_glia_during.md)) papers.

## Open questions / limitations

- **Organoid architecture and timing are not faithful.** Severely compressed VZ-to-pia distance, small IZ/CP, heterogeneous composition across individuals/protocols (off-target hindbrain in some lines), and **variable maturation tempo** - so only **gene regulation** (not cytoarchitecture, connectivity, lamination) is validated for evolutionary inference; the authors restrict claims accordingly.
- **Pervasive metabolic-stress artifact.** Glycolysis / ER-stress / electron-transport over-activation across all protocols is a systematic deviation from primary tissue (optimization target; potential confound, esp. for stress-sensitive disease phenotypes).
- **Residual genome-assembly/annotation bias**, especially for **macaque**, may distort some cross-species expression estimates; mitigated but not eliminated by CAT + de novo chimp assembly. Authors call for long-read primate genomes + more individuals/cells.
- **mTOR causality is partial.** INSR/ITGB8 knockdown lowers pS6 (necessity in human slices), but the *human-specific* upstream genetic change driving INSR/ITGB8 upregulation is not identified; increased mTOR could partly be a *consequence* of greater human RG proliferation rather than a cause. Effects on actual neuron output/brain size untested here.
- **ASD/duplication overlaps are statistically modest** (p < 0.005; small gene counts) and correlational; no disease modeling is performed (this is a normal cross-species developmental study).
- **Chimpanzee iPSC ethics/availability** constrain replication; relies on a limited set of ape lines.

## Related

- [Camp 2015 — Human cerebral organoids recapitulate gene expression programs of fetal neocortex development](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md) — the foundational single-cell organoid-fetal fidelity benchmark this study extends across species (and whose Lancaster-protocol data are reanalyzed here).
- [Pollen 2015 — Molecular identity of human outer radial glia during cortical development](pollen_2015_molecular_identity_human_outer_radial_glia_during.md) — same lead author; defines the HOPX+ oRG compartment and the LIFR-STAT3 (conserved, non-human-specific) signature contrasted with the human-derived mTOR change here.
- [Andrews 2020 — mTOR signaling regulates the morphology and migration of outer radial glia](andrews_2020_mtor_signaling_regulates_morphology_migration_outer_radial.md) — same lab; downstream cell-biology of the mTOR-in-oRG axis identified here.
- [Amiri 2018 — Transcriptome and epigenome landscape of human cortical development modeled in organoids](amiri_2018_transcriptome_epigenome_landscape_human_cortical_development_modeled.md) — complementary human-gained-enhancer / epigenome evidence for organoids as human-evolution models.
- [Hevner 2019 — Intermediate progenitors and Tbr2 in cortical development](hevner_2019_intermediate_progenitors_tbr2_cortical_development.md) — biology of the TBR2/EOMES+ IPC compartment marked here; indirect neurogenesis and cortical expansion.
- [Fiddes 2018 — Human-specific NOTCH2NL genes affect Notch signaling and cortical neurogenesis](fiddes_2018_human_specific_notch2nl_genes_affect_notch_signaling.md) — human-specific duplicated genes expanding cortical neurogenesis; the duplication-driven expansion theme.
- [Suzuki 2018 — Human-specific NOTCH2NL genes expand cortical neurogenesis through Delta/Notch regulation](suzuki_2018_human_specific_notch2nl_genes_expand_cortical_neurogenesis.md) — parallel NOTCH2NL human-expansion study.
- [Benito-Kwiecinski 2021 — An early cell shape transition drives evolutionary expansion of the human forebrain](benitokwiecinski_2021_early_cell_shape_transition_drives_evolutionary_expansion.md) — human-vs-ape organoid comparison of progenitor behavior driving expansion.
- [Kanton 2019 — Organoid single-cell genomic atlas uncovers human-specific features of brain development](kanton_2019_organoid_single-cell_genomic_atlas.md) — contemporaneous human/ape organoid single-cell atlas on the same human-specific-evolution question.
- [Bhaduri 2020 — Cell stress in cortical organoids impairs molecular subtype specification](bhaduri_2020_cell_stress_in_cortical.md) — first-author overlap; formalizes the glycolysis/metabolic-stress signature flagged here.
- Concept: [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- Entity: [Single-cell atlas benchmarking](../entities/single-cell-atlas-benchmarking.md)
