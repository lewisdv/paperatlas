---
title: From Patient Liver Tissue to Organoids: Establishment of a Translational Platform Using Healthy, Steatotic, and Cirrhotic Tissue Sources
kind: paper
status: ingested
added: 2026-04-21T14:30:05+09:00
raw_source: raw/sources/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12984627/
published_date: 2026-02-28
organ: liver
protocol_focus: from Patient Liver Tissue to Organoids: Establishment of a Translational Platform Using Healthy, Steatotic, and Cirrhotic Tissue Sources
deep_ingested: 2026-04-22
---

# From Patient Liver Tissue to Organoids: Establishment of a Translational Platform Using Healthy, Steatotic, and Cirrhotic Tissue Sources

## Source

- PDF: [raw/sources/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea.pdf](../../raw/sources/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12984627/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12984627/)
- Status: deep ingested 2026-04-22
- Organ focus: patient-derived liver organoids banked from healthy, steatotic, and cirrhotic surgical tissue
- Protocol focus: adapt adult liver organoid derivation to real surgical specimens, then characterize growth, lineage state, and disease-context retention across a hospital-scale biobank

## Study design

- Starting material: tumor-free surgical liver tissue from 207 resections and transplants, yielding 55 derivation attempts and 45 established organoid lines
- Protocol stages:
  - adapt the Broutier adult liver workflow to hospital specimens by mincing tissue, washing away fat and blood, digesting with collagenase D plus DNase I, filtering through 70 um mesh, and embedding the resulting pellet in 50 uL Geltrex domes
  - initiate cultures in HepatiCult initiation medium plus ROCK inhibitor, change medium every 3 days, and switch to HepatiCult growth medium on day 7
  - passage cultures at roughly 1:1 when domes become dense or individual organoids exceed about 1 mm, fragmenting them with a 22-gauge cannula rather than full single-cell dissociation
  - profile established lines with multiplex immunofluorescence, qPCR, and time-lapse growth modeling across healthy, steatotic, and cirrhotic donor groups
- Key validation: the workflow achieved an 82% initiation success rate, maintained cultures for at least 6 passages, showed about 40% Ki-67-positive proliferative cells with Albumin or HNF4a plus CK19 co-expression, detected intermittent LGR5 positivity, and revealed biphasic growth with linear expansion in the first 15 hours followed by exponential growth between 30 and 72 hours
- Distinct protocol emphasis: this is an organoid-bank construction paper as much as a derivation paper, with explicit attention to disease-stratified donor capture, assay-ready characterization, and quantitative growth behavior

## Key findings

- Shows that routine surgical material from healthy, steatotic, and cirrhotic livers can seed a reasonably efficient adult liver organoid bank without requiring unusually clean specimens or highly selective pre-sorting.
- Preserves clinically meaningful heterogeneity rather than collapsing every line into a uniform endpoint, as seen in variable HNF4a expression, partial Albumin loss at the transcript level, mixed Albumin or HNF4a plus CK19 staining, and disease-linked collagen I or alpha-SMA signals.
- Treats time-lapse growth modeling as part of the platform definition, making growth kinetics and donor-to-donor variability explicit instead of leaving expansion behavior as an undocumented background variable.

## Distinctive contribution in this corpus

- One of the clearest adult liver biobank papers in the collection for stratifying donors across healthy, steatotic, and cirrhotic states within the same workflow.
- Gives the adult-platform branch a disease-context-preserving liver comparator that sits between generic adult liver expansion and downstream infection or drug-response assays.
- Makes the translational infrastructure visible: collection logistics, initiation efficiency, characterization panels, and growth modeling are all part of the platform, not just supporting detail.

## Limitations and caveats

- The organoids remain heterogeneous and somewhat mixed in identity, with strong CK19 expression, variable HNF4a, and low or undetectable ALB transcripts in some lines, so this is not a clean mature-hepatocyte endpoint.
- The characterization still leaves important compartments unresolved, especially stellate, endothelial, Kupffer, and broader stromal composition.
- Because the paper centers on derivation and bank setup, it establishes assay readiness more than it demonstrates a mature downstream disease-modeling benchmark across the entire panel.

## Relevance to corpus

- Strengthens the adult-platform and gastrointestinal-endoderm branches with a liver paper centered on clinical stratification rather than on pluripotent differentiation or viral challenge.
- Useful when the question is how to capture donor liver state in a scalable adult organoid bank before layering on perturbation, infection, or drug testing.
- Pairs naturally with adult liver baseline papers and liver-assay papers elsewhere in the corpus.

## Related concepts

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Gastrointestinal and endodermal organoid systems](../concepts/gastrointestinal-and-endodermal-organoid-systems.md)

## Related sources

- [Culture and establishment of self-renewing human and mouse adult liver and pancreas 3D organoids and their genetic manipulation](broutier_2016_culture_and_establishment_of_self-renewing.md) - the adult liver baseline this paper adapts for real-world surgical biobanking.
- [Isolation and propagation of primary human cholangiocyte organoids for the generation of bioengineered biliary tissue](tysoe_2019_isolation_and_propagation_of_primary.md) - another adult endoderm platform, but one optimized for mature cholangiocyte identity and scaffold engineering.
- [Human liver-derived organoids recapitulate Oropouche virus infection and manifestation, enabling antiviral drug discovery](j_2026_human-liver-derived-organoids-recapitulate-oropouche-virus-infection-and-manifestation-ena.md) - a downstream liver assay comparator that starts from an established adult organoid platform rather than from a bank-building workflow.

## Open questions

- Which sample-handling variables during surgery-to-culture transfer matter most for the jump from failed initiation to stable line establishment?
- How long do healthy, steatotic, and cirrhotic signatures remain separable across later passages and drug-perturbation experiments?
- When should this mixed hepatocyte-cholangiocyte platform be preferred over more explicitly multicellular liver organoids?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:50:26+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea -f json,markdown`
- Manifest: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/opendataloader-run.json](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/opendataloader-run.json)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea.json](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea.json)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea.md](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea.md)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile1.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile1.png)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile10.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile10.png)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile2.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile2.png)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile3.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile3.png)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile4.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile4.png)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile5.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile5.png)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile6.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile6.png)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile7.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile7.png)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile8.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile8.png)
- Output: [raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile9.png](../../raw/derived/opendataloader/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea/r_2026_from-patient-liver-tissue-to-organoids-establishment-of-a-translational-platform-using-hea_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
