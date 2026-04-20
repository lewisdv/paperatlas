---
title: "Reliability of human cortical organoid generation"
kind: paper
status: ingested
added: 2026-04-09T16:00:00+09:00
raw_source: raw/sources/yoon_2019_reliability_of_human_cortical.pdf
article_url: https://www.nature.com/articles/s41592-018-0255-0
published_date: 2019-01-07
organ: brain
protocol_focus: directed cortical spheroid (hCS) reliability across 12 hiPSC lines
deep_ingested: 2026-04-09
---

# Reliability of human cortical organoid generation

## Source

- PDF: [raw/sources/yoon_2019_reliability_of_human_cortical.pdf](../../raw/sources/yoon_2019_reliability_of_human_cortical.pdf)
- Article: [Nature Methods](https://www.nature.com/articles/s41592-018-0255-0)
- Lab: Sergiu Pasca (Stanford)
- Status: deep ingested 2026-04-09

## Study design

- Starting material: 12 hiPSC lines from 13 individuals, feeder-free xeno-free on vitronectin in Essential 8
- Protocol: Pasca lab directed human cortical spheroid (hCS) protocol — no extracellular matrix embedding
- Aggregation: AggreWell-800 plates (~10,000 cells per spheroid)
- Patterning: SMAD/WNT modulators + EGF + FGF2
- Duration: ≥100 days in vitro
- Readouts: 85 differentiations total; bulk + scRNA-seq + immunocytochemistry

## Key findings

- **90% of differentiations successfully maintained >100 days in vitro** (5% failed at aggregation, ~5% disintegrated over time).
- Strong forebrain patterning at day 25 (FOXG1+, SIX3+, PAX6+) with no endoderm/mesoderm contamination and no off-target hypothalamus/spinal cord/midbrain/ventral forebrain markers in 11 of 12 lines.
- **High transcriptional overlap between day-100 hCS and mid-gestation human cerebral cortex (up to PCW 24)** assessed by rank-rank hypergeometric overlap.
- **Principal source of transcriptional variance = differentiation stage, not cell line** — indicates temporal program dominates over inter-line variability.
- Scalability: one researcher can run 10-15 lines/week for >100 days.

## Distinctive contribution in this corpus

- Complements Velasco 2019 from a different angle: **Velasco used one protocol × 5 lines; Yoon used one protocol × 12 lines × 85 differentiations**.
- Establishes the Pasca lab hCS as a scalable, matrix-free alternative to Lancaster 2014's whole-brain approach.
- Foundation for downstream Pasca-lab assembloid work (cf. Sloan 2018).

## Limitations and caveats

- Dorsal forebrain only.
- "Reliability" defined primarily by gross patterning success and transcriptional overlap, not fine subtype identity.
- Does not directly compare to primary fetal cortex with single-cell resolution (unlike Bhaduri 2020).

## Relevance to brain synchronization query

- Reliability axis: differentiation stage dominates variance → supports the idea that **the maturation timeline is the primary synchronization axis** in directed protocols.
- Batch success rate (90%) provides a hard number for "how often does the protocol work" that most papers do not report.

## Related concepts

- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)

## Related sources

- [Sloan 2018](sloan_2018_generation_and_assembly_of_human.md) — same lab (Pasca), extends hCS to assembloids.
- [Velasco 2019](velasco_2019_individual_brain_organoids_reproducibly.md) — parallel reproducibility study with a different protocol.
- [Bhaduri 2020](bhaduri_2020_cell_stress_in_cortical.md) — fidelity counterpoint.

## Open questions

- How do the 10% failure cases fail — which step is most fragile?
- Does hCS reliability translate to functional (electrophysiological) reproducibility in MEA / patch clamp?
- How does hCS compare to Velasco's dorsal forebrain protocol on fidelity (subtype-level) rather than just reliability?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-12T12:46:58+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/yoon_2019_reliability_of_human_cortical.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical -f json,markdown`
- Manifest: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/opendataloader-run.json](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/opendataloader-run.json)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical.json](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical.json)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical.md](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical.md)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile1.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile1.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile10.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile10.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile11.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile11.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile12.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile12.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile13.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile13.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile14.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile14.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile15.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile15.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile2.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile2.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile3.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile3.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile4.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile4.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile5.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile5.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile6.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile6.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile7.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile7.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile8.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile8.png)
- Output: [raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile9.png](../../raw/derived/opendataloader/yoon_2019_reliability_of_human_cortical/yoon_2019_reliability_of_human_cortical_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
