---
title: Protocol for generating liver organoids containing Kupffer cells using human iPSCs.
kind: paper
status: ingested
added: 2026-04-21T20:30:53+09:00
raw_source: raw/sources/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12547730/
published_date: 2025-10-10
organ: liver
protocol_focus: generating liver organoids containing Kupffer cells using human iPSCs
deep_ingested: 2026-04-22
---

# Protocol for generating liver organoids containing Kupffer cells using human iPSCs.

## Source

- PDF: [raw/sources/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs.pdf](../../raw/sources/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12547730/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12547730/)
- Status: deep ingested 2026-04-22
- Organ focus: multilineage human iPSC-derived liver organoids that include resident macrophage-like Kupffer cells
- Protocol focus: generate EMP and hepatic endoderm in parallel, then assemble Kupffer-containing liver organoids in Elplasia microwells

## Study design

- Starting material: human iPSC-derived hepatic endoderm, endothelial cells, mesenchymal cells, and erythroid-myeloid progenitors (EMPs)
- Protocol stages:
  - maintain separate iPSC timelines because hepatic endoderm and EMPs are intended for fresh co-culture rather than freeze-thaw cycling
  - differentiate EMPs over 12 days using a staged cytokine program built around WNT3A, BMP4, VEGF, bFGF, SCF, TPO, and FLT3L
  - generate hepatic endoderm in parallel and combine it with previously generated endothelial and mesenchymal populations
  - seed HE, ECs, MCs, and EMPs into scaffold-free Elplasia U-bottom plates with KuLO medium and ROCK inhibitor to initiate co-culture day 0
  - refresh medium every 2 days, monitor albumin secretion over time, and characterize hematopoietic maturation by flow cytometry and whole-mount staining
- Key validation: by day 14 more than 90% of the EMP-derived cells can express Kupffer-associated markers CD45, CD14, and CD163, while the organoids also increase hepatic readouts such as albumin secretion and mature hepatic markers
- Distinct protocol emphasis: rather than adding macrophages as an external coculture later, the workflow builds Kupffer-like cells into the organoid during multilineage assembly

## Key findings

- Shows that liver-resident macrophage integration can be built into organoid formation by co-culturing EMPs with hepatic, endothelial, and mesenchymal lineages.
- Uses Elplasia microwells as a scaffold-free assembly platform where multicellular spheroids form quickly and the hematopoietic compartment expands around the growing organoid.
- Demonstrates that the resulting KuLOs are not only multilineage but functionally usable, with albumin secretion, hepatic maturation markers, and macrophage differentiation readouts.
- Extends the system into a disease-relevant assay by showing endotoxin-triggered Kupffer activation and reversible impairment of hepatic function after medium refreshment.

## Distinctive contribution in this corpus

- One of the strongest immune-bearing endoderm organoid protocols in the collection because it integrates a resident macrophage lineage instead of treating immune cells as an optional add-on.
- Pushes the liver branch beyond parenchymal organoid generation into inflammation, repair, and regeneration questions.
- Serves as a concrete example of how multilineage assembly can be used to model tissue-resident immune biology rather than only morphogenesis.

## Limitations and caveats

- The workflow is timing-sensitive because four lineage programs have to converge at the right moment for co-culture.
- The paper does not recommend freezing hepatic endoderm or EMPs for co-culture, which limits scheduling flexibility.
- Failure to form organoids on co-culture day 1 can result from weak HE differentiation, poor cell viability, or omission of ROCK inhibitor.
- Flow-cytometry proportions from dissociated organoids are useful for tracking differentiation but do not perfectly report the true spatial composition inside intact organoids.

## Relevance to corpus

- Strengthens both the gastrointestinal or endodermal and multi-lineage concept pages with a liver-specific immune-integration example.
- Useful as a comparator to adult liver organoid papers that expand epithelial tissue but do not build in resident macrophage biology.
- Gives the collection a liver protocol that already contains its own inflammation-response use case rather than needing a separate coculture paper to supply it.

## Related concepts

- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Gastrointestinal and endodermal organoid systems](../concepts/gastrointestinal-and-endodermal-organoid-systems.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)

## Related sources

- [Engineering human hepato-biliary-pancreatic organoids from pluripotent stem cells](koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md) - another multilineage endoderm protocol that expands tissue complexity beyond a single hepatic lineage.
- [Establishment of human fetal hepatocyte organoids and CRISPR-Cas9-based gene knockin and knockout in organoid cultures from human liver](hendriks_2020_establishment_of_human_fetal_hepatocyte.md) - a liver organoid comparator centered on epithelial expansion and engineering rather than immune integration.
- [Culture and establishment of self-renewing human and mouse adult liver and pancreas 3D organoids and their genetic manipulation](broutier_2016_culture_and_establishment_of_self-renewing.md) - the adult endoderm organoid baseline that highlights how different this iPSC multilineage strategy is.

## Related entities

- [Whole-mount 3D clearing and imaging](../entities/whole-mount-3d-clearing-and-imaging.md)

## Open questions

- What EMP-to-hepatic-endoderm ratio most reliably maximizes Kupffer-cell integration without compromising hepatic maturation?
- How stable are Kupffer-like phenotypes beyond the day-14 window or under chronic inflammatory stimulation?
- Which liver phenotypes truly require built-in resident macrophages rather than later macrophage coculture?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:31:58+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs -f json,markdown`
- Manifest: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/opendataloader-run.json](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/opendataloader-run.json)
- Output: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs.json](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs.json)
- Output: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs.md](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs.md)
- Output: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile1.png](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile1.png)
- Output: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile2.png](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile2.png)
- Output: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile3.png](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile3.png)
- Output: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile4.png](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile4.png)
- Output: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile5.png](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile5.png)
- Output: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile6.png](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile6.png)
- Output: [raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile7.png](../../raw/derived/opendataloader/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs/y_2025_protocol-for-generating-liver-organoids-containing-kupffer-cells-using-human-ipscs_images/imageFile7.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
