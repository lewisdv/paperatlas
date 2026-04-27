const fs = await import("node:fs/promises");
const path = await import("node:path");
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

const TITLE_FACE = "Apple SD Gothic Neo";
const BODY_FACE = "Apple SD Gothic Neo";
const MONO_FACE = "Aptos Mono";

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
      "organoid 위키를 정리하면서, 단순한 region 비교 질문이\nbenchmark와 readout 중심 질문으로 어떻게 확장됐는지를 보여준다.",
    moment: "질문이 바뀌면 비교 기준도 바뀐다",
    notes:
      "이 발표는 결론만 요약하는 발표가 아니라, 질문이 위키 안에서 어떻게 정교해졌는지를 보여주는 발표다.\n처음에는 brain subregion별 프로토콜 차이를 비교하고 싶었지만, 정리할수록 reproducibility, fidelity, timing, readout 문제가 분리되기 시작했다.\n오늘의 핵심 문장은 '질문이 바뀌면 비교 기준도 바뀐다'이다.",
    sources: ["index", "q1", "q2", "q3"],
  },
  {
    id: "process",
    kicker: "WHY THIS TALK",
    title: "교수님 가이드에 맞춘\n발표 프레임",
    subtitle:
      "논문을 많이 읽었다는 사실보다,\n위키를 통해 질문이 어떻게 진화했는지를 중심에 둔다.",
    notes:
      "발표의 목적은 brain organoid 리뷰를 완성형 결론으로 제시하는 것이 아니라, paper_collect 위키에서 질문이 확장되는 과정을 보여주는 것이다.\n이 컬렉션은 active source page 96개, 그중 brain cluster 17개를 갖고 있고, 오늘 발표는 그중 3개의 질문 노트를 핵심 체인으로 삼는다.\n즉 corpus -> 첫 질문 -> 질문 재정의의 흐름 자체가 발표 내용이다.",
    sources: ["overview", "index", "q1", "q2", "q3"],
  },
  {
    id: "graph-subregion",
    kicker: "QUESTION 1",
    title: "1차 질문: brain subregion별\n프로토콜 비교",
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
    title: "1차 정리에서 얻은 답",
    subtitle:
      "brain organoid 비교는 우선\nsubregion과 patterning logic의 문제로 정리할 수 있었다.",
    notes:
      "첫 번째 정리에서 얻은 핵심은 세 갈래였다.\n첫째, broad cerebral baseline은 diversity가 크지만 variability도 크다.\n둘째, forebrain or cortical routes는 더 clean한 regional control을 준다.\n셋째, posterior or niche routes는 특정 biological question에 더 직접적이다.\n이 단계의 잠정 결론은 '많은 brain design 문제는 subregion selection 문제다'였다.",
    sources: ["q1", "conceptPattern", "synthBaseline", "lancaster", "sloan", "zagare", "atamian"],
  },
  {
    id: "limitation",
    kicker: "LIMITATION",
    title: "하지만 이 질문만으로는 부족했다",
    subtitle:
      "같은 forebrain이어도 같은 모델이라고 말할 수는 없었다.\n질문은 region 밖으로 확장되기 시작했다.",
    notes:
      "subregion 비교는 useful한 출발점이었지만, 그것만으로는 모델의 quality를 설명하지 못했다.\n같은 cortical branch 안에서도 어떤 프로토콜은 더 reproducible하고, 어떤 것은 primary tissue와 더 닮고, 어떤 것은 timing mapping이 더 분명했다.\n그래서 질문이 '어떤 region인가'에서 '어떤 benchmark로 믿을 수 있는가'로 이동했다.",
    sources: ["q1", "q2", "conceptBench"],
  },
  {
    id: "graph-benchmark",
    kicker: "QUESTION 2",
    title: "2차 질문: 발달정도·동기화 비교는\n어느 수준의 세분화가 필요한가",
    subtitle:
      "Round 2-4의 benchmark 논문들이 들어오면서,\n질문 자체가 새 프레임으로 재구성됐다.",
    notes:
      "두 번째 질문 노트는 benchmark question이다.\nVelasco와 Yoon은 reproducibility, Bhaduri는 fidelity, Kanton은 timing, He는 cross-protocol atlas alignment를 제공했다.\n즉 새 논문이 추가되면서 더 많은 근거가 생긴 것이 아니라, 어떤 질문을 던져야 하는지 자체가 바뀌었다.",
    sources: ["q2", "conceptBench", "velasco", "yoon", "bhaduri", "kanton", "he"],
  },
  {
    id: "framework",
    kicker: "FRAMEWORK",
    title: "최종적으로 얻은 5축 프레임워크",
    subtitle:
      "brain organoid protocol 비교는 한 축이 아니라,\n서로 다른 benchmark 축을 분리해서 봐야 했다.",
    notes:
      "결국 이 컬렉션에서 brain organoid 비교는 다섯 축으로 정리됐다.\nregion identity, reproducibility, fidelity, temporal mapping, atlas alignment는 서로 다른 measurement question이다.\n여기서 가장 중요한 메시지는 reproducibility와 fidelity가 같은 말이 아니라는 점이다.",
    sources: ["q2", "conceptBench", "velasco", "yoon", "bhaduri", "kanton", "he"],
  },
  {
    id: "readout",
    kicker: "QUESTION 3",
    title: "다음 단계: 결국 무엇을\n먼저 믿고 싶은가",
    subtitle:
      "최종적으로 protocol choice는 region보다도\nreadout을 먼저 적는 문제에 가까워졌다.",
    notes:
      "세 번째 질문 노트에서는 protocol choice가 readout-first rule로 재정리된다.\ncomposition reproducibility를 원하면 Velasco or Yoon 계열, fidelity를 원하면 Bhaduri or He, timing을 원하면 Kanton, dish function을 원하면 Fitzgerald, host relevance를 원하면 Kelley, screening을 원하면 Chen or Meng이 우선 anchor가 된다.\n즉 최종 질문은 '어느 region을 만들까'보다 '무슨 readout을 먼저 믿고 싶은가'가 됐다.",
    sources: ["q3", "conceptPattern", "conceptBench", "fitzgerald", "kelley", "chen", "meng", "kanton", "he"],
  },
  {
    id: "conclusion",
    kicker: "CLOSING",
    title: "결론과 토론",
    subtitle:
      "이 발표의 핵심은 brain organoid 정답이 아니라,\n질문이 위키를 통해 어떻게 더 좋은 질문으로 변했는가이다.",
    notes:
      "마무리에서는 세 가지 takeaway를 다시 강조한다.\n첫째, subregion comparison은 출발점으로 유효했다.\n둘째, benchmark 축이 들어오면서 질문이 바뀌었다.\n셋째, 최종 rule은 readout-first protocol selection이다.\nQ and A에서는 reproducibility와 fidelity를 왜 분리해야 하는지, 어느 축을 먼저 볼지, host validation이 언제 필요한지를 중심으로 받으면 된다.",
    sources: ["q1", "q2", "q3", "conceptBench", "conceptPattern"],
  },
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

