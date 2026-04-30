# Predictive Models, Reference Substrates, and Roadmaps in Deeplearning_Model

## Claim

- This collection no longer behaves like a single leaderboard of biological foundation models.
- It now contains at least four distinct paper roles: direct predictive systems, reference substrates, roadmap or infrastructure papers, and heterogeneity anchors.
- Comparing all of them with one benchmark lens would flatten important differences in what each source is trying to contribute.

## 1. Direct Predictive Systems

- These papers build a model that directly predicts, retrieves, generates, or embeds biological states.
- Representative examples include [SAVE](../entities/SAVE.md), [scGPT](../entities/scGPT.md), [scFoundation](../entities/scFoundation.md), [SCimilarity](../entities/SCimilarity.md), [C2S-Scale](../entities/C2S-Scale.md), [CellOT](../entities/CellOT.md), [Cell2fate](../entities/Cell2fate.md), [GEARS](../entities/GEARS.md), [GPerturb](../entities/GPerturb.md), [Squidiff](../entities/Squidiff.md), [Tahoe-x1](../entities/Tahoe-x1.md), [Orthrus](../entities/Orthrus.md), and [scRL](../entities/scRL.md).
- Their main evaluation logic is direct performance on held-out tasks such as annotation, retrieval, perturbation prediction, transition reconstruction, developmental inference, or transfer learning.
- Even inside this subset, the collection already shows multiple distinct modeling families rather than one dominant recipe.

## 2. Reference Substrates

- Some sources matter mainly because they create a reusable reference landscape rather than because they ship a new predictive model.
- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md) and [HNOCA](../entities/HNOCA.md) provide a queryable fidelity benchmark and projection substrate.
- [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md) contributes a developmental multi-omics scaffold that supports lineage reconstruction, spatial localization, and in silico disease-oriented reasoning.
- [Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus](../sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md) adds a developmental atlas for region-specific maturation logic.
- These sources are not secondary just because they are not predictors. In this collection, they act as evaluation targets, supervision substrates, or biological structure references that future models could train against or be judged against.

## 3. Roadmap and Infrastructure Papers

- Another subset does not primarily answer one benchmark task but instead defines what future systems should be able to do.
- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md) frames a multi-scale virtual-cell stack around [Universal Representation](../concepts/universal-representation.md) and [Virtual Instruments](../concepts/virtual-instruments.md).
- [Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas](../sources/rood_2024_toward_a_foundation_model_of.md) reframes perturbation modeling as an atlas-building program tied to [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md).
- [Towards multimodal foundation models in molecular cell biology](../sources/cui_2025_towards_multimodal_foundation_models_in.md) and [Multimodal foundation transformer models for multiscale genomics](../sources/khan_2025_multimodal_foundation_transformer_models_for.md) define broader architectural language for [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md) and [Super Transformer Architecture](../concepts/super-transformer-architecture.md).
- [Reinforcement Learning and Its Clinical Applications Within Healthcare: A Systematic Review of Precision Medicine and Dynamic Treatment Regimes](../sources/frommeyer_2025_reinforcement_learning_and_its_clinical.md) serves a similar role on the clinical side by identifying what translation constraints matter once models leave the cell-state setting.

## 4. Heterogeneity Anchors

- A small but important subset functions as a benchmark for biological variation that future models may need to preserve rather than smooth away.
- [Transcriptomic sex differences in postmortem brain samples from patients with psychiatric disorders](../sources/xia_2024_transcriptomic_sex_differences_in_postmortem.md) is the clearest case: it argues for [Sex-Stratified Transcriptomic Burden](../concepts/sex-stratified-transcriptomic-burden.md) as a meaningful disease axis.
- These papers are not primarily about architecture or atlas infrastructure, but they change what should count as a faithful prediction target.

## What This Means For The Collection

- The collection should not be organized as if every source were competing on the same axis.
- Predictive systems should usually be compared by task family and inductive bias.
- Reference substrates should be compared by coverage, queryability, and suitability as evaluation or supervision scaffolds.
- Roadmap papers should be compared by what data, architecture, and benchmarking assumptions they make explicit.
- Heterogeneity anchors should be treated as constraints on what future models ought not erase.

## Practical Consequence

- A future model can look weak if judged only by one-task benchmark scores while still being central to the collection because it defines an evaluation substrate or a scaling roadmap.
- Conversely, a strong predictor may still be narrow if it does not connect to atlas resources, multimodal integration, or heterogeneity-aware evaluation.
- The most valuable next syntheses are therefore probably not "best model" rankings but cross-role comparisons such as substrate versus predictor or roadmap versus implementation.

## Sources Used

- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
- [Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas](../sources/rood_2024_toward_a_foundation_model_of.md)
- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
- [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md)
- [Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus](../sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md)
- [Reinforcement Learning and Its Clinical Applications Within Healthcare: A Systematic Review of Precision Medicine and Dynamic Treatment Regimes](../sources/frommeyer_2025_reinforcement_learning_and_its_clinical.md)
- [Transcriptomic sex differences in postmortem brain samples from patients with psychiatric disorders](../sources/xia_2024_transcriptomic_sex_differences_in_postmortem.md)
- [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md)
- [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md)
- [Clinical Reinforcement-Learning Translation](../concepts/clinical-reinforcement-learning-translation.md)
- [Sex-Stratified Transcriptomic Burden](../concepts/sex-stratified-transcriptomic-burden.md)
