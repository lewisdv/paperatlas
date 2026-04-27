const fs = await import("node:fs/promises");
const path = await import("node:path");
const { execFile } = await import("node:child_process");
const { promisify } = await import("node:util");
const { Presentation, PresentationFile } = await import("@oai/artifact-tool");

const W = 1280;
const H = 720;

const DECK_ID = "brain-organoid-question-journey";
const OUT_DIR = "/Users/davin/paper_collect/collections/organoid/presentation/brain-organoid-question-journey/outputs";
const REF_DIR = "/Users/davin/paper_collect/collections/organoid/presentation/brain-organoid-question-journey/references";
const SCRATCH_DIR = path.resolve(process.env.PPTX_SCRATCH_DIR || path.join("tmp", "slides", DECK_ID));
const PREVIEW_DIR = path.join(SCRATCH_DIR, "preview");
const VERIFICATION_DIR = path.join(SCRATCH_DIR, "verification");
const INSPECT_PATH = path.join(SCRATCH_DIR, "inspect.ndjson");
const MAX_RENDER_VERIFY_LOOPS = 3;

const INK = "#132024";
const GRAPHITE = "#344146";
const MUTED = "#6A767C";
const PAPER = "#F7F1E7";
const WHITE = "#FFFDF8";
const PANEL = "#FFFDF8F7";
const PANEL_SOFT = "#FBF7EF";
const MINT = "#DDF4E8";
const MIST = "#E6EEF0";
const GOLD_TINT = "#F4E8C8";
const ROSE_TINT = "#F7DDD8";
const ACCENT = "#1D9A69";
const ACCENT_DARK = "#0F5B3F";
const GOLD = "#C9972B";
const CORAL = "#D66C60";
const NAVY_TINT = "#DCE7EE";
const TRANSPARENT = "#00000000";

const TITLE_FACE = "Malgun Gothic";
const BODY_FACE = "Malgun Gothic";
const MONO_FACE = "Aptos Mono";
const LATIN_FACE = "Arial";
const execFileAsync = promisify(execFile);

const FALLBACK_PLATE_DATA_URL =
  "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII=";

const SOURCES = {
  overview: "collections/organoid/wiki/overview.md",
  index: "collections/organoid/wiki/index.md",
  q1: "collections/organoid/wiki/queries/20260408_174047_brain-subregion-protocol-comparison.md",
  q2: "collections/organoid/wiki/queries/20260409_brain-protocol-maturation-synchronization.md",
  q3: "collections/organoid/wiki/queries/20260420_172825_brain-functional-readout-selection.md",
  conceptSubregion: "collections/organoid/wiki/concepts/brain-subregion-specific-organoid-protocols.md",
  conceptBench: "collections/organoid/wiki/concepts/brain-organoid-fidelity-reproducibility-and-atlases.md",
  conceptPattern: "collections/organoid/wiki/concepts/brain-organoid-patterning-and-assembloids.md",
  synthBaseline: "collections/organoid/wiki/syntheses/20260424_organoid-developmental-baseline-and-regionalization-playbook.md",
  lancaster: "Lancaster 2014 | Generation of cerebral organoids from human pluripotent stem cells",
  sloan: "Sloan 2018 | Generation and assembly of human brain region-specific three-dimensional cultures",
  fitzgerald: "Fitzgerald 2024 | Generation of semi-guided cortical organoids with complex neural oscillations",
  eura: "Eura 2020 | Brainstem organoids from human pluripotent stem cells",
  pomeshchik: "Pomeshchik 2020 | Human iPSC-derived hippocampal spheroids",
  zagare: "Zagare 2021 | A robust protocol for the generation of human midbrain organoids",
  valiulahi: "Valiulahi 2021 | Generation of caudal-type serotonin neurons and hindbrain-fate organoids",
  atamian: "Atamian 2024 | Generation and long-term culture of human cerebellar organoids",
  ullah: "Ullah 2025 | Generating and characterizing human telencephalic brain organoids",
  velasco: "Velasco 2019 | Individual brain organoids reproducibly form cell diversity of the human cerebral cortex",
  yoon: "Yoon 2019 | Reliability of human cortical organoid generation",
  bhaduri: "Bhaduri 2020 | Cell stress in cortical organoids impairs molecular subtype specification",
  kanton: "Kanton 2019 | Organoid single-cell genomic atlas uncovers human-specific features of brain development",
  he: "He 2024 | An integrated transcriptomic cell atlas of human neural organoids",
  giandomenico: "Giandomenico 2021 | Generation and long-term culture of advanced cerebral organoids",
  kelley: "Kelley 2024 | Host circuit engagement of human cortical organoids transplanted in rodents",
  chen: "Chen 2023 | Protocol for generating reproducible miniaturized controlled midbrain organoids",
  meng: "Meng 2025 | CRISPR screens in human neural organoids and assembloids",
};

