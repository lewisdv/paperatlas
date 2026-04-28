---
title: "flow, TF-driven vascularization, mesodermal mixing, stand-alone vessel addition, host transplantation은 organ과 질문에 따라 어떻게 골라야 하나"
status: active
created: 2026-04-23T16:26:26+09:00
---

# flow, TF-driven vascularization, mesodermal mixing, stand-alone vessel addition, host transplantation은 organ과 질문에 따라 어떻게 골라야 하나

## Question

`vascularization`이라고 묶어 부르기 쉽지만, 이 corpus에는 실제로는 서로 다른 다섯 갈래가 있다. flow-based perfusion, TF-driven vascularization, mesodermal progenitor mixing, stand-alone vascular organoid, host transplantation이 그것이다. 이 다섯 갈래는 organ과 질문에 따라 어떻게 골라야 하나?

## Short answer

이 corpus에서는 vascularization route를 하나의 연속선으로 보면 안 된다. 가장 실용적인 규칙은 **organ-specific bottleneck과 final claim**을 먼저 정하는 것이다.

- **kidney maturation이 목적**이면 `flow/perfusion`
- **brain organoid 안에서 hypoxia를 줄이며 in-dish vascular-like network를 만들고 싶으면** `TF-driven vascularization`
- **범용 vascular module이나 vessel-only baseline이 필요하면** `stand-alone vascular organoid`
- **여러 organoid context에 재사용 가능한 multicompartment addition이 필요하면** `mesodermal mixing`
- **repair, host integration, or full in vivo validation이 목적이면** `host transplantation`

즉 route choice는 "더 강한 혈관화"를 고르는 문제가 아니라, **어떤 missing layer를 어디까지 복구하려는가**를 고르는 문제다.

## Practical route table

| route | 가장 잘 맞는 질문 | organ fit in this corpus | 장점 | 주의점 | 대표 anchor |
|---|---|---|---|---|---|
| Flow / perfusion | endogenous vascular maturation과 tissue polarity를 밀어줄 수 있는가 | kidney | organ-specific maturation과 perfusable architecture를 동시에 밀어준다 | device와 ECM adoption cost가 높다 | [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md) |
| TF-driven vascularization | host 없이 integrated vascular-like network를 심을 수 있는가 | brain | cortical identity를 크게 흐리지 않으면서 hypoxia와 apoptosis를 줄인다 | genetic engineering 의존성이 크다 | [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md) |
| Mesodermal progenitor mixing | reusable multicompartment vascular addition이 필요한가 | neural, tumor, mixed systems | vasculature와 mural support, 때로는 microglia-like cells까지 같이 넣을 수 있다 | downstream specification control이 거칠 수 있다 | [Worsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) |
| Stand-alone vessel organoid | vessel baseline 자체를 만들고 싶은가 | vascular branch, modular add-on planning | vessel-only system 정의가 가장 선명하다 | organ-specific vasculature는 아니다 | [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md), [L 2026](../sources/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.md) |
| Host transplantation | in vivo repair, circulation integration, or host-context validation이 필요한가 | intestine, vascular, brain follow-up | 가장 강한 integration or repair validation을 준다 | host가 phenotype의 일부가 되어 attribution이 어려워진다 | [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md), [Wimmer 2019](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md) |

## 1. Kidney: choose flow when the bottleneck is maturation inside the dish

[Flow-enhanced vascularization and maturation of kidney organoids in vitro](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)는 kidney branch에서 가장 명확한 rule을 준다. 여기서 문제는 단순히 endothelial cell이 없다는 것이 아니라, **static culture가 organoid maturation을 가로막는다는 것**이다.

- high fluidic shear stress에서 PECAM1-positive vessel area가 크게 늘어난다
- endogenous endothelial progenitor pool이 커진다
- podocyte와 tubule polarity가 개선된다
- more adult-like expression이 나타난다

즉 kidney에서는 vascularization route가 `vessel addition`보다 `flow as a maturation variable`에 가깝다. 이 corpus 기준으로 kidney question이 **avascular immaturity**라면 Homan-type route가 가장 먼저 떠야 한다.

## 2. Brain: choose TF-driven vascularization when you need integrated in-dish rescue

[Engineering of human brain organoids with a functional vascular-like system](../sources/cakir_2019_engineering_of_human_brain.md)은 brain branch의 병목을 정확히 찌른다.

- large cortical organoid의 hypoxic core
- apoptosis accumulation
- vascular-like support absence

여기서 Cakir 2019는 ETV2-induced endothelial program을 organoid 안에 직접 심는다. 중요한 건 이 route가 단순히 vessel marker를 붙이는 게 아니라:

- CD31-positive tubular network
- 일부 perfusable lumen
- hypoxia and apoptosis reduction
- BBB-like features

까지 간다는 점이다.

따라서 brain에서는 `TF-driven vascularization`이 다음 질문에 잘 맞는다.

- host 없이 cortical organoid 내부에서 integrated vascular support를 만들 수 있는가
- hypoxic stress를 줄이면서 neural architecture를 유지할 수 있는가

## 3. Multi-lineage or reusable modules: choose mesodermal mixing

[Generation of complex human organoid models including vascular networks by incorporation of mesodermal progenitor cells](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)는 organ-specific tuning보다 **modular add-on logic**를 보여준다.

- Brachyury-positive MPCs를 만든다
- neural or tumor organoid context에 섞는다
- vasculature와 mural cells를 함께 들여온다
- neural branch에서는 microglia-like cells까지 같이 들어온다

