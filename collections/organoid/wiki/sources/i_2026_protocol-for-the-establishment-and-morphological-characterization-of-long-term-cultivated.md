---
title: Protocol for the establishment and morphological characterization of long-term cultivated murine cerebral organoids.
kind: paper
status: ingested
added: 2026-04-21T20:30:45+09:00
raw_source: raw/sources/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12819030/
published_date: 2026-01-09
organ: brain
protocol_focus: the establishment and morphological characterization of long-term cultivated murine cerebral organoids
deep_ingested: 2026-04-22
---

# Protocol for the establishment and morphological characterization of long-term cultivated murine cerebral organoids.

## Source

- PDF: [raw/sources/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated.pdf](../../raw/sources/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12819030/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12819030/)
- Status: deep ingested 2026-04-22
- Organ focus: murine cerebral organoids derived from embryonic stem cells and carried into a longer-term cortical-like maturation window
- Protocol focus: B27-guided murine cerebral organoid generation, Matrigel embedding, orbital-shaker culture, and morphology-first characterization

## Study design

- Starting material: E14.5 mouse embryonic stem cells, specifically the E14tg2a ESC line used to build cerebral organoids from scratch
- Protocol stages:
  - initiate embryoid-body formation from ESCs and confirm compact aggregate formation within the first 24 hours
  - embed the early aggregates in Matrigel and transfer them to cortical maturation medium with B27 at day 5
  - move cultures to orbital-shaker conditions from day 10 onward to support continued growth and tissue organization
  - characterize organoids between days 15 and 30 for rosette formation, cortical-like architecture, and lineage progression using markers such as PAX6, SOX2, TBR1, CTIP2, SATB2, NeuN, GFAP, OLIG2, and Reelin
  - extend cultures into the day-40 to day-60 window to document long-term morphology, viability loss, and necrotic-core emergence
- Key validation: the protocol reports organized neural rosettes and cortical-like zones together with progressive neuronal and glial differentiation, but also shows that viability falls sharply after organoids exceed roughly 2 mm and pass the day-40 to day-50 range
- Distinct protocol emphasis: this is a morphology-heavy murine baseline protocol whose value comes from reproducible histology, staging, and troubleshooting rather than from maximal human-like maturity or circuit assays

## Key findings

- Establishes a straightforward murine cerebral organoid workflow that stays useful well beyond the earliest neuroepithelial stage and makes later morphology easier to benchmark.
- Makes the main failure mode explicit: central necrosis and greater than 50% non-viability become common by days 55 to 60, so the paper effectively argues that about 40 days is the safer standardized window for comparisons.
- Gives unusually practical troubleshooting around embryoid-body quality, Matrigel handling, seeding density, and rosette preservation, which is often the information missing from higher-level brain organoid papers.
- Frames murine organoids as a rapid and reproducible system for neurogenesis-focused questions rather than as a substitute for the most human-faithful cortical atlas models.

## Distinctive contribution in this corpus

- One of the clearest low-complexity brain baselines in the collection for users who need morphology, histology, and timing guidance before moving into expensive human-brain workflows.
- Strengthens the corpus on the reproducibility side by documenting where apparently successful long-term cultures start to fail structurally.
- Complements the collection's human cerebral organoid papers by showing how a murine system can be used to study neurogenesis and staging questions with faster iteration.

## Limitations and caveats

- This is a mouse ESC protocol, so it is not a direct proxy for human cortical diversity or human developmental timing.
- The long-term label should be interpreted carefully because the paper itself shows substantial necrosis and declining viability once cultures become large and old.
- Most validation is morphological and immunostaining-based; the protocol is much less informative for electrophysiology, network behavior, or transcriptomic fidelity than later human-brain papers.
- Matrigel lot effects, aggregate heterogeneity, and manual handling remain important sources of variability.

## Relevance to corpus

- Strengthens the brain-patterning and brain-fidelity branches of the collection with a pragmatic murine comparator.
- Useful when the question is how to establish a reproducible neural organoid workflow for morphology-first studies before layering on higher-order assays.
- Helps interpret why some later long-term brain protocols emphasize perfusion, transplantation, or careful maturity benchmarking once simple static culture starts to break down.

## Related concepts

- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)

## Related entities

- [Single-cell atlas benchmarking](../entities/single-cell-atlas-benchmarking.md)

## Related sources

- [Generation of cerebral organoids from human pluripotent stem cells](lancaster_2014_generation_of_cerebral_organoids_from.md) - the canonical human cerebral-organoid baseline that highlights how this paper trades human fidelity for murine speed and practicality.
- [Generation and long-term culture of advanced cerebral organoids for studying later stages of neural development](giandomenico_2021_generation_and_long-term_culture_of.md) - a human long-term culture comparator with a stronger emphasis on later-stage maturation.
- ["Reliability of human cortical organoid generation"](yoon_2019_reliability_of_human_cortical.md) - a better match for reproducibility and standardization questions in human cortical organoids.

## Open questions

- How far can the viable culture window be extended with perfusion, size control, or metabolic support before the murine system changes character?
- Which morphology readouts from this murine protocol actually predict transcriptional or functional maturity in later neural assays?
- When is a murine cerebral organoid sufficient for the question, and when does the user need to switch to human region-specific models?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:31:21+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated -f json,markdown`
- Manifest: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/opendataloader-run.json](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/opendataloader-run.json)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated.json](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated.json)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated.md](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated.md)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile1.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile1.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile10.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile10.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile11.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile11.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile12.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile12.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile13.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile13.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile14.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile14.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile2.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile2.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile3.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile3.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile4.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile4.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile5.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile5.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile6.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile6.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile7.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile7.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile8.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile8.png)
- Output: [raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile9.png](../../raw/derived/opendataloader/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated/i_2026_protocol-for-the-establishment-and-morphological-characterization-of-long-term-cultivated_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