const SLIDES = [
  {
    id: "cover",
    kicker: "BRAIN ORGANOID QUESTION CHAIN",
    title: "Brain organoid protocol 비교는\n왜 subregion 비교만으로 끝나지 않는가",
    subtitle:
      "LLM-wiki를 collection 단위로 운영한 뒤,\nbrain organoid 질문이 subregion 비교에서 readout-first rule로 어떻게 확장됐는지를 보여준다.",
    moment: "질문이 바뀌면 비교 기준도 바뀐다",
    notes:
      "이 발표는 LLM-wiki 운영 방식을 짧게 소개한 뒤, 그 위에서 brain organoid 질문이 어떻게 정교해졌는지를 보여준다.\n처음에는 brain subregion별 프로토콜 차이를 비교하고 싶었지만, 정리할수록 reproducibility, fidelity, timing, readout 문제가 분리되기 시작했다.\n오늘의 핵심 문장은 '질문이 바뀌면 비교 기준도 바뀐다'이다.",
    sources: ["index", "q1", "q2", "q3"],
  },
  {
    id: "process",
    kicker: "LLM-WIKI WORKFLOW",
    title: "내가 LLM-wiki를\n운영하는 방식",
    subtitle:
      "collection으로 문헌 범위를 나누고,\nraw와 wiki를 분리해 질문 범위를 좁혔다.",
    notes:
      "이 슬라이드에서는 문헌을 어떻게 구조화했는지 먼저 소개한다.\ncollections 단위로 주제를 분리하고, raw source와 wiki synthesis를 나눠서 질문 범위를 좁혔다.\n그 결과 관련 없는 topic drift를 줄이고, 같은 주제 안에서 source, concept, query를 더 조밀하게 연결할 수 있었다.",
    sources: ["overview", "index", "q1", "q2", "q3"],
  },
  {
    id: "scope",
    kicker: "ACCESS LAYER",
    title: "Markdown wiki를\n탐색 가능한 HTML로 열어두기",
    subtitle:
      "저장된 Markdown을 정적 HTML로 바꾸고,\n로컬 뷰어와 GitHub Pages로 계속 접근할 수 있게 했다.",
    notes:
      "Markdown wiki를 그대로 두지 않고 HTML site로 렌더링해 읽기 쉬운 탐색 계층을 따로 운영했다.\nrender_wiki_html.py는 collection site와 top-level hub를 만들고, localhost viewer는 검색과 태그 필터, 그래프 뷰를 제공한다.\n또 GitHub Actions와 Pages를 붙여 원격에서도 같은 구조로 접근할 수 있게 했다.",
    sources: ["index"],
  },
  {
    id: "graph-subregion",
    kicker: "QUESTION 1",
    title: "1차 질문: 어떤 brain subregion\n프로토콜을 비교해야 하는가",
    subtitle:
      "처음에는 '어느 뇌 영역을 만들 것인가'가\n가장 중요한 비교 기준처럼 보였다.",
    notes:
      "첫 번째 질문 노트는 subregion 중심 비교다.\nLancaster는 broad cerebral baseline, Sloan과 Fitzgerald는 forebrain or cortical control, Zagare와 Eura와 Valiulahi는 posterior branch, Pomeshchik과 Atamian은 niche specialization으로 묶였다.\n이 단계에서는 brain organoid 설계 문제가 주로 subregion selection 문제처럼 보였다.",
    sources: [
      "q1",
      "conceptSubregion",
      "lancaster",
      "sloan",
      "fitzgerald",
      "zagare",
      "eura",
      "valiulahi",
      "pomeshchik",
      "atamian",
    ],
  },
  {
    id: "answer-one",
    kicker: "FIRST ANSWER",
    title: "1차 정리: 질문은 subregion selection으로\n정리될 수 있었다",
    subtitle:
      "brain organoid 비교는 우선\nsubregion과 patterning logic의 문제로 정리할 수 있었다.",
    notes:
      "첫 번째 정리에서 얻은 핵심은 세 갈래였다.\n첫째, broad cerebral baseline은 diversity가 크지만 variability도 크다.\n둘째, forebrain or cortical routes는 더 clean한 regional control을 준다.\n셋째, posterior or niche routes는 특정 biological question에 더 직접적이다.\n이 단계의 잠정 결론은 '많은 brain design 문제는 subregion selection 문제다'였다.",
    sources: ["q1", "conceptPattern", "synthBaseline", "lancaster", "sloan", "zagare", "atamian"],
  },
  {
    id: "limitation",
    kicker: "LIMITATION",
    title: "하지만 같은 subregion이어도\n같은 모델은 아니었다",
    subtitle:
      "같은 forebrain이어도 같은 모델이라고 말할 수는 없었다.\n질문은 region 밖으로 확장되기 시작했다.",
    notes:
      "subregion 비교는 useful한 출발점이었지만, 그것만으로는 모델의 quality를 설명하지 못했다.\n같은 cortical branch 안에서도 어떤 프로토콜은 더 reproducible하고, 어떤 것은 primary tissue와 더 닮고, 어떤 것은 timing mapping이 더 분명했다.\n그래서 질문이 '어떤 region인가'에서 '어떤 benchmark로 믿을 수 있는가'로 이동했다.",
    sources: ["q1", "q2", "conceptBench"],
  },
  {
    id: "graph-benchmark",
    kicker: "QUESTION 2",
    title: "2차 질문: region 말고\n무엇을 따로 benchmark해야 하는가",
    subtitle:
      "Round 2-4의 benchmark 논문들이 들어오면서,\n질문 자체가 새 프레임으로 재구성됐다.",
    notes:
      "두 번째 질문 노트는 benchmark question이다.\nVelasco와 Yoon은 reproducibility, Bhaduri는 fidelity, Kanton은 timing, He는 cross-protocol atlas alignment를 제공했다.\n즉 새 논문이 추가되면서 더 많은 근거가 생긴 것이 아니라, 어떤 질문을 던져야 하는지 자체가 바뀌었다.",
    sources: ["q2", "conceptBench", "velasco", "yoon", "bhaduri", "kanton", "he"],
  },
  {
    id: "tension",
    kicker: "KEY TENSION",
    title: "가장 중요한 분리:\nreproducibility와 fidelity",
    subtitle:
      "이 발표에서 가장 중요한 전환은\nreproducibility와 fidelity를 분리한 순간이다.",
    notes:
      "이 슬라이드는 benchmark slide와 framework slide 사이의 다리 역할을 한다.\nVelasco와 Yoon은 잘 반복되는 cortical branch를 보여주지만, Bhaduri는 그 branch가 primary fetal cortex와 얼마나 다른지를 보여준다.\n즉 '잘 반복된다'와 '더 진짜 같다'는 다른 질문이며, 이 구분이 이후 5축 프레임워크의 핵심이 된다.",
    sources: ["q2", "conceptBench", "velasco", "yoon", "bhaduri"],
  },
  {
    id: "framework",
    kicker: "FRAMEWORK",
    title: "그래서 protocol 비교는\n5개의 축으로 나뉘었다",
    subtitle:
      "brain organoid protocol 비교는 한 축이 아니라,\n서로 다른 benchmark 축을 분리해서 봐야 했다.",
    notes:
      "결국 이 컬렉션에서 brain organoid 비교는 다섯 축으로 정리됐다.\nregion identity, reproducibility, fidelity, temporal mapping, atlas alignment는 서로 다른 measurement question이다.\n여기서 가장 중요한 메시지는 reproducibility와 fidelity가 같은 말이 아니라는 점이다.",
    sources: ["q2", "conceptBench", "velasco", "yoon", "bhaduri", "kanton", "he"],
  },
  {
    id: "readout",
    kicker: "QUESTION 3",
    title: "3차 질문: region보다\nreadout을 먼저 적어야 하는가",
    subtitle:
      "최종적으로 protocol choice는 region보다도\nreadout을 먼저 적는 문제에 가까워졌다.",
    notes:
      "세 번째 질문 노트에서는 protocol choice가 readout-first rule로 재정리된다.\ncomposition reproducibility를 원하면 Velasco or Yoon 계열, fidelity를 원하면 Bhaduri or He, timing을 원하면 Kanton, dish function을 원하면 Fitzgerald, host relevance를 원하면 Kelley, screening을 원하면 Chen or Meng이 우선 anchor가 된다.\n즉 최종 질문은 '어느 region을 만들까'보다 '무슨 readout을 먼저 믿고 싶은가'가 됐다.",
    sources: ["q3", "conceptPattern", "conceptBench", "fitzgerald", "kelley", "chen", "meng", "kanton", "he"],
  },
  {
    id: "review-writing",
    kicker: "REVIEW WRITING",
    title: "이 연결고리를 리뷰논문으로\n바꾸면 어떻게 쓰게 되는가",
    subtitle:
      "위키에서 질문이 이동한 순서가,\n리뷰논문의 장 구조와 핵심 주장 구조가 된다.",
    notes:
      "이 슬라이드는 발표의 마지막 부분에서 review paper writing과 직접 연결해 주는 역할을 한다.\n핵심은 논문을 하나씩 나열하는 리뷰가 아니라, 질문이 이동한 순서대로 chapter를 세우는 것이다.\n즉 protocol family에서 시작해 benchmark axes로 확장하고, 마지막에는 readout-first selection rule로 정리하는 구조가 된다.",
    sources: ["q1", "q2", "q3", "synthBaseline", "conceptBench", "conceptPattern"],
  },
  {
    id: "review-implication",
    kicker: "WHY BRAIN",
    title: "왜 organoid collection에서\nbrain branch를 발표 사례로 골랐나",
    subtitle:
      "protocol family, benchmark, readout이 한 branch 안에서\n연속적으로 이어져 질문의 이동을 보여주기 좋았다.",
    notes:
      "brain branch는 broad cerebral baseline에서 niche subregion까지 이어지고, 그 위에 benchmark 논문과 functional readout 논문이 덧붙는다.\n그래서 단순 문헌 요약이 아니라 질문의 이동을 단계적으로 보여주기 좋다.\n즉 workflow를 설명한 뒤 실제 branch 사례로 넘어가기에 가장 적합한 축이었다.",
    sources: ["overview", "index", "q1", "q2", "q3", "synthBaseline", "conceptBench", "conceptPattern"],
  },
  {
    id: "conclusion",
    kicker: "CLOSING",
    title: "정리: 좋은 질문은\n위키를 정리하면서 생겨났다",
    subtitle:
      "LLM-wiki 운영에서 출발한 질문 제한이,\n결국 더 정교한 brain organoid 비교 기준으로 이어졌다.",
    notes:
      "마무리에서는 세 가지 takeaway를 다시 강조한다.\n첫째, subregion comparison은 출발점으로 유효했다.\n둘째, benchmark 축이 들어오면서 질문이 바뀌었다.\n셋째, 최종 rule은 readout-first protocol selection이다.\nQ and A에서는 reproducibility와 fidelity를 왜 분리해야 하는지, 어느 축을 먼저 볼지, host validation이 언제 필요한지를 중심으로 받으면 된다.",
    sources: ["q1", "q2", "q3", "conceptBench", "conceptPattern"],
  },
];

