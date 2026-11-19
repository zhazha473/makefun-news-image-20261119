#!/usr/bin/env python3
"""Compose the news-image-20261119 entry: a world atlas + timeline of
Thursday 19 November 2026. Build-time only: reads the public-domain
world.geo.json country outlines, draws everything with PIL, writes
news.png (1024x1024, deterministic). The submitted program (main.py)
only copies news.png to /output/entry.png.
"""
import json
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 230)
INK = (20, 32, 46)
RED = (178, 38, 30)
NAVY = (16, 42, 67)
OCEAN = (214, 228, 238)
LAND = (233, 223, 200)
LAND_EDGE = (122, 106, 79)
GRID = (190, 206, 218)
MUTED = (90, 100, 112)
REGION_COLORS = {
    "ASIA-PACIFIC": (27, 94, 122),
    "EUROPE · AFRICA · MIDDLE EAST": (122, 62, 27),
    "THE AMERICAS": (46, 94, 46),
}

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONTB if bold else FONT, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- stories
# (number, headline, lon, lat) — pinned on the map
PINNED = [
    (1, "GTA VI launches worldwide after a 13-year wait", 174.8, -36.8),
    (2, "Trump, Xi and Putin to hold trilateral talks in Shenzhen", 114.06, 22.55),
    (3, "US\u2013Iran exchange widens: drones over Kuwait and Bahrain", 47.98, 29.38),
    (4, "Anthropic debuts on Nasdaq at $83 \u2014 record $81.3bn IPO", -74.0, 40.7),
    (5, "EU proposes a \u20ac45bn loan for Ukraine", 4.35, 50.85),
    (6, "Canada rethinks China ties, Carney says", -75.7, 45.42),
    (7, "Israeli tanks cross the \u2018yellow line\u2019 in central Gaza", 34.47, 31.5),
    (8, "Cyclone Akvan nears India\u2019s east coast", 84.5, 15.5),
    (9, "Australia sanctions Israeli settlers over the West Bank", 149.13, -35.28),
    (10, "LPG tanker that sank off Bulgaria \u2018hit by projectiles\u2019", 28.0, 43.0),
    (11, "Somalia accuses UAE of building secret bases", 45.32, 2.05),
    (12, "US loses measles-free status after 26 years", -84.39, 33.75),
    (13, "India and Japan to review defence ties in Tokyo", 139.69, 35.68),
    (14, "Voyager 1: NASA confirms one light-day from Earth", None, None),
]

