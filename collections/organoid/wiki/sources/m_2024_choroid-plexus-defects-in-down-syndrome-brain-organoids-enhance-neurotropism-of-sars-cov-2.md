---
title: Choroid plexus defects in Down syndrome brain organoids enhance neurotropism of SARS-CoV-2
kind: paper
status: ingested
added: 2026-04-21T14:26:34+09:00
raw_source: raw/sources/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11152128/
published_date: 2024-06-07
organ: choroid-plexus
protocol_focus: self-organizing cortical organoids with choroid-plexus-like epithelium for Down syndrome and SARS-CoV-2 neurotropism studies
deep_ingested: 2026-04-22
---

# Choroid plexus defects in Down syndrome brain organoids enhance neurotropism of SARS-CoV-2

## Source

- PDF: [raw/sources/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.pdf](../../raw/sources/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11152128/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11152128/)
- Status: deep ingested 2026-04-22
- Organ focus: cortical brain organoids encased in a functional choroid-plexus-like epithelial shell
- Protocol focus: generating self-organizing ChPCOs that combine developmental choroid-plexus morphogenesis with viral neurotropism and drug-response assays

## Study design

- Starting material: human pluripotent stem cells
- Protocol stages:
  - induce human neuroectoderm with dual SMAD inhibition using SB and LDN for 3 days
  - lift the cells into low-attachment spheres in N2 medium plus bFGF, then pattern them with BMP4 and CHIR99021 to bias cortical-hem and choroid-plexus fate
  - use low-dose BMP4 at 2.5 ng/mL rather than stronger doses, and keep Matrigel embedding because non-embedded organoids failed to form the epithelial shell
  - follow early cortical-hem markers by day 14, emergence of thin choroid-plexus-like epithelia between days 21 and 28, and more mature epithelial coverage by days 42 to 56 and beyond
  - infect mature organoids with SARS-CoV-2 and compare DS versus isogenic euploid lines with TMPRSS2 inhibitors, a furin inhibitor, and remdesivir
- Key validation: more than 77% of organoids across lines or clones formed the characteristic TTR-positive epithelial shell, the resulting transcriptomes correlated with adult human lateral-ventricle choroid plexus, and DS organoids showed polarity or ciliogenesis defects together with higher SARS-CoV-2 susceptibility
- Distinct protocol emphasis: the paper uses a partly self-organized cortical-plus-barrier system to show that brain infection phenotypes can be shaped by a specialized epithelial access compartment, not only by neurons

## Key findings

- Shows that a single organoid can jointly support cortical tissue and choroid-plexus-like epithelium, creating a built-in barrier or access layer for infection studies.
- Demonstrates that the DS phenotype is not only neuronal: DS organoids showed altered ciliogenesis, polarity defects, and elevated TMPRSS2 or FURIN expression in the choroid-plexus-like epithelium.
- Links those epithelial differences to virology, with stronger SARS-CoV-2 infection and replication in DS organoids and reduced viral load after TMPRSS2 or furin inhibition.
- Makes the drug-screening logic concrete: avoralstat, camostat, nafamostat, furin inhibition, and remdesivir were all tested within the organoid system, with remdesivir eliminating detectable virus and nafamostat appearing especially potent among TMPRSS2 inhibitors.
- Shows that the model is developmentally informative too, because the same organoids reproduce reduced oligodendrocyte-lineage signatures and other DS-associated cortical abnormalities.

## Distinctive contribution in this corpus

- One of the strongest examples in the collection where developmental patterning and disease-assay layering are inseparable.
- Expands the brain corpus beyond cortex, midbrain, hindbrain, or assembloid logic into a choroid-plexus or cortical-hem axis that matters for barrier biology and viral entry.
- Provides a brain-side analogue to other barrier-access models in the collection by showing that epithelial gatekeeping can drive downstream neural phenotypes.

## Limitations and caveats

- The architecture is more complex and therefore harder to standardize than a simpler cortical-only protocol.
- Infection experiments were performed with a specific viral isolate and specific dosing, so cross-paper potency comparisons should be made cautiously.
- The model still lacks true vasculature and immune-cell circulation, even though it captures epithelial barrier properties better than many neuronal organoid systems.
- DS conclusions are compelling but still depend on a limited number of lines and organoid batches relative to the heterogeneity seen clinically.

## Relevance to corpus

- Strengthens the collection's weak spot around choroid plexus and cortical-hem biology.
- Useful when the key hypothesis depends on how viruses, drugs, or inflammatory signals gain access to neural tissue rather than only on intrinsic neuronal susceptibility.
- Connects developmental patterning, barrier organization, and pharmacologic response inside one protocol rather than scattering them across separate papers.

## Related concepts

- [Brain subregion-specific organoid protocols](../concepts/brain-subregion-specific-organoid-protocols.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)

## Related sources

- [Generation and assembly of human brain region-specific three-dimensional cultures](sloan_2018_generation_and_assembly_of_human.md) - a modular region-specific brain strategy that contrasts with this paper's endogenous cortical-plus-choroid organization.
- [Blood-brain-barrier organoids for investigating the permeability of CNS therapeutics](bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.md) - another neural access-control model, but one built from multicellular BBB assembly rather than choroid-plexus-like self-organization.
- [A robust protocol for the generation of human midbrain organoids](zagare_2021_a_robust_protocol_for_the.md) - a reminder that many subregion protocols optimize neuronal identity without building the epithelial barrier compartment explored here.

## Related entities

- [Blood-brain-barrier (BBB) spheroids](../entities/blood-brain-barrier-bbb-spheroids.md)
- [Single-cell atlas benchmarking](../entities/single-cell-atlas-benchmarking.md)

## Open questions

- Which neural infection questions truly require a choroid-plexus-containing model instead of a simpler cortical organoid?
- How stable are the epithelial polarity and cilia phenotypes across additional DS or euploid genetic backgrounds?
- Can this platform generalize from SARS-CoV-2 to other neurotropic viruses or choroid-plexus-linked developmental disorders without major redesign?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:49:59+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2 -f json,markdown`
- Manifest: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/opendataloader-run.json](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/opendataloader-run.json)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.json](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.json)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.md](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.md)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile1.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile1.png)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile10.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile10.png)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile2.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile2.png)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile3.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile3.png)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile4.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile4.png)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile5.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile5.png)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile6.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile6.png)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile7.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile7.png)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile8.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile8.png)
- Output: [raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile9.png](../../raw/derived/opendataloader/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
