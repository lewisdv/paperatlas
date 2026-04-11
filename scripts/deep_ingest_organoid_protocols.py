#!/usr/bin/env python3

import argparse
import csv
import re
import subprocess
import unicodedata
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

from workspace import resolve_workspace


TODAY = "2026-04-08"

PAPER_NOTES = {
    "mccracken_2011_generating_human_intestinal_tissue_from": {
        "bucket": "foundation",
        "contribution": "builds a stepwise hPSC-to-endoderm-to-mid/hindgut route that turns gut spheroids into intestinal organoids",
        "relevance": "foundational entry point for endodermal organoid work in this collection",
        "concepts": [
            "self-organization-and-directed-patterning",
            "gastrointestinal-and-endodermal-organoid-systems",
        ],
    },
    "lancaster_2014_generation_of_cerebral_organoids_from": {
        "bucket": "foundation",
        "contribution": "establishes the classic unguided cerebral organoid workflow with broad regional self-organization",
        "relevance": "the key starting point for later brain-organoid diversification in this corpus",
        "concepts": [
            "self-organization-and-directed-patterning",
            "brain-organoid-patterning-and-assembloids",
            "multi-lineage-and-tissue-complexity",
        ],
    },
    "drost_2016_organoid_culture_systems_for_prostate": {
        "bucket": "adult",
        "contribution": "shows how healthy and cancer prostate organoids can be expanded from primary material rather than only stem-cell differentiation",
        "relevance": "anchors the adult-tissue and disease-modeling side of the corpus",
        "concepts": [
            "adult-stem-cell-and-patient-derived-organoid-platforms",
        ],
    },
    "cattaneo_2019_tumor_organoid-t-cell_coculture_systems": {
        "bucket": "functional",
        "contribution": "turns tumor organoids into an immune-interaction assay by adding T-cell coculture workflows",
        "relevance": "important when the goal is not just culture establishment but testing immune engagement",
        "concepts": [
            "adult-stem-cell-and-patient-derived-organoid-platforms",
            "organoid-functional-assays-transplantation-and-coculture",
        ],
    },
    "driehuis_2020_establishment_of_patient-derived_cancer_organoids": {
        "bucket": "adult",
        "contribution": "focuses on robust establishment of patient-derived cancer organoids for downstream drug-screening workflows",
        "relevance": "one of the clearest translational protocol papers in the organoid set",
        "concepts": [
            "adult-stem-cell-and-patient-derived-organoid-platforms",
            "organoid-functional-assays-transplantation-and-coculture",
        ],
    },
    "hendriks_2020_establishment_of_human_fetal_hepatocyte": {
        "bucket": "engineering",
        "contribution": "combines liver organoid establishment with knockin and knockout workflows",
        "relevance": "useful when organoid derivation and targeted genetic manipulation must live in the same protocol stack",
        "concepts": [
            "adult-stem-cell-and-patient-derived-organoid-platforms",
            "organoid-engineering-imaging-and-screening",
        ],
    },
    "koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from": {
        "bucket": "multi",
        "contribution": "models a foregut-midgut boundary by fusing anterior and posterior spheroids into a hepato-biliary-pancreatic organoid",
        "relevance": "a strong example of why multi-organ boundary models matter beyond single-tissue organoids",
        "concepts": [
            "self-organization-and-directed-patterning",
            "gastrointestinal-and-endodermal-organoid-systems",
            "multi-lineage-and-tissue-complexity",
        ],
    },
    "dekkers_2021_long-term_culture_genetic_manipulation_and": {
        "bucket": "engineering",
        "contribution": "extends breast organoids into long-term culture, genetic manipulation, and xenotransplantation",
        "relevance": "bridges stable patient-derived organoid culture with intervention and in vivo follow-up",
        "concepts": [
            "adult-stem-cell-and-patient-derived-organoid-platforms",
            "organoid-engineering-imaging-and-screening",
            "organoid-functional-assays-transplantation-and-coculture",
        ],
    },
    "drakhlis_2021_generation_of_heart-forming_organoids_from": {
        "bucket": "multi",
        "contribution": "captures early cardiac morphogenesis in a structured heart-forming organoid model",
        "relevance": "the main baseline cardiac protocol that later heart extensions build on",
        "concepts": [
            "self-organization-and-directed-patterning",
            "cardiac-and-hematoendothelial-organoids",
            "multi-lineage-and-tissue-complexity",
        ],
    },
    "vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney": {
        "bucket": "foundation",
        "contribution": "optimizes kidney differentiation toward stronger proximal-tubule representation",
        "relevance": "shows the field moving from generic kidney organoids toward segment-biased refinement",
        "concepts": [
            "self-organization-and-directed-patterning",
            "kidney-organoid-differentiation-routes",
        ],
    },
    "xia_2014_the_generation_of_kidney_organoids": {
        "bucket": "foundation",
        "contribution": "uses a ureteric-bud-progenitor route and chimeric culture logic rather than a nephron-only strategy",
        "relevance": "important for understanding one of the early branching choices in kidney organoid design",
        "concepts": [
            "self-organization-and-directed-patterning",
            "kidney-organoid-differentiation-routes",
        ],
    },
    "takasato_2016_generation_of_kidney_organoids_from": {
        "bucket": "foundation",
        "contribution": "details a widely used kidney workflow that brings multiple renal progenitor populations into the same culture",
        "relevance": "one of the central reference protocols for nephron-rich kidney organoids",
        "concepts": [
            "self-organization-and-directed-patterning",
            "kidney-organoid-differentiation-routes",
        ],
    },
    "morizane_2016_generation_of_nephron_progenitor_cells": {
        "bucket": "foundation",
        "contribution": "prioritizes high-efficiency nephron-progenitor generation as a cleaner entry into kidney organoid production",
        "relevance": "useful when reproducibility and progenitor purity matter more than maximal developmental breadth",
        "concepts": [
            "self-organization-and-directed-patterning",
            "kidney-organoid-differentiation-routes",
        ],
    },
    "broutier_2016_culture_and_establishment_of_self-renewing": {
        "bucket": "engineering",
        "contribution": "establishes expandable adult liver and pancreas organoids and pairs them with genetic manipulation",
        "relevance": "a core adult endoderm protocol for long-term expansion rather than developmental differentiation",
        "concepts": [
            "adult-stem-cell-and-patient-derived-organoid-platforms",
            "gastrointestinal-and-endodermal-organoid-systems",
            "organoid-engineering-imaging-and-screening",
        ],
    },
    "sloan_2018_generation_and_assembly_of_human": {
        "bucket": "foundation",
        "contribution": "builds dorsal and ventral forebrain spheroids and then assembles them to study migration and circuit formation",
        "relevance": "the clearest directed-brain alternative to unguided cerebral organoids in this corpus",
        "concepts": [
            "self-organization-and-directed-patterning",
            "brain-organoid-patterning-and-assembloids",
        ],
    },
    "giandomenico_2021_generation_and_long-term_culture_of": {
        "bucket": "foundation",
        "contribution": "pushes cerebral organoids toward later-stage neural development and longer maturation windows",
        "relevance": "important for users who care more about long-term maturation than only early tissue generation",
        "concepts": [
            "self-organization-and-directed-patterning",
            "brain-organoid-patterning-and-assembloids",
            "multi-lineage-and-tissue-complexity",
        ],
    },
    "puschhof_2021_intestinal_organoid_cocultures_with_microbes": {
        "bucket": "functional",
        "contribution": "adds lumenal microinjection, 2D exposure, and microbial viability workflows to intestinal organoids",
        "relevance": "a strong example of organoids becoming host-microbe assay systems rather than only developmental models",
        "concepts": [
            "gastrointestinal-and-endodermal-organoid-systems",
            "organoid-functional-assays-transplantation-and-coculture",
        ],
    },
    "co_2021_controlling_the_polarity_of_human": {
        "bucket": "functional",
        "contribution": "re-engineers epithelial polarity so apical biology becomes experimentally accessible",
        "relevance": "particularly useful when infection or barrier questions are blocked by standard inward-facing organoid geometry",
        "concepts": [
            "gastrointestinal-and-endodermal-organoid-systems",
            "organoid-functional-assays-transplantation-and-coculture",
        ],
    },
    "watanabe_2022_transplantation_of_intestinal_organoids_into": {
        "bucket": "transplantation",
        "contribution": "moves intestinal organoids into an in vivo repair context using a colitis model",
        "relevance": "one of the most direct translational validation protocols in the collection",
        "concepts": [
            "gastrointestinal-and-endodermal-organoid-systems",
            "organoid-functional-assays-transplantation-and-coculture",
        ],
    },
    "matkovicleko_2023_a_distal_lung_organoid_model": {
        "bucket": "multi",
        "contribution": "positions distal lung organoids as a disease, infection, and developmental model in one workflow",
        "relevance": "broadens the collection beyond gut, brain, kidney, and heart into respiratory tissue",
        "concepts": [
            "self-organization-and-directed-patterning",
            "multi-lineage-and-tissue-complexity",
        ],
    },
    "broda_2018_generation_of_human_antral_and": {
        "bucket": "foundation",
        "contribution": "separates gastric differentiation into antral and fundic trajectories from pluripotent stem cells",
        "relevance": "useful when a generic gut protocol is too coarse and gastric subtype identity matters",
        "concepts": [
            "self-organization-and-directed-patterning",
            "gastrointestinal-and-endodermal-organoid-systems",
        ],
    },
    "miller_2019_generation_of_lung_organoids_from": {
        "bucket": "foundation",
        "contribution": "offers a baseline pluripotent-stem-cell route into lung organoid generation",
        "relevance": "serves as the foundational respiratory protocol before later disease-specific lung refinements",
        "concepts": [
            "self-organization-and-directed-patterning",
            "multi-lineage-and-tissue-complexity",
        ],
    },
    "lee_2022_generation_and_characterization_of_hair-bearing": {
        "bucket": "multi",
        "contribution": "builds skin organoids with appendages and sensory features rather than a simple epithelial sheet",
        "relevance": "a good example of organoid protocols reaching tissue complexity beyond single-cell-layer models",
        "concepts": [
            "self-organization-and-directed-patterning",
            "multi-lineage-and-tissue-complexity",
        ],
    },
    "olijnik_2024_generating_human_bone_marrow_organoids": {
        "bucket": "multi",
        "contribution": "creates a bone marrow niche model with vascular, stromal, and hematopoietic elements",
        "relevance": "extends the collection into non-epithelial organoid territory and niche modeling",
        "concepts": [
            "multi-lineage-and-tissue-complexity",
            "organoid-functional-assays-transplantation-and-coculture",
        ],
    },
    "fitzgerald_2024_generation_of_semi-guided_cortical_organoids": {
        "bucket": "engineering",
        "contribution": "positions semi-guided cortical organoids as a reproducible platform for oscillations, calcium imaging, and MEA readouts",
        "relevance": "captures the intermediate space between unguided diversity and tightly guided patterning",
        "concepts": [
            "self-organization-and-directed-patterning",
            "brain-organoid-patterning-and-assembloids",
            "organoid-engineering-imaging-and-screening",
        ],
    },
    "kelley_2024_host_circuit_engagement_of_human": {
        "bucket": "transplantation",
        "contribution": "uses transplantation to test whether cortical organoids engage host neural circuits in vivo",
        "relevance": "important when maturation and circuit claims need stronger validation than dish-based assays alone",
        "concepts": [
            "brain-organoid-patterning-and-assembloids",
            "organoid-functional-assays-transplantation-and-coculture",
        ],
    },
    "ullah_2025_generating_and_characterizing_human_telencephalic": {
        "bucket": "foundation",
        "contribution": "starts from single neural rosettes to tighten telencephalic brain organoid generation",
        "relevance": "represents a newer attempt to reduce starting-state variability in brain organoid workflows",
        "concepts": [
            "self-organization-and-directed-patterning",
            "brain-organoid-patterning-and-assembloids",
        ],
    },
    "dardano_2025_production_of_human_blood-generating_heart-forming": {
        "bucket": "engineering",
        "contribution": "extends heart-forming organoids toward blood generation and pairs them with scalable clearing and imaging preparation",
        "relevance": "connects developmental heart organoids to hematoendothelial co-development and better morphology readouts",
        "concepts": [
            "cardiac-and-hematoendothelial-organoids",
            "multi-lineage-and-tissue-complexity",
            "organoid-engineering-imaging-and-screening",
        ],
    },
    "meng_2025_crispr_screens_in_human_neural": {
        "bucket": "engineering",
        "contribution": "turns neural organoids and assembloids into pooled CRISPR screening systems",
        "relevance": "a high-leverage protocol when the goal shifts from making organoids to perturbing them systematically",
        "concepts": [
            "brain-organoid-patterning-and-assembloids",
            "organoid-engineering-imaging-and-screening",
        ],
    },
}

