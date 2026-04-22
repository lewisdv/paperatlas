---
title: Protocol for modeling the repair of intestinal damage by co-culturing mesenchymal stromal/stem cells and intestinal organoids.
kind: paper
status: ingested
added: 2026-04-21T20:30:56+09:00
raw_source: raw/sources/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12800398/
published_date: 2025-12-24
organ: colon-intestine
protocol_focus: modeling the repair of intestinal damage by co-culturing mesenchymal stromal/stem cells and intestinal organoids
deep_ingested: 2026-04-22
---

# Protocol for modeling the repair of intestinal damage by co-culturing mesenchymal stromal/stem cells and intestinal organoids.

## Source

- PDF: [raw/sources/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.pdf](../../raw/sources/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12800398/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12800398/)
- Status: deep ingested 2026-04-22
- Organ focus: human duodenal organoids cocultured with bone-marrow-derived mesenchymal stromal or stem cells under injury conditions
- Protocol focus: scalable intestinal epithelial injury-repair assay using MSC coculture and low-threshold image analysis

## Study design

- Starting material: established human duodenal organoids and healthy-donor bone-marrow-derived MSCs
- Protocol stages:
  - prepare organoid support media and MSC growth media, including conditioned media quality control
  - dissociate organoids and seed small Matrigel droplets at densities optimized for later image segmentation, typically around 500 cells per droplet
  - induce epithelial injury with busulfan, then remove the drug and introduce MSC coculture
  - image wells by standard light microscopy and quantify organoid number and size using OrganoSeg plus the companion OrganoAna analysis workflow
  - adapt the same framework for short-term survival readouts or longer-term regenerative follow-up
- Key validation: the assay reads out immediate and longer-term effects of MSCs on busulfan-injured organoids and was built to be statistically robust because each droplet contains many measurable organoids
- Distinct protocol emphasis: the paper is as much about making the repair assay easy to analyze as it is about the coculture itself

## Key findings

- Provides a controllable epithelial-injury model that is simpler than animal studies but more disease-relevant than uninjured organoid coculture.
- Makes MSC support a measurable regenerative variable rather than a vague coculture add-on.
- Couples the biology to an accessible analysis pipeline, lowering the barrier for labs that do not have bespoke imaging infrastructure.
- Shows how injury context can transform a standard intestinal organoid system into a clinically adjacent regeneration assay.

## Distinctive contribution in this corpus

- One of the best repair-oriented assay papers in the refill cohort because it makes epithelial-stromal regeneration experimentally tractable at scale.
- Strengthens the functional-assay concept page with a defined injury model instead of a pure coculture or transplantation example.
- Adds an intestinal regeneration comparator to the more immune-focused or transplantation-focused assay sources already in the deep-ingested tier.

## Limitations and caveats

- The model is intentionally simplified and omits immune cells, inflammatory cytokine complexity, and many other in vivo modifiers of MSC behavior.
- The current setup does not distinguish direct cell-cell contact effects from purely paracrine effects unless the assay is redesigned with physical separation.
- Organoids remain mostly stem-like and not fully differentiated, so lineage-specific repair biology is only partially represented.
- Busulfan concentration and seeding density both need titration; overseeding reduces image-analysis quality and underinjury collapses assay resolution.

## Relevance to corpus

- Useful whenever the practical question is how to model intestinal epithelial repair without immediately escalating to animals.
- Strengthens the gastrointestinal and coculture branches with a repair-focused stromal assay.
- Provides a clear example of organoids being used to test regenerative therapeutics rather than only developmental patterning.

## Related concepts

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Gastrointestinal and endodermal organoid systems](../concepts/gastrointestinal-and-endodermal-organoid-systems.md)

## Related sources

- [Transplantation of intestinal organoids into a mouse model of colitis](watanabe_2022_transplantation_of_intestinal_organoids_into.md) - a stronger in vivo repair escalation step after in vitro assay results.
- [Protocol for the establishment and characterization of an endometrial-derived epithelial organoid and stromal cell co-culture system](ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.md) - a stromal-epithelial coculture comparator outside the intestine.
- [Protocol for generating and analyzing organ-on-chip using human and mouse intestinal organoids](iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md) - another intestinal assay-layer platform that trades repair focus for polarized access and flow.

## Open questions

- Which MSC effects in this system depend on contact versus soluble signaling?
- How well do busulfan-repair phenotypes predict what would happen in more complex inflammatory injury settings such as GvHD?
- What is the minimum analysis stack needed to preserve throughput without sacrificing segmentation quality?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:31:34+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal -f json,markdown`
- Manifest: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/opendataloader-run.json](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/opendataloader-run.json)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.json](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.json)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.md](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.md)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile1.png](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile1.png)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile2.png](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile2.png)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile3.png](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile3.png)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile4.png](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile4.png)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile5.png](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile5.png)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile6.png](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile6.png)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile7.png](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile7.png)
- Output: [raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile8.png](../../raw/derived/opendataloader/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal_images/imageFile8.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