function addFooter(slide, slideNo, text = "paper_collect / organoid collection / brain question chain") {
  addText(slide, slideNo, text, 64, 684, 900, 18, {
    size: 10,
    color: MUTED,
    face: BODY_FACE,
    checkFit: false,
    role: "footer",
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
  addShape(slide, "rect", x, y, 8, h, accent, TRANSPARENT, 0, { slideNo, role: "banner accent" });
  addText(slide, slideNo, text, x + 22, y + 16, w - 40, h - 28, {
    size: 18,
    color: INK,
    face: BODY_FACE,
    role: "banner text",
  });
}

function addCard(slide, slideNo, x, y, w, h, label, body, accent = ACCENT, fill = PANEL) {
  addShape(slide, "roundRect", x, y, w, h, fill, INK, 1.2, { slideNo, role: `card panel: ${label}` });
  addShape(slide, "rect", x, y, w, 8, accent, TRANSPARENT, 0, { slideNo, role: `card accent: ${label}` });
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
  addShape(slide, "rect", x, y, w, 8, accent, TRANSPARENT, 0, { slideNo, role: `metric accent: ${label}` });
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
  addShape(slide, "rect", x, y, 7, h, accent, TRANSPARENT, 0, { slideNo, role: `node accent: ${title}` });
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
  addRotatedBar(slide, slideNo, nodeA.cx, nodeA.cy, nodeB.cx, nodeB.cy, color, thickness, "graph connector");
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

  addPill(slide, slideNo, "15 min talk", 86, 572, 116, 28, GOLD_TINT, "#7A5A14");
  addPill(slide, slideNo, "question journey", 214, 572, 164, 28, MINT, ACCENT_DARK);
  addFooter(slide, slideNo, "발표 구조: 출발 질문 -> 한계 발견 -> 질문 재정의 -> 최종 선택 규칙");
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
    "교수님 포인트: 결론보다 '지식-위키 체인'이 어떻게 만들어졌는지를 보여주는 발표",
    816,
    104,
    390,
    92,
    GOLD_TINT,
    GOLD,
  );

  addMetricCard(slide, slideNo, 64, 232, 344, 116, "96", "active source pages", "overview.md", ACCENT);
  addMetricCard(slide, slideNo, 432, 232, 344, 116, "17", "brain cluster sources", "overview.md", GOLD);
  addMetricCard(slide, slideNo, 800, 232, 344, 116, "3", "core question notes in this talk", "q1 -> q2 -> q3", CORAL);

  addCard(
    slide,
    slideNo,
    82,
    406,
    314,
    184,
    "1. corpus browse",
    "index와 overview에서 organoid corpus 전체 구조를 잡고, brain 관련 source와 concept page를 먼저 추렸다.",
    ACCENT,
    PANEL,
  );
  addArrowBetween(slide, slideNo, 418, 486, 76);
  addCard(
    slide,
    slideNo,
    506,
    406,
    314,
    184,
    "2. first query",
    "subregion별 프로토콜 차이를 정리하면서 region choice를 중심 질문으로 세웠다.",
    GOLD,
    PANEL,
  );
  addArrowBetween(slide, slideNo, 842, 486, 76);
  addCard(
    slide,
    slideNo,
    930,
    406,
    256,
    184,
    "3. refined query",
    "그 질문만으로는 부족하다는 걸 발견하고 benchmark와 readout 질문으로 확장했다.",
    CORAL,
    PANEL,
  );
  addFooter(slide, slideNo, "오늘 발표는 이 세 단계 자체를 보여주는 발표다.");
  addNotes(slide, data.notes, data.sources);
}

async function slideGraphSubregion(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "green");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, data.subtitle, 64, 88, 720, { titleSize: 38, subtitleSize: 18 });

  const q = addNode(slide, slideNo, 472, 274, 280, 116, "Q1 | brain subregion별 프로토콜 비교", "어느 region을 만들 것인가?", ACCENT_DARK, MINT, "query");

  const n1 = addNode(slide, slideNo, 98, 188, 178, 112, "Lancaster 2014", "whole cerebral", "#5C8F74", WHITE, "source");
  const n2 = addNode(slide, slideNo, 296, 128, 178, 112, "Sloan 2018", "dorsal / ventral\nforebrain", "#5C8F74", WHITE, "source");
  const n3 = addNode(slide, slideNo, 804, 132, 182, 112, "Fitzgerald 2024", "semi-guided\ncortical", "#5C8F74", WHITE, "source");
  const n4 = addNode(slide, slideNo, 1004, 210, 174, 112, "Zagare 2021", "midbrain", "#5C8F74", WHITE, "source");
  const n5 = addNode(slide, slideNo, 996, 386, 182, 112, "Atamian 2024", "cerebellum", "#5C8F74", WHITE, "source");
  const n6 = addNode(slide, slideNo, 760, 498, 182, 112, "Pomeshchik 2020", "hippocampus", "#5C8F74", WHITE, "source");
  const n7 = addNode(slide, slideNo, 326, 500, 182, 112, "Valiulahi 2021", "hindbrain / 5-HT", "#5C8F74", WHITE, "source");
  const n8 = addNode(slide, slideNo, 108, 392, 178, 112, "Eura 2020", "brainstem", "#5C8F74", WHITE, "source");

  [n1, n2, n3, n4, n5, n6, n7, n8].forEach((node) => connectNodes(slide, slideNo, q, node));

  addPill(slide, slideNo, "whole cerebral", 64, 642, 132, 28, NAVY_TINT, "#274D63");
  addPill(slide, slideNo, "forebrain / cortical", 210, 642, 180, 28, NAVY_TINT, "#274D63");
  addPill(slide, slideNo, "posterior / niche", 404, 642, 156, 28, NAVY_TINT, "#274D63");
  addBanner(slide, slideNo, "1차 질문이 잘 풀어준 것: brain design 문제를 subregion selection 문제로 읽기 시작했다.", 726, 620, 490, 58, PANEL, ACCENT);
  addFooter(slide, slideNo, "graph-style view: question note를 중심으로 source cluster가 확장되는 모습");
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
  addTitleBlock(slide, slideNo, data.title, data.subtitle, 64, 88, 760, { titleSize: 37, subtitleSize: 18 });

  addPill(slide, slideNo, "Round 2-4 added", 878, 92, 162, 28, GOLD_TINT, "#7A5A14");
  const q = addNode(slide, slideNo, 456, 274, 320, 124, "Q2 | 발달정도·동기화 비교 프레임워크", "어느 수준의 세분화가 필요한가?", ACCENT_DARK, MINT, "query");

  const n1 = addNode(slide, slideNo, 102, 210, 204, 120, "Velasco 2019", "within-protocol\nreproducibility", ACCENT, WHITE, "source");
  const n2 = addNode(slide, slideNo, 164, 412, 204, 120, "Yoon 2019", "cross-line\nreliability", ACCENT, WHITE, "source");
  const n3 = addNode(slide, slideNo, 860, 164, 214, 128, "Bhaduri 2020", "fidelity versus\nstress", CORAL, WHITE, "source");
  const n4 = addNode(slide, slideNo, 930, 336, 214, 128, "Kanton 2019", "temporal map", GOLD, WHITE, "source");
  const n5 = addNode(slide, slideNo, 838, 510, 254, 110, "He 2024", "integrated atlas\nalignment", "#517C95", WHITE, "source");

  [n1, n2, n3, n4, n5].forEach((node) => connectNodes(slide, slideNo, q, node));
  addLegendItem(slide, slideNo, 64, 646, "query note", MINT);
  addLegendItem(slide, slideNo, 214, 646, "benchmark source", WHITE);
  addBanner(slide, slideNo, "새 논문이 추가되면서 '더 많이 안다'가 아니라 '무엇을 따로 질문해야 하는가'가 바뀌었다.", 636, 620, 580, 58, PANEL, ACCENT);
  addFooter(slide, slideNo, "graph-style view: subregion map 위에 benchmark branch가 새로 얹힌 순간");
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
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 760, { titleSize: 38, subtitleSize: 18 });

  addCard(
    slide,
    slideNo,
    66,
    218,
    300,
    374,
    "readout-first rule",
    "1. 먼저 가장 중요한 readout을 적는다.\n2. 그 readout을 가장 직접적으로 최적화한 branch를 고른다.\n3. region, benchmark, host validation은 그다음 순서로 붙인다.",
    ACCENT,
    MINT,
  );

  const nodes = [
    [404, 222, "composition", "stability\nVelasco / Yoon", ACCENT],
    [690, 222, "fidelity", "primary-like\nBhaduri / He", GOLD],
    [976, 222, "timing", "maturation map\nKanton / Giandomenico", "#517C95"],
    [404, 412, "MEA", "oscillation\nFitzgerald", CORAL],
    [690, 412, "host circuit", "integration\nKelley", ACCENT_DARK],
    [976, 412, "screening", "perturbation\nChen / Meng", "#7D6AA7"],
  ];

  for (const [x, y, title, body, accent] of nodes) {
    addNode(slide, slideNo, x, y, 242, 132, title, body, accent, WHITE, "source");
  }

  addFooter(slide, slideNo, "최종 질문: 어느 region을 만들까? 보다 무엇을 먼저 믿고 싶은가?");
  addNotes(slide, data.notes, data.sources);
}

