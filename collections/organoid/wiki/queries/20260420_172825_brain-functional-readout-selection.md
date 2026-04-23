---
title: "Choosing a brain organoid protocol by functional readout"
status: active
created: 2026-04-20T17:28:25+09:00
---

# brain organoid는 functional readout에 따라 어떻게 고르는 게 맞나

## Question

Brain organoid 프로젝트에서 readout이 다를 때, 어떤 프로토콜 또는 프로토콜 계열을 우선 고려해야 하나? 특히 composition reproducibility, fidelity, maturation timeline, oscillations, host integration, pooled perturbation 같은 readout별 선택 기준이 궁금하다.

## Short answer

이 corpus에서 brain organoid 선택은 “어느 region을 만들까”만의 문제가 아니다. **어떤 readout을 가장 먼저 믿고 싶은가**가 더 중요하다.

- **composition reproducibility**를 원하면 Velasco/Yoon 계열
- **primary tissue fidelity**를 보려면 Bhaduri/He 계열 관점
- **temporal mapping**이 중요하면 Kanton와 long-term maturation 계열
- **electrophysiology and oscillations**가 핵심이면 Fitzgerald
- **host-context validation**이 필요하면 Kelley
- **pooled perturbation or screening**이 목표면 Meng, 또는 screening-scale specific system으로 Chen

## Readout-first decision table

| 우선 readout | 먼저 볼 프로토콜/논문 | 이유 | 대표 페이지 |
|---|---|---|---|
| batch-to-batch composition reproducibility | directed cortical reproducibility branch | organoid 간 분산을 가장 직접적으로 다룸 | [Velasco 2019](../sources/velasco_2019_individual_brain_organoids_reproducibly.md), [Yoon 2019](../sources/yoon_2019_reliability_of_human_cortical.md) |
| fidelity to primary fetal brain | benchmark and atlas branch | organoid-to-primary distance를 직접 문제 삼음 | [Bhaduri 2020](../sources/bhaduri_2020_cell_stress_in_cortical.md), [He 2024](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md) |
| developmental timing and later-stage maturation | longitudinal maturation branch | day-to-stage mapping과 장기 배양 가치가 핵심 | [Kanton 2019](../sources/kanton_2019_organoid_single-cell_genomic_atlas.md), [Giandomenico 2021](../sources/giandomenico_2021_generation_and_long-term_culture_of.md) |
| oscillations, calcium imaging, MEA | semi-guided functional branch | readout compatibility 자체가 프로토콜 목표 | [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md) |
| host circuit engagement | transplantation branch | in vivo host integration을 직접 테스트 | [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md) |
| pooled CRISPR perturbation | perturbation-ready branch | organoid를 screening system으로 전환 | [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md) |
| screening-scale midbrain phenotype | miniaturized controlled branch | necrosis-limited, reproducible, throughput-friendly | [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md) |

## 1. If you care about reproducibility, start with Velasco and Yoon

- [Velasco 2019](../sources/velasco_2019_individual_brain_organoids_reproducibly.md): organoid-to-organoid cell type composition reproducibility를 가장 직접적으로 다룬다
- [Yoon 2019](../sources/yoon_2019_reliability_of_human_cortical.md): differentiation success rate와 stage-dominant variance를 보여준다

이 계열은 **같은 프로토콜을 여러 번 돌렸을 때 얼마나 안정적인가**를 먼저 묻는다.

## 2. If you care about fidelity, do not stop at reproducibility

- [Bhaduri 2020](../sources/bhaduri_2020_cell_stress_in_cortical.md): reproducibility와 primary-like fidelity가 다르다는 점을 가장 강하게 보여준다
- [He 2024](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md): 여러 프로토콜을 같은 atlas 좌표계에서 비교하는 데 유리하다

따라서 brain organoid가 “잘 반복된다”는 이유만으로 충분하지 않고, **무엇에 닮았는지**를 분리해서 봐야 한다.

## 3. If you care about developmental timing, use Kanton and long-term culture logic

- [Kanton 2019](../sources/kanton_2019_organoid_single-cell_genomic_atlas.md): cell state emergence timeline을 가장 잘 준다
- [Giandomenico 2021](../sources/giandomenico_2021_generation_and_long-term_culture_of.md): later-stage maturation 관심이 클 때 baseline 역할을 한다

즉, 질문이 “day X에 무엇이 나와야 하나”라면 Kanton-style temporal map이 먼저고, “더 늦은 stage까지 밀고 싶은가”라면 Giandomenico-style long-term branch가 중요하다.

## 4. If you care about neural function in the dish, use Fitzgerald

[Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)는 readout 자체가 oscillations, calcium imaging, MEA 쪽에 맞춰져 있다. 이 corpus에서 가장 중요한 포인트는 **functional readout compatibility가 derivation design의 일부**라는 점이다.

따라서 neural oscillation이나 network activity가 핵심 질문이라면, 단순히 region marker가 맞는 프로토콜보다 readout-ready workflow를 우선해야 한다.

## 5. If you need host-context relevance, use Kelley

[Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)는 dish-based maturation만으로는 답하기 어려운 질문을 host circuit integration으로 옮긴다. 이 branch는 strongest validation을 줄 수 있지만, 동시에 host environment가 phenotype에 섞여 들어온다.

## 6. If you need perturbation or screening leverage, use Meng or Chen

- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md): pooled CRISPR perturbation을 위한 neural organoid/assembloid branch
- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md): midbrain-specific이지만 controlled, miniaturized, screening-friendly

즉, broad mechanistic screening이면 Meng 쪽, **specific controlled midbrain screening**이면 Chen 쪽이 더 맞는다.

## A practical readout-first rule

1. 먼저 **region**이 아니라 **가장 중요한 readout**을 적는다.
2. 그 다음 readout을 가장 직접적으로 최적화한 branch를 고른다.
3. reproducibility와 fidelity는 따로 평가한다.
4. dish readout으로 충분한지, host-context validation이 필요한지 일찍 결정한다.

## What this corpus suggests avoiding

- reproducibility paper로 fidelity를 대신 판단하는 것
- atlas mapping만으로 oscillation readiness를 추정하는 것
- transplantation question을 dish-only protocol로 마무리하는 것
- screening question인데 giant heterogeneous organoid를 baseline으로 삼는 것

## What this knowledge base does not settle

- 하나의 brain protocol이 모든 readout에서 최고라는 결론은 지원되지 않는다.
- midbrain, hindbrain, cerebellum 등 posterior brain branch에 대해 Velasco- or Bhaduri-equivalent benchmark depth는 아직 부족하다.

## Related entities

- [Calcium imaging readouts](../entities/calcium-imaging-readouts.md)
- [MEA electrophysiology readouts](../entities/mea-electrophysiology-readouts.md)
- [Host circuit engagement](../entities/host-circuit-engagement.md)

## Sources used

- [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Velasco 2019](../sources/velasco_2019_individual_brain_organoids_reproducibly.md)
- [Yoon 2019](../sources/yoon_2019_reliability_of_human_cortical.md)
- [Bhaduri 2020](../sources/bhaduri_2020_cell_stress_in_cortical.md)
- [Kanton 2019](../sources/kanton_2019_organoid_single-cell_genomic_atlas.md)
- [He 2024](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
- [Giandomenico 2021](../sources/giandomenico_2021_generation_and_long-term_culture_of.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)
