---
title: "pancreas, intestine, BBB, lung에서는 screening stack를 어떻게 다르게 짜야 하나"
status: active
created: 2026-04-23T16:20:07+09:00
---

# pancreas, intestine, BBB, lung에서는 screening stack를 어떻게 다르게 짜야 하나

## Question

`screening-ready organoid stack`라는 말은 organ 공통 규칙처럼 들리지만, 실제로는 pancreas, intestine, BBB, lung에서 screening의 첫 병목이 꽤 다르게 보인다. 이 corpus 기준으로 이 네 시스템은 baseline, assay layer, hit definition, escalation 순서를 어떻게 다르게 짜는 게 맞나?

## Short answer

이 corpus에서는 네 organ system이 같은 screening stack를 공유하지 않는다. 가장 실용적인 차이는 **무엇이 첫 병목인가**에 있다.

- **pancreas**
  - first bottleneck: maturation credibility
  - rule: scalable baseline 뒤에 secretion benchmark를 먼저 붙인다
- **intestine**
  - first bottleneck: access and compartment control
  - rule: baseline 뒤에 polarity, exposure route, chip or coculture layer를 먼저 붙인다
- **BBB**
  - first bottleneck: barrier assay 자체의 interpretability
  - rule: developmental organoid보다 tri-cell barrier organoid와 penetration readout을 먼저 고른다
- **lung**
  - first bottleneck: baseline complexity choice
  - rule: disease or infection question을 버티는 distal lung baseline을 먼저 세운 뒤 assay를 붙인다

즉 이 corpus에서는 screening stack를 `baseline -> assay -> perturbation`의 고정 순서로 읽기보다, **organ별로 어떤 failure mode가 먼저 오는지**에 맞춰 바꿔야 한다.

## Organ-by-organ stack table

| organ | first bottleneck | baseline choice | first assay layer | believable hit definition | later escalation |
|---|---|---|---|---|---|
| Pancreas | maturity | [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md) | [Balboa 2022](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)-style GSIS and maturity benchmarking | secretion competence, insulin content, granules, cytoarchitecture | only after secretion-linked maturity is believable |
| Intestine | access | adult or organoid-derived intestinal baseline | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md), [IV 2024](../sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md) | apical exposure, permeability, microbial response, side-specific sampling | repair or host validation if claim leaves dish-access questions |
| BBB | assay-ready barrier function | [Bergmann 2018](../sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.md) tri-cell BBB spheroids | confocal or MALDI-based penetration readout | selective compound entry or exclusion | chip or in vivo pharmacokinetic escalation only if triage is insufficient |
| Lung | baseline complexity | [Matkovic Leko 2023](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md) distal lung organoid | infection, disease, or development readout layered later | depends on whether the question is developmental, ILD-like, or infection-facing | richer assay stack still underdeveloped in this corpus |

## 1. Pancreas: the stack is maturity-first

Pancreatic screening stack는 이 corpus에서 가장 분명하다. [Generation of insulin-producing pancreatic β cells from multiple human stem cell lines](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)가 **생산 가능한 baseline**을 주고, [Functional, metabolic and transcriptional maturation of human pancreatic islets derived from stem cells](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)가 **믿을 수 있는 function benchmark**를 준다.

핵심 순서는 이렇다.

1. reproducible SC-beta baseline을 만든다
2. GSIS, insulin content, dense-core granules, cytoarchitecture를 본다
3. secretion-linked maturity가 성립한 뒤에야 screening으로 넘어간다

여기서 중요한 점은 pancreas screening에서 첫 질문이 `access`도 `complexity`도 아니라는 것이다. **marker-positive beta identity가 아니라 secretion competence가 있는가**가 첫 gate다.

따라서 pancreas stack는 다음처럼 읽는 편이 맞다.

- baseline simplification
- functional maturation benchmark
- then perturbation or screen

## 2. Intestine: the stack is access-first

Intestinal screening stack에서는 baseline culture만으로는 실험 질문이 잘 열리지 않는다. [Controlling the polarity of human gastrointestinal organoids to investigate epithelial biology and infectious diseases](../sources/co_2021_controlling_the_polarity_of_human.md), [Intestinal organoid cocultures with microbes](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md), [Protocol for generating and analyzing organ-on-chip using human and mouse intestinal organoids.](../sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md)이 함께 보여주는 건 **access correction이 assay 그 자체**라는 점이다.

이 stack의 기본 순서는 이렇다.

1. baseline intestinal organoid를 확보한다
2. apical access를 열거나, luminal delivery를 설계하거나, chip으로 side-specific access를 만든다
3. 그 다음 microbial exposure, permeability, cytokine, secretion, coculture를 읽는다

즉 intestine에서는 screening 실패가 대개 biology 부족보다 **geometry and compartment 문제**에서 먼저 온다.

그래서 practical rule도 다르다.

- quick infection or epithelial exposure면 polarity inversion
- lumenal cargo placement면 microinjection or microbial coculture
- apical and basal sampling을 오래 유지해야 하면 organ-on-chip

## 3. BBB: the stack is barrier-readout-first