const SLIDE_ORDER = [
  "cover",
  "process",
  "scope",
  "review-implication",
  "graph-subregion",
  "answer-one",
  "limitation",
  "graph-benchmark",
  "tension",
  "framework",
  "readout",
  "review-writing",
  "conclusion",
];

const inspectRecords = [];

async function pathExists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

async function readImageBlob(imagePath) {
  const bytes = await fs.readFile(imagePath);
  if (!bytes.byteLength) {
    throw new Error(`Image file is empty: ${imagePath}`);
  }
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
}

async function normalizeImageConfig(config) {
  if (!config.path) return config;
  const { path: imagePath, ...rest } = config;
  return {
    ...rest,
    blob: await readImageBlob(imagePath),
  };
}

async function ensureDirs() {
  await fs.mkdir(OUT_DIR, { recursive: true });
  const obsoleteFinalArtifacts = [
    "preview",
    "verification",
    "inspect.ndjson",
    ["presentation", "proto.json"].join("_"),
    ["quality", "report.json"].join("_"),
  ];
  for (const obsolete of obsoleteFinalArtifacts) {
    await fs.rm(path.join(OUT_DIR, obsolete), { recursive: true, force: true });
  }
  await fs.mkdir(SCRATCH_DIR, { recursive: true });
  await fs.mkdir(PREVIEW_DIR, { recursive: true });
  await fs.mkdir(VERIFICATION_DIR, { recursive: true });
}

function lineConfig(fill = TRANSPARENT, width = 0, style = "solid") {
  return { style, fill, width };
}

function recordShape(slideNo, shape, role, shapeType, x, y, w, h) {
  if (!slideNo) return;
  inspectRecords.push({
    kind: "shape",
    slide: slideNo,
    id: shape?.id || `slide-${slideNo}-${role}-${inspectRecords.length + 1}`,
    role,
    shapeType,
    bbox: [x, y, w, h],
  });
}

function addShape(slide, geometry, x, y, w, h, fill = TRANSPARENT, line = TRANSPARENT, lineWidth = 0, meta = {}) {
  const shape = slide.shapes.add({
    geometry,
    position: { left: x, top: y, width: w, height: h },
    fill,
    line: lineConfig(line, lineWidth),
  });
  recordShape(meta.slideNo, shape, meta.role || geometry, geometry, x, y, w, h);
  return shape;
}

function addRotatedBar(slide, slideNo, x1, y1, x2, y2, color = GRAPHITE, thickness = 3, role = "connector") {
  const dx = x2 - x1;
  const dy = y2 - y1;
  const length = Math.sqrt(dx * dx + dy * dy);
  const angle = (Math.atan2(dy, dx) * 180) / Math.PI;
  const left = (x1 + x2) / 2 - length / 2;
  const top = (y1 + y2) / 2 - thickness / 2;
  const shape = slide.shapes.add({
    geometry: "rect",
    position: { left, top, width: length, height: thickness, rotation: angle },
    fill: color,
    line: lineConfig(TRANSPARENT, 0),
  });
  recordShape(slideNo, shape, role, "rect", left, top, length, thickness);
  return shape;
}

function normalizeText(text) {
  if (Array.isArray(text)) return text.map((item) => String(item ?? "")).join("\n");
  return String(text ?? "");
}

function textLineCount(text) {
  const value = normalizeText(text);
  if (!value.trim()) return 0;
  return Math.max(1, value.split(/\n/).length);
}

function requiredTextHeight(text, fontSize, lineHeight = 1.18, minHeight = 8) {
  const lines = textLineCount(text);
  if (lines === 0) return minHeight;
  return Math.max(minHeight, lines * fontSize * lineHeight);
}

function assertTextFits(text, boxHeight, fontSize, role = "text") {
  const required = requiredTextHeight(text, fontSize);
  const tolerance = Math.max(2, fontSize * 0.08);
  if (normalizeText(text).trim() && boxHeight + tolerance < required) {
    throw new Error(
      `${role} text box is too short: height=${boxHeight.toFixed(1)}, required>=${required.toFixed(1)}, ` +
        `lines=${textLineCount(text)}, fontSize=${fontSize}, text=${JSON.stringify(normalizeText(text).slice(0, 90))}`,
    );
  }
}

function wrapText(text, widthChars) {
  const words = normalizeText(text).split(/\s+/).filter(Boolean);
  const lines = [];
  let current = "";
  for (const word of words) {
    const next = current ? `${current} ${word}` : word;
    if (next.length > widthChars && current) {
      lines.push(current);
      current = word;
    } else {
      current = next;
    }
  }
  if (current) lines.push(current);
  return lines.join("\n");
}

function recordText(slideNo, shape, role, text, x, y, w, h) {
  const value = normalizeText(text);
  inspectRecords.push({
    kind: "textbox",
    slide: slideNo,
    id: shape?.id || `slide-${slideNo}-${role}-${inspectRecords.length + 1}`,
    role,
    text: value,
    textPreview: value.replace(/\n/g, " | ").slice(0, 180),
    textChars: value.length,
    textLines: textLineCount(value),
    bbox: [x, y, w, h],
  });
}

function recordImage(slideNo, image, role, imagePath, x, y, w, h) {
  inspectRecords.push({
    kind: "image",
    slide: slideNo,
    id: image?.id || `slide-${slideNo}-${role}-${inspectRecords.length + 1}`,
    role,
    path: imagePath,
    bbox: [x, y, w, h],
  });
}

function applyTextStyle(box, text, size, color, bold, face, align, valign, autoFit, listStyle) {
  box.text = text;
  box.text.fontSize = size;
  box.text.color = color;
  box.text.bold = Boolean(bold);
  box.text.alignment = align;
  box.text.verticalAlignment = valign;
  box.text.typeface = face;
  box.text.insets = { left: 0, right: 0, top: 0, bottom: 0 };
  if (autoFit) box.text.autoFit = autoFit;
  if (listStyle) box.text.style = "list";
}

