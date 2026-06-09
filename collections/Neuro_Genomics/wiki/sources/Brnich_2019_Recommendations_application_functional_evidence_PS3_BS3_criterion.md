---
title: "Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1186/s13073-019-0690-2
pmid: 31892348
authors: Brnich SE et al.
journal: Genome medicine (2019)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Brnich_2019_Recommendations_application_functional_evidence_PS3_BS3_criterion.pdf
pdf_status: downloaded
---

# Recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework.

## Source

- Authors: Brnich SE, Abou Tayoun AN, Couch FJ, Cutting GR, Greenblatt MS, Heinen CD, Kanavy DM, Luo X et al. (on behalf of the ClinGen Sequence Variant Interpretation Working Group)
- Journal: Genome medicine (2019); published in vol. 12:3 (2020)
- DOI: [10.1186/s13073-019-0690-2](https://doi.org/10.1186/s13073-019-0690-2)
- PMID: [31892348](https://pubmed.ncbi.nlm.nih.gov/31892348/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

**BACKGROUND:** The American College of Medical Genetics and Genomics (ACMG)/Association for Molecular Pathology (AMP) clinical variant interpretation guidelines established criteria for different types of evidence. This includes the strong evidence codes PS3 and BS3 for "well-established" functional assays demonstrating a variant has abnormal or normal gene/protein function, respectively. However, they did not provide detailed guidance on how functional evidence should be evaluated, and differences in the application of the PS3/BS3 codes are a contributor to variant interpretation discordance between laboratories. This recommendation seeks to provide a more structured approach to the assessment of functional assays for variant interpretation and guidance on the use of various levels of strength based on assay validation.

**METHODS:** The Clinical Genome Resource (ClinGen) Sequence Variant Interpretation (SVI) Working Group used curated functional evidence from ClinGen Variant Curation Expert Panel-developed rule specifications and expert opinions to refine the PS3/BS3 criteria over multiple in-person and virtual meetings. We estimated the odds of pathogenicity for assays using various numbers of variant controls to determine the minimum controls required to reach moderate level evidence. Feedback from the ClinGen Steering Committee and outside experts were incorporated into the recommendations at multiple stages of development.

**RESULTS:** The SVI Working Group developed recommendations for evaluators regarding the assessment of the clinical validity of functional data and a four-step provisional framework to determine the appropriate strength of evidence that can be applied in clinical variant interpretation. These steps are as follows: (1) define the disease mechanism, (2) evaluate the applicability of general classes of assays used in the field, (3) evaluate the validity of specific instances of assays, and (4) apply evidence to individual variant interpretation. We found that a minimum of 11 total pathogenic and benign variant controls are required to reach moderate-level evidence in the absence of rigorous statistical analysis.

**CONCLUSIONS:** The recommendations and approach to functional evidence evaluation described here should help clarify the clinical variant interpretation process for functional assays. Further, we hope that these recommendations will help develop productive partnerships with basic scientists who have developed functional assays that are useful for interrogating the function of a variety of genes.

## Key findings

- **Functional assays are no longer "strong by default."** Unlike the 2015 ACMG/AMP guidelines (PS3/BS3 = strong for "well-established" assays), the SVI recommends starting from **no evidence (OddsPath ≈ neutral)** and earning strength from demonstrated clinical validation.
- **OddsPath → evidence-strength calibration (Table 3).** OddsPath = [P2 × (1 − P1)] / [(1 − P2) × P1], where P1 = prior (proportion pathogenic among controls) and P2 = posterior (proportion pathogenic among the abnormal- or normal-readout group):

  | OddsPath | Evidence strength |
  |---|---|
  | < 0.053 | BS3 (strong, benign) |
  | < 0.23 | BS3_moderate* |
  | < 0.48 | BS3_supporting |
  | 0.48–2.1 | Indeterminate (no evidence) |
  | > 2.1 | PS3_supporting |
  | > 4.3 | PS3_moderate |
  | **> 18.7** | **PS3 (strong)** |
  | > 350 | PS3_very_strong |

  *No moderate benign code exists in Richards et al., so BS3_moderate = two supporting-level benign instances.
- **Control-count thresholds (no formal statistics; from modeled Table S2, allowing one indeterminate control).**
  - ≤10 validation controls (with experimental controls + replicates) → **PS3/BS3_supporting** only.
  - **≥11 total validation controls** (mix of known benign + known pathogenic) → **PS3/BS3_moderate**.
  - **Strong (PS3 / BS3) or higher requires a formal, statistically derived OddsPath** (e.g., enough controls to compute positive predictive value); strong cannot be reached on control counts alone.
- **Worked example (Fig. 1):** 11 controls (6 LB/B + 5 LP/P) with one benign control giving an indeterminate readout → PS3_moderate / BS3_moderate at the set thresholds.
- **Floor requirements.** Assays lacking *both* a normal/wild-type negative control and an abnormal/null positive control, or lacking technical/biological replicates, should not be used at all (unless the dynamic range and thresholds are extremely well characterized).
- **Standardized terminology (Recommendation 4):** report variant effects as "**functionally normal**" / "**functionally abnormal**" (with granular subtypes — complete LoF, partial LoF / hypomorphic, gain-of-function, dominant-negative), never as "pathogenic," "benign," "deleterious," or "damaging," which conflate assay readout with clinical classification.
- **Functional evidence is never stand-alone:** even a very-strong OddsPath needs at least one other independent evidence type (e.g., PS4) to classify a variant.
- **Anti-circularity rule:** validation controls must reach P/LP or B/LB using evidence *independent of functional data* before they can benchmark the assay.

## Methods

- ClinGen SVI Working Group refined PS3/BS3 over conference calls and in-person meetings (Nov 2018 SVI call; Dec 2018 ClinGen Steering Committee, Seattle; Mar 2019 SVI call; Apr 2019 ACMG meeting), drawing on six published VCEP rule specifications and expert opinion.
- Modeled OddsPath for a theoretical assay over varying numbers of previously classified controls: P1 = prior probability (proportion pathogenic among all modeled controls); P2 = posterior (proportion pathogenic among functionally abnormal/normal readout groups). Strength mapped via the Tavtigian Bayesian adaptation of ACMG/AMP.
- Two scenarios: (S1) perfect binary classifier (all controls concordant); (S2) conservative case adding exactly one misclassified/indeterminate control to each set to avoid posterior odds of 0 or ∞ — the basis for the ≥11-control moderate threshold.
- Output = a **four-step provisional framework**: (1) define gene-disease mechanism (HGNC/MONDO/GO structured narrative; LoF vs GoF vs dominant-negative); (2) evaluate applicability of general assay classes vs that mechanism; (3) evaluate validity of specific assay instances (controls, replicates, OddsPath/PPV); (4) apply to individual variant interpretation. Includes guidance on physiologic context, molecular consequence (NMD, cDNA vs CRISPR endogenous context, splicing vs PVS1/PM4), CLIA vs research labs, and rules for stacking conflicting/concordant assay results.

## Relevance to the brain-organoid ASD review

- **This is the calibration bar the review's organoid assays must clear.** For an organoid functional readout (e.g., neuronal phenotype from a CRISPR-introduced ASD/NDD variant) to count as clinical evidence, it must be benchmarked against an allelic series of known pathogenic and known benign variants and mapped to an OddsPath: **>4.3 → PS3_moderate, >18.7 → PS3 (strong), <0.053 → BS3**.
- **Concrete design constraints for organoid assays:** include matched normal/wild-type and null/abnormal controls plus technical + biological replicates; ≤10 controls caps the assay at *supporting*, ≥11 mixed controls reaches *moderate*, and *strong* needs a statistically derived OddsPath. CRISPR edits in the endogenous genomic context (vs overexpressed cDNA) are favored — relevant because organoid models typically engineer variants at the endogenous locus.
- **Caveats the review must flag:** model-system data (organoids sit between cellular in vitro and patient-derived material) warrant a "nuanced" strength adjustment (Recommendation 2); a "functionally normal" organoid readout may simply mean the relevant function was not assayed (limits BS3); and an assay validated for one disease mechanism does not transfer to a gene's other mechanisms.
- **Multiplexed assays of variant effect (MAVEs)** are explicitly highlighted as the path to strong/very-strong calibration — directly applicable if organoid platforms are scaled to many variants at once.
- Cross-link: functional-evidence consumers in this collection — mosaic/PZM burden in ASD [Lim 2017](Lim_2017_Rates_distribution_implications_postzygotic_mosaic_mutations_autism.md); candidate NDD genes whose variants need PS3/BS3 adjudication [Stessman 2017](Stessman_2017_Targeted_sequencing_identifies_91_neurodevelopmental_disorder_risk.md).

## Open questions / limitations

- Explicitly a **provisional** framework; the OddsPath thresholds and control counts assume the modeled scenarios and are expected to be revised as ACMG/AMP guidelines evolve.
- **No consensus** on combining evidence across *different* assay classes (risk of double-counting non-independent functions); stacking rules for conflicting results remain judgment calls.
- Many historical publications will fail these specs and drop from strong to supporting (or to unusable), shrinking the pool of citable functional evidence.
- Applicability to **rare diseases with few known pathogenic/benign variants** is untested — control-count thresholds may be unreachable.
- Modeled OddsPath assumes controls are correctly pre-classified by independent evidence; mis-/over-fitting and assay-specific dynamic-range issues are acknowledged but not fully resolved.
