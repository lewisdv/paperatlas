---
title: Squidiff: predicting cellular development and responses to perturbations using a diffusion model
kind: paper
status: ingested
added: 2026-04-29T21:20:22+09:00
raw_source: raw/sources/he_2025_squidiff_predicting_cellular_development_and.pdf
---

# Squidiff: predicting cellular development and responses to perturbations using a diffusion model

## Source

- File: [raw/sources/he_2025_squidiff_predicting_cellular_development_and.pdf](../../raw/sources/he_2025_squidiff_predicting_cellular_development_and.pdf)
- Added: 2026-04-29T21:20:22+09:00
- Venue/status: Nature Methods article; received 16 November 2024 and accepted 18 September 2025. The extracted markdown shows the online-publication field as `xx xx xxxx`.
- Authors: Siyu He, Yuefei Zhu, Daniel Naveed Tavakol, Haotian Ye, Yeh-Hsing Lao, Zixian Zhu, Cong Xu, Shradha Chauhan, Guy Garty, Raju Tomer, Gordana Vunjak-Novakovic, James Zou, Elham Azizi, and Kam W. Leong
- DOI: `10.1038/s41592-025-02877-y`

## Summary

This paper presents Squidiff, a conditional diffusion-model framework for predicting transcriptomic changes during differentiation, gene perturbation, drug response, and environmental injury. The central idea is to encode cells into a semantic latent space and then use conditional denoising diffusion to generate future, past, or perturbed transcriptomes under specified stimuli. In this collection, the paper matters because it provides a strong diffusion-based alternative to VAE, transport, and token-based perturbation models, and it explicitly targets transient intermediate states that simpler methods tend to miss.

## Methods

- Squidiff combines a semantic encoder with a conditional denoising diffusion implicit model (DDIM), using a semantic latent variable `zsem` plus Gaussian noise `xT` to generate target transcriptomes.
- Cell-state changes are produced by manipulating latent semantics in two main ways: interpolation between states for developmental trajectories and vector addition for perturbations or stimulus responses.
- The framework can incorporate explicit perturbation information such as gene edits, drug identities, dosages, and later an adaptor based on rescaled functional class fingerprints (`rFCFP`) for unseen-drug generalization.
- Benchmarks span iPSC differentiation, nonadditive gene perturbation in K562 cells, melanoma drug combinations, glioblastoma drug-response transfer, unseen-drug sci-Plex evaluation, and blood vessel organoid (BVO) development under neutron irradiation and G-CSF treatment.
- Several analyses deliberately mask some cell types or conditions during training to test whether Squidiff can reconstruct missing states from partial observations.

## Key Claims

- Diffusion-based generation can better capture smooth, high-resolution, transient cell-state transitions than prior perturbation models built around VAEs or simpler latent-vector operations.
- A single generative framework can cover differentiation, gene perturbation, drug response, and injury-response modeling rather than staying narrow to one task family.
- Semantic latent directions can be used as reusable stimulus vectors for interpolation, extrapolation, and combination of perturbations.
- Squidiff can support in silico screening and dynamic hypothesis generation even in complex systems such as blood vessel organoids exposed to radiation or protective factors.

## Evidence

- In iPSC-to-endoderm differentiation, the paper reports that Squidiff outperformed scGen across time-point prediction metrics including Pearson correlation and `R2`, with six-run significance testing reported in Figure 2.
- For nonadditive gene perturbation in K562 cells, the source states that Squidiff produced more robust and precise predictions than both GEARS and scGen without needing explicit graph priors.
- For unseen-drug prediction on sci-Plex, the paper says Squidiff with the drug adaptor performs comparably to or better than PRnet in both unseen-drug and random-split evaluations.
- In blood vessel organoids, Squidiff reconstructed developmental trajectories, suggested a mural-to-endothelial pathway consistent with cited experimental work, and captured transient mural-progenitor-like states that the paper says scGen failed to recover.
- The organoid injury studies further test cross-condition prediction: Squidiff predicts irradiation responses and then G-CSF-treated responses for fibroblasts and mural cells even when only endothelial training information is provided for some conditions.

## Limitations

- The paper explicitly notes that diffusion training is slow and computationally heavier than simpler generative frameworks such as VAEs or GANs.
- The model's semantic-variable arithmetic currently assumes an approximate linearity that may break down in more complex biological scenarios.
- Prediction for completely unseen drugs is limited unless an adaptor such as `rFCFP` is introduced, meaning native transfer is not fully open-ended.
- Some validations use alternative modalities or partial training setups, such as the `4i` melanoma assay with only about `50` features per condition, so not every benchmark is full scRNA-seq end to end.

## Related Pages

- [Squidiff](../entities/Squidiff.md)
- [Stimulus-Response Diffusion Modeling](../concepts/stimulus-response-diffusion-modeling.md)
- [CellOT](../entities/CellOT.md)
- [AIVC](../entities/AIVC.md)

## Open Questions

- How often will diffusion-based transient-state interpolation outperform transport-based or token-based perturbation models on datasets beyond the organoid and cancer settings used here?
- Does the semantic-latent-vector arithmetic remain reliable for higher-order perturbation combinations, or will it need more explicit biological structure?
- As more virtual-cell and perturbation papers accumulate in this collection, should Squidiff be treated mainly as a perturbation model, a developmental simulator, or an early virtual-cell ingredient?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T21:19:25+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/he_2025_squidiff_predicting_cellular_development_and.pdf -o /tmp/odl-check-squidiff -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/he_2025_squidiff_predicting_cellular_development_and/opendataloader-run.json](../../raw/derived/opendataloader/he_2025_squidiff_predicting_cellular_development_and/opendataloader-run.json)
- Output: [raw/derived/opendataloader/he_2025_squidiff_predicting_cellular_development_and/he_2025_squidiff_predicting_cellular_development_and.md](../../raw/derived/opendataloader/he_2025_squidiff_predicting_cellular_development_and/he_2025_squidiff_predicting_cellular_development_and.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->

## Open Questions

- Pending ingest.
