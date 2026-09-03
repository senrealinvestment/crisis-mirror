#!/usr/bin/env python3
"""Convert the four Notebook LM source markdown files to letter PDFs."""
from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent
SOURCES = [
    "01-the-problem-and-the-product.md",
    "02-how-we-build-it.md",
    "03-team-and-engineering-backing.md",
    "04-the-ask-seed-and-springboard.md",
]


def md_inline(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(.+?)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r"<font face='Courier'>\1</font>", text)
    return text


def parse_table(lines: list[str]) -> list[list[str]]:
    rows = []
    for line in lines:
        if re.match(r"^\s*\|?\s*:?-{3,}", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    return rows


def build_story(md: str, styles: dict):
    story = []
    lines = md.splitlines()
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("# "):
            story.append(Paragraph(md_inline(line[2:].strip()), styles["h1"]))
            story.append(Spacer(1, 8))
            i += 1
            continue
        if line.startswith("## "):
            story.append(Spacer(1, 10))
            story.append(Paragraph(md_inline(line[3:].strip()), styles["h2"]))
            story.append(Spacer(1, 4))
            i += 1
            continue
        if line.startswith("### "):
            story.append(Spacer(1, 6))
            story.append(Paragraph(md_inline(line[4:].strip()), styles["h3"]))
            i += 1
            continue
        if line.lstrip().startswith("|"):
            block = []
            while i < n and lines[i].lstrip().startswith("|"):
                block.append(lines[i])
                i += 1
            rows = parse_table(block)
            if rows:
                wrapped = []
                for r_i, row in enumerate(rows):
                    wrapped.append(
                        [Paragraph(md_inline(c), styles["th" if r_i == 0 else "td"]) for c in row]
                    )
                col_w = 6.5 * inch / max(len(wrapped[0]), 1)
                table = Table(wrapped, colWidths=[col_w] * len(wrapped[0]), repeatRows=1)
                table.setStyle(
                    TableStyle(
                        [
                            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#9aa3ad")),
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f3a5f")),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 5),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                            ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f7f5f0")),
                        ]
                    )
                )
                story.append(table)
                story.append(Spacer(1, 10))
            continue
        if re.match(r"^\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i]):
                items.append(
                    ListItem(
                        Paragraph(md_inline(re.sub(r"^\d+\.\s+", "", lines[i])), styles["body"]),
                        leftIndent=12,
                    )
                )
                i += 1
            story.append(ListFlowable(items, bulletType="1", start="1", leftIndent=18))
            story.append(Spacer(1, 6))
            continue
        if line.startswith("- "):
            items = []
            while i < n and lines[i].startswith("- "):
                items.append(
                    ListItem(
                        Paragraph(md_inline(lines[i][2:]), styles["body"]),
                        leftIndent=8,
                    )
                )
                i += 1
            story.append(ListFlowable(items, bulletType="bullet", leftIndent=16))
            story.append(Spacer(1, 6))
            continue
        para = [line]
        i += 1
        while i < n and lines[i].strip() and not lines[i].startswith(("#", "- ", "|")) and not re.match(
            r"^\d+\.\s+", lines[i]
        ):
            para.append(lines[i])
            i += 1
        story.append(Paragraph(md_inline(" ".join(p.strip() for p in para)), styles["body"]))
        story.append(Spacer(1, 6))
    return story


def main() -> None:
    base = getSampleStyleSheet()
    styles = {
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Times-Bold",
            fontSize=16,
            leading=20,
            textColor=colors.HexColor("#1f3a5f"),
            spaceAfter=0,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Times-Bold",
            fontSize=13,
            leading=16,
            textColor=colors.HexColor("#1f3a5f"),
            spaceBefore=0,
            spaceAfter=0,
        ),
        "h3": ParagraphStyle(
            "H3",
            parent=base["Heading3"],
            fontName="Times-Bold",
            fontSize=11.5,
            leading=14,
            textColor=colors.HexColor("#3d4f61"),
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#1a1a1a"),
        ),
        "th": ParagraphStyle(
            "TH",
            parent=base["BodyText"],
            fontName="Times-Bold",
            fontSize=9,
            leading=12,
            textColor=colors.white,
        ),
        "td": ParagraphStyle(
            "TD",
            parent=base["BodyText"],
            fontName="Times-Roman",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#1a1a1a"),
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontName="Times-Italic",
            fontSize=8,
            textColor=colors.HexColor("#5c6570"),
            alignment=1,
        ),
    }

    written = []
    for name in SOURCES:
        src = ROOT / name
        out = ROOT / name.replace(".md", ".pdf")
        md = src.read_text(encoding="utf-8")
        title = md.splitlines()[0].lstrip("# ").strip()

        def on_page(canvas, doc, title=title):
            canvas.saveState()
            canvas.setStrokeColor(colors.HexColor("#1f3a5f"))
            canvas.setLineWidth(1.5)
            canvas.line(0.75 * inch, letter[1] - 0.45 * inch, letter[0] - 0.75 * inch, letter[1] - 0.45 * inch)
            canvas.setFont("Times-Italic", 8)
            canvas.setFillColor(colors.HexColor("#5c6570"))
            canvas.drawString(0.75 * inch, letter[1] - 0.38 * inch, "Cognitive Companion  ·  VCU Anesthesiology  ·  leadership briefing")
            canvas.line(0.75 * inch, 0.55 * inch, letter[0] - 0.75 * inch, 0.55 * inch)
            canvas.drawCentredString(letter[0] / 2, 0.38 * inch, f"{title}   ·   {doc.page}")
            canvas.restoreState()

        doc = SimpleDocTemplate(
            str(out),
            pagesize=letter,
            leftMargin=0.75 * inch,
            rightMargin=0.75 * inch,
            topMargin=0.7 * inch,
            bottomMargin=0.75 * inch,
            title=title,
            author="Sergio Navarrete, D.O.",
            subject="Cognitive Companion leadership briefing for Notebook LM",
        )
        doc.build(build_story(md, styles), onFirstPage=on_page, onLaterPages=on_page)
        written.append((out.name, out.stat().st_size))
    for name, size in written:
        print(f"{name}\t{size}")


if __name__ == "__main__":
    main()
