---
title: "Triaging organoid assay failures before changing the whole model"
status: active
created: 2026-04-20T19:04:11+09:00
---

# Organoid assay가 실패할 때 무엇부터 의심해야 하나

## Question

Organoid assay를 붙였는데 signal이 약하거나, batch마다 흔들리거나, biological interpretation이 안 설 때가 많다. 이 corpus 기준으로 이런 실패는 어떤 순서로 triage하는 것이 맞나?

## Short answer

이 corpus는 assay failure를 크게 여섯 가지로 나눌 수 있다고 말한다.

1. **access or geometry mismatch**
2. **baseline organoid instability**
3. **missing biological partner**
4. **diffusion or maturation ceiling**
5. **engineering or readout bottleneck**
6. **host-context attribution failure**

중요한 점은 많은 실패가 "organoid biology가 틀렸다"기보다 **질문과 assay layer가 어긋난 것**이라는 점이다.

## Failure-mode table

| symptom | first suspicion | what to check next | anchor pages |
|---|---|---|---|
| no interpretable exposure phenotype | access or polarity problem | apical/basal orientation, exposure route, microinjection feasibility | [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) |
| noisy batches, drifting size, inconsistent composition | unstable baseline derivation | scale control, necrotic core, line dependence, protocol simplification | [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md), [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md) |
| clean baseline but no biology in coculture | missing interaction partner | effector cell, microbe, stromal support, direct-contact logic | [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md), [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md) |
| central stress, poor maturation, weak functional gain | tissue-support bottleneck | vascular-like support, flow, perfusion, tissue size | [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md), [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md), [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md) |
| transduction or screening fails despite decent tissue | readout-layer bottleneck | delivery, assay timing, imaging, selection design, follow-up validation | [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md), [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md), [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md) |
| in vivo result is strong but uninterpretable | host attribution failure | which part comes from host, injury context, recipient variability | [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md), [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md) |

## 1. Check access and geometry before adding more biology

[Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)와 [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)는 many failures가 exposure route mismatch에서 생길 수 있음을 보여준다.

- apical biology를 보고 싶은데 lumen이 닫혀 있음
- microbe나 ligand를 올바른 surface에 못 닿게 함
- 3D geometry 때문에 readout이 물리적으로 가려짐

이 경우 immune, vascular, animal branch를 더하는 것은 대개 순서가 잘못된 대응이다.

## 2. Re-check whether the baseline is actually stable

[Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)는 reproducible size and composition control이 screening compatibility의 핵심이라고 보여준다. [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)도 cross-line robustness와 simplification의 중요성을 강조한다.

따라서 downstream assay가 흔들릴 때는 먼저:

- organoid size dispersion
- necrotic center 여부
- line-to-line robustness
- baseline composition drift

를 다시 보는 편이 맞다.

많은 경우 assay failure는 **assay가 아니라 baseline batch problem**이다.

## 3. If the assay asks for interaction, verify that the partner is really present

[Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)는 immune biology가 target organoid alone에서 나오지 않는다는 점을 보여준다. [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)도 host-microbe interaction이 단순 epithelial baseline만으로는 열리지 않음을 보여준다.

즉 phenotype가 interaction-derived라면, 실패를 baseline derivation 탓으로 돌리기 전에 **정말 필요한 partner가 assay 안에 들어왔는지**를 먼저 봐야 한다.

## 4. If tissue support is limiting, improve support before adding more readouts

[Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md), [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md), [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)는 large or complex organoid가 **diffusion, perfusion, or support bottleneck**에 걸릴 수 있음을 보여준다.

대표적인 신호는:

- stressed or necrotic core
- weak maturation despite long culture
- readout 전에 tissue quality가 무너짐
- larger constructs일수록 phenotype가 악화됨

이 경우 더 정교한 imaging이나 더 많은 perturbation을 추가하기 전에 **vascular or perfusion correction**이 우선일 수 있다.

## 5. Some failures are really engineering failures

[Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md), [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md), [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md)는 organoid가 이미 괜찮아도 **delivery, imaging, selection, follow-up validation**에서 프로젝트가 막힐 수 있음을 보여준다.

이런 경우 failure는 "biology가 없다"가 아니라:

- perturbation delivery가 약함
- assay timing이 잘못됨
- imaging window가 적절하지 않음
- pooled screen design이나 downstream validation이 약함

일 수 있다.

즉 organoid를 다시 만드는 대신 **readout stack**을 triage해야 할 때가 많다.

## 6. Animal rescue can create a new failure mode

[Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)와 [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)는 animal branch가 강한 validation을 줄 수 있지만, 동시에 **host attribution failure**를 만들어낼 수 있음을 보여준다.

in vivo signal이 좋아도:

- host environment가 얼마나 phenotype를 만들었는지
- recipient variability가 얼마나 큰지
- organoid-intrinsic effect가 얼마나 남아 있는지

를 분리하기 어려울 수 있다.

그래서 unclear in vitro assay를 animal로 옮기는 것이 항상 해결책은 아니다.

## A practical triage order

1. **surface and geometry가 맞는지 본다**
2. **baseline organoid가 reproducible한지 본다**
3. **질문에 필요한 partner가 실제로 들어왔는지 본다**
4. **tissue-support bottleneck이 있는지 본다**
5. **readout or engineering layer 자체를 점검한다**
6. **마지막에만 host-context branch를 고려한다**

이 순서를 따르면 "다시 처음부터 다 갈아엎자"로 가기 전에 어디가 진짜 병목인지 더 빨리 볼 수 있다.

## Rule of thumb

- **signal이 없으면** 먼저 geometry와 partner를 의심한다
- **noise가 크면** baseline reproducibility를 의심한다
- **성숙이 안 오르면** vascular or perfusion bottleneck을 의심한다
- **screen이 깨지면** readout stack을 의심한다
- **animal만 잘 되면** host attribution problem을 의심한다

## What this query does not settle

- 각 failure mode의 빈도를 숫자로 비교할 수 있는 corpus-level meta-analysis는 없다.
- organ별로 가장 흔한 failure mode ranking도 아직 충분히 정리되지 않았다.
- assay failure를 자동으로 구분할 formal diagnostic checklist는 아직 없다.

## Sources used

- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)
- [Organoid vascularization and perfusion strategies](../concepts/organoid-vascularization-and-perfusion-strategies.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)
- [Hogrebe 2021](../sources/hogrebe_2021_generation_of_insulin-producing_pancreatic.md)
- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Cakir 2019](../sources/cakir_2019_engineering_of_human_brain.md)
- [Homan 2019](../sources/homan_2019_flow-enhanced_vascularization_and_maturation.md)
- [Wörsdorfer 2019](../sources/worsdorfer_2019_generation_of_complex_human_organoid.md)
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
