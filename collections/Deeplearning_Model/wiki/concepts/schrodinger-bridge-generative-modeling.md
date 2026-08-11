# Schrödinger Bridge Generative Modeling

## Definition

- A Schrödinger bridge infers a stochastic path distribution between observed marginals while remaining close, in path-space relative entropy, to a chosen reference process.
- It is related to entropy-regularized optimal transport, but its finite-noise formulation retains a stochastic reference process and a whole path distribution rather than only a deterministic source-to-target map.

## Static and Dynamic Views

- The static problem solves for an endpoint coupling that satisfies the endpoint marginals while remaining close to the reference endpoint coupling.
- The dynamic problem minimizes `KL(P || Q)` over path measures `P` subject to marginal constraints, with `Q` the reference process.
- The low-noise limit links the dynamic bridge to optimal transport. It does not make finite-noise Schrödinger bridge inference interchangeable with ordinary deterministic OT.

## Constructive Machinery

- Iterative proportional fitting and Sinkhorn updates alternate marginal enforcement through Schrödinger potentials.
- Equivalent or linked expressions use forward and backward SDEs, Fokker–Planck equations, Doob `h` transforms, Girsanov change of measure, and stochastic control.
- Current generative-model connections include score-based diffusion, diffusion Schrödinger bridge matching, flow matching, stochastic interpolants, likelihood methods, and simulation-free objectives.

## Single-Cell Uses

- [ARTEMIS](../entities/ARTEMIS.md) applies an unbalanced dynamic bridge in VAE latent space to time-series scRNA-seq distributions and augments it with a population-mass killing-rate function.
- Multi-marginal bridges can constrain several observed time points; unbalanced variants can represent changing population mass. Both are modeling choices that require biological validation.
- [PFM](../entities/PFM.md) is related through flow-matching and Fokker–Planck language, but it is not a Schrödinger-bridge formulation: it fits a probability flow with conditional flow matching and multi-marginal OT conditioning rather than constraining a path measure by KL divergence to a reference process.
- This differs from [CMonge](../entities/CMonge.md), which uses a conditional Monge-Gap transport objective across treatment contexts, and from [CellOT](../entities/CellOT.md), which learns perturbation-specific deterministic transport maps.
- It also differs from [RNA Velocity Modules](rna-velocity-modules.md), which obtain temporal information from spliced and unspliced transcription kinetics.

## Interpretation Boundaries

- A fitted bridge is not observed lineage tracing or proof of individual-cell ancestry. It is one stochastic coupling consistent with data and modeling assumptions.
- Biological conclusions depend on the selected reference process, cost/noise scale, marginals, representation, and numerical solver.
- A good distributional fit does not by itself prove causality, mechanism, proliferation, death, or a unique intervening trajectory.

## Sources

- [Foundations of Schrödinger Bridges for Generative Modeling](../sources/tang_2026_foundations_schrodinger_bridges_generative_modeling.md)
- [ARTEMIS integrates autoencoders and Schrödinger Bridges to predict continuous dynamics](../sources/alatkar_2025_artemis_schrodinger_bridge_dynamics.md)
- [Conditional Monge Gap enables generalizable single-cell perturbation modelling](../sources/driessen_2026_cmonge_generalizable_perturbation.md)
