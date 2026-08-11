# PFM

## Type

- Simulation-free stochastic dynamics framework for time-resolved single-cell snapshots

## Definition

- PFM means Probability Flow Matching.
- It learns a biophysically parameterized probability-flow process from multiple cross-sectional single-cell time points, including force, diffusion, and optionally population growth/death dynamics.

## Core Components

- A Fokker–Planck / probability-flow representation combines a regulatory force `f(x)`, diffusion `D(x)`, and a time-dependent score estimate.
- A conditional flow-matching objective regresses the velocity field without repeatedly solving high-dimensional ODEs during training.
- Multi-marginal optimal transport supplies conditioning variables across observed time points.
- Regularized Chebyshev interpolants define smooth conditional Gaussian paths across the full time range.
- An unbalanced mass extension uses a state-dependent growth/death function `g(x)`.

## Reported Uses

- Synthetic recovery of stochastic drift fields and comparison of temporal interpolation schemes.
- Hematopoietic TF-network inference, shifted-initial-condition transfer, and simulated `KLF1` / `FLI1` knockouts.
- Joint fate and proliferation/death inference in a clonally tracked neutrophil/monocyte differentiation dataset.

## Caveats

- The inferred process is underdetermined by snapshot marginals alone; regulatory form, diffusion, score estimation, and TF feature selection are substantive assumptions.
- Good interpolation does not demonstrate that the force field or its local perturbation effects are biologically correct.
- Current evidence is a hematopoiesis-focused preprint and uses a curated TF gene space rather than unrestricted full-transcriptome modeling.

## Related

- [Biophysical Stochastic Gene-Regulatory Dynamics](../concepts/biophysical-stochastic-gene-regulatory-dynamics.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)
- [ARTEMIS](ARTEMIS.md)
- [Schrödinger Bridge Generative Modeling](../concepts/schrodinger-bridge-generative-modeling.md)
- [Source: Learning biophysical models of gene regulation with probability flow matching](../sources/maddu_2026_learning_biophysical_models_probability_flow_matching.md)
