"""Write README.md from qb_epa_2026.csv and qb_epa_2026_nongarbage.csv."""
import sys

import pandas as pd

WEEK = sys.argv[1] if len(sys.argv) > 1 else "?"
THROUGH = sys.argv[2] if len(sys.argv) > 2 else "?"

d = pd.read_csv("qb_epa_2026.csv")
n = pd.read_csv("qb_epa_2026_nongarbage.csv")

t = d[["rank", "qb", "team", "conf", "games", "db_plays", "rush_plays", "tot_plays",
       "db_epa_per", "rush_epa_per", "tot_epa_per", "tot_success", "tot_epa_per_nongarbage"]].copy()
t["rush_plays"] = t["rush_plays"].astype(int)
t.columns = ["#", "QB", "Team", "Conf", "G", "Dropbacks", "Rushes", "Plays", "EPA/dropback",
             "EPA/rush", "EPA/play", "Success", "EPA/play (WP 10–90%)"]

g = n[["rank", "overall_rank", "qb", "team", "conf", "ng_plays", "tot_epa_per_nongarbage",
       "ng_success", "tot_epa_per"]].copy()
g["ng_plays"] = g["ng_plays"].astype(int)
g.columns = ["#", "Overall #", "QB", "Team", "Conf", "Plays (WP 10–90%)",
             "EPA/play (WP 10–90%)", "Success (WP 10–90%)", "EPA/play (all)"]

md = f"""# 2026 CFB QB EPA — through Week {WEEK}

FBS offenses, games through {THROUGH} (Week 0 games are folded into Week 1).
**Minimum 60 dropbacks**, which leaves {len(d)} QBs. Sorted by EPA/play over all dropbacks + QB rushes.

- **Dropbacks** = pass attempts + sacks. **Rushes** = designed runs + scrambles.
- **Success** = share of plays with positive EPA.
- **EPA/play (WP 10–90%)** leaves out garbage time.
- Not opponent-adjusted, so a team that has played FCS opponents looks better.
- Source: cfbfastR play-by-play (`sportsdataverse/cfbfastR-data`, `data/rds/pbp_players_pos_2026.rds`). Rebuild with `python qb_epa.py <rds> [min_dropbacks]` then `python make_readme.py <week> "<through date>"`.

Full tables: [`qb_epa_2026.csv`](qb_epa_2026.csv), [`qb_epa_2026_nongarbage.csv`](qb_epa_2026_nongarbage.csv)

## Non-garbage time (win probability 10–90%)

Same 60-dropback pool, plus at least 40 plays in competitive game states ({len(n)} QBs).

{g.to_markdown(index=False, floatfmt='.3f')}

## All plays

{t.to_markdown(index=False, floatfmt='.3f')}
"""
open("README.md", "w").write(md)
