---
title: "Generation of complex human organoid models including vascular networks by incorporation of mesodermal progenitor cells"
kind: paper
status: ingested
added: 2026-04-09T17:00:00+09:00
raw_source: raw/sources/worsdorfer_2019_generation_of_complex_human_organoid.pdf
article_url: https://www.nature.com/articles/s41598-019-52204-7
published_date: 2019-10-31
organ: multi-lineage + vascular
protocol_focus: MPC incorporation strategy for vascularizing tumor and neural organoids
deep_ingested: 2026-04-09
---

# Generation of complex human organoid models including vascular networks by incorporation of mesodermal progenitor cells

## Source

- PDF: [raw/sources/worsdorfer_2019_generation_of_complex_human_organoid.pdf](../../raw/sources/worsdorfer_2019_generation_of_complex_human_organoid.pdf)
- Article: [Scientific Reports](https://www.nature.com/articles/s41598-019-52204-7)
- Lab: Süleyman Ergün (University of Würzburg, Institute of Anatomy and Cell Biology)
- Status: deep ingested 2026-04-09

## Study design

- Starting material: human iPSCs
- Approach: differentiate iPSCs into **Brachyury+ mesodermal progenitor cells (MPCs)** via CHIR99021 (WNT) + BMP4, then mix MPCs with either neural spheroids or tumor cells to generate vascularized organoids.
- MPC induction validation: >80% Brachyury+ at day 2; treatment with PDGF or VEGF yields SMC or EC fates respectively.
- Organoid models tested:
  - Vascularized tumor organoids (MPCs + GFP-labeled MDA-MB-435s tumor cells, 1:1 ratio)
  - Vascularized neural organoids
- Culture conditions tested: normoxic (20% O₂) vs hypoxic (2% O₂)
- In vivo validation: transplantation onto chicken CAM (chorion allantois membrane) and mouse host

## Key findings

- MPCs delivered into organoids generate **hierarchically organized blood vessels with endothelial cell-cell junctions, basement membrane, luminal caveolae, and microvesicles** — ultrastructural vessel features, not just "cords."
- Mural cells (αSMA+) are assembled into the vessel wall, indicating true vessel architecture.
- **High plasticity**: vascular network responds to anti-angiogenic drugs (17-AAG, Sorafenib) and pro-angiogenic conditions (hypoxia).
- **Vessels connect to host circulation after transplantation** — functional integration.
- Remarkably, **MPCs also deliver Iba1+ microglia-like cells** into neural organoids, adding a tissue-resident immune cell component.
- Applicable across organoid types (demonstrated in tumor and neural organoids).

## Distinctive contribution in this corpus

- **General-purpose vascularization strategy**, not organ-specific.
- Only entry in corpus that explicitly delivers both vasculature AND microglia-like immune cells in a single system.
- Complements Cakir 2019 (TF-based brain vascularization) and Homan 2019 (flow-based kidney vascularization) with a cell-mixing approach.
- Cheaper and more scalable than microfluidic chip approaches.

## Limitations and caveats

- Mesodermal progenitor definition is broad — downstream specification may not be controllable.
- Tumor organoid context is a simplified model.
- Vessel network formation depends on hypoxic signaling (not always physiological).
- Hierarchical vessel organization does not yet reach capillary bed complexity.

## Relevance to corpus

- Belongs to the vascularization cluster with Wimmer 2019, Cakir 2019, Homan 2019.
- Provides a unique insight: **MPCs can be a single source for both vasculature and microglia-like cells**, relevant to multi-lineage complexity questions.

## Related concepts

- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related sources

- [Wimmer 2019](wimmer_2019_generation_of_blood_vessel_organoids.md), [Cakir 2019](cakir_2019_engineering_of_human_brain.md), [Homan 2019](homan_2019_flow-enhanced_vascularization_and_maturation.md) — vascularization cluster.
- [Pereira 2021](pereira_2021_human_sensorimotor_organoids_derived.md) — another NMP/MPC-based co-development strategy.
- [Cattaneo 2019](cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md), [Driehuis 2020](driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) — tumor organoid context for which vascularization is most needed.

## Open questions

- Is the microglia-like cell yield reproducible?
- Can MPCs deliver other tissue-resident immune cells (T cells, macrophages)?
- What is the upper limit of organoid size achievable with MPC-mediated vascularization?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-12T12:46:44+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/worsdorfer_2019_generation_of_complex_human_organoid.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid -f json,markdown`
- Manifest: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/opendataloader-run.json](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/opendataloader-run.json)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid.json](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid.json)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid.md](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid.md)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile1.png](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile1.png)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile2.png](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile2.png)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile3.png](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile3.png)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile4.png](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile4.png)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile5.png](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile5.png)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile6.png](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile6.png)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile7.png](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile7.png)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile8.png](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile8.png)
- Output: [raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile9.png](../../raw/derived/opendataloader/worsdorfer_2019_generation_of_complex_human_organoid/worsdorfer_2019_generation_of_complex_human_organoid_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
