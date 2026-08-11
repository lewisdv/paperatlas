---
title: Learning biophysical models of gene regulation with probability flow matching
kind: paper
status: ingested
added: 2026-08-11T11:15:30+09:00
raw_source: raw/sources/maddu_2026_learning_biophysical_models_probability_flow_matching.pdf
---

# Learning biophysical models of gene regulation with probability flow matching

## Source

- File: [raw/sources/maddu_2026_learning_biophysical_models_probability_flow_matching.pdf](../../raw/sources/maddu_2026_learning_biophysical_models_probability_flow_matching.pdf)
- Added: 2026-08-11T11:15:30+09:00
- Authors: Suryanarayana Maddu, Victor Chardès, and Michael J. Shelley
- Venue/status: arXiv preprint, arXiv:2604.25062v1 (27 April 2026)
- SHA-256: `acb74cdb435b0e8d19486a70639291c01c560389a84af31730104c83529eec04`
- Code and processed data: the paper links its project page at [vchz.github.io/pfi](https://vchz.github.io/pfi/) and processed scRNA-seq data at Zenodo record `19237708`.

## Summary

- [Probability Flow Matching (PFM)](../entities/PFM.md) is a simulation-free framework for fitting a biophysically parameterized stochastic process to multiple time-resolved single-cell snapshot distributions.
- Instead of treating a continuous trajectory only as a latent-space interpolation, the method represents transcriptomic dynamics through a Fokker–Planck / probability-flow formulation with a gene-regulatory force, state-dependent diffusion, and optionally cell-state-dependent growth or death.
- The paper argues that similar interpolation error can arise from mechanistically different dynamics. It therefore evaluates fitted models not only by observed-time-point reconstruction but also by regulatory-network agreement, shifted-initial-condition transfer, in-silico knockouts, and clonal fate/growth evidence.

## Method

- The method models a time-varying cell-state density with a Fokker–Planck equation. Its probability-flow velocity contains a regulatory drift/force `f(x)`, diffusion matrix `D(x)`, and a score term `nabla log p_t(x)`; an unbalanced extension adds a growth/death rate `g(x)`.
- PFM first estimates time-dependent scores from snapshots with denoising score matching. It then samples conditioning variables from a multi-marginal optimal-transport coupling and regresses a continuous probability-flow velocity with a conditional flow-matching objective.
- Conditional Gaussian paths are built with regularized Chebyshev interpolants rather than linear or cubic-spline paths. This makes the conditional velocity smooth across all observed time points and avoids repeated high-dimensional ODE simulation during training.
- The framework can fit several force/diffusion choices, including deterministic ODE or TrajectoryNet-style flows and stochastic additive, multiplicative, or Chemical Langevin Equation (CLE) formulations.
- For the gene-regulation experiments, the state is not the full transcriptome or a generic VAE latent. It is a curated transcription-factor (TF) count space, chosen to preserve a tractable and interpretable regulatory representation.

## Data and Reported Evidence

- Synthetic tests include a two-dimensional Ornstein–Uhlenbeck process and a Waddington-like bifurcating system with dimensions `10` through `50` and five time points. In the shown 2D reconstruction, Chebyshev interpolation has reported drift RMSE `0.1534` versus `0.5897` for a cubic spline; the paper also reports an order-of-magnitude reduction in time and memory against its simulation-based PFI baseline in a supplementary comparison.
- The ex vivo hematopoiesis analysis follows CD34++ hematopoietic stem/progenitor cells for 12 days, with scRNA-seq at days `2`, `4`, `6`, `8`, and `11`. It models a set of `24` TF genes across erythroid and megakaryocytic differentiation.
- In that experiment, a diffusion-free TrajectoryNet-style formulation has the lowest leave-one-out interpolation error, yet the paper reports that the stochastic biophysically constrained CLE formulation better recovers signed, directed TF interactions and aligns with cell-type-matched ChIP-seq networks. The evidence supports the paper's distinction between fitting observed marginals and recovering a useful regulatory mechanism; it does not make the inferred edges experimentally established causal effects.
- For shifted initial conditions, models trained on the ex vivo experiment are tested against an independent in vitro CITE-seq hematopoiesis experiment. The authors report that the CLE model more consistently recovers erythroid and megakaryocytic terminal patterns, whereas deterministic ODE and TrajectoryNet+ variants lose performance despite good interpolation of training snapshots.
- The paper simulates `KLF1` and `FLI1` knockouts by setting TF expression to zero in fitted dynamics. Stochastic formulations reproduce the expected asymmetric lineage effects more closely than the deterministic comparators. These remain in-silico predictions benchmarked against known knockout phenotypes.
- In a separate six-day neutrophil/monocyte in vitro differentiation dataset with clonal lineage information and pronounced population imbalance, unbalanced PFM models growth alongside regulatory dynamics. The source reports that only CLE exceeds random fate assignment for both lineages and that estimated growth patterns agree qualitatively with clonal-lineage estimates.

## Interpretation Boundaries and Limitations

- Recovering force and diffusion from sparse cross-sectional marginals is an ill-posed inverse problem: distinct dynamics can interpolate the same measured distributions. The paper's extra tests reduce, but do not eliminate, this non-identifiability.
- The mechanistic interpretation depends on selecting a relevant, low-dimensional TF gene set using prior biological knowledge. The authors state that finding such a set for less characterized systems, including neural or T-cell differentiation, remains open.
- The paper is a hematopoiesis-focused arXiv preprint. Its reported transfer, gene-network, perturbation, and growth results should not be generalized without validation to arbitrary tissues, gene panels, experimental protocols, or cell populations.
- Current force and score parameterizations use simple feed-forward networks. The paper identifies spatial context, longitudinal clonal information, and structured architectures such as graph neural networks or masked sparse layers as future work.

## Related Pages

- [PFM](../entities/PFM.md)
- [Biophysical Stochastic Gene-Regulatory Dynamics](../concepts/biophysical-stochastic-gene-regulatory-dynamics.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)
- [Schrödinger Bridge Generative Modeling](../concepts/schrodinger-bridge-generative-modeling.md)
- [ARTEMIS](../entities/ARTEMIS.md)
- [Cell2fate](../entities/Cell2fate.md)

## Open Questions

- What experimental constraints most effectively distinguish the many force/diffusion models that fit the same time-series marginals?
- Can a TF-space representation remain interpretable while scaling to systems without a well curated regulator set?
- How should spatial context, lineage tracing, and measured perturbations be incorporated without overconstraining the inferred stochastic process?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF under OpenJDK 21.0.12
- Generated: 2026-08-11T11:15:30+0900
- Manifest: [raw/derived/opendataloader/maddu_2026_learning_biophysical_models_probability_flow_matching/opendataloader-run.json](../../raw/derived/opendataloader/maddu_2026_learning_biophysical_models_probability_flow_matching/opendataloader-run.json)
- Output: [raw/derived/opendataloader/maddu_2026_learning_biophysical_models_probability_flow_matching/maddu_2026_learning_biophysical_models_probability_flow_matching.md](../../raw/derived/opendataloader/maddu_2026_learning_biophysical_models_probability_flow_matching/maddu_2026_learning_biophysical_models_probability_flow_matching.md)
- Layout text: [raw/derived/pdftext/Maddu_2026_PFM/Maddu_2026_PFM.txt](../../raw/derived/pdftext/Maddu_2026_PFM/Maddu_2026_PFM.txt)

These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
<!-- opendataloader:end -->
