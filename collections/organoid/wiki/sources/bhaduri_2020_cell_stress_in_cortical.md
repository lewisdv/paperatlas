---
title: "Cell stress in cortical organoids impairs molecular subtype specification"
kind: paper
status: ingested
added: 2026-04-09T16:00:00+09:00
raw_source: raw/sources/bhaduri_2020_cell_stress_in_cortical.pdf
article_url: https://www.nature.com/articles/s41586-020-1962-0
published_date: 2020-01-29
organ: brain
protocol_focus: benchmark of cortical organoid fidelity vs. primary fetal cortex
deep_ingested: 2026-04-09
---

# Cell stress in cortical organoids impairs molecular subtype specification

## Source

- PDF: [raw/sources/bhaduri_2020_cell_stress_in_cortical.pdf](../../raw/sources/bhaduri_2020_cell_stress_in_cortical.pdf)
- Article: [Nature](https://www.nature.com/articles/s41586-020-1962-0)
- Lab: Arnold Kriegstein (UCSF)
- Status: deep ingested 2026-04-09

## Study design

- Primary reference data: scRNA-seq of 189,409 cells from 5 cortical samples (GW 6-22) across 7 cortical areas (PFC, motor, parietal, somatosensory, V1, hippocampus, etc.)
- Organoid data: 235,121 cells from 37 organoids generated with 3 different forebrain protocols using 3 iPSC lines + 1 ESC line
- Time course: 3, 5, 8, 10, 15, 24 weeks of differentiation
- Approach: systematic benchmarking of organoid fidelity against primary developing cortex

## Key findings

- Primary cortical development is characterized by progenitor maturation trajectories, diverse cell subtype emergence, and areal specification of newborn neurons.
- **Organoids contain broad cell classes but do not recapitulate distinct cellular subtype identities** or appropriate progenitor maturation.
- Although molecular signatures of cortical areas emerge in organoid neurons, they are **not spatially segregated**.
- **Organoids ectopically activate cellular stress pathways**, which impairs cell-type specification.
- Stress and subtype defects are **alleviated by transplantation into mouse cortex** — suggesting the issue is in vitro microenvironment, not cell-intrinsic.
- Increased directed patterning (more stringent protocols) did NOT consistently yield more endogenous-like subtypes.

## Distinctive contribution in this corpus

- **Critical counterpoint to Velasco 2019**: organoids can be reproducible across themselves but still systematically diverge from primary fetal brain.
- Establishes the "reproducibility ≠ fidelity" distinction that the field needed.
- Demonstrates that transplantation (cf. Kelley 2024) can rescue some fidelity issues.
- Provides the primary cortex scRNA-seq reference dataset that later cross-protocol analyses (He 2024) build on.

## Main claim vs. Velasco 2019

- Velasco: cortical organoids are highly reproducible in cell type composition → good for disease modeling.
- Bhaduri: organoids recapitulate broad classes but fail on fine-grained subtype and areal identity → fidelity caution.
- **These are not contradictory** — they measure different things. Together they frame the "how much precision do you need" question.

## Limitations and caveats

- Only cortical / forebrain organoids analyzed; does not generalize to other brain regions.
- Three protocols compared, not comprehensive.
- Primary GW 6-22 reference may itself have technical batch effects.

## Relevance to brain synchronization query

- Directly addresses the "fidelity" axis missing in Velasco-based reproducibility arguments.
- Quantifies the divergence between organoid and primary cortex at single-cell resolution.
- Provides evidence that "cell synchronization" in organoids may be synchronized to an organoid-specific stress state rather than to native development.

## Related concepts

- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related sources

- [Velasco 2019](velasco_2019_individual_brain_organoids_reproducibly.md) — reproducibility counterpart.
- [Kelley 2024](kelley_2024_host_circuit_engagement_of_human.md) — uses transplantation to address fidelity, consistent with Bhaduri's rescue finding.
- [He 2024](he_2024_an_integrated_transcriptomic_cell_atlas.md) — systematizes cross-protocol vs primary comparison.

## Open questions

- Which specific media components or culture conditions drive the stress signatures?
- Do recent protocols (Fitzgerald 2024 semi-guided, Ullah 2025 single rosette) reduce stress?
- Is the stress response a universal organoid feature or brain-organoid-specific?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-12T12:40:08+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/bhaduri_2020_cell_stress_in_cortical.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical -f json,markdown`
- Manifest: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/opendataloader-run.json](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/opendataloader-run.json)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical.json](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical.json)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical.md](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical.md)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile1.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile1.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile10.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile10.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile100.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile100.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile101.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile101.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile102.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile102.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile103.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile103.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile104.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile104.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile105.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile105.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile106.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile106.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile107.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile107.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile108.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile108.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile109.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile109.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile11.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile11.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile110.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile110.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile111.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile111.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile112.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile112.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile113.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile113.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile114.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile114.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile115.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile115.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile116.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile116.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile117.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile117.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile118.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile118.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile119.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile119.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile12.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile12.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile120.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile120.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile121.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile121.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile122.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile122.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile123.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile123.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile124.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile124.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile125.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile125.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile126.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile126.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile127.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile127.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile128.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile128.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile129.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile129.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile13.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile13.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile130.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile130.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile131.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile131.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile132.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile132.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile133.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile133.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile134.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile134.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile135.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile135.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile136.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile136.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile137.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile137.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile138.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile138.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile139.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile139.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile14.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile14.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile140.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile140.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile141.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile141.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile142.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile142.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile143.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile143.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile144.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile144.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile145.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile145.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile146.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile146.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile147.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile147.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile148.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile148.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile149.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile149.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile15.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile15.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile150.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile150.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile151.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile151.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile152.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile152.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile153.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile153.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile154.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile154.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile155.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile155.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile156.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile156.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile157.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile157.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile158.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile158.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile159.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile159.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile16.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile16.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile160.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile160.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile161.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile161.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile162.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile162.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile163.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile163.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile164.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile164.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile165.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile165.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile166.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile166.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile167.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile167.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile168.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile168.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile169.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile169.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile17.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile17.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile170.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile170.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile171.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile171.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile172.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile172.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile173.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile173.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile174.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile174.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile175.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile175.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile176.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile176.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile177.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile177.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile178.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile178.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile179.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile179.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile18.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile18.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile180.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile180.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile181.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile181.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile182.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile182.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile183.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile183.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile184.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile184.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile185.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile185.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile186.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile186.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile19.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile19.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile2.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile2.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile20.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile20.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile21.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile21.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile22.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile22.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile23.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile23.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile24.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile24.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile25.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile25.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile26.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile26.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile27.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile27.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile28.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile28.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile29.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile29.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile3.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile3.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile30.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile30.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile31.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile31.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile32.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile32.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile33.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile33.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile34.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile34.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile35.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile35.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile36.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile36.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile37.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile37.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile38.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile38.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile39.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile39.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile4.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile4.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile40.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile40.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile41.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile41.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile42.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile42.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile43.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile43.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile44.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile44.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile45.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile45.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile46.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile46.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile47.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile47.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile48.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile48.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile49.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile49.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile5.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile5.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile50.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile50.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile51.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile51.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile52.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile52.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile53.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile53.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile54.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile54.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile55.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile55.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile56.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile56.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile57.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile57.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile58.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile58.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile59.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile59.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile6.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile6.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile60.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile60.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile61.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile61.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile62.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile62.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile63.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile63.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile64.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile64.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile65.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile65.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile66.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile66.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile67.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile67.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile68.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile68.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile69.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile69.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile7.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile7.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile70.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile70.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile71.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile71.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile72.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile72.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile73.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile73.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile74.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile74.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile75.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile75.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile76.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile76.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile77.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile77.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile78.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile78.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile79.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile79.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile8.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile8.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile80.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile80.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile81.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile81.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile82.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile82.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile83.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile83.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile84.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile84.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile85.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile85.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile86.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile86.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile87.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile87.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile88.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile88.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile89.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile89.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile9.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile9.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile90.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile90.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile91.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile91.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile92.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile92.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile93.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile93.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile94.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile94.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile95.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile95.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile96.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile96.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile97.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile97.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile98.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile98.png)
- Output: [raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile99.png](../../raw/derived/opendataloader/bhaduri_2020_cell_stress_in_cortical/bhaduri_2020_cell_stress_in_cortical_images/imageFile99.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