CONCEPT_PAGES = OrderedDict(
    [
        (
            "self-organization-and-directed-patterning",
            {
                "title": "Self-organization and directed patterning",
                "sources": [
                    "lancaster_2014_generation_of_cerebral_organoids_from",
                    "mccracken_2011_generating_human_intestinal_tissue_from",
                    "takasato_2016_generation_of_kidney_organoids_from",
                    "morizane_2016_generation_of_nephron_progenitor_cells",
                    "sloan_2018_generation_and_assembly_of_human",
                    "fitzgerald_2024_generation_of_semi-guided_cortical_organoids",
                    "ullah_2025_generating_and_characterizing_human_telencephalic",
                ],
                "position": "This corpus repeatedly shows the main protocol design tradeoff in organoid work: broad self-organization gives richer tissue diversity, while stronger patterning gives cleaner identity and better reproducibility.",
                "synthesis": [
                    "Unguided or lightly guided protocols such as Lancaster and some later brain workflows are strongest when emergent architecture and cell-type diversity are part of the biological question.",
                    "More directed protocols such as McCracken, Morizane, Takasato, Sloan, and Ullah are better when a specific organ region or lineage must be generated reproducibly.",
                    "Recent protocols increasingly aim for an intermediate position rather than a strict binary, especially in the brain-organoid literature.",
                ],
                "tension": [
                    "diversity and self-organization versus reproducibility and subtype control",
                    "developmental breadth versus assay tractability",
                ],
                "questions": [
                    "How much heterogeneity is acceptable for a given experimental question?",
                    "Which steps matter most for reducing line-to-line and batch variability without overspecifying the tissue?",
                ],
            },
        ),
        (
            "brain-organoid-patterning-and-assembloids",
            {
                "title": "Brain organoid patterning and assembloids",
                "sources": [
                    "lancaster_2014_generation_of_cerebral_organoids_from",
                    "sloan_2018_generation_and_assembly_of_human",
                    "giandomenico_2021_generation_and_long-term_culture_of",
                    "fitzgerald_2024_generation_of_semi-guided_cortical_organoids",
                    "kelley_2024_host_circuit_engagement_of_human",
                    "ullah_2025_generating_and_characterizing_human_telencephalic",
                    "meng_2025_crispr_screens_in_human_neural",
                ],
                "position": "Brain-organoid protocols in this collection have already split into distinct subfamilies: broad cerebral self-organization, region-specific forebrain patterning, long-term maturation, transplantation, and perturbation-ready assembloid systems.",
                "synthesis": [
                    "Lancaster remains the self-organizing cerebral reference point, whereas Sloan and Ullah move toward cleaner forebrain or telencephalic control.",
                    "Giandomenico and Fitzgerald emphasize later-stage maturation and functional readouts rather than only tissue generation.",
                    "Kelley and Meng show that modern brain workflows increasingly depend on transplantation or pooled perturbation rather than morphology alone.",
                ],
                "tension": [
                    "whole-cerebral diversity versus region-specific precision",
                    "in vitro maturation versus host-assisted validation",
                ],
                "questions": [
                    "Which brain questions require assembloids or transplantation rather than single-organoid cultures?",
                    "What is the best tradeoff between regional control, long-term survival, and experimental throughput?",
                ],
            },
        ),
        (
            "gastrointestinal-and-endodermal-organoid-systems",
            {
                "title": "Gastrointestinal and endodermal organoid systems",
                "sources": [
                    "mccracken_2011_generating_human_intestinal_tissue_from",
                    "broda_2018_generation_of_human_antral_and",
                    "puschhof_2021_intestinal_organoid_cocultures_with_microbes",
                    "co_2021_controlling_the_polarity_of_human",
                    "watanabe_2022_transplantation_of_intestinal_organoids_into",
                    "broutier_2016_culture_and_establishment_of_self-renewing",
                    "koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from",
                ],
                "position": "The endodermal side of the corpus spans both foundational derivation and later assay engineering, from gut and gastric generation through polarity control, microbe exposure, transplantation, and multi-organ boundary models.",
                "synthesis": [
                    "McCracken and Broda provide the developmental starting points for intestinal and gastric identity from pluripotent cells.",
                    "Puschhof, Co, and Watanabe show how intestinal organoids become experimentally useful when lumen access, polarity, host interaction, or transplantation are built in.",
                    "Koike and Broutier broaden endodermal work toward boundary models and adult self-renewing tissue systems.",
                ],
                "tension": [
                    "developmental derivation versus downstream assay engineering",
                    "simple epithelial models versus boundary-connected or repair-oriented systems",
                ],
                "questions": [
                    "When is a baseline gut or gastric protocol enough, and when is polarity control or transplantation essential?",
                    "How far can endodermal protocols be pushed toward multi-organ connectivity without sacrificing robustness?",
                ],
            },
        ),
        (
            "kidney-organoid-differentiation-routes",
            {
                "title": "Kidney organoid differentiation routes",
                "sources": [
                    "xia_2014_the_generation_of_kidney_organoids",
                    "takasato_2016_generation_of_kidney_organoids_from",
                    "morizane_2016_generation_of_nephron_progenitor_cells",
                    "vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney",
                ],
                "position": "Kidney protocols in this collection are less about whether organoids are possible and more about which developmental route and segment balance should be prioritized.",
                "synthesis": [
                    "Xia emphasizes a ureteric-bud-oriented route and chimeric assembly logic.",
                    "Takasato pushes toward a broader kidney model that includes several renal progenitor compartments.",
                    "Morizane and Vanslambrouck illustrate the newer move toward efficiency and segment-biased refinement rather than a single generic kidney organoid recipe.",
                ],
                "tension": [
                    "broad renal complexity versus cleaner progenitor control",
                    "general kidney identity versus segment-enriched optimization",
                ],
                "questions": [
                    "Which kidney differentiation route best matches the disease or screening question at hand?",
                    "How much specialization is worth the tradeoff in developmental breadth or compatibility with older protocols?",
                ],
            },
        ),
        (
            "cardiac-and-hematoendothelial-organoids",
            {
                "title": "Cardiac and hematoendothelial organoids",
                "sources": [
                    "drakhlis_2021_generation_of_heart-forming_organoids_from",
                    "dardano_2025_production_of_human_blood-generating_heart-forming",
                ],
                "position": "The heart-oriented papers show a progression from early heart-forming organoids to more elaborate models that include vascular and hematopoietic co-development plus imaging preparation.",
                "synthesis": [
                    "Drakhlis is the baseline developmental heart-forming protocol in this collection.",
                    "Dardano extends that platform into blood-generating heart-forming organoids and better whole-mount imaging workflows.",
                    "Together they show that cardiac organoids are moving toward multi-lineage developmental windows rather than isolated cardiomyocyte production.",
                ],
                "tension": [
                    "cardiac morphogenesis models versus broader co-developmental systems",
                    "protocol speed versus structural richness and imaging depth",
                ],
                "questions": [
                    "How much added value comes from hematoendothelial co-development for a given heart study?",
                    "Which readouts best justify the extra complexity of blood-generating cardiac models?",
                ],
            },
        ),
        (
            "adult-stem-cell-and-patient-derived-organoid-platforms",
            {
                "title": "Adult stem cell and patient-derived organoid platforms",
                "sources": [
                    "drost_2016_organoid_culture_systems_for_prostate",
                    "driehuis_2020_establishment_of_patient-derived_cancer_organoids",
                    "hendriks_2020_establishment_of_human_fetal_hepatocyte",
                    "dekkers_2021_long-term_culture_genetic_manipulation_and",
                    "broutier_2016_culture_and_establishment_of_self-renewing",
                ],
                "position": "Not all organoid workflows in this corpus are developmental hPSC differentiations. A major branch instead expands adult, fetal, or patient-derived tissue into organoid platforms that are closer to donor biology and often more immediately translational.",
                "synthesis": [
                    "These protocols are strongest when donor context, tumor state, or long-term expandability matter more than recapitulating early embryogenesis.",
                    "They also tend to be the quickest route into perturbation, drug screening, or xenotransplantation once tissue access is solved.",
                    "The main tradeoff is that they often preserve epithelial or disease-specific features better than they capture whole-organ developmental context.",
                ],
                "tension": [
                    "developmental fidelity versus donor or disease specificity",
                    "expandable epithelial platforms versus multicompartment organ complexity",
                ],
                "questions": [
                    "When should a project start from patient-derived tissue rather than from pluripotent differentiation?",
                    "Which missing stromal, immune, or vascular compartments most limit interpretation in adult or tumor organoid systems?",
                ],
            },
        ),
        (
            "multi-lineage-and-tissue-complexity",
            {
                "title": "Multi-lineage and tissue complexity",
                "sources": [
                    "lancaster_2014_generation_of_cerebral_organoids_from",
                    "koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from",
                    "drakhlis_2021_generation_of_heart-forming_organoids_from",
                    "matkovicleko_2023_a_distal_lung_organoid_model",
                    "lee_2022_generation_and_characterization_of_hair-bearing",
                    "olijnik_2024_generating_human_bone_marrow_organoids",
                    "dardano_2025_production_of_human_blood-generating_heart-forming",
                ],
                "position": "A major trend across this collection is the move away from simple epithelial balls toward organoids with multiple coordinated lineages, appendages, or anatomical boundary relationships.",
                "synthesis": [
                    "Lancaster, Lee, and some cardiac papers show the value of emergent tissue complexity.",
                    "Koike and Dardano explicitly pursue linked developmental programs across neighboring organs or hematopoietic compartments.",
                    "Olijnik and Matkovic Leko push organoid logic into niche or disease contexts where multicellular composition is central to the model.",
                ],
                "tension": [
                    "biological richness versus protocol simplicity and scalability",
                    "compositional realism versus clean mechanistic interpretation",
                ],
                "questions": [
                    "Which extra tissue compartments materially change the answer to the biological question?",
                    "When does added complexity improve realism, and when does it mostly increase variability?",
                ],
            },
        ),
        (
            "organoid-functional-assays-transplantation-and-coculture",
            {
                "title": "Organoid functional assays, transplantation, and coculture",
                "sources": [
                    "cattaneo_2019_tumor_organoid-t-cell_coculture_systems",
                    "puschhof_2021_intestinal_organoid_cocultures_with_microbes",
                    "co_2021_controlling_the_polarity_of_human",
                    "watanabe_2022_transplantation_of_intestinal_organoids_into",
                    "kelley_2024_host_circuit_engagement_of_human",
                    "olijnik_2024_generating_human_bone_marrow_organoids",
                ],
                "position": "Several papers in this corpus are best understood as second-wave protocols: they assume an organoid already exists, then teach how to expose it to microbes, immune cells, injury models, or host tissue.",
                "synthesis": [
                    "These workflows matter because many organoid questions are really assay-design problems rather than derivation problems.",
                    "They often determine whether the resulting model is useful for infection, immune interaction, repair, or circuit-engagement questions.",
                    "Their success depends heavily on the maturity, polarity, and baseline quality of the starting organoid culture.",
                ],
                "tension": [
                    "baseline organoid robustness versus sophistication of the downstream assay layer",
                    "controlled in vitro exposure versus more realistic but noisier in vivo validation",
                ],
                "questions": [
                    "What baseline maturity or polarity is required before a coculture or transplantation result is believable?",
                    "Which assays genuinely add biological insight rather than just technical complexity?",
                ],
            },
        ),
        (
            "organoid-engineering-imaging-and-screening",
            {
                "title": "Organoid engineering, imaging, and screening",
                "sources": [
                    "hendriks_2020_establishment_of_human_fetal_hepatocyte",
                    "dekkers_2021_long-term_culture_genetic_manipulation_and",
                    "broutier_2016_culture_and_establishment_of_self-renewing",
                    "fitzgerald_2024_generation_of_semi-guided_cortical_organoids",
                    "dardano_2025_production_of_human_blood-generating_heart-forming",
                    "meng_2025_crispr_screens_in_human_neural",
                ],
                "position": "The newest protocols in this collection do not stop at making organoids. They increasingly add gene editing, pooled perturbation, viral delivery, advanced imaging, or whole-mount preparation to turn organoids into higher-leverage experimental systems.",
                "synthesis": [
                    "Engineering layers make organoids much more useful for mechanism, screening, and lineage interrogation.",
                    "At the same time, these workflows usually assume that the baseline organoid pipeline is already stable and reproducible.",
                    "The practical bottleneck often shifts from differentiation itself to delivery, imaging quality, screen design, or readout normalization.",
                ],
                "tension": [
                    "organoid generation as an endpoint versus organoid generation as a platform for perturbation",
                    "experimental leverage versus technical overhead",
                ],
                "questions": [
                    "Which engineering layer adds the most insight for the least extra protocol burden?",
                    "How should screening or imaging workflows be standardized across organoid lines and batches?",
                ],
            },
        ),
    ]
)


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = (
        text.replace("ﬁ", "fi")
        .replace("ﬂ", "fl")
        .replace("–", "-")
        .replace("—", "-")
        .replace("’", "'")
        .replace("‘", "'")
        .replace("“", '"')
        .replace("”", '"')
    )
    return text


