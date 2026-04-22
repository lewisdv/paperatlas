---
title: Blood–brain-barrier organoids for investigating the permeability of CNS therapeutics
kind: paper
status: ingested
added: 2026-04-21T14:21:48+09:00
raw_source: raw/sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.pdf
article_url: https://doi.org/10.1038/s41596-018-0066-x
published_date: 
organ: blood-brain-barrier
protocol_focus: blood–brain-barrier organoids for investigating the permeability of CNS therapeutics
deep_ingested: 2026-04-22
---

# Blood–brain-barrier organoids for investigating the permeability of CNS therapeutics

## Source

- PDF: [raw/sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.pdf](../../raw/sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.pdf)
- Article: [https://doi.org/10.1038/s41596-018-0066-x](https://doi.org/10.1038/s41596-018-0066-x)
- Status: deep ingested 2026-04-22
- Organ focus: direct-contact multicellular blood-brain-barrier organoids rather than neural parenchymal brain organoids
- Protocol focus: assemble endothelial cells, pericytes, and astrocytes into low-adhesion BBB spheroids, then test compound penetration by confocal microscopy or MALDI mass spectrometry imaging

## Study design

- Starting material: hCMEC/D3 brain endothelial cells, human astrocytes, and human brain pericytes combined under low-adhesion culture conditions
- Protocol stages:
  - prepare 1% agarose-coated low-adhesion wells in a 96-well format so that the three BBB cell types self-assemble rather than attach as a flat monolayer
  - combine endothelial cells, pericytes, and astrocytes and culture the spheroids for about 48 h, yielding BBB organoids in 2-3 days total
  - confirm cell-type marker expression and barrier-like organization before using the organoids for permeability experiments
  - assess fluorescent compound entry by confocal z-stacks and ImageJ-based core-intensity quantification, or assess nonfluorescent small molecules by cryosectioning followed by MALDI MSI
- Key validation: the organoids recapitulate tight-junction and transporter features, allow robust uptake of angiopep-2 and Bip(1), exclude scramble peptide, dextran-rhodamine, and free rhodamine, and distinguish a BBB-penetrant small molecule such as BKM120 from the weakly penetrating dabrafenib
- Distinct protocol emphasis: this is a barrier-screening organoid rather than a developmental brain organoid, and the central move is multicellular direct contact plus assay-ready permeability readout

## Key findings

- Replaces leaky or oversimplified monolayer BBB assays with a direct-contact three-cell spheroid that is still easy to scale and comparatively fast to build.
- Makes permeability testing modular: fluorescent probes and peptides can be read by confocal imaging, whereas unlabeled small molecules can be profiled by MALDI MSI.
- Shows that the platform captures selective transport behavior rather than nonspecific leakiness, which is the whole point of the system.

## Distinctive contribution in this corpus

- One of the clearest non-neural brain-facing assay papers in the collection because the biology is organized around barrier function rather than neuronal differentiation.
- Gives the functional-assay branch a tri-cellular access-control model, not just infection or coculture systems.
- Bridges multicellular assembly and quantitative compound-penetration readouts in a way that fits translational screening much better than most classic brain organoid papers.

## Limitations and caveats

- The system is still a simplified neurovascular unit: it lacks flow, immune traffic, and the wider tissue context of in vivo brain vasculature.
- Agarose quality and well geometry matter; uneven agarose surfaces can deform or prevent proper spheroid formation.
- A positive permeability readout is useful for triage, but it does not resolve the full in vivo pharmacokinetic problem.

## Relevance to corpus

- Strengthens the functional-assay, engineering-imaging, and multicellular-complexity branches at the same time.
- Useful when the question is drug access across a barrier rather than neuronal maturation inside a neural organoid.
- Serves as a barrier-screening comparator to later infection, permeability, and non-destructive imaging papers elsewhere in the corpus.

## Related concepts

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)

## Related sources

- [Controlling the polarity of human gastrointestinal organoids to investigate epithelial biology and infectious diseases](co_2021_controlling_the_polarity_of_human.md) - another access-focused assay paper where geometry and exposure design determine whether the biology is interpretable.
- [Human liver-derived organoids recapitulate Oropouche virus infection and manifestation, enabling antiviral drug discovery](j_2026_human-liver-derived-organoids-recapitulate-oropouche-virus-infection-and-manifestation-ena.md) - an assay comparator where a tissue-specific organoid becomes useful once the right compound-exposure and readout logic are built in.
- [Automated detection and growth tracking of 3D bio-printed organoid clusters using optical coherence tomography with deep convolutional neural networks](d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.md) - a non-destructive readout comparator showing a different route from organoid assembly to screening-ready quantification.

## Open questions

- How well do these BBB spheroids predict transport of larger biologics, nanoparticles, or transporter-sensitive cargo beyond the example compounds shown here?
- Which added feature would improve realism most without destroying throughput: flow, immune cells, or patient-specific endothelial sources?
- When should BBB organoids be preferred over microfluidic BBB-on-chip systems despite the absence of shear stress?
