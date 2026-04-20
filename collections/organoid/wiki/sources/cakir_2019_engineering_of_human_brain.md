---
title: "Engineering of human brain organoids with a functional vascular-like system"
kind: paper
status: ingested
added: 2026-04-09T17:00:00+09:00
raw_source: raw/sources/cakir_2019_engineering_of_human_brain.pdf
article_url: https://www.nature.com/articles/s41592-019-0586-5
published_date: 2019-10-07
organ: brain + vascular
protocol_focus: ETV2-induced vascular-like network in human cortical organoids
deep_ingested: 2026-04-09
---

# Engineering of human brain organoids with a functional vascular-like system

## Source

- PDF: [raw/sources/cakir_2019_engineering_of_human_brain.pdf](../../raw/sources/cakir_2019_engineering_of_human_brain.pdf)
- Article: [Nature Methods](https://www.nature.com/articles/s41592-019-0586-5)
- Lab: In-Hyun Park (Yale School of Medicine)
- Status: deep ingested 2026-04-09

## Study design

- Starting material: hESCs engineered to ectopically express human ETS variant 2 (ETV2) — a transcription factor that reprograms cells toward endothelial fate
- Approach: mix 20% ETV2+ cells with 80% regular hPSCs to form cortical organoids
- ETV2 induction: day 18
- Timepoints analyzed: day 30, 70, 120
- Readouts: CD31/CDH5 immunostaining, whole-mount imaging, qPCR for EC markers, TUNEL (apoptosis), HIF-1α (hypoxia), FITC-dextran perfusion test, electron microscopy, blood-brain barrier marker expression, trans-endothelial electrical resistance

## Key findings

- **ETV2 overexpression induces EC differentiation in hESCs regardless of differentiation condition** — works in EB, neural, and EC differentiation protocols.
- Optimal: 20% ETV2+ cells + induction at day 18 → best vascular-like network formation.
- **Vascularized cortical organoids (vhCOs) form CD31+ endothelial tubes** by day 30; more complex networks by day 70.
- vhCOs have **significantly more vessel area and vessel length** than control hCOs.
- **Perfusable vasculature**: FITC-dextran perfusion shows functional lumen connectivity (~8% of VZ lumens are perfusable).
- **Dramatic reduction in apoptosis and hypoxia**: control hCOs show ~35% TUNEL+ at day 70 and ~42% HIF-1α+ regions at day 120; vhCOs show minimal cell death and only ~2.5% hypoxic regions.
- **Blood-brain barrier characteristics acquired**: tight junctions, nutrient transporters, increased trans-endothelial electrical resistance.
- After transplantation in vivo: ETV2-induced endothelium supports formation of perfused blood vessels.
- Both control and vhCOs have similar VZ/SVZ/cortical layer organization — vascularization does not perturb neural identity.

## Distinctive contribution in this corpus

- **First example of ectopic TF-driven vascularization in a brain organoid in this corpus.**
- Demonstrates that engineered co-development (not just co-culture) can produce integrated vascular networks.
- Provides one answer to the hypoxia/necrotic core problem that plagues large cerebral organoids.
- Complements Homan 2019 (flow-enhanced) and Wörsdorfer 2019 (MPC incorporation) vascularization strategies.

## Limitations and caveats

- Requires genetic engineering (ETV2 transduction) — not trivial for all labs.
- Vascular-like structures are not true capillaries; missing mural cell complexity.
- Only cortical organoids tested; generalization to other brain regions unclear.
- "Functional" BBB features are suggestive, not comprehensive.

## Relevance to corpus

- Complements the vascularization paper cluster: Wimmer 2019 (stand-alone vessels), Homan 2019 (flow for kidney), Wörsdorfer 2019 (MPC incorporation).
- Mechanistically closest to Wörsdorfer 2019: both use mesodermal/endothelial progenitor incorporation, but Cakir uses a TF approach while Wörsdorfer uses direct cell mixing.

## Related concepts

- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Related sources

- [Wimmer 2019](wimmer_2019_generation_of_blood_vessel_organoids.md) — stand-alone vessel organoid protocol.
- [Homan 2019](homan_2019_flow-enhanced_vascularization_and_maturation.md) — alternative vascular maturation via flow.
- [Wörsdorfer 2019](worsdorfer_2019_generation_of_complex_human_organoid.md) — alternative via MPC mixing.
- [Lancaster 2014](lancaster_2014_generation_of_cerebral_organoids_from.md) — baseline brain organoid that suffers from the hypoxic core this paper addresses.

## Open questions

- How does BBB fidelity compare to in vivo human BBB?
- Can this approach be extended to other brain regions (hippocampus, midbrain)?
- Does ETV2-induced endothelium alter neural subtype specification, even subtly?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-12T12:40:25+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/cakir_2019_engineering_of_human_brain.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/cakir_2019_engineering_of_human_brain -f json,markdown`
- Manifest: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/opendataloader-run.json](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/opendataloader-run.json)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain.json](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain.json)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain.md](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain.md)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile1.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile1.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile10.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile10.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile11.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile11.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile12.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile12.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile13.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile13.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile14.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile14.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile15.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile15.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile16.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile16.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile17.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile17.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile18.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile18.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile19.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile19.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile2.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile2.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile20.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile20.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile21.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile21.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile22.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile22.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile23.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile23.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile24.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile24.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile25.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile25.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile26.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile26.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile27.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile27.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile28.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile28.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile29.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile29.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile3.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile3.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile30.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile30.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile31.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile31.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile32.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile32.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile33.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile33.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile34.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile34.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile35.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile35.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile36.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile36.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile37.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile37.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile38.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile38.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile39.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile39.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile4.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile4.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile40.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile40.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile41.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile41.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile42.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile42.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile43.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile43.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile44.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile44.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile5.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile5.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile6.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile6.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile7.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile7.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile8.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile8.png)
- Output: [raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile9.png](../../raw/derived/opendataloader/cakir_2019_engineering_of_human_brain/cakir_2019_engineering_of_human_brain_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
