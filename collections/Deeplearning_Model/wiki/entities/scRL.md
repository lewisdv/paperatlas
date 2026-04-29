# scRL

## Type

- Named system / method

## Definition

- scRL is an actor-critic reinforcement-learning framework for evaluating where and when cells make fate decisions along inferred developmental trajectories.
- The source frames it as a decision-analysis method rather than as a general-purpose generative model: its main outputs are decision intensity, contribution intensity, and policy trajectories over a learned manifold.

## Core Architecture

- Builds an interpretable latent manifold with LDA and projects cells through UMAP onto a grid representation.
- Assigns pseudotime through Dijkstra shortest paths from user-defined early states.
- Uses two reward modes: early-decaying decision rewards and late-increasing contribution rewards.
- Trains a critic to estimate state values and an actor to trace high-value developmental routes.

## Reported Uses

- Pinpointing early lineage-decision states in hematopoiesis and endocrinogenesis.
- Analyzing abnormal decision structure in acute myeloid leukemia.
- Testing regulator relevance through Dapp1 knockout effects on lineage landscapes.
- Tracking radiation-induced shifts in erythroid-versus-myeloid bias during hematopoietic recovery.

## Caveats

- Results depend on root-state selection, grid construction, and the assumption that shortest-path distances reflect developmental time.
- The framework is strong on decision localization but is not itself a multimodal or perturbation-generative simulator.
- Grid discretization may distort fine manifold geometry in difficult datasets.

## Related

- [Fate Decision Intensity](../concepts/fate-decision-intensity.md)
- [Cell2fate](../entities/Cell2fate.md)
- [Source: scRL: Utilizing Reinforcement Learning to Evaluate Fate Decisions in Single-Cell Data](../sources/fu_2025_scrl_utilizing_reinforcement_learning_to.md)
