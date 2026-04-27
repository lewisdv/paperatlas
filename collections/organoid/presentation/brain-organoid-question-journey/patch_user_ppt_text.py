#!/usr/bin/env python3
import argparse
import copy
import io
import zipfile
from xml.etree import ElementTree as ET


P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS = {"p": P_NS, "a": A_NS}
ET.register_namespace("p", P_NS)
ET.register_namespace("a", A_NS)


def qn(ns: str, tag: str) -> str:
    return f"{{{ns}}}{tag}"


def shape_texts(shape):
    return [t.text for t in shape.findall(".//a:t", NS) if t.text]


def normalize_joined_text(shape) -> str:
    parts = shape_texts(shape)
    return "".join(parts).replace("\u00a0", " ").strip()


def find_shape(slide_root, contains: str):
    for shape in slide_root.findall(".//p:sp", NS):
        if contains in normalize_joined_text(shape):
            return shape
    raise ValueError(f"Could not find shape containing: {contains}")


def replace_shape_text(shape, paragraphs):
    tx_body = shape.find("p:txBody", NS)
    if tx_body is None:
        raise ValueError("Shape has no txBody")

    body_pr = tx_body.find("a:bodyPr", NS)
    lst_style = tx_body.find("a:lstStyle", NS)
    template_p = tx_body.find("a:p", NS)
    if template_p is None:
        raise ValueError("Shape has no template paragraph")

    template_ppr = template_p.find("a:pPr", NS)
    template_rpr = template_p.find(".//a:rPr", NS)
    template_end = template_p.find("a:endParaRPr", NS)

    for child in list(tx_body):
        if child is body_pr or child is lst_style:
            continue
        tx_body.remove(child)

    for text in paragraphs:
        p = ET.SubElement(tx_body, qn(A_NS, "p"))
        if template_ppr is not None:
            p.append(copy.deepcopy(template_ppr))
        r = ET.SubElement(p, qn(A_NS, "r"))
        if template_rpr is not None:
            r.append(copy.deepcopy(template_rpr))
        t = ET.SubElement(r, qn(A_NS, "t"))
        t.text = text
        if template_end is not None:
            p.append(copy.deepcopy(template_end))


def patch_slide_4(slide_root):
    replace_shape_text(find_shape(slide_root, "Query branch about Brain region"), ["Brain branch 선택의 이유"])
    replace_shape_text(
        find_shape(slide_root, "reproducibility, fidelity,"),
        ["동일 branch 내에서도 reproducibility, fidelity, timing, atlas alignment를", "분리하여 평가할 수 있다."],
    )
    replace_shape_text(
        find_shape(slide_root, "최종적으로protocolchoice가readout-firstrule로이동하면서결론구조완성"),
        ["최종적으로 protocol choice는 readout-first rule로 정리되며,", "발표의 결론 구조를 형성한다."],
    )
    replace_shape_text(
        find_shape(slide_root, "brainbranch는protocolfamily"),
        ["brain branch는 protocol family -> benchmark -> readout 흐름이 연속적으로 연결되어,", "질문 체인의 이동을 가장 선명하게 드러낸다."],
    )


def patch_slide_12(slide_root):
    replace_shape_text(
        find_shape(slide_root, "핵심은개별논문나열이아니라"),
        ["핵심은 개별 논문 나열이 아니라, wiki에서 확인된 질문 이동 순서에 따라", "review의 장과 비교 기준을 구성하는 데 있다."],
    )
    replace_shape_text(
        find_shape(slide_root, "'어느protocol이우월한가'"),
        ["중심 질문은 '어느 protocol이 우월한가'가 아니라,", "'어떤 질문과 readout이 어떤 selection rule을 요구하는가'이다."],
    )


def patch_slide_13(slide_root):
    replace_shape_text(
        find_shape(slide_root, "질문제한은단순한안전장치가아니라사고의틀이다"),
        [
            "• 질문 제한은 단순한 안전장치가 아니라 비교 프레임의 설정이었다.",
            "• 위키의 성장은 논문 수보다 비교 축의 분화에서 두드러졌다.",
            "• query note는 답안 저장소보다 질문 수정 장치로 기능하였다.",
            "• 질문 체인은 발표 구조를 넘어 리뷰논문의 장 구조로 전환되었다.",
        ],
    )


def patch_pptx(input_path: str, output_path: str):
    buffer = io.BytesIO()
    with zipfile.ZipFile(input_path, "r") as src, zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as dst:
        for info in src.infolist():
            data = src.read(info.filename)
            if info.filename in {"ppt/slides/slide4.xml", "ppt/slides/slide12.xml", "ppt/slides/slide13.xml"}:
                root = ET.fromstring(data)
                if info.filename.endswith("slide4.xml"):
                    patch_slide_4(root)
                elif info.filename.endswith("slide12.xml"):
                    patch_slide_12(root)
                elif info.filename.endswith("slide13.xml"):
                    patch_slide_13(root)
                data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
            dst.writestr(info, data)

    with open(output_path, "wb") as f:
        f.write(buffer.getvalue())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("output_path")
    args = parser.parse_args()
    patch_pptx(args.input_path, args.output_path)


if __name__ == "__main__":
    main()
