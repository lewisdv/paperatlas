---
title: Protocol for generating and analyzing organ-on-chip using human and mouse intestinal organoids.
kind: paper
status: ingested
added: 2026-04-21T20:31:00+09:00
raw_source: raw/sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11066468/
published_date: 2024-04-26
organ: colon-intestine
protocol_focus: generating and analyzing organ-on-chip using human and mouse intestinal organoids
deep_ingested: 2026-04-22
---

# Protocol for generating and analyzing organ-on-chip using human and mouse intestinal organoids.

## Source

- PDF: [raw/sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.pdf](../../raw/sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11066468/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11066468/)
- Status: deep ingested 2026-04-22
- Organ focus: human descending-colon and murine distal-colon organoid-derived intestinal epithelium on chip
- Protocol focus: convert adult-stem-cell intestinal organoids into a membrane-free microfluidic epithelial barrier with separate apical and basal access

## Study design

- Starting material: established human and mouse adult-stem-cell intestinal organoids expanded under proliferative conditions
- Protocol stages:
  - expand human and mouse organoids using species-specific maintenance and dissociation conditions
  - prepare a Mimetas OrganoPlate 3-lane 40 by loading collagen I into the gel lane and collagen IV into the top channel as a coating
  - dissociate organoids to cells, seed them onto the chip, and maintain flow-driven culture that creates distinct apical and basal reservoirs
  - analyze barrier integrity, permeability, RNA yield, staining, and cytokine or supernatant sampling separately from each side of the epithelium
  - use the system as a platform for later apical or basal stimulation with microbes, cytokines, toxins, metabolites, or added cell types
- Key validation: the paper shows barrier formation, polarized ZO-1-positive epithelium, apical microvilli enrichment, crypt-like invaginations, and successful permeability assays
- Distinct protocol emphasis: unlike closed 3D organoids, this chip makes the luminal face experimentally accessible without stripping away organoid-derived epithelial diversity

## Key findings

- Solves one of the main practical limitations of intestinal organoids by giving continuous access to both the apical and basal compartments.
- Uses a membrane-free ECM barrier to support more direct cell-ECM interaction than many conventional chip layouts.
- Preserves enough epithelial organization to support permeability, staining, RNA, and secreted-factor assays in one platform.
- Works as an assay-enabling infrastructure layer that other intestinal experiments can be plugged into later.

## Distinctive contribution in this corpus

- One of the strongest infrastructure papers in the refill cohort because it turns adult intestinal organoids into a modular interface for polarized assays.
- Connects the gastrointestinal concept page directly to the engineering and assay-layer concept pages.
- Gives the collection a concrete "open the lumen without losing organoid-derived biology" protocol, complementing polarity-control and microbial-exposure papers.

## Limitations and caveats

- The membrane-free ECM gradually loses integrity, limiting culture duration to roughly 14 days for human chips and 7 days for mouse chips unless the matrix is modified.
- The system does not fully recreate native crypt-villus 3D patterning even though it captures some invagination-like features.
- Chip preparation is technically sensitive: ECM loading can fail, coating is pH dependent, and channels can clog with dead cells or mucus.
- Reproducibility can vary across chips because some lanes load more poorly than others.

## Relevance to corpus

- Useful whenever the question is not just how to grow an intestinal organoid, but how to run polarized exposure, barrier, or sampling experiments on it.
- Strengthens the engineering branch with a platform paper rather than a perturbation-only paper.
- Serves as a bridge from baseline intestinal culture to later infection, permeability, cytokine, and multicellular coculture studies.

## Related concepts

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Gastrointestinal and endodermal organoid systems](../concepts/gastrointestinal-and-endodermal-organoid-systems.md)

## Related sources

- [Controlling the polarity of human gastrointestinal organoids to investigate epithelial biology and infectious diseases](co_2021_controlling_the_polarity_of_human.md) - another route to luminal accessibility, but through polarity inversion rather than chip engineering.
- [Intestinal organoid cocultures with microbes](puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) - a complementary assay-layer paper that benefits from improved access to the epithelial interface.
- [Protocol for modeling the repair of intestinal damage by co-culturing mesenchymal stromal/stem cells and intestinal organoids](kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.md) - another example of intestinal organoids being converted into a more controlled assay platform.

## Open questions

- Which intestinal applications really need a chip rather than simpler polarity-control or monolayer approaches?
- How much additional fidelity is gained by adding immune, endothelial, or microbial compartments into this membrane-free layout?
- What chip-to-chip QC metrics best predict whether downstream permeability or secretion data will be trustworthy?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:31:27+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ -f json,markdown`
- Manifest: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/opendataloader-run.json](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/opendataloader-run.json)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.json](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.json)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile1.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile1.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile10.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile10.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile11.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile11.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile12.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile12.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile13.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile13.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile14.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile14.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile15.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile15.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile16.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile16.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile17.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile17.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile2.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile2.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile3.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile3.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile4.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile4.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile5.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile5.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile6.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile6.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile7.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile7.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile8.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile8.png)
- Output: [raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile9.png](../../raw/derived/opendataloader/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
