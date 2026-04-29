---
title: scRL: Utilizing Reinforcement Learning to Evaluate Fate Decisions in Single-Cell Data
kind: paper
status: ingested
added: 2026-04-29T21:20:22+09:00
raw_source: raw/sources/fu_2025_scrl_utilizing_reinforcement_learning_to.pdf
---

# scRL: Utilizing Reinforcement Learning to Evaluate Fate Decisions in Single-Cell Data

## Source

- File: [raw/sources/fu_2025_scrl_utilizing_reinforcement_learning_to.pdf](../../raw/sources/fu_2025_scrl_utilizing_reinforcement_learning_to.pdf)
- Added: 2026-04-29T21:20:22+09:00
- Venue/status: Biology 2025, volume 14, article 679; published 11 June 2025
- Authors: Zeyu Fu, Chunlin Chen, Song Wang, Junping Wang, and Shilei Chen
- DOI: `10.3390/biology14060679`

## Summary

This paper presents scRL, an actor-critic reinforcement-learning framework for identifying where and when fate decisions occur in single-cell developmental trajectories. Instead of only ordering cells along pseudotime, scRL tries to estimate a cell state's decision intensity before overt lineage commitment and separately quantify later lineage contribution. In this collection, the paper matters because it adds a trajectory-and-decision modeling axis that is distinct from generative foundation models, yet still targets the core problem of predicting cell-state change.

## Methods

- scRL first builds an interpretable latent space with Latent Dirichlet Allocation (LDA), embeds cells with UMAP, and rasterizes the manifold onto a topology-preserving grid.
- Pseudotime is assigned over this grid with Dijkstra shortest paths from user-defined early cells or clusters.
- The method defines two reward landscapes: a decision mode whose reward decays with pseudotime to emphasize early commitment signals, and a contribution mode whose reward increases with pseudotime to emphasize later lineage output.
- An actor network learns policy trajectories over the grid, while a critic network learns state values that become cell-level decision or contribution intensities.
- The framework is evaluated on hematopoiesis, mouse endocrinogenesis, acute myeloid leukemia, Dapp1 knockout, and irradiation-response datasets.

## Key Claims

- Reinforcement learning can recover early decision states that standard trajectory tools miss because it explicitly treats differentiation as a sequential decision process.
- Fate decision intensity and lineage contribution intensity should be modeled separately rather than conflated with pseudotime or marker expression alone.
- scRL can outperform a large panel of fate-inference, pseudotime, and latent-space baselines across multiple biological systems.
- The same framework can surface regulators of lineage choice, not only trajectory structure, as illustrated by Dapp1-centered perturbation analyses.

## Evidence

- The abstract and simple summary both state that scRL outperformed fifteen state-of-the-art methods across five evaluation dimensions and recovered early decision states that precede obvious lineage commitment.
- The source benchmarks scRL on several distinct regimes rather than one curated example: normal hematopoiesis, mouse endocrinogenesis, acute myeloid leukemia, Dapp1 knockout, and irradiation injury.
- Comparative tables and figure summaries report that LDA latent spaces and scRL-derived intensities outperform or exceed multiple alternatives such as PCA, ICA, NMF, diffusion maps, scVI, and related methods on interpretability-oriented metrics.
- The perturbation validation uses Dapp1 knockout hematopoietic data to show that altering a proposed regulator reshapes lineage decision landscapes, supporting the biological relevance of the learned decision intensities.
- Radiation-injury analyses further show that scRL can track changing erythroid-versus-myeloid fate biases during recovery, extending the method beyond normal differentiation.

## Limitations

- The method depends on user-defined starting points, so poor choice of early cells or clusters can bias pseudotime alignment and downstream decision scores.
- It assumes shortest-path distances on the grid approximate developmental time, which the paper itself notes may fail in systems with rapid or nonmonotonic transitions.
- Grid discretization can introduce artificial barriers or shortcuts relative to the continuous manifold.
- The framework's interpretability and performance still depend on several design choices, including the LDA representation and grid hyperparameters such as `n = 50` and `j = 3`.

## Related Pages

- [scRL](../entities/scRL.md)
- [Fate Decision Intensity](../concepts/fate-decision-intensity.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)
- [Cell2fate](../entities/Cell2fate.md)

## Open Questions

- How often will decision-intensity peaks agree with RNA-velocity-based dynamic programs versus reveal earlier or different commitment structure?
- Could a future source in this collection combine reinforcement-learning trajectory analysis with a stronger generative or multimodal foundation-model backbone?
- How sensitive are scRL conclusions to the chosen root-state definition in datasets without a clean primitive starting population?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T21:19:25+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/fu_2025_scrl_utilizing_reinforcement_learning_to.pdf -o /tmp/odl-check-scrl -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/fu_2025_scrl_utilizing_reinforcement_learning_to/opendataloader-run.json](../../raw/derived/opendataloader/fu_2025_scrl_utilizing_reinforcement_learning_to/opendataloader-run.json)
- Output: [raw/derived/opendataloader/fu_2025_scrl_utilizing_reinforcement_learning_to/fu_2025_scrl_utilizing_reinforcement_learning_to.md](../../raw/derived/opendataloader/fu_2025_scrl_utilizing_reinforcement_learning_to/fu_2025_scrl_utilizing_reinforcement_learning_to.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->

## Open Questions

- Pending ingest.
