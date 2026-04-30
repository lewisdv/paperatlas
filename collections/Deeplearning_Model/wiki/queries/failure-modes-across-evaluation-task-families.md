# What does failure look like across the main evaluation task families in this collection?

## Short Answer

- This collection does not support one generic definition of model failure.
- Failure is task-family-specific.
- Retrieval and annotation fail by overclaiming outside reference coverage.
- Transfer-oriented foundation models fail when broad reuse claims outrun task-specific evidence or robust representation under shift.
- Perturbation models fail when impressive average prediction masks weak support for unseen, heterogeneous, or gene-level effects.
- Transition models fail when they match endpoints without supporting the underlying notion of movement, timing, or commitment.
- Multimodal systems fail when latent alignment or completion is mistaken for validated biological equivalence across modalities or scales.
- Reference substrates fail when the target space is incomplete, pooled too aggressively, or blind to key heterogeneity axes.
- Roadmap and translation papers fail when they describe an ambitious system without a workable validation, data, or deployment path.

## 1. Retrieval And Annotation Fail When Coverage Is Weak But The System Speaks As If It Were Strong

- [SCimilarity](../entities/SCimilarity.md), through [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md), is strongest when a query sits inside a well-covered atlas neighborhood.
- The failure mode is not mainly `bad generation`. It is misplaced confidence when the reference space does not adequately support the query.
- [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md) makes the paired lesson explicit: if uncertainty is real, forcing a fragile leaf label is itself a failure.
- In this family, the collection treats overconfident specificity under weak reference support as a more revealing failure than a simple drop in average accuracy.

## 2. Foundation-Transfer Systems Fail When Reuse Claims Outrun The Representational Evidence

- [scGPT](../entities/scGPT.md), [scFoundation](../entities/scFoundation.md), [C2S-Scale](../entities/C2S-Scale.md), [scELMo](../entities/scELMo.md), and [Orthrus](../entities/Orthrus.md) all promise reusable representations, but they do not share one reusable object.
- The collection's representation pages, including [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md), [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md), [Cell Sentences](../concepts/cell-sentences.md), [LLM-Derived Feature Embeddings](../concepts/llm-derived-feature-embeddings.md), and [Evolutionary Contrastive RNA Pretraining](../concepts/evolutionary-contrastive-rna-pretraining.md), show that these systems solve different transfer problems.
- Failure here happens when broad `foundation model` language hides that the pretrained object may be narrow, task-contingent, modality-specific, or sensitive to pretraining design and downstream adaptation.
- In the more language-native branch, the collection also makes space for a second failure mode: biologically fluent output that still needs guardrails because open-ended interpretation is broader than atlas-bounded retrieval.

## 3. Perturbation Prediction Fails When Average Agreement Hides Unsupported Effect Claims

- [CellOT](../entities/CellOT.md), [GEARS](../entities/GEARS.md), [GPerturb](../entities/GPerturb.md), [Squidiff](../entities/Squidiff.md), [Tahoe-x1](../entities/Tahoe-x1.md), [SAVE](../entities/SAVE.md), and [AURORA](../entities/AURORA.md) all participate in the intervention or conditional-response family, but with different assumptions.
- The collection's [Gene-Level Perturbation Uncertainty](../concepts/gene-level-perturbation-uncertainty.md) page is especially important here.
- A perturbation model can fail by looking good on pooled metrics while still giving weakly supported effect direction, missing unseen combinatorial structure, collapsing heterogeneous responses, or extrapolating poorly under strong condition shift.
- This is why the collection keeps transport, graph-guided, diffusion, sparse probabilistic, perturbation-pretrained, and multimodal health-response systems separate rather than collapsing them into one perturbation scoreboard.

## 4. Transition Models Fail When Endpoint Accuracy Replaces A Credible Transition Story

- [Cell2fate](../entities/Cell2fate.md), [scRL](../entities/scRL.md), [CellOT](../entities/CellOT.md), and [Squidiff](../entities/Squidiff.md) all model change, but they do not agree on what a change is.
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md) care about interpretable dynamics with posterior support.
- [Fate Decision Intensity](../concepts/fate-decision-intensity.md) cares about early commitment pressure.
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md) cares about believable source-to-target population movement.
- [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md) cares about realistic intermediate and condition-shifted paths.
- Failure in this family therefore means more than `wrong endpoint`. It can mean a transition explanation that is mechanically unconvincing, temporally unsupported, or too weakly grounded to justify the biological story attached to it.

## 5. Multimodal Systems Fail When Alignment Is Overread As Unification

