# How do transition-oriented models in this collection differ in what they think a cell-state transition is?

## Short Answer

- The transition-oriented papers in this collection do not share one common definition of `cell-state transition`.
- They split into at least five views:
- a latent biophysical dynamic program inferred from spliced and unspliced counts
- an early decision landscape over a developmental manifold
- a transport map between source and target populations
- a generative path through semantic latent space under stimuli
- a direct prediction problem for unseen combinatorial perturbation endpoints

## 1. Cell2fate: Transition As Explicit Transcriptional Dynamics

- [Cell2fate infers RNA velocity modules to improve cell fate prediction](../sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md) treats transition as a dynamical process grounded in splicing kinetics.
- Through [RNA Velocity Modules](../concepts/rna-velocity-modules.md), the model decomposes transcription-rate changes into interpretable modules with switch times, ON/OFF behavior, and posterior uncertainty.
- This is the most explicitly mechanistic transition view in the current collection.

## 2. scRL: Transition As Early Decision Pressure

- [scRL: Utilizing Reinforcement Learning to Evaluate Fate Decisions in Single-Cell Data](../sources/fu_2025_scrl_utilizing_reinforcement_learning_to.md) treats transition less as kinetics and more as a sequential decision landscape.
- Through [Fate Decision Intensity](../concepts/fate-decision-intensity.md), the key question becomes where commitment pressure rises before overt lineage separation becomes obvious.
- In this view, transition is about identifying decision points and policy structure over a manifold, not about reconstructing the full biophysical state-update equation.

## 3. CellOT: Transition As Distribution Transport

- [Learning single-cell perturbation responses using neural optimal transport](../sources/bunne_2023_learning_single-cell_perturbation_responses_using.md) frames transition as a map from one population distribution to another.
- Through [Neural Optimal Transport](../concepts/neural-optimal-transport.md), the model asks how control mass should move into perturbed mass under a minimal-effort geometry.
- The emphasis is therefore on source-target alignment and heterogeneous response preservation, not on explicit intracellular dynamics over inferred time.

## 4. Squidiff: Transition As Generative Interpolation And Stimulus Response

- [Squidiff: predicting cellular development and responses to perturbations using a diffusion model](../sources/he_2025_squidiff_predicting_cellular_development_and.md) treats transition as a generative path through semantic latent space.
- Through [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md), trajectories can be interpolated, extrapolated, or shifted by perturbation vectors and then decoded into transcriptomes.
- This view is less tied to one explicit kinetic model and more focused on recovering smooth intermediate states and complex condition-dependent state changes.

## 5. GEARS: Transition As Endpoint Generalization Under Unseen Intervention Combinations

- [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](../sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md) takes a narrower but practically important position.
- Through [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md), transition becomes the problem of predicting the endpoint transcriptome for perturbation combinations that were not directly observed.
- This is not a continuous-time or trajectory-heavy notion of transition. It is closer to compositional intervention reasoning with strong graph priors.

## What The Collection Supports Right Now

- The collection clearly supports the claim that these models are not interchangeable even when all of them speak about cell-state change.
- Cell2fate is strongest on interpretable dynamical evidence and posterior uncertainty.
- scRL is strongest on early commitment localization.
- CellOT is strongest on unpaired source-target transport between populations.
- Squidiff is strongest on smooth generative state interpolation and broad stimulus-response simulation.
- GEARS is strongest on unseen multigene endpoint prediction with explicit combinatorial inductive bias.

## What The Collection Does Not Yet Support

- The current knowledge base does not support a single ranking that says one transition notion dominates all the others.
- It also does not support treating endpoint perturbation prediction, developmental decision scoring, RNA velocity inference, and generative interpolation as the same benchmark problem.

## Bottom Line

- In this collection, `cell-state transition` is a family of modeling targets rather than one task.
- Some papers try to infer why and when a state changes.
- Some try to map where a population will move.
- Some try to generate the intermediate path.
- Some try to predict the final perturbation endpoint.

## Pages Used

- [Cell2fate infers RNA velocity modules to improve cell fate prediction](../sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md)
- [scRL: Utilizing Reinforcement Learning to Evaluate Fate Decisions in Single-Cell Data](../sources/fu_2025_scrl_utilizing_reinforcement_learning_to.md)
- [Learning single-cell perturbation responses using neural optimal transport](../sources/bunne_2023_learning_single-cell_perturbation_responses_using.md)
- [Squidiff: predicting cellular development and responses to perturbations using a diffusion model](../sources/he_2025_squidiff_predicting_cellular_development_and.md)
- [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](../sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)
- [Fate Decision Intensity](../concepts/fate-decision-intensity.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md)
- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [Cell2fate](../entities/Cell2fate.md)
- [scRL](../entities/scRL.md)
- [CellOT](../entities/CellOT.md)
- [Squidiff](../entities/Squidiff.md)
- [GEARS](../entities/GEARS.md)
