---
title: "Choosing the next assay or engineering layer after a baseline organoid works"
status: active
created: 2026-04-20T17:20:30+09:00
---

# baseline organoid가 만들어진 뒤 어떤 assay 또는 engineering layer를 먼저 붙여야 하나

## Question

기본 organoid derivation이 돌아간 뒤, 다음 단계로 어떤 assay 또는 engineering layer를 붙이는 게 가장 합리적인가?

## Short answer

이 corpus의 공통 메시지는 단순하다. **두 번째 레이어는 organoid를 더 “멋있게” 만드는 장치가 아니라, 질문을 더 직접적으로 만드는 장치**다.

- apical exposure가 막혀 있으면 polarity control 또는 microbial coculture
- immune interaction이 질문이면 immune coculture
- host validation이 필요하면 transplantation
- function readout이 핵심이면 electrophysiology-friendly neural workflow
- causal perturbation이 목표면 CRISPR/screening layer
- long-term expandable epithelial platform 위에서 gene editing이 핵심이면 adult/fetal tissue organoid engineering

## Gating rule before adding any second-wave layer

이 corpus의 여러 engineering/assay protocol은 공통으로 같은 경고를 준다.

- baseline organoid pipeline이 이미 **robust**해야 한다
- assay 결과는 baseline의 **maturity, polarity, reproducibility**에 크게 좌우된다
- 실패 원인이 biology가 아니라 **delivery, imaging, screen design, host logistics**일 수 있다

즉, 두 번째 레이어를 고르기 전에 “organoid를 만들 수 있는가”가 아니라 “이 baseline을 믿을 수 있는가”를 먼저 봐야 한다.

## Decision table

| 다음 질문 | 우선 붙일 레이어 | 이유 | 대표 페이지 |
|---|---|---|---|
| apical infection, barrier exposure, lumen access가 핵심인가 | polarity control / microbial exposure | inward-facing geometry를 assay-friendly하게 바꿔야 함 | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) |
| immune interaction 또는 tumor-reactive phenotype을 보고 싶은가 | immune coculture | organoid를 immune-engagement assay로 바꿈 | [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md) |
| repair, engraftment, host-context relevance가 핵심인가 | transplantation | dish-based claim을 host context에서 검증 | [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md), [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md) |
| neural function, oscillation, calcium imaging이 핵심인가 | electrophysiology-friendly brain workflow | derivation보다 readout compatibility가 중요해짐 | [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md) |
| pooled perturbation과 mechanism discovery가 목표인가 | CRISPR screening layer | organoid를 systematic perturbation platform으로 전환 | [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md) |
| stable editing을 donor-derived epithelial platform에 붙이고 싶은가 | adult/fetal tissue organoid engineering | expandable tissue organoid와 genetic manipulation을 결합 | [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md), [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md), [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md) |

## How to choose the first added layer

## 1. Add access before adding complexity

장벽은 종종 biology 자체가 아니라 **접근성**이다.

- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md): apical biology 접근을 위해 polarity를 뒤집는다
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md): lumenal microinjection과 microbial viability workflow를 붙인다

즉, 질문이 host-microbe, barrier, apical exposure라면 가장 먼저 붙여야 할 레이어는 대개 “더 많은 세포 타입”이 아니라 **올바른 접근 방식**이다.

## 2. Add biologically specific interaction when derivation alone is not the experiment

- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md): tumor organoid를 immune interaction assay로 바꾼다
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md): intestinal organoid를 repair assay로 바꾼다
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md): cortical organoid를 host circuit-engagement question으로 옮긴다

이 단계의 포인트는 organoid를 더 복잡하게 만드는 것이 아니라, **실험 질문을 organoid와 맞물리게 만드는 것**이다.

## 3. Add readout leverage when the organoid is already stable

- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md): oscillation, calcium imaging, MEA readout을 중심으로 설계
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md): pooled CRISPR screening system으로 확장
- [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md), [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md), [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md): organoid derivation과 editing/manipulation을 한 스택으로 묶는다

이 계열은 baseline reproducibility가 없으면 가장 먼저 무너질 가능성이 높다.

## Practical sequencing rule

1. **access bottleneck가 있으면** polarity or coculture workflow를 먼저 붙인다.
2. **host relevance가 병목이면** transplantation을 붙인다.
3. **mechanism discovery가 병목이면** editing or screening layer를 붙인다.
4. **function readout이 병목이면** electrophysiology-friendly or imaging-friendly workflow를 고른다.

## What this corpus suggests not to do

- baseline variability가 큰데 바로 pooled screen부터 붙이지 않는다.
- apical access가 없는 상태에서 host-microbe interpretation을 밀어붙이지 않는다.
- host validation이 필요한 질문인데 dish-only readout으로 결론을 확정하지 않는다.

## What this knowledge base does not settle

- 어떤 engineering layer가 “가장 범용적으로 최고”인지는 이 corpus가 답하지 못한다.
- 대신 이 corpus는 **가장 먼저 붙여야 하는 레이어는 질문에 가장 가까운 병목을 해결하는 것**이라는 점을 반복해서 보여준다.

## Sources used

- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md)
- [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md)
- [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)
