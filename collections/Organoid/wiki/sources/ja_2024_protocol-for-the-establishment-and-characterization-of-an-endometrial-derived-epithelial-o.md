---
title: Protocol for the establishment and characterization of an endometrial-derived epithelial organoid and stromal cell co-culture system.
kind: paper
status: ingested
added: 2026-04-21T20:27:39+09:00
raw_source: raw/sources/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10879800/
published_date: 2024-02-16
organ: endometrium
protocol_focus: the establishment and characterization of an endometrial-derived epithelial organoid and stromal cell co-culture system
deep_ingested: 2026-04-22
---

# Protocol for the establishment and characterization of an endometrial-derived epithelial organoid and stromal cell co-culture system.

## Source

- PDF: [raw/sources/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.pdf](../../raw/sources/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC10879800/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10879800/)
- Status: deep ingested 2026-04-22
- Organ focus: murine endometrial epithelial organoids paired with primary uterine stromal fibroblasts
- Protocol focus: same-system epithelial plus stroma co-culture for paracrine control of endometrial organoid development

## Study design

- Starting material: epithelial and stromal cells isolated from juvenile mouse uterus, with the protocol designed so both populations can be obtained from the same animals
- Protocol stages:
  - dissect postnatal day-15 mouse uteri and use sequential enzymatic digestion to isolate epithelial sheets and stromal fractions
  - establish endometrial epithelial organoids and expand them for characterization, typically passaging at 1:3 every 5 to 7 days
  - culture stromal fibroblasts in 2D to build a confluent feeder-like stromal layer
  - seed stromal cells 24 h before assay start so they reach roughly 70% confluence when epithelial organoid inserts are introduced
  - maintain co-cultures for about 20 days, renewing stroma every 5 days and passaging epithelial organoids every 6 to 8 days, with optional hormone treatment such as E2
- Key validation: KRT7-positive columnar epithelial identity, KRT5 and p63 basal markers, and the Esr1-KO phenotype that shifts toward basal differentiation unless restrained by stromal co-culture
- Distinct protocol emphasis: the biological question is explicitly stromal-derived paracrine control of epithelial fate, not organoid growth alone

## Key findings

- Separates epithelial and stromal contributions cleanly enough to test how stromal paracrine signals alter organoid growth and lineage state.
- Uses a paired isolation strategy that keeps the epithelial and stromal components biologically aligned.
- Demonstrates a concrete phenotype for the system: stromal co-culture suppresses the abnormal basal differentiation seen in Esr1-knockout organoids.
- Creates a manageable reproductive-tissue analog of the broader epithelial-stroma coculture logic seen elsewhere in the corpus.

## Distinctive contribution in this corpus

- One of the clearest non-gastrointestinal coculture protocols in the collection, which helps keep the assay-layer concept page from being intestine-only.
- Adds a genuinely multicompartment epithelial-plus-stroma example to the adult-platform branch.
- Useful as a compact model of organoid biology being reshaped by adjacent non-epithelial tissue rather than by a distant soluble factor screen alone.

## Limitations and caveats

- The protocol is optimized in mouse tissue and is not yet fully optimized for primary human endometrial co-culture.
- It still lacks vasculature and broader uterine microenvironment complexity, so the stromal compartment is only a partial in vivo proxy.
- Stromal confluence is a hard operational dependency; under-confluent stroma weakens the assay.
- Early-passage epithelial cells can attach to plastic and drift toward unwanted 2D behavior if handling during passaging is rough.

## Relevance to corpus

- Strengthens the coculture concept page with a stromal-epithelial assay rather than an immune or microbial one.
- Broadens the adult or patient-derived branch with a reproductive-tissue protocol that still uses the same core logic of matched tissue-derived organoid platforms.
- Useful whenever the user wants to reason about what a stromal compartment adds to an epithelial organoid assay.

## Related concepts

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)

## Related entities

- [Reproductive mucosal epithelial organoids](../entities/reproductive-mucosal-epithelial-organoids.md)
- [Adult tissue-derived epithelial organoids](../entities/adult-tissue-derived-epithelial-organoids.md)

## Related sources

- [Protocol for the coculture of murine vaginal epithelial organoids and T cells to induce resident memory CD8 T cell differentiation](jc_2025_protocol-for-the-coculture-of-murine-vaginal-epithelial-organoids-and-t-cells-to-induce-re.md) - another reproductive-tissue coculture protocol, but with immune cells instead of stroma.
- [Protocol for modeling the repair of intestinal damage by co-culturing mesenchymal stromal/stem cells and intestinal organoids](kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.md) - a gastrointestinal analog focused on stromal support after injury.
- [Long-term culture, genetic manipulation and xenotransplantation of human normal and breast cancer organoids](dekkers_2021_long-term_culture_genetic_manipulation_and.md) - another adult-tissue organoid framework that becomes more informative once paired with a non-epithelial context.

## Open questions

- Which stromal signals are truly paracrine drivers of epithelial state versus indirect correlates of culture quality?
- How far can this mouse workflow be pushed toward primary human endometrial coculture without losing robustness?
- What additional uterine compartments would matter most after stroma: immune, vascular, or endocrine control?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:28:39+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o -f json,markdown`
- Manifest: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/opendataloader-run.json](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/opendataloader-run.json)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.json](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.json)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.md](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.md)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile1.png](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile1.png)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile2.png](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile2.png)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile3.png](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile3.png)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile4.png](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile4.png)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile5.png](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile5.png)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile6.png](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile6.png)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile7.png](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile7.png)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile8.png](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile8.png)
- Output: [raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile9.png](../../raw/derived/opendataloader/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