async function slideConclusion(presentation, data, slideNo, idx) {
  const slide = presentation.slides.add();
  await addPlate(slide, slideNo, "gold");
  addShape(slide, "rect", 0, 0, W, H, "#FFFCF7CC", TRANSPARENT, 0, { slideNo, role: "content overlay" });
  addHeader(slide, slideNo, data.kicker, idx, SLIDES.length);
  addTitleBlock(slide, slideNo, data.title, null, 64, 88, 760, { titleSize: 38, subtitleSize: 18 });

  addCard(slide, slideNo, 74, 220, 330, 176, "takeaway 1", "subregion comparison은 좋은 출발점이었다.\n질문을 broad brain에서 subregion choice로 좁혀줬다.", ACCENT, PANEL);
  addCard(slide, slideNo, 430, 220, 330, 176, "takeaway 2", "하지만 benchmark 축이 들어오자,\n같은 region 안에서도 다른 질문이 생겼다.", GOLD, PANEL);
  addCard(slide, slideNo, 786, 220, 420, 176, "takeaway 3", "최종적으로 protocol choice는 region choice를 넘어\nreadout-first selection rule로 이동했다.", CORAL, PANEL);

  addBanner(slide, slideNo, "토론용 질문: 왜 reproducibility와 fidelity를 분리해야 하는가? 어느 축을 먼저 봐야 하는가? host validation은 언제 필요한가?", 74, 430, 1132, 86, PANEL, ACCENT);
  addBanner(slide, slideNo, "정리: 위키를 정리하자 질문이 바뀌었고, 질문이 바뀌자 비교 기준도 바뀌었다.", 74, 552, 1132, 82, GOLD_TINT, GOLD);
  addFooter(slide, slideNo, "Q&A로 넘어가면 각 질문의 우선축과 validation 순서를 중심으로 답하면 된다.");
  addNotes(slide, data.notes, data.sources);
}

