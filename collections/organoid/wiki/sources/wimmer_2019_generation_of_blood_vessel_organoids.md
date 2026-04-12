---
title: "Generation of blood vessel organoids from human pluripotent stem cells"
kind: paper
status: ingested
added: 2026-04-09T15:30:00+09:00
raw_source: raw/sources/wimmer_2019_generation_of_blood_vessel_organoids.pdf
article_url: https://www.nature.com/articles/s41596-019-0213-z
published_date: 2019-09-25
organ: blood vessel
protocol_focus: self-organizing 3D blood vessel organoid with endothelium and pericytes
deep_ingested: 2026-04-09
---

# Generation of blood vessel organoids from human pluripotent stem cells

## Source

- PDF: [raw/sources/wimmer_2019_generation_of_blood_vessel_organoids.pdf](../../raw/sources/wimmer_2019_generation_of_blood_vessel_organoids.pdf)
- Article: [Nature Protocols](https://www.nature.com/articles/s41596-019-0213-z)
- Lab: Josef Penninger (IMBA Vienna / UBC)
- Status: deep ingested 2026-04-09

## Study design

- Starting material: human iPSCs
- Protocol stages (step-by-step):
  - d-1: Aggregate formation, 2×10⁵ cells/mL in low-attachment plate, Y-27632 (ROCKi)
  - d0: Mesoderm induction — CHIR99021 12 µM (WNT) + BMP-4 30 ng/mL
  - d3: Vascular lineage induction — VEGF-A 100 ng/mL + forskolin 2 µM
  - d5: Embedding in collagen I–Matrigel matrix — VEGF-A 100 ng/mL + FGF-2 100 ng/mL + 15% FBS
  - d10: Extract vascular networks for organoid self-assembly (96-well plate)
- Total duration: 2-3 weeks for vessel formation; scalable to suspension culture for long-term
- Key validation: in vitro human blood vessel organoids transplanted into NSG mice integrated with mouse circulation and specified into functional arteries, arterioles, and veins.

## Key findings

- Self-organizing 3D organoids composed of endothelial cells + pericytes + basement membrane.
- Morphological, functional, and molecular features of human microvasculature.
- Blood vessels form within 2-3 weeks; scalable.
- In vivo transplantation → integration with host circulation + specification into arterial/venous identities.
- Used for modeling diabetic vasculopathy.

## Distinctive contribution in this corpus

- **First entry for vascular organoids** — fills a major gap in the collection.
- The gold-standard detailed protocol for blood vessel organoids from hPSCs.
- Provides the baseline that later vascular+organ intersection work (Cakir, Homan, Wörsdorfer) can reference or modify.

## Limitations and caveats

- Does not generate organ-specific vasculature (lung, kidney, brain) — these require organ-specific protocols.
- Requires collagen I–Matrigel matrix (batch variability).
- Vessel organoids are microvessels; larger arteries not formed in vitro.
- In vivo arterial specification requires transplantation.

## Relevance to corpus

- Together with Cakir 2019 (brain+vessel), Homan 2019 (kidney+vessel), and Wörsdorfer 2019 (multi-lineage+vessel) this establishes a four-paper cluster on organoid vascularization.
- Essential baseline for understanding what "vascularized organoid" means across other papers.

## Related concepts

- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related sources

- [Cakir 2019](cakir_2019_engineering_of_human_brain.md) — applies similar logic inside cortical organoids via ETV2.
- [Homan 2019](homan_2019_flow-enhanced_vascularization_and_maturation.md) — adds flow to kidney organoids for vascular maturation.
- [Wörsdorfer 2019](worsdorfer_2019_generation_of_complex_human_organoid.md) — generalizes MPC incorporation strategy to multiple organs.

## Open questions

- How does this protocol compare to organ-specific vascularization (Cakir for brain, Homan for kidney)?
- Can these organoids be vascularized within non-vascular organoids without perturbing the host organoid identity?
- How mature do the vessels become over longer time courses (>3 months)?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-12T12:46:35+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/wimmer_2019_generation_of_blood_vessel_organoids.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids -f json,markdown`
- Manifest: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/opendataloader-run.json](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/opendataloader-run.json)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids.json](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids.json)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids.md](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids.md)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile1.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile1.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile10.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile10.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile11.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile11.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile12.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile12.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile13.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile13.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile14.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile14.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile15.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile15.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile16.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile16.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile17.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile17.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile18.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile18.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile19.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile19.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile2.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile2.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile20.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile20.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile21.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile21.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile22.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile22.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile23.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile23.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile24.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile24.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile25.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile25.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile3.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile3.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile4.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile4.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile5.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile5.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile6.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile6.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile7.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile7.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile8.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile8.png)
- Output: [raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile9.png](../../raw/derived/opendataloader/wimmer_2019_generation_of_blood_vessel_organoids/wimmer_2019_generation_of_blood_vessel_organoids_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