# (tag, headline) — the day sweeps west: Asia-Pacific, then Europe/Africa/
# Middle East, then the Americas
TIMELINE = {
    "ASIA-PACIFIC": [
        ("TECH", "Microsoft in talks to sell AI services to ByteDance"),
        ("TRADE", "US\u2013China barriers rise even as leaders meet often"),
        ("MEDIA", "\u2018We are journalists, not reel makers\u2019 \u2014 India press hits back"),
        ("SPORT", "Duckett\u2019s 133 puts England on top in Australia ODI"),
        ("MARKETS", "Oil prices fall as Gulf risk rises"),
        ("TAIWAN", "Taiwan adds transnational-repression crime to infiltration law"),
    ],
    "EUROPE \u00b7 AFRICA \u00b7 MIDDLE EAST": [
        ("POLITICS", "M\u00e9lenchon could win the French presidency, minister says"),
        ("UK", "Prince Harry: I would rejoin the army; warns of Russia threat"),
        ("TECH", "TfL photocard breach exposes 265,000 customers"),
        ("IRELAND", "Ax-wielding man destroys $60m US plane in Ireland"),
        ("SPORT", "Haaland penalty sends Norway to Nations League quarters"),
        ("FINANCE", "Deutsche Bank handled $582m in Epstein-linked deals \u2014 FT"),
        ("CRIME", "Cocaine and millions of pills seized in eastern Libya"),
        ("GULF", "Saudi Arabia: danger has passed in three southern cities"),
    ],
    "THE AMERICAS": [
        ("POLITICS", "Liu Yunping elected House Democratic Caucus chair"),
        ("SECURITY", "US senators warn AI cyber threats outpacing defences"),
        ("POLITICS", "US proposes tougher rules for employment green cards"),
        ("TECH", "Four Maryland students sue over AI Doritos-bag gun alert"),
        ("LAW", "McDonald\u2019s abuse case can proceed, judge rules"),
        ("TRADE", "Trump: US finalised \u2018significant\u2019 Philippines trade deal"),
        ("TECH", "Nadella: much critical infrastructure is \u2018unpatchable\u2019"),
        ("CULTURE", "GTA VI scores 99 on Metacritic from 140+ reviews"),
    ],
}


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=3)

    # ---------------------------------------------------------------- masthead
    d.text((28, 24), "THE WORLD IN A DAY  \u00b7  AN ATLAS AND A TIMELINE",
           font=font(14, bold=True), fill=RED)
    d.text((28, 42), "THURSDAY 19 NOVEMBER 2026",
           font=font(40, bold=True), fill=INK)
    d.text((28, 90), "36 stories  \u00b7  6 continents  \u00b7  from the Gulf to deep space",
           font=font(17), fill=MUTED)
    d.line([(28, 116), (996, 116)], fill=RED, width=3)

    # ---------------------------------------------------------------- map panel
    mx0, my0, mx1, my1 = 28, 124, 996, 428
    d.rectangle([mx0, my0, mx1, my1], fill=OCEAN, outline=INK, width=2)
    mw, mh = mx1 - mx0, my1 - my0

    def project(lon, lat):
        x = mx0 + (lon + 180.0) / 360.0 * mw
        y = my0 + (90.0 - lat) / 150.0 * mh  # lat 90 .. -60
        return x, y

    # graticule
    for lon in range(-150, 181, 30):
        x, _ = project(lon, 0)
        d.line([(x, my0), (x, my1)], fill=GRID, width=1)
    for lat in range(-60, 91, 30):
        _, y = project(0, lat)
        d.line([(mx0, y), (mx1, y)], fill=GRID, width=1)

    # country outlines (public-domain world.geo.json, build time only)
    with open("/tmp/world.geo.json", encoding="utf-8") as fh:
        world = json.load(fh)
    for feat in world["features"]:
        if feat["properties"].get("name") == "Antarctica":
            continue
        geom = feat["geometry"]
        polys = []
        if geom["type"] == "Polygon":
            polys = [geom["coordinates"]]
        elif geom["type"] == "MultiPolygon":
            polys = geom["coordinates"]
        for poly in polys:
            for ring in poly:
                pts = []
                for lon, lat in ring:
                    if lat < -60:
                        lat = -60
                    if lat > 85:
                        lat = 85
                    pts.append(project(lon, lat))
                if len(pts) > 2:
                    d.polygon(pts, fill=LAND, outline=LAND_EDGE)

    # deep-space inset (bottom-left, over empty South Pacific ocean)
    bx0, by0, bx1, by1 = 36, 372, 334, 420
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=6, fill=NAVY)
    d.text((bx0 + 10, by0 + 6), "\u2605  14  DEEP SPACE",
           font=font(13, bold=True), fill=(255, 214, 90))
    d.text((bx0 + 10, by0 + 25), "Voyager 1, one light-day out \u2014 NASA confirms",
           font=font(12), fill=(235, 240, 245))

    # pins (numbered dots; label offsets keep the crowded US north-east readable)
    offsets = {4: (13, -13), 6: (-16, -16), 12: (13, 12), 5: (12, -12)}
    pin_xy = {}
    for num, _headline, lon, lat in PINNED:
        if lon is None:
            continue
        x, y = project(lon, lat)
        pin_xy[num] = (x, y)
        ox, oy = offsets.get(num, (0, 0))
        cx, cy = x + ox, y + oy
        if (ox, oy) != (0, 0):
            d.line([(x, y), (cx, cy)], fill=RED, width=1)
            d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=RED)
        d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10],
                  fill=RED, outline=(255, 255, 255), width=2)
        label = str(num)
        tw = d.textlength(label, font=font(11, bold=True))
        d.text((cx - tw / 2, cy - 8), label, font=font(11, bold=True),
               fill=(255, 255, 255))

    # ---------------------------------------------------------------- legend
    d.text((28, 440), "PINNED ON THE MAP \u2014 THE DAY\u2019S 14 BIGGEST STORIES",
           font=font(14, bold=True), fill=INK)
    d.line([(28, 462), (996, 462)], fill=INK, width=2)
    legend_font = font(13)
    for i, (num, headline, _lon, _lat) in enumerate(PINNED):
        col = 0 if i < 7 else 1
        row = i % 7
        x = 28 if col == 0 else 520
        y = 470 + row * 20
        d.ellipse([x, y + 1, x + 16, y + 17], fill=RED)
        lab = str(num)
        tw = d.textlength(lab, font=font(10, bold=True))
        d.text((x + 8 - tw / 2, y + 2), lab, font=font(10, bold=True),
               fill=(255, 255, 255))
        d.text((x + 22, y + 1), headline, font=legend_font, fill=INK)

    # ---------------------------------------------------------------- timeline
    d.text((28, 618), "THE DAY SWEEPS WEST",
           font=font(20, bold=True), fill=INK)
    d.text((560, 624), "ASIA \u2192 EUROPE \u2192 THE AMERICAS",
           font=font(13, bold=True), fill=MUTED)
    d.line([(28, 646), (996, 646)], fill=INK, width=2)

    col_x = [28, 352, 676]
    col_w = [312, 312, 320]
    item_font = font(12)
    for ci, (region, items) in enumerate(TIMELINE.items()):
        x = col_x[ci]
        color = REGION_COLORS[region]
        d.rectangle([x, 654, x + col_w[ci], 678], fill=color)
        d.text((x + 8, 658), region, font=font(12, bold=True),
               fill=(255, 255, 255))
        y = 686
        for tag, text in items:
            d.rectangle([x, y + 3, x + 7, y + 10], fill=color)
            lines = wrap(d, tag + " \u2014 " + text, item_font, col_w[ci] - 14)
            ly = y
            for ln in lines:
                d.text((x + 12, ly), ln, font=item_font, fill=INK)
                ly += 14
            y = ly + 5
            if y > 950:
                break

    # ---------------------------------------------------------------- footer
    d.rectangle([0, 962, W, 988], fill=NAVY)
    d.text((28, 968), "36 STORIES  \u00b7  6 CONTINENTS  \u00b7  14 PINNED ON THE MAP  \u00b7  22 MORE IN THE TIMELINE",
           font=font(13, bold=True), fill=(255, 255, 255))
    d.text((28, 994),
           "Compiled from reporting first published Thursday 19 November 2026. Full sources in the README.",
           font=font(11), fill=MUTED)

    img.save("news.png", optimize=True)
    print("wrote news.png", img.size)


if __name__ == "__main__":
    main()
