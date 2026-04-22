---
title: Optical coherence tomography (OCT)
status: active
created: 2026-04-22T19:29:26+09:00
kind: entity
entity_type: imaging-modality
---

# Optical coherence tomography (OCT)

## Current role in this corpus

OCT is the main label-free 3D imaging branch in this collection for longitudinal organoid tracking, especially in tumor-organoid engineering workflows.

## Strong supporting pages

- [Automated detection and growth tracking of 3D bio-printed organoid clusters using optical coherence tomography with deep convolutional neural networks](../sources/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.md)
- [Segmentation and Multi-Timepoint Tracking of 3D Cancer Organoids from Optical Coherence Tomography Images Using Deep Neural Networks](../sources/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.md)
- [Shape Factor Analysis as a Quantitative Framework for Assessing Spheroid and Organoid Morphology and Invasiveness](../sources/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Working synthesis

- OCT in this corpus is valuable because it keeps organoids observable over time without destructive staining.
- The engineering branch uses it for more than image capture: segmentation models, tracking logic, growth classes, cavity dynamics, and morphology summaries all depend on OCT volumes.
- OCT therefore belongs to the readout-infrastructure layer of the corpus, especially when the bottleneck is monitoring quality, size change, or structural evolution during culture.

## Main tension

- label-free longitudinal visibility versus hardware-specific pipelines and segmentation dependence
- high-throughput observability versus transfer difficulty across culture formats and instruments

## Related concepts

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)

## Open questions

- Which OCT-derived features are most predictive of later assay usefulness?
- How well do OCT-tracking pipelines transfer across printed and non-printed organoid systems?
- When should a project stop improving segmentation and instead simplify the morphology question?
