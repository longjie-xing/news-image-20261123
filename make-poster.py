#!/usr/bin/env python3
"""Draw the 23 November 2026 news poster: 'The World in One Picture'.

Everything is drawn from scratch with Pillow. No external assets.
Output: entry.png (1024x1024) next to this script.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY_BOTTOM = (10, 27, 51)
NAVY_TOP = (7, 19, 38)
PANEL = (18, 41, 77)
WHITE = (255, 255, 255)
BODY = (201, 214, 232)
MUTED = (148, 165, 194)
GOLD = (255, 184, 77)
ORANGE = (255, 122, 61)
RED = (255, 84, 72)
RULE = (58, 84, 128)
FOOTER_BG = (6, 15, 31)

MARGIN = 48


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def wrap(draw, s, f, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = s.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if text_w(draw, trial, f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_font(draw, s, path, start, max_w):
    """Largest bold size <= start whose rendered width fits max_w."""
    size = start
    while size > 12:
        f = font(path, size)
        if text_w(draw, s, f) <= max_w:
            return f
        size -= 2
    return font(path, size)


def draw_gradient(img):
    px = img.load()
    for y in range(H):
        t = y / max(1, H - 1)
        r = int(NAVY_TOP[0] + (NAVY_BOTTOM[0] - NAVY_TOP[0]) * t)
        g = int(NAVY_TOP[1] + (NAVY_BOTTOM[1] - NAVY_TOP[1]) * t)
        b = int(NAVY_TOP[2] + (NAVY_BOTTOM[2] - NAVY_TOP[2]) * t)
        for x in range(W):
            px[x, y] = (r, g, b)


def main():
    img = Image.new("RGB", (W, H))
    draw_gradient(img)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    y = 34
    date_f = font(BOLD, 34)
    date = "MONDAY, 23 NOVEMBER 2026"
    d.text(((W - text_w(d, date, date_f)) / 2, y), date, font=date_f, fill=GOLD)
    y += 52
    title_f = font(BOLD, 56)
    title = "THE WORLD IN ONE PICTURE"
    d.text(((W - text_w(d, title, title_f)) / 2, y), title, font=title_f, fill=WHITE)
    y += 78
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=GOLD, width=3)
    y += 22

    # ---- Lead panel ----
    panel_x0, panel_x1 = MARGIN, W - MARGIN
    panel_y0 = y
    panel_h = 196
    panel_y1 = panel_y0 + panel_h
    d.rounded_rectangle([panel_x0, panel_y0, panel_x1, panel_y1],
                        radius=16, fill=PANEL)
    # red accent bar on the left edge
    d.rounded_rectangle([panel_x0, panel_y0, panel_x0 + 10, panel_y1],
                        radius=5, fill=RED)
    inner_x = panel_x0 + 30
    inner_w = panel_x1 - inner_x - 24
    py = panel_y0 + 18
    label_f = font(BOLD, 20)
    d.text((inner_x, py), "TOP STORY", font=label_f, fill=ORANGE)
    py += 32
    headline = "COP31 COLLAPSES"
    head_f = fit_font(d, headline, BOLD, 64, inner_w)
    d.text((inner_x, py), headline, font=head_f, fill=RED)
    py += head_f.size + 14
    body_f = font(REG, 21)
    lead_body = ("UN climate talks in Antalya end with no deal \u2014 the first "
                 "breakdown since Copenhagen in 2009 \u2014 after fossil-fuel "
                 "language is stripped from the final text.")
    for line in wrap(d, lead_body, body_f, inner_w):
        d.text((inner_x, py), line, font=body_f, fill=BODY)
        py += 28

    # ---- Five numbered stories ----
    stories = [
        ("DEMOCRATS' BIGGEST HOUSE WIN SINCE 1992",
         "A recount win in North Carolina gives Democrats at least 258 House "
         "seats, the largest majority for either party in over 30 years."),
        ("BOY, 7, PULLED ALIVE FROM RUBBLE",
         "Rescuers free a seven-year-old after 14 hours under a collapsed "
         "block in Dymer; nine dead there, 12 across the Kyiv region."),
        ("HOUTHIS CLAIM SAUDI REFINERY HIT",
         "Yemen's Houthis say they hit the Rabigh oil refinery and a radar "
         "site; Saudi Arabia does not confirm any damage."),
        ("NATO MEETS OVER POLAND MISSILES",
         "All three objects that fell in Poland are confirmed Russian Kh-101 "
         "cruise missiles; NATO's council meets in Brussels."),
        ("BEPICOLOMBO REACHES MERCURY",
         "After an eight-year journey, the ESA\u2013JAXA probe enters orbit "
         "around Mercury \u2014 only the second mission ever to do so."),
    ]
    sy = panel_y1 + 20
    head_f2 = font(BOLD, 23)
    body_f2 = font(REG, 19)
    badge_f = font(BOLD, 20)
    for i, (head, body) in enumerate(stories, start=1):
        # gold circle badge with number
        cx, cy = MARGIN + 18, sy + 16
        d.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], fill=GOLD)
        num = str(i)
        d.text((cx - text_w(d, num, badge_f) / 2, cy - 13), num,
               font=badge_f, fill=NAVY_TOP)
        tx = MARGIN + 52
        tw = W - MARGIN - tx
        d.text((tx, sy), head, font=head_f2, fill=WHITE)
        by = sy + 30
        for line in wrap(d, body, body_f2, tw):
            d.text((tx, by), line, font=body_f2, fill=BODY)
            by += 24
        sy = by + 6
        if i < len(stories):
            d.line([(tx, sy), (W - MARGIN, sy)], fill=RULE, width=1)
            sy += 10

    # ---- Footer strip ----
    fy0 = 902
    d.rectangle([0, fy0, W, H], fill=FOOTER_BG)
    d.line([(0, fy0), (W, fy0)], fill=RULE, width=2)
    fx = MARGIN
    fy = fy0 + 16
    foot_label_f = font(BOLD, 20)
    d.text((fx, fy), "ALSO TODAY", font=foot_label_f, fill=GOLD)
    fy += 32
    foot_f = font(REG, 20)
    d.text((fx, fy), "\u2022  Marc M\u00e1rquez seals a record-equalling eighth MotoGP title in Portugal",
           font=foot_f, fill=BODY)
    fy += 28
    d.text((fx, fy), "\u2022  Magnitude 6.5 quake strikes the Vanuatu region, nearly 600 km deep",
           font=foot_f, fill=BODY)

    img.save(OUT, "PNG")
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
