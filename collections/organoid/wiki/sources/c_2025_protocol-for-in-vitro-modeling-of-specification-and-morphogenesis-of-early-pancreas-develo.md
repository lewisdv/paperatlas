---
title: Protocol for in vitro modeling of specification and morphogenesis of early pancreas development using human pluripotent stem cell-based organoid differentiation.
kind: paper
status: ingested
added: 2026-04-21T20:27:53+09:00
raw_source: raw/sources/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12149599/
published_date: 2025-05-21
organ: pancreas
protocol_focus: in vitro modeling of specification and morphogenesis of early pancreas development using human pluripotent stem cell-based organoid differentiation
deep_ingested: 2026-04-22
---

# Protocol for in vitro modeling of specification and morphogenesis of early pancreas development using human pluripotent stem cell-based organoid differentiation.

## Source

- PDF: [raw/sources/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo.pdf](../../raw/sources/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12149599/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12149599/)
- Status: deep ingested 2026-04-22
- Organ focus: hPSC-derived pancreatic epithelial organoids used to model early morphogenesis and endocrine differentiation
- Protocol focus: create a Matrigel-overlay epithelial niche on top of a 2D hPSC culture so pancreas specification, lumen morphogenesis, and endocrine fate decisions can be imaged in real time

## Study design

- Starting material: human pluripotent stem cells expanded as a 2D monolayer and then converted into a Matrigel-overlay organoid differentiation system
- Protocol stages:
  - seed hPSCs in imaging-compatible dishes, then apply a growth-factor-reduced Matrigel overlay to create a three-dimensional epithelial niche without fully detaching the culture into free-floating aggregates
  - drive the cells through six differentiation stages, moving from definitive endoderm through primitive gut tube and pancreatic progenitor states into endocrine progenitor and endocrine-cell stages
  - use staged media containing factors such as Activin A, CHIR99021, KGF, LDN-193189, SANT-1, retinoic acid, ALK5 inhibition, and gamma-secretase inhibition to coordinate morphogenesis with lineage progression
  - quantify lineage transitions by flow cytometry and immunofluorescence at key checkpoints, while following lumen remodeling and apical organization by live-cell imaging and EZRIN staining
- Key validation: by day 3 more than 90% of cells expressed definitive-endoderm markers FOXA2 and SOX17, by day 10 more than 50% expressed the bipotent pancreatic progenitor markers PDX1 and NKX6.1, and by day 20 more than 55% expressed INS while more than 17% expressed GCG
- Distinct protocol emphasis: this is a morphogenesis-aware pancreas protocol, using an intermediate format between flat monolayer differentiation and classical floating organoids so lineage progression and epithelial architecture can be tracked together

## Summary

- The paper is most useful as a bridge protocol between directed pancreas differentiation and organoid-style morphogenesis.
- Its distinctive move is the Matrigel-overlay format, which keeps the culture imageable and experimentally accessible while still allowing luminal epithelial remodeling.
- Within this corpus, it sharpens the middle ground between heavy self-organization and fully flattened, maximally controlled monolayer differentiation.

## Key findings

- The system preserves dynamic epithelial lumen formation during pancreas differentiation rather than treating morphogenesis as irrelevant background.
- It yields useful endocrine output while remaining readable as a developmental model, not only as a cell-production pipeline.
- The protocol is explicitly built for live-cell imaging and real-time fate tracking, which makes it stronger for mechanism questions than a black-box endpoint differentiation workflow.

## Distinctive contribution in this corpus

- One of the clearest pancreas protocols here for integrating morphogenesis and lineage specification instead of optimizing only for terminal endocrine yield.
- Gives the gastrointestinal-and-endoderm branch a pancreas counterpart to the collection's better-developed gut and liver systems.
- Helps the self-organization concept page by showing that some protocols deliberately occupy an intermediate zone: more structured than unguided organoids, but more morphogenetic than standard 2D differentiation.

## Limitations and caveats

- Differentiation efficiency still depends strongly on line-specific behavior, cytokine timing, and the quality or uniformity of the Matrigel overlay.
- The model is strongest for early pancreas specification and morphogenesis, not for claiming mature adult islet physiology.
- Because the system balances imageability and morphogenesis, it may not reach the same final-state optimization as protocols built purely for beta-cell output.

## Relevance to corpus

- Strengthens the pancreas and endoderm branch with a protocol that is useful for development questions, not only for cell replacement or endpoint maturation.
- Useful whenever the experimental goal is to watch epithelial remodeling and lineage restriction unfold in one system rather than infer them from terminal markers alone.
- Provides a practical comparator to more fully directed beta-cell protocols and to multi-organ boundary pancreas systems.

## Related concepts

- [Gastrointestinal and endodermal organoid systems](../concepts/gastrointestinal-and-endodermal-organoid-systems.md)
- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)

## Related entities

- [Stem-cell-derived islets (SC-islets)](../entities/stem-cell-derived-islets-sc-islets.md)

## Related sources

- [Engineering human hepato-biliary-pancreatic organoids from pluripotent stem cells](koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md) - a broader endodermal boundary model where pancreas identity is linked to neighboring foregut lineages rather than isolated as a single epithelial track.
- [Generation of insulin-producing pancreatic β cells from multiple human stem cell lines](hogrebe_2021_generation_of_insulin-producing_pancreatic.md) - a more yield-oriented beta-cell differentiation comparator.
- [Functional, metabolic and transcriptional maturation of human pancreatic islets derived from stem cells](balboa_2022_functional_metabolic_and_transcriptional.md) - a later-stage maturation comparator showing what has to be added once early morphogenesis is no longer the main question.

## Open questions

- Which morphogenetic events seen in the Matrigel-overlay system are essential for endocrine competence and which are only correlated with it?
- How far can this imageable intermediate format be pushed toward later functional maturation without losing the morphogenesis window that makes it useful?
- Which perturbations, ECM properties, or live reporters would most productively exploit the system's real-time imaging strengths?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:28:27+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo -f json,markdown`
- Manifest: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/opendataloader-run.json](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/opendataloader-run.json)
- Output: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo.json](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo.json)
- Output: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo.md](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo.md)
- Output: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile1.png](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile1.png)
- Output: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile2.png](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile2.png)
- Output: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile3.png](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile3.png)
- Output: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile4.png](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile4.png)
- Output: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile5.png](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile5.png)
- Output: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile6.png](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile6.png)
- Output: [raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile7.png](../../raw/derived/opendataloader/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo/c_2025_protocol-for-in-vitro-modeling-of-specification-and-morphogenesis-of-early-pancreas-develo_images/imageFile7.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
