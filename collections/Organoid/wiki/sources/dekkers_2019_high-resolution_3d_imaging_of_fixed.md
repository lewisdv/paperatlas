---
title: High-resolution 3D imaging of ﬁxed and cleared organoids
kind: paper
status: ingested
added: 2026-04-21T14:21:48+09:00
raw_source: raw/sources/dekkers_2019_high-resolution_3d_imaging_of_fixed.pdf
article_url: https://doi.org/10.1038/s41596-019-0160-8
published_date: 
organ: organoid-system
protocol_focus: high-resolution 3D imaging of ﬁxed and cleared organoids
deep_ingested: 2026-04-22
---

# High-resolution 3D imaging of ﬁxed and cleared organoids

## Source

- PDF: [raw/sources/dekkers_2019_high-resolution_3d_imaging_of_fixed.pdf](../../raw/sources/dekkers_2019_high-resolution_3d_imaging_of_fixed.pdf)
- Article: [https://doi.org/10.1038/s41596-019-0160-8](https://doi.org/10.1038/s41596-019-0160-8)
- Status: deep ingested 2026-04-22
- Organ focus: whole-mount organoids from many tissues prepared for volumetric fluorescence imaging and cell-by-cell quantification
- Protocol focus: recover organoids from BME, fix and immunolabel them, clear them with a homemade fructose-glycerol solution, and image them by confocal, multiphoton, or light-sheet microscopy

## Study design

- Starting material: pre-existing organoids grown in BME or Matrigel, typically in the 100 to 500 micrometer size range
- Protocol stages:
  - recover organoids from their 3D matrix using ice-cold recovery solution for about 30 to 60 minutes while preserving morphology
  - fix them with 4% PFA, block, and immunolabel them with sufficiently long antibody incubations for full organoid penetration
  - clear the labeled organoids for about 20 minutes at room temperature in a homemade fructose-glycerol solution instead of harsher tissue-clearing reagents
  - prepare slides or light-sheet capillaries for confocal, multiphoton, super-resolution confocal, or light-sheet imaging depending on the question
  - render and segment 3D datasets with software such as Imaris, with Fiji as a lighter-weight alternative for some steps
- Key validation: the protocol works across colon, airway, liver, kidney, breast tumor, and mouse mammary organoids, improves z-depth fluorescence performance relative to no clearing or FocusClear, and supports cell-by-cell segmentation and marker quantification in intact organoids
- Distinct protocol emphasis: this is a widely reusable whole-mount imaging pipeline designed for small, fragile organoids rather than for large tissue-clearing projects

## Key findings

- Provides a fast, relatively gentle 3D imaging workflow that can be completed in about 3 days rather than the weeks required for many tissue-clearing methods.
- Shows that a simple fructose-glycerol clearing reagent can outperform FocusClear on signal preservation by avoiding fluorescence quenching while still improving depth penetration.
- Makes whole-organoid architecture quantifiable, not just visible, by coupling the imaging workflow to nuclear segmentation and per-cell marker readouts.
- Clarifies when not to clear: large cystic organoids can shrink or distort, in which case multiphoton imaging without clearing is often the better choice.

## Distinctive contribution in this corpus

- Probably the most generally reusable microscopy-preparation page in the current collection.
- Gives the engineering and imaging concept layer a broadly applicable whole-mount fluorescence standard that complements more specialized readouts such as MSI or viral microinjection.
- Helps the corpus distinguish "section-based snapshots" from true volumetric organoid analysis.

## Limitations and caveats

- Large cystic organoids can shrink during clearing and may need multiphoton imaging without clearing.
- The protocol is operationally simple but still requires careful handling to avoid organoid loss during recovery, washing, and mounting.
- Full-value use often depends on commercial 3D-analysis software such as Imaris, although some steps can be reproduced in Fiji.
- Light-sheet imaging is faster for large datasets but trades away some subcellular resolution and is sensitive to bubbles or debris in the optical path.

## Relevance to corpus

- Strengthens the engineering and imaging branch with a foundational whole-mount readout protocol.
- Useful whenever a project needs intact 3D architecture, cellular composition, reporter retention, or volumetric quantification rather than thin-section snapshots.
- Serves as a practical first-choice imaging workflow before escalating to more specialized or destructive spatial readouts.

## Related concepts

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Related entities

- [Whole-mount 3D clearing and imaging](../entities/whole-mount-3d-clearing-and-imaging.md)

## Related sources

- [Preparing ductal epithelial organoids for high-spatial-resolution molecular proﬁling using mass spectrometry imaging](bakker_2022_preparing_ductal_epithelial_organoids_for.md) - another high-value readout-preparation paper, but one focused on spatial chemistry rather than fluorescence architecture.
- [Protocol for differentiating human pluripotent stem cells into midbrain organoids for targeted microinjection of viruses](m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.md) - a brain assay paper where improved whole-mount imaging becomes important after targeted perturbation.
- [Automated detection and growth tracking of 3D bio-printed organoid clusters using optical coherence tomography with deep convolutional neural networks](d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.md) - a complementary imaging page centered on automated growth tracking rather than post-fixation whole-mount analysis.

## Open questions

- Which organoid morphologies should be cleared, and which are better imaged uncleared with multiphoton microscopy?
- How much analytical value is lost when labs substitute lighter-weight software for full 3D segmentation suites such as Imaris?
- What should become the default QC panel for cross-lab comparison of whole-mount organoid imaging?
