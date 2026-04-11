---
title: "Human sensorimotor organoids derived from healthy and amyotrophic lateral sclerosis stem cells form neuromuscular junctions"
kind: paper
status: ingested
added: 2026-04-09T15:30:00+09:00
raw_source: raw/sources/pereira_2021_human_sensorimotor_organoids_derived.pdf
article_url: https://www.nature.com/articles/s41467-021-24776-4
published_date: 2021-07-29
organ: spinal cord / neuromuscular
protocol_focus: sensorimotor organoid with functional NMJs and ALS modeling
deep_ingested: 2026-04-09
---

# Human sensorimotor organoids derived from healthy and ALS stem cells form neuromuscular junctions

## Source

- PDF: [raw/sources/pereira_2021_human_sensorimotor_organoids_derived.pdf](../../raw/sources/pereira_2021_human_sensorimotor_organoids_derived.pdf)
- Article: [Nature Communications](https://www.nature.com/articles/s41467-021-24776-4)
- Lab: Brian Wainger (MGH Healey Center for ALS, Harvard)
- Status: deep ingested 2026-04-09

## Study design

- Starting material: 5 iPSC lines (2 healthy controls, 2 familial ALS lines, 1 sporadic ALS)
- Additional: isogenic iPSC pairs harboring TARDBP, SOD1, and PFN1 familial ALS mutations
- Protocol: suspension sphere formation → 1 week patterning → adherent plating → 15 weeks total in matrigel-coated plates
- Key patterning: **neuromesodermal progenitor (NMP) induction via FGF + WNT agonists + forskolin** (rather than pure neural or pure muscle differentiation)
- Readouts: scRNA-seq (27,000 cells), immunohistochemistry, electrophysiology (NMJ function)

## Key findings

- Organoids contain motor neurons, sensory neurons, skeletal muscle, astrocytes, microglia, AND vasculature — all derived from the same starting material.
- **Physiologically functional NMJs form between motor neurons and skeletal muscle** (measured by contraction + immunocytochemistry).
- NMJs are impaired in all 3 ALS lines tested.
- **Isogenic gene-edited ALS lines replicate the NMJ impairment** and show reduced within-line and among-line variances.
- Demonstrates utility for precision medicine / ALS subtype-specific modeling.

## Distinctive contribution in this corpus

- **First spinal cord / neuromuscular entry in the collection** — fills major gap.
- Unique co-development strategy: NMPs give rise to both ectodermal (neural) and mesodermal (muscle) derivatives in the same organoid.
- Only paper in corpus with functional NMJ physiological measurements.
- Provides a template for motor/sensory disease modeling beyond ALS.

## Limitations and caveats

- 15 weeks is relatively short for full NMJ maturation.
- Skeletal muscle remains immature compared to in vivo adult muscle.
- Single-cell heterogeneity complicates interpretation — which cells drive NMJ impairment?

## Relevance to corpus

- Parallels brain+vascular integration seen in Cakir 2019: this paper shows NMP-driven co-development of multiple lineages.
- Contributes to multi-lineage / multi-tissue organoid discussion alongside Koike 2021 (hepato-biliary-pancreatic) and Dardano 2025 (blood-generating heart).

## Related concepts

- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related sources

- [Koike 2021](koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from.md) — another multi-lineage boundary model, different developmental axis.
- [Meng 2025](meng_2025_crispr_screens_in_human_neural.md) — CRISPR screening in neural organoids, useful for ALS gene discovery follow-up.

## Open questions

- Which cell type is the primary driver of NMJ dysfunction in ALS organoids — motor neuron, muscle, or astrocyte?
- Can NMJ maturation be extended beyond 15 weeks to study late-stage disease?
- Does adding vasculature or microglia change the ALS phenotype (non-cell autonomous effects)?