def clean_line(line: str) -> str:
    return re.sub(r"\s+", " ", normalize_text(line)).strip()


def is_noise_line(line: str) -> bool:
    lower = line.lower()
    if not line:
        return True
    if lower in {"protocol", "abstract", "key points", "introduction"}:
        return True
    if lower.startswith("https://doi.org/"):
        return True
    if lower.startswith("nature protocols"):
        return True
    if "check for updates" in lower:
        return True
    if "correspondence should be addressed" in lower:
        return True
    if "e-mail:" in lower or lower.startswith("e-mail:"):
        return True
    if lower.startswith("published online"):
        return True
    if lower.startswith("received:") or lower.startswith("accepted:"):
        return True
    if lower.startswith("www.nature.com"):
        return True
    if "✉" in line:
        return True
    if re.search(r"\b\d{1,2}(?:,\d{3})*\b", line) and line.count(",") >= 2 and "." not in line:
        return True
    if re.fullmatch(r"[0-9():,;\- ]+", line):
        return True
    return False


def first_sentences(text: str, max_sentences: int = 2, max_chars: int = 320) -> str:
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", text)
    chosen = []
    total = 0
    for part in parts:
        part = part.strip()
        if not part:
            continue
        candidate_total = total + len(part) + (1 if chosen else 0)
        if chosen and (len(chosen) >= max_sentences or candidate_total > max_chars):
            break
        chosen.append(part)
        total = candidate_total
        if len(chosen) >= max_sentences:
            break
    return " ".join(chosen).strip()


