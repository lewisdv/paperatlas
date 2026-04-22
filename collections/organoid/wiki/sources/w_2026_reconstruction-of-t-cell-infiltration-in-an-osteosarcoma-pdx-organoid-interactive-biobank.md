---
title: Reconstruction of T cell infiltration in an osteosarcoma PDX-organoid interactive biobank for personalized immunotherapy
kind: paper
status: ingested
added: 2026-04-21T14:30:15+09:00
raw_source: raw/sources/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13006418/
published_date: 2026-02-27
organ: organoid-system
protocol_focus: reconstruction of T cell infiltration in an osteosarcoma PDX-organoid interactive biobank for personalized immunotherapy
deep_ingested: 2026-04-22
---

# Reconstruction of T cell infiltration in an osteosarcoma PDX-organoid interactive biobank for personalized immunotherapy

## Source

- PDF: [raw/sources/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.pdf](../../raw/sources/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC13006418/](https://pmc.ncbi.nlm.nih.gov/articles/PMC13006418/)
- Status: deep ingested 2026-04-22
- Organ focus: osteosarcoma patient- and PDX-derived self-assembled tumor organoids used for immune-reconstruction and immunotherapy testing
- Protocol focus: build a rapid osteosarcoma PDX-organoid biobank, then reconstruct T cell infiltration with PBMC coculture so immune-response questions can be tested in a tumor architecture that still resembles paired tissue

## Study design

- Starting material: necrosis-free osteosarcoma specimens from patients or matched PDX tissue, enzymatically dissociated to viable single-cell suspensions
- Protocol stages:
  - derive individualized osteosarcoma organoids by plating about 2 x 10^5 cells in 50 uL into round-bottom ultra-low-attachment wells, centrifuging briefly, overlaying with a Matrigel:culture-medium mix at 3:2, and maturing self-assembled iOS structures over 5-7 days
  - validate organoid fidelity against paired tissues and PDXs using histology, spatial features, whole-genome profiling, transcriptomics, and pharmacogenomic comparison
  - pre-activate PBMCs with anti-CD3, anti-CD28, and IL-2, then mix them with dissociated iOS cells at roughly 1:1 to reconstruct T cell infiltration over 7-10 days
  - score successful immune reconstruction using both infiltration and function criteria, including at least 2% CD8-positive or CD45-positive cells plus Granzyme B and Perforin readouts, then test immunotherapy-response logic including anti-PD1 and PRMT5-MTA inhibition
- Key validation: the overall iOS establishment rate was 74.2% across 93 attempts, workflows could be completed in about 10 days, the models preserved major osteosarcoma genomic lesions such as MYC amplification, RB1 deletion, and CDKN2A deletion, and CD8 infiltration remained stable while the platform supported combination-immunotherapy testing in Chr9p21.3-deleted disease
- Distinct protocol emphasis: this paper treats self-assembly, fidelity benchmarking, and immune reconstruction as one interactive cancer-modeling pipeline rather than three separate systems

## Summary

- The paper matters because it turns osteosarcoma organoids from static ex vivo models into an interactive platform that can reintroduce immune cells on demand.
- It also shows that large, millimeter-scale tumor organoids can still be practical if assembly speed, size control, and readout design are handled explicitly.
- Within this corpus, it belongs to the patient-derived cancer branch where organoid engineering and functional coculture become inseparable.

## Key findings

- Patient- and PDX-derived osteosarcoma iOS models can be generated quickly enough for short-turnaround experimental use without collapsing tumor architecture into a flat assay.
- PDX-derived models preserve the key tumor genotype well, but they arrive immunologically depleted, so PBMC reconstitution becomes a deliberate repair move rather than a biological nuisance.
- The paper makes size itself a protocol variable: around 1000 um supports better immune infiltration, whereas larger organoids accumulate more hypoxia and apoptosis.
- The combination of matched PDXs, iOSs, and reconstructed immune context lets the authors test immunotherapy logic in a system that is faster than full in vivo work but much richer than tumor cells alone.

## Distinctive contribution in this corpus

- One of the strongest tumor-organoid papers here for showing how to rebuild a missing compartment rather than simply lamenting its absence.
- Gives the functional-assay branch an immune-reconstruction cancer model that sits between classic tumor-organoid T-cell coculture and slow in vivo immunotherapy work.
- Also broadens the engineering or screening branch because the organoid is explicitly designed as a rapid, assay-ready biobank substrate.

## Limitations and caveats

- PBMC addition is still a synthetic reconstruction and cannot fully restore the bone, stromal, and myeloid ecosystem of native osteosarcoma.
- PDX-derived organoids are easier to establish than direct patient organoids, but that convenience also shifts the model further from the original human immune context.
- The rapid workflow is a major strength, yet it may underrepresent slower remodeling processes that appear only after longer tumor-host interaction.

## Relevance to corpus

- Strengthens the functional-assay and adult-platform concept paths with a clear example of how to turn a patient- or PDX-derived tumor organoid into an immunotherapy testbed.
- Useful when the question is not just whether a tumor organoid can be grown, but how to repair the missing immune layer without abandoning throughput entirely.
- Helps connect tumor-biobank logic, immune coculture, and translational combination-therapy design inside one protocol family.

## Related concepts

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Related sources

- [Tumor organoid-T-cell coculture systems](cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md) - a simpler tumor-immune coculture comparator without the PDX-linked biobank and size-control logic.
- [Protocol for generation and utilization of patient-derived organoids from multimodal specimen](s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.md) - another translational paper where specimen handling and rapid assay readiness are treated as core platform features.
- [Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids](j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md) - a host-restoration comparator showing a different route for recovering context-sensitive biology lost in isolated tumor organoid culture.

## Open questions

- Which additional immune compartments, beyond PBMC-derived T cells and macrophage-like populations, would most improve predictive fidelity for osteosarcoma immunotherapy?
- When should direct patient-derived iOS models be preferred over easier-to-establish PDX-derived iOS models despite the lower success rate?
- How often will the 1000 um size sweet spot generalize across osteosarcoma subtypes or across other solid-tumor organoid biobanks?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:50:48+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank -f json,markdown`
- Manifest: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/opendataloader-run.json](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/opendataloader-run.json)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.json](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.json)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.md](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.md)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile1.png](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile1.png)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile2.png](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile2.png)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile3.png](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile3.png)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile4.png](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile4.png)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile5.png](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile5.png)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile6.png](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile6.png)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile7.png](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile7.png)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile8.png](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile8.png)
- Output: [raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile9.png](../../raw/derived/opendataloader/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
