---
title: ARTEMIS integrates autoencoders and Schrödinger Bridges to predict continuous dynamics of gene expression, cell population, and perturbation from time-series single-cell data
kind: paper
status: ingested
added: 2026-08-03T18:26:05+09:00
raw_source: raw/sources/alatkar_2025_artemis_schrodinger_bridge_dynamics.pdf
---

# ARTEMIS integrates autoencoders and Schrödinger Bridges to predict continuous dynamics of gene expression, cell population, and perturbation from time-series single-cell data

## Source

- File: [raw/sources/alatkar_2025_artemis_schrodinger_bridge_dynamics.pdf](../../raw/sources/alatkar_2025_artemis_schrodinger_bridge_dynamics.pdf)
- Added: 2026-08-03T18:26:05+09:00
- Authors: Sayali Anil Alatkar and Daifeng Wang
- Venue/status: *Bioinformatics* 41 (Supplement 1), i189–i197 (2025), ISMB/ECCB 2025 proceedings
- DOI: [10.1093/bioinformatics/btaf218](https://doi.org/10.1093/bioinformatics/btaf218)
- License shown in the supplied PDF: CC BY 4.0
- SHA-256: `9793bf57fefccc652c3d00aa2a66183cdc805fea486e9b451afa7f28fd15d8d6`

## Summary

- [ARTEMIS](../entities/ARTEMIS.md) (`trAjectory infeRence wiTh unbalancEd dynaMic optImal tranSport`) predicts continuous cell-state, cell-population, and in-silico perturbation trajectories from time-series scRNA-seq snapshots.
- It combines a variational autoencoder (VAE) with an unbalanced dynamic Schrödinger bridge (uDSB). The VAE places expression profiles in a lower-dimensional latent space; the uDSB learns stochastic paths between observed time-point distributions.
- The unbalanced component estimates a time-varying killing rate, allowing the fitted path to represent changing population mass through proliferation or death rather than forcing every time point to contain the same mass.
- The source makes ARTEMIS relevant to this collection as a time-aware complement to endpoint perturbation models: it predicts a distributional path and its drift, not only a treated endpoint.

## Method

- A VAE is first trained to encode high-dimensional scRNA-seq profiles into a latent representation. ARTEMIS then jointly refines the VAE and uDSB components.
- The uDSB uses forward and backward stochastic differential equation drifts and iterative proportional fitting / Sinkhorn-style updates to match observed marginal distributions across time.
- A neural killing-rate function represents time-dependent birth/death imbalance. The output therefore includes predicted relative population sizes as well as latent cell distributions.
- The learned drift can be mapped back to genes, yielding a ranked interpretation of genes associated with movement along the inferred latent trajectory.
- For in-silico perturbation, the paper modifies selected genes at an observed time point, transports the modified cells forward, and compares their predicted later-state assignments with the unperturbed prediction.

## Data and Reported Evidence

- The study uses pancreatic beta-cell differentiation (`51,274` cells across eight time points; GSE114412), zebrafish embryogenesis (`38,731` cells across 12 time points), and epithelial-to-mesenchymal transition (EMT; `3,133` cells across five time points; GSE147405).
- The held-out-time-point comparison uses Wasserstein distance against uDSB, MIOFlow, PRESCIENT, and scNODE. ARTEMIS is reported to be competitive across all three datasets and lower than several baselines in later pancreatic time points and the EMT evaluation.
- The table is not a uniform win: at pancreatic time point 3, scNODE's reported Wasserstein value (`9.73`) is slightly lower than ARTEMIS's (`9.84`). The paper therefore supports competitive, task-dependent gains rather than an across-the-board superiority claim.
- In zebrafish, the authors use the inferred drift to highlight temporally changing genes and construct an `artemis` R package workflow for trajectory inspection.
- In EMT, simulated over- and under-expression of `TPM1` and `AMIGO2` changes the predicted later-state distribution. These are model-based counterfactual outputs, not experimental validation that the edits cause the predicted transitions.

## Interpretation Boundaries and Limitations

- Sparse observation times limit temporal resolution: a continuous bridge interpolates between snapshots, but it does not observe every intervening cellular event.
- The source requires preprocessing or prior correction when batch effects are substantial; technical variation can otherwise be interpreted as biological movement.
- Joint VAE/uDSB optimization adds model and hyperparameter complexity. The inferred killing rate is a representation of mass change, not direct measurement of individual cell birth or death.
- The supplied study is limited to scRNA-seq. Chromatin or other modalities, explicit lineage tracing, and experimental perturbation validation are future directions rather than demonstrated guarantees.

## Related Pages

- [ARTEMIS](../entities/ARTEMIS.md)
- [Schrödinger Bridge Generative Modeling](../concepts/schrodinger-bridge-generative-modeling.md)
- [Neural Optimal Transport](../concepts/neural-optimal-transport.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)
- [Cell2fate](../entities/Cell2fate.md)
- [Squidiff](../entities/Squidiff.md)

## Open Questions

- Under what time-point density and sequencing depth does an inferred bridge remain stable enough to support gene-level drift interpretation?
- How should ARTEMIS's inferred population killing rate be validated against lineage tracing, division, and cell-death measurements?
- Can a multimodal version distinguish transcriptional movement from chromatin-state changes that precede it?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF under OpenJDK 21.0.12
- Generated: 2026-08-03T18:26:05+0900
- Manifest: [raw/derived/opendataloader/alatkar_2025_artemis_schrodinger_bridge_dynamics/opendataloader-run.json](../../raw/derived/opendataloader/alatkar_2025_artemis_schrodinger_bridge_dynamics/opendataloader-run.json)
- Output: [raw/derived/opendataloader/alatkar_2025_artemis_schrodinger_bridge_dynamics/alatkar_2025_artemis_schrodinger_bridge_dynamics.md](../../raw/derived/opendataloader/alatkar_2025_artemis_schrodinger_bridge_dynamics/alatkar_2025_artemis_schrodinger_bridge_dynamics.md)
- Layout text: [raw/derived/pdftext/Alatkar_2025_ARTEMIS/Alatkar_2025_ARTEMIS.txt](../../raw/derived/pdftext/Alatkar_2025_ARTEMIS/Alatkar_2025_ARTEMIS.txt)

These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
<!-- opendataloader:end -->
