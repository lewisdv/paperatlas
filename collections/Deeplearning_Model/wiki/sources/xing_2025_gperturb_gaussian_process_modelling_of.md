---
title: GPerturb: Gaussian process modelling of single-cell perturbation data
kind: paper
status: ingested
added: 2026-04-29T22:01:57+09:00
raw_source: raw/sources/xing_2025_gperturb_gaussian_process_modelling_of.pdf
---

# GPerturb: Gaussian process modelling of single-cell perturbation data

## Source

- File: [raw/sources/xing_2025_gperturb_gaussian_process_modelling_of.pdf](../../raw/sources/xing_2025_gperturb_gaussian_process_modelling_of.pdf)
- Added: 2026-04-29T22:01:57+09:00
- Venue/status: Nature Communications article; accepted 11 June 2025, with the extracted PDF showing the article DOI but not a separate online-publication date line
- Authors: Hanwen Xing and Christopher Yau
- DOI: `10.1038/s41467-025-61165-7`

## Summary

This paper introduces GPerturb, a sparse additive perturbation-regression model built from hierarchical Bayesian modeling and Gaussian processes rather than deep latent embeddings. GPerturb directly estimates gene-level perturbation effects, supports both count-based and continuous expression inputs, and provides uncertainty estimates for effect presence and strength. In this collection, the paper matters because it shows that competitive perturbation modeling does not have to rely on foundation models or neural latent spaces; a more classical probabilistic model can remain competitive while staying comparatively interpretable.

## Methods

- GPerturb decomposes each observed expression value into a basal cell-state component plus an additive perturbation-effect component.
- Both components are modeled with feature-specific nonlinear Gaussian processes, and sparsity is enforced through binary on/off switches controlling whether each perturbation affects each gene.
- The framework supports two observation models: `GPerturb-Gaussian` for continuous transformed expression and `GPerturb-ZIP` for zero-inflated Poisson count data.
- The model is supervised and directly predicts gene-level perturbation effects without learning a low-dimensional latent perturbation embedding.
- For dosage-based perturbations, the paper additionally analyzes derivatives of perturbation-effect curves to identify dosage-sensitive genes and non-monotonic response patterns.

## Key Claims

- A sparse additive Gaussian-process model can achieve predictive performance comparable to or better than several popular deep perturbation models while remaining more interpretable at the gene-effect level.
- Modeling choices about preprocessing and observation model are not cosmetic; they can materially change inferred perturbation effects even when predictive correlations stay high.
- GPerturb is flexible enough to handle binary perturbations, multigene perturbations, and continuous dosage settings inside one probabilistic framework.
- Foundation-model-style approaches are promising, but their benefits for perturbation prediction remain unclear enough that strong classical baselines are still valuable.

## Evidence

- On a single-gene Perturb-seq benchmark, the paper reports Pearson correlations of `0.972` for `GPerturb-ZIP` versus `0.944` for SAMS-VAE on count-based inputs, while `GPerturb-Gaussian` reaches `0.981` versus `0.977` for GEARS and `0.984` for CPA-mlp on continuous inputs.
- On multigene perturbation data, GPerturb is reported as comparable to GEARS and stronger than CPA and SAMS-VAE in the two-gene setting, despite not using an external knowledge graph.
- On a highly multiplexed Perturb-seq dataset, GPerturb and GEARS achieve similar average predictive correlation (`0.798` versus `0.802`), but the inferred perturbation-effect scales differ substantially.
- On SciPlex2 dosage experiments, the paper reports that GPerturb outperforms both CPA variants and better captures non-monotonic dose-response patterns.
- The paper repeatedly highlights a methodological warning: directionality agreement between methods can be weak even when overall prediction correlation is high, and switching between Gaussian and ZIP observation models can change inferred biological conclusions on the same raw data.

## Limitations

- Predictive comparisons across perturbation methods are not fully clean because many baselines assume different preprocessing, perturbation encodings, or input modalities.
- The paper shows that GPerturb-Gaussian and GPerturb-ZIP can infer meaningfully different effects from the same underlying dataset, which adds uncertainty to biological interpretation.
- Although competitive, GPerturb is not positioned here as a reusable foundation representation across many downstream tasks.
- The extracted source does not provide a clear separate online-publication date beyond the article DOI and acceptance line.

## Related Pages

- [GPerturb](../entities/GPerturb.md)
- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [GEARS](../entities/GEARS.md)
- [CellOT](../entities/CellOT.md)
- [Tahoe-x1](../entities/Tahoe-x1.md)

## Open Questions

- When should this collection prefer a directly interpretable gene-level perturbation model like GPerturb over larger latent or foundation-model approaches?
- How should method comparisons in this collection account for preprocessing-sensitive differences in inferred effect directionality, not only average prediction correlation?
- If future sources include multi-omics or spatial perturbation models, does GPerturb’s classical structure still scale gracefully or does it become too restrictive?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T22:01:10+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/xing_2025_gperturb_gaussian_process_modelling_of.pdf -o /tmp/odl-check-gperturb -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/xing_2025_gperturb_gaussian_process_modelling_of/opendataloader-run.json](../../raw/derived/opendataloader/xing_2025_gperturb_gaussian_process_modelling_of/opendataloader-run.json)
- Output: [raw/derived/opendataloader/xing_2025_gperturb_gaussian_process_modelling_of/xing_2025_gperturb_gaussian_process_modelling_of.md](../../raw/derived/opendataloader/xing_2025_gperturb_gaussian_process_modelling_of/xing_2025_gperturb_gaussian_process_modelling_of.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
