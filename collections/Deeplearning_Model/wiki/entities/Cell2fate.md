# Cell2fate

## Type

- Named system / model

## Definition

- Cell2fate is a fully Bayesian RNA-velocity model designed to infer transcriptional dynamics and cell fate direction from spliced and unspliced single-cell counts.
- The source presents it as an analytically tractable yet more biophysically faithful alternative to earlier velocity models, with interpretable module outputs and posterior uncertainty estimates.

## Core Architecture

- Models transcription, splicing, and degradation dynamics with coupled ODEs over spliced and unspliced counts.
- Linearizes the derivative of the transcription rate into a small number of analytically integrable modules.
- Uses shared module switch times, activation rates, and cell-specific timescales to regularize inference while retaining gene-specific behavior.
- Fits a Bayesian generative model on raw counts with technical-noise components for overdispersion, detection sensitivity, ambient RNA, and batches.

## Reported Uses

- RNA-velocity benchmarking across multiple developmental and low-coverage datasets.
- Improved fate-direction inference in mature granule neurons and erythroid maturation.
- Posterior-uncertainty-based quality control for deciding whether a dataset supports meaningful velocity analysis.
- Spatial mapping of neuronal maturation modules in developing human brain tissue.

## Caveats

- The model is more computationally demanding than some older RNA-velocity baselines.
- The published formulation still assumes a constant degradation rate and does not include stochastic bifurcations.
- Future extensions proposed by the authors include cell-specific rates, dynamic regulatory links, and cell-cell interaction effects, so the current model does not yet capture those mechanisms.

## Related

- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)
- [Source: Cell2fate infers RNA velocity modules to improve cell fate prediction](../sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md)
