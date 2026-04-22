---
title: Segmentation and Multi-Timepoint Tracking of 3D Cancer Organoids from Optical Coherence Tomography Images Using Deep Neural Networks
kind: paper
status: ingested
added: 2026-04-21T14:26:30+09:00
raw_source: raw/sources/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11203156/
published_date: 2024-06-01
organ: breast
protocol_focus: segmentation and Multi-Timepoint Tracking of 3D Cancer Organoids from Optical Coherence Tomography Images Using Deep Neural Networks
deep_ingested: 2026-04-22
---

# Segmentation and Multi-Timepoint Tracking of 3D Cancer Organoids from Optical Coherence Tomography Images Using Deep Neural Networks

## Source

- PDF: [raw/sources/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.pdf](../../raw/sources/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11203156/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11203156/)
- Status: deep ingested 2026-04-22
- Organ focus: murine BRCA1-deficient breast cancer organoids imaged longitudinally by OCT
- Protocol focus: use K-Net plus Swin Transformer segmentation and a probability-scored tracking algorithm to follow single cancer organoids over a 13-day OCT time series

## Study design

- Starting material: murine BRCA1-deficient breast cancer organoids seeded from 1000 cells in 50:50 medium and basement membrane extract within 8-well plates
- Protocol stages:
  - establish the breast cancer organoids, then challenge the cultures with 8 uM carboplatin from day 3 for 5 days before returning to standard medium
  - image the cultures on a home-built spectral-domain OCT system across days 1 to 13, generating 698-slice volumes with a 3.0 mm x 1.8 mm field of view
  - preprocess the OCT data with histogram normalization, contrast stretching, square-root noise redistribution, and denoising before 2D slice-based segmentation
  - train a K-Net model with Swin Transformer backbone on days 5 and later, then track organoids across timepoints using centroid distance, volume changes, shape descriptors, and IoU-based probability scoring
- Key validation: the segmentation model achieved a Dice score of 0.726 +/- 0.152 with accuracy 0.996 +/- 0.002, sensitivity 0.740 +/- 0.202, and precision 0.743 +/- 0.132; the optimized tracking configuration used a 30 um centroid threshold and 10% volume tolerance and successfully tracked 142 of 253 reference organoids across the 13-day series
- Distinct protocol emphasis: this is a longitudinal imaging and analytics workflow for treatment-relevant tumor organoids, not a derivation paper, and its main value is consistent non-destructive follow-up over time

## Key findings

- Extends OCT-based organoid tracking from short proof-of-principle windows into a 13-day pipeline with an explicit train-validation-test design.
- Makes the tracking logic biologically informed rather than purely geometric by including allowable volume oscillations and choosing an early reference day before fusion events dominate.
- Demonstrates that relatively fast inference, about 30 s per volume, is compatible with repeated longitudinal analysis.

## Distinctive contribution in this corpus

- One of the clearest examples in the collection where organoid imaging becomes a longitudinal analytics platform rather than a static visualization step.
- Provides a higher-rigor OCT tracking comparator to the earlier bioprinted-cluster paper by separating training, validation, and testing more carefully and by making the tracking criteria explicit.
- Strengthens the breast or tumor branch without needing new wet-lab derivation complexity.

## Limitations and caveats

- The dataset is still small, especially for the earliest stages, and days 1 and 3 were excluded from training because manual annotation of tiny organoids was unreliable.
- Fusion events remain a major problem; even with optimized tracking, only 56% of reference organoids were maintained across the full series.
- The approach is portable in principle, but segmentation and tracking parameters still need tissue- and protocol-specific fine-tuning.

## Relevance to corpus

- Strengthens the engineering-imaging branch with a treatment-aware, non-destructive tumor-organoid monitoring workflow.
- Useful when the project needs quantitative growth trajectories, morphologic evolution, or a possible imaging backbone for drug-response phenotyping.
- Pairs naturally with smaller-data segmentation and morphology-summary papers elsewhere in the collection.

## Related concepts

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Related sources

- [Automated detection and growth tracking of 3D bio-printed organoid clusters using optical coherence tomography with deep convolutional neural networks](d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.md) - an earlier OCT tracking paper that is more tied to bioprinted microbeads and multi-cancer cluster analysis.
- [A Convexity-Preserving Level-Set Method for the Segmentation of Tumor Organoids](x_2024_a-convexity-preserving-level-set-method-for-the-segmentation-of-tumor-organoids.md) - a classical segmentation comparator for situations where training data are too limited for deep learning.
- [Shape Factor Analysis as a Quantitative Framework for Assessing Spheroid and Organoid Morphology and Invasiveness](shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.md) - a morphology-summary framework that could sit on top of tracked masks and volumes like the ones generated here.

## Open questions

- How much better would the system perform with full 3D or instance-segmentation models once fusion becomes common?
- Which imaging-derived features beyond volume and shape are most predictive of drug response in tumor organoids?
- What is the minimum dataset size needed before the same pipeline can generalize across organoid types without heavy retraining?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:48:51+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to -f json,markdown`
- Manifest: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/opendataloader-run.json](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/opendataloader-run.json)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.json](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.json)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.md](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.md)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile1.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile1.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile10.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile10.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile11.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile11.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile12.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile12.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile2.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile2.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile3.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile3.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile4.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile4.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile5.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile5.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile6.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile6.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile7.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile7.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile8.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile8.png)
- Output: [raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile9.png](../../raw/derived/opendataloader/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
