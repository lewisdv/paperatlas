---
title: "Generation of inner ear organoids containing functional hair cells from human pluripotent stem cells"
kind: paper
status: ingested
added: 2026-04-09T15:30:00+09:00
raw_source: raw/sources/koehler_2017_generation_of_inner_ear_organoids.pdf
article_url: https://www.nature.com/articles/nbt.3840
published_date: 2017-05-01
organ: inner ear
protocol_focus: 3D inner ear organoid with functional vestibular-like hair cells from hPSCs
deep_ingested: 2026-04-09
---

# Generation of inner ear organoids containing functional hair cells from human pluripotent stem cells

## Source

- PDF: [raw/sources/koehler_2017_generation_of_inner_ear_organoids.pdf](../../raw/sources/koehler_2017_generation_of_inner_ear_organoids.pdf)
- Article: [Nature Biotechnology](https://www.nature.com/articles/nbt.3840)
- Labs: Karl Koehler + Eri Hashino (Indiana University / Harvard)
- Status: deep ingested 2026-04-09

## Study design

- Starting material: WA25 hESCs + mND2-0 hiPSCs in E8 medium + Y-27632
- Protocol duration: ~60+ days
- Key signaling modulations over time:
  - **SB431542 alone (SB)**: induces non-neural ectoderm epithelium (TFAP2A+/ECAD+) at day 4-6
  - Adding **low BMP4 (2.5 ng/mL, SBB)** for cell lines with low endogenous BMP
  - **FGF-2 + LDN-193189 (SBFL)** at day 4: pre-placodal epithelium (PAX8+/SOX2+/TFAP2A+/ECAD+/NCAD+)
  - **CHIR99021 (WNT activation)** starting day 12 in Matrigel droplets: generates PAX2+PAX8+SOX2+SOX10+JAG1+ otic pits in 91% of aggregates
- Transfer to orbital shaker/spinner flask day 18 for self-organized maturation
- Reporter line: ATOH1-2A-eGFP CRISPR knock-in for hair cell identification

## Key findings

- **91% of aggregates form otic pits** with appropriate markers.
- Over 2 months, otic vesicles develop into inner ear organoids with **sensory epithelia that are innervated by sensory neurons**.
- Derived hair cells express multiple hair cell markers (MYO7A, PCP4, ANXA4, SOX2, CALB2) and have F-actin-rich stereocilia bundles with kinocilia.
- **Hair cells exhibit electrophysiological properties similar to native vestibular hair cells** — confirms functional, not just morphological, identity.
- Organoids also contain cranial neural crest-derived mesenchyme and chondrocyte masses, recapitulating peri-otic development.
- Developmentally faithful: follows the same signaling pathway sequence as in vivo otic development (BMP activation + TGFβ inhibition → pre-otic fate).

## Distinctive contribution in this corpus

- **Foundational inner ear organoid protocol from Koehler lab** — the reference point for the entire inner ear organoid field.
- First hPSC-derived inner ear tissue with functional hair cells.
- Framework translated from mouse work (Koehler & Hashino earlier work).

## Limitations and caveats

- Produces vestibular-like (not cochlear) hair cells.
- Cell-line-dependent: some lines need SB alone, others need SBB with added BMP4.
- Long differentiation (2 months) with multi-step signaling modulation.
- Orientation and laminar organization are heterogeneous.

## Relevance to corpus

- Must be read with van der Valk 2025 which extends this work with an updated vestibular protocol.
- Only functional sensory organoid (vs. Lee 2022 skin with hair follicles, Dardano 2025 heart+blood).

## Related concepts

- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)

## Related entities

- [Sensory ectoderm and appendage organoids](../entities/sensory-ectoderm-and-appendage-organoids.md)

## Related sources

- [van der Valk 2025](vandervalk_2025_generation_and_characterization_of_vestibular.md) — Nature Protocols extension with detailed step-by-step method from the same lab.
- [Lee 2022](lee_2022_generation_and_characterization_of_hair-bearing.md) — parallel skin+appendage organoid from similar ectodermal logic.

## Open questions

- Can cochlear (not just vestibular) hair cells be generated from this approach?
- How do the electrophysiological properties compare to native human (not mouse) hair cells?
- What is the maximum useful in vitro lifespan?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-12T12:43:08+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/koehler_2017_generation_of_inner_ear_organoids.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids -f json,markdown`
- Manifest: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/opendataloader-run.json](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/opendataloader-run.json)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids.json](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids.json)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids.md](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids.md)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile1.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile1.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile10.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile10.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile11.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile11.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile12.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile12.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile13.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile13.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile14.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile14.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile15.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile15.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile16.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile16.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile2.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile2.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile3.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile3.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile4.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile4.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile5.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile5.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile6.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile6.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile7.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile7.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile8.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile8.png)
- Output: [raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile9.png](../../raw/derived/opendataloader/koehler_2017_generation_of_inner_ear_organoids/koehler_2017_generation_of_inner_ear_organoids_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