function applyBilingualTypeface(box, text) {
  const value = normalizeText(text);
  const latinTokens = value.match(/[A-Za-z0-9][A-Za-z0-9&+./,:;'"!?()\-<>]*/g) || [];
  for (const token of latinTokens) {
    try {
      box.text.get(token).typeface = LATIN_FACE;
    } catch {
      // Ignore tokens the presentation surface cannot target precisely.
    }
  }
}

function addText(
  slide,
  slideNo,
  text,
  x,
  y,
  w,
  h,
  {
    size = 22,
    color = INK,
    bold = false,
    face = BODY_FACE,
    align = "left",
    valign = "top",
    fill = TRANSPARENT,
    line = TRANSPARENT,
    lineWidth = 0,
    autoFit = null,
    listStyle = false,
    checkFit = true,
    role = "text",
  } = {},
) {
  if (!checkFit && textLineCount(text) > 1) {
    throw new Error("checkFit=false is only allowed for single-line headers, footers, and captions.");
  }
  if (checkFit) assertTextFits(text, h, size, role);
  const box = addShape(slide, "rect", x, y, w, h, fill, line, lineWidth, { slideNo, role });
  applyTextStyle(box, text, size, color, bold, face, align, valign, autoFit, listStyle);
  if (face !== MONO_FACE) {
    applyBilingualTypeface(box, text);
  }
  recordText(slideNo, box, role, text, x, y, w, h);
  return box;
}

async function addImage(slide, slideNo, config, position, role, sourcePath = null) {
  const image = slide.images.add(await normalizeImageConfig(config));
  image.position = position;
  recordImage(
    slideNo,
    image,
    role,
    sourcePath || config.path || config.uri || "inline-data-url",
    position.left,
    position.top,
    position.width,
    position.height,
  );
  return image;
}

function addAtmosphere(slide, slideNo, tone = "green") {
  addShape(slide, "ellipse", 826, 82, 382, 382, tone === "coral" ? "#F9E5E1" : "#E4F5EC", TRANSPARENT, 0, {
    slideNo,
    role: "background glow",
  });
  addShape(slide, "ellipse", 968, 436, 206, 206, tone === "gold" ? "#F6EAD0" : "#E6EDF1", TRANSPARENT, 0, {
    slideNo,
    role: "background glow",
  });
  addShape(slide, "roundRect", 896, 148, 258, 148, PANEL, INK, 1, {
    slideNo,
    role: "background panel",
  });
  addShape(slide, "roundRect", 946, 322, 226, 118, PANEL, INK, 1, {
    slideNo,
    role: "background panel",
  });
  addShape(slide, "roundRect", 844, 486, 210, 96, PANEL, INK, 1, {
    slideNo,
    role: "background panel",
  });
}

async function addPlate(slide, slideNo, tone = "green") {
  slide.background.fill = PAPER;
  const platePath = path.join(REF_DIR, `slide-${String(slideNo).padStart(2, "0")}.png`);
  if (await pathExists(platePath)) {
    await addImage(
      slide,
      slideNo,
      { path: platePath, fit: "cover", alt: `Text-free art-direction plate for slide ${slideNo}` },
      { left: 0, top: 0, width: W, height: H },
      "art plate",
      platePath,
    );
  } else {
    await addImage(
      slide,
      slideNo,
      { dataUrl: FALLBACK_PLATE_DATA_URL, fit: "cover", alt: `Fallback blank art plate for slide ${slideNo}` },
      { left: 0, top: 0, width: W, height: H },
      "fallback art plate",
      "fallback-data-url",
    );
  }
  addAtmosphere(slide, slideNo, tone);
}

function addHeader(slide, slideNo, kicker, idx, total) {
  addText(slide, slideNo, String(kicker || "").toUpperCase(), 64, 34, 500, 24, {
    size: 13,
    color: ACCENT_DARK,
    bold: true,
    face: MONO_FACE,
    checkFit: false,
    role: "header",
  });
  addText(slide, slideNo, `${String(idx).padStart(2, "0")} / ${String(total).padStart(2, "0")}`, 1114, 34, 104, 24, {
    size: 13,
    color: ACCENT_DARK,
    bold: true,
    face: MONO_FACE,
    align: "right",
    checkFit: false,
    role: "header",
  });
  addShape(slide, "rect", 64, 64, 1152, 2, INK, TRANSPARENT, 0, { slideNo, role: "header rule" });
  addShape(slide, "ellipse", 57, 57, 16, 16, ACCENT, INK, 2, { slideNo, role: "header marker" });
}

function addFooter(slide, slideNo, text = "paper_collect / organoid collection / LLM-wiki workflow") {
  addText(slide, slideNo, text, 64, 684, 900, 18, {
    size: 10,
    color: MUTED,
    face: BODY_FACE,
    checkFit: false,
    role: "footer",
  });
}

function addGraphPlaceholder(slide, slideNo, x, y, w, h, pagePath, note = "Insert Obsidian screenshot here") {
  addShape(slide, "roundRect", x, y, w, h, PANEL_SOFT, INK, 1.2, { slideNo, role: "graph placeholder panel" });
  addShape(slide, "rect", x + 6, y + 6, w - 12, 6, "#A9C9BB", TRANSPARENT, 0, {
    slideNo,
    role: "graph placeholder accent",
  });
  addText(slide, slideNo, "Obsidian Local Graph", x + 28, y + 34, w - 56, 28, {
    size: 21,
    color: INK,
    bold: true,
    face: TITLE_FACE,
    align: "center",
    role: "graph placeholder title",
  });
  addText(slide, slideNo, "Insert screenshot here", x + 28, y + 76, w - 56, 22, {
    size: 12,
    color: GRAPHITE,
    face: MONO_FACE,
    align: "center",
    checkFit: false,
    role: "graph placeholder subtitle",
  });
  addShape(slide, "roundRect", x + 32, y + 118, w - 64, h - 194, WHITE, "#B6C1C5", 1, {
    slideNo,
    role: "graph image frame",
  });
  addText(slide, slideNo, pagePath, x + 52, y + h - 84, w - 104, 34, {
    size: 11,
    color: ACCENT_DARK,
    face: MONO_FACE,
    align: "center",
    role: "graph placeholder path",
  });
  addText(slide, slideNo, note, x + 32, y + h - 42, w - 64, 18, {
    size: 10,
    color: MUTED,
    face: BODY_FACE,
    align: "center",
    checkFit: false,
    role: "graph placeholder note",
  });
}

function addTitleBlock(slide, slideNo, title, subtitle, x = 64, y = 88, w = 760, options = {}) {
  const titleSize = options.titleSize || 40;
  const subtitleSize = options.subtitleSize || 18;
  const dark = Boolean(options.dark);
  const titleColor = dark ? WHITE : INK;
  const subtitleColor = dark ? WHITE : GRAPHITE;
  addText(slide, slideNo, title, x, y, w, options.titleHeight || 118, {
    size: titleSize,
    color: titleColor,
    bold: true,
    face: TITLE_FACE,
    role: "title",
  });
  if (subtitle) {
    addText(slide, slideNo, subtitle, x + 2, y + (options.subtitleOffset || 126), Math.min(w, 720), options.subtitleHeight || 66, {
      size: subtitleSize,
      color: subtitleColor,
      face: BODY_FACE,
      role: "subtitle",
    });
  }
}

function addPill(slide, slideNo, text, x, y, w, h, fill = MINT, textColor = ACCENT_DARK) {
  addText(slide, slideNo, text, x, y, w, h, {
    size: 12,
    color: textColor,
    bold: true,
    face: MONO_FACE,
    align: "center",
    valign: "middle",
    fill,
    line: INK,
    lineWidth: 1,
    role: "pill",
  });
}

function addBanner(slide, slideNo, text, x, y, w, h, fill = PANEL, accent = ACCENT) {
  addShape(slide, "roundRect", x, y, w, h, fill, INK, 1.2, { slideNo, role: "banner panel" });
  addShape(slide, "rect", x + 5, y + 5, 6, h - 10, accent, TRANSPARENT, 0, { slideNo, role: "banner accent" });
  addText(slide, slideNo, text, x + 22, y + 16, w - 40, h - 28, {
    size: 18,
    color: INK,
    face: BODY_FACE,
    role: "banner text",
  });
}

function addCard(slide, slideNo, x, y, w, h, label, body, accent = ACCENT, fill = PANEL) {
  addShape(slide, "roundRect", x, y, w, h, fill, INK, 1.2, { slideNo, role: `card panel: ${label}` });
  addShape(slide, "rect", x + 6, y + 6, w - 12, 6, accent, TRANSPARENT, 0, { slideNo, role: `card accent: ${label}` });
  addText(slide, slideNo, label, x + 22, y + 20, w - 44, 30, {
    size: 15,
    color: ACCENT_DARK,
    bold: true,
    face: MONO_FACE,
    role: "card label",
  });
  const wrapped = wrapText(body, Math.max(22, Math.floor(w / 12)));
  addText(slide, slideNo, wrapped, x + 22, y + 64, w - 44, h - 82, {
    size: 16,
    color: INK,
    face: BODY_FACE,
    role: `card body: ${label}`,
  });
}

function addMetricCard(slide, slideNo, x, y, w, h, metric, label, note, accent) {
  addShape(slide, "roundRect", x, y, w, h, PANEL, INK, 1.2, { slideNo, role: `metric panel: ${label}` });
  addShape(slide, "rect", x + 6, y + 6, w - 12, 6, accent, TRANSPARENT, 0, { slideNo, role: `metric accent: ${label}` });
  addText(slide, slideNo, metric, x + 20, y + 18, w - 40, 40, {
    size: 31,
    color: INK,
    bold: true,
    face: TITLE_FACE,
    role: "metric value",
  });
  addText(slide, slideNo, label, x + 20, y + 66, w - 40, 26, {
    size: 14,
    color: GRAPHITE,
    face: BODY_FACE,
    role: "metric label",
  });
  addText(slide, slideNo, note, x + 20, y + h - 28, w - 40, 18, {
    size: 10,
    color: MUTED,
    face: BODY_FACE,
    role: "metric note",
  });
}

function addNode(slide, slideNo, x, y, w, h, title, body = "", accent = ACCENT, fill = WHITE, kind = "source") {
  addShape(slide, "roundRect", x, y, w, h, fill, INK, 1.1, { slideNo, role: `node panel: ${title}` });
  addShape(slide, "rect", x + 5, y + 5, 5, h - 10, accent, TRANSPARENT, 0, { slideNo, role: `node accent: ${title}` });
  if (kind === "query") {
    addPill(slide, slideNo, "query", x + 18, y + 16, 64, 24, MINT, ACCENT_DARK);
  } else if (kind === "concept") {
    addPill(slide, slideNo, "concept", x + 18, y + 16, 76, 24, GOLD_TINT, "#7A5A14");
  } else {
    addPill(slide, slideNo, "source", x + 18, y + 16, 68, 24, NAVY_TINT, "#274D63");
  }
  addText(slide, slideNo, title, x + 18, y + 46, w - 34, body ? 24 : 56, {
    size: body ? 17 : 15,
    color: INK,
    bold: true,
    face: TITLE_FACE,
    role: "node title",
  });
  if (body) {
    addText(slide, slideNo, body, x + 18, y + 72, w - 34, h - 84, {
      size: 11,
      color: GRAPHITE,
      face: BODY_FACE,
      role: "node body",
    });
  }
  return { x, y, w, h, cx: x + w / 2, cy: y + h / 2 };
}

function connectNodes(slide, slideNo, nodeA, nodeB, color = "#98A7AD", thickness = 3) {
  addRotatedBar(slide, slideNo, nodeA.cx, nodeA.cy, nodeB.cx, nodeB.cy, color, thickness, "path connector");
}

function addLegendItem(slide, slideNo, x, y, label, fill) {
  addShape(slide, "roundRect", x, y, 18, 18, fill, INK, 1, { slideNo, role: "legend swatch" });
  addText(slide, slideNo, label, x + 28, y - 1, 160, 22, {
    size: 11,
    color: GRAPHITE,
    face: BODY_FACE,
    role: "legend label",
    checkFit: false,
  });
}

function addArrowBetween(slide, slideNo, x, y, w = 72) {
  addShape(slide, "rightArrow", x, y, w, 24, GOLD_TINT, INK, 1, { slideNo, role: "flow arrow" });
}

function addNotes(slide, body, sourceKeys) {
  const sourceLines = (sourceKeys || []).map((key) => `- ${SOURCES[key] || key}`).join("\n");
  slide.speakerNotes.setText(`${body || ""}\n\n[Sources]\n${sourceLines}`);
}

async function slideCover(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "green");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "cover overlay" });
  addShape(slide, "rect", 64, 86, 8, 458, ACCENT, TRANSPARENT, 0, { slideNo, role: "cover accent rule" });
  addText(slide, slideNo, data.kicker, 86, 88, 520, 24, {
    size: 13,
    color: ACCENT_DARK,
    bold: true,
    face: MONO_FACE,
    role: "kicker",
  });
  addText(slide, slideNo, data.title, 82, 130, 690, 152, {
    size: 45,
    color: INK,
    bold: true,
    face: TITLE_FACE,
    role: "cover title",
  });
  addText(slide, slideNo, data.subtitle, 86, 308, 620, 82, {
    size: 20,
    color: GRAPHITE,
    face: BODY_FACE,
    role: "cover subtitle",
  });
  addShape(slide, "roundRect", 86, 442, 432, 92, PANEL, INK, 1.2, { slideNo, role: "cover message panel" });
  addText(slide, slideNo, data.moment, 112, 468, 388, 40, {
    size: 22,
    color: INK,
    bold: true,
    face: TITLE_FACE,
    role: "cover moment",
  });

  const a = addNode(slide, slideNo, 842, 126, 214, 116, "subregion", "whole cerebral,\nforebrain, midbrain", ACCENT, WHITE, "concept");
  const b = addNode(slide, slideNo, 976, 280, 208, 116, "benchmark", "reproducibility,\nfidelity, timing", GOLD, WHITE, "concept");
  const c = addNode(slide, slideNo, 840, 440, 222, 116, "readout", "MEA, atlas, host,\nscreening", CORAL, WHITE, "concept");
  const center = addNode(slide, slideNo, 776, 274, 220, 104, "질문의 이동", "what should I compare first?", ACCENT_DARK, MINT, "query");
  connectNodes(slide, slideNo, center, a, "#97B7AA", 3);
  connectNodes(slide, slideNo, center, b, "#B7B0A1", 3);
  connectNodes(slide, slideNo, center, c, "#CDA69F", 3);

  addPill(slide, slideNo, "LLM-wiki", 86, 572, 104, 28, GOLD_TINT, "#7A5A14");
  addPill(slide, slideNo, "brain branch", 202, 572, 132, 28, MINT, ACCENT_DARK);
  addFooter(slide, slideNo, "흐름: LLM-wiki 운영 -> subregion 질문 -> benchmark -> readout-first rule");
  addNotes(slide, data.notes, data.sources);
}

