---
title: Protocol for generating human vascular organoids via orthogonal activation of ETV2 and NKX3.1.
kind: paper
status: ingested
added: 2026-04-21T20:30:40+09:00
raw_source: raw/sources/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12800413/
published_date: 2025-12-24
organ: vascular
protocol_focus: generating human vascular organoids via orthogonal activation of ETV2 and NKX3.1
deep_ingested: 2026-04-22
---

# Protocol for generating human vascular organoids via orthogonal activation of ETV2 and NKX3.1.

## Source

- PDF: [raw/sources/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.pdf](../../raw/sources/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12800413/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12800413/)
- Status: deep ingested 2026-04-22
- Organ focus: human iPSC-derived vascular organoids with endothelial and mural compartments
- Protocol focus: rapid vascular organoid generation through orthogonal transcription-factor programming

## Study design

- Starting material: human iPSCs engineered with doxycycline-inducible PiggyBac ETV2 and NKX3.1 transgenes
- Protocol stages:
  - maintain engineered hiPSC lines on Matrigel and establish the dual-programmable lines needed for endothelial and mural induction
  - electroporate hiPSCs with the PiggyBac system using Neon settings of 1150 V, 30 ms, and 2 pulses
  - run a mesoderm-induction stage to produce inducible progenitors
  - aggregate cells under orbital shaking with doxycycline so endothelial and mural programs emerge in parallel
  - embed organoids in a collagen I-Matrigel matrix and culture with VEGF-A and FGF2 to drive vascular sprouting and network maturation
- Total duration: the paper positions the core organoid-formation phase as a five-day workflow after engineered lines are established
- Key validation: qPCR confirms transgene induction, flow cytometry identifies VE-Cadherin-positive endothelial and PDGFRB-positive mural populations, and whole-mount imaging shows CD31-positive vascular tubes with MYH11-positive mural coverage
- Distinct protocol emphasis: lineage specification is decoupled from slower spontaneous differentiation by forcing endothelial and mural fates independently and then allowing them to self-organize in 3D

## Key findings

- Simultaneous activation of ETV2 and NKX3.1 is sufficient to produce vascular organoids with both endothelial and mural compartments on a much shorter timescale than classic morphogen-led protocols.
- The combined two-factor condition matters mechanistically: single-factor conditions do not generate organized vascular networks.
- Collagen-Matrigel embedding is not just a support step; it is where radial sprouting and visible vascular complexity emerge.
- The workflow is explicitly built for reproducibility and scale, with suspension culture and orbital shaking treated as core parts of the system rather than optional optimization.

## Distinctive contribution in this corpus

- The fastest and most transcription-factor-programmed vascular paper in the collection, making it a strong counterpoint to slower self-organization-first vascular protocols.
- Sharpens the vascularization concept layer by showing a "program the lineages first, then assemble" strategy rather than relying on endogenous timing cues alone.
- Gives the refill cohort a modern vascular baseline that is easier to compare against brain- and kidney-vascularization papers built around ETV2 or perfusion logic.

## Limitations and caveats

- The protocol depends on pre-engineered doxycycline-inducible hiPSC lines, so it is less plug-and-play than morphogen-only vascular workflows.
- Differentiation efficiency is sensitive to seeding density, aggregate handling, and constant 100 rpm suspension culture.
- Medium changes and matrix handling are operationally fragile because free-floating organoids are easy to aspirate or mechanically disturb.
- The system yields vascular organoids, not organ-specific vasculature, so tissue-context fidelity still has to be added elsewhere.

## Relevance to corpus

- Strengthens the vascularization cluster with a route that prioritizes speed and reproducibility over developmental naturalism.
- Useful as a comparator to older vascular organoid work when the practical question is whether to trust directed lineage programming or longer morphogen-guided differentiation.
- Helps connect pure vascular organoids to broader organoid-engineering questions about how much tissue complexity can be forced rather than allowed to emerge.

## Related concepts

- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)

## Related sources

- [Generation of blood vessel organoids from human pluripotent stem cells](wimmer_2019_generation_of_blood_vessel_organoids.md) - the main self-organization-first vascular baseline in this corpus.
- [Engineering of human brain organoids with a functional vascular-like system](cakir_2019_engineering_of_human_brain.md) - uses ETV2-driven vascular logic inside a neural-organoid context.
- [Flow-enhanced vascularization and maturation of kidney organoids in vitro](homan_2019_flow-enhanced_vascularization_and_maturation.md) - a complementary strategy where perfusion and flow, not transcription-factor programming, drive vascular maturation.

## Open questions

- How far do these rapidly programmed vascular organoids mature over long culture or after transplantation?
- Can the same orthogonal transcription-factor logic vascularize other organoid systems without destabilizing their host tissue identity?
- What is the practical tradeoff between this protocol's speed and the developmental fidelity offered by slower spontaneous vascular differentiation routes?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T20:31:41+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx -f json,markdown`
- Manifest: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/opendataloader-run.json](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/opendataloader-run.json)
- Output: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.json](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.json)
- Output: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.md](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.md)
- Output: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile1.png](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile1.png)
- Output: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile2.png](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile2.png)
- Output: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile3.png](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile3.png)
- Output: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile4.png](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile4.png)
- Output: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile5.png](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile5.png)
- Output: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile6.png](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile6.png)
- Output: [raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile7.png](../../raw/derived/opendataloader/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx_images/imageFile7.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
