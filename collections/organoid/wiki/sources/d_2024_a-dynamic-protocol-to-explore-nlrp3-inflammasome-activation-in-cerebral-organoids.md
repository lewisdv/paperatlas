---
title: A Dynamic Protocol to Explore NLRP3 Inflammasome Activation in Cerebral Organoids
kind: paper
status: ingested
added: 2026-04-21T14:25:43+09:00
raw_source: raw/sources/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11204242/
published_date: 2024-06-01
organ: brain
protocol_focus: long-term cerebral organoid slicing and two-step NLRP3 inflammasome activation in 3D neural tissue
deep_ingested: 2026-04-22
---

# A Dynamic Protocol to Explore NLRP3 Inflammasome Activation in Cerebral Organoids

## Source

- PDF: [raw/sources/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.pdf](../../raw/sources/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11204242/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11204242/)
- Status: deep ingested 2026-04-22
- Organ focus: six-month cerebral organoids converted into slice-based neuroinflammation tissue assays
- Protocol focus: adapting the classic LPS plus nigericin two-step NLRP3 activation workflow to thick 3D cerebral organoid tissue while preserving architecture

## Study design

- Starting material: H9 ESC-derived long-term cerebral organoids
- Protocol stages:
  - generate cerebral organoids on an orbital shaker until 24 weeks, when astrocytes are mature enough to support inflammasome readouts
  - once organoids exceed 2 mm, keep no more than four per well, embed each in 4% low-melting agarose, and slice them on a vibratome into 400 um sections
  - recover slices in maturation medium with penicillin-streptomycin, then prime them with 100 ng/mL LPS for 3 h
  - use 100 nM MCC950 for 2 h as an inhibition control before exposing slices to 10 uM nigericin for 1, 4, or 16 h
  - fix slices for GFAP, MAP2, SOX2, and ASC imaging, and collect supernatant for ccf-mtDNA, IL-1beta, caspase-1, NO, ROS, and dsDNA assays
- Key validation: the 4 h nigericin condition produced the clearest ASC speck signal in GFAP-positive astrocytes, while MCC950 suppressed both imaging and supernatant inflammatory readouts
- Distinct protocol emphasis: the paper is not about inventing a new cerebral organoid lineage but about turning mature cerebral organoids into a tractable assay for astrocyte-dominant inflammasome biology

## Key findings

- Establishes that 3D cerebral organoid tissue requires a different timing regime from older 2D immune-cell protocols: 4 h of nigericin gave strong ASC speck formation, whereas 1 h and 16 h were both weaker.
- Shows that the signal localizes mainly to GFAP-positive astrocytes rather than MAP2-positive neurons, which matters for interpreting what this assay is actually measuring.
- Uses 400 um vibratome slices as a practical compromise between tissue integrity and reagent penetration.
- Builds a multi-readout assay stack rather than relying on one marker, combining ASC speck imaging with ccf-mtDNA, IL-1beta, caspase-1, NO, ROS, and dsDNA release.
- Adds a semi-automated FIJI workflow for ASC speck detection because standard whole-cell counting was not enough for such small puncta.

## Distinctive contribution in this corpus

- One of the clearest examples in the collection where a mature brain organoid is used as assay substrate rather than as an endpoint differentiation product.
- Complements transplantation and infection papers by covering an earlier dish-based decision point: whether a neuroinflammatory phenotype is even inducible and measurable in 3D human tissue.
- Makes brain-organoid maturity operational, because the assay depends on late astrocyte emergence and would be much less interpretable in earlier-stage organoids.

## Limitations and caveats

- The assay is largely astrocyte-centered because these organoids do not include a standardized microglial compartment.
- Six-month organoid culture plus vibratome slicing makes this substantially lower throughput than simple monolayer or acute dissociation assays.
- The paper validates the assay mostly in a controlled baseline system, so patient-line variability and disease-specific dynamic range still need case-by-case testing.
- Some supernatant measures are semi-quantitative rather than absolute, so cross-lab comparison will depend on careful normalization.

## Relevance to corpus

- Strengthens the bridge between brain-organoid maturity and assay-layer design in this collection.
- Useful when the real question is not how to make a brain organoid, but how to test inflammasome activation or inhibitor response in human 3D neural tissue.
- Serves as a practical comparator for later infection, transplantation, or perturbation studies that also depend on mature astrocytic or neural states.

## Related concepts

- [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related sources

- [Generation of cerebral organoids from human pluripotent stem cells](lancaster_2014_generation_of_cerebral_organoids_from.md) - the cerebral baseline underlying later assay-layer adaptations like this one.
- [Primitive and Definitive Neural Precursor Cells Are Present in Human Cerebral Organoids](r_2024_primitive-and-definitive-neural-precursor-cells-are-present-in-human-cerebral-organoids.md) - another paper that uses cerebral organoids as a source of interpretable cell-state assays rather than treating morphology as the endpoint.
- [Choroid plexus defects in Down syndrome brain organoids enhance neurotropism of SARS-CoV-2](m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.md) - a complementary mature-brain assay system focused on infection and barrier-linked vulnerability rather than inflammasome activation.

## Open questions

- How much would the signal change once microglia-containing or vascularized cerebral organoid systems are substituted for the astrocyte-dominant baseline here?
- Which patient-specific neuropsychiatric or neurodegenerative lines generate enough dynamic range to make this assay useful for screening rather than just proof-of-principle?
- Does the 4 h optimum remain stable across other cerebral organoid derivation workflows, or is it specific to the maturation state and slicing conditions used here?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:48:27+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids -f json,markdown`
- Manifest: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/opendataloader-run.json](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/opendataloader-run.json)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.json](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.json)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.md](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.md)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile1.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile1.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile10.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile10.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile11.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile11.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile12.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile12.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile13.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile13.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile14.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile14.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile2.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile2.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile3.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile3.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile4.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile4.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile5.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile5.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile6.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile6.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile7.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile7.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile8.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile8.png)
- Output: [raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile9.png](../../raw/derived/opendataloader/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
