---
title: Protocol for transducing human primary epithelial prostate cells and patient-derived organoids with high efficiency.
kind: paper
status: ingested
added: 2026-04-21T20:28:00+09:00
raw_source: raw/sources/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11315182/
published_date: 2024-07-18
organ: prostate
protocol_focus: transducing human primary epithelial prostate cells and patient-derived organoids with high efficiency
deep_ingested: 2026-04-22
---

# Protocol for transducing human primary epithelial prostate cells and patient-derived organoids with high efficiency.

## Source

- PDF: [raw/sources/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.pdf](../../raw/sources/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11315182/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11315182/)
- Status: deep ingested 2026-04-22
- Organ focus: human primary prostate epithelial cells and prostate patient-derived organoids, with reported transferability to other organoid types
- Protocol focus: high-efficiency lentiviral transduction for knockdown or overexpression before organoid re-seeding

## Study design

- Starting material: human primary prostate epithelial cells and prostate PDOs, with additional in-lab use on mouse mammary and mouse prostate organoids
- Protocol stages:
  - produce lentivirus in Lenti-X 293T cells using shRNA or overexpression vectors
  - passage primary epithelial cells into suspension and prepare the transduction mix before 3D re-seeding
  - combine cells and virus immediately before forming Matrigel domes, using a workflow designed to avoid repeated harsh digestion steps
  - seed domes with a 25% cell-plus-virus suspension and 75% Matrigel, then expand cells in prostate organoid medium
  - measure transduction efficiency with GFP and validate knockdown at mRNA and protein level
- Distinct protocol emphasis: the key move is infecting the cells in suspension just before organoid reconstitution, rather than trying to force virus into already formed dense 3D organoids
- Key validation: the paper reports strong GFP signal and greater than 80% protein-level knockdown for IDH1 in prostate cancer PDOs, alongside successful modulation of ERa-related biology

## Key findings

- Provides a relatively low-friction viral-delivery route for adult or patient-derived organoids that avoids the throughput hit of repeated mechanical and enzymatic processing.
- Supports both shRNA knockdown and lentiviral overexpression, making the workflow broadly useful beyond one prostate-specific perturbation.
- Turns primary prostate epithelial culture into an engineering-ready intermediate rather than a dead end before organoid formation.
- Suggests the method is portable to other epithelial organoid contexts, not just prostate PDOs.

## Distinctive contribution in this corpus

- One of the clearest refill-era papers for the transition from adult or patient-derived organoid establishment into routine perturbation.
- Strengthens the adult-platform branch by showing that patient-derived organoids are not only biologically relevant but also technically tractable for gene-delivery experiments.
- Gives the engineering concept page a practical viral-delivery complement to the genome-editing papers already in the deep-ingested set.

## Limitations and caveats

- Results vary across patients, both in organoid-forming capacity and in transduction success.
- The protocol does not include formal virus titration, so exact viral particle input remains approximate unless users add that step themselves.
- Efficient organoid formation still depends on using low-passage primary cells; high-passage cells may fail during reconstitution.
- Matrigel timing is operationally important because rapid polymerization can compromise consistent dome formation.

## Relevance to corpus

- Strengthens the overlap between adult stem cell or patient-derived platforms and engineering workflows.
- Useful whenever the practical question is how to perturb a donor-derived epithelial organoid without abandoning the PDO system for easier 2D cell lines.
- Adds a prostate-specific counterpart to more general editing workflows elsewhere in the collection.

## Related concepts

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Related entities

- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)

## Related sources

- [Organoid culture systems for prostate epithelial and cancer tissue](drost_2016_organoid_culture_systems_for_prostate.md) - the core baseline for prostate organoid establishment before perturbation.
- [Protocol to create isogenic disease models from adult stem cell-derived organoids using next-generation CRISPR tools](m_2024_protocol-to-create-isogenic-disease-models-from-adult-stem-cell-derived-organoids-using-ne.md) - a complementary adult-organoid engineering paper centered on genome editing rather than lentiviral delivery.
- [Long-term culture, genetic manipulation and xenotransplantation of human normal and breast cancer organoids](dekkers_2021_long-term_culture_genetic_manipulation_and.md) - another example of adult organoids becoming perturbable systems instead of just stable cultures.

## Open questions

- How broadly does the suspension-phase transduction logic transfer across adult organoid systems with different fragility profiles?
- When is viral delivery preferable to electroporation or CRISPR-based editing for patient-derived organoid studies?
- Which prostate PDO phenotypes remain stable enough after transduction to support longer-term mechanistic assays?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:28:22+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ -f json,markdown`
- Manifest: [raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/opendataloader-run.json](../../raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/opendataloader-run.json)
- Output: [raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.json](../../raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.json)
- Output: [raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.md](../../raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.md)
- Output: [raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ_images/imageFile1.png](../../raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ_images/imageFile1.png)
- Output: [raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ_images/imageFile2.png](../../raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ_images/imageFile2.png)
- Output: [raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ_images/imageFile3.png](../../raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ_images/imageFile3.png)
- Output: [raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ_images/imageFile4.png](../../raw/derived/opendataloader/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ_images/imageFile4.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
