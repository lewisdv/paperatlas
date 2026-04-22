---
title: Th2 Cytokines Reshape the Transcriptome: Insights from a Canine Organoid Model of Atopic Dermatitis
kind: paper
status: ingested
added: 2026-04-21T14:30:02+09:00
raw_source: raw/sources/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12984901/
published_date: 2026-02-26
organ: skin
protocol_focus: th2 Cytokines Reshape the Transcriptome: Insights from a Canine Organoid Model of Atopic Dermatitis
deep_ingested: 2026-04-22
---

# Th2 Cytokines Reshape the Transcriptome: Insights from a Canine Organoid Model of Atopic Dermatitis

## Source

- PDF: [raw/sources/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de.pdf](../../raw/sources/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12984901/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12984901/)
- Status: deep ingested 2026-04-22
- Organ focus: primary canine epidermal organoids used as a keratinocyte-only inflammatory skin model
- Protocol focus: expose canine epidermal organoids to IL-4 and IL-13, then use transcriptomics to define which parts of atopic-dermatitis biology are epithelial and Th2 driven

## Study design

- Starting material: canine primary epidermal organoids derived from keratinocytes isolated from healthy skin of four dogs of different breeds
- Protocol stages:
  - establish keratinocyte-only epidermal organoids in Matrigel using the previously described canine primary epidermal organoid workflow
  - stimulate organoids from day 0 with 30 ng/mL IL-4 plus 30 ng/mL IL-13, refresh cytokine-containing medium on days 3 and 6, and maintain cultures to day 8
  - compare treated and untreated organoids by RNA sequencing after 7 days of cytokine exposure, with principal-component and enrichment analyses used to distinguish treatment effects from donor-to-donor variability
  - interpret the transcriptome together with the earlier morphological phenotype reported for the same model, including spongiosis, reduced suprabasal differentiation, and increased Ki67
- Key validation: IL-4 or IL-13-treated organoids reproducibly separated from controls, 224 differentially expressed genes were narrowed to 69 high-confidence disease-relevant genes, and the pathway signal shifted toward immune activation, neuro-immune and calcium pathways, apoptosis or ECM remodeling, and away from epidermal differentiation, keratinization, and lipid metabolism
- Distinct protocol emphasis: this is an epithelial perturbation model rather than a baseline derivation paper, designed to isolate the direct contribution of Th2 cytokines to atopic skin biology

## Summary

- The key move here is not organoid generation itself, but the use of a simplified keratinocyte-only platform to ask which atopic-dermatitis features are directly inducible by Th2 cytokines.
- The paper is strongest when read as a disease-induction assay that separates epithelial-intrinsic responses from immune-cell and fibroblast effects.
- Within this corpus, it extends the assay-layer branch into comparative inflammatory skin biology.

## Key findings

- The organoids support a controlled "inside-out" disease logic in which IL-4 and IL-13 alone can reprogram epidermal organoids toward an atopic-like state.
- Canonical barrier and differentiation programs are suppressed, consistent with the earlier finding that filaggrin and loricrin fall while proliferative and spongiotic features increase.
- The model also surfaces less obvious disease axes, including neuro-immune signaling, calcium handling, pyroptosis-linked genes, ECM remodeling, and metabolic or epigenetic shifts.
- Donor identity still contributes meaningful variance, which is useful because it shows that the platform preserves biological heterogeneity rather than behaving like a fully standardized cell line assay.

## Distinctive contribution in this corpus

- One of the clearest examples in the corpus of using an epithelial organoid as a controlled cytokine-perturbation assay rather than as a developmental endpoint.
- Broadens the collection beyond gut, brain, and tumor organoids into comparative dermatology while still staying within the organoid-assay logic of the corpus.
- Provides a strong counterpoint to more complex coculture systems: here the simplification is deliberate because the question is what Th2 cytokines do to keratinocytes directly.

## Limitations and caveats

- The model is epithelial only, so it cannot recapitulate the full fibroblast, immune-cell, and chronic-cytokine circuitry of canine or human atopic dermatitis.
- Organoids were generated from healthy skin rather than from atopic animals, so intrinsic disease predisposition is not captured here.
- The platform is strongest for acute Th2-response mapping and weaker for chronic remodeling, pruritus circuitry, or multicellular lesion evolution.

## Relevance to corpus

- Strengthens the adult-platform and functional-assay branches with a primary epithelial organoid system built for cytokine-driven disease induction.
- Useful when the biological question is whether a phenotype requires multicellular complexity or can already be seen in an epithelial-only organoid.
- Adds a comparative animal-model angle to the collection without falling back to monolayer keratinocyte culture.

## Related concepts

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related sources

- [Generation and characterization of hair-bearing skin organoids from human pluripotent stem cells](lee_2022_generation_and_characterization_of_hair-bearing.md) - a developmental skin comparator where tissue complexity is generated rather than imposed by cytokine stimulation.
- [Patient-derived and mouse endo-ectocervical organoid generation, genetic manipulation and applications to model infection](gurumurthy_2022_patient-derived_and_mouse_endo-ectocervical_organoid.md) - another epithelial-first organoid platform where perturbation and disease modeling are layered onto a primary tissue baseline.
- [Protocol for the coculture of murine vaginal epithelial organoids and T cells to induce resident memory CD8 T cell differentiation](jc_2025_protocol-for-the-coculture-of-murine-vaginal-epithelial-organoids-and-t-cells-to-induce-re.md) - a mucosal comparator showing what happens when immune partners are deliberately reintroduced rather than intentionally excluded.

## Open questions

- Which transcriptomic changes are fully keratinocyte intrinsic and which would collapse or reverse once fibroblasts or immune cells are added back?
- How differently would organoids derived from atopic dogs respond compared with the healthy-donor organoids used here?
- Which of the newly highlighted pathways, such as neuro-immune or TRP-related signaling, are the best next therapeutic entry points?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:48:19+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de -f json,markdown`
- Manifest: [raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/opendataloader-run.json](../../raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/opendataloader-run.json)
- Output: [raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de.json](../../raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de.json)
- Output: [raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de.md](../../raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de.md)
- Output: [raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile1.png](../../raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile1.png)
- Output: [raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile2.png](../../raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile2.png)
- Output: [raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile3.png](../../raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile3.png)
- Output: [raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile4.png](../../raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile4.png)
- Output: [raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile5.png](../../raw/derived/opendataloader/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de_images/imageFile5.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