def clean_scope_sentence(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^\d+/\S+\s*", "", text)
    text = re.sub(r"^\d+\s*", "", text)
    text = re.sub(r"^Key points\s*", "", text, flags=re.I)
    text = re.sub(r"^Abstract\s*", "", text, flags=re.I)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_scope_from_plain_text(pdf_path: Path) -> str:
    try:
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "2", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        return ""

    text = normalize_text(result.stdout.replace("\f", "\n"))
    text = re.sub(r"\s+", " ", text)
    patterns = [
        r"Abstract\s+(.*?)\s+(?:Key points|Introduction)",
        r"Published online .*?; doi:[^.]+\.\s*(.*?)\s*INTRODUCTION",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.I | re.S)
        if match:
            return clean_scope_sentence(first_sentences(match.group(1).strip()))
    return ""


def extract_scope(pdf_path: Path) -> str:
    plain_scope = extract_scope_from_plain_text(pdf_path)
    if plain_scope:
        return plain_scope

    try:
        result = subprocess.run(
            ["pdftotext", "-layout", "-f", "1", "-l", "2", str(pdf_path), "-"],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        return ""

    raw_lines = [clean_line(line) for line in result.stdout.replace("\f", "\n").splitlines()]
    lines = [line for line in raw_lines if line]

    if not lines:
        return ""

    intro_idx = None
    for idx, line in enumerate(lines):
        if line.lower() == "introduction":
            intro_idx = idx
            break
    if intro_idx is None:
        intro_idx = min(len(lines), 80)

    start = None
    for idx, line in enumerate(lines[:intro_idx]):
        if line.lower() == "abstract":
            start = idx + 1
            break

    if start is None:
        for idx, line in enumerate(lines[:intro_idx]):
            if is_noise_line(line):
                continue
            lower = line.lower()
            if (
                len(line.split()) >= 12
                and not line.startswith("*")
                and re.search(r"\b(protocol|organoid|organoids|cells?|tissue|culture|development|model|spheroid|differentiation)\b", lower)
            ):
                start = idx
                break

    if start is None:
        return ""

    collected = []
    for line in lines[start:intro_idx]:
        if is_noise_line(line):
            continue
        if len(line.split()) < 4:
            continue
        if line.lower().startswith("key references"):
            break
        collected.append(line)
        joined = " ".join(collected)
        if len(joined) > 900:
            break

    scope = re.sub(r"\s+", " ", " ".join(collected)).strip()
    return clean_scope_sentence(first_sentences(scope))


def protocol_stem(row: dict) -> str:
    return Path(row["source_page"]).stem


def short_label(row: dict) -> str:
    return f"{row['first_author']} {row['year']}"


def readable_organ(row: dict) -> str:
    mapping = {
        "colon-intestine": "colon / intestine",
        "hepato-biliary-pancreatic": "hepato-biliary-pancreatic",
        "bone-marrow": "bone marrow",
        "liver-pancreas": "liver / pancreas",
    }
    return mapping.get(row["organ"], row["organ"].replace("-", " "))


def starting_material(row: dict) -> str:
    title_lower = row["title"].lower()
    focus_lower = row["focus"].lower()
    scope_lower = row.get("scope", "").lower()
    organ = row["organ"]
    if "patient-derived" in title_lower:
        return "patient-derived tumor tissue or matched clinical samples"
    if "circulating tumor cells" in focus_lower or organ in {"tumor", "cancer", "prostate", "breast"}:
        return "primary healthy or disease tissue, tumor material, and related patient samples"
    if "adult" in title_lower or "self-renewing" in title_lower:
        return "adult stem or progenitor cells from primary tissue"
    if "fetal hepatocyte" in title_lower:
        return "human fetal liver-derived organoid cultures"
    if "microbes" in title_lower:
        return "pre-established intestinal organoids plus bacterial, viral, or microbial cultures"
    if "transplantation" in title_lower or "transplanted" in title_lower:
        return "pre-established organoids combined with an in vivo recipient assay"
    if "crispr" in title_lower or "genetic manipulation" in title_lower:
        return "pre-established organoids prepared for perturbation, editing, or screening"
    if (
        "pluripotent stem cells" in title_lower
        or "pluripotent cells" in title_lower
        or "stem cells" in scope_lower
        or "hpsc" in scope_lower
        or "ipsc" in scope_lower
    ):
        return "human pluripotent stem cells"
    if organ == "brain" and not any(
        key in title_lower for key in ["transplanted", "crispr", "screen", "host circuit"]
    ):
        return "human pluripotent stem cells"
    return "pre-established organoid cultures or matched source tissue"


def with_indefinite_article(text: str) -> str:
    article = "an" if text[:1].lower() in {"a", "e", "i", "o", "u"} else "a"
    return f"{article} {text}"


def protocol_type(bucket: str) -> str:
    mapping = {
        "foundation": "stepwise derivation and maturation protocol",
        "adult": "primary-tissue or patient-derived organoid culture protocol",
        "functional": "functional assay extension layered onto organoid culture",
        "engineering": "engineering, imaging, or perturbation protocol layered onto organoid culture",
        "multi": "multi-lineage developmental organoid protocol",
        "transplantation": "transplantation or host-engagement protocol",
    }
    return mapping[bucket]


def core_readouts(row: dict, bucket: str) -> str:
    title_lower = row["title"].lower()
    if "oscillation" in title_lower or "microelectrode" in title_lower:
        return "electrophysiology, calcium imaging, and viral-delivery-compatible brain readouts"
    if "crispr" in title_lower:
        return "pooled perturbation, selection, and follow-up validation workflows"
    if "microbes" in title_lower:
        return "microinjection, microbial viability, microscopy, and sequencing-ready coculture measurements"
    if "polarity" in title_lower:
        return "apical versus basal exposure experiments and epithelial-access assays"
    if "transplantation" in title_lower or "transplanted" in title_lower:
        return "engraftment, repair, or host-integration readouts in vivo"
    if re.search(r"\bgene\b", title_lower) or "genetic manipulation" in title_lower:
        return "editing, manipulation, and downstream phenotyping workflows"
    if bucket == "adult":
        return "organoid establishment, long-term expansion, and disease- or donor-relevant downstream assays"
    return "organoid morphology, lineage markers, and downstream functional assays"


def summary_bullets(row: dict, note: dict, scope: str) -> list[str]:
    corpus_line = {
        "foundation": "Within this collection, it belongs to the baseline derivation branch of organoid protocol work.",
        "adult": "Within this collection, it belongs to the adult or patient-derived platform branch of organoid protocol work.",
        "functional": "Within this collection, it belongs to the assay-extension branch of organoid protocol work.",
        "engineering": "Within this collection, it belongs to the engineering and readout-expansion branch of organoid protocol work.",
        "multi": "Within this collection, it belongs to the multi-lineage and complexity-oriented branch of organoid protocol work.",
        "transplantation": "Within this collection, it belongs to the host-context and transplantation branch of organoid protocol work.",
    }[note["bucket"]]
    bullets = [
        f"This paper is best understood as {with_indefinite_article(protocol_type(note['bucket']))} for {row['focus']}.",
        f"Its main distinctive contribution in this corpus is that it {note['contribution']}.",
        corpus_line,
    ]
    if scope:
        bullets.append(f"Paper framing: {scope}")
    return bullets


def key_findings(row: dict, note: dict) -> list[str]:
    bucket = note["bucket"]
    bullets = [
        f"Defines a workflow centered on {row['focus']}.",
        f"Its distinctive focus in practice is the way it {note['contribution']}.",
    ]
    if bucket == "foundation":
        bullets.append("Serves as a baseline generation protocol that other assay, maturation, or perturbation papers can build on.")
    elif bucket == "adult":
        bullets.append("Shows that expandable organoid platforms can come from primary or patient material, not only from pluripotent differentiation.")
    elif bucket == "functional":
        bullets.append("Demonstrates that experimental value often comes from the assay layer added on top of an existing organoid rather than from derivation alone.")
    elif bucket == "engineering":
        bullets.append("Adds a leverage layer such as imaging, editing, or screening that turns organoids into more mechanistic systems.")
    elif bucket == "multi":
        bullets.append("Prioritizes multicompartment or boundary biology that would be missed in simpler single-lineage cultures.")
    elif bucket == "transplantation":
        bullets.append("Pushes the model into a host or injury context to test whether in vitro claims hold up in a more functional setting.")
    return bullets


def strengths(bucket: str) -> list[str]:
    mapping = {
        "foundation": [
            "Useful as a starting-point protocol for building this organ system from stem cells.",
            "Makes lineage commitments and media transitions explicit enough to anchor comparison across later protocols.",
        ],
        "adult": [
            "Closer to donor or disease-specific biology than a generic pluripotent derivation alone.",
            "Expandable enough to support downstream drug testing, perturbation, or translational work once established.",
        ],
        "functional": [
            "Moves organoids beyond derivation into a biologically interpretable assay context.",
            "Clarifies how to operationalize exposure, coculture, or host interaction instead of leaving it as an ad hoc extension.",
        ],
        "engineering": [
            "Adds a reusable perturbation or imaging layer that increases experimental leverage.",
            "Makes organoids more compatible with mechanistic and platform-style studies.",
        ],
        "multi": [
            "Captures relationships among multiple lineages or tissue compartments rather than isolating a single fate.",
            "Useful when single-tissue organoids are too simple for the developmental question.",
        ],
        "transplantation": [
            "Tests organoid behavior in a host or injury context rather than staying purely in vitro.",
            "Brings maturation, repair, or integration claims closer to functional validation.",
        ],
    }
    return mapping[bucket]


def limitations(bucket: str) -> list[str]:
    mapping = {
        "foundation": [
            "Still likely to depend on stem-cell line quality, timing precision, and local optimization.",
            "Baseline derivation protocols often need additional maturation or assay layers before they answer higher-order biological questions.",
        ],
        "adult": [
            "Requires access to suitable primary or patient tissue and careful tissue-specific media handling.",
            "May capture epithelial or donor-specific behavior better than whole-organ multicompartment biology.",
        ],
        "functional": [
            "Best treated as an extension protocol, not a replacement for a stable baseline organoid pipeline.",
            "Assay outcomes can be dominated by the quality, polarity, or maturity of the starting organoid culture.",
        ],
        "engineering": [
            "Usually assumes that the baseline organoid system is already robust before engineering begins.",
            "Technical failure modes may come from delivery, imaging, or screen design rather than from the organoid biology itself.",
        ],
        "multi": [
            "More complex systems are harder to standardize and interpret than simpler single-lineage cultures.",
            "Some compartments may remain immature or only partially faithful even when the structure is biologically appealing.",
        ],
        "transplantation": [
            "Host environment becomes part of the phenotype, which makes attribution harder.",
            "In vivo logistics and recipient variability increase the practical barrier to adoption.",
        ],
    }
    return mapping[bucket]


def relevance_lines(row: dict, note: dict) -> list[str]:
    lines = [
        f"Specific role in this corpus: {note['relevance'][0].upper() + note['relevance'][1:]}.",
        f"This paper broadens the collection's coverage of {readable_organ(row)} organoid work.",
    ]
    bucket = note["bucket"]
    if bucket == "foundation":
        lines.append("It is most valuable as a baseline protocol to compare against later assay, maturation, or refinement papers.")
    elif bucket == "adult":
        lines.append("It helps keep the collection from collapsing into hPSC-only developmental protocols.")
    elif bucket == "functional":
        lines.append("It represents the second-wave move from making organoids to actually using them in a biologically specific experiment.")
    elif bucket == "engineering":
        lines.append("It matters because many practical organoid projects stall at the perturbation or readout stage rather than at derivation.")
    elif bucket == "multi":
        lines.append("It shows why multi-lineage or boundary-level models are often needed when single-tissue organoids become too reductionist.")
    elif bucket == "transplantation":
        lines.append("It is one of the clearest reminders that some claims about repair, maturation, or circuit engagement need host-context testing.")
    return lines


def open_questions(row: dict, note: dict) -> list[str]:
    bucket = note["bucket"]
    organ = readable_organ(row)
    if bucket == "foundation":
        return [
            f"Which steps in this {organ} workflow drive the most variability across lines or batches?",
            "What extra maturation or assay layer is usually needed after the baseline derivation works?",
        ]
    if bucket == "adult":
        return [
            "Which parts of the donor or disease context stay stable over long-term expansion?",
            "What missing non-epithelial compartments most limit interpretation in this platform?",
        ]
    if bucket == "functional":
        return [
            "How much of the observed phenotype comes from the added assay layer versus the baseline organoid state?",
            "What maturity or polarity checks should be mandatory before this assay is trusted?",
        ]
    if bucket == "engineering":
        return [
            "Which engineering or readout step is most likely to fail before the biology is interpretable?",
            "How should this workflow be standardized across cell lines, batches, or perturbation sets?",
        ]
    if bucket == "multi":
        return [
            "Which extra lineage or compartment materially changes the answer to the biological question?",
            "How much extra complexity is worth the loss in simplicity and throughput?",
        ]
    return [
        "Which phenotypes remain robust after moving into an in vivo host context?",
        "How should host-driven effects be separated from organoid-intrinsic effects?",
    ]


def source_page_text(row: dict, note: dict, scope: str) -> str:
    concept_lines = "\n".join(
        f"- [{CONCEPT_PAGES[slug]['title']}](../concepts/{slug}.md)" for slug in note["concepts"]
    )
    summary = "\n".join(f"- {line}" for line in summary_bullets(row, note, scope))
    findings = "\n".join(f"- {line}" for line in key_findings(row, note))
    strengths_text = "\n".join(f"- {line}" for line in strengths(note["bucket"]))
    limitations_text = "\n".join(f"- {line}" for line in limitations(note["bucket"]))
    relevance_text = "\n".join(f"- {line}" for line in relevance_lines(row, note))
    questions_text = "\n".join(f"- {line}" for line in open_questions(row, note))

    return (
        "---\n"
        f"title: {row['title']}\n"
        "kind: paper\n"
        "status: ingested\n"
        f"added: {row['added']}\n"
        f"raw_source: {row['local_path']}\n"
        f"article_url: {row['article_url']}\n"
        f"published_date: {row['published_date']}\n"
        f"organ: {row['organ']}\n"
        f"protocol_focus: {row['focus']}\n"
        f"deep_ingested: {TODAY}\n"
        "---\n\n"
        f"# {row['title']}\n\n"
        "## Source\n\n"
        f"- PDF: [{row['local_path']}](../../{row['local_path']})\n"
        f"- Article: [{row['article_url']}]({row['article_url']})\n"
        f"- Status: deep ingested on {TODAY}\n"
        f"- Organ focus: {readable_organ(row)}\n"
        f"- Protocol focus: {row['focus']}\n\n"
        "## Study design\n\n"
        f"- Starting material: {starting_material(row)}\n"
        f"- Protocol type: {protocol_type(note['bucket'])}\n"
        f"- Aim: {row['focus']}\n"
        f"- Core readouts: {core_readouts(row, note['bucket'])}\n\n"
        "## Summary\n\n"
        f"{summary}\n\n"
        "## Key findings\n\n"
        f"{findings}\n\n"
        "## Strengths\n\n"
        f"{strengths_text}\n\n"
        "## Limitations and caveats\n\n"
        f"{limitations_text}\n\n"
        "## Relevance to this corpus\n\n"
        f"{relevance_text}\n\n"
        "## Related concepts\n\n"
        f"{concept_lines}\n\n"
        "## Open questions\n\n"
        f"{questions_text}\n"
    )


def concept_page_text(slug: str, data: dict, rows_by_stem: dict) -> str:
    sources_text = "\n".join(
        f"- [{short_label(rows_by_stem[stem])}](../sources/{Path(rows_by_stem[stem]['source_page']).name})"
        for stem in data["sources"]
    )
    synthesis_text = "\n".join(f"- {line}" for line in data["synthesis"])
    tension_text = "\n".join(f"- {line}" for line in data["tension"])
    questions_text = "\n".join(f"- {line}" for line in data["questions"])
    return (
        f"# {data['title']}\n\n"
        "## Current position in this corpus\n\n"
        f"{data['position']}\n\n"
        "## Strong supporting sources\n\n"
        f"{sources_text}\n\n"
        "## Working synthesis\n\n"
        f"{synthesis_text}\n\n"
        "## Main tension\n\n"
        f"{tension_text}\n\n"
        "## Open questions\n\n"
        f"{questions_text}\n"
    )


def overview_text(rows: list[dict]) -> str:
    return (
        "# Overview\n\n"
        "This collection contains 29 deeply ingested organoid protocol papers spanning foundational hPSC differentiation, adult and patient-derived systems, multi-lineage developmental models, and second-wave assay or perturbation workflows.\n\n"
        "## What this collection is good for\n\n"
        "- finding baseline protocols for brain, gastrointestinal, kidney, heart, lung, skin, bone marrow, and gastric organoids\n"
        "- comparing self-organizing versus more directed patterning strategies\n"
        "- identifying when organoid work shifts from derivation into coculture, transplantation, imaging, or screening\n"
        "- choosing between developmental hPSC systems and adult or patient-derived organoid platforms\n\n"
        "## Major protocol families\n\n"
        "### Foundational derivation and regional patterning\n\n"
        "- McCracken 2011\n"
        "- Lancaster 2014\n"
        "- Xia 2014\n"
        "- Takasato 2016\n"
        "- Morizane 2016\n"
        "- Sloan 2018\n"
        "- Broda 2018\n"
        "- Miller 2019\n"
        "- Drakhlis 2021\n"
        "- Vanslambrouck 2023\n"
        "- Ullah 2025\n\n"
        "### Adult stem and patient-derived platforms\n\n"
        "- Drost 2016\n"
        "- Broutier 2016\n"
        "- Driehuis 2020\n"
        "- Hendriks 2020\n"
        "- Dekkers 2021\n\n"
        "### Functional extensions and validation layers\n\n"
        "- Cattaneo 2019\n"
        "- Puschhof 2021\n"
        "- Co 2021\n"
        "- Watanabe 2022\n"
        "- Kelley 2024\n"
        "- Meng 2025\n\n"
        "### Multi-lineage and complexity-oriented systems\n\n"
        "- Koike 2021\n"
        "- Lee 2022\n"
        "- Matkovic Leko 2023\n"
        "- Olijnik 2024\n"
        "- Fitzgerald 2024\n"
        "- Dardano 2025\n\n"
        "## Recommended first reading order\n\n"
        "1. McCracken 2011\n"
        "2. Lancaster 2014\n"
        "3. Takasato 2016\n"
        "4. Sloan 2018\n"
        "5. Drakhlis 2021\n"
        "6. Broutier 2016\n"
        "7. Puschhof 2021\n"
        "8. Fitzgerald 2024\n"
        "9. Kelley 2024\n"
        "10. Meng 2025\n\n"
        "This order works well because it starts with foundational derivation logic, then moves into region-specific brain control, adult-tissue alternatives, functional assay layers, and finally perturbation-ready organoid systems.\n\n"
        "## Best concept entry points\n\n"
        "- [Self-organization and directed patterning](concepts/self-organization-and-directed-patterning.md)\n"
        "- [Brain organoid patterning and assembloids](concepts/brain-organoid-patterning-and-assembloids.md)\n"
        "- [Gastrointestinal and endodermal organoid systems](concepts/gastrointestinal-and-endodermal-organoid-systems.md)\n"
        "- [Kidney organoid differentiation routes](concepts/kidney-organoid-differentiation-routes.md)\n"
        "- [Adult stem cell and patient-derived organoid platforms](concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)\n"
        "- [Organoid functional assays, transplantation, and coculture](concepts/organoid-functional-assays-transplantation-and-coculture.md)\n"
        "- [Organoid engineering, imaging, and screening](concepts/organoid-engineering-imaging-and-screening.md)\n"
    )


def synthesis_text(rows_by_stem: dict) -> str:
    def link(stem: str) -> str:
        row = rows_by_stem[stem]
        return f"- [{row['title']}](../sources/{Path(row['source_page']).name})"

    return (
        "---\n"
        "title: Organoid Protocol Starter Corpus\n"
        "status: active\n"
        f"created: {datetime.now().astimezone().isoformat(timespec='seconds')}\n"
        "---\n\n"
        "# Organoid Protocol Starter Corpus\n\n"
        "## Scope\n\n"
        "This corpus contains 29 deeply ingested organoid protocol papers spanning baseline organ generation, regional patterning, adult and patient-derived platforms, functional coculture or transplantation workflows, and newer engineering or screening layers.\n\n"
        "## Coverage Map\n\n"
        "### Foundational derivation and regional patterning\n\n"
        f"{link('mccracken_2011_generating_human_intestinal_tissue_from')}\n"
        f"{link('lancaster_2014_generation_of_cerebral_organoids_from')}\n"
        f"{link('xia_2014_the_generation_of_kidney_organoids')}\n"
        f"{link('takasato_2016_generation_of_kidney_organoids_from')}\n"
        f"{link('morizane_2016_generation_of_nephron_progenitor_cells')}\n"
        f"{link('sloan_2018_generation_and_assembly_of_human')}\n"
        f"{link('broda_2018_generation_of_human_antral_and')}\n"
        f"{link('miller_2019_generation_of_lung_organoids_from')}\n"
        f"{link('drakhlis_2021_generation_of_heart-forming_organoids_from')}\n"
        f"{link('vanslambrouck_2023_generation_of_proximal_tubule-enhanced_kidney')}\n"
        f"{link('ullah_2025_generating_and_characterizing_human_telencephalic')}\n\n"
        "### Adult stem and patient-derived organoid platforms\n\n"
        f"{link('drost_2016_organoid_culture_systems_for_prostate')}\n"
        f"{link('broutier_2016_culture_and_establishment_of_self-renewing')}\n"
        f"{link('driehuis_2020_establishment_of_patient-derived_cancer_organoids')}\n"
        f"{link('hendriks_2020_establishment_of_human_fetal_hepatocyte')}\n"
        f"{link('dekkers_2021_long-term_culture_genetic_manipulation_and')}\n\n"
        "### Functional assays, transplantation, and host interaction\n\n"
        f"{link('cattaneo_2019_tumor_organoid-t-cell_coculture_systems')}\n"
        f"{link('puschhof_2021_intestinal_organoid_cocultures_with_microbes')}\n"
        f"{link('co_2021_controlling_the_polarity_of_human')}\n"
        f"{link('watanabe_2022_transplantation_of_intestinal_organoids_into')}\n"
        f"{link('kelley_2024_host_circuit_engagement_of_human')}\n\n"
        "### Multi-lineage and complexity-oriented systems\n\n"
        f"{link('koike_2021_engineering_human_hepato-biliary-pancreatic_organoids_from')}\n"
        f"{link('lee_2022_generation_and_characterization_of_hair-bearing')}\n"
        f"{link('matkovicleko_2023_a_distal_lung_organoid_model')}\n"
        f"{link('olijnik_2024_generating_human_bone_marrow_organoids')}\n"
        f"{link('dardano_2025_production_of_human_blood-generating_heart-forming')}\n\n"
        "### Engineering, imaging, and screening layers\n\n"
        f"{link('fitzgerald_2024_generation_of_semi-guided_cortical_organoids')}\n"
        f"{link('meng_2025_crispr_screens_in_human_neural')}\n\n"
        "## Cross-paper Claims\n\n"
        "- Organoid work in this collection separates cleanly into baseline derivation papers and second-wave papers that add assay, transplantation, or perturbation layers.\n"
        "- The most persistent design tension is self-organization versus stronger directed patterning, especially in brain and kidney systems.\n"
        "- Adult and patient-derived organoids answer different questions from pluripotent developmental organoids; neither branch is a universal replacement for the other.\n"
        "- Recent protocol development is increasingly about maturation, host interaction, imaging quality, and screening compatibility rather than only making the tissue for the first time.\n"
        "- Multi-lineage and boundary models matter most when the target biology depends on neighboring tissues, appendages, or hematopoietic, vascular, or immune context.\n\n"
        "## Main Tensions\n\n"
        "- self-organization versus directed reproducibility\n"
        "- developmental breadth versus assay tractability\n"
        "- hPSC developmental models versus adult or patient-derived platforms\n"
        "- in vitro maturation versus transplantation or host-context validation\n"
        "- simpler single-lineage organoids versus more complex multicompartment systems\n\n"
        "## Concept Entry Points\n\n"
        "- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)\n"
        "- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)\n"
        "- [Gastrointestinal and endodermal organoid systems](../concepts/gastrointestinal-and-endodermal-organoid-systems.md)\n"
        "- [Kidney organoid differentiation routes](../concepts/kidney-organoid-differentiation-routes.md)\n"
        "- [Cardiac and hematoendothelial organoids](../concepts/cardiac-and-hematoendothelial-organoids.md)\n"
        "- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)\n"
        "- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)\n"
        "- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)\n\n"
        "## Questions To Drive Next Work\n\n"
        "- Which organ systems in this collection are best served by broad self-organization, and which require tighter patterning?\n"
        "- Which assay-layer papers are essential for translational work after a baseline protocol is established?\n"
        "- Where do adult or patient-derived platforms outperform hPSC differentiation for disease modeling and drug response?\n"
        "- Which organoid models in this corpus are mature enough for meaningful host interaction or transplantation studies?\n"
        "- Which protocols should be treated as baseline build steps and which should be treated as optional extensions?\n"
    )


def index_text(rows: list[dict]) -> str:
    source_lines = "\n".join(
        f"- [{row['title']}](sources/{Path(row['source_page']).name}) - deeply ingested protocol source."
        for row in rows
    )
    concept_lines = "\n".join(
        f"- [{data['title']}](concepts/{slug}.md) - working synthesis page."
        for slug, data in CONCEPT_PAGES.items()
    )
    synthesis_lines = "- [Organoid Protocol Starter Corpus](syntheses/20260408_organoid-protocol-corpus.md) - corpus-level synthesis."
    return (
        "# Index\n\n"
        "## Overview\n\n"
        "- [Overview](overview.md) - top-level summary of the current collection.\n\n"
        "## Sources\n\n"
        f"{source_lines}\n\n"
        "## Entities\n\n"
        "\n"
        "## Concepts\n\n"
        f"{concept_lines}\n\n"
        "## Queries\n\n"
        "\n"
        "## Syntheses\n\n"
        f"{synthesis_lines}\n"
    )


def append_log(log_path: Path, rows: list[dict]) -> None:
    marker = "deep ingest | Organoid protocol corpus"
    existing = log_path.read_text(encoding="utf-8")
    if marker in existing:
        return
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    titles = ", ".join(short_label(row) for row in rows[:8]) + ", ..."
    entry = (
        f"\n## [{timestamp}] {marker}\n\n"
        f"- Deep-ingested {len(rows)} organoid protocol source pages from raw PDFs.\n"
        f"- Added {len(CONCEPT_PAGES)} concept pages and one corpus synthesis page.\n"
        "- Refreshed overview, index, and cross-links for the organoid collection.\n"
        f"- Representative sources in this pass: {titles}\n"
    )
    log_path.write_text(existing.rstrip() + "\n" + entry, encoding="utf-8")


def configure_workspace(root: Path) -> dict:
    return {
        "root": root,
        "manifest": root / "organoid_protocols_manifest.tsv",
        "wiki": root / "wiki",
        "sources": root / "wiki" / "sources",
        "concepts": root / "wiki" / "concepts",
        "syntheses": root / "wiki" / "syntheses",
        "overview": root / "wiki" / "overview.md",
        "index": root / "wiki" / "index.md",
        "log": root / "wiki" / "log.md",
    }


def ensure_dirs(paths: dict) -> None:
    paths["sources"].mkdir(parents=True, exist_ok=True)
    paths["concepts"].mkdir(parents=True, exist_ok=True)
    paths["syntheses"].mkdir(parents=True, exist_ok=True)


def read_rows(manifest_path: Path) -> list[dict]:
    rows = list(csv.DictReader(manifest_path.open(encoding="utf-8"), delimiter="\t"))
    for row in rows:
        row["added"] = row.get("added") or datetime.now().astimezone().isoformat(timespec="seconds")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Deep ingest the organoid protocol corpus.")
    parser.add_argument("--collection", default="organoid")
    parser.add_argument("--workspace")
    args = parser.parse_args()

    workspace = resolve_workspace(
        collection=args.collection,
        workspace=args.workspace,
        default_collection="organoid",
    )
    paths = configure_workspace(workspace.root)
    ensure_dirs(paths)

    rows = read_rows(paths["manifest"])
    rows_by_stem = {protocol_stem(row): row for row in rows}

    for row in rows:
        stem = protocol_stem(row)
        if stem not in PAPER_NOTES:
            raise KeyError(f"Missing PAPER_NOTES entry for {stem}")
        note = PAPER_NOTES[stem]
        scope = extract_scope(workspace.root / row["local_path"])
        row["scope"] = scope
        target = workspace.root / row["source_page"]
        target.write_text(source_page_text(row, note, scope), encoding="utf-8")

    for slug, data in CONCEPT_PAGES.items():
        target = paths["concepts"] / f"{slug}.md"
        target.write_text(concept_page_text(slug, data, rows_by_stem), encoding="utf-8")

    synthesis_path = paths["syntheses"] / "20260408_organoid-protocol-corpus.md"
    synthesis_path.write_text(synthesis_text(rows_by_stem), encoding="utf-8")
    paths["overview"].write_text(overview_text(rows), encoding="utf-8")
    paths["index"].write_text(index_text(rows), encoding="utf-8")
    append_log(paths["log"], rows)

    print(f"Deep-ingested {len(rows)} organoid protocol sources")
    print(f"Wrote concept pages: {len(CONCEPT_PAGES)}")
    print(f"Wrote synthesis: {synthesis_path}")


if __name__ == "__main__":
    main()
