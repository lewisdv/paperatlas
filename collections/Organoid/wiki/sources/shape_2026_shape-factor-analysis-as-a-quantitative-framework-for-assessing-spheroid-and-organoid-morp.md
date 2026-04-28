---
title: Shape Factor Analysis as a Quantitative Framework for Assessing Spheroid and Organoid Morphology and Invasiveness
kind: paper
status: ingested
added: 2026-04-21T14:26:23+09:00
raw_source: raw/sources/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13060997/
published_date: 2026-03-12
organ: organoid-system
protocol_focus: shape Factor Analysis as a Quantitative Framework for Assessing Spheroid and Organoid Morphology and Invasiveness
deep_ingested: 2026-04-22
---

# Shape Factor Analysis as a Quantitative Framework for Assessing Spheroid and Organoid Morphology and Invasiveness

## Source

- PDF: [raw/sources/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.pdf](../../raw/sources/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC13060997/](https://pmc.ncbi.nlm.nih.gov/articles/PMC13060997/)
- Status: deep ingested 2026-04-22
- Organ focus: cross-system morphology analysis spanning breast-cancer spheroids, reproductive-tract organoids, and low-resolution screening images
- Protocol focus: generate FIJI ROIs, quantify standard and custom shape descriptors, and add MATLAB-based radial length metrics to classify invasion and irregular morphology

## Study design

- Starting material: digital phantoms, breast cancer spheroids, endometrial and oviductal organoids, and collagen-embedded coculture spheroids collected by bright-field, confocal, or optical coherence microscopy
- Protocol stages:
  - generate or segment ROIs in FIJI from low-resolution bright-field images, confocal projections, OCT-derived images, or histologic sections
  - quantify standard FIJI descriptors such as circularity, solidity, roundness, and aspect ratio, and add convexity through a custom FIJI macro
  - import FIJI ROIs into a custom MATLAB workflow to compute radial-length-based metrics including standard deviation of radial lengths and average radial length crossings
  - compare the different metrics on digital phantoms and experimental models to identify which descriptors best capture invasion, protrusions, folds, or elongation
- Key validation: circularity and convexity best captured irregular or invasive protrusive morphologies, roundness mainly reported elongation, and radial length analysis added sensitivity to collective radial invasion that standard shape factors often miss
- Distinct protocol emphasis: this is a morphology-phenotyping framework rather than a segmentation paper, and its central message is that organoid shape readouts must be chosen by biologic question rather than by convenience

## Key findings

- Argues convincingly that no single descriptor is enough: circularity and convexity report protrusions or folds, roundness reports elongation, and radial-length analysis is best for collective radial invasion.
- Keeps the workflow accessible by building on FIJI plus MATLAB rather than requiring specialized machine-learning infrastructure.
- Makes morphology more comparable across imaging modalities and experimental systems, which is valuable for screening and phenotypic profiling.

## Distinctive contribution in this corpus

- One of the strongest cross-platform quantification papers in the collection because it translates visual organoid phenotypes into interpretable descriptor choices.
- Extends the engineering branch beyond segmentation into the harder question of what morphology metrics actually mean biologically.
- Useful as a synthesis anchor for imaging papers that produce masks or contours but do not by themselves explain which summary metrics matter.

## Limitations and caveats

- The workflow still depends on upstream ROI quality, and some use cases rely on manual tracing or thresholding rather than fully automated segmentation.
- Radial-length analysis is tuned for collective radial invasion and is less suitable for single-cell-dominant invasion or strongly non-spheroidal systems.
- Descriptor interpretation remains context dependent; a decrease in circularity or convexity can reflect biologically different processes in different models.

## Relevance to corpus

- Strengthens the engineering-imaging branch with a practical framework for turning segmented organoid outlines into screening-relevant phenotype scores.
- Useful when the problem is not obtaining an image, but deciding which morphology measurement actually corresponds to invasion, roughness, or elongation.
- Pairs naturally with OCT and segmentation papers that generate masks but need a principled downstream readout.

## Related concepts

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Related entities

- [Optical coherence tomography (OCT)](../entities/optical-coherence-tomography-oct.md)
- [Morphology segmentation and descriptor analysis](../entities/morphology-segmentation-and-descriptor-analysis.md)

## Related sources

- [A Convexity-Preserving Level-Set Method for the Segmentation of Tumor Organoids](x_2024_a-convexity-preserving-level-set-method-for-the-segmentation-of-tumor-organoids.md) - a precise ROI-generation method that could feed directly into descriptor analysis like the one used here.
- [Segmentation and Multi-Timepoint Tracking of 3D Cancer Organoids from Optical Coherence Tomography Images Using Deep Neural Networks](f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.md) - a longitudinal OCT pipeline whose masks and time series become much more informative when paired with better morphology descriptors.
- [Automated detection and growth tracking of 3D bio-printed organoid clusters using optical coherence tomography with deep convolutional neural networks](d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.md) - another readout-layer paper that could use shape-factor analysis to summarize the structures it segments and tracks.

## Open questions

- Which combinations of descriptors are most robust across organoid types and imaging modalities?
- How much manual ROI curation can be removed before descriptor quality starts to drift?
- Can radial-length metrics be adapted for fused organoids or single-cell invasion without losing interpretability?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:50:32+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp -f json,markdown`
- Manifest: [raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/opendataloader-run.json](../../raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/opendataloader-run.json)
- Output: [raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.json](../../raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.json)
- Output: [raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.md](../../raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.md)
- Output: [raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile1.png](../../raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile1.png)
- Output: [raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile2.png](../../raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile2.png)
- Output: [raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile3.png](../../raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile3.png)
- Output: [raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile4.png](../../raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile4.png)
- Output: [raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile5.png](../../raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile5.png)
- Output: [raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile6.png](../../raw/derived/opendataloader/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp_images/imageFile6.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