async function createDeck() {
  await ensureDirs();
  const presentation = Presentation.create({ slideSize: { width: W, height: H } });
  for (let idx = 0; idx < SLIDES.length; idx += 1) {
    const slideNo = idx + 1;
    const data = SLIDES[idx];
    if (data.id === "cover") await slideCover(presentation, data, slideNo, slideNo);
    else if (data.id === "process") await slideProcess(presentation, data, slideNo, slideNo);
    else if (data.id === "graph-subregion") await slideGraphSubregion(presentation, data, slideNo, slideNo);
    else if (data.id === "answer-one") await slideAnswerOne(presentation, data, slideNo, slideNo);
    else if (data.id === "limitation") await slideLimitation(presentation, data, slideNo, slideNo);
    else if (data.id === "graph-benchmark") await slideGraphBenchmark(presentation, data, slideNo, slideNo);
    else if (data.id === "framework") await slideFramework(presentation, data, slideNo, slideNo);
    else if (data.id === "readout") await slideReadout(presentation, data, slideNo, slideNo);
    else if (data.id === "conclusion") await slideConclusion(presentation, data, slideNo, slideNo);
    else throw new Error(`Unknown slide id: ${data.id}`);
  }
  return presentation;
}

async function saveBlobToFile(blob, filePath) {
  const bytes = new Uint8Array(await blob.arrayBuffer());
  await fs.writeFile(filePath, bytes);
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
  const loopRecord = await appendRenderVerifyLoop(presentation, previewPaths, pptxPath);
  return { pptxPath, loopRecord };
}

const presentation = await createDeck();
const result = await verifyAndExport(presentation);
console.log(result.pptxPath);
