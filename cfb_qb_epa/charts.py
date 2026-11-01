"""Build team_net_epa_2026.csv and the four phone-sized top-25 charts.

Reads qb_epa_2026_nongarbage.csv, team_off_epa_2026.csv and
team_def_epa_2026.csv (run qb_epa.py and team_epa.py first). Writes
top25_qb.png, top25_offense.png, top25_defense.png and top25_net.png.

Usage: python charts.py
"""
import glob
import html

import pandas as pd
from playwright.sync_api import sync_playwright

SHORT = {"North Dakota State": "North Dakota St.", "Florida International": "FIU",
         "Massachusetts": "UMass"}
HIGHLIGHT_TEAM = "Michigan"
HIGHLIGHT_QB = "Bryce Underwood"

CSS = """*{box-sizing:border-box;margin:0;padding:0}
body{background:#1a1a19;font-family:-apple-system,'Helvetica Neue',Helvetica,Arial,sans-serif;color:#fff}
#card{width:390px;padding:24px 18px 18px;background:#1a1a19}
h1{font-size:22px;font-weight:800;letter-spacing:-.3px}
.sub{font-size:12.5px;color:#c3c2b7;margin-top:5px;line-height:1.4}
.rows{margin-top:16px}
.row{display:grid;grid-template-columns:22px 118px 1fr;align-items:center;height:25px;column-gap:8px}
.row.two{height:36px;grid-template-columns:22px 140px 1fr}
.rk{font-size:12px;color:#8f8e86;text-align:right;font-variant-numeric:tabular-nums}
.tm{font-size:13.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tm small{display:block;font-size:11px;font-weight:400;color:#c3c2b7;margin-top:1px}
.bw{display:flex;align-items:center;gap:7px}
.bar{height:13px;border-radius:0 4px 4px 0}
.v{font-size:12.5px;font-weight:600;color:#fff;font-variant-numeric:tabular-nums}
.sep{border-top:1px dashed #3a3a37;margin:8px 0 6px}"""


def chrome():
    found = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))
    return found[-1] if found else None


def card(rows, extra, title, sub, color, key, out, name="team", label=None):
    mx = max(abs(r[key]) for r in rows + extra)

    def row(r):
        w = abs(r[key]) / mx * 70
        nm = html.escape(SHORT.get(r[name], r[name]))
        if label:
            nm += f"<small>{html.escape(r[label])}</small>"
        return (f'<div class="row{" two" if label else ""}"><div class=rk>{r["rank"]}</div>'
                f'<div class=tm>{nm}</div>'
                f'<div class=bw><div class=bar style="width:{w:.1f}%;background:{color}"></div>'
                f'<span class=v>{r[key]:+.3f}</span></div></div>')

    body = "".join(row(r) for r in rows)
    if extra:
        body += "<div class=sep></div>" + "".join(row(r) for r in extra)
    page = (f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>"
            f"<div id=card><h1>{title}</h1><div class=sub>{sub}</div>"
            f"<div class=rows>{body}</div></div></body></html>")
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=chrome())
        pg = b.new_page(viewport={"width": 390, "height": 900}, device_scale_factor=3)
        pg.set_content(page)
        pg.locator("#card").screenshot(path=out)
        b.close()


off = pd.read_csv("team_off_epa_2026.csv")
dfn = pd.read_csv("team_def_epa_2026.csv")
net = (off[["team", "conf", "ng_epa_per", "rank"]].rename(columns={"rank": "off_rank"})
       .merge(dfn[["team", "ng_epa_allowed", "rank"]].rename(columns={"rank": "def_rank"}), on="team"))
net["net"] = (net["ng_epa_per"] - net["ng_epa_allowed"]).round(3)
net = net.sort_values("net", ascending=False).reset_index(drop=True)
net.insert(0, "rank", range(1, len(net) + 1))
net.to_csv("team_net_epa_2026.csv", index=False)

qb = pd.read_csv("qb_epa_2026_nongarbage.csv").to_dict("records")
o, d, n = (t.to_dict("records") for t in (off, dfn, net))
below = lambda rows, col, who: [r for r in rows if r[col] == who and r["rank"] > 25]

card(qb[:25], below(qb, "qb", HIGHLIGHT_QB), "Top 25 QBs", "EPA per play · garbage time removed",
     "#3987e5", "tot_epa_per_nongarbage", "top25_qb.png", name="qb", label="team")
card(o[:25], below(o, "team", HIGHLIGHT_TEAM), "Top 25 Offenses", "EPA per play · higher is better",
     "#3987e5", "ng_epa_per", "top25_offense.png")
card(d[:25], below(d, "team", HIGHLIGHT_TEAM), "Top 25 Defenses", "EPA allowed per play · lower is better",
     "#d95926", "ng_epa_allowed", "top25_defense.png")
card(n[:25], below(n, "team", HIGHLIGHT_TEAM), "Top 25 Net EPA",
     "Offense EPA/play minus defense EPA allowed · garbage time removed",
     "#199e70", "net", "top25_net.png")
