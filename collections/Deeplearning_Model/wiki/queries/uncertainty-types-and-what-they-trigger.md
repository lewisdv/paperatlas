# What different kinds of uncertainty are explicit in this collection, and what do they trigger?

## Short Answer

- Uncertainty in this collection is not one single warning light.
- It appears in at least five distinct forms:
- fallback-label uncertainty in annotation
- atlas-coverage uncertainty in retrieval
- reference-coverage uncertainty in benchmarking
- posterior dynamical uncertainty in trajectory inference
- gene-level perturbation-effect uncertainty in intervention modeling

## 1. Annotation Uncertainty Triggers A Broader Label

- [Uncertainty-aware single-cell annotation with a hierarchical reject option](../sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.md) makes the clearest label-level move.
- Through [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md), uncertainty triggers a fallback from a fine-grained leaf label to an internal hierarchy node rather than a forced wrong answer or a full abstention.
- This is the most direct `what label should we return under uncertainty?` answer in the collection.

## 2. Retrieval Uncertainty Triggers Confidence Downgrading

- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md) uses a different response.
- Through [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md), [SCimilarity](../entities/SCimilarity.md) keeps the retrieved state but attaches low representation confidence when the query lies in a weakly covered part of atlas space.
- The action here is not fallback labeling, but caution about how strongly the atlas supports the query.

## 3. Reference Uncertainty Triggers Coverage Diagnosis

- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md) and [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md) move uncertainty to the system level.
- The question becomes whether a whole organoid protocol or projected dataset is adequately covered by the relevant primary reference, or whether important states are missing, immature, or stress-shifted.
- The action here is diagnosis of biological mismatch and coverage gaps rather than a per-cell fallback or per-query confidence score.

## 4. Dynamical Uncertainty Triggers Quality Control On Trajectory Claims

- [Cell2fate infers RNA velocity modules to improve cell fate prediction](../sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md) makes uncertainty part of dynamical inference itself.
- Through [RNA Velocity Modules](../concepts/rna-velocity-modules.md) and [Cell2fate](../entities/Cell2fate.md), posterior uncertainty over cell-specific time is used as a quality-control signal for whether a dataset actually supports meaningful velocity structure.
- The action here is not label fallback or atlas warning, but restraint about whether temporal conclusions should be trusted at all.

## 5. Perturbation Uncertainty Triggers Caution On Effect Interpretation

- [GPerturb: Gaussian process modelling of single-cell perturbation data](../sources/xing_2025_gperturb_gaussian_process_modelling_of.md) and, in a weaker adjacent form, [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](../sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md), expose a different uncertainty mode.
- Through [Gene-Level Perturbation Uncertainty](../concepts/gene-level-perturbation-uncertainty.md), the main issue is whether a predicted perturbation effect is present, directional, and large enough to interpret robustly.
- The action here is caution about biological claims from perturbation predictions, especially when graph support is weak or when observation-model choice changes inferred effects.

## What The Collection Supports Right Now

- The collection clearly supports the claim that uncertainty is operationalized at several different biological levels.
- Some methods use it to soften labels.
- Some use it to weaken trust in retrieved neighbors.
- Some use it to diagnose missing reference coverage.
- Some use it to decide whether temporal inference is meaningful.
- Some use it to warn that predicted perturbation effects are model-sensitive or weakly supported.

## What The Collection Does Not Yet Support

- The current knowledge base does not support one unified uncertainty framework that spans annotation, retrieval, dynamics, and perturbation modeling.
- It also does not support treating all uncertainty scores as directly comparable, because they act on different objects and trigger different decisions.

## Bottom Line

- In this collection, uncertainty is action-specific.
- Sometimes it says `return a broader label`.
- Sometimes it says `keep the answer but lower confidence`.
- Sometimes it says `the reference space may not cover this system`.
- Sometimes it says `do not overtrust this trajectory`.
- Sometimes it says `do not overinterpret this perturbation effect`.

## Pages Used

- [Uncertainty-aware single-cell annotation with a hierarchical reject option](../sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.md)
- [A cell atlas foundation model for scalable search of similar human cells](../sources/heimberg_2025_a_cell_atlas_foundation_model.md)
- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
- [Cell2fate infers RNA velocity modules to improve cell fate prediction](../sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md)
- [GPerturb: Gaussian process modelling of single-cell perturbation data](../sources/xing_2025_gperturb_gaussian_process_modelling_of.md)
- [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](../sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md)
- [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)
- [Gene-Level Perturbation Uncertainty](../concepts/gene-level-perturbation-uncertainty.md)
- [SCimilarity](../entities/SCimilarity.md)
- [Cell2fate](../entities/Cell2fate.md)
- [GPerturb](../entities/GPerturb.md)
- [GEARS](../entities/GEARS.md)