BBB는 이 corpus에서 brain organoid branch와 달리 developmental fidelity 경쟁이 아니라 **barrier triage**로 읽는 편이 맞다. [Blood–brain-barrier organoids for investigating the permeability of CNS therapeutics](../sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.md)는 처음부터 endothelial, pericyte, astrocyte direct-contact spheroid와 penetration assay를 한 세트로 제시한다.

이 branch의 screening stack는 다음처럼 압축된다.

1. tri-cell BBB spheroid baseline을 만든다
2. tight-junction and transporter logic가 있는지 본다
3. confocal or MALDI-based penetration readout으로 selective entry를 본다

여기서 hit definition은 neuronal phenotype이 아니라 **compound penetration or exclusion**이다. 그래서 BBB branch는 organoid screening에서 보기 드물게 baseline과 readout이 거의 동시에 설계된다.

이 corpus에서는 BBB screening이 다음을 우선한다.

- speed
- selective permeability triage
- direct quantitative readout

반대로 full neurovascular realism, flow, immune traffic는 later escalation 질문으로 남는다.

## 4. Lung: the stack is baseline-complexity-first

Lung는 이 corpus에서 pancreas나 intestine처럼 assay logic가 아주 촘촘히 정리된 branch는 아니다. 대신 [A distal lung organoid model to study interstitial lung disease, viral infection and human lung development](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md)가 보여주듯이, 먼저 **어떤 lung baseline이 질문을 버틸 수 있느냐**가 핵심이다.

이 source는 distal lung organoid를 developmental, ILD, infection three-way baseline으로 둔다. 그래서 lung stack는 다음처럼 보인다.

1. distal lung baseline을 고른다
2. disease, infection, development 중 어떤 framing인지 정한다
3. 그다음에 필요한 assay layer를 붙인다

즉 lung에서는 현재 corpus 기준으로 `first assay`보다 `right baseline complexity`가 더 중요하다. 이건 강점이자 한계다.

- 강점: wrong tissue simplification을 피할 수 있다
- 한계: screening operation을 바로 설계할 만큼 assay-layer comparator가 pancreas/intestine/BBB만큼 풍부하진 않다

따라서 lung screening stack는 아직 이 corpus에서 **baseline-rich, assay-thin** branch에 가깝다.

## Cross-organ rule

이 네 organ을 같이 보면 같은 `screening-ready`라는 말도 실제 의미가 다르다.

- **pancreas**
  - screening-ready = functionally mature
- **intestine**
  - screening-ready = experimentally accessible
- **BBB**
  - screening-ready = barrier readout이 바로 operational
- **lung**
  - screening-ready = question을 버틸 baseline이 먼저 정해진 상태

그래서 organ-specific screening stack를 짤 때는 먼저 이렇게 묻는 편이 낫다.

1. 이 organ의 첫 병목은 maturity인가, access인가, assay-readout인가, baseline complexity인가
2. 그 병목을 넘기는 가장 싼 첫 레이어가 무엇인가
3. hit definition을 언제부터 믿을 수 있는가

## Practical rule

- pancreas는 **maturity benchmark before screening**
- intestine는 **access layer before screening**
- BBB는 **barrier assay with direct penetration readout**
- lung는 **baseline selection before assay inflation**

## What this corpus suggests avoiding

- pancreas에서 marker-positive stage를 바로 screening-ready라고 부르는 것
- intestine에서 polarity or compartment 문제를 해결하지 않고 response assay를 먼저 올리는 것
- BBB에서 neuronal richness를 이유로 barrier-triage branch를 흐리는 것
- lung에서 baseline question을 정리하기 전에 screening infrastructure부터 과하게 붙이는 것

## What this knowledge base does not settle

- lung branch의 screening readout stack는 pancreas, intestine, BBB만큼 풍부하지 않다
- same-perturbation을 네 organ에서 직접 head-to-head 비교한 benchmark는 없다
- throughput, cost, and turnaround의 공통 numerical comparison도 없다

## Related entities

- [Organ-on-chip](../entities/organ-on-chip.md)

## Sources used

- [Designing a screening-ready organoid protocol stack](20260420_173504_screening-ready-protocol-stack-design.md)
- [Choosing functional validation for non-brain organoids](20260420_173505_non-brain-functional-validation-selection.md)
- [barrier 또는 infection study에서 polarity inversion, organ-on-chip, BBB spheroids, microinjection 중 무엇을 골라야 하나](20260423_1408_access-route-selection-for-barrier-and-infection-studies.md)
- [Generation of insulin-producing pancreatic β cells from multiple human stem cell lines](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)
- [Functional, metabolic and transcriptional maturation of human pancreatic islets derived from stem cells](../sources/balboa_2022_functional_metabolic_and_transcriptional.md)
- [Controlling the polarity of human gastrointestinal organoids to investigate epithelial biology and infectious diseases](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Intestinal organoid cocultures with microbes](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Protocol for generating and analyzing organ-on-chip using human and mouse intestinal organoids.](../sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md)
- [Blood–brain-barrier organoids for investigating the permeability of CNS therapeutics](../sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.md)
- [A distal lung organoid model to study interstitial lung disease, viral infection and human lung development](../sources/matkovicleko_2023_a_distal_lung_organoid_model.md)
