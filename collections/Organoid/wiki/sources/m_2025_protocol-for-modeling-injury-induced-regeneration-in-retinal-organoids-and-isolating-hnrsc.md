---
title: Protocol for modeling injury-induced regeneration in retinal organoids and isolating hNRSCs for subretinal transplantation in rd10 mice.
kind: paper
status: ingested
added: 2026-04-21T20:25:46+09:00
raw_source: raw/sources/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12702322/
published_date: 2025-11-27
organ: retina
protocol_focus: retinal organoid injury-repair modeling, CPAMD8-positive hNRSC isolation, and subretinal transplantation
deep_ingested: 2026-04-22
---

# Protocol for modeling injury-induced regeneration in retinal organoids and isolating hNRSCs for subretinal transplantation in rd10 mice.

## Source

- PDF: [raw/sources/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc.pdf](../../raw/sources/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12702322/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12702322/)
- Status: deep ingested 2026-04-22
- Organ focus: hESC-derived retinal organoids with ciliary-margin-like regenerative zones
- Protocol focus: turning retinal organoids into a staged injury-repair assay, isolating CPAMD8-positive hNRSCs, and testing them by rd10 subretinal transplantation

## Study design

- Starting material: human ESC-derived retinal organoids, with an optional VSX2-P2A-tdTomato reporter line for dissection guidance
- Protocol stages:
  - differentiate hESCs into retinal organoids with a BMP4-based workflow, moving aggregates into suspension at day 18 and trimming low-quality, cystic, or fused structures through roughly days 20 to 30
  - continue maturation until the 60 to 75 day window where organoids show a clear CMZ-like region and laminated retinal architecture
  - surgically remove the central neural-retina domain while preserving the CMZ-like rim and pigmented epithelium, then track repair at R5, R10, R20, and R40
  - isolate the regenerative population at R5, when MECOM peaks, by dissociation and FACS sorting for CPAMD8-positive hNRSCs
  - transplant sorted cells into the subretinal space of 3 to 4 week rd10 mice using a 33 G Hamilton syringe, with cyclosporine A immunosuppression starting 24 h before surgery
- Key validation: injured organoids show regenerative cell migration and marker induction, the workflow yields roughly 100,000 to 200,000 CPAMD8-positive cells from 10 organoids with greater than 90% viability, and transplanted cells integrate into outer retinal layers with previously reported ERG improvement
- Distinct protocol emphasis: the paper turns retinal organoids into a regenerative assay pipeline rather than stopping at developmental differentiation

## Key findings

- Uses deliberate microsurgical injury to activate an otherwise quiescent CMZ-like stem-like compartment, making hNRSC recovery experimentally feasible.
- Makes the temporal logic explicit: R5 is the harvest window because MECOM expression peaks there.
- Standardizes a full chain from organoid differentiation to repair imaging, FACS isolation, and in vivo validation instead of treating these as separate ad hoc methods.
- Shows that the sorted cells are numerous enough and viable enough for downstream transplantation, which is often the hidden practical bottleneck in regeneration workflows.
- Moves the retinal organoid from descriptive morphology toward regenerative testing by tying injury-induced repair to transplantation-readout logic.

## Distinctive contribution in this corpus

- One of the clearest repair-oriented organoid protocols in the collection.
- Gives the functional-assay branch a retinal example where the key question is endogenous stem-like activation after injury, not only coculture, infection, or generic transplantation.
- Helps the corpus cover organoid use cases where the desired output is a candidate therapeutic cell population rather than a stable long-term organoid line.

## Limitations and caveats

- The injury step depends on manual microsurgery, so operator skill strongly affects reproducibility.
- CPAMD8 is a useful practical enrichment marker, but it may not capture the full regenerative stem-like compartment.
- rd10 transplantation adds substantial surgical and host-variability burdens, and the rapid degeneration of the model constrains longer-term follow-up.
- The protocol paper itself focuses on isolation and transplantation workflow; deeper functional rescue analysis is delegated to the companion study rather than fully reproduced here.

## Relevance to corpus

- Strengthens the host-validation side of the corpus with a non-cortical regenerative example.
- Useful when the question is whether an organoid can reveal, isolate, and test an injury-responsive progenitor population rather than just recreate tissue identity.
- Serves as a good comparator for other assay-layer papers where in vivo escalation is necessary to evaluate whether an in vitro phenotype matters.

## Related concepts

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)

## Related sources

- [Host circuit engagement of human cortical organoids transplanted in rodents](kelley_2024_host_circuit_engagement_of_human.md) - another protocol where organoid claims are pushed into an in vivo host to test whether they survive functional escalation.
- [Protocol to enhance pre-sexual and sexual differentiation of Toxoplasma gondii using retinal cells and intestinal organoid-derived monolayers](s_2026_protocol-to-enhance-pre-sexual-and-sexual-differentiation-of-toxoplasma-gondii-using-retin.md) - a different retinal assay-layer paper in which the retinal tissue serves as a host context rather than a transplantation source.
- [Protocol for modeling the repair of intestinal damage by co-culturing mesenchymal stromal/stem cells and intestinal organoids](kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.md) - a non-neural repair paper that helps compare how organoid injury models are operationalized across tissues.

## Related entities

- [Host-context transplantation and repair validation](../entities/host-context-transplantation-and-repair-validation.md)

## Open questions

- How specific is CPAMD8 for the most therapeutically relevant regenerative retinal stem-like cells?
- Which parts of the observed benefit after transplantation reflect true lineage replacement versus trophic or structural support?
- Can this workflow be scaled beyond careful microsurgical proof-of-concept into a more throughput-friendly regenerative screening platform?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:25:56+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc -f json,markdown`
- Manifest: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/opendataloader-run.json](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/opendataloader-run.json)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc.json](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc.json)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc.md](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc.md)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile1.png](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile1.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile2.png](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile2.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile3.png](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile3.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile4.png](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile4.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile5.png](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile5.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile6.png](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile6.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile7.png](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile7.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile8.png](../../raw/derived/opendataloader/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc_images/imageFile8.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
