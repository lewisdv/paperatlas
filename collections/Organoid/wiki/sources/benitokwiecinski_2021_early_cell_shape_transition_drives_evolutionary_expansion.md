---
title: "An early cell shape transition drives evolutionary expansion of the human forebrain."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.cell.2021.02.050
pmid: 33765444
authors: Benito-Kwiecinski S et al.
journal: Cell (2021)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# An early cell shape transition drives evolutionary expansion of the human forebrain.

## Source

- Authors: Benito-Kwiecinski S, Giandomenico SL (co-first), Sutcliffe M, Riis ES, Freire-Pritchett P, Kelava I, Wunderlich S, Martin U, Wray GA, McDole K, Lancaster MA (corresponding, lead contact).
- Journal: Cell (2021) 184, 2084–2102, April 15 2021 (open access, CC BY). Received 6 Jul 2020; accepted 22 Feb 2021; published online 24 Mar 2021.
- DOI: [10.1016/j.cell.2021.02.050](https://doi.org/10.1016/j.cell.2021.02.050)
- PMID: [33765444](https://pubmed.ncbi.nlm.nih.gov/33765444/)
- Lab: Madeline A. Lancaster, MRC Laboratory of Molecular Biology, Cambridge.
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

The human brain has undergone rapid expansion since humans diverged from other great apes, but the mechanism of this human-specific enlargement is still unknown. Here, we use cerebral organoids derived from human, gorilla, and chimpanzee cells to study developmental mechanisms driving evolutionary brain expansion. We find that neuroepithelial differentiation is a protracted process in apes, involving a previously unrecognized transition state characterized by a change in cell shape. Furthermore, we show that human organoids are larger due to a delay in this transition, associated with differences in interkinetic nuclear migration and cell cycle length. Comparative RNA sequencing (RNA-seq) reveals differences in expression dynamics of cell morphogenesis factors, including ZEB2, a known epithelial-mesenchymal transition regulator. We show that ZEB2 promotes neuroepithelial transition, and its manipulation and downstream signaling leads to acquisition of nonhuman ape architecture in the human context and vice versa, establishing an important role for neuroepithelial cell shape in human brain expansion.

## Key findings

Central thesis: the neuroepithelial (NE) → radial glia (RG) switch is **not instantaneous** (as in mouse, ~hours) but a **gradual, multi-day transition through a newly named "transitioning NE" (tNE) morphotype defined by apical constriction / cell-shape change that precedes change in cell identity and neurogenesis**. **Humans delay this transition relative to gorilla and chimpanzee**, keeping progenitors longer in the proliferative columnar NE state and (combined with a shorter cell cycle) expanding the founder progenitor pool → larger forebrain. Comparison spans **human, gorilla, AND chimpanzee** (including a new gorilla line), using one identical protocol to attribute differences to species, not method.

- **Human organoids are larger BEFORE neurogenesis.** At day 10 (pre-neurogenesis), mean neural-tissue area: H9 = 168,327 µm² vs gorilla G1 = 84,876 µm² vs chimp = 81,086 µm² (~2-fold). Mean NE-bud perimeter: 322 (H9) vs 237 (G1) vs 204 µm (chimp). Day-5 apical lumens are larger in human: mean luminal surface area 51,243 (H9) vs 15,437 (G1) vs 19,632 µm² (chimp). Difference is **not** explained by faster ape neurogenesis — TBR2⁺ intermediate progenitors and DCX⁺ neurons are absent at day 5 in human and gorilla, appearing only ~days 10–15.
- **The cell-shape transition (tNE) is delayed in human.** At day 5 (when tissue differences first appear) human NE cells are still wide/columnar while gorilla and chimp cells show constricted apical processes. Mean apical surface area per cell at day 5: H9 = 9.39, IMR-90 = 8.53 µm² (human) vs G1 = 4.48, G2 = 4.54, chimp = 3.55 µm² (~2-fold smaller in apes; *p* < 0.0001). Apical surface shrinks ~**7-fold from day 3 to day 10 in both species**, but human at day 8 ≈ gorilla at day 5 (a ~3-day lag). Apical process volume:surface ratio drops in gorilla by day 5 (0.76 vs human 1.23) but not in human until later (human catches up by day 10: ~0.66 both).
- **Cell-cycle and interkinetic nuclear migration (INM) differences.** Human NE nuclei sit more apically at day 5 (mean nuclear position 59.3% vs gorilla 67.1% of apicobasal thickness; *p* < 0.0001), indicating different INM. Live light-sheet (SiMView) imaging: **human NE cell cycle is shorter — mean 18.83 h (human H9) vs 22.10 h (gorilla G1)** (~3 h shorter; *p* < 0.0001). Mathematical growth-curve modeling predicts this 3-h difference alone yields a **~1.9-fold increase in both progenitor and neuron numbers** in human.
- **Comparative bulk RNA-seq (human H9 vs gorilla G1).** 42 samples / ~9,000 organoids, 7 time points day 0→day 25, 3 biological replicates each. Samples cluster by **time point, not species**, confirming highly comparable trajectories; cross-species Pearson correlation is **lowest exactly at days 5 and 10** (r = 0.52 and 0.40 vs ~0.63–0.66 elsewhere) — the window of the cell-shape transition. TCseq temporal clustering (2,905 → 2,342 robust genes per species, 10 clusters) found "cell morphogenesis"/"cellular component morphogenesis" GO terms shifted to **earlier-rising clusters in gorilla than human**, matching the faster ape shape change; "cell cycle" terms also decline earlier in gorilla (fits the cell-cycle data). Day-25 synaptic-maturation genes rise faster in gorilla (consistent with slower human neuronal maturation, cf. Schörnig 2021, Kanton 2019).
- **Candidate effectors identified:** SHROOM3 (actin-mediated apical constriction) — RNA and protein rise apically earlier in gorilla (strong apical SHROOM3 at day 5 in gorilla, minimal in human; both strong by day 10); phalloidin shows earlier apical actin in gorilla. OCLN (tight junction) redistributes apically later in human. A "partial-EMT" gene signature rises earlier in gorilla. Of 8 cell-morphogenesis transcription factors with species-specific dynamics, **ZEB2** (EMT master regulator, SMAD-interacting protein SIP1; flagged by human accelerated regions / selection) stood out — **ZEB2 mRNA peaks day 5 in gorilla vs day 10 in human**; protein onset earlier in gorilla, with earlier CDH1/EpCAM down and Vimentin up.
- **ZEB2 is functionally a driver of the NE→RG transition (loss-of-function).** Only **heterozygous** ZEB2 KO hESCs were recoverable (homozygous loss may be incompatible with pluripotency/survival; heterozygous LOF = Mowat-Wilson syndrome, which features ventriculomegaly). **ZEB2⁺/⁻ organoids show enlarged, extended, thinner NE buds** (larger perimeter, reduced thickness; *p* = 0.0001 and *p* < 0.0001), retained apicobasal OCLN, increased CDH1/OCLN + decreased CDH2 on western blot, and delayed neurogenesis (fewer early TBR2⁺ cells, normalizing later) — i.e. a **delayed transition / expanded neuroepithelium**, phenocopying the human-like direction. Doxycycline-inducible ZEB2 re-expression in ZEB2⁺/⁻ cells **rescued** bud size and TBR2⁺ numbers, confirming specificity.
- **Bidirectional interspecies phenocopy (the key causal result).**
  - *Human → ape:* premature ZEB2 induction in otherwise-WT human organoids (HumiZEB2 + Dox) produced **gorilla-like** smaller/rounder NE buds by day 5, earlier apical SHROOM3, and apical constriction quantitatively matching gorilla (apical surface 3.08 µm² induced vs 9.62 µm² uninduced vs ~4.50 µm² gorilla; day-10 organoid area 132,325 induced vs 201,434 uninduced vs 93,447 µm² gorilla). Later neurogenesis was normal — timing changed, not fate.
  - *Ape → human:* manipulating ZEB2 downstream signaling pushed gorilla toward human-like architecture. SMAD inhibition rescued ZEB2⁺/⁻ junctional/architecture effects (implicating SMAD signaling). **BMP4** (activates BMP-responsive SMADs, inhibits EMT) on gorilla organoids dilated apical processes and enlarged apical contacts (2.72 → 4.13 µm²). **LPA** (lysophosphatidic acid, enlarges NE apical contacts) on gorilla restored human-like enlarged apical surfaces (2.44 → 4.73 µm²) and extended apicobasal OCLN.
- **Model (Fig. 7N):** ZEB2, acting through BMP-responsive SMADs, downregulates epithelial/tight-junction features and drives actin-based apical constriction to convert NE → tNE → RG; a **delayed onset of ZEB2 in human** prolongs the proliferative NE stage and, with a shorter cell cycle, expands the human forebrain in the **tangential** dimension (matching comparative neuroanatomy: humans enlarge overall rather than thickening specific cortical layers).

## Methods

- **Models:** cerebral/telencephalic organoids from human (H9, IMR-90), gorilla (G1, G2 — new line), and chimpanzee cells, all on one optimized identical protocol (chimp EB stage 2 days shorter to match identity; all post-germ-layer steps identical).
- **Imaging/quantification:** whole-mount immunofluorescence (ZO1, SOX2, SHROOM3, OCLN, ZEB2, BLBP/GLAST, TBR2, DCX, CDH1/2, EpCAM, VIM, EMX1); sparse viral GFP labeling + 3D cell segmentation (MATLAB) for apical surface area / process volume; live **SiMView adaptive light-sheet** microscopy for cell-cycle length and INM; nuclear-position quantification.
- **Transcriptomics:** bulk RNA-seq (42 samples, ~9,000 organoids, day 0–25, 3 reps × 7 time points, human vs gorilla); orthology-filtered TPMs, Z-scaling across time; PCA, hierarchical clustering, Pearson correlation; TCseq temporal clustering + GO enrichment.
- **Functional genetics/pharmacology:** CRISPR ZEB2 heterozygous-LOF hESCs; doxycycline-inducible ZEB2-GFP (rescue in KO; over-expression in WT human = HumiZEB2); SMAD inhibitors; BMP4; LPA. Western blots for ZEB2 and junction proteins.
- **Statistics:** Kruskal-Wallis + Dunn's, one-way ANOVA + Tukey's, Mann–Whitney U, Student's *t*-test (all two-tailed); detailed *n* (cells/organoids/batches) reported per panel above.

## Relevance to the brain-organoid ASD review

Supports the review theme **"cell-shape transition driving human forebrain expansion" / human-specific developmental timing**. For "Programmable Brain Organoids for Proactive Autism Genetics":

- Identifies a **discrete, manipulable human-specific developmental parameter** — the timing of the NE→tNE→RG cell-shape transition — and shows it is **causally controllable** (ZEB2 / SMAD / BMP4 / LPA) to convert human↔ape forebrain architecture. This is a strong demonstration that **programmable organoids can causally test what makes human cortical development distinct**, exactly the review's "programmable organoid" premise.
- Demonstrates a complete **comparative-omics → candidate factor → bidirectional functional validation** pipeline in organoids (3 great-ape species, time-resolved RNA-seq, ZEB2 LOF + GOF + small-molecule manipulation) — a methodological model for proactively dissecting ASD-relevant developmental mechanisms rather than only cataloguing them.
- **Direct disease link:** ZEB2 heterozygous loss causes **Mowat-Wilson syndrome** (neurodevelopmental disorder, intellectual disability, frequently with autistic features and ventriculomegaly), and ZEB2 sits under human-accelerated-region selection. This connects an evolutionary brain-size mechanism to a Mendelian neurodevelopmental disorder — a template for how ASD-risk genes might act on early progenitor dynamics/brain size, upstream of the neuronal-maturation phenotypes.
- Together with [Schörnig 2021](schrnig_2021_comparison_induced_neurons_reveals_slower_structural_functional.md): this paper supplies the **early (progenitor-stage) heterochrony** and Schörnig the **late (neuronal-maturation) heterochrony** — the review can frame human-specific protracted development as acting at *both* ends. Complements [Esk 2020](esk_2020_human_tissue_screen_identifies_regulator_er_secretion.md) (same broad organoid-genetics toolkit, but cell-shape/expansion phenotype rather than a proliferation depletion screen).

## Open questions / limitations

- **Authors' stated limitation:** organoids are imperfect models of the in vivo brain; they call for in vivo validation (transgenic mice, non-invasive imaging of ape embryos). No in vivo confirmation here.
- Deepest cell-level and RNA-seq comparisons reduce to **one representative human (H9) vs one gorilla (G1) line**; chimpanzee included mainly for tissue/architecture measures. Cell-line / genetic-background effects cannot be fully excluded (the authors flag chimp EB-timing differences as possibly line- rather than species-driven).
- **Homozygous ZEB2 loss was not obtainable**, so ZEB2's full requirement is inferred from heterozygous LOF + inducible rescue/over-expression; dosage and pleiotropy (ZEB2 also acts in germ-layer specification, neural-tube morphogenesis, laminar fate) complicate clean interpretation.
- The **3-h cell-cycle difference → 1.9-fold neuron increase** is from a growth model, not a direct neuron count to adulthood; predicted, not measured at scale.
- Mechanism is a **"partial EMT" analogy**; precise molecular wiring (ZEB2 → SMAD → junctions/SHROOM3/actin) is supported by perturbations but not fully resolved. Whether the tNE state is evolutionarily conserved (a *Drosophila* parallel is noted) is speculative.
- Findings concern **forebrain size/architecture**, not directly autism phenotypes — relevance to the review is the human-specific *mechanism and programmability*, plus the ZEB2/Mowat-Wilson disease bridge.

## Related

- [Schörnig 2021](schrnig_2021_comparison_induced_neurons_reveals_slower_structural_functional.md) — companion human-specific timing paper at the neuronal-maturation stage (later in development).
- [Esk 2020](esk_2020_human_tissue_screen_identifies_regulator_er_secretion.md) — organoid functional-genetics toolkit (CRISPR-LICHT) for brain-size genes.
- Kanton et al. 2019 / Mora-Bermúdez et al. 2016 / Pollen et al. 2019 — great-ape organoid comparisons cited here for slower human neuronal maturation and RG behavior (not yet wiki pages).
- See collection [index](../index.md) for related human cortical-development sources (Pollen 2015 oRG identity, Camp 2015 organoid–fetal concordance, Quadrato 2017 organoid cell diversity).
