---
title: Patient-derived and mouse endo-ectocervical organoid generation, genetic manipulation and applications to model infection
kind: paper
status: ingested
added: 2026-04-21T14:21:48+09:00
raw_source: raw/sources/gurumurthy_2022_patient-derived_and_mouse_endo-ectocervical_organoid.pdf
article_url: https://doi.org/10.1038/s41596-022-00695-6
published_date: 
organ: cervix
protocol_focus: patient-derived and mouse endo-ectocervical organoid generation, genetic manipulation and applications to model infection
deep_ingested: 2026-04-22
---

# Patient-derived and mouse endo-ectocervical organoid generation, genetic manipulation and applications to model infection

## Source

- PDF: [raw/sources/gurumurthy_2022_patient-derived_and_mouse_endo-ectocervical_organoid.pdf](../../raw/sources/gurumurthy_2022_patient-derived_and_mouse_endo-ectocervical_organoid.pdf)
- Article: [https://doi.org/10.1038/s41596-022-00695-6](https://doi.org/10.1038/s41596-022-00695-6)
- Status: deep ingested 2026-04-22
- Organ focus: adult human and mouse endocervical plus ectocervical epithelial organoids with explicit lineage separation
- Protocol focus: derive niche-specific cervical organoids, optionally expand ectocervical stem cells in feeder culture, then apply HPV engineering and Chlamydia infection workflows

## Study design

- Starting material: human endocervical and ectocervical biopsies plus mouse cervical tissue, with epithelial cells isolated from dissected lineage-specific regions
- Protocol stages:
  - dissect endocervix, ectocervix, and transition-zone-adjacent tissue carefully, digest the tissue, and embed cells in Matrigel for lineage-specific organoid derivation
  - apply different niche logic to each epithelial branch: endocervical cultures rely on WNT3A and R-spondin support, whereas ectocervical expansion depends on EGF, FGF10, A83-01, active BMP signaling, and is actually impaired by WNT3A or R-spondin
  - optionally expand human ectocervical stem cells in 2D on collagen-coated plates with irradiated 3T3-J2 feeders for about 2-3 weeks before moving back into 3D organoid culture
  - validate lineage identity with morphology and KRT8 versus KRT5 staining, then use established lines for lentiviral HPV16 E6E7 introduction or Chlamydia trachomatis infection assays
- Key validation: endocervical organoids are relatively hollow and single-layered, ectocervical organoids are denser and stratified, 14-day lines stain for KRT8 or KRT5 as expected, and Chlamydia infection experiments are run on 5-6 day organoids at around MOI 10
- Distinct protocol emphasis: this is a niche-dissection paper as much as an infection paper, because adjacent cervical epithelia require opposite WNT logic and different expansion strategies

## Key findings

- Demonstrates that the cervix cannot be treated as one generic epithelial organoid system, because endocervical and ectocervical compartments follow different signaling rules and failure modes.
- Makes feeder-based 2D ectocervical stem-cell expansion part of the platform, which is especially valuable for later genetic manipulation.
- Integrates derivation, lineage validation, HPV engineering, and bacterial infection into one workflow rather than scattering them across unrelated systems.

## Distinctive contribution in this corpus

- The clearest adult cervix platform paper in the collection and one of the best reproductive-tract niche-comparison protocols overall.
- Gives the adult-platform branch an example where opposite WNT requirements emerge across two adjacent epithelia from the same organ.
- Bridges organoid derivation and host-pathogen modeling without abandoning tissue-specific epithelial identity.

## Limitations and caveats

- Dissection precision and medium choice are major failure points, because cross-contamination between endocervical and ectocervical tissue or wrong WNT conditions can flip the observed phenotype.
- The system remains highly epithelial even when used for infection studies, so immune and stromal interpretation is limited.
- Chlamydia experiments are technically fragile: incomplete Matrigel removal or excessive MOI can rapidly damage organoids and confound the biology.

## Relevance to corpus

- Strengthens both the adult-platform and functional-assay branches with a reproductive-tract system that is lineage aware from the beginning.
- Useful when the project needs niche-specific adult epithelial organoids for infection, oncogene introduction, or cervical lineage comparison.
- Complements endometrial and vaginal assay systems by providing the baseline epithelial platform those later coculture questions often depend on.

## Related concepts

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related entities

- [Reproductive mucosal epithelial organoids](../entities/reproductive-mucosal-epithelial-organoids.md)
- [Adult tissue-derived epithelial organoids](../entities/adult-tissue-derived-epithelial-organoids.md)

## Related sources

- [Protocol for the establishment and characterization of an endometrial-derived epithelial organoid and stromal cell co-culture system](ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.md) - a reproductive-tract comparator that adds stromal support rather than focusing on epithelial niche divergence.
- [Protocol for the coculture of murine vaginal epithelial organoids and T cells to induce resident memory CD8 T cell differentiation](jc_2025_protocol-for-the-coculture-of-murine-vaginal-epithelial-organoids-and-t-cells-to-induce-re.md) - a nearby mucosal assay system that layers immune education onto an epithelial organoid baseline.
- [Protocol for transducing human primary epithelial prostate cells and patient-derived organoids with high efficiency](c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.md) - an adult-organoid engineering comparator for the genetic manipulation branch of the workflow.

## Open questions

- Can stable transition-zone-specific organoid states be isolated and maintained without collapsing into one neighboring lineage?
- What is the best first added compartment for cervical infection studies: immune cells, fibroblasts, or hormone-cycling context?
- How faithfully do donor-specific infection or HPV-response phenotypes persist over long-term expansion?
