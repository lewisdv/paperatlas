---
title: Automated detection and growth tracking of 3D bio-printed organoid clusters using optical coherence tomography with deep convolutional neural networks
kind: paper
status: ingested
added: 2026-04-21T15:48:22+09:00
raw_source: raw/sources/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10130530/
published_date: 2023-01-01
organ: tumor
protocol_focus: automated detection and growth tracking of 3D bio-printed organoid clusters using optical coherence tomography with deep convolutional neural networks
deep_ingested: 2026-04-22
---

# Automated detection and growth tracking of 3D bio-printed organoid clusters using optical coherence tomography with deep convolutional neural networks

## Source

- PDF: [raw/sources/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.pdf](../../raw/sources/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC10130530/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10130530/)
- Status: deep ingested 2026-04-22
- Organ focus: printed patient-derived tumor organoid clusters from liver, gastric, and intestinal cancers rather than a single organ-specific system
- Protocol focus: combine dot-extrusion bioprinting, OCT, and multiscale CNN segmentation to track cavity formation, fusion, and size-dependent growth in printed organoid microbeads

## Study design

- Starting material: 52 printed microbead samples containing patient-derived liver, gastric, or intestinal cancer organoids embedded in Matrigel-rich bioink
- Protocol stages:
  - digest patient tumor material, suspend cells in DMEM/F12 plus 10% FBS and 1% penicillin-streptomycin, mix with Matrigel at 1:2 to form a printable bioink, and deposit dot-extrusion microbeads
  - image the printed microbeads with an inverted OCT system to obtain label-free 3D volumes that capture organoid cores, cavities, and surrounding matrix
  - segment the printable microbead region of interest with a VGG-U-Net step, then identify organoids with the multiscale EGO-Net model
  - improve 3D continuity by averaging orthogonal predictions and track organoid number, equivalent diameter, volume, cavity dynamics, and printing-position errors over 7 days
- Key validation: the pipeline uses 32 um as the lower biologically relevant bound, improves recognition of the more actionable >=50 um organoids, reports 83.9% segmentation accuracy in the 50-90 um range, and captures scale-dependent phenomena including cavity loss, cavity regrowth, fusion, and size oscillations
- Distinct protocol emphasis: this paper ties organoid manufacturing and organoid analysis together, so imaging is not just an endpoint readout but part of automated bioprinted-culture quality control

## Key findings

- Shows that OCT plus CNN analysis can monitor organoid development inside printed microbeads without destructive staining, which is valuable for scaling tumor-organoid preparation.
- Makes organoid size an explicit analytical axis: >=50 um organoids are treated as biologically more informative, and growth behavior differs substantially by starting size and cancer type.
- Uses orthogonal continuous prediction to repair common 2D segmentation discontinuities that otherwise distort 3D reconstruction.

## Distinctive contribution in this corpus

- One of the strongest automation-facing papers in the collection because it integrates bioprinting, image segmentation, and growth analytics in one workflow.
- Gives the engineering concept page a multiscale tumor-organoid tracking system that is less about biology-specific markers and more about process observability.
- Useful as a bridge between organoid manufacture and screening triage, especially when printed culture position and microbead geometry matter.

## Limitations and caveats

- Small organoids remain the weak point: objects below 50 um are the hardest to segment and track, and those below 32 um are excluded from the main analysis.
- The analysis is tightly coupled to printed microbead geometry and OCT image characteristics, so transfer to non-printed cultures or different imaging hardware will require retuning.
- Tracking errors inherit segmentation errors, especially when small organoids later grow across the chosen size thresholds.

## Relevance to corpus

- Strengthens the engineering-imaging branch with a direct example of label-free, high-throughput monitoring for patient-derived tumor organoid production.
- Useful when the experimental bottleneck is deciding which printed organoids are large enough, stable enough, or structurally mature enough for later drug assays.
- Complements later tracking and morphology papers by showing how multiscale OCT analysis can begin at the preparation stage rather than only once organoids are already mature.

## Related concepts

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)

## Related sources

- [Segmentation and Multi-Timepoint Tracking of 3D Cancer Organoids from Optical Coherence Tomography Images Using Deep Neural Networks](f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.md) - a later OCT tracking paper that uses a cleaner train-validation-test split and a longer 13-day window.
- [A Convexity-Preserving Level-Set Method for the Segmentation of Tumor Organoids](x_2024_a-convexity-preserving-level-set-method-for-the-segmentation-of-tumor-organoids.md) - a small-data segmentation comparator that trades deep-learning throughput for interpretable single-organoid precision.
- [Shape Factor Analysis as a Quantitative Framework for Assessing Spheroid and Organoid Morphology and Invasiveness](shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.md) - a downstream morphology-phenotyping framework that could sit on top of automated ROI generation like the one developed here.

## Open questions

- How much of the remaining error comes from OCT acquisition quality versus the segmentation architecture itself?
- Can the microbead-position calibration layer be coupled directly to a closed-loop bioprinting workflow?
- What is the best way to connect the observed size classes and cavity dynamics to later drug-response outcomes?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T15:48:29+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical -f json,markdown`
- Manifest: [raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/opendataloader-run.json](../../raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/opendataloader-run.json)
- Output: [raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.json](../../raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.json)
- Output: [raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.md](../../raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.md)
- Output: [raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile1.png](../../raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile1.png)
- Output: [raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile2.png](../../raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile2.png)
- Output: [raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile3.png](../../raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile3.png)
- Output: [raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile4.png](../../raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile4.png)
- Output: [raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile5.png](../../raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile5.png)
- Output: [raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile6.png](../../raw/derived/opendataloader/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical_images/imageFile6.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
