# CellOT

## Type

- Named system / model

## Definition

- CellOT is a neural optimal transport framework for predicting single-cell perturbation responses from unpaired control and treated populations.
- The source presents it as a way to infer likely post-perturbation cell states and apply the learned perturbation map to previously unseen control cells.

## Core Architecture

- Learns a separate perturbation-specific transport map `T_k` from control distribution `rho_c` to perturbed distribution `rho_k`.
- Parameterizes dual optimal transport potentials `f` and `g` with input convex neural networks rather than directly fitting the primal map.
- Recovers the transport map as the gradient `nabla g_k`, giving a fully parameterized predictor for unseen cells.
- Applies the transport model to autoencoder latent representations in high-dimensional scRNA-seq settings.

## Reported Uses

- Predicting drug-response distributions in melanoma 4i and scRNA-seq datasets.
- Predicting IFN-beta responses for holdout lupus patients.
- Inferring LPS responses across species.
- Modeling hematopoietic developmental trajectories and potency changes.

## Caveats

- The method depends on an optimal-transport minimal-effort prior and on sufficiently preserved geometry between control and perturbed populations.
- The source says out-of-distribution prediction works only when the training cohort contains samples similar in both baseline state and perturbation response; unique glioblastoma responses remained difficult.
- Performance drops for strong or long-range perturbations and for sparsely represented cell types.

## Related

- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [Source: Learning single-cell perturbation responses using neural optimal transport](../sources/bunne_2023_learning_single-cell_perturbation_responses_using.md)
