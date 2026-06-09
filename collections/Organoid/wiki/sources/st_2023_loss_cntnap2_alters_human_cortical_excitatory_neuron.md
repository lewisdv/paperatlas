---
title: "Loss of CNTNAP2 Alters Human Cortical Excitatory Neuron Differentiation and Neural Network Development."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.biopsych.2023.03.014
pmid: 37001843
authors: St George-Hyslop F et al.
journal: Biological psychiatry (2023)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/st_2023_loss_cntnap2_alters_human_cortical_excitatory_neuron.pdf
pdf_status: downloaded
---

# Loss of CNTNAP2 Alters Human Cortical Excitatory Neuron Differentiation and Neural Network Development.

## Source

- Authors: St George-Hyslop F, Haneklaus M, Kivisild T, Livesey FJ (UCL Great Ormond Street Institute of Child Health; corresponding: Frederick J. Livesey).
- Journal: Biological Psychiatry 2023;94(10):780–791 (Nov 15, 2023). Open access (CC BY).
- DOI: [10.1016/j.biopsych.2023.03.014](https://doi.org/10.1016/j.biopsych.2023.03.014)
- PMID: [37001843](https://pubmed.ncbi.nlm.nih.gov/37001843/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

**BACKGROUND:** Loss-of-function mutations in the contactin-associated protein-like 2 (CNTNAP2) gene are causal for neurodevelopmental disorders, including autism, schizophrenia, epilepsy, and intellectual disability. CNTNAP2 encodes CASPR2, a single-pass transmembrane protein that belongs to the neurexin family of cell adhesion molecules. These proteins have a variety of functions in developing neurons, including connecting presynaptic and postsynaptic neurons, and mediating signaling across the synapse.

**METHODS:** To study the effect of loss of CNTNAP2 function on human cerebral cortex development, and how this contributes to the pathogenesis of neurodevelopmental disorders, we generated human induced pluripotent stem cells from one neurotypical control donor null for full-length CNTNAP2, modeling cortical development from neurogenesis through to neural network formation in vitro.

**RESULTS:** CNTNAP2 is particularly highly expressed in the first two populations of early-born excitatory cortical neurons, and loss of CNTNAP2 shifted the relative proportions of these two neuronal types. Live imaging of excitatory neuronal growth showed that loss of CNTNAP2 reduced neurite branching and overall neuronal complexity. At the network level, developing cortical excitatory networks null for CNTNAP2 had complex changes in activity compared with isogenic controls: an initial period of relatively reduced activity compared with isogenic controls, followed by a lengthy period of hyperexcitability, and then a further switch to reduced activity.

**CONCLUSIONS:** Complete loss of CNTNAP2 contributes to the pathogenesis of neurodevelopmental disorders through complex changes in several aspects of human cerebral cortex excitatory neuron development that culminate in aberrant neural network formation and function.

## Key findings

- **Isogenic full-length-CNTNAP2-null human cortical model (not 3D organoid).** CRISPR–Cas9 inserted stop codons in **both alleles at exon 3** of CNTNAP2 in the neurotypical donor line **NDC1.2** (male, 86 yr), disrupting the canonical **full-length CNTNAP2-201** isoform (the isoform carrying most disease-associated mutations) while sparing the short CNTNAP2-203. iPSCs were differentiated as a 2D-style directed cortical excitatory differentiation (retinoid/dual-SMAD) that "replays" cortical neurogenesis → network formation; **no cortical interneurons are produced** in this system.
- **CNTNAP2 (long isoform) is expressed mainly in postmitotic excitatory neurons, rising over time.** Full-length CNTNAP2 mRNA undetectable in iPSCs, first appears at **D30** (progenitors), and rises significantly from **D50→D80** (qRT-PCR; ANOVA F₃,₂₄ = 167.9, P = 3.1 × 10⁻¹⁶). Protein follows the same trajectory. CNTNAP2 localizes to puncta on axons/dendrites/soma and co-localizes with pre- (SYP) and post-synaptic (PSD-95) markers by ~D75. In vivo (BrainSpan DLPFC) both isoforms appear by PCW 8 and rise to PCW 12 — concordant with the in-vitro timing.
- **LOF does not block cortical fate but shifts neuronal subtype proportions.** Nanostring cell-fate panel: null vs control cultures not significantly different in overall composition (P > .05). scRNA-seq (D50, 2 null + 2 control inductions, 11,941 cells; 7 cell types) showed **cortical neurons were the only cell type with significantly reduced CNTNAP2** and **the highest number of DEGs**. Within neurons, **CALB2 (calretinin) and NTS (neurotensin) up**, **LMO3, NEUROD2, CSRP2 down** in null cells.
- **The DEGs reflect a shift in mature neuron subtype ratios.** Subclustering neurons gave 4 maturity-ordered populations; the two terminal types — **CALB2⁺ "late 1"** and **LMO3⁺ "late 2"** — carry the up/down DEGs respectively. CNTNAP2-null cultures had **more CALB2⁺ late-1 and fewer LMO3⁺ late-2 neurons** (reproduced in 2 independent inductions; under-powered for formal significance on proportions). Cholesterol/fatty-acid synthesis genes (HMGCR, HMGCS1, SQLE, FDFT1, DHCR7) were down in null neurons. Interpreted as **overproduction of early CALB2⁺ pioneer-type neurons and underproduction of later LMO3⁺ (subplate-like) neurons** — i.e. a possible maturation delay/retention at the CALB2-high stage.
- **Reduced neurite branching / dendritic-arbor complexity, cell-autonomously.** Live single-neuron tracing (birth-dated D35, imaged ~D40–D66) of branch number, branch length, total length. CNTNAP2-null neurons had **significantly fewer branches per neuron** in both separate and mixed (1:1 coculture) cultures (mixed: ANOVA F₅,₁₇₅ = 14.54, P = 6.5 × 10⁻¹²; significant at D55/D60/D66). Branch *length* largely unchanged; total neuron length reduced in mixed cultures (D51/D55). Coculture with isogenic controls confirmed the branching deficit is **cell-autonomous** (and was clearer in coculture, controlling for microenvironment).
- **Triphasic network-activity abnormality.** Two orthogonal assays — calcium imaging (NeuroBurst Orange, D40→D105) and **multielectrode arrays (MEA, D35 onward)** — showed the same pattern: (1) an **early phase of reduced activity** vs isogenic controls (~D41–D60; fewer active objects, lower burst rate); (2) a **prolonged (>30 day) period of hyperexcitability** (from ~D60–D63; significantly more active objects, higher burst rate, more spikes/electrode); (3) a **late switch back to reduced activity**, dropping to/below control levels (~D70–D81 onward) as control activity kept rising. Two-way ANOVA: calcium active-objects F₃₉,₅₆₀ = 297.4, P < .0001; burst rate F₃₉,₅₆₀ = 68.21, P < .0001.
- **Convergence with prior human/mouse data.** The early-hyperactivity phase matches a previous human forebrain-network model from a *heterozygous* CNTNAP2 schizophrenia patient; the late reduced activity is consistent with the hypoactivity reported in postnatal *Cntnap2*-null mice. Authors cite a proposed mechanism (CNTNAP2 promotes neuronal calcium export → loss raises intracellular Ca²⁺ → hyperexcitability, possibly also suppressing neurite outgrowth) as a hypothesis to be tested.

## Methods

- **Genome engineering:** CRISPR–Cas9 (Bruntraeger-adapted), guide targeting CNTNAP2 exon 3 in NDC1.2; biallelic stop-codon insertion verified by MiSeq + Sanger; isoform-specific LOF of full-length CNTNAP2 confirmed at mRNA (exon 3–4 primers) and protein (Western) in D50 neurons.
- **Differentiation:** established Livesey-lab directed cortical excitatory differentiation (retinoid + dual-SMAD inhibition) generating progenitors → glutamatergic deep-layer cortical neurons in in-vivo-like temporal order; fate validated by Nanostring 150-gene brain-development code set. **Not a self-organizing 3D organoid**; no interneurons generated.
- **scRNA-seq:** 10x Genomics 3′ v2, D50, cell-hashing multiplex; Seurat v4 clustering; pseudobulk DESeq2 for DE; Monocle pseudotime for the progenitor→neuron trajectory (4,917 cortical cells of 11,941).
- **Neurite imaging:** sparse fluorescent nucleofection (Amaxa 4D) at D50, Opera Phenix confocal every 3–6 days to D61/D66; NeuronStudio reconstruction (branch number / branch length / total length); separate vs mixed-genotype coculture (with reporter swap).
- **Network activity:** calcium imaging on Incucyte S3 (lentiviral genetically-encoded Ca²⁺ indicator); **MEA on Maestro Pro** (Axis Navigator); longitudinal recording.
- **Replication caveat:** single donor background (NDC1.2); 2 null + 2 control inductions for most assays (MEA: 1 each).

## Relevance to the brain-organoid ASD review

- **Table-1 monogenic disease-model entry — CNTNAP2.** Serves as the CNTNAP2/CASPR2 exemplar for the review's monogenic ASD-model catalogue: a complete-LOF, **isogenic** human cortical model spanning neurogenesis → network formation, demonstrating that CNTNAP2-LOF pathology **begins early in development**.
- **Cell-adhesion/synapse axis complements the translational-regulation axis.** Where [Kang 2021](kang_2021_human_forebrain_organoid_model_fragile_x_syndrome.md) (FMR1) covers RNA-binding/translational dysregulation, this paper supplies a **neurexin-family cell-adhesion** mechanism, broadening the review's gene-mechanism coverage while landing on a **shared excitatory-hyperexcitability** phenotype.
- **Network-level functional readouts (MEA + calcium imaging).** The triphasic activity trajectory is a strong example of the review's "functional/network phenotyping in human models" theme and an argument for longitudinal electrophysiology — directly relevant given CNTNAP2's epilepsy association.
- **Subtype-specification phenotype.** The CALB2⁺-over / LMO3⁺-under shift in early-born excitatory neurons ties into the review's recurring "altered timing/proportions of neuron classes" convergence motif (cf. [Paulsen 2022](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md), [Villa 2022 CHD8](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md)).
- **Caveat the review should flag:** this is a **directed 2D-style cortical differentiation, not a self-organizing organoid**, and produces **no interneurons** — useful contrast for the review's discussion of model choice (guided neuron culture vs organoid vs assembloid for E/I-balance questions), and a motivation for CNTNAP2 work in assembloids ([Birey 2017](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md)).

## Open questions / limitations

- **Single genetic background, low replication.** All results from one donor (NDC1.2); 2 inductions/genotype (MEA n = 1/genotype). Authors explicitly call replication in additional donor lines a key next step.
- **Homozygous complete LOF models the most severe end.** Most patients are heterozygous missense/LOF; dosage-sensitivity (CNTNAP2 severity scales with allele dose) means the full-null phenotype may overstate heterozygous biology.
- **No interneurons / no 3D cytoarchitecture.** GABAergic contributions to E/I imbalance (robustly implicated for reduced CNTNAP2 dosage) cannot be assessed; a human CNTNAP2-null model with interneurons (or assembloid) is needed.
- **Under-powered for cell-proportion statistics** — the CALB2⁺/LMO3⁺ shift is reproducible but not formally significant; whether late-1 are precursors of late-2 (delay) vs an independent overproduction is unresolved.
- **Mechanism is hypothesis-level.** The calcium-export model for hyperexcitability (and its link to reduced branching) is proposed, not demonstrated here.
- **No rescue experiment.** Whether re-expressing CNTNAP2 reverses the phenotypes, and the developmental window for rescue, is flagged as important but untested.

## Related

- [Kang 2021 — Human forebrain organoid model of fragile X (FMR1)](kang_2021_human_forebrain_organoid_model_fragile_x_syndrome.md) — sibling Table-1 monogenic model; shared excitatory-hyperexcitability phenotype.
- [Hébert 2008 — Genetics of early telencephalon patterning](hbert_2008_genetics_early_telencephalon_patterning_some_assembly_required.md) — patterning/regionalization background for dorsal-cortical excitatory differentiation.
- [Mariani 2015 — FOXG1-dependent GABA/glutamate dysregulation in ASD](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md) — E/I-balance disease modeling in organoids.
- [Villa 2022 — CHD8 haploinsufficiency: transient excitatory/inhibitory trajectory alterations](villa_2022_chd8_haploinsufficiency_links_autism_transient_alterations_excitatory.md) — convergent altered-subtype-trajectory phenotype.
- [Paulsen 2022 — Autism genes converge on asynchronous development of shared neuron classes](paulsen_2022_autism_genes_converge_asynchronous_development_shared_neuron.md) — convergence framing for subtype-timing shifts.
- [Birey 2017 — Assembly of functionally integrated human forebrain spheroids](birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.md) — assembloid route for E/I and interneuron biology absent here.
- Entity: [MEA electrophysiology readouts](../entities/mea-electrophysiology-readouts.md)
- Entity: [Calcium imaging readouts](../entities/calcium-imaging-readouts.md)
