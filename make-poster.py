#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news poster (1024x1024 PNG).

Pure Pillow drawing: dark-navy news poster, masthead, one lead story,
five further stories and a footer strip. Run: python3 make-poster.py
Writes entry.png next to this script.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
MARGIN = 48
CONTENT_W = W - 2 * MARGIN

# Palette
NAVY = (10, 27, 51)
NAVY_DEEP = (7, 19, 38)
PANEL = (18, 41, 77)
WHITE = (255, 255, 255)
BODY = (201, 214, 232)
MUTED = (148, 165, 194)
GOLD = (255, 184, 77)
ORANGE = (255, 122, 61)
RED = (255, 84, 72)
RULE = (58, 84, 128)
FOOTER_BG = (6, 15, 31)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Word-wrap text to lines that fit max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def main():
    img = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(img)

    # Subtle vertical gradient: navy deep at top to navy at bottom.
    for y in range(H):
        t = y / H
        r = int(NAVY_DEEP[0] + (NAVY[0] - NAVY_DEEP[0]) * t)
        g = int(NAVY_DEEP[1] + (NAVY[1] - NAVY_DEEP[1]) * t)
        b = int(NAVY_DEEP[2] + (NAVY[2] - NAVY_DEEP[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # ---------- Masthead ----------
    date_f = font(BOLD, 34)
    draw_centered(draw, 28, "MONDAY, 23 NOVEMBER 2026", date_f, GOLD)
    title_f = font(BOLD, 56)
    draw_centered(draw, 74, "THE WORLD IN ONE PICTURE", title_f, WHITE)
    draw.line([(MARGIN, 148), (W - MARGIN, 148)], fill=GOLD, width=3)
    draw.line([(MARGIN, 155), (W - MARGIN, 155)], fill=RULE, width=1)

    # ---------- Lead story ----------
    panel_top, panel_bottom = 172, 420
    draw.rounded_rectangle(
        [MARGIN, panel_top, W - MARGIN, panel_bottom], radius=10, fill=PANEL
    )
    # Red accent bar on the left edge of the panel.
    draw.rounded_rectangle(
        [MARGIN, panel_top, MARGIN + 10, panel_bottom], radius=5, fill=RED
    )
    x = MARGIN + 30
    label_f = font(BOLD, 24)
    draw.text((x, panel_top + 12), "TOP STORY", font=label_f, fill=ORANGE)
    head_text = "COP31 COLLAPSES"
    head_size = 88
    while head_size > 40:
        head_f = font(BOLD, head_size)
        if draw.textlength(head_text, font=head_f) <= CONTENT_W - 30:
            break
        head_size -= 2
    draw.text((x - 4, panel_top + 38), head_text, font=head_f, fill=RED)
    lead = (
        "UN climate talks in Antalya end with no deal \u2014 the first "
        "breakdown since Copenhagen in 2009 \u2014 after fossil-fuel "
        "language is stripped from the final text."
    )
    body_f = font(REG, 27)
    lines = wrap(draw, lead, body_f, CONTENT_W - 30)
    ly = panel_top + 146
    for line in lines:
        draw.text((x, ly), line, font=body_f, fill=BODY)
        ly += 32

    # ---------- Five stories ----------
    stories = [
        (
            "DEMOCRATS\u2019 BIGGEST HOUSE WIN SINCE 1992",
            "A recount win in North Carolina gives Democrats at least 258 "
            "House seats, the largest majority for either party in over "
            "30 years.",
        ),
        (
            "BOY, 7, PULLED ALIVE FROM RUBBLE",
            "Rescuers free a seven-year-old after 14 hours under a collapsed "
            "block in Dymer; nine dead there, 12 across the Kyiv region.",
        ),
        (
            "HOUTHIS CLAIM SAUDI REFINERY HIT",
            "Yemen\u2019s Houthis say they hit the Rabigh oil refinery and a "
            "radar site; Saudi Arabia does not confirm any damage.",
        ),
        (
            "NATO MEETS OVER POLAND MISSILES",
            "All three objects that fell in Poland are confirmed Russian "
            "Kh-101 cruise missiles; NATO\u2019s council meets in Brussels.",
        ),
        (
            "BEPICOLOMBO REACHES MERCURY",
            "After an eight-year journey, the ESA\u2013JAXA probe enters "
            "orbit around Mercury \u2014 only the second mission ever to "
            "do so.",
        ),
    ]
    story_head_f = font(BOLD, 32)
    story_body_f = font(REG, 24)
    row_top = 430
    row_h = 100
    for i, (headline, body) in enumerate(stories):
        y = row_top + i * row_h
        # Number badge.
        cx, cy = MARGIN + 22, y + 22
        draw.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=GOLD)
        num = str(i + 1)
        nw = draw.textlength(num, font=font(BOLD, 26))
        draw.text((cx - nw / 2, cy - 18), num, font=font(BOLD, 26), fill=NAVY_DEEP)
        tx = MARGIN + 56
        draw.text((tx, y), headline, font=story_head_f, fill=WHITE)
        blines = wrap(draw, body, story_body_f, W - MARGIN - tx)
        by = y + 40
        for line in blines:
            draw.text((tx, by), line, font=story_body_f, fill=BODY)
            by += 28
        if i < len(stories) - 1:
            draw.line(
                [(tx, y + row_h - 3), (W - MARGIN, y + row_h - 3)],
                fill=RULE,
                width=1,
            )

    # ---------- Footer strip ----------
    foot_top = 934
    draw.rectangle([0, foot_top, W, H], fill=FOOTER_BG)
    draw.line([(0, foot_top), (W, foot_top)], fill=GOLD, width=2)
    foot_label_f = font(BOLD, 20)
    draw.text(
        (MARGIN, foot_top + 8), "ALSO TODAY", font=foot_label_f, fill=GOLD
    )
    foot_f = font(REG, 21)
    draw.text(
        (MARGIN, foot_top + 36),
        "Marc M\u00e1rquez seals a record-equalling eighth MotoGP title in Portugal",
        font=foot_f,
        fill=MUTED,
    )
    draw.text(
        (MARGIN, foot_top + 62),
        "Magnitude 6.5 quake strikes the Vanuatu region, nearly 600 km deep",
        font=foot_f,
        fill=MUTED,
    )

    img.save(OUT, "PNG")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
