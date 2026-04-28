# Brain Organoid Question Journey

## Audience

- 교수님과 동료 학생
- organoid 문헌을 읽고 있지만, 질문이 어떻게 정교해졌는지의 과정을 보고 싶은 청중

## Objective

- `brain organoid protocol 비교는 왜 subregion 비교만으로 끝나지 않는가`라는 질문이 어떻게 생기고 변했는지 15분 안에 보여준다.
- 발표 초반에는 내가 LLM-wiki를 어떻게 운영하는지 소개하고, 이후에는 `wiki -> query -> refined query` 체인을 중심에 둔다.

## Narrative Arc

1. collection 기반 LLM-wiki 운영 방식과 HTML 접근 계층을 먼저 소개한다.
2. 그다음 organoid corpus에서 왜 brain branch를 발표 사례로 골랐는지 설명한다.
3. 첫 질문은 `brain subregion별 프로토콜 비교`였다.
4. 그 정리만으로는 모델의 질을 설명하지 못하는 한계가 드러난다.
5. 질문은 `reproducibility, fidelity, temporal mapping`을 묻는 benchmark question으로 확장된다.
6. 특히 `reproducibility != fidelity`라는 긴장이 핵심 전환점이 된다.
7. 최종적으로 protocol choice는 `readout-first rule`로 재정리된다.

## Slide List

1. Cover: 발표 질문과 핵심 메시지
2. LLM-wiki workflow: collection, raw/wiki 분리, 질문 범위 제한
3. HTML access layer: static HTML, local viewer, GitHub Pages, auto update
4. Why brain branch: 왜 organoid collection에서 이 branch를 발표 사례로 골랐는가
5. Graph view 1: Q1 subregion query와 연결된 branch
6. First answer: subregion logic로 얻은 1차 정리
7. Limitation: 왜 첫 질문만으로는 부족했는가
8. Graph view 2: Q2 benchmark query로의 확장
9. Tension: reproducibility와 fidelity의 분리
10. Framework: 5축 비교 프레임워크
11. Graph view 3: Q3 readout-first selection query
12. Conclusion and Q&A prompts

## Source Plan

- Core query notes:
  - `collections/Organoid/wiki/queries/20260408_174047_brain-subregion-protocol-comparison.md`
  - `collections/Organoid/wiki/queries/20260409_brain-protocol-maturation-synchronization.md`
  - `collections/Organoid/wiki/queries/20260420_172825_brain-functional-readout-selection.md`
- Supporting concept pages:
  - `collections/Organoid/wiki/concepts/brain-subregion-specific-organoid-protocols.md`
  - `collections/Organoid/wiki/concepts/brain-organoid-fidelity-reproducibility-and-atlases.md`
  - `collections/Organoid/wiki/concepts/brain-organoid-patterning-and-assembloids.md`
- Supporting synthesis:
  - `collections/Organoid/wiki/syntheses/20260424_organoid-developmental-baseline-and-regionalization-playbook.md`
- Overview counts:
  - `collections/Organoid/wiki/overview.md`

## Visual System

- Warm paper background with green, gold, and coral accents
- Korean-friendly sans typography
- explicit placeholder panels for real Obsidian local graph screenshots
- editable text everywhere; no slide depends on rasterized text

## Asset Needs

- No external image generation required for the first build
- fallback image plate kept only to satisfy preview/export workflow
- user will manually replace placeholder panels with Obsidian graph screenshots

## Editability Plan

- All titles, subtitles, graph node labels, cards, and banners remain editable text objects
- no screenshot-only slides
- speaker notes hold presenter script anchors and source trace
