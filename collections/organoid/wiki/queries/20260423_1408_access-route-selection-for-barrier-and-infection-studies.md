---
title: "Choosing among polarity inversion, organ-on-chip, BBB spheroids, and microinjection for barrier or infection studies"
status: active
created: 2026-04-23T14:08:00+09:00
---

# barrier 또는 infection study에서 polarity inversion, organ-on-chip, BBB spheroids, microinjection 중 무엇을 골라야 하나

## Question

Barrier biology나 infection assay를 설계할 때 비슷해 보이는 선택지가 많다. closed organoid를 polarity inversion으로 열 수도 있고, organ-on-chip으로 옮길 수도 있고, 그냥 microinjection으로 안쪽에 넣을 수도 있으며, 아예 BBB spheroid 같은 barrier-specific system을 고를 수도 있다. 이 corpus 기준으로 이 네 가지는 언제 각각 우선 선택하는 것이 맞나?

## Short answer

이 corpus는 네 선택지를 같은 종류의 기술로 보지 않는다. 핵심은 "무엇을 넣을까"보다 **무엇을 접근 가능하게 만들고 싶은가**다.

- **polarity inversion**
  - 이미 괜찮은 epithelial organoid가 있고, apical surface만 열면 되는 경우
- **standard microinjection**
  - 3D 구조를 유지한 채 닫힌 lumen이나 내부 구획에 정의된 cargo를 넣어야 하는 경우
- **organ-on-chip**
  - apical/basal access를 반복해서 쓰고, sampling, permeability, secretion, flow, exposure geometry를 모두 제어해야 하는 경우
- **BBB spheroids**
  - 질문이 generic infection이 아니라 **barrier penetration or exclusion** 자체인 경우

즉 이 corpus의 rule은 이렇다. **surface access면 polarity inversion, internal targeting이면 microinjection, repeated compartment control이면 organ-on-chip, barrier triage면 BBB spheroids**다.

## Decision table

| dominant question | best first choice in this corpus | why | main anchors |
|---|---|---|---|
| apical host-microbe exposure만 열면 되는가 | polarity inversion | geometry correction이 핵심이고 baseline epithelial system은 유지 가능 | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md) |
| closed lumen 안에 microbe, virus, tracer, or reagent를 직접 넣어야 하는가 | standard microinjection | 3D architecture를 유지한 채 defined delivery를 해야 함 | [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md), [M 2025](../sources/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.md) |
| apical/basal 분리, 반복 sampling, permeability, barrier readout, or flow까지 필요한가 | organ-on-chip | closed organoid보다 compartment control이 훨씬 크고 반복 측정이 쉬움 | [IV 2024](../sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md) |
| compound가 barrier를 통과하는지 자체가 질문인가 | BBB spheroids | developmental neural organoid가 아니라 barrier triage 모델이 더 direct함 | [Bergmann 2018](../sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.md) |

## 1. Use polarity inversion when geometry is the only real bottleneck

[Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)는 closed gastrointestinal organoid의 inward-facing geometry가 assay를 막는다고 본다. 이 경우 필요한 것은 새로운 multicellular platform이 아니라 **surface orientation correction**이다.

이 branch는 다음 같은 경우에 가장 적합하다.

- apical infection or ligand exposure가 핵심
- baseline epithelial identity는 이미 충분함
- device burden 없이 빠르게 assay route를 바꾸고 싶음
- repeated compartment sampling보다는 "surface를 연다"가 우선임

따라서 polarity inversion은 가장 가벼운 access fix다. 하지만 그만큼 할 수 있는 일도 명확히 제한된다. apical과 basal side를 장기간 분리 유지하거나, flow를 걸거나, barrier permeability를 체계적으로 재측정하는 데는 덜 유리하다.

## 2. Use standard microinjection when the system must stay closed but the cargo must enter

[Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)는 intestinal lumen 안으로 microbial cargo를 넣는 route를 보여주고, [M 2025](../sources/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.md)는 midbrain organoid 내부 ventricular-zone-like region으로 targeted viral delivery를 수행한다.

이 branch의 공통점은 이렇다.

- 3D tissue architecture를 유지하고 싶다
- 표면 전체 exposure가 아니라 **위치가 있는 delivery**가 필요하다
- bulk exposure나 polarity inversion으로는 질문이 풀리지 않는다

즉 microinjection은 access route라기보다 **defined internal delivery**다. 장점은 공간 선택성이지만, 단점도 분명하다.

- throughput이 낮다
- operator skill에 민감하다
- injection site bias가 생긴다
- 반복 sampling이나 continuous compartment separation에는 약하다

