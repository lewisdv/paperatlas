---
title: Clinically used drug arsenic trioxide targets XIAP and overcomes apoptosis resistance in an organoid-based preclinical cancer model
kind: paper
status: ingested
added: 2026-04-21T14:26:13+09:00
raw_source: raw/sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11151819/
published_date: 2024-05-03
organ: cancer
protocol_focus: clinically used drug arsenic trioxide targets XIAP and overcomes apoptosis resistance in an organoid-based preclinical cancer model
deep_ingested: 2026-04-22
---

# Clinically used drug arsenic trioxide targets XIAP and overcomes apoptosis resistance in an organoid-based preclinical cancer model

## Source

- PDF: [raw/sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.pdf](../../raw/sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11151819/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151819/)
- Status: deep ingested 2026-04-22
- Organ focus: patient-derived colon cancer organoids used as translational validation for a broader apoptosis-sensitization mechanism
- Protocol focus: test whether arsenic trioxide can act as a clinically reachable XIAP antagonist and sensitize apoptosis-resistant cancer organoids to cisplatin

## Study design

- Starting material: multiple apoptosis-resistant cancer cell lines plus patient-derived colon cancer organoids from four donors
- Protocol stages:
  - derive colon cancer organoids from patient tumor tissue using a standard tumor-organoid workflow, dissociate them to single cells, and re-embed them in Matrigel for short-term drug testing
  - allow organoids to establish for about 2 days, then expose them to cisplatin at 6.25 or 12.5 uM with or without arsenic trioxide
  - reduce the arsenic trioxide dose to 1 mM for comparative organoid experiments after observing that 2 mM arsenic alone suppressed viability in two of four donor lines
  - quantify viability with CellTiter-Lumi 3D and use Bliss-style combination logic to assess whether arsenic is sensitizing cisplatin response rather than only contributing its own toxicity
  - anchor the organoid findings with mechanistic biochemistry showing that arsenic binds XIAP BIR-domain cysteines, displaces zinc, impairs anti-apoptotic function, and promotes ubiquitination-dependent XIAP degradation
- Key validation: arsenic rapidly depleted XIAP across multiple cancer contexts, and the patient-derived colon cancer organoids became more cisplatin sensitive under the combined treatment than under either agent alone
- Distinct protocol emphasis: the organoid component is a late translational filter for a mechanistic apoptosis paper, not a baseline derivation workflow

## Summary

- The paper is mainly a mechanism-to-validation bridge: first define a plausible druggable apoptosis node, then ask whether patient-derived organoids agree.
- Its most useful contribution to this corpus is showing how organoids can function as a translational checkpoint for combination therapy rather than as the primary experimental system.
- Within this collection, it belongs to the tumor-organoid assay branch more than to the derivation branch.

## Key findings

- Arsenic trioxide is presented here not as a generic cytotoxin but as a direct XIAP antagonist that perturbs BIR-domain zinc coordination and promotes XIAP loss.
- The organoid experiments show that the mechanism is not restricted to immortalized cell lines: patient-derived colon cancer organoids also become more vulnerable to cisplatin when XIAP is targeted this way.
- The paper therefore reframes the organoid assay as a donor-aware sensitization screen, which is more informative than testing single-agent killing alone.

## Distinctive contribution in this corpus

- One of the cleaner examples in the collection of using patient-derived organoids as the last translational sanity check for a mechanistic oncology claim.
- Gives the functional-assay branch a cancer-drug-sensitization paper that is shorter and simpler than xenograft-heavy workflows but still more patient-relevant than cell lines.
- Helps separate two questions that are often conflated: whether a pathway is biologically interesting and whether targeting it actually shifts drug response in donor-derived 3D models.

## Limitations and caveats

- The organoid portion is limited to four colon cancer donor lines and a short-term viability assay, so it is not a broad tumor-organoid platform paper.
- Because arsenic has its own direct toxicity, dose choice matters a lot; the authors had to step down from 2 mM to 1 mM in the organoid setting to keep sensitization interpretable.
- Most mechanistic depth comes from cell lines and biochemistry rather than from deeper multi-omic organoid characterization.

## Relevance to corpus

- Strengthens the functional-assay branch with a compact example of donor-derived tumor organoids used for combination-therapy triage.
- Useful when the question is whether a mechanistic cancer vulnerability is strong enough to survive translation into patient-derived 3D models.
- Pairs well with larger PDO and PDO-X papers in the corpus as a lower-complexity validation layer before escalating into animals or multi-omic host-context studies.

## Related concepts

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related sources

- [Establishment of patient-derived cancer organoids for drug-screening applications](driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) - the more general tumor-PDO baseline for building clinically relevant drug-testing cultures.
- [Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids](j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md) - a richer host-context comparator for cases where simple ex vivo drug response may miss microenvironment-sensitive biology.
- [Patient-derived organoid xenografts reveal the multifaceted role of the lncRNA MALAT1 in breast cancer progression](patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.md) - a more escalated translational workflow where organoid perturbation is carried into in vivo metastasis and stromal readouts.

## Open questions

- Which tumor-organoid features, such as baseline XIAP abundance or apoptosis-state markers, best predict sensitization to arsenic plus cisplatin?
- How generalizable is this combination beyond colon cancer organoids and beyond the specific cisplatin showcase used here?
- At what point should a sensitization signal seen in organoids be escalated into PDO-X or more complex host-context testing?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:49:51+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a -f json,markdown`
- Manifest: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/opendataloader-run.json](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/opendataloader-run.json)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.json](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.json)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.md](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.md)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile1.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile1.png)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile10.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile10.png)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile2.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile2.png)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile3.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile3.png)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile4.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile4.png)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile5.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile5.png)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile6.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile6.png)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile7.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile7.png)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile8.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile8.png)
- Output: [raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile9.png](../../raw/derived/opendataloader/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a_images/imageFile9.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