이 route는 특히 이런 질문에 맞는다.

- 여러 organoid context에 재사용 가능한 vascular module이 필요한가
- vascular addition이 single-lineage endothelial add-on보다 더 풍부해야 하는가
- multicompartment complexity 자체가 readout의 일부인가

즉 Worsdorfer-type route는 `organ-specific perfection`보다는 **breadth and modularity** 쪽에 강하다.

## 4. Stand-alone vessel organoids are best when the vessel branch itself is the experiment

[Generation of blood vessel organoids from human pluripotent stem cells](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)와 [Protocol for generating human vascular organoids via orthogonal activation of ETV2 and NKX3.1.](../sources/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.md)는 둘 다 stand-alone vessel branch를 대표하지만, 성격은 다르다.

### Wimmer 2019

- self-organization-first
- endothelial plus pericyte microvascular baseline
- transplantation 후 circulation integration까지 간다

### L 2026

- orthogonal TF programming
- endothelial and mural lineage를 빠르게 강제한다
- speed와 reproducibility를 강하게 민다

따라서 stand-alone vessel route 안에서도 다시 갈라진다.

- **developmental self-organization과 classic vessel baseline이 중요하면** Wimmer
- **빠른 build와 programmable reproducibility가 중요하면** L 2026

이 두 paper는 모두 `organ-specific host organoid를 vascularize한다`기보다, **vascular branch 자체를 definition-level로 잡는 baseline**에 가깝다.

## 5. Choose host transplantation when the claim is no longer purely in vitro

[Transplantation of intestinal organoids into a mouse model of colitis](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)와 Wimmer 2019의 host circulation integration은 같은 메시지를 준다. transplantation은 vascularization route의 "강한 버전"이 아니라, **validation question을 바꾸는 route**다.

- intestine에서는 repair in injured tissue가 claim이 된다
- vascular organoid에서는 circulation integration이 claim이 된다

따라서 transplantation은 다음 상황에서 가장 맞다.

- in vivo repair 여부가 중요하다
- host circulation integration이 readout이다
- dish 안에서 얻은 vascular improvement를 최종 functional context에서 확인해야 한다

반대로 in vitro mechanistic optimization이 아직 끝나지 않았다면 transplantation은 너무 이르다.

## Organ-specific rule of thumb

- **kidney**
  - choose `flow/perfusion`
  - because maturation bottleneck is mechanical and endogenous
- **brain**
  - choose `TF-driven vascularization`
  - because integrated in-dish vascular support and hypoxia rescue matter most
- **tumor or neural multicompartment build**
  - choose `mesodermal mixing`
  - because reusable vascular plus support-cell addition is the main advantage
- **vascular organoid branch itself**
  - choose `stand-alone vessel organoid`
  - because the vessel system is the baseline, not an add-on
- **repair or integration claim**
  - choose `host transplantation`
  - because the endpoint only exists in host context

## A simple decision ladder

1. Is the main problem **organ-specific maturation inside the dish**?
   - choose flow/perfusion
2. Is the main problem **integrated vascular support without leaving the dish**?
   - choose TF-driven vascularization
3. Is the main problem **building a reusable multicompartment module**?
   - choose mesodermal mixing
4. Is the main problem **defining the vascular system itself**?
   - choose stand-alone vessel organoids
5. Is the main problem **repair, circulation integration, or host validation**?
   - choose transplantation

## What this corpus suggests avoiding

- kidney immaturity question을 vessel marker addition만으로 해결하려는 것
- brain hypoxia problem을 host transplantation까지 바로 올려서 in-dish engineering options을 건너뛰는 것
- stand-alone vessel organoid를 organ-specific vasculature와 같은 것으로 취급하는 것
- modular multicompartment question인데 organ-specific optimized route만 찾으려는 것
- host-only endpoint가 아닌데 too early transplantation으로 넘어가는 것

## What this knowledge base does not settle

- 같은 organ에서 이 다섯 route를 head-to-head로 비교한 benchmark는 없다
- adoption cost, throughput, and long-term maturity를 한 점수로 묶은 공통 표준도 없다
- lung, liver, pancreas 같은 organ에서 route choice가 kidney or brain만큼 선명하게 정리된 자료는 아직 적다

## Related entities

- [Organ-on-chip](../entities/organ-on-chip.md)
- [Stand-alone vascular organoids](../entities/stand-alone-vascular-organoids.md)
- [ETV2-driven vascular induction](../entities/etv2-driven-vascular-induction.md)
- [Mesodermal progenitor cell mixing](../entities/mesodermal-progenitor-cell-mixing.md)

## Sources used

- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [When to choose vascularization, perfusion, or transplantation](20260420_172029_vascularization-perfusion-vs-transplantation.md)
- [Flow-enhanced vascularization and maturation of kidney organoids in vitro](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- [Engineering of human brain organoids with a functional vascular-like system](../sources/cakir_2019_engineering_of_human_brain.md)
- [Generation of complex human organoid models including vascular networks by incorporation of mesodermal progenitor cells](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)
- [Generation of blood vessel organoids from human pluripotent stem cells](../sources/wimmer_2019_generation_of_blood_vessel_organoids.md)
- [Protocol for generating human vascular organoids via orthogonal activation of ETV2 and NKX3.1.](../sources/l_2026_protocol-for-generating-human-vascular-organoids-via-orthogonal-activation-of-etv2-and-nkx.md)
- [Transplantation of intestinal organoids into a mouse model of colitis](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
