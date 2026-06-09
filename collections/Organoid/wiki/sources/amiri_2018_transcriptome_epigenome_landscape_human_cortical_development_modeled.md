---
title: "Transcriptome and epigenome landscape of human cortical development modeled in organoids."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1126/science.aat6720
pmid: 30545853
authors: Amiri A et al.
journal: Science (New York, N.Y.) (2018)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/amiri_2018_transcriptome_epigenome_landscape_human_cortical_development_modeled.pdf
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# Transcriptome and epigenome landscape of human cortical development modeled in organoids.

## Source

- Authors: Anahita Amiri*, Gianfilippo Coppola*, Soraya Scuderi*, Feinan Wu*, Tanmoy Roychowdhury*, Fuchen Liu, Sirisha Pochareddy, Yurae Shin, Alexias Safi, Lingyun Song, Ying Zhu, André M. M. Sousa, The PsychENCODE Consortium, Mark Gerstein, Gregory E. Crawford, Nenad Sestan, Alexej Abyzov‡ (corresponding; Mayo Clinic), Flora M. Vaccarino‡ (corresponding; Yale Child Study Center). (*equal contribution.)
- Journal: Science (2018), Vol 362(6420):eaat6720 (PsychENCODE package, 14 Dec 2018).
- DOI: [10.1126/science.aat6720](https://doi.org/10.1126/science.aat6720)
- PMID: [30545853](https://pubmed.ncbi.nlm.nih.gov/30545853/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Genes implicated in neuropsychiatric disorders are active in human fetal brain, yet difficult to study in a longitudinal fashion. We demonstrate that organoids from human pluripotent cells model cerebral cortical development on the molecular level before 16 weeks postconception. A multiomics analysis revealed differentially active genes and enhancers, with the greatest changes occurring at the transition from stem cells to progenitors. Networks of converging gene and enhancer modules were assembled into six and four global patterns of expression and activity across time. A pattern with progressive down-regulation was enriched with human-gained enhancers, suggesting their importance in early human brain development. A few convergent gene and enhancer modules were enriched in autism-associated genes and genomic variants in autistic children. The organoid model helps identify functional elements that may drive disease onset.

## Key findings

This is the manuscript's **epigenome-fidelity / enhancer-mirroring anchor**: a longitudinal **multiomics** (RNA-seq + snRNA-seq + ChIP-seq for 3 histone marks) comparison of dorsal-forebrain organoids against **isogenic** fetal cortex from the *same* fetal specimens, establishing that organoids reproduce the embryonic-to-early-fetal cortical **gene-regulatory** program, deploy a *larger* enhancer repertoire than mid-fetal cortex, and that organoid/fetal enhancers are enriched for human-gained enhancers and ASD-associated genes/variants.

### Design and developmental staging
- **Isogenic system:** hiPSC lines from **skull/skin fibroblasts of 3 male postmortem fetal specimens (310, 313, 320), aged 15-17 postconception weeks (PCW)**; two hiPSC lines per specimen; two cortical-tissue samples per specimen collected for comparison. (Fetal-derived hiPSCs comparable to adult-derived for pluripotency/growth/differentiation.)
- **Organoids:** telencephalic, patterned to **dorsal forebrain** (Mariani 2015 protocol); 11 days proliferative, then terminal-differentiation (TD) medium. Sampled at **TD0, TD11, TD30** for cellular + nuclear RNA-seq and nuclear ChIP-seq.
- **Histone marks:** H3K4me3 (promoters), H3K27ac (active enhancers/promoters), H3K27me3 (polycomb-repressed). External references: PsychENCODE developmental "Capstone" (Li et al. 2018, *Science* eaat7615), other PsychENCODE, Roadmap Epigenomics (111 epigenomes).
- **Staging result:** organoid transcriptomes map most closely to human neocortex **8-16 PCW**, with isogenic fetal samples mapping to **~16 PCW** - i.e. organoids are reproducibly **younger** (late embryonic-early fetal) than the 17-PCW fetal counterpart. Organoids/iPSC/hESC cluster with fetal (not adult) brain; organoid samples cluster by **in vitro age (TD0/TD11/TD30)** irrespective of hiPSC genetic background, but always **separately from isogenic fetal cortex**.

### Enhancer landscape (the headline numbers)
- **327,877 putative enhancers** called (H3K27ac+, H3K4me3-/H3K27me3-) across organoids + fetal brains; H3K27ac highly concordant with ATAC-seq.
- **96,375 gene-linked enhancers (29.4%)** associated with **22,835** protein-coding/lincRNA genes (of 27,585 Gencode V25), linked by <20 kb proximity or fetal-brain **Hi-C** (Won 2016). 90% concordant with ENCODE/Roadmap; **10,243 (10%) completely novel**.
- **83,608** active in organoids vs **46,735** in isogenic mid-fetal cortex; **49,640 (59%)** of organoid-active enhancers are **organoid-only** and down-regulated in mid-fetal brain → organoids (and by extension embryonic/early-fetal cortex) use **~1.8x as many enhancers** as later cortex. ~11,700 enhancers become active only at TD30.
- **A-regs vs R-regs:** 10.6% of gene-enhancer pairs significantly correlated (15,026 enhancers, 7,858 genes) → **10,192 (67.8%) activating regulators** (A-regs) and **4,993 (33.2%) repressing regulators** (R-regs); **98.9%** are exclusively one or the other. Differential A-/R-reg activity tracks DEG direction (Fisher p < 2.2e-16 both transitions).

### The first transition dominates (stem cell → progenitor)
- Largest gene/enhancer changes are at **TD0→TD11**: **71% of DEGs and 76% of DAEs** occur here, mostly transition-specific (⅔-¾). Down at transition 1: mitosis/cell-cycle (CDK2/4/6) + DNA repair (TP53, BRCA1/2, PCNA). Down at transition 2 (TD11→TD30): cortical-progenitor TFs (SOX1/2, EOMES, LHX2, FOXG1, POU3F2/3, SIX3, FEZF2, EMX2, GLI1/3, NEUROD4, HES5/6, REST, DLL3). Up at both: neuronal/synaptic, channels, CNTN-family ID genes.
- Interpreted as: the in vivo embryonic→fetal transition is a **vulnerable step** for normal brain development.

### Single-nucleus validation
- snRNA-seq of **17,837 nuclei** (1 sample/TD + 1 brain) → **15 clusters**, 11 mostly organoid, 4 mostly fetal cortex. Organoid-specific clusters = diverse RG types (eRG, oRG, vRG, divRG, tRG) + an EN cluster; **only 1 cluster ("cluster 5/Novel") lacked any in vivo correspondence** (possible culture artifact). Fetal-specific clusters carry IN/EN, RG, and a small OPC cluster. TD0 organoid cells match **6-9 PCW** fetal cells; CTX1 matches **15-16.5 PCW** - confirming organoids are younger.

### Networks, human evolution, and ASD
- **WGCNA:** 54 gene modules (MG1-54) + 29 enhancer modules (ME1-29), grouped into **6 gene + 4 enhancer "supermodules."** G1up = synapse/transport (up); G4down = cell-cycle/DNA-repair (down); G5down = cortical-progenitor TFs.
- **Human-gained enhancers (HGEs):** of 8,996 published HGEs (active 7-12 PCW, human > macaque/mouse; Reilly/Noonan), **70% (6,295) overlap** organoid/fetal enhancers; 3,310 gene-associated, **85.3% with differential organoid-vs-fetal activity**. HGEs concentrate in the **down-regulated E3down supermodule** (6 of 8 HGE-enriched enhancer modules), targeting proliferation/communication growth factors (FGF6/7, FGFRL1, ERBB4, IGF2, EGFL7, VEGFA, PDGFA). Consistent with HGE activity peaking in RG, **especially oRG** (expanded in humans).
- **ASD signal:** SFARI genes overrepresented in neuronal/synaptic modules **MG4, MG5** and cell-cycle module **MG51**; these converge with ASD-associated enhancer modules **ME9, ME29, ME2** (ME29 carries both A-regs and R-regs for all 3 ASD gene modules). MG4/MG5 overlap synaptic modules **down-regulated in ASD postmortem cortex** and a synapse module **up in macrocephaly-ASD organoids (Mariani 2015)**; MG51 overlaps the ASD de-novo-variant module M3 (Parikshak 2013). >24% of SFARI genes are DEGs across organoid time; >80% are enhancer-linked.
- **Inherited + de-novo variant enrichment (Simons Simplex Collection, 540 families):** low-frequency inherited SNPs (MAF 0.1-5%) significantly enriched in **probands vs siblings in *early* (organoid-only) enhancers** (p=0.02) and in enhancer modules ME2/ME29 (p=0.05/0.03) - but **not** in late or constant enhancers → supports a multiple-low-effect-inherited-variant model. De novo mutations (66,306 total; 2,422 in gene-linked enhancers) trend toward constant enhancers in probands; ~24% overlap a TF motif; motif-breaking DNMs significantly enriched in probands for **homeodomain, Hes1, NR4A2, Sox3, NFIX** TFs (NR4A2 CNVs previously tied to ASD with language/cognitive impairment).

## Methods

- **Organoids:** dorsal-forebrain telencephalic organoids per Mariani et al. 2015 (FOXG1+ forebrain protocol); proliferative 11 d → TD medium; collected at TD0/TD11/TD30. IHC for proliferation, glutamatergic, GABAergic markers as differentiation QC; proliferation markers progressively down TD0→TD30.
- **Assays:** total stranded RNA-seq (whole cells + nuclei; the two are highly correlated, so cellular transcriptome used downstream); **snRNA-seq** (~10,000 cells/sample shallow-seq, top 6,000 informative, ≥500 genes → 17,837 cells); **ChIP-seq** for H3K4me3/H3K27ac/H3K27me3 (nuclei).
- **Analysis:** edgeR (trended dispersion) for DEGs/DAEs; **Seurat** (snRNA-seq clustering, batch-corrected tSNE); **Monocle** (pseudotime/trajectories, cell-cycle scoring); MACS2 peak calling; **chromHMM** chromatin segmentation into promoter/enhancer/repressed states; enhancer→gene linkage by <20 kb proximity + fetal-brain **Hi-C** (Won 2016); **WGCNA** modules + K-means supermodules; ConsensusPathDB/ToppGene GO; qPCR cross-validation incl. ASD genes; JASPAR TF motifs. Variant data: SFARI/Simons Simplex Collection (540 families), Werling et al. de novo SNPs.

## Relevance to the brain-organoid ASD review

- **The epigenome/enhancer half of the fidelity argument.** Where [Camp 2015](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md) anchors *transcriptomic* organoid-fetal concordance at single-cell resolution, Amiri supplies the **regulatory-genome mirroring** evidence using **isogenic** organoid/fetal pairs and three histone marks: organoid and fetal cortex deploy a shared, stage-resolved enhancer program. This is the citation for "organoids recapitulate the **epigenetic / gene-regulatory** landscape of early human cortex," not just steady-state expression.
- **Defines *which* developmental window and a key asymmetry.** Organoids model **late-embryonic to early-fetal (8-16 PCW)** cortex - earlier than the ~16-17 PCW isogenic tissue and earlier than most accessible postmortem material - and reveal that this early window uses **~1.8x more enhancers** (the 49,640 organoid-only enhancers), most extinguished by mid-fetal stages. The review can cite organoids as a window onto a *regulatory-rich, otherwise-inaccessible* embryonic period when ASD lineage decisions are made.
- **Direct noncoding-ASD mechanism.** Provides one of the field's first demonstrations that **noncoding/enhancer variants** (inherited low-frequency SNPs in early enhancers; motif-breaking de novo mutations at Hes1/Sox3/NR4A2/NFIX/homeodomain sites) are enriched in ASD probands and converge on ASD gene modules - a model that "programmable" organoids could prospectively test. Ties the SFARI/Simons Simplex cohorts to organoid-derived regulatory elements.
- **Human-specific evolution bridge.** HGEs are active earliest in organoids, target RG growth/proliferation genes (FGF/IGF/VEGF/PDGF), and concentrate in oRG - linking the fidelity strand to the human-cortical-expansion strand carried by [Pollen 2015](pollen_2015_molecular_identity_human_outer_radial_glia_during.md), [Pollen 2019](pollen_2019_establishing_cerebral_organoids_as_models_human_specific.md), and the NOTCH2NL papers. (Same Vaccarino group as Mariani 2015 - the macrocephaly-ASD organoid module overlaps MG4/MG5 here.)

## Open questions / limitations

- **Organoids are younger and never fully match isogenic fetal cortex.** They cluster separately from the 17-PCW tissue at every stage; the authors explicitly note it "remains unclear whether organoids fully recapitulate developmental processes, particularly those at later stages," and that longer cultures may overlap mid-fetal brain more (Giandomenico 2019, Quadrato 2017). The organoid-only enhancer set is partly a *stage* difference, not purely an in-vitro artifact.
- **One snRNA-seq cluster ("Novel", cluster 5) has no in vivo counterpart** - a candidate culture artifact left unexplained.
- **Enhancers are computationally defined and largely unvalidated functionally.** Linkage rests on H3K27ac + proximity/Hi-C correlation; the authors state cataloged elements "may require further validation of their in vivo activity." Causality from variant → enhancer → gene → ASD phenotype is inferred, not demonstrated.
- **Small, male-only, dorsal-forebrain cohort.** 3 male fetal specimens, two hiPSC lines each, single guided protocol; no female specimens, no ventral/other regional identities, no functional/neuronal-activity readouts. Generalizability across protocols/lines is argued (shared neural-stem-cell origin) but not tested here.
- **Variant enrichments are modest.** Inherited-SNP enrichment p=0.02 and motif-breaking-DNM signals (p<0.05 binomial) are statistically modest on small de-novo counts; the low-effect-inherited-variant model is supported but not proven.

## Related

- [Camp 2015 — Human cerebral organoids recapitulate gene expression programs of fetal neocortex development](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md) — the single-cell transcriptomic fidelity benchmark this paper complements on the epigenome/enhancer axis.
- [Mariani 2015 — FOXG1-dependent dysregulation of GABA/glutamate neuron differentiation in ASD](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md) — same Vaccarino lab; supplies the dorsal-forebrain organoid protocol used here, and the macrocephaly-ASD synapse module that overlaps MG4/MG5.
- [Pollen 2015 — Molecular identity of human outer radial glia during cortical development](pollen_2015_molecular_identity_human_outer_radial_glia_during.md) — the oRG compartment where human-gained enhancers are most active.
- [Pollen 2019 — Establishing cerebral organoids as models of human-specific brain evolution](pollen_2019_establishing_cerebral_organoids_as_models_human_specific.md) — companion human-specific-evolution organoid study (HGE/duplication-driven RG biology).
- [Hevner 2019 — Intermediate progenitors and Tbr2 in cortical development](hevner_2019_intermediate_progenitors_tbr2_cortical_development.md) — EOMES/TBR2 (a transition-2 down-regulated TF here) and the IPC compartment that links RG to neurons.
- [Bhaduri 2020 — Cell stress in cortical organoids impairs molecular subtype specification](bhaduri_2020_cell_stress_in_cortical.md) — formalizes the metabolic/culture-stress caveats relevant to the organoid-only signatures seen here.
- [Cheroni 2022 — Benchmarking brain organoid recapitulation of fetal corticogenesis](cheroni_2022_benchmarking_brain_organoid_recapitulation_fetal_corticogenesis.md) — multi-protocol fidelity-window benchmark against BrainSpan.
- [Kanton 2019 — Organoid single-cell genomic atlas uncovers human-specific features of brain development](kanton_2019_organoid_single-cell_genomic_atlas.md) — single-cell + epigenome organoid-vs-primate atlas extending this comparison.
- Concept: [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- Entity: [Single-cell atlas benchmarking](../entities/single-cell-atlas-benchmarking.md)
