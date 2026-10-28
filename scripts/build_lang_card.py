import json
import os
import urllib.request

USER = "SoulmatelynchVFX"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "languages.svg")
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


repos = api("https://api.github.com/users/%s/repos?per_page=100&type=owner" % USER)
totals = {}
for repo in repos:
    if repo.get("fork"):
        continue
    try:
        langs = api("https://api.github.com/repos/%s/%s/languages" % (USER, repo["name"]))
    except Exception:
        continue
    for k, v in langs.items():
        totals[k] = totals.get(k, 0) + v

if not totals:
    raise SystemExit("no language data")

grand = sum(totals.values())
items = sorted(totals.items(), key=lambda kv: -kv[1])
top = items[:5]
rest = sum(v for _, v in items[5:])
rows = [(n, v / grand * 100.0) for n, v in top]
if rest:
    rows.append(("Other", rest / grand * 100.0))

# layout
W = 560
PAD = 36
BAR_W = 420          # 75% of 560
BAR_H = 16
BAR_Y = 76
TITLE_Y = 44
LEG_Y = 128
ROW_H = 38
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

H = LEG_Y + ROW_H * ((len(rows) + 2) // 3) + 6

parts = []
parts.append(
    '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
    'role="img" aria-label="Most Used Languages">' % (W, H, W, H)
)
parts.append(
    '<text x="%d" y="%d" fill="#2F81F7" font-family="%s" font-size="26" font-weight="600">'
    'Most Used Languages</text>' % (PAD, TITLE_Y, FONT)
)

# stacked bar with rounded ends via clip path
parts.append('<defs><clipPath id="bar"><rect x="%d" y="%d" width="%d" height="%d" rx="%d"/></clipPath></defs>'
             % (PAD, BAR_Y, BAR_W, BAR_H, BAR_H // 2))
parts.append('<g clip-path="url(#bar)">')
x = float(PAD)
for name, pct in rows:
    seg = BAR_W * pct / 100.0
    parts.append('<rect x="%.2f" y="%d" width="%.2f" height="%d" fill="%s"/>'
                 % (x, BAR_Y, seg, BAR_H, COLORS.get(name, "#8B949E")))
    x += seg
parts.append("</g>")

# legend, three columns x two rows
for i, (name, pct) in enumerate(rows):
    col = i % 3
    row = i // 3
    cx = PAD + col * 172
    cy = LEG_Y + row * ROW_H
    parts.append('<circle cx="%d" cy="%d" r="6" fill="%s"/>' % (cx, cy - 5, COLORS.get(name, "#8B949E")))
    parts.append('<text x="%d" y="%d" fill="#C9D1D9" font-family="%s" font-size="14">%s %.2f%%</text>'
                 % (cx + 16, cy, FONT, name, pct))

parts.append("</svg>")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(parts))
print("written", OUT, "rows:", rows)
