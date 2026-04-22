---
title: Protocol for differentiating human pluripotent stem cells into midbrain organoids for targeted microinjection of viruses.
kind: paper
status: ingested
added: 2026-04-21T20:30:50+09:00
raw_source: raw/sources/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12318278/
published_date: 2025-07-25
organ: midbrain
protocol_focus: differentiating human pluripotent stem cells into midbrain organoids for targeted microinjection of viruses
deep_ingested: 2026-04-22
---

# Protocol for differentiating human pluripotent stem cells into midbrain organoids for targeted microinjection of viruses.

## Source

- PDF: [raw/sources/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.pdf](../../raw/sources/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12318278/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12318278/)
- Status: deep ingested 2026-04-22
- Organ focus: hPSC-derived midbrain organoids with a ventricular-zone-targeted viral delivery workflow
- Protocol focus: staged midbrain differentiation plus targeted viral microinjection into the organoid interior

## Study design

- Starting material: human pluripotent stem cells
- Protocol stages:
  - day 0 neural induction with SB431542, DMH1, CHIR99021, and SHHC25
  - days 2 to 8 half-medium changes to maintain early patterned neural induction in 6-well plates
  - day 9 transfer partially dissociated colonies into flask culture, where rosette-like and tube-like structures become apparent
  - days 11 to 13 continue patterning with CHIR99021, SHHC25, and SAG; day 14 switches to FGF8b plus SAG; days 20 to 34 move into neural maturation with FGF8b plus low-dose SHHC25
  - once organoids are established, use a microsyringe plus glass-electrode setup to deliver virus directly into ventricular-zone-like regions
- Key validation: by day 30 the organoids show strong OTX2 and FOXA2 dopaminergic-progenitor identity, by day 60 they contain TH-positive neurons, and post-injection cultures show low cell death with sustained reporter expression in internal organoid regions
- Distinct protocol emphasis: the assay innovation is physical access to the organoid interior, enabling lower viral load and more localized infection than bulk exposure methods

## Key findings

- Pairs a reasonably standard patterned midbrain derivation with a practical solution to one of the field's persistent problems: how to perturb cells deep inside a 3D organoid.
- Targeted microinjection improves spatial precision while reducing viral dosage, cytotoxicity, and tissue disruption.
- The protocol explicitly notes that serotype and promoter choice matter, with AAV9 and synapsin highlighted as effective for neuronal targeting.
- Demonstrates that infected cells can be maintained and visualized over time without grossly compromising organoid architecture.

## Distinctive contribution in this corpus

- One of the clearest brain papers in this collection for solving assay access rather than just generating a new organoid subtype.
- Bridges the gap between subregion-specific brain organoid generation and downstream perturbation workflows such as infection, reporter delivery, or targeted gene-expression studies.
- Makes the midbrain cluster more operational by showing how a mature patterned organoid can be used as an experimental substrate, not only as a developmental endpoint.

## Limitations and caveats

- Best treated as an assay-layer protocol on top of a stable midbrain organoid workflow; malformed or weakly patterned organoids will undermine the injection step.
- The microinjection setup is technically demanding and lower throughput than bulk viral exposure.
- Viral serotype, promoter choice, and injection location require re-optimization when the target cell class or payload changes.
- The day-9 transfer and detachment step is a practical failure point, with low survival and uneven cluster release explicitly called out in troubleshooting.

## Relevance to corpus

- Strengthens the brain subregion and assay-layer branches of the corpus at the same time.
- Useful whenever the practical question is how to deliver viruses, reporters, or perturbations into internal organoid compartments without sacrificing structure.
- Complements neural screen and perturbation papers by adding the missing physical-delivery layer for midbrain organoids.

## Related concepts

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Brain subregion-specific organoid protocols](../concepts/brain-subregion-specific-organoid-protocols.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Related sources

- [A robust protocol for the generation of human midbrain organoids](zagare_2021_a_robust_protocol_for_the.md) - the baseline midbrain differentiation comparator in this collection.
- [Protocol for generating reproducible miniaturized controlled midbrain organoids](chen_2023_protocol_for_generating_reproducible_miniaturized.md) - another protocol that prioritizes midbrain reproducibility before assay layering.
- [CRISPR screens in human neural organoids and assembloids](meng_2025_crispr_screens_in_human_neural.md) - a later-stage neural perturbation workflow that benefits from precise access and delivery logic.

## Open questions

- What organoid maturity window best balances ventricular-zone accessibility with sufficiently mature dopaminergic differentiation?
- How scalable is targeted viral microinjection when experiments move from proof-of-concept to larger perturbation screens?
- How strongly does injection-site choice bias which neural subpopulations become infected over longer follow-up periods?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:31:47+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ -f json,markdown`
- Manifest: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/opendataloader-run.json](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/opendataloader-run.json)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.json](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.json)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.md](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.md)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile1.png](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile1.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile2.png](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile2.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile3.png](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile3.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile4.png](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile4.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile5.png](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile5.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile6.png](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile6.png)
- Output: [raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile7.png](../../raw/derived/opendataloader/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ_images/imageFile7.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
