---
title: Protocol to generate genetically engineered organoid-initiated mouse models of esophageal cancer.
kind: paper
status: ingested
added: 2026-04-21T20:28:08+09:00
raw_source: raw/sources/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12361750/
published_date: 2025-08-12
organ: esophagus
protocol_focus: generate genetically engineered organoid-initiated mouse models of esophageal cancer
deep_ingested: 2026-04-22
---

# Protocol to generate genetically engineered organoid-initiated mouse models of esophageal cancer.

## Source

- PDF: [raw/sources/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.pdf](../../raw/sources/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12361750/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12361750/)
- Status: deep ingested 2026-04-22
- Organ focus: murine esophageal organoids edited ex vivo and transplanted orthotopically to form squamous-cell-carcinoma models
- Protocol focus: build genetically defined organoid-initiated precision cancer models in vivo faster than full GEMM workflows

## Study design

- Starting material: primary esophageal epithelial cells isolated from Trp53-null Cas9-expressing mice
- Protocol stages:
  - isolate mouse esophageal primary cells and establish organoids in Matrigel, typically using 1000 to 3000 cells per 30 uL dome
  - expand organoids for roughly one week under conditions tuned for esophageal epithelial growth
  - introduce sgRNA-based knockout and oncogene overexpression constructs into organoids, then validate editing by Sanger sequencing and qPCR
  - collect approximately 500 edited organoids and transplant them orthotopically into the esophageal mucosa near the gastroesophageal junction by laparotomy
  - monitor tumor growth by luciferase imaging and confirm squamous-carcinoma identity histologically and by marker staining
- Key validation: the paper reports in situ esophageal squamous cell carcinoma formation within about 20 days in nude recipients, with TP63, KRT5, KRT13, and KRT14 marker support
- Distinct protocol emphasis: this is a hybrid platform that starts with ex vivo organoid engineering but insists on orthotopic in vivo validation as the real endpoint

## Key findings

- Compresses the path from genotype design to orthotopic cancer model compared with breeding-heavy genetically engineered mouse models.
- Makes combinatorial cancer-genotype testing feasible by editing organoids before transplantation.
- Preserves anatomical context better than subcutaneous transplantation by injecting edited organoids into the esophageal mucosa.
- Demonstrates that organoid engineering and host-context testing can be one continuous workflow rather than two separate model systems.

## Distinctive contribution in this corpus

- One of the strongest bridge papers in the corpus between engineering and transplantation.
- Gives the collection a cancer-modeling analog to regenerative transplantation papers: here the host context is used to test tumorigenicity and orthotopic growth rather than repair.
- Clarifies what "organoid-initiated mouse model" really means operationally, including the surgical bottlenecks and in vivo validation markers.

## Limitations and caveats

- Orthotopic surgery is technically demanding because the mouse esophageal wall is thin and easy to puncture incorrectly.
- The model places the graft at the gastroesophageal junction, which does not fully recapitulate the upper or mid-esophageal locations common in human ESCC.
- The esophagus is non-sterile and prone to contamination during tissue isolation.
- The genetic strategy captures selected gene combinations more readily than large chromosomal alterations common in patient tumors.

## Relevance to corpus

- Strengthens both the engineering and functional-transplantation concept pages with a cancer-focused host-validation workflow.
- Useful whenever the question is whether an engineered organoid phenotype survives contact with tissue context and tumor ecology in vivo.
- Provides a strong template for orthotopic organoid-initiated disease modeling outside the brain and gut-repair examples already in the corpus.

## Related concepts

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Related entities

- [Host-context transplantation and repair validation](../entities/host-context-transplantation-and-repair-validation.md)

## Related sources

- [Long-term culture, genetic manipulation and xenotransplantation of human normal and breast cancer organoids](dekkers_2021_long-term_culture_genetic_manipulation_and.md) - another adult-organoid paper that explicitly bridges genetic manipulation and in vivo follow-up.
- [Transplantation of intestinal organoids into a mouse model of colitis](watanabe_2022_transplantation_of_intestinal_organoids_into.md) - a non-cancer transplantation comparator where the in vivo endpoint is repair rather than tumorigenesis.
- [Protocol to create isogenic disease models from adult stem cell-derived organoids using next-generation CRISPR tools](m_2024_protocol-to-create-isogenic-disease-models-from-adult-stem-cell-derived-organoids-using-ne.md) - a complementary ex vivo engineering workflow that stops before the host-validation step.

## Open questions

- Which edited genotype combinations produce the strongest tradeoff between biological realism and surgical tractability in this model?
- How generalizable is the organoid-initiated precision cancer model framework across other anatomically difficult organs?
- What host-context phenotypes appear only after orthotopic growth and would be missed entirely in vitro?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:28:34+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal -f json,markdown`
- Manifest: [raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/opendataloader-run.json](../../raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/opendataloader-run.json)
- Output: [raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.json](../../raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.json)
- Output: [raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.md](../../raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.md)
- Output: [raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile1.png](../../raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile1.png)
- Output: [raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile2.png](../../raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile2.png)
- Output: [raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile3.png](../../raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile3.png)
- Output: [raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile4.png](../../raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile4.png)
- Output: [raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile5.png](../../raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile5.png)
- Output: [raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile6.png](../../raw/derived/opendataloader/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal_images/imageFile6.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
