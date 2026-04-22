---
title: Monocytes prevent apoptosis of iPSCs and promote differentiation of kidney organoids
kind: paper
status: ingested
added: 2026-04-21T14:26:10+09:00
raw_source: raw/sources/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11069262/
published_date: 2024-01-01
organ: kidney
protocol_focus: monocytes prevent apoptosis of iPSCs and promote differentiation of kidney organoids
deep_ingested: 2026-04-22
---

# Monocytes prevent apoptosis of iPSCs and promote differentiation of kidney organoids

## Source

- PDF: [raw/sources/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids.pdf](../../raw/sources/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11069262/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11069262/)
- Status: deep ingested 2026-04-22
- Organ focus: hPSC kidney organoids whose early differentiation window is supported by monocytes or macrophage-like cells
- Protocol focus: rescue CHIR-sensitive early renal differentiation with transwell monocytes, iPSC-macrophages, rapamycin, and extracellular-vesicle transfer experiments

## Study design

- Starting material: human iPSCs undergoing kidney differentiation plus peripheral-blood classical monocytes, iPSC-derived macrophages, or purified monocyte extracellular vesicles
- Protocol stages:
  - begin a standard CHIR99021-driven mesoderm induction workflow, the stage the authors identify as a major apoptosis and ROS bottleneck during kidney organoid differentiation
  - compare two rescue strategies: pharmacologic autophagy induction with rapamycin versus indirect transwell coculture with monocytes or iPSC-macrophages
  - test whether secreted signals are sufficient by isolating monocyte-derived extracellular vesicles with PEG precipitation and applying them without intact monocytes
  - quantify apoptosis, autophagy, renal marker induction, and final organoid morphology using cleaved Caspase-3, PARP1, TBX6, OSR1, Pax2, Gata3, Nephrin, E-cadherin, and 3D confocal imaging
- Key validation: monocyte or macrophage coculture improves survival during CHIR exposure, activates autophagy, increases renal marker expression, and yields more numerous and better-formed organoids; rapamycin helps survival but does not reproduce the full differentiation benefit; EVs transfer part of the effect
- Distinct protocol emphasis: this paper does not replace the kidney lineage recipe, but shows that the most important intervention may be a support-compartment rescue during the earliest differentiation bottleneck

## Key findings

- Reframes a kidney-organoid failure mode as a cell-survival problem during CHIR exposure, not only as a lineage-patterning problem.
- Shows that monocytes outperform rapamycin because they rescue viability and promote downstream renal differentiation, rather than merely blunting apoptosis.
- Points to extracellular vesicles as one mechanistic route by which immune support cells can influence organoid differentiation without direct cell mixing.

## Distinctive contribution in this corpus

- Extends the kidney branch beyond route-comparison papers into support-cell-assisted differentiation design.
- One of the clearest examples in the corpus where a coculture layer acts during derivation itself rather than only after a mature organoid already exists.
- Gives the functional-assay concept page a non-infection example where a secondary cell type changes organoid competence rather than only reporting on it.

## Limitations and caveats

- The paper is an optimization study rather than a fully manualized protocol, so exact differentiation timing and media logic still depend on the underlying kidney-organoid workflow it modifies.
- Monocyte state, donor variability, and extracellular-vesicle composition are likely to shift the magnitude of the rescue effect.
- The mechanism is only partly resolved: autophagy activation is implicated, but the key EV cargo and broader transcriptional consequences remain open.

## Relevance to corpus

- Strengthens the kidney-differentiation and functional-assay branches at the same time.
- Useful when kidney protocols fail through poor yield or high death during early mesoderm induction rather than through obvious terminal-patterning errors.
- Complements route-definition papers such as Takasato and Morizane by showing that support-cell context can matter as much as lineage recipe choice.

## Related concepts

- [Kidney organoid differentiation routes](../concepts/kidney-organoid-differentiation-routes.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related sources

- [Generation of kidney organoids from human pluripotent stem cells](takasato_2016_generation_of_kidney_organoids_from.md) - a foundational kidney route paper that defines the lineage logic this study tries to stabilize.
- [Generation of nephron progenitor cells and kidney organoids from human pluripotent stem cells](morizane_2016_generation_of_nephron_progenitor_cells.md) - another core kidney differentiation comparator focused on directed lineage control rather than immune support.
- [Flow-enhanced vascularization and maturation of kidney organoids in vitro](homan_2019_flow-enhanced_vascularization_and_maturation.md) - a later-stage maturation comparator showing a different way to rescue kidney organoid performance after derivation succeeds.

## Open questions

- Which monocyte state or extracellular-vesicle cargo is most responsible for the renal differentiation boost?
- At what exact stage should immune support be added to maximize rescue without disrupting renal patterning?
- How general is this strategy across different kidney-organoid recipes and pluripotent lines?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:48:44+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids -f json,markdown`
- Manifest: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/opendataloader-run.json](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/opendataloader-run.json)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids.json](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids.json)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids.md](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids.md)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile1.png](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile1.png)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile2.png](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile2.png)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile3.png](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile3.png)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile4.png](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile4.png)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile5.png](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile5.png)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile6.png](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile6.png)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile7.png](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile7.png)
- Output: [raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile8.png](../../raw/derived/opendataloader/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids_images/imageFile8.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
