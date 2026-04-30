# RNA Velocity Modules

## Definition

- In this collection, RNA velocity modules are interpretable components of transcriptional dynamics inferred from spliced and unspliced counts over cellular trajectories.
- Rather than treating velocity as a single opaque vector field, the module view decomposes transcription-rate changes into smaller programs that can be tracked over inferred time.

## In Cell2fate

- Cell2fate linearizes the derivative of the transcription rate into individually integrable basis functions called modules.
- Each module has ON and OFF behavior, activation or deactivation rates, and a contribution to gene-specific transcription-rate changes.
- Module activations can be visualized over inferred time, linked to marker genes, and projected back onto spatial transcriptomics data.
- Compared with [Fate Decision Intensity](fate-decision-intensity.md), the aim here is to recover interpretable transcriptional dynamics rather than score where commitment pressure is highest on a manifold.
- Compared with [Stimulus-Response Diffusion Modeling](stimulus-response-diffusion-modeling.md), this concept is tied to explicit splicing-based temporal structure rather than generative latent interpolation between conditions.
- Compared with [Gene-Level Perturbation Uncertainty](gene-level-perturbation-uncertainty.md), the uncertainty role here is posterior quality control over temporal dynamics, not confidence over intervention-effect presence or magnitude.

## Claimed Benefits

- Provides a biophysical connection between RNA velocity and dimensionality reduction or factor-style decompositions.
- Helps resolve subtle, late, or overlapping maturation programs that simpler velocity models miss.
- Creates interpretable dynamic programs that can be used for downstream lineage analysis, confidence assessment, and spatial mapping.

## Caveats

- Module quality still depends on the adequacy of the underlying velocity model and its simplifying assumptions.
- The current formulation does not yet include richer mechanisms such as stochastic branching, cell-specific degradation rates, or explicit cell-cell interaction dynamics.
- Spatial interpretation of modules may also depend on external deconvolution tooling such as `cell2location`.

## Sources

- [Cell2fate infers RNA velocity modules to improve cell fate prediction](../sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md)
