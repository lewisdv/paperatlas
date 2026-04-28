#!/usr/bin/env python3
import argparse
import io
import re
import zipfile


def patch_theme_fonts(xml_text: str, latin: str, east_asian: str, complex_script: str) -> str:
    xml_text = re.sub(
        r"<a:majorFont><a:latin typeface=\"[^\"]*\" /><a:ea typeface=\"[^\"]*\" /><a:cs typeface=\"[^\"]*\" /></a:majorFont>",
        f'<a:majorFont><a:latin typeface="{latin}" /><a:ea typeface="{east_asian}" /><a:cs typeface="{complex_script}" /></a:majorFont>',
        xml_text,
    )
    xml_text = re.sub(
        r"<a:minorFont><a:latin typeface=\"[^\"]*\" /><a:ea typeface=\"[^\"]*\" /><a:cs typeface=\"[^\"]*\" /></a:minorFont>",
        f'<a:minorFont><a:latin typeface="{latin}" /><a:ea typeface="{east_asian}" /><a:cs typeface="{complex_script}" /></a:minorFont>',
        xml_text,
    )
    return xml_text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx_path")
    parser.add_argument("--latin", required=True)
    parser.add_argument("--ea", required=True)
    parser.add_argument("--cs", required=True)
    args = parser.parse_args()

    buffer = io.BytesIO()
    with zipfile.ZipFile(args.pptx_path, "r") as src, zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as dst:
        for info in src.infolist():
            data = src.read(info.filename)
            if info.filename == "ppt/theme/theme1.xml":
                text = data.decode("utf-8")
                text = patch_theme_fonts(text, args.latin, args.ea, args.cs)
                data = text.encode("utf-8")
            dst.writestr(info, data)

    with open(args.pptx_path, "wb") as f:
        f.write(buffer.getvalue())


if __name__ == "__main__":
    main()
