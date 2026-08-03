---
title: Foundations of Schrödinger Bridges for Generative Modeling
kind: paper
status: ingested
added: 2026-08-03T18:26:05+09:00
raw_source: raw/sources/tang_2026_foundations_schrodinger_bridges_generative_modeling.pdf
---

# Foundations of Schrödinger Bridges for Generative Modeling

## Source

- File: [raw/sources/tang_2026_foundations_schrodinger_bridges_generative_modeling.pdf](../../raw/sources/tang_2026_foundations_schrodinger_bridges_generative_modeling.pdf)
- Added: 2026-08-03T18:26:05+09:00
- Author: Sophia Tang
- Venue/status: arXiv preprint, arXiv:2603.18992v1 (19 March 2026)
- SHA-256: `5e707a69bd7ba57d90625e84bb3b3ffb54da5df485f6dd3a6503d7225f08ffd1`

## Summary

- This 220-page tutorial develops [Schrödinger bridge generative modeling](../concepts/schrodinger-bridge-generative-modeling.md) from static and dynamic formulations through algorithms, stochastic control, diffusion-model connections, and extensions.
- A Schrödinger bridge seeks a stochastic path distribution that matches prescribed endpoint distributions while staying closest, in relative entropy, to a chosen reference stochastic process.
- The source provides the theoretical context for ARTEMIS's unbalanced dynamic bridge, but it is not an empirical single-cell benchmark and does not independently validate ARTEMIS or CMonge results.

## Core Formulation

- The dynamic problem minimizes path-space Kullback–Leibler divergence `KL(P || Q)`, where `P` is the fitted path measure and `Q` is a reference process, subject to initial and terminal marginal constraints.
- The static formulation instead optimizes a coupling over endpoints relative to the reference endpoint coupling. Under its stated conditions, it has a unique solution and connects to entropy-regularized optimal transport.
- Iterative proportional fitting / Sinkhorn updates alternately enforce the endpoint marginals through Schrödinger potentials. The dynamic construction can be expressed with forward and backward drifts, Fokker–Planck equations, Doob `h` transforms, and stochastic-control objectives.
- The low-noise limit connects the bridge to dynamic optimal transport, but finite-noise Schrödinger bridges are not simply deterministic optimal-transport maps: the reference stochasticity remains part of the model.

## Generative-Model Connections

- The tutorial relates Schrödinger bridges to score-based diffusion models, forward-backward SDEs, likelihood computation, flow matching, stochastic interpolants, and simulation-free bridge-matching objectives.
- It covers Gaussian, branched, unbalanced, multi-marginal, fractional, and mean-field-interaction variants. These choices alter the reference process, constraints, or mass behavior rather than being interchangeable implementations.
- The multi-marginal and unbalanced variants are especially relevant to time-series biology: intermediate snapshots can be constrained explicitly, while a source/sink term can represent changing population mass.

## Relevance to Single-Cell Modeling

- In the source's biological modeling discussion, consecutive cell-state distributions can be treated as time-indexed marginals. A multi-marginal bridge then constrains intermediate measurements rather than only matching the endpoints.
- An unbalanced bridge provides one formal way to model cell-population growth or loss across time, which is the mechanism used by [ARTEMIS](../entities/ARTEMIS.md).
- This is distinct from [CMonge](../entities/CMonge.md): CMonge uses a conditional Monge-Gap transport objective for treatment-context mapping, not the reference-process path-space KL formulation described here.
- It is also distinct from splicing-based [RNA Velocity Modules](../concepts/rna-velocity-modules.md), whose temporal signal arises from spliced and unspliced count kinetics.

## Interpretation Boundaries

- A bridge is conditional on its marginal observations, reference process, noise level, parameterization, and optimization procedure. It is an inferential coupling, not direct observation of individual cells moving through time.
- Matching distributions does not establish biological causality, lineage ancestry, or a unique molecular mechanism. Those conclusions require orthogonal measurements and interventions.
- The tutorial collects general theory and examples. Its practical guidance does not establish that every variant is identifiable or numerically stable for sparse, high-dimensional, or heavily confounded biological data.

## Related Pages

- [Schrödinger Bridge Generative Modeling](../concepts/schrodinger-bridge-generative-modeling.md)
- [ARTEMIS](../entities/ARTEMIS.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [CMonge](../entities/CMonge.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)

## Open Questions

- What biologically defensible reference processes and noise scales should be used for single-cell developmental or perturbation paths?
- How many time points, cells, and independently measured intermediates are needed to distinguish a bridge from other plausible couplings?
- Which constraints can combine lineage tracing, multimodal state, and population growth without treating model assumptions as observed biology?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF under OpenJDK 21.0.12
- Generated: 2026-08-03T18:26:05+0900
- Manifest: [raw/derived/opendataloader/tang_2026_foundations_schrodinger_bridges_generative_modeling/opendataloader-run.json](../../raw/derived/opendataloader/tang_2026_foundations_schrodinger_bridges_generative_modeling/opendataloader-run.json)
- Output: [raw/derived/opendataloader/tang_2026_foundations_schrodinger_bridges_generative_modeling/tang_2026_foundations_schrodinger_bridges_generative_modeling.md](../../raw/derived/opendataloader/tang_2026_foundations_schrodinger_bridges_generative_modeling/tang_2026_foundations_schrodinger_bridges_generative_modeling.md)
- Layout text: [raw/derived/pdftext/Tang_2026_Schrodinger_Bridges/Tang_2026_Schrodinger_Bridges.txt](../../raw/derived/pdftext/Tang_2026_Schrodinger_Bridges/Tang_2026_Schrodinger_Bridges.txt)

These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
<!-- opendataloader:end -->
