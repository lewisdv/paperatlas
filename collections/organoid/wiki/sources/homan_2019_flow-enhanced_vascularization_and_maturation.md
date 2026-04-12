---
title: "Flow-enhanced vascularization and maturation of kidney organoids in vitro"
kind: paper
status: ingested
added: 2026-04-09T17:00:00+09:00
raw_source: raw/sources/homan_2019_flow-enhanced_vascularization_and_maturation.pdf
article_url: https://www.nature.com/articles/s41592-019-0325-y
published_date: 2019-03-11
organ: kidney + vascular
protocol_focus: millifluidic chip flow-enhanced kidney organoid maturation
deep_ingested: 2026-04-09
---

# Flow-enhanced vascularization and maturation of kidney organoids in vitro

## Source

- PDF: [raw/sources/homan_2019_flow-enhanced_vascularization_and_maturation.pdf](../../raw/sources/homan_2019_flow-enhanced_vascularization_and_maturation.pdf)
- Article: [Nature Methods](https://www.nature.com/articles/s41592-019-0325-y)
- Labs: Jennifer A. Lewis (Harvard Wyss Institute) + Ryuji Morizane (Brigham and Women's / Harvard Medical)
- Status: deep ingested 2026-04-09

## Study design

- Starting material: hPSC-derived kidney organoids following Morizane 2016 / Takasato 2016-type differentiation
- Device: 3D-printed millifluidic chip with gelatin-fibrin ("gelbrin") ECM coating
- Fluidic shear stress (FSS) tested: low (0.0001 dyn/cm²) to high (0.008-0.035 dyn/cm²)
- Media optimization: low FBS (1.5%) permits both nephrogenesis and vascular network formation
- Timepoints: days 12-35 of differentiation with 10 days perfusion
- Readouts: PECAM1/MCAM immunostaining, AngioTool vessel quantification, podocyte markers, nephron maturation scRNA-seq, VEGF gradient disruption experiments

## Key findings

- **5× increase in PECAM1+ vessel area under high FSS** vs. low FSS.
- Developing kidney organoids exposed to flow show:
  - **Expanded endogenous endothelial progenitor pool**
  - **Perfusable vascular networks with luminal architecture** surrounded by mural cells
  - **Enhanced cellular polarity in podocytes and tubular compartments**
  - **More mature adult gene expression** in both vascular and tubular cells
- Glomerular vascular development progresses through intermediate stages **resembling embryonic capillary loop formation abutting foot processes**.
- VEGF gradient disruption reduces vessel-nephron association — confirming endogenous signaling axis.
- Gelbrin ECM (vs. glass, plastic, fibrin alone) critical for peripheral PECAM1 expression.

## Distinctive contribution in this corpus

- **First organ-on-chip / microfluidic paper in the collection** — fills a major gap.
- Solves a specific, well-known problem: static kidney organoids are avascular and immature.
- Alternative to in vivo transplantation for kidney organoid vascularization.
- Bridges the "static culture" bulk of the kidney organoid literature (Xia, Takasato, Morizane, Vanslambrouck) with organ-on-chip maturation.

## Limitations and caveats

- Requires custom 3D-printed millifluidic device — not all labs can adopt.
- Vessel maturation is improved but still not equivalent to adult kidney.
- 10-day perfusion is short relative to the months-long kidney organoid differentiation.
- "Flow over top" is not physiological perfusion through lumens.

## Relevance to corpus

- Direct extension of Morizane 2016 / Takasato 2016 kidney organoid work.
- Pairs with Wimmer 2019 (stand-alone vessels), Cakir 2019 (brain vascularization), Wörsdorfer 2019 (MPC mixing) to form the organoid vascularization cluster.
- First concrete demonstration that mechanical (flow) stimulation can substitute for in vivo niche in organoid maturation.

## Related concepts

- [Kidney organoid differentiation routes](../concepts/kidney-organoid-differentiation-routes.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)

## Related sources

- [Morizane 2016](morizane_2016_generation_of_nephron_progenitor_cells.md) — base kidney organoid protocol this builds on.
- [Takasato 2016](takasato_2016_generation_of_kidney_organoids_from.md) — alternative kidney baseline.
- [Vanslambrouck 2023](vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney.md) — recent proximal-tubule-enhanced variant.
- [Wimmer 2019](wimmer_2019_generation_of_blood_vessel_organoids.md), [Cakir 2019](cakir_2019_engineering_of_human_brain.md), [Wörsdorfer 2019](worsdorfer_2019_generation_of_complex_human_organoid.md) — vascularization cluster.

## Open questions

- Does flow-enhanced maturation transfer to other organoid systems (lung, intestine)?
- What is the maximum maturation achievable with longer perfusion (weeks-months)?
- How does flow-driven vs. TF-driven (Cakir) vs. cell-mixing (Wörsdorfer) vascularization compare on fidelity and throughput?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-12T12:42:23+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/homan_2019_flow-enhanced_vascularization_and_maturation.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation -f json,markdown`
- Manifest: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/opendataloader-run.json](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/opendataloader-run.json)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation.json](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation.json)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation.md](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile1.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile1.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile10.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile10.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile11.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile11.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile12.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile12.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile13.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile13.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile14.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile14.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile15.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile15.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile16.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile16.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile17.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile17.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile18.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile18.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile19.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile19.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile2.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile2.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile20.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile20.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile21.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile21.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile22.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile22.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile23.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile23.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile24.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile24.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile25.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile25.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile26.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile26.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile27.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile27.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile28.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile28.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile29.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile29.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile3.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile3.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile30.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile30.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile31.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile31.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile32.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile32.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile33.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile33.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile34.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile34.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile35.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile35.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile4.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile4.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile5.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile5.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile6.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile6.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile7.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile7.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile8.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile8.png)
- Output: [raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile9.png](../../raw/derived/opendataloader/homan_2019_flow-enhanced_vascularization_and_maturation/homan_2019_flow-enhanced_vascularization_and_maturation_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