async function slideProcess(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "gold");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7C8", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 720, { titleSize: 38, subtitleSize: 18 });

  addBanner(
    slide,
    slideNo,
    "collection 단위로 질문 범위를 제한해 관련 없는 지식 혼입을 줄이고, 같은 주제 안에서 source와 해석을 더 조밀하게 쌓아갔다.",
    64,
    174,
    1140,
    78,
    GOLD_TINT,
    GOLD,
  );

  addCard(
    slide,
    slideNo,
    76,
    286,
    252,
    192,
    "collection 분리",
    "organoid, single-cell, sequencing처럼 collection을 나눠 unrelated topic이 한 답변 안에 섞이지 않게 했다.",
    ACCENT,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    352,
    286,
    252,
    192,
    "raw / wiki 분리",
    "raw는 원본으로 남겨 두고, wiki에서 source page와 concept page, query를 계속 갱신한다.",
    GOLD,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    628,
    286,
    252,
    192,
    "질문 범위 제한",
    "collection 질문은 그 collection의 wiki와 raw만 쓰도록 해서 hallucination과 topic drift를 줄인다.",
    CORAL,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    904,
    286,
    252,
    192,
    "지식 밀도 축적",
    "source -> concept -> query -> synthesis가 같은 공간에 연결되면서 주제별 정보 밀도가 높아진다.",
    "#517C95",
    PANEL,
  );

  addPill(slide, slideNo, "raw/sources", 138, 560, 146, 30, NAVY_TINT, "#274D63");
  addArrowBetween(slide, slideNo, 292, 564, 70);
  addPill(slide, slideNo, "wiki/sources", 378, 560, 146, 30, MINT, ACCENT_DARK);
  addArrowBetween(slide, slideNo, 532, 564, 70);
  addPill(slide, slideNo, "concept / entity", 620, 560, 162, 30, GOLD_TINT, "#7A5A14");
  addArrowBetween(slide, slideNo, 792, 564, 70);
  addPill(slide, slideNo, "query / synthesis", 878, 560, 178, 30, ROSE_TINT, CORAL);
  addFooter(slide, slideNo, "운영 원리: topic boundary를 좁히고, 해석 가능한 지식을 같은 collection 안에 누적한다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideScope(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "green");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 740, { titleSize: 38, subtitleSize: 18 });

  addBanner(
    slide,
    slideNo,
    "Markdown으로 저장한 위키를 정적 HTML로 렌더링하고, 로컬 뷰어와 GitHub Pages를 통해 계속 읽고 탐색할 수 있게 했다.",
    64,
    174,
    1140,
    78,
    MINT,
    ACCENT,
  );

  addCard(
    slide,
    slideNo,
    74,
    286,
    268,
    202,
    "static HTML render",
    "Markdown wiki를 collection별 HTML site로 바꾸고, top-level hub도 함께 갱신한다.",
    ACCENT,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    368,
    286,
    268,
    202,
    "local viewer",
    "localhost viewer에서 검색, 태그 필터, 그래프 뷰를 통해 collection 내부 페이지를 빠르게 탐색한다.",
    GOLD,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    662,
    286,
    268,
    202,
    "GitHub Pages",
    "원격에서도 같은 구조로 읽을 수 있도록 public static site로 export하고 GitHub Pages에 배포한다.",
    CORAL,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    956,
    286,
    248,
    202,
    "auto update",
    "watcher와 deploy workflow를 붙여 collection 변경이 생기면 site도 함께 갱신되도록 만들었다.",
    "#517C95",
    PANEL,
  );

  addPill(slide, slideNo, "wiki/*.md", 120, 560, 120, 30, NAVY_TINT, "#274D63");
  addArrowBetween(slide, slideNo, 252, 564, 68);
  addPill(slide, slideNo, "wiki_html", 336, 560, 120, 30, MINT, ACCENT_DARK);
  addArrowBetween(slide, slideNo, 470, 564, 68);
  addPill(slide, slideNo, "local search", 556, 560, 132, 30, GOLD_TINT, "#7A5A14");
  addArrowBetween(slide, slideNo, 700, 564, 68);
  addPill(slide, slideNo, "GitHub Pages", 786, 560, 146, 30, ROSE_TINT, CORAL);
  addFooter(slide, slideNo, "접근 계층: Markdown wiki를 읽기 쉬운 site로 바꿔 검색, 탐색, 공유가 가능하도록 했다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideGraphSubregion(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "green");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 640, { titleSize: 36, subtitleSize: 18 });

  addCard(
    slide,
    slideNo,
    72,
    224,
    336,
    140,
    "출발 질문",
    "whole, forebrain,\nposterior/niche 중\n어떤 branch가 맞는가?",
    ACCENT,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    72,
    382,
    336,
    140,
    "여기에 연결된 문헌",
    "Lancaster, Sloan,\nFitzgerald,\nZagare 등 주요 protocol paper",
    GOLD,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    72,
    542,
    336,
    120,
    "1차 해석",
    "1차 결론:\n우선 subregion selection 문제로 읽었다.",
    CORAL,
    PANEL,
  );

  addGraphPlaceholder(
    slide,
    slideNo,
    458,
    204,
    738,
    428,
    "collections/organoid/wiki/queries/20260408_174047_brain-subregion-protocol-comparison.md",
    "Insert the local graph for Q1 here",
  );
  addFooter(slide, slideNo, "오른쪽에는 Q1 query note의 Obsidian local graph를 삽입하면 된다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideAnswerOne(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "gold");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 760, { titleSize: 38, subtitleSize: 18 });

  addCard(
    slide,
    slideNo,
    78,
    232,
    348,
    292,
    "broad cerebral baseline",
    "자가조직화 기반.\nregional diversity가 넓고 emergent architecture를 보기 좋지만,\nbatch variability와 mixed identity가 커진다.\n대표 anchor: Lancaster 2014.",
    ACCENT,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    466,
    232,
    348,
    292,
    "forebrain / cortical control",
    "dual SMAD 또는 semi-guided control을 통해\ncleaner regional identity와 더 높은 재현성을 노린다.\n대표 anchor: Sloan 2018, Fitzgerald 2024, Ullah 2025.",
    GOLD,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    854,
    232,
    348,
    292,
    "posterior / niche specialization",
    "midbrain, brainstem, hindbrain, hippocampus, cerebellum처럼\n질문 특이적인 posterior or niche branch로 간다.\n대표 anchor: Zagare, Eura, Pomeshchik, Atamian.",
    CORAL,
    PANEL,
  );

  addBanner(
    slide,
    slideNo,
    "1차 결론: 많은 brain organoid design 문제는 'brain vs brain'이 아니라 subregion selection 문제다.",
    90,
    562,
    1110,
    74,
    GOLD_TINT,
    GOLD,
  );
  addFooter(slide, slideNo, "subregion logic는 출발점으로 강력했지만, 아직 quality question을 충분히 설명하지 못했다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideLimitation(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "coral");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7D0", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 760, { titleSize: 38, subtitleSize: 18 });

  addBanner(
    slide,
    slideNo,
    "같은 forebrain branch 안에서도 어떤 protocol은 더 reproducible하고, 어떤 protocol은 primary fetal brain에 더 닮고, 어떤 protocol은 발달 timing 해석이 더 쉽다.",
    84,
    224,
    1112,
    102,
    ROSE_TINT,
    CORAL,
  );
  addCard(
    slide,
    slideNo,
    84,
    382,
    330,
    190,
    "reproducibility",
    "같은 protocol을 여러 번 돌렸을 때\ncell composition과 success rate가 얼마나 안정적인가?",
    ACCENT,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    474,
    382,
    330,
    190,
    "fidelity",
    "organoid cell state가\nprimary fetal brain과 얼마나 가까운가?",
    GOLD,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    864,
    382,
    330,
    190,
    "temporal mapping",
    "day 30, day 60 같은 culture day가\n실제 human developmental stage와 어떻게 대응되는가?",
    CORAL,
    PANEL,
  );
  addPill(slide, slideNo, "Q1 -> Q2", 1030, 582, 126, 28, MINT, ACCENT_DARK);
  addFooter(slide, slideNo, "한계 발견의 순간: region question만으로는 모델의 믿을 만함을 설명할 수 없었다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideGraphBenchmark(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "green");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 640, { titleSize: 36, subtitleSize: 18 });

  addCard(
    slide,
    slideNo,
    72,
    224,
    336,
    140,
    "새로 붙은 질문",
    "같은 cortical branch라도\nreproducibility, fidelity, timing을\n따로 물어야 하지 않는가?",
    ACCENT,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    72,
    382,
    336,
    120,
    "여기에 연결된 문헌",
    "Velasco, Yoon,\nBhaduri,\nKanton, He",
    GOLD,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    72,
    522,
    336,
    140,
    "질문의 변화",
    "subregion map 위에\nbenchmark axis가 덧붙으면서\n비교 기준이 완전히 달라졌다.",
    CORAL,
    PANEL,
  );

  addGraphPlaceholder(
    slide,
    slideNo,
    458,
    204,
    738,
    428,
    "collections/organoid/wiki/queries/20260409_brain-protocol-maturation-synchronization.md",
    "Insert the local graph for Q2 here",
  );
  addFooter(slide, slideNo, "오른쪽에는 Q2 query note의 Obsidian local graph를 삽입하면 된다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideTension(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "coral");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7D0", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 760, { titleSize: 38, subtitleSize: 18 });

  addBanner(
    slide,
    slideNo,
    "Velasco / Yoon이 보여준 것은 '잘 반복되는 cortical branch'이고, Bhaduri가 보여준 것은 '그 branch가 primary brain과 어디서 어긋나는가'이다.",
    78,
    210,
    1124,
    86,
    ROSE_TINT,
    CORAL,
  );

  addCard(
    slide,
    slideNo,
    92,
    344,
    486,
    240,
    "reproducibility 쪽 질문",
    "같은 protocol을 여러 번 돌렸을 때 organoid-to-organoid variance가 얼마나 낮은가?\n대표 anchor:\nVelasco 2019, Yoon 2019",
    ACCENT,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    700,
    344,
    486,
    240,
    "fidelity 쪽 질문",
    "그 organoid cell state가 primary fetal cortex와 얼마나 가까운가?\nstress-linked divergence는 없는가?\n대표 anchor:\nBhaduri 2020, He 2024",
    GOLD,
    PANEL,
  );

  addArrowBetween(slide, slideNo, 586, 456, 90);
  addPill(slide, slideNo, "same region, different question", 468, 604, 268, 28, MINT, ACCENT_DARK);
  addFooter(slide, slideNo, "이 구분이 있어야 5축 프레임워크가 단순 taxonomy가 아니라 실제 비교 도구가 된다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideFramework(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "gold");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7D2", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 760, { titleSize: 38, subtitleSize: 18 });

  addCard(slide, slideNo, 72, 220, 352, 146, "1. region identity", "어떤 brain region 또는 subregion을 만들고 있는가?\nanchor: Q1, Sloan, Atamian", ACCENT, PANEL);
  addCard(slide, slideNo, 464, 220, 352, 146, "2. reproducibility", "같은 protocol 안에서 cell composition variance가 얼마나 낮은가?\nanchor: Velasco, Yoon", GOLD, PANEL);
  addCard(slide, slideNo, 856, 220, 352, 146, "3. fidelity", "primary fetal brain과의 distance를 어떻게 볼 것인가?\nanchor: Bhaduri, He", CORAL, PANEL);
  addCard(slide, slideNo, 144, 398, 462, 150, "4. temporal mapping", "culture day를 developmental stage로 어떻게 읽을 것인가?\nanchor: Kanton, Giandomenico", "#517C95", PANEL);
  addCard(slide, slideNo, 676, 398, 462, 150, "5. atlas alignment", "여러 protocol을 같은 reference atlas 좌표계에서 어떻게 정렬할 것인가?\nanchor: He 2024", ACCENT_DARK, PANEL);

  addBanner(slide, slideNo, "핵심 메시지: reproducibility와 fidelity는 같은 말이 아니다.", 214, 586, 852, 64, ROSE_TINT, CORAL);
  addFooter(slide, slideNo, "5축은 서로 다른 benchmark question이며, 한 축의 강점이 다른 축의 답을 대신하지 않는다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideReadout(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "green");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 640, { titleSize: 36, subtitleSize: 18 });

  addCard(
    slide,
    slideNo,
    72,
    224,
    336,
    140,
    "최종 선택 규칙",
    "먼저 가장 중요한 readout을 적고,\n그 readout을 가장 직접적으로\n뒷받침하는 branch를 고른다.",
    ACCENT,
    MINT,
  );
  addCard(
    slide,
    slideNo,
    72,
    382,
    336,
    120,
    "대표 readout 묶음",
    "stability, fidelity/atlas,\nfunction, host, screening",
    GOLD,
    PANEL,
  );
  addCard(
    slide,
    slideNo,
    72,
    522,
    336,
    126,
    "대표 anchor",
    "Velasco, Bhaduri, He,\nFitzgerald, Kelley, Chen 등",
    CORAL,
    PANEL,
  );

  addGraphPlaceholder(
    slide,
    slideNo,
    458,
    204,
    738,
    428,
    "collections/organoid/wiki/queries/20260420_172825_brain-functional-readout-selection.md",
    "Insert the local graph for Q3 here",
  );
  addFooter(slide, slideNo, "오른쪽에는 Q3 query note의 Obsidian local graph를 삽입하면 된다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideReviewWriting(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "gold");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 760, { titleSize: 38, subtitleSize: 18 });

  addBanner(
    slide,
    slideNo,
    "핵심은 paper-by-paper 요약이 아니라, 위키에서 질문이 이동한 순서대로 review의 장과 비교 기준을 세우는 것이다.",
    74,
    182,
    1130,
    76,
    GOLD_TINT,
    GOLD,
  );

  addCard(
    slide,
    slideNo,
    74,
    300,
    320,
    220,
    "1장: protocol family",
    "whole cerebral,\nforebrain/cortical,\nposterior/niche를 baseline family로 먼저 정리한다.",
    ACCENT,
    PANEL,
  );
  addArrowBetween(slide, slideNo, 410, 396, 74);
  addCard(
    slide,
    slideNo,
    500,
    300,
    320,
    220,
    "2장: benchmark axes",
    "reproducibility,\nfidelity,\ntiming, atlas alignment를 비교 축으로 분리한다.",
    GOLD,
    PANEL,
  );
  addArrowBetween(slide, slideNo, 836, 396, 74);
  addCard(
    slide,
    slideNo,
    926,
    300,
    278,
    220,
    "3장: design rule",
    "마지막에는\nreadout-first selection rule로 protocol choice를 다시 묶는다.",
    CORAL,
    PANEL,
  );

  addBanner(
    slide,
    slideNo,
    "따라서 리뷰논문의 중심 주장도 '어느 protocol이 최고인가'가 아니라 '어떤 질문과 readout이 어떤 protocol selection rule을 요구하는가'가 된다.",
    74,
    562,
    1130,
    82,
    MINT,
    ACCENT,
  );
  addFooter(slide, slideNo, "이 연결고리가 발표의 질문 체인을 리뷰논문의 장 구조와 주장 구조로 바꿔준다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideReviewImplication(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "gold");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 760, { titleSize: 38, subtitleSize: 18 });

  addCard(
    slide,
    slideNo,
    74,
    242,
    332,
    236,
    "protocol family가 보인다",
    "whole cerebral, forebrain/cortical, posterior/niche가 한 branch 안에서 연속적으로 정리된다.",
    ACCENT,
    PANEL,
  );
  addArrowBetween(slide, slideNo, 420, 342, 74);
  addCard(
    slide,
    slideNo,
    500,
    242,
    332,
    236,
    "benchmark가 붙는다",
    "같은 branch 안에서도 reproducibility, fidelity, timing, atlas alignment를 따로 볼 수 있다.",
    GOLD,
    PANEL,
  );
  addArrowBetween(slide, slideNo, 846, 342, 74);
  addCard(
    slide,
    slideNo,
    926,
    242,
    280,
    236,
    "readout로 닫힌다",
    "결국 protocol choice가 readout-first rule로 이동하면서 발표의 결론을 만들 수 있다.",
    CORAL,
    PANEL,
  );

  addBanner(
    slide,
    slideNo,
    "brain branch는 protocol family -> benchmark -> readout이 한 흐름으로 이어져, 질문이 이동하는 과정을 가장 선명하게 보여준다.",
    76,
    528,
    1128,
    82,
    GOLD_TINT,
    GOLD,
  );
  addFooter(slide, slideNo, "그래서 organoid collection 전체 중에서도 brain branch가 발표 사례로 가장 적합했다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideConclusion(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "gold");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 760, { titleSize: 38, subtitleSize: 18 });

  addCard(slide, slideNo, 74, 220, 330, 176, "takeaway 1", "collection 단위의 LLM-wiki 운영은 질문 범위를 좁히고 문헌 해석을 더 조밀하게 쌓게 해줬다.", ACCENT, PANEL);
  addCard(slide, slideNo, 430, 220, 330, 176, "takeaway 2", "brain branch에서는 질문이 subregion selection에서 benchmark question으로 확장됐다.", GOLD, PANEL);
  addCard(slide, slideNo, 786, 220, 420, 176, "takeaway 3", "최종적으로 protocol choice는 region choice를 넘어 readout-first selection rule로 이동했다.", CORAL, PANEL);

  addBanner(slide, slideNo, "토론용 질문: 왜 reproducibility와 fidelity를 분리해야 하는가? 어떤 readout을 먼저 적어야 하는가? host validation은 언제 필요한가?", 74, 430, 1132, 86, PANEL, ACCENT);
  addBanner(slide, slideNo, "정리: 좋은 질문은 더 많은 논문을 나열해서가 아니라, 위키를 정리하면서 비교 기준을 다시 세울 때 생겨났다.", 74, 552, 1132, 82, GOLD_TINT, GOLD);
  addFooter(slide, slideNo, "LLM-wiki 운영 방식이 질문의 정교화와 발표의 구조를 함께 만들었다.");
  addNotes(slide, data.notes, data.sources);
}

async function createDeck() {
  await ensureDirs();
  const presentation = Presentation.create({ slideSize: { width: W, height: H } });
  const slideMap = new Map(SLIDES.map((slide) => [slide.id, slide]));
  for (let idx = 0; idx < SLIDE_ORDER.length; idx += 1) {
    const slideNo = idx + 1;
    const data = slideMap.get(SLIDE_ORDER[idx]);
    if (!data) throw new Error(`Unknown slide id in order: ${SLIDE_ORDER[idx]}`);
    if (data.id === "cover") await slideCover(presentation, data, slideNo, slideNo);
    else if (data.id === "process") await slideProcess(presentation, data, slideNo, slideNo);
    else if (data.id === "scope") await slideScope(presentation, data, slideNo, slideNo);
    else if (data.id === "graph-subregion") await slideGraphSubregion(presentation, data, slideNo, slideNo);
    else if (data.id === "answer-one") await slideAnswerOne(presentation, data, slideNo, slideNo);
    else if (data.id === "limitation") await slideLimitation(presentation, data, slideNo, slideNo);
    else if (data.id === "graph-benchmark") await slideGraphBenchmark(presentation, data, slideNo, slideNo);
    else if (data.id === "tension") await slideTension(presentation, data, slideNo, slideNo);
    else if (data.id === "framework") await slideFramework(presentation, data, slideNo, slideNo);
    else if (data.id === "readout") await slideReadout(presentation, data, slideNo, slideNo);
    else if (data.id === "review-writing") await slideReviewWriting(presentation, data, slideNo, slideNo);
    else if (data.id === "review-implication") await slideReviewImplication(presentation, data, slideNo, slideNo);
    else if (data.id === "conclusion") await slideConclusion(presentation, data, slideNo, slideNo);
    else throw new Error(`Unknown slide id: ${data.id}`);
  }
  return presentation;
}

async function saveBlobToFile(blob, filePath) {
  const bytes = new Uint8Array(await blob.arrayBuffer());
  await fs.writeFile(filePath, bytes);
}

async function patchExportedPptxFonts(pptxPath) {
  const patcherPath = "/Users/davin/paper_collect/collections/organoid/presentation/brain-organoid-question-journey/patch_pptx_theme_fonts.py";
  await execFileAsync(process.env.PPTX_PYTHON || "python3", [
    patcherPath,
    pptxPath,
    "--latin",
    LATIN_FACE,
    "--ea",
    BODY_FACE,
    "--cs",
    LATIN_FACE,
  ]);
}

async function writeInspectArtifact(presentation) {
  inspectRecords.unshift({
    kind: "deck",
    id: DECK_ID,
    slideCount: presentation.slides.count,
    slideSize: { width: W, height: H },
  });
  presentation.slides.items.forEach((slide, index) => {
    inspectRecords.splice(index + 1, 0, {
      kind: "slide",
      slide: index + 1,
      id: slide?.id || `slide-${index + 1}`,
    });
  });
  const lines = inspectRecords.map((record) => JSON.stringify(record)).join("\n") + "\n";
  await fs.writeFile(INSPECT_PATH, lines, "utf8");
}

async function currentRenderLoopCount() {
  const logPath = path.join(VERIFICATION_DIR, "render_verify_loops.ndjson");
  if (!(await pathExists(logPath))) return 0;
  const previous = await fs.readFile(logPath, "utf8");
  return previous.split(/\r?\n/).filter((line) => line.trim()).length;
}

async function nextRenderLoopNumber() {
  return (await currentRenderLoopCount()) + 1;
}

async function appendRenderVerifyLoop(presentation, previewPaths, pptxPath) {
  const logPath = path.join(VERIFICATION_DIR, "render_verify_loops.ndjson");
  const priorCount = await currentRenderLoopCount();
  const record = {
    kind: "render_verify_loop",
    deckId: DECK_ID,
    loop: priorCount + 1,
    maxLoops: MAX_RENDER_VERIFY_LOOPS,
    capReached: priorCount + 1 >= MAX_RENDER_VERIFY_LOOPS,
    timestamp: new Date().toISOString(),
    slideCount: presentation.slides.count,
    previewCount: previewPaths.length,
    previewDir: PREVIEW_DIR,
    inspectPath: INSPECT_PATH,
    pptxPath,
  };
  await fs.appendFile(logPath, JSON.stringify(record) + "\n", "utf8");
  return record;
}

async function verifyAndExport(presentation) {
  await ensureDirs();
  const nextLoop = await nextRenderLoopNumber();
  if (nextLoop > MAX_RENDER_VERIFY_LOOPS) {
    throw new Error(
      `Render/verify/fix loop cap reached: ${MAX_RENDER_VERIFY_LOOPS} total renders are allowed. ` +
        "Do not rerender; note any remaining visual issues in the final response.",
    );
  }
  await writeInspectArtifact(presentation);
  const previewPaths = [];
  for (let idx = 0; idx < presentation.slides.items.length; idx += 1) {
    const slide = presentation.slides.items[idx];
    const preview = await presentation.export({ slide, format: "png", scale: 1 });
    const previewPath = path.join(PREVIEW_DIR, `slide-${String(idx + 1).padStart(2, "0")}.png`);
    await saveBlobToFile(preview, previewPath);
    previewPaths.push(previewPath);
  }
  const pptxBlob = await PresentationFile.exportPptx(presentation);
  const pptxPath = path.join(OUT_DIR, "output.pptx");
  await pptxBlob.save(pptxPath);
  await patchExportedPptxFonts(pptxPath);
  const loopRecord = await appendRenderVerifyLoop(presentation, previewPaths, pptxPath);
  return { pptxPath, loopRecord };
}

const presentation = await createDeck();
const result = await verifyAndExport(presentation);
console.log(result.pptxPath);
