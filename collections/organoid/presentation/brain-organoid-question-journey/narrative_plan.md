# Brain Organoid Question Journey

## Audience

- 교수님과 동료 학생
- organoid 문헌을 읽고 있지만, 질문이 어떻게 정교해졌는지의 과정을 보고 싶은 청중

## Objective

- `brain organoid protocol 비교는 왜 subregion 비교만으로 끝나지 않는가`라는 질문이 어떻게 생기고 변했는지 15분 안에 보여준다.
- 논문 요약보다 `wiki -> query -> refined query` 체인을 중심에 둔다.

## Narrative Arc

1. organoid wiki corpus에서 brain branch를 먼저 분리한다.
2. 첫 질문은 `brain subregion별 프로토콜 비교`였다.
3. 그 정리만으로는 모델의 질을 설명하지 못하는 한계가 드러난다.
4. 질문은 `reproducibility, fidelity, temporal mapping`을 묻는 benchmark question으로 확장된다.
5. 특히 `reproducibility != fidelity`라는 긴장이 핵심 전환점이 된다.
6. 최종적으로 protocol choice는 `readout-first rule`로 재정리된다.
7. 이 질문 이동은 리뷰 논문 장 구조로 다시 고정된다.

## Slide List

1. Cover: 발표 질문과 핵심 메시지
2. Process framing: 교수님 가이드와 발표 구조
3. Scope: 왜 brain branch를 사례로 잡았는가
4. Graph view 1: 첫 질문과 source cluster
5. First answer: subregion logic로 얻은 1차 정리
6. Limitation: 왜 첫 질문만으로는 부족했는가
7. Graph view 2: benchmark question으로의 확장
8. Tension: reproducibility와 fidelity의 분리
9. Framework: 5축 비교 프레임워크
10. Readout-first rule: 최종 선택 기준
11. Review implication: 리뷰 논문 구조로의 연결
12. Conclusion and Q&A prompts

## Source Plan

- Core query notes:
  - `collections/organoid/wiki/queries/20260408_174047_brain-subregion-protocol-comparison.md`
  - `collections/organoid/wiki/queries/20260409_brain-protocol-maturation-synchronization.md`
  - `collections/organoid/wiki/queries/20260420_172825_brain-functional-readout-selection.md`
- Supporting concept pages:
  - `collections/organoid/wiki/concepts/brain-subregion-specific-organoid-protocols.md`
  - `collections/organoid/wiki/concepts/brain-organoid-fidelity-reproducibility-and-atlases.md`
  - `collections/organoid/wiki/concepts/brain-organoid-patterning-and-assembloids.md`
- Supporting synthesis:
  - `collections/organoid/wiki/syntheses/20260424_organoid-developmental-baseline-and-regionalization-playbook.md`
- Overview counts:
  - `collections/organoid/wiki/overview.md`

## Visual System

- Warm paper background with green, gold, and coral accents
- Korean-friendly sans typography
- graph-style node panels to mimic local graph thinking without requiring Obsidian screenshots
- editable text everywhere; no slide depends on rasterized text

## Asset Needs

- No external image generation required for the first build
- fallback image plate kept only to satisfy preview/export workflow
- graph-style visuals built with native PowerPoint shapes

## Editability Plan

- All titles, subtitles, graph node labels, cards, and banners remain editable text objects
- no screenshot-only slides
- speaker notes hold presenter script anchors and source trace
