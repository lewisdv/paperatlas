---
title: Human brain organoids record the passage of time over multiple years
kind: paper
status: ingested
added: 2026-08-21
deep_ingested: 2026-08-21
doi: 10.1038/s41586-026-10877-x
authors: Faravelli I, Antón-Bolaños N, Wei A, et al.; Arlotta P
journal: Nature (2026)
organ: brain
protocol_focus: five-year cortical-organoid maturation, activity-permissive culture, and temporal-memory testing
raw_source: raw/sources/faravelli_2026_human_brain_organoids_record_time_years.pdf
---

# Human brain organoids record the passage of time over multiple years

## Source

- Authors: Irene Faravelli, Noelia Antón-Bolaños, Anqi Wei, Tyler Faits, Abhishek Sampath Kumar, Sophia Andreadis, Rahel Kastli, Marta Montero Crespo, Mara Steiger, Daniel Leible, Elizabeth Zhang, Bobae An, Yaron Meirovitch, Sayara Silwal, Sung Min Yang, Alexander Kovacsovics, Xian Adiconis, Helene Kretzmer, Joshua Z. Levin, Edward S. Boyden, Jeff Lichtman, Aviv Regev, Alexander Meissner, and Paola Arlotta.
- Journal: *Nature* (2026). The supplied PDF states acceptance on 1 July 2026; its online-publication field is still shown as `xx xx xxxx`.
- DOI: [10.1038/s41586-026-10877-x](https://doi.org/10.1038/s41586-026-10877-x)
- Raw PDF: [faravelli_2026_human_brain_organoids_record_time_years.pdf](../../raw/sources/faravelli_2026_human_brain_organoids_record_time_years.pdf)
- Deep-ingest helpers: [text extraction](../../raw/derived/pdftext/Faravelli_2026_Brain_Organoid_Time/Faravelli_2026_Brain_Organoid_Time.txt) and [ingest manifest](../../raw/derived/pdftext/Faravelli_2026_Brain_Organoid_Time/ingest-manifest.md). These are navigation aids; the raw PDF is the source of truth.

## Study design

- Cortical organoids were profiled from 15 days to 5 years in culture. The integrated single-cell dataset contains 110 organoids and 424,720 cells: 34 newly profiled organoids from 6 months to 5 years plus 76 previously generated organoids from 15 days to 6 months.
- Time in vitro was compared with endogenous human cortical development through single-cell label transfer and DIALOGUE-derived, age-associated multicellular programs. Whole-genome bisulfite sequencing covered nine time points from 3 months to 5 years, and three DNA-methylation clocks were applied.
- To retain active excitatory neurons, organoids were switched at day in vitro 70 to activity-permissive medium (APM: BrainPhys plus GlutaMax) or retained in conventional CDM4. Readouts include scRNA-seq, methylome profiling, electron microscopy, expansion-microscopy tracing, and 3D multi-electrode-array recordings.
- Temporal-memory experiments reaggregated cells from 9–12-month organoids alone or with DIV15 progenitors, then assayed fate output by single-cell RNA-seq and immunostaining.

## Main findings

- **Long-term cortical organoids align progressively with endogenous developmental time.** Early cultures map to first-trimester reference tissue, 3–6-month cultures predominantly to the second trimester, and 9-month-to-5-year cultures progressively to late-prenatal and postnatal reference ages. Postnatal-like signatures emerge after roughly 12 months.
- **Epigenomic age tracks time in vitro.** Age-associated methylation dynamics, including CpG and non-CpG changes, follow patterns the authors compare with developing cortex. Horvath and cortex-specific clock estimates correlate with culture time at `r = 0.88–0.90`; these are evidence of model-aligned temporal progression, not a claim that an organoid has an unrestricted universal chronological age.
- **APM improves long-term excitatory-neuron maintenance and maturation.** Relative to CDM4, APM increases callosal projection neurons and active SATB2-positive neurons at 9 months, synapse density and spine-associated synapses at 1 year, and neuronal arbor complexity at 7 months. Its excitatory-neuron populations show no increasing apoptosis, hypoxia, or glycolysis signatures across the tested 4-month-to-1.5-year interval.
- **Functional network activity persists for at least two years under APM.** APM organoids have higher spike and burst metrics than CDM4 across 6–12 months; all nine one-year APM organoids showed robust network bursts whereas no one-year CDM4 organoid did. Two-year APM organoids retained bursting activity and NeuN-positive neurons.
- **Old progenitors retain a developmentally ordered memory.** In heterochronic chimeroids, progenitors from 9–12-month organoids respond to young-cell signals by restarting excitatory neurogenesis, but preferentially generate late progeny rather than repeating early fates. Old-cell derivatives included 49.0% callosal projection neurons after reaggregation, versus 0.02–0.55% in the old monochronic controls; the authors interpret this as temporal memory with retained plasticity.

## Interpretation for this corpus

- This extends [Gordon 2021](gordon_2021_longterm_maturation_human_cortical_organoids_postnatal_transitions.md) from a 250–300-day fetal-to-postnatal transition to a cell-type-resolved, multimodal 5-year series. The two studies support long-horizon maturation as a measurable branch of brain-organoid validation, but use different protocols, reference mappings, and temporal windows.
- The strongest addition is not merely a longer culture duration: it joins molecular temporal alignment, structural and electrophysiological neuronal readouts, and an intervention-like test of progenitor temporal state in one design.
- For protocol selection, the paper separates three questions that should not be collapsed: whether the composition remains reproducible, whether a cell type retains functional activity, and whether its developmental timing corresponds to an endogenous reference.

## Limitations and caveats

- The time alignment depends on selected human reference datasets and clock models. It supports similarity to specific endogenous temporal programs, not complete equivalence to an intact postnatal or adult human brain.
- Five-year molecular profiling and two-year functional network measurements are not the same endpoint; durable molecular temporal signatures do not by themselves establish five-year circuit function for every neuronal population.
- APM changes neuronal survival, composition, activity, and some locus-specific methylation. Improvements under this medium therefore cannot be treated as a culture-condition-independent maturation clock.
- The temporal-memory interpretation rests on reaggregation/heterochronic-chimeroid assays. It shows preserved developmental ordering under those conditions, not a fully identified molecular mechanism for the memory.

## Related

- Concept: [Long-horizon brain-organoid maturation and temporal memory](../concepts/long-horizon-brain-organoid-maturation-and-temporal-memory.md)
- Concept: [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- [Gordon 2021 — long-term maturation and early postnatal transitions](gordon_2021_longterm_maturation_human_cortical_organoids_postnatal_transitions.md)
- [Velasco 2019 — reproducible cell diversity in brain organoids](velasco_2019_individual_brain_organoids_reproducibly.md)
- [He 2024 — integrated transcriptomic atlas of human neural organoids](he_2024_an_integrated_transcriptomic_cell_atlas.md)
