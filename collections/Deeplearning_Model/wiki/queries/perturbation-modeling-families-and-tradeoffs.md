# What perturbation modeling families are emerging in this collection, and what tradeoffs do they claim?

## Short Answer

- At least six perturbation-modeling families are visible in this collection.
- They differ less by headline accuracy alone than by what structure they assume about perturbation effects: transport geometry, biological graphs, diffusion trajectories, sparse probabilistic gene effects, perturbation-rich pretraining, or atlas-scale causal infrastructure.
- No single family dominates every use case in the current knowledge base.

## 1. Transport-Map Models

- [CellOT](../entities/CellOT.md) represents the transport-map family through [Neural Optimal Transport](../concepts/neural-optimal-transport.md).
- Its core assumption is that perturbation response can be modeled as moving mass from a control distribution to a treated distribution with minimal effort.
- Strength: it works with unpaired measurements and emphasizes preserving heterogeneous response structure rather than only mean shifts.
- Tradeoff: it becomes weaker when perturbations are very strong, when developmental gaps are long, or when the training data do not contain responses similar to the new case.

## 2. Graph-Guided Combinatorial Extrapolation

- [GEARS](../entities/GEARS.md) represents the graph-guided family through [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md).
- Its core assumption is that prior biological structure, especially coexpression and ontology-derived gene relationships, can make unseen single-gene and multigene perturbations predictable.
- Strength: it is especially aimed at the hard combinatorial regime where some perturbed genes were never seen during training.
- Tradeoff: the same graph priors that enable extrapolation can become failure points when poorly connected genes or mismatched biological graphs are involved.

## 3. Diffusion-Based State Generators

- [Squidiff](../entities/Squidiff.md) represents the diffusion family through [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md).
- Its core assumption is that perturbation and developmental responses can be generated as smooth denoising trajectories through a semantic latent space.
- Strength: the framework can handle transient intermediate states, differentiation, drug response, and injury-response modeling in one generative language.
- Tradeoff: training is slower and more expensive than lighter methods, and transfer to completely unseen perturbagens still benefits from extra molecular adaptors.

## 4. Sparse Probabilistic Gene-Effect Models

- [GPerturb](../entities/GPerturb.md) is the clearest example of a non-foundation, directly interpretable perturbation family.
- Its core assumption is that observed expression can be decomposed into basal state plus sparse additive perturbation effects modeled with Gaussian processes.
- Strength: it exposes gene-level effect presence, dosage sensitivity, and uncertainty more directly than many deep latent models.
- Tradeoff: it is less naturally positioned as a reusable broad foundation representation, and the source itself warns that inference can shift materially with observation-model choices.

## 5. Perturbation-Rich Foundation Pretraining

- [Tahoe-x1](../entities/Tahoe-x1.md) represents the perturbation-pretrained foundation-model family through [Perturbation-Trained Foundation Models](../concepts/perturbation-trained-foundation-models.md).
- Its core assumption is that perturbation exposure during pretraining changes what the representation can generalize about biological intervention.
- Strength: it argues that observational atlas scale alone is not enough and that interventional coverage is itself a scaling ingredient.
- Tradeoff: the approach is data- and compute-intensive, and some downstream perturbation predictions still rely on additional transition modules instead of one self-sufficient model.

## 6. Atlas and Infrastructure Roadmaps

- [Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas](../sources/rood_2024_toward_a_foundation_model_of.md) and [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md) represent an infrastructure family rather than a finished predictor.
- The core assumption is that exhaustive combinatorial measurement is impossible, so perturbation modeling must be coupled to atlas construction, compressed screening, and active-learning loops.
- Strength: this family explains why the other model families matter as parts of a larger causal modeling program rather than as isolated benchmarks.
- Tradeoff: it is still mostly a roadmap in this collection, not a deployed atlas with standardized quantitative comparisons.

## Cross-Family Pattern

- The major split in this collection is between methods that assume a structured transition geometry and methods that assume a strong external prior.
- CellOT and Squidiff emphasize transition geometry, but CellOT uses transport while Squidiff uses denoising generation.
- GEARS and GPerturb emphasize explicit prior structure, but GEARS relies on graphs whereas GPerturb relies on sparse probabilistic effect decomposition.
- Tahoe-x1 moves the problem upstream by changing the pretraining corpus rather than only the prediction head.
- The Perturbation Cell Atlas view sits above all of them and asks how these pieces could become components of a larger causal infrastructure.

## Practical Reading Of The Tradeoffs

- If the main challenge is unpaired control-versus-treated alignment, the current knowledge base most strongly points to [CellOT](../entities/CellOT.md).
- If the hardest problem is unseen multigene combinations, the strongest direct answer in the current collection is [GEARS](../entities/GEARS.md).
- If transient or multi-stimulus intermediate states matter most, [Squidiff](../entities/Squidiff.md) is the most explicit fit.
- If interpretability at the gene-effect level matters more than broad representation reuse, [GPerturb](../entities/GPerturb.md) looks strongest.
- If the central bottleneck is insufficient perturbation exposure during pretraining, [Tahoe-x1](../entities/Tahoe-x1.md) is the clearest argument.

## Bottom Line

- This collection does not yet support the claim that one perturbation family wins universally.
- It does support a more specific conclusion: perturbation modeling here is fragmenting into complementary families with different inductive biases, and the most important comparison axis is the biological problem each family is designed to solve.

## Pages Used

- [Learning single-cell perturbation responses using neural optimal transport](../sources/bunne_2023_learning_single-cell_perturbation_responses_using.md)
- [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](../sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md)
- [Squidiff: predicting cellular development and responses to perturbations using a diffusion model](../sources/he_2025_squidiff_predicting_cellular_development_and.md)
- [GPerturb: Gaussian process modelling of single-cell perturbation data](../sources/xing_2025_gperturb_gaussian_process_modelling_of.md)
- [Tahoe-x1: Scaling Perturbation-Trained Single-Cell Foundation Models to 3 Billion Parameters](../sources/gandhi_2025_tahoe-x1_scaling_perturbation-trained_single-cell_foundation.md)
- [Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas](../sources/rood_2024_toward_a_foundation_model_of.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md)
- [Perturbation-Trained Foundation Models](../concepts/perturbation-trained-foundation-models.md)
- [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md)
