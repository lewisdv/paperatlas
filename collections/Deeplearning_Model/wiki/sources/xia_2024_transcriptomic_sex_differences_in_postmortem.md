---
title: Transcriptomic sex differences in postmortem brain samples from patients with psychiatric disorders
kind: paper
status: ingested
added: 2026-04-29T22:36:05+09:00
raw_source: raw/sources/xia_2024_transcriptomic_sex_differences_in_postmortem.pdf
---

# Transcriptomic sex differences in postmortem brain samples from patients with psychiatric disorders

## Source

- File: [raw/sources/xia_2024_transcriptomic_sex_differences_in_postmortem.pdf](../../raw/sources/xia_2024_transcriptomic_sex_differences_in_postmortem.pdf)
- Added: 2026-04-29T22:36:05+09:00
- Venue/status: Science Translational Medicine research article; first released 23 May 2024 and final published 29 May 2024
- Authors: Yan Xia, Cuihua Xia, Yi Jiang, Yu Chen, Jiaqi Zhou, Rujia Dai, Cong Han, Zhongzheng Mao, the PsychENCODE Consortium, Chunyu Liu, and Chao Chen
- DOI: `10.1126/scitranslmed.adh9974`

## Summary

This paper analyzes sex differences in transcriptomic dysfunction across schizophrenia, bipolar disorder, and autism spectrum disorder using postmortem prefrontal cortex data from the PsychENCODE project. The core result is that female case samples show a higher burden of transcriptomic dysregulation than male case samples, measured both by differential-expression magnitude and by coexpression-network connectivity disruption. In this collection, the paper matters less as a model paper than as a heterogeneity reference: it suggests that future disease-oriented or multimodal models may need to preserve sex-stratified burden patterns rather than treating psychiatric transcriptomes as one pooled disease signal.

## Methods

- The study analyzes RNA-seq data from `2160` postmortem prefrontal cortex samples drawn from the `PsychENCODE` project.
- Samples include `928` cases across schizophrenia (`SCZ`), bipolar disorder (`BD`), and autism spectrum disorder (`ASD`), plus `1232` controls.
- The authors perform sex-stratified case-control differential-expression analysis separately for males and females rather than using only pooled disease contrasts.
- They assess transcriptomic burden at both the individual-gene level and the gene-network level using `WGCNA` and module differential connectivity analyses.
- Down-sampling is used to partially address sex-imbalance concerns, and single-cell RNA-seq references are used for cell-type enrichment of coexpression modules.

## Key Claims

- Female brain samples from patients with SCZ, BD, and ASD show a higher burden of transcriptomic dysfunction than male samples from patients with the same disorders.
- The burden difference appears not only in the number and magnitude of differentially expressed genes but also in network-level connectivity changes.
- Immune-related and synaptic pathways help explain part of the observed sex-biased burden pattern.
- Psychiatric transcriptomic pathology may therefore need sex-stratified interpretation rather than one shared disease signature.

## Evidence

- The dataset includes `2160` postmortem samples, with `928` psychiatric cases and `1232` controls.
- Female-to-male effect-size slopes for case-control transcriptomic changes are reported as `1.7` for SCZ, `1.7` for BD, and `8.3` for ASD.
- Connectivity-change slopes are also larger in females, reported as `2.1` for SCZ, `5.1` for BD, and `18` for ASD.
- The analysis highlights hub or burden-related genes and modules involving immune and synaptic functions, including genes such as `SCN2A`, `FGF14`, and `C3`.
- The workflow retains `25,774` genes after quality control and uses both differential-expression and coexpression analyses to argue that the sex difference is system-level rather than a single-metric artifact.

## Limitations

- The study is based on postmortem adult prefrontal cortex tissue and does not provide longitudinal or causal evidence about how the burden differences arise.
- It relies on bulk transcriptomic samples, so cell-type-composition effects and cell-state resolution remain limited compared with single-cell designs.
- Female sample sizes are smaller for some disorders, especially ASD, which makes some burden estimates more fragile despite down-sampling checks.
- The work is focused on psychiatric disease heterogeneity, not on developing a transferable deep model or perturbation predictor.
- In this collection, the paper is best treated as a heterogeneity benchmark or reference signal rather than as a model architecture contribution.

## Related Pages

- [Sex-Stratified Transcriptomic Burden](../concepts/sex-stratified-transcriptomic-burden.md)

## Open Questions

- Could future psychiatric or multimodal foundation models preserve these sex-stratified burden asymmetries without explicitly training separate models by sex?
- How much of the observed burden signal reflects cell-type composition versus within-cell-type dysregulation that only single-cell designs could resolve?
- If more psychiatric transcriptomic sources are added, should the collection maintain a separate heterogeneity thread distinct from the main generative-model thread?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T22:34:57+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/xia_2024_transcriptomic_sex_differences_in_postmortem.pdf -o /tmp/odl-check-xia -f json,markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/xia_2024_transcriptomic_sex_differences_in_postmortem/opendataloader-run.json](../../raw/derived/opendataloader/xia_2024_transcriptomic_sex_differences_in_postmortem/opendataloader-run.json)
- Output (markdown): [raw/derived/opendataloader/xia_2024_transcriptomic_sex_differences_in_postmortem/xia_2024_transcriptomic_sex_differences_in_postmortem.md](../../raw/derived/opendataloader/xia_2024_transcriptomic_sex_differences_in_postmortem/xia_2024_transcriptomic_sex_differences_in_postmortem.md)
- Output (json): [raw/derived/opendataloader/xia_2024_transcriptomic_sex_differences_in_postmortem/xia_2024_transcriptomic_sex_differences_in_postmortem.json](../../raw/derived/opendataloader/xia_2024_transcriptomic_sex_differences_in_postmortem/xia_2024_transcriptomic_sex_differences_in_postmortem.json)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->

## Open Questions

- Pending ingest.
