---
title: Protocol for the derivation and culture of murine trophoblast organoids for CRISPR-Cas9 screening.
kind: paper
status: ingested
added: 2026-04-21T20:31:03+09:00
raw_source: raw/sources/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11532991/
published_date: 2024-10-19
organ: placenta
protocol_focus: the derivation and culture of murine trophoblast organoids for CRISPR-Cas9 screening
deep_ingested: 2026-04-22
---

# Protocol for the derivation and culture of murine trophoblast organoids for CRISPR-Cas9 screening.

## Source

- PDF: [raw/sources/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc.pdf](../../raw/sources/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11532991/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11532991/)
- Status: deep ingested 2026-04-22
- Organ focus: murine placental trophoblast organoids used as a perturbation-compatible platform for lineage and screening work
- Protocol focus: derive and differentiate murine trophoblast organoids, install stable Cas9, and run focused sgRNA-library screens at controlled coverage

## Study design

- Starting material: murine trophoblast stem cells or placental tissue used to derive mouse trophoblast organoids
- Protocol stages:
  - derive murine trophoblast organoids under maintenance conditions and drive differentiation when subtype analysis is needed
  - characterize maintenance-state and differentiated organoids with morphology, immunostaining, lineage-marker assays, and optionally single-cell profiling
  - generate a stable Cas9-BFP trophoblast stem-cell line using PiggyBac-based Cas9 delivery and select uniformly BFP-positive colonies
  - construct focused sgRNA libraries, determine viral titer, and transduce the Cas9-expressing trophoblast stem cells at low multiplicity before organoid formation
  - run the screen at an MOI around 0.3 with a coverage ratio typically in the 100 to 1,000 range, then sequence sgRNA representation and analyze the data with MAGeCK
- Key validation: maintenance cultures can remain stable for more than 6 months across 13 passages, mTOs and mPOs show distinct growth rates, differentiated organoids express expected trophoblast-lineage markers, and screen sequencing is considered robust when at least about 99.5% library coverage and roughly 60% mapped reads are achieved
- Distinct protocol emphasis: this is one of the clearest examples in the corpus of turning an organoid system into a pooled-functional-screening platform rather than stopping at differentiation alone

## Key findings

- Makes placental organoids experimentally actionable by explicitly connecting derivation, differentiation, and CRISPR screening logistics in one workflow.
- Treats MOI and library coverage as first-class design parameters rather than afterthoughts, which is essential for interpretable screening.
- Highlights that the organoids support a broader trophoblast subtype balance than simpler cell systems, making them attractive for developmental-regulator discovery.
- Provides a useful benchmark for when an organoid screen is technically good enough to trust, including mapped-read and coverage expectations.

## Distinctive contribution in this corpus

- One of the most explicit pooled-screening protocols in the collection outside the neural CRISPR papers.
- Strengthens the engineering concept page with a non-brain example where screen design and organoid-state quality are both central.
- Gives the placental branch a practical upgrade from "interesting developmental model" to "screenable discovery platform."

## Limitations and caveats

- Screen quality is highly sensitive to library quality, targeting efficiency, viral titer, and maintenance of low MOI.
- Large libraries quickly become expensive and noisy in this format because coverage requirements scale sharply.
- The differentiated trophoblast states remain dependent on culture context and may vary with derivation conditions or genetic background.
- This is a murine trophoblast system, so it is not a direct substitute for human placental organoid questions.

## Relevance to corpus

- Strengthens the engineering and screening branch with a screen-ready placental system.
- Useful when the question is how to connect organoid subtype complexity to gene-function discovery rather than only phenotype description.
- Serves as a concrete bridge between baseline trophoblast organoid derivation and pooled perturbation experiments.

## Related concepts

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)

## Related sources

- [Establishment and differentiation of long-term trophoblast organoid cultures from the human placenta](sheridan_2020_establishment_and_differentiation_of_long-term.md) - the closest trophoblast-organoid comparator for derivation and differentiation without the screening layer.
- [Protocol to create isogenic disease models from adult stem cell-derived organoids using next-generation CRISPR tools](m_2024_protocol-to-create-isogenic-disease-models-from-adult-stem-cell-derived-organoids-using-ne.md) - a complementary organoid-editing paper focused on precise engineering rather than pooled screening.
- [CRISPR screens in human neural organoids and assembloids](meng_2025_crispr_screens_in_human_neural.md) - a brain-screening comparator that helps frame how unusual it is to have a similar screen-ready workflow in placental organoids.

## Open questions

- How well do hit lists from murine trophoblast screens transfer to human placental organoid contexts?
- What is the best tradeoff between library size and signal quality in organoid-based trophoblast screening?
- Which differentiation state should be screened first when the biological question concerns lineage specification versus mature trophoblast function?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:31:52+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc -f json,markdown`
- Manifest: [raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/opendataloader-run.json](../../raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/opendataloader-run.json)
- Output: [raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc.json](../../raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc.json)
- Output: [raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc.md](../../raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc.md)
- Output: [raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile1.png](../../raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile1.png)
- Output: [raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile2.png](../../raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile2.png)
- Output: [raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile3.png](../../raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile3.png)
- Output: [raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile4.png](../../raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile4.png)
- Output: [raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile5.png](../../raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile5.png)
- Output: [raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile6.png](../../raw/derived/opendataloader/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc_images/imageFile6.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
