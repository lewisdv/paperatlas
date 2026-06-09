---
title: "Proper acquisition of cell class identity in organoids allows definition of fate specification programs of the human cerebral cortex."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.cell.2022.09.010
pmid: 36179669
authors: Uzquiano A et al.
journal: Cell (2022)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Proper acquisition of cell class identity in organoids allows definition of fate specification programs of the human cerebral cortex.

## Source

- Authors: Uzquiano A, Kedaigle AJ, Pigoni M, Paulsen B, Adiconis X, Kim K, Faits T, Nagaraja S et al. (Arlotta lab; co-senior Regev, Levin)
- Journal: Cell (2022); 185(20):3770–3788
- DOI: [10.1016/j.cell.2022.09.010](https://doi.org/10.1016/j.cell.2022.09.010)
- PMID: [36179669](https://pubmed.ncbi.nlm.nih.gov/36179669/)
- Added via: manuscript_brain_organoid_v6 reference ingest
- Data resource: Single Cell Portal SCP1756; Mendeley Data 10.17632/7cxccpv4hg.1

## Abstract

Realizing the full utility of brain organoids to study human development requires understanding whether organoids precisely replicate endogenous cellular and molecular events, particularly since acquisition of cell identity in organoids can be impaired by abnormal metabolic states. We present a comprehensive single-cell transcriptomic, epigenetic, and spatial atlas of human cortical organoid development, comprising over 610,000 cells, from generation of neural progenitors through production of differentiated neuronal and glial subtypes. We show that processes of cellular diversification correlate closely to endogenous ones, irrespective of metabolic state, empowering the use of this atlas to study human fate specification. We define longitudinal molecular trajectories of cortical cell types during organoid development, identify genes with predicted human-specific roles in lineage establishment, and uncover early transcriptional diversity of human callosal neurons. The findings validate this comprehensive atlas of human corticogenesis in vitro as a resource to prime investigation into the mechanisms of human cortical development.

## Key findings

- **Multiomic atlas scale**: >610,000 cells across 6 months / 8 timepoints (23 days, 1, 1.5, 2, 3, 4, 5, 6 months). Components: 532,414 scRNA-seq cells (218,240 newly profiled + prior Velasco 2019 / Paulsen 2022) across 83 individually profiled organoids, 2–6 stem-cell lines per stage, 2–7 differentiation batches per line/stage; 38,017 scATAC-seq nuclei; 42,810 SHARE-seq cells (paired RNA+ATAC, 23 days–3 months); 10 organoids by Slide-seqV2 spatial transcriptomics (1, 2, 3 months). Lines include 11a, GM08330, HUES66, Mito210 c1/c2, PGP1 c1/c2.
- **Reproducible, in-vivo-ordered diversification**: differentiation transitions (aRG → IP → oRG; deep-layer then upper-layer neurons; later astroglia/OPC/interneurons) mirror the in vivo order. Adjusted mutual information (AMI) between cell type and organoid-of-origin was comparable to that of two published fetal datasets (Polioudakis 2019; Trevino 2021) and a newly generated fetal dataset — i.e., organoid-to-organoid variability is in the same low range as fetal/technical variability, including at the epigenetic level.
- **Off-target cell types are early and transient**: at 23 days, 25–60% of cells were non-telencephalic (putative midbrain, hindbrain, thalamus, neural placode, neural crest, subcortical interneurons); 8.1% non-cortical remained at 1 month; from 2 months onward organoids were **exclusively** cortical cell types.
- **Fidelity is cell-type- and stage-specific and high**: cell-type gene-expression signatures (top 200 genes) showed no statistically significant difference in mean across organoids at any timepoint (one-way ANOVA, p > 0.05). Integration with 91,844 published fetal profiles + 60,806 newly generated fetal snRNA-seq (PCW 14/15/16/18); bidirectional random-forest classifiers and RRHO2 showed high organoid↔fetal correspondence (e.g., organoid CFuPN↔fetal ExDp, CPN↔ExM-U, unspecified PN↔ExN, aRG↔vRG).
- **Metabolic state does NOT broadly impair identity** (central claim, rebuts Bhaduri 2020): a WGCNA glycolysis module (emerging ~1.5 months) and MSigDB glycolysis/hypoxia gene sets were enriched specifically in aRG and an early "unspecified PN" population (TBR1/NEUROD2/NEUROD6+, lacking subtype markers) — but a comparable enrichment is seen in a subset of endogenous fetal progenitors. Removing each of 38 MSigDB metabolic gene sets from the classifier changed assignments only for glucose-metabolism and hypoxia sets, and only increased fetal-cell assignment to the aRG and unspecified-PN labels (FDR < 0.0001); apoptosis and oxidative phosphorylation had no effect. Compass flux-balance analysis could not discriminate organoid vs fetal cells on metabolic flux (PC1 tracked cell complexity, not dataset).
- **Affected cells are few and spatially confined**: metabolically affected aRG + unspecified PN are only **3–15% of cells at 2–6 months** and are restricted to the hypoxic organoid core (confirmed by pimonidazole hypoxia reagent and stress-marker IHC). Glycolysis/hypoxia gene expression rose toward the center independent of cell identity.
- **Cross-protocol replication**: 69,333 cells from a different model (Quadrato 2017 whole-brain organoids, 3.5 months) showed the same restricted glycolysis/hypoxia enrichment in aRG and unspecified PN; oxidative phosphorylation was not specifically enriched in any cortical type in either model or fetal tissue.
- **Lineage logic**: trajectory inference on 459,711 cortical cells (FLOWMAP force-directed graph + URD tree) reproduced expected relationships (aRG→IP/oRG and neurons; oRG→neurons and, at 5–6 months, glia). Evidence for oRG→IP (2.7% of IP neighbors are oRG) and a late (5–6 month) pre-OPC population co-expressing oRG markers (HES1/HOPX/MOXD1) and oligodendrocyte markers (EGFR/PDGFRA/OLIG1/OLIG2), supporting oRG contribution to glial lineages.
- **Predicted human-specific regulators**: TFs not previously tied to neuro/gliogenesis associated with human-tree branches — DACH1, TSHZ1 (neuronal), CXXC5, ZFHX4 (glial), ZNF704 (CPN, divergent vs mouse Zfp704). Candidate human regulators lacking 1:1 mouse orthologs: ZNF26, ZNF37A (neuronal commitment); ZNF264 (motif enriched in early CFuPN lineage in SHARE-seq, expressed in 3 fetal datasets). FEZF2 highlighted as a DORC with a CADPS-region cis-regulatory interaction specific to the CFuPN lineage.
- **Early callosal (CPN) diversity**: the gene-expression heterogeneity of adult human CPN (5 subtypes; Hodge 2019 / Berg 2021) begins to emerge in early development — all 5 adult CPN modules were already expressed in both fetal and organoid CPN (module 5 most distinct), though not yet resolving 5 discrete subpopulations. Suggests diversity arises from developmental events, not later activity.

## Methods

- **Modalities**: 10X scRNA-seq (8 timepoints), scATAC-seq (1/3/6 months, 49,568 profiles analyzed incl. prior data), SHARE-seq (paired RNA+ATAC, 4 timepoints), bulk ATAC-seq at 23 days (reference peak set), Slide-seqV2 spatial (10 µm beads; deconvolved with RCTD).
- **Organoid model**: dorsally-patterned cortical organoids (Velasco 2019 protocol lineage); validated against Quadrato 2017 whole-brain organoids as a second model.
- **Fetal references**: newly generated snRNA-seq at PCW 14/15/16/18 (60,806 nuclei) plus published Polioudakis 2019 and Trevino 2021 datasets.
- **Analysis**: AMI for reproducibility; pseudo-bulk DE with organoid-variability control; HOMER TF-motif enrichment; SHARE-seq motif–expression correlation and DORCs (Cicero); random-forest cross-classification; RRHO2 overlap; WGCNA; Compass flux-balance metabolic modeling; FLOWMAP + URD trajectory inference; cNMF for CPN modules; mouse comparison via Di Bella 2021.

## Relevance to the brain-organoid ASD review

- **Fidelity / cell-class-identity benchmark — the keystone reference.** This is the most comprehensive multiomic demonstration that dorsally-patterned cortical organoids acquire correct cortical cell-class identity, with cell-type signatures statistically indistinguishable across organoids and high bidirectional concordance to fetal cortex. It is the affirmative answer to the "do organoids make the right cells?" question that any organoid-based ASD model must clear before phenotypes can be trusted.
- **Directly rebuts the metabolic-stress critique** ([Bhaduri 2020](bhaduri_2020_cell_stress_in_cortical.md)): under appropriate culture, metabolic perturbation affects identity of only 2 cell types (aRG, unspecified PN), only 3–15% of cells, confined to the organoid core, and via glycolysis/hypoxia specifically — not a broad failure of identity. This bounds the known fidelity caveat for the review's methods section.
- **Provides the cell-type and temporal map** against which ASD perturbations (e.g., [Fu 2023 PTEN](fu_2023_autism_specific_pten_p_ile135leu_variant_autism.md), [Paulsen 2022](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md)) can be located: neurogenesis windows (DL PN ~1 mo, CFuPN ~1.5 mo, CPN ~2 mo, glia 4–6 mo), and the oRG/IP progenitor sources whose overproduction is the Fu phenotype.
- **Human-specific corticogenesis features** (early CPN diversification; human-specific regulators) are exactly the upper-layer/callosal programs implicated in ASD, motivating organoids as the platform for human-specific disease mechanisms.
- Notes microglia (Mic) only as a fetal cell type absent from these organoids — flagging the neuroimmune gap that [Schafer 2023](schafer_2023_vivo_neuroimmune_organoid_model_study_human_microglia.md) fills.

## Open questions / limitations

- aRG and "unspecified PN" identity remain genuinely sensitive to core hypoxia/glycolysis; these populations are the weakest-fidelity compartment and should be interpreted cautiously.
- Loss of rosette/structural organization by 3 months limits later-stage spatial/architectural fidelity.
- Maturation ceiling: synapse- and cell-cycle-related terms were the most prominent differences between organoid and fetal cells (RRHO2), consistent with incomplete maturation; oxidative phosphorylation and lipid metabolism ranked higher in organoids than fetal datasets.
- Human-specific regulator candidates (ZNF704, ZNF26, ZNF37A, ZNF264, etc.) are predictions from motif/expression correlation, not functionally validated here.
- Full adult CPN subtype diversity is not yet reached at 6 months — early divergence only.
- Findings are specific to this dorsal cortical protocol (plus one whole-brain replication); generalization to other protocols is not exhaustively tested.

## Related

- [Velasco 2019 — individual brain organoids reproducibly](velasco_2019_individual_brain_organoids_reproducibly.md) (same lab; reproducibility foundation, data reused here)
- [Bhaduri 2020 — cell stress in cortical organoids](bhaduri_2020_cell_stress_in_cortical.md) (the metabolic-impairment claim this paper bounds/rebuts)
- [Camp 2015 — organoid–fetal gene-expression concordance](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md)
- [Pollen 2015 — molecular identity of human oRG](pollen_2015_molecular_identity_human_outer_radial_glia_during.md)
- [Trevino 2021 — chromatin/gene-regulatory dynamics of developing human cortex](trevino_2021_chromatin_gene_regulatory_dynamics_developing_human_cerebral.md) (fetal reference)
- [Quadrato 2017 — whole-brain organoid cell diversity](quadrato_2017_cell_diversity_network_dynamics_photosensitive_human_brain.md) (second model validated here)
- [Pollen 2019 — cerebral organoids as models of human-specific features](pollen_2019_establishing_cerebral_organoids_as_models_human_specific.md)
- [Paulsen 2022 — ASD genes converge on shared neuron development](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) (same lab, ASD application)
- Concept: [Brain organoid fidelity, reproducibility, and atlases](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
