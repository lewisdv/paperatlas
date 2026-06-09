---
title: "Site-saturation mutagenesis of 500 human protein domains."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41586-024-08370-4
pmid: 39779847
authors: Beltran A et al.
journal: Nature (2025)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Beltran_2025_Site_saturation_mutagenesis_500_human_protein_domains.pdf
pdf_status: downloaded
---

# Site-saturation mutagenesis of 500 human protein domains.

## Source

- Authors: Beltran A, Jiang X, Shen Y, Lehner B (corresponding: Ben Lehner, CRG Barcelona / Wellcome Sanger)
- Journal: Nature (2025); Vol 637, 23 January 2025, pp. 885–892. Open access.
- DOI: [10.1038/s41586-024-08370-4](https://doi.org/10.1038/s41586-024-08370-4)
- PMID: [39779847](https://pubmed.ncbi.nlm.nih.gov/39779847/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Missense variants that change the amino acid sequences of proteins cause one-third of human genetic diseases1. Tens of millions of missense variants exist in the current human population, and the vast majority of these have unknown functional consequences. Here we present a large-scale experimental analysis of human missense variants across many different proteins. Using DNA synthesis and cellular selection experiments we quantify the effect of more than 500,000 variants on the abundance of more than 500 human protein domains. This dataset reveals that 60% of pathogenic missense variants reduce protein stability. The contribution of stability to protein fitness varies across proteins and diseases and is particularly important in recessive disorders. We combine stability measurements with protein language models to annotate functional sites across proteins. Mutational effects on stability are largely conserved in homologous domains, enabling accurate stability prediction across entire protein families using energy models. Our data demonstrate the feasibility of assaying human protein variants at scale and provides a large consistent reference dataset for clinical variant interpretation and training and benchmarking of computational methods.

## Key findings

- **Scale ("Human Domainome 1").** Designed library of **1,230,584 aa variants in 1,248 domains** (every residue → all 19 other aa; 91% designed coverage). After QC, final dataset = **abundance measurements for 563,534 variants in 522 protein domains** (503 from human proteins). Represents **~5× increase** in stability measurements for human protein variants over prior datasets.
- **Coverage of the proteome.** 522 domains span 127 families = **2.1% of all proteins, 1.2% of all domains, 2.0% of unique domain families** in the human proteome. Structurally diverse: 195 all-alpha, 127 all-beta, 48 mixed α+β, 148 zinc-fingers. 275 domains from disease genes; 108 contain annotated pathogenic variants.
- **Assay quality.** Replicate Pearson **r ≈ 0.85** (median). Correlates with in vitro folding ΔΔG (median Spearman **ρ = 0.73**, n=10 domains) and with high-throughput proteolysis stability (median **ρ = 0.65**, n=13). Core mutations more damaging than surface; **proline substitutions most destabilizing** overall.
- **Stability is a major but variable driver of pathogenicity (headline result).** **380/621 pathogenic variants (61%) detectably destabilize**; 303/621 (48%) strongly destabilize — vs 40% / 16% of 322 benign variants. Strongly family-dependent: β/γ-crystallins (cataract) almost all destabilizing (13/18, OR 11.98 vs benign); DNA-binding folds much less so (homeodomains OR 3.94; HMG-box OR 2.10; CUT OR 1.65, n.s.) — implying non-stability mechanisms (loss of DNA binding, gain-of-function).
- **Dominant vs recessive split.** Stability explains a median **44% of fitness variance in recessive-disease proteins vs 26% in dominant** (P = 1.1×10⁻³). Loss-of-function and aggregation diseases better explained by destabilization than "altered-function" (gain-of-function / dominant-negative) diseases. Per-domain examples: FHL1 LIM2 (reducing-body myopathy, MCC=1), TP63 SAM (ectodermal dysplasia, MCC=0.83) stability-driven; MECP2 MBD (Rett, MCC=0.4) and CRX homeodomain (retinal dystrophy, MCC=0.52) not — pathogenic variants cluster in DNA-binding interfaces / 2nd-shell / charged surfaces instead.
- **VEP benchmarking.** Best general predictors of measured stability: protein language model **ESM1v (median ρ=0.48)** and **EVE (ρ=0.48)**; best dedicated stability predictor **ThermoMPNN (ρ=0.50; ρ=0.57 excluding zinc-fingers**, robust even on domains non-homologous to its Megascale training set). All stability predictors fail on metal-dependent zinc-fingers.
- **Functional-site discovery.** aPCA abundance vs ESM1v evolutionary fitness modelled with sigmoids; residuals flag function-not-stability effects. **102,231 mutations (24%)** have larger fitness effects than stability accounts for, enriched in CDD functional sites (OR 2.72). Defines **5,231 evolutionary functional sites in 426 domains**, strongly enriched in annotated sites (OR 4.50) and recovering DNA/RNA/protein interfaces; **1,942 sites in 180 domains have no prior CDD annotation** (many "second-shell", median 3.62 Å from annotated sites).
- **Mutational effects conserved across homologues → family energy models.** A **Boltzmann/thermodynamic additive-ΔΔG model** fit per family predicts mutational effects across homologues well (homeodomains: Pearson **r=0.78** by 10-fold CV; n=36). Across **26 families with ≥5 homologues: median r=0.80** (held-out variants), **median r=0.66** on left-out homologues — beating ThermoMPNN. Epistasis is small but real (decays with sequence divergence): 25,410 epistatic variants identified, enriched in buried cores (OR 2.71), depleted at surfaces.
- **Proteome-wide extrapolation.** Energy models predict **4,107,436 additional variants in 7,271 domains**, including **13,878 clinical variants (1,310 pathogenic, 951 benign, 11,617 VUS)**. **52% of these predicted-pathogenic variants reduce stability** (34% strongly), mirroring the experimental rate.

## Methods

- **Library construction:** **microchip-based massive parallel synthesis (mMPS)** of site-saturation oligos; pooled cloning + yeast transformation of structurally diverse small domains (median ~100 aa; chosen for independent folding).
- **Abundance readout (aPCA):** abundance protein-fragment complementation assay — each domain expressed as a fusion to a **DHFR fragment**; cellular concentration of the reporter linearly sets growth rate over ≥3 orders of magnitude, so **variant abundance/stability ⇒ growth**. Input-vs-output variant frequencies by high-throughput sequencing give a fitness score. 27 experiments (3 biological replicates × 9 sub-libraries).
- **Predictor / annotation pipeline:** ESM1v, EVE, AlphaMissense, Tranception, PopEVE (general VEPs) and FoldX, DDMut, RaSP, ThermoMPNN (stability) benchmarked vs aPCA. Functional sites from sigmoidal aPCA-vs-ESM1v residuals (z-test FDR<0.1); CDD annotations + AlphaFold2 structures for spatial analysis.
- **Family energy models:** thermodynamic two-state (Boltzmann partition-function) model fit with MoCHI to all variants of a family; infers homologue-averaged ΔΔG; evaluated by 10-fold CV and leave-one-homologue-out; compared with in vitro proteolysis scans.
- **Data:** sequencing in GEO **GSE265942**; aPCA measurements in Supplementary Table 2; code at github.com/lehner-lab/domainome (Zenodo 10.5281/zenodo.11043642). Benchmarks the dataset against all human-missense abundance (VAMP-seq, aPCA) data in **MaveDB** (Esposito et al.) — i.e. it is positioned as a **MaveDB-style multiplexed-assay-of-variant-effects (MAVE) reference resource**.

## Relevance to the brain-organoid ASD review

- **Scales variant-effect mapping from one gene to hundreds — the trajectory the review wants for ASD genes.** Where SGE papers ([Sahu BRCA2](Sahu_2025_Saturation_genome_editing_based_clinical_classification_BRCA2.md), Findlay BRCA1) deeply map a single locus, this provides a **proteome-spanning, standardized MAVE reference** (563,534 variants / 522 domains) plus an explicit recipe to extend it proteome-wide via family energy models. That breadth is the model for a "**MaveDB-style**" atlas the review envisions feeding organoid-based ASD variant interpretation.
- **Directly relevant ASD/NDD gene domains are in the dataset or its extrapolation:** **MECP2 MBD (Rett syndrome)** and **CRX/PROP1/SOX11 DNA-binding domains** are highlighted — and crucially these are the cases where **stability is NOT the mechanism** (variants disrupt DNA binding / are gain-of-function). This is a direct caution that **abundance alone under-classifies neurodevelopmental transcription-factor variants**, motivating the review's argument for *cellular/organoid* phenotypes beyond protein stability.
- **Quantifies the dominant-disease gap.** Many ASD genes act via haploinsufficiency / dominant-negative / gain-of-function; this paper shows stability explains only ~26% of fitness variance in dominant disorders vs 44% in recessive — i.e. for the dominant-acting ASD architecture, a stability MAVE is necessary but insufficient, and **functional-site / activity readouts (organoid endophenotypes) are required**.
- **Supplies reference data and benchmarks for the computational layer** (ESM1v, EVE, AlphaMissense, ThermoMPNN) that any organoid variant-effect program will need to calibrate against; demonstrates VEPs are decent for stability but do not capture function-specific or gain-of-function effects.
- **Methodological complement** to the base-resolution SGE template (Sahu/Findlay) and the dosage/architecture clinical genetics of [Brunetti-Pierri 2008](BrunettiPierri_2008_Recurrent_reciprocal_1q21_1_deletions_duplications_associated.md): together they cover dosage → single-gene saturation → proteome-scale domain saturation.

## Open questions / limitations

- **Isolated domains, not full-length proteins.** Domains assayed out of native context (median ~100 aa); how far mutational effects transfer to full-length proteins is an explicit open question — especially relevant for large multidomain ASD proteins.
- **Stability-only readout.** aPCA measures abundance, so it **misses function-specific, interaction and gain-of-function effects** and consequently classifies clinical variants worse than general VEPs overall; non-stability mechanisms (DNA-binding TFs) are systematically under-detected.
- **Coverage still small.** Only ~1–2% of the human proteome's domains/families; many designed domains gave insufficient aPCA signal (low stability/solubility) or non-two-state behaviour and were filtered out. Zinc-fingers and metal-dependent folds poorly handled by stability predictors.
- **Energy-model assumptions.** Additive ΔΔG works well but ignores epistasis that grows with divergence (25,410 epistatic variants found in cores); proteome-wide predictions inherit this and, like the experimental data, are weaker for non-stability-driven pathogenicity.
- **No insertions/deletions, no transmembrane/extracellular proteins**; extension to these and to additional molecular traits (binding, localization, aggregation, allostery) left for future work.
- **Clinical-annotation imbalance.** Pathogenic variants concentrated in few domains (75% in 25% of domains; 41 domains have a single pathogenic variant), limiting per-domain classification confidence.

## Related pages

- [Sahu 2025 — Saturation genome editing-based clinical classification of BRCA2 variants](Sahu_2025_Saturation_genome_editing_based_clinical_classification_BRCA2.md)
- [Findlay 2018 — Accurate classification of BRCA1 variants with saturation genome editing](Findlay_2018_Accurate_classification_BRCA1_variants_saturation_genome_editing.md)
- [Frazer 2021 — Disease variant prediction with deep generative models of evolutionary data (EVE)](Frazer_2021_Disease_variant_prediction_deep_generative_models_evolutionary.md)
- [Cheng 2023 — Accurate proteome-wide missense variant effect prediction with AlphaMissense](Cheng_2023_Accurate_proteome_wide_missense_variant_effect_prediction.md)
- [Brunetti-Pierri 2008 — Recurrent reciprocal 1q21.1 deletions and duplications](BrunettiPierri_2008_Recurrent_reciprocal_1q21_1_deletions_duplications_associated.md)
