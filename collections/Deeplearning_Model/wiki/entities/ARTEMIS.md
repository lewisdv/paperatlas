# ARTEMIS

## Type

- Time-series single-cell trajectory and perturbation model

## Definition

- ARTEMIS means `trAjectory infeRence wiTh unbalancEd dynaMic optImal tranSport`.
- It combines a variational autoencoder with an unbalanced dynamic Schrödinger bridge to infer continuous latent trajectories between time-series scRNA-seq snapshots.

## Core Components

- A VAE maps cells into a latent space in which trajectory modeling is performed.
- Forward and backward stochastic drifts are fit through an unbalanced dynamic Schrödinger bridge.
- A time-varying killing-rate function captures population-mass change that the model interprets as birth, proliferation, or death.
- A back-projection of the inferred drift supports gene-level trajectory interpretation and a perturbation workflow modifies selected genes before forward prediction.

## Reported Uses

- Held-out time-point reconstruction for pancreatic beta-cell differentiation, zebrafish embryogenesis, and EMT.
- Prediction of relative population-size changes across time.
- Model-assisted over- and under-expression experiments for `TPM1` and `AMIGO2` in EMT.

## Caveats

- The inferred path, drift, and mass change depend on sparse snapshots, the latent VAE, reference stochasticity, and transport assumptions.
- A killing-rate estimate is not direct lineage, proliferation, or cell-death measurement.
- In-silico gene modification is a counterfactual model output, not evidence of causal intervention without experimental validation.

## Related

- [Schrödinger Bridge Generative Modeling](../concepts/schrodinger-bridge-generative-modeling.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [Cell2fate](Cell2fate.md)
- [Squidiff](Squidiff.md)
- [Source: ARTEMIS integrates autoencoders and Schrödinger Bridges to predict continuous dynamics](../sources/alatkar_2025_artemis_schrodinger_bridge_dynamics.md)
