---
title: Human neuromodulatory assembloids to study serotonin signaling and disease
kind: paper
status: ingested
added: 2026-04-21T14:26:20+09:00
raw_source: raw/sources/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13060871/
published_date: 2026-03-10
organ: brain assembloid
protocol_focus: human neuromodulatory assembloids to study serotonin signaling and disease
deep_ingested: 2026-04-22
---

# Human neuromodulatory assembloids to study serotonin signaling and disease

## Source

- PDF: [raw/sources/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease.pdf](../../raw/sources/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC13060871/](https://pmc.ncbi.nlm.nih.gov/articles/PMC13060871/)
- Status: deep ingested 2026-04-22
- Organ focus: fused human cortical and midbrain-hindbrain organoids built to model serotonergic neuromodulation and disease
- Protocol focus: pattern serotonergic hMHO organoids, fuse them with cortical organoids, and assay 5-HT signaling with multimodal functional readouts

## Study design

- Starting material: human iPSC-derived cortical organoids and separately patterned human midbrain-hindbrain organoids across multiple donor lines
- Protocol stages:
  - pattern the midbrain-hindbrain organoid branch with SAG, CHIR, and FGF4 to generate a serotonergic hindbrain or midbrain-hindbrain identity
  - verify early regional specification around days 19 to 22 using hindbrain-associated markers such as GATA2 and GATA3
  - continue maturation into the day-50 to day-60 range and confirm serotonergic identity with TPH2, FEV, and SLC6A4 while showing absence of FOXG1 from the hMHO branch
  - fuse the serotonergic hMHO compartment with human cortical organoids to create human neuromodulatory assembloids
  - validate the resulting system with scRNA-seq, HPLC, serotonin-sensor imaging, and network-level functional assays, then apply it to 22q11.2 deletion syndrome modeling
- Key validation: the paper profiles 54,117 cells across four hiPSC lines, maps more than 75% of hMHO cells to midbrain or hindbrain identities, detects serotonin biochemically, and shows serotonergic projections altering cortical activity after fusion
- Distinct protocol emphasis: the central innovation is not just fusion itself but building an assembloid where neuromodulatory transmitter dynamics become a measurable experimental variable

## Key findings

- Pushes the assembloid concept from structural connectivity into neurotransmitter-specific modulation, with serotonin release and cortical-response coupling as the central readout.
- Couples strong cell-identity validation to functional measurements, which helps the protocol avoid being only a visually appealing fusion system.
- Extends the platform into disease modeling by showing altered serotonergic dynamics in 22q11.2 deletion syndrome and pharmacologic rescue with an SSRI.
- Demonstrates that serotonergic neurons can be generated in one compartment and then allowed to modulate another tissue in a way that simpler single-organoid models cannot capture.

## Distinctive contribution in this corpus

- One of the strongest neuromodulation-focused organoid papers in the collection and likely the clearest serotonin-specific assembloid protocol currently represented.
- Expands the brain-assembloid branch beyond wiring questions into transmitter dynamics, pharmacologic response, and psychiatric or neurodevelopmental disease modeling.
- Gives the corpus a concrete example of when a modular brain fusion is justified because the phenotype is fundamentally cross-compartmental.

## Limitations and caveats

- The workflow combines long differentiation, fusion, single-cell validation, and advanced functional assays, so it is not a simple entry-level protocol.
- Accurate interpretation depends on both strong serotonergic patterning in the hMHO branch and successful projection into the cortical partner.
- Disease conclusions may not generalize beyond the specific 22q11.2 context without additional comparator lines and perturbations.
- This is a powerful but lower-throughput platform relative to simpler serotonin-neuron or cortical-only models.

## Relevance to corpus

- Strengthens the collection at the intersection of brain assembloids, subregion patterning, and functional disease modeling.
- Useful when the scientific question is not just whether a serotonergic lineage exists, but whether it can modulate cortical physiology in a disease-relevant way.
- Helps position neuromodulatory assembloids as a next-step option after simpler single-region organoids stop being sufficient.

## Related concepts

- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)

## Related entities

- [Assembloids and regional fusion](../entities/assembloids-and-regional-fusion.md)
- [Calcium imaging readouts](../entities/calcium-imaging-readouts.md)

## Related sources

- [Engineering brain assembloids to interrogate human neural circuits](miura_2022_engineering_brain_assembloids_to_interrogate.md) - the clearest circuit-assembly comparator, with this paper adding transmitter-specific neuromodulation and disease use cases.
- [Generation of caudal-type serotonin neurons from human pluripotent stem cells for in vivo and in vitro studies](valiulahi_2021_generation_of_caudal-type_serotonin_neurons.md) - a serotonergic-lineage comparator that lacks the cross-compartment cortical target layer.
- [Protocol for differentiating human pluripotent stem cells into midbrain organoids for targeted microinjection of viruses](m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.md) - a more focused subregion-plus-perturbation protocol that helps clarify when fusion is unnecessary.

## Open questions

- How reproducibly do serotonergic projections and 5-HT signaling emerge across lines, batches, and different cortical target preparations?
- When is a neuromodulatory assembloid necessary, and when would a simpler serotonergic organoid or 2D co-culture be sufficient?
- Which disease classes beyond 22q11.2 most clearly benefit from a cross-compartment serotonin-signaling platform?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:49:18+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease -f json,markdown`
- Manifest: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/opendataloader-run.json](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/opendataloader-run.json)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease.json](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease.json)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease.md](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease.md)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile1.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile1.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile10.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile10.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile11.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile11.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile2.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile2.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile3.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile3.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile4.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile4.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile5.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile5.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile6.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile6.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile7.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile7.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile8.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile8.png)
- Output: [raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile9.png](../../raw/derived/opendataloader/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease/human_2026_human-neuromodulatory-assembloids-to-study-serotonin-signaling-and-disease_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
