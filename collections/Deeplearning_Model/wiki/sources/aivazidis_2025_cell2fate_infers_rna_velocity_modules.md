---
title: Cell2fate infers RNA velocity modules to improve cell fate prediction
kind: paper
status: ingested
added: 2026-04-29T15:08:37+09:00
raw_source: raw/sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.pdf
---

# Cell2fate infers RNA velocity modules to improve cell fate prediction

## Source

- File: [raw/sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.pdf](../../raw/sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.pdf)
- Added: 2026-04-29T15:08:37+09:00
- Venue/status: Nature Methods article; published online 3 March 2025
- Authors: Alexander Aivazidis, Fani Memi, Vitalii Kleshchevnikov, Sezgin Er, Brian Clarke, Oliver Stegle, Omer Ali Bayraktar
- DOI: `10.1038/s41592-025-02608-3`
- Code: [BayraktarLab/cell2fate](https://github.com/BayraktarLab/cell2fate)

## Summary

This paper introduces cell2fate, a fully Bayesian RNA velocity model that linearizes the underlying ODE system so a more biophysically faithful transcription-dynamics model can still be solved analytically. The method decomposes velocity dynamics into interpretable modules, ties those modules to a mixed-membership style view of transcriptional programs, and exposes posterior uncertainty over inferred cell-specific time. The paper positions cell2fate as a way to improve cell fate prediction, resolve weak or late dynamical signals in rare and mature cell types, and connect temporal transcriptional dynamics to spatial tissue architecture.

## Methods

- Cell2fate models spliced and unspliced counts with coupled RNA-velocity ODEs over transcription, splicing, and degradation rates.
- Its main technical move is to linearize the derivative of the transcription rate into individually integrable basis functions, called modules, so the system remains analytically solvable while allowing more complex transcription dynamics.
- Module switch times, activation and deactivation rates, and cell-specific timescales are shared structure that reduce parameter count while still allowing gene-specific transcription-rate behavior.
- The model is fully Bayesian, fits raw cell-level counts, and explicitly accounts for overdispersion, detection sensitivity differences between spliced and unspliced molecules, ambient RNA, and known batches.
- The implementation uses Pyro stochastic variational inference and integrates with `scvi-tools`, while downstream analysis uses posterior time, module activation, velocity graphs, and confidence heuristics derived from posterior samples.

## Key Claims

- A linearized, fully Bayesian RNA-velocity model can capture complex transcriptional dynamics without falling back to either coarse stepwise biophysical assumptions or heavy numerical approximations.
- Decomposing velocity into modules improves interpretability by linking RNA velocity to a biophysically grounded form of dimensionality reduction.
- Better uncertainty estimates and better recovery of subtle or late dynamics lead to more accurate cell fate directionality than competing RNA-velocity methods.

## Evidence

- Benchmark breadth: the paper compares cell2fate against ten RNA-velocity methods across five scRNA-seq datasets, including dentate gyrus, pancreas, erythroid maturation, human bone marrow, and a low-coverage mouse bone marrow dataset.
- Main benchmark result: the source reports that cell2fate achieved the best average cross-boundary directional correctness (CBDir) score across datasets and inferred the correct transition direction in all benchmark settings, whereas every other method except `pyroVelocity_model2` produced reverse-order dynamics in at least one benchmark.
- Subtle late dynamics: in mouse dentate gyrus, the paper says cell2fate resolved the late maturation trajectory of granule neurons that other methods failed to recover, including when the downstream fate analysis used CellRank.
- Complex transcriptional boosts: in mouse erythroid maturation, cell2fate recovered multi-rate kinetic genes such as `Hba-x` and `Nudt4` and reconstructed the correct lineage trajectories where simpler models performed poorly.
- Uncertainty calibration: the posterior coefficient of variation for inferred cell-specific time stayed close to zero in dynamic datasets but approached `1` in a steady-state PBMC dataset, which the paper presents as a useful quality-control signal for when velocity structure is or is not meaningful.
- Spatial application: on developing human brain data, cell2fate identified seven sequential and overlapping neuronal maturation modules and mapped progenitor-associated modules to germinal zones and neuronal modules to cortical plate regions in Visium data.

## Limitations

- The source notes that cell2fate has higher computational requirements than some existing methods, even though the authors say those requirements remain aligned with other scalable alternatives.
- The paper explicitly says the model still makes simplifying assumptions, including a constant degradation rate and no stochastic bifurcations.
- The discussion argues that future extensions should add cell-specific splicing and degradation rates, branching stochasticity, dynamic regulatory connections, and eventually cell-cell interaction effects from spatial data, which means the current model does not yet cover those mechanisms.

## Related Pages

- [Cell2fate](../entities/Cell2fate.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)

## Open Questions

- As more trajectory-oriented papers are ingested in this collection, how often do explicit dynamical models such as cell2fate outperform foundation-style embedding models on fate prediction rather than only on representation learning?
- Which later sources in this collection reuse interpretable module decompositions, and are those modules closer to regulatory programs, latent factors, or transport directions?
- How portable will cell2fate's spatial RNA-velocity workflow be to organoid or perturbation-heavy datasets if both single-cell and spatial measurements are available?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T15:08:06+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.pdf -o /tmp/odl-check-cell2fate -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/aivazidis_2025_cell2fate_infers_rna_velocity_modules/opendataloader-run.json](../../raw/derived/opendataloader/aivazidis_2025_cell2fate_infers_rna_velocity_modules/opendataloader-run.json)
- Output: [raw/derived/opendataloader/aivazidis_2025_cell2fate_infers_rna_velocity_modules/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md](../../raw/derived/opendataloader/aivazidis_2025_cell2fate_infers_rna_velocity_modules/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