그래서 microinjection은 "닫힌 구조를 유지한 채 정확히 넣어야 할 때" 쓰는 것이지, generic barrier assay의 default는 아니다.

## 3. Use organ-on-chip when access must become a durable assay architecture

[IV 2024](../sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md)는 adult intestinal organoid를 membrane-free microfluidic epithelial barrier로 전환한다. 이 시스템의 핵심은 단순히 surface가 열린다는 점이 아니라, **apical and basal compartment가 실험적으로 분리된 채 유지된다**는 점이다.

이 branch는 다음에 맞다.

- barrier integrity를 반복적으로 봐야 한다
- apical/basal sampling이 모두 필요하다
- cytokine, toxin, metabolite, microbe exposure를 compartment-specific하게 운영해야 한다
- chip-to-chip QC와 device prep burden을 감수할 가치가 있다

따라서 organ-on-chip은 access correction보다 한 단계 큰 move다. geometry를 여는 것에 더해 **assay infrastructure 자체를 바꾼다**.

이 corpus에서 [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)도 같은 device logic의 다른 버전을 보여준다. 거기서는 question이 gut barrier가 아니라 kidney perfusion and maturation이지만, 공통점은 "기존 organoid가 못 주는 compartmental or mechanical control을 chip이 준다"는 점이다.

## 4. Use BBB spheroids when the model should be barrier-first, not organoid-first

[Bergmann 2018](../sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.md)는 brain organoid처럼 보이지만 실제 질문은 neural development가 아니라 **compound penetration across a barrier**다. 이 점이 중요하다.

이 branch는 다음에 맞다.

- question이 infection susceptibility generality가 아니라 penetration/exclusion triage다
- endothelial, pericyte, astrocyte direct-contact barrier가 핵심이다
- throughput과 barrier selectivity가 중요하다
- flowless spheroid여도 screening triage에는 충분하다

이 corpus에서 BBB spheroids는 organ-on-chip과 비슷한 면도 있지만 완전히 대체재는 아니다. chip은 compartment control과 flow 쪽으로 강하고, BBB spheroids는 **barrier-selective tri-cell assembly and compound triage** 쪽으로 더 direct하다.

## 5. A practical selection order

이 corpus 기준 실전 순서는 다음이 가장 안정적이다.

1. **surface만 열면 되는가**
   그러면 polarity inversion부터 본다.
2. **닫힌 구조 안에 정확히 넣어야 하는가**
   그러면 microinjection을 본다.
3. **compartment separation을 assay 구조로 유지해야 하는가**
   그러면 organ-on-chip으로 간다.
4. **질문이 tissue infection이 아니라 barrier penetration 자체인가**
   그러면 BBB spheroids를 우선 본다.

중요한 보정도 하나 있다. organ-on-chip과 BBB spheroids는 둘 다 "better barrier model"처럼 보일 수 있지만, 이 corpus에서는 목적이 다르다.

- **organ-on-chip**: exposed epithelium or perfused tissue를 operationalize
- **BBB spheroids**: selective barrier penetration을 triage

## 6. What this corpus suggests avoiding

- apical access 문제를 곧바로 multicellular complexity 문제로 오인하는 것
- repeated permeability or secretion assay가 필요한데 단발성 microinjection으로 버티는 것
- barrier penetration question인데 generic developmental brain organoid를 먼저 고르는 것
- chip prep burden이 과한데 사실 polarity inversion만으로 답이 나는 질문에 device를 먼저 도입하는 것
- 정확한 internal targeting이 필요한데 bulk exposure나 coarse access correction으로 대신하려는 것

## Rule of thumb

- **surface access**: polarity inversion
- **internal cargo placement**: microinjection
- **durable compartment control**: organ-on-chip
- **barrier triage itself**: BBB spheroids

## What this knowledge base does not settle

- 같은 cargo를 네 route에서 head-to-head로 직접 비교한 benchmark는 없다.
- BBB-on-chip과 BBB spheroids의 formal comparison은 이 corpus에 충분하지 않다.
- infection assay와 drug-permeability assay를 동시에 최적화하는 single best platform도 지원되지 않는다.

## Related entities

- [Organ-on-chip](../entities/organ-on-chip.md)

## Sources used

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Gastrointestinal and endodermal organoid systems](../concepts/gastrointestinal-and-endodermal-organoid-systems.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [IV 2024](../sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md)
- [Bergmann 2018](../sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.md)
- [M 2025](../sources/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.md)
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
