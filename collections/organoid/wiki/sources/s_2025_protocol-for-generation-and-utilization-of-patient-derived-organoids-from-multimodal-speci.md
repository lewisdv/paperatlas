---
title: Protocol for generation and utilization of patient-derived organoids from multimodal specimen.
kind: paper
status: ingested
added: 2026-04-21T20:27:49+09:00
raw_source: raw/sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12395520/
published_date: 2025-08-18
organ: tumor
protocol_focus: generation and utilization of patient-derived organoids from multimodal specimen
deep_ingested: 2026-04-22
---

# Protocol for generation and utilization of patient-derived organoids from multimodal specimen.

## Source

- PDF: [raw/sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.pdf](../../raw/sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12395520/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12395520/)
- Status: deep ingested 2026-04-22
- Organ focus: cross-cancer patient-derived tumor organoids from surgical tissue, core biopsies, and liquid biopsy-like specimens
- Protocol focus: standardized specimen-to-PDO pipeline spanning collection, dissociation, biobanking, QC, and drug screening

## Study design

- Starting material: patient tumor material collected as resection tissue, punch or needle biopsy, EUS-FNB, percutaneous liver biopsy, ascites, or pleural effusion
- Protocol stages:
  - prepare transport media, dissociation reagents, and tumor-type-specific PDO media before specimen arrival
  - process surgical samples by mincing and controlled enzymatic plus mechanical dissociation, using gentleMACS when available but allowing simpler alternatives for low-input samples
  - process liquid or fluid specimens with enrichment steps such as density separation and RBC removal when needed
  - seed dissociated material in BME, stabilize and passage organoids, then bank lines for future use
  - run freeze-thaw QC, histology or IHC concordance checks, STR-style validation, and high-throughput drug screening once cultures stabilize
- Key validation: the paper emphasizes stabilized organoid growth over serial days, post-thaw regrowth checks, and histologic concordance with original specimens as quality gates before downstream screening
- Distinct protocol emphasis: this is not one tumor protocol but a specimen-logistics framework for making PDOs work in patients who cannot contribute large surgical resections

## Key findings

- Broadens PDO accessibility from surgery-only workflows to smaller biopsies and body-fluid specimens.
- Treats specimen handling, tumor cellularity, and dissociation strategy as first-order determinants of PDO success.
- Integrates biobanking, thaw validation, and screening into the same operating pipeline rather than leaving them as separate downstream improvisations.
- Makes the case that translational PDO programs are as much about specimen logistics as they are about media recipes.

## Distinctive contribution in this corpus

- One of the strongest patient-derived platform papers in the refill cohort because it systematizes how to work with real-world low-input clinical material.
- Complements more organ-specific PDO papers by adding the missing biobank and specimen-diversity layer.
- Helps the collection speak to translational deployment, not only to technically ideal lab specimens.

## Limitations and caveats

- Tumor cellularity is the central bottleneck; high stromal or immune content can make even adequately sized samples fail.
- Digestion must be tuned to tissue stiffness but should not exceed about 1 h because prolonged treatment reduces viability.
- Fibroblast overgrowth, RBC carryover, and microbiota contamination can each derail establishment before organoids stabilize.
- Media optimization remains tumor-type specific, so the pipeline is standardized at the specimen-handling level more than at the niche-factor level.

## Relevance to corpus

- Strengthens the adult stem cell and patient-derived concept page with a cross-cancer operational framework rather than one organ-specific example.
- Useful whenever the practical question is how to build a PDO workflow from whatever specimen a clinic can actually provide.
- Adds a translational bridge from PDO establishment to banking and drug-screening deployment.

## Related concepts

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)

## Related entities

- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)

## Related sources

- [Establishment of patient-derived cancer organoids for drug-screening applications](driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) - the clearest earlier PDO baseline for downstream screening.
- [Protocol for the establishment and characterization of South African patient-derived intestinal organoids](n_2025_protocol-for-the-establishment-and-characterization-of-south-african-patient-derived-intes.md) - a more organ-specific patient-derived intestinal comparator with strong emphasis on specimen handling.
- [Protocol for transducing human primary epithelial prostate cells and patient-derived organoids with high efficiency](c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.md) - shows what becomes possible once multimodal-specimen PDOs are stable enough for perturbation.

## Open questions

- Which specimen types contribute the best tradeoff between clinical accessibility and organoid establishment rate?
- How much can tumor-cell enrichment be pushed before selective loss of clinically relevant subclones becomes a problem?
- What minimal QC panel is sufficient before a newly established PDO line is trusted for treatment-guidance style drug screening?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:28:55+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci -f json,markdown`
- Manifest: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/opendataloader-run.json](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/opendataloader-run.json)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.json](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.json)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.md](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.md)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile1.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile1.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile10.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile10.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile11.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile11.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile12.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile12.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile13.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile13.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile14.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile14.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile15.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile15.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile16.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile16.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile17.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile17.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile2.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile2.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile3.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile3.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile4.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile4.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile5.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile5.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile6.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile6.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile7.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile7.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile8.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile8.png)
- Output: [raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile9.png](../../raw/derived/opendataloader/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
