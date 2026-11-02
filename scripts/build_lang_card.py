import html
import json
import os
import urllib.request

USER = "SoulmatelynchVFX"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "lang-card.svg")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

COLORS = {
    "Python": "#3572A5",
    "TypeScript": "#3178C6",
    "JavaScript": "#F1E05A",
    "CSS": "#563D7C",
    "HTML": "#E34C26",
    "Shell": "#89E051",
    "PowerShell": "#012456",
    "Batchfile": "#C1F12E",
    "Other": "#8B949E",
}


def api(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "lang-card")
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


repos = []
page = 1
while True:
    batch = api("https://api.github.com/users/%s/repos?per_page=100&type=owner&page=%d" % (USER, page))
    repos.extend(batch)
    if len(batch) < 100:
        break
    page += 1

totals = {}
for repo in repos:
    if repo.get("fork"):
        continue
    # Fail the run instead of publishing a plausible but incomplete chart.
    langs = api("https://api.github.com/repos/%s/%s/languages" % (USER, repo["name"]))
    for k, v in langs.items():
        if type(v) is not int or v < 0:
            raise ValueError("invalid language byte count")
        totals[k] = totals.get(k, 0) + v

if not totals or not sum(totals.values()):
    raise SystemExit("no language data")

grand = sum(totals.values())
items = sorted(totals.items(), key=lambda kv: (-kv[1], kv[0]))
# Retain every language, and round labels to a total of exactly 100.00%.
units = {name: value * 10000 // grand for name, value in items}
remaining = 10000 - sum(units.values())
by_remainder = sorted(items, key=lambda kv: -(kv[1] * 10000 % grand))
for name, _ in by_remainder[:remaining]:
    units[name] += 1
rows = [(name, units[name] / 100.0) for name, _ in items]

# layout — 与技能表同宽(572)、左对齐、压扁
W = 572
PAD = 16
BAR_W = 540          # 卡片内可用满宽
BAR_H = 13
BAR_Y = 42
TITLE_Y = 26
TITLE_SIZE = 22
LEG_Y = 76
ROW_H = 26
COL_W = 180
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

nrows = (len(rows) + 2) // 3
H = LEG_Y + ROW_H * (nrows - 1) + 14

parts = []
parts.append(
    '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
    'role="img" aria-label="Most Used Languages">' % (W, H, W, H)
)
parts.append(
    '<text x="%d" y="%d" fill="#2F81F7" font-family="%s" font-size="%d" font-weight="600">'
    'Most Used Languages</text>' % (PAD, TITLE_Y, FONT, TITLE_SIZE)
)

# stacked bar with rounded ends via clip path
parts.append('<defs><clipPath id="bar"><rect x="%d" y="%d" width="%d" height="%d" rx="%d"/></clipPath></defs>'
             % (PAD, BAR_Y, BAR_W, BAR_H, BAR_H // 2))
parts.append('<g clip-path="url(#bar)">')
x = float(PAD)
for name, pct in rows:
    seg = BAR_W * totals[name] / grand
    parts.append('<rect x="%.6f" y="%d" width="%.6f" height="%d" fill="%s"/>'
                 % (x, BAR_Y, seg, BAR_H, COLORS.get(name, "#8B949E")))
    x += seg
parts.append("</g>")

# Legend uses three columns, growing by row as needed.
for i, (name, pct) in enumerate(rows):
    col = i % 3
    row = i // 3
    cx = PAD + col * COL_W
    cy = LEG_Y + row * ROW_H
    parts.append('<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (cx, cy - 4, COLORS.get(name, "#8B949E")))
    parts.append('<text x="%d" y="%d" fill="#C9D1D9" font-family="%s" font-size="14">%s %.2f%%</text>'
                 % (cx + 16, cy, FONT, html.escape(name), pct))

parts.append("</svg>")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(parts))
print("written", OUT, "rows:", rows)

