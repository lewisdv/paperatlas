---
title: A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response
kind: paper
status: ingested
added: 2026-04-29T10:28:05+09:00
raw_source: raw/sources/chen_2026_a_generative_ai_framework_unifies.pdf
---

# A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response

## Source

- File: [raw/sources/chen_2026_a_generative_ai_framework_unifies.pdf](../../raw/sources/chen_2026_a_generative_ai_framework_unifies.pdf)
- Added: 2026-04-29T10:28:05+09:00
- Venue/status: Cell Metabolism 38 (June 2, 2026)
- Authors: Jiawei Chen, Ya Ren, Yong Zhou, Ziyang Wang, Kehang Mao, Zhengqing Yu, Jiyang Li, Xiaoxiao Guo, Hao Xu, Yiyang Wang, Yi Wang, Bo Pang, Hongxiao Liu, Huiru Tang, Jing-Dong J. Han
- DOI: `10.1016/j.cmet.2026.03.014`

## Summary

This paper introduces AURORA, a generative deep-learning framework for unifying fragmented human multi-omics and phenotypic data into a shared latent representation. The system integrates seven modalities across a very large cohort and then uses that representation to reconstruct missing modalities, build multimodal aging clocks and disease risk predictors, and simulate lifestyle or drug perturbations. The paper positions AURORA as a route from sparse, partially observed measurements toward individualized digital human models and intervention-aware multimodal reports.

## Methods

- AURORA Unification separates each modality into discrete feature terms and continuous values, learns feature embeddings with multi-head self-attention, and encodes modality-specific values into low-dimensional sample embeddings.
- A modality classifier adversarially aligns sample embeddings across modalities, while one latent dimension is explicitly disentangled to represent age and the remaining dimensions capture age-confounding biological variation.
- A decoder reconstructs modality values from the interaction between unified sample embeddings and feature embeddings.
- AURORA Perturbation estimates intervention effects with ridge coefficients in latent space, adds those effects to a reference embedding, and decodes the perturbed profile to simulate lifestyle, medication, or other conditional changes.
- The paper also presents an AURORA Agent proof of concept that combines the biological model with LLM-style natural-language interfaces for user-facing multimodal reports.

## Key Claims

- AURORA can harmonize batch effects and infer missing modalities across heterogeneous human datasets well enough to support unified aging and disease modeling.
- Generated multimodal profiles can outperform real-data-only baselines for aging clocks and chronic disease prediction.
- Latent-space perturbation can recover meaningful lifestyle and pharmacological effects, including person-specific treatment-response stratification.
- Sparse inputs such as facial images or routine blood tests can be expanded into richer multimodal health representations.

## Evidence

- Data scale: the paper reports seven modalities across 581,763 samples from 425,258 individuals, with a generalized multi-modality aging atlas spanning China cohorts, GTEx blood transcriptomes, and UK Biobank metabolome/physiome data.
- Cross-modality generation: AURORA reports robust alignment across modalities, batches, races, platforms, and sexes, and still maintains useful performance when trained on only 40% of the training data.
- Aging clocks: the latent-embedding clock is reported as the strongest model, with `PCC = 0.957` and `MAD = 2.493` years on training data and `PCC = 0.713` and `MAD = 7.363` on validation data.
- UKB physiome improvement: the paper reports that generated-data clocks improve the UKB physiome-only aging clock from `PCC 0.497` to `0.799` and reduce `MAD` from `5.842` to `4.915` years.
- China-cohort disease prediction: age-confounding embeddings yield the best chronic-disease classifiers, with `AUC = 0.79-0.88` in training and `0.64-0.82` in validation.
- UKB disease prediction: AURORA increases predictable non-cancer diseases with `AUC > 0.7` from `29` to `96` and predictable cancers from `3` to `17`; example gains include heart failure/pulmonary edema `0.67 -> 0.84` and stroke `0.74 -> 0.84`.
- Drug-response simulation: predicted versus observed longitudinal medication effects show a reported median correlation of about `0.45`, and the paper highlights responder/non-responder biomarker differences for metformin and insulin-based therapy.
- Personalized anti-aging claims: the paper reports that metformin is predicted to reduce aging for `84.92%` of individuals, with the remaining `15.08%` predicted to show the opposite direction.

## Limitations

- The paper explicitly states that flawless high-fidelity molecular reconstruction from sparse single-modal inputs remains aspirational rather than solved.
- The source states that comprehensive paired multi-omic measurements are still needed as ground truth for model training and biological coverage.
- The source also notes that prospective validation across diverse populations and experimental confirmation of newly suggested treatment strategies are still needed.
- The AURORA Agent is presented only as a proof of concept and is not yet optimized for real-world deployment.

## Related Pages

- [AURORA](../entities/AURORA.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)

## Open Questions

- How well would AURORA generalize when key high-information modalities such as 3D or thermal facial imaging are unavailable in new deployment settings?
- Which parts of the gains come from latent alignment and missing-modality generation versus simply enlarging effective training sets with generated data?
- How reliable are the perturbation outputs for intervention discovery beyond the medication classes and cohorts validated here?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T10:30:58+09:00
- Command: `.venv-opendataloader/bin/opendataloader-pdf raw/sources/chen_2026_a_generative_ai_framework_unifies.pdf -o /tmp/odl-chen -f markdown --use-struct-tree --image-output off -q`
- Manifest: [raw/derived/opendataloader/chen_2026_a_generative_ai_framework_unifies/opendataloader-run.json](../../raw/derived/opendataloader/chen_2026_a_generative_ai_framework_unifies/opendataloader-run.json)
- Output: [raw/derived/opendataloader/chen_2026_a_generative_ai_framework_unifies/chen_2026_a_generative_ai_framework_unifies.md](../../raw/derived/opendataloader/chen_2026_a_generative_ai_framework_unifies/chen_2026_a_generative_ai_framework_unifies.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
