---
title: Learning single-cell perturbation responses using neural optimal transport
kind: paper
status: ingested
added: 2026-04-29T15:02:54+09:00
raw_source: raw/sources/bunne_2023_learning_single-cell_perturbation_responses_using.pdf
---

# Learning single-cell perturbation responses using neural optimal transport

## Source

- File: [raw/sources/bunne_2023_learning_single-cell_perturbation_responses_using.pdf](../../raw/sources/bunne_2023_learning_single-cell_perturbation_responses_using.pdf)
- Added: 2026-04-29T15:02:54+09:00
- Venue/status: Nature Methods article; published online 28 September 2023
- Authors: Charlotte Bunne, Stefan G. Stark, Gabriele Gut, Jacobo Sarabia del Castillo, Mitch Levesque, Kjong-Van Lehmann, Lucas Pelkmans, Andreas Krause, Gunnar Raetsch
- DOI: `10.1038/s41592-023-01969-x`

## Summary

This paper presents CellOT, a neural optimal transport framework for predicting single-cell perturbation responses when only unpaired control and treated populations are observed. Instead of modeling perturbations as a simple latent shift, the method learns perturbation-specific transport maps between distributions and uses those maps to forecast treated states for previously unseen control cells. The paper positions this as a way to preserve heterogeneous subpopulation structure while generalizing across samples, patients, species, and developmental settings.

## Methods

- CellOT learns a perturbation-specific map `T_k` that transports an unperturbed control distribution `rho_c` to a perturbed distribution `rho_k`.
- Rather than directly parameterizing the primal transport map, the method parameterizes dual optimal transport potentials `f` and `g` with input convex neural networks.
- The learned transport map is recovered as the gradient of a convex function, `nabla g_k`, which gives a fully parameterized predictor that can be applied to unseen control cells.
- For high-dimensional scRNA-seq settings, the source applies CellOT on latent representations learned by an autoencoder before transport modeling.
- Evaluation is distributional rather than cell-pair-based, using metrics such as maximum mean discrepancy, `l2` feature means, and average correlation coefficient `r^2`.

## Key Claims

- Unpaired single-cell perturbation-response prediction can be modeled effectively with neural optimal transport rather than relying on linear latent shifts.
- Explicit transport maps better preserve heterogeneous response structure and higher moments of the treated population than the compared autoencoder baselines.
- Fully parameterized transport maps can generalize beyond the training cells to unseen patients, new sample compositions, and some cross-species settings when similar structure is represented in training data.

## Evidence

- Benchmark setup: the paper compares CellOT against `scGEN`, `cAE`, and `PopAlign` on melanoma 4i drug-response data with `34` treatments and scRNA-seq data with `9` treatments.
- Distribution matching: the source states that autoencoder baselines tend to capture the treated mean but miss heterogeneous states, whereas CellOT captures higher moments and approaches the observed lower bound on MMD while baselines often do not improve much over the identity baseline.
- Aggregate performance: across all `35` 4i therapies and `6` scRNA-seq therapies, the paper reports that CellOT outperforms baselines on MMD, `l2` feature means, and overall mean correlation coefficient `r^2`, typically by one order of magnitude.
- Unseen-patient generalization: on lupus PBMC scRNA-seq under IFN-beta treatment, the source reports that CellOT outperforms baselines in both i.i.d. and out-of-sample holdout-patient settings and suffers a smaller performance drop when generalizing to the unseen patient.
- Cross-species transfer: for LPS-stimulated mononuclear phagocytes from pig, rabbit, mouse, and rat, the paper reports stronger out-of-distribution reconstruction of innate immune responses, including lower MMD and better marker-gene alignment in holdout mouse or rat settings.
- Developmental modeling: the source also applies CellOT to hematopoietic differentiation and reports better short-range developmental predictions than the compared methods, while noting performance declines for longer-range transitions and sparse cell types.

## Limitations

- The source explicitly says out-of-distribution success requires training data that contain samples similar in both baseline state and perturbation response; unique patient responses remained difficult in the glioblastoma cohort.
- The paper reports that performance drops when perturbations are too strong, when molecular transitions have progressed too far, or when time resolution is too coarse for the minimal-effort OT assumption to remain plausible.
- Sparse cell types and highly variable cohorts reduce performance, and the scRNA-seq workflow still uses an auxiliary autoencoder latent space for high-dimensional data.

## Related Pages

- [CellOT](../entities/CellOT.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)

## Open Questions

- How often will neural optimal transport remain competitive in this collection once more perturbation-focused transformer and diffusion papers are ingested?
- When this collection accumulates more perturbation datasets, where do OT-based maps appear strongest: acute drug response, developmental trajectories, or cross-sample patient transfer?
- Which later sources in this collection, if any, relax CellOT's requirement that training data already contain samples with similar baseline and response structure?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T15:05:15+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/bunne_2023_learning_single-cell_perturbation_responses_using.pdf -o /tmp/odl-check-bunne -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/bunne_2023_learning_single-cell_perturbation_responses_using/opendataloader-run.json](../../raw/derived/opendataloader/bunne_2023_learning_single-cell_perturbation_responses_using/opendataloader-run.json)
- Output: [raw/derived/opendataloader/bunne_2023_learning_single-cell_perturbation_responses_using/bunne_2023_learning_single-cell_perturbation_responses_using.md](../../raw/derived/opendataloader/bunne_2023_learning_single-cell_perturbation_responses_using/bunne_2023_learning_single-cell_perturbation_responses_using.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
