---
title: "Generation of insulin-producing pancreatic β cells from multiple human stem cell lines"
kind: paper
status: ingested
added: 2026-04-09T15:30:00+09:00
raw_source: raw/sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.pdf
article_url: https://www.nature.com/articles/s41596-021-00560-y
published_date: 2021-06-25
organ: pancreas
protocol_focus: six-stage planar SC-β cell differentiation with latrunculin A maturation
deep_ingested: 2026-04-09
---

# Generation of insulin-producing pancreatic β cells from multiple human stem cell lines

## Source

- PDF: [raw/sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.pdf](../../raw/sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.pdf)
- Article: [Nature Protocols](https://www.nature.com/articles/s41596-021-00560-y)
- Lab: Jeffrey Millman (Washington University, St. Louis)
- Status: deep ingested 2026-04-09

## Study design

- Six-stage directed differentiation protocol (~34 days + 1-2 weeks for stem cell expansion and final assessment)
- Starting material: 10 hPSC lines (5 new + 5 previously published) on Matrigel-coated TCP
- **Key innovation: fully planar culture** (no 3D suspension required)
- Stages:
  - Stage 0: hPSC culture in mTeSR1
  - Stage 1 (4 d): Definitive endoderm — Activin A + CHIR99021
  - Stage 2 (2 d): Primitive gut tube
  - Stage 3 (2 d): Pancreatic progenitor (PDX1+)
  - Stage 4 (4 d): PDX1+/NKX6-1+ pancreatic progenitor — KGF + SANT1 + TPPB + LDN193189 + RA
  - Stage 5 (7 d): Endocrine induction — **latrunculin A (24 h)** + XXI + T3 + ALK5i + SANT1 + RA
  - Stage 6 (14+ d): SC-β cell maturation
- Final step: optional aggregation into islet-like clusters on orbital shaker

## Key findings

- **Eliminates the previous requirement for 3D suspension culture** to generate functional SC-β cells.
- Key mechanistic insight: actin cytoskeleton state controls NEUROG3 endocrine induction.
  - TCP monolayer culture → high actin polymerization → prevents premature NEUROG3, enables NKX6-1 expression (good).
  - But polymerization also blocks subsequent endocrine specification — solved by **24 h latrunculin A depolymerization** at the start of stage 5.
- Planar methodology is **more reproducible across multiple hPSC lines** (many lines don't adapt well to suspension culture).
- Simplifies differentiation significantly — removes need for spinner flasks or Transwells.
- Produces 0.5-0.75 million cells/cm² with 2-3× higher cell yield per media volume vs. suspension protocols.
- Transplanted cells rapidly reverse severe preexisting diabetes in mice.

## Distinctive contribution in this corpus

- **First pancreatic islet entry in the collection** — fills major gap.
- Represents a new generation of "simplified" hPSC differentiation protocols that prioritize cross-line robustness over 3D architecture.
- Should be read alongside Balboa 2022 which focuses on maturation / functional benchmarking.

## Limitations and caveats

- Planar β cells still need aggregation step for downstream assays.
- 34+ days is still a long differentiation timeline.
- α, δ, and other endocrine cell types form in lower proportions.
- Non-endocrine byproducts require cluster aggregation to sort out.

## Relevance to corpus

- Establishes baseline pancreatic islet protocol for the collection.
- Complements Balboa 2022 (functional maturation benchmark) and Koike 2021 (hepato-biliary-pancreatic multi-organ model).

## Related concepts

- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Gastrointestinal and endodermal organoid systems](../concepts/gastrointestinal-and-endodermal-organoid-systems.md)

## Related sources

- [Balboa 2022](balboa_2022_functional_metabolic_and_transcriptional.md) — detailed maturation benchmarking of SC-islets against primary.
- [Koike 2021](koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md) — multi-organ hepato-biliary-pancreatic model.

## Open questions

- How does planar SC-β functional maturity compare to Balboa's optimized suspension protocol?
- Can the latrunculin A insight transfer to other endocrine differentiation protocols?
- What is the upper limit of batch-to-batch reproducibility in the planar approach?
