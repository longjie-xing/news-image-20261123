#!/usr/bin/env python3
"""Draw the news-image-20261123 poster: entry.png (1024x1024), Pillow only.

No external images. All text is drawn with DejaVu fonts.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY_TOP = (7, 17, 36)
NAVY_BOTTOM = (17, 36, 68)
PANEL = (26, 52, 88)
FOOTER = (5, 12, 26)
GOLD = (212, 175, 55)
ORANGE = (255, 150, 50)
RED = (214, 48, 48)
WHITE = (255, 255, 255)
PALE = (196, 210, 228)
DIVIDER = (70, 95, 130)


def font(path, size):
    return ImageFont.truetype(path, size)


def make_gradient():
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        r = int(NAVY_TOP[0] + (NAVY_BOTTOM[0] - NAVY_TOP[0]) * t)
        g = int(NAVY_TOP[1] + (NAVY_BOTTOM[1] - NAVY_TOP[1]) * t)
        b = int(NAVY_TOP[2] + (NAVY_BOTTOM[2] - NAVY_TOP[2]) * t)
        for x in range(W):
            px[x, y] = (r, g, b)
    return img


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, text, y, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)


def main():
    img = make_gradient()
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    draw_centered(d, "MONDAY, 23 NOVEMBER 2026", 34, font(BOLD, 34), GOLD)
    draw_centered(d, "THE WORLD IN ONE PICTURE", 82, font(BOLD, 56), WHITE)
    d.line([(362, 158), (662, 158)], fill=GOLD, width=2)

    # ---- Lead panel ----
    px0, py0, px1, py1 = 44, 184, 980, 380
    d.rounded_rectangle([px0, py0, px1, py1], radius=16, fill=PANEL)
    # red accent bar on the left edge
    d.rounded_rectangle([px0, py0, px0 + 14, py1], radius=7, fill=RED)
    d.rectangle([px0 + 7, py0, px0 + 14, py1], fill=RED)

    tx = px0 + 32
    d.text((tx, 200), "TOP STORY", font=font(BOLD, 18), fill=ORANGE)
    d.text((tx, 224), "COP31 COLLAPSES", font=font(BOLD, 64), fill=RED)

    lead_body = (
        "Antalya talks collapsed as the EU and UK rejected a text with no "
        "mention of fossil fuels \u2014 the longest summit ever, the first "
        "breakdown since Copenhagen 2009."
    )
    body_font = font(REG, 21)
    lines = wrap(d, lead_body, body_font, px1 - 24 - tx)
    assert len(lines) <= 2, f"lead body wrapped to {len(lines)} lines: {lines}"
    y = 302
    for ln in lines:
        d.text((tx, y), ln, font=body_font, fill=PALE)
        y += 28

    # ---- Five numbered stories ----
    stories = [
        (
            "Democrats Win Biggest House Majority Since 1992",
            "A recount confirms Chuck Hubbard beat Virginia Foxx by 330 votes "
            "in North Carolina's 5th district, taking Democrats to at least 258 "
            "seats \u2014 their largest majority in over 30 years.",
        ),
        (
            "Boy, 7, Pulled Alive From Rubble After 14 Hours",
            "Davyd was rescued in Dymer, where 11 people died; 15 died across "
            "the Kyiv region in total, and a 79-year-old woman was also pulled out alive.",
        ),
        (
            "24 Killed in Indonesia Candy Factory Fire",
            "The blaze at a factory in Cikande left about 30 workers still missing "
            "as rescuers search unstable wreckage; DNA identification may take weeks.",
        ),
        (
            "Houthis Claim Strike on Saudi Oil Refinery",
            "The group says it hit the Rabigh refinery and a radar site, but "
            "Saudi Arabia has not confirmed any damage.",
        ),
        (
            "NATO Meets Over Missiles That Fell in Poland",
            "All three objects that fell in Poland are confirmed as Russian Kh-101 "
            "cruise missiles, as the NATO council meets in Brussels.",
        ),
    ]

    head_font = font(BOLD, 23)
    story_font = font(REG, 19)
    num_font = font(BOLD, 20)
    block_y = 404
    for i, (headline, body) in enumerate(stories, start=1):
        # gold numbered badge
        cx, cy, r = 68, block_y + 20, 17
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD)
        num = str(i)
        nw = d.textlength(num, font=num_font)
        nh = num_font.getbbox(num)[3]
        d.text((cx - nw / 2, cy - nh / 2 - 2), num, font=num_font, fill=NAVY_TOP)

        sx = 96
        d.text((sx, block_y), headline, font=head_font, fill=WHITE)
        slines = wrap(d, body, story_font, 980 - 24 - sx)
        assert len(slines) <= 2, f"story {i} wrapped to {len(slines)} lines"
        sy = block_y + 34
        for ln in slines:
            d.text((sx, sy), ln, font=story_font, fill=PALE)
            sy += 25
        if i < len(stories):
            d.line([(sx, block_y + 88), (980, block_y + 88)], fill=DIVIDER, width=1)
        block_y += 100

    # ---- Footer strip ----
    d.rectangle([0, 916, W, H], fill=FOOTER)
    d.text((48, 930), "ALSO TODAY", font=font(BOLD, 18), fill=GOLD)
    foot_font = font(REG, 20)
    d.text((48, 958), "\u2022  BepiColombo enters orbit around Mercury after an eight-year journey.",
           font=foot_font, fill=PALE)
    d.text((48, 986), "\u2022  Marc M\u00e1rquez seals a record-equalling eighth MotoGP title in Portugal.",
           font=foot_font, fill=PALE)

    img.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
