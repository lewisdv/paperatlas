# Biophysical Stochastic Gene-Regulatory Dynamics

## Definition

- Biophysical stochastic gene-regulatory dynamics models a cell's expression state as an evolving stochastic process whose force, diffusion, and possibly population growth terms are tied to interpretable gene-regulatory assumptions.
- It is more demanding than a smooth trajectory fit: the intended output includes a candidate dynamical mechanism and its local response to state or gene perturbation.

## In PFM

- [PFM](../entities/PFM.md) represents the snapshot-density evolution with a Fokker–Planck / probability-flow formulation. A regulatory force `f(x)`, diffusion `D(x)`, and score determine the state velocity; an unbalanced term `g(x)` models growth or death.
- It uses conditional flow matching and Chebyshev-interpolated Gaussian paths to fit multi-marginal snapshots without the repeated high-dimensional simulation used by the earlier PFI workflow.
- The paper deliberately compares deterministic and stochastic parameterizations. It reports that a deterministic flow can interpolate observed data well while a stochastic Chemical Langevin formulation better matches regulatory and shifted-condition tests.

## What Must Be Evaluated Separately

- **Interpolation:** does the fitted process reproduce held-out time-point distributions?
- **Mechanistic recovery:** do signed and directed local regulatory interactions agree with independent biological evidence such as ChIP-seq?
- **Transfer:** do terminal states persist when the model is initialized from a related but unseen progenitor distribution?
- **Counterfactuals:** do in-silico knockouts reproduce known lineage-specific outcomes?
- **Mass dynamics:** when unbalanced, do inferred growth/death patterns agree with lineage or abundance measurements?

PFM's hematopoiesis results argue that strong performance in the first category does not guarantee success in the other four.

## Relation to Other Transition Models

- [RNA Velocity Modules](rna-velocity-modules.md) infer temporal information from spliced and unspliced kinetics. PFM instead fits a stochastic process to time-indexed cross-sectional distributions and does not require paired splicing measurements.
- [ARTEMIS](../entities/ARTEMIS.md) uses a VAE-latent unbalanced dynamic Schrödinger bridge. PFM instead uses a Fokker–Planck probability-flow formulation in curated TF gene space; both infer snapshot-consistent dynamics and both require care not to equate an inferred mass term with directly observed birth or death.
- [Schrödinger Bridge Generative Modeling](schrodinger-bridge-generative-modeling.md) constrains a path measure by its relative entropy to a reference process. PFM uses a conditional flow-matching objective and multi-marginal OT conditioning; it is related in generative-model vocabulary but is not, by itself, a Schrödinger-bridge objective.
- [Neural Optimal Transport](neural-optimal-transport.md) focuses on a source-to-target transport map. PFM uses optimal transport to construct multi-time conditioning while fitting an explicit stochastic gene-regulatory process.

## Interpretation Boundaries

- Multiple force/diffusion combinations can be consistent with the same cross-sectional marginals. No one fitted process establishes a unique causal regulatory network.
- Gene-level in-silico perturbations are predictions of the selected dynamical model. Their biological interpretation needs targeted perturbation experiments.
- A curated TF coordinate system may improve interpretability but can omit relevant genes, signaling, spatial context, and non-transcriptional mechanisms.

## Sources

- [Learning biophysical models of gene regulation with probability flow matching](../sources/maddu_2026_learning_biophysical_models_probability_flow_matching.md)