- [AURORA](../entities/AURORA.md) is the clearest practical completion-oriented multimodal system in the collection.
- [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md) and [Super Transformer Architecture](../concepts/super-transformer-architecture.md) point to a broader architecture and pretraining agenda.
- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md) point to yet another multimodal role: a richer reference substrate rather than a deployed predictor.
- Failure here happens when these different meanings are treated as interchangeable.
- A model can complete a missing modality yet still fall short of a broad multimodal foundation model.
- A multimodal atlas can strengthen biological interpretation without proving that one shared latent space already captures all relevant modality-specific structure.
- A virtual-cell roadmap can be scientifically ambitious without yet validating cross-scale equivalence.

## 6. Reference Benchmarking Fails When The Target Space Is Too Thin Or Too Smoothed

- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md), [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md), [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md), and [Sex-Stratified Transcriptomic Burden](../concepts/sex-stratified-transcriptomic-burden.md) together make one point hard to ignore.
- A reference can fail not because it lacks a model, but because it defines the target space too narrowly.
- The collection supports at least four substrate-side failure modes:
- missing or immature primary-state coverage
- flattening region-specific developmental structure
- ignoring multimodal regulatory or spatial context
- averaging away subgroup-specific disease burden
- Once those axes are visible, later predictive systems can also fail simply by targeting the wrong or impoverished biological benchmark.

## 7. Roadmap And Translation Work Fail When Vision Outruns Validation Path

- [AIVC](../entities/AIVC.md), [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md), and [Clinical Reinforcement-Learning Translation](../concepts/clinical-reinforcement-learning-translation.md) show that not every important paper here is trying to win a current modeling benchmark.
- Their failure mode is different.
- A roadmap fails when it cannot specify the substrate, interfaces, validation loops, or deployment constraints that would make the vision testable.
- The clinical RL branch makes this especially concrete: reward misalignment, retrospective bias, reproducibility problems, interpretability demands, regulatory friction, and workflow mismatch are all supported failure modes in the current knowledge base.
- The virtual-cell and perturbation-atlas branches carry an adjacent risk: a compelling systems vision that remains too aspirational to compare with narrower but operational methods.

## Cross-Family Lesson

- The collection supports a strong negative conclusion: `failure` is not one scalar across these papers.
- A retrieval system can fail by overclaiming coverage.
- A foundation model can fail by overclaiming transfer.
- A perturbation model can fail by overclaiming causal or gene-level certainty.
- A transition model can fail by overclaiming the mechanism of change.
- A multimodal system can fail by overclaiming what alignment means.
- A reference substrate can fail by overclaiming what biology is covered.
- A roadmap can fail by overclaiming deployability or testability.

## Bottom Line

- The most useful evaluation question in this collection is not only `which paper performs best?`
- It is `what counts as failure for the kind of biological task this paper is trying to solve?`
- Once that question is asked first, the collection becomes much easier to compare honestly.

## Pages Used

- [Evaluation Task Families and Success Criteria in Deeplearning_Model](../syntheses/evaluation-task-families-and-success-criteria.md)
- [What different kinds of uncertainty are explicit in this collection, and what do they trigger?](uncertainty-types-and-what-they-trigger.md)
- [Which heterogeneity axes do the reference papers in this collection make hard to ignore?](which-heterogeneity-axes-do-the-reference-papers-make-hard-to-ignore.md)
- [How should this collection distinguish retrieval-first and generative-first single-cell models?](retrieval-first-vs-generative-first-single-cell-models.md)
- [How do transition-oriented models in this collection differ in what they think a cell-state transition is?](how-do-transition-oriented-models-differ-in-what-they-think-a-cell-state-transition-is.md)
- [What perturbation modeling families are emerging in this collection, and what tradeoffs do they claim?](perturbation-modeling-families-and-tradeoffs.md)
- [What does `multimodal` actually mean across this collection?](what-multimodal-means-across-the-collection.md)
- [How do virtual-cell roadmaps differ from multimodal foundation-model roadmaps in this collection?](virtual-cell-vs-multimodal-foundation-roadmaps.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
- [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md)
- [Single-Cell Generative Pretraining](../concepts/single-cell-generative-pretraining.md)
- [Read-Depth-Aware Pretraining](../concepts/read-depth-aware-pretraining.md)
- [Cell Sentences](../concepts/cell-sentences.md)
- [LLM-Derived Feature Embeddings](../concepts/llm-derived-feature-embeddings.md)
- [Evolutionary Contrastive RNA Pretraining](../concepts/evolutionary-contrastive-rna-pretraining.md)
- [Gene-Level Perturbation Uncertainty](../concepts/gene-level-perturbation-uncertainty.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)
- [Fate Decision Intensity](../concepts/fate-decision-intensity.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md)
- [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md)
- [Super Transformer Architecture](../concepts/super-transformer-architecture.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md)
- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md)
- [Sex-Stratified Transcriptomic Burden](../concepts/sex-stratified-transcriptomic-burden.md)
- [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md)
- [Clinical Reinforcement-Learning Translation](../concepts/clinical-reinforcement-learning-translation.md)
