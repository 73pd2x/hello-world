"""2026 FBS team offensive EPA (all pass + rush plays) from cfbfastR play-by-play.

Usage: python team_epa.py [path/to/pbp_players_pos_2026.rds]
"""
import sys

import pandas as pd
import pyreadr

PBP = sys.argv[1] if len(sys.argv) > 1 else "pbp_players_pos_2026.rds"
FBS = {"ACC", "Big Ten", "Big 12", "SEC", "Pac-12", "American Athletic",
       "Mountain West", "Sun Belt", "Mid-American", "Conference USA",
       "FBS Independents"}

df = next(iter(pyreadr.read_r(PBP).values()))
df = df[df["EPA"].notna() & df["offense_conference"].isin(FBS)
        & ((df["pass"] == 1) | (df["rush"] == 1))]
ng = df[df["wp_before"].between(0.1, 0.9)]

g, gn = df.groupby("pos_team"), ng.groupby("pos_team")
out = pd.DataFrame({
    "conf": g["offense_conference"].first(),
    "games": g["game_id"].nunique(),
    "plays": g.size(),
    "epa_per": g["EPA"].mean(),
    "success": g["epa_success"].mean(),
    "pass_epa_per": df[df["pass"] == 1].groupby("pos_team")["EPA"].mean(),
    "rush_epa_per": df[df["rush"] == 1].groupby("pos_team")["EPA"].mean(),
    "ng_plays": gn.size(),
    "ng_epa_per": gn["EPA"].mean(),
    "ng_success": gn["epa_success"].mean(),
    "ng_pass_epa_per": ng[ng["pass"] == 1].groupby("pos_team")["EPA"].mean(),
    "ng_rush_epa_per": ng[ng["rush"] == 1].groupby("pos_team")["EPA"].mean(),
}).fillna({"ng_plays": 0})
out = out.sort_values("ng_epa_per", ascending=False).round(3)
out.insert(0, "rank", range(1, len(out) + 1))
out = out.reset_index().rename(columns={"pos_team": "team"})
out.to_csv("team_off_epa_2026.csv", index=False)
print(out.to_string(index=False))

# Defense: EPA allowed per play (lower is better), garbage time removed.
dd = next(iter(pyreadr.read_r(PBP).values()))
dd = dd[dd["EPA"].notna() & dd["defense_conference"].isin(FBS)
        & ((dd["pass"] == 1) | (dd["rush"] == 1))
        & dd["wp_before"].between(0.1, 0.9)]
gd = dd.groupby("def_pos_team")
dout = pd.DataFrame({
    "conf": gd["defense_conference"].first(),
    "games": gd["game_id"].nunique(),
    "ng_plays": gd.size(),
    "ng_epa_allowed": gd["EPA"].mean(),
    "ng_success_allowed": gd["epa_success"].mean(),
    "ng_pass_epa_allowed": dd[dd["pass"] == 1].groupby("def_pos_team")["EPA"].mean(),
    "ng_rush_epa_allowed": dd[dd["rush"] == 1].groupby("def_pos_team")["EPA"].mean(),
}).sort_values("ng_epa_allowed").round(3)
dout.insert(0, "rank", range(1, len(dout) + 1))
dout.reset_index().rename(columns={"def_pos_team": "team"}).to_csv("team_def_epa_2026.csv", index=False)
