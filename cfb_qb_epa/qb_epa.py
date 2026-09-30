"""2026 college football QB EPA leaderboard (FBS offenses).

Source: cfbfastR play-by-play with EPA (sportsdataverse/cfbfastR-data,
data/rds/pbp_players_pos_2026.rds).

Usage: python qb_epa.py [path/to/pbp_players_pos_2026.rds] [min_dropbacks]
"""
import re
import sys

import pandas as pd
import pyreadr

PBP = sys.argv[1] if len(sys.argv) > 1 else "pbp_players_pos_2026.rds"
MIN_DROPBACKS = int(sys.argv[2]) if len(sys.argv) > 2 else 60
MIN_NG_PLAYS = 40

FBS = {"ACC", "Big Ten", "Big 12", "SEC", "Pac-12", "American Athletic",
       "Mountain West", "Sun Belt", "Mid-American", "Conference USA",
       "FBS Independents"}

df = next(iter(pyreadr.read_r(PBP).values()))
df = df[df["EPA"].notna() & df["offense_conference"].isin(FBS)]

# Passer id/name from the stat-attribution columns; passer_player_name is
# unreliable (raw play-text fragments, blank on most passing TDs).
pb = df[df["pass"] == 1].copy()
pb["qb_id"] = pd.NA
pb["qb"] = pd.NA
for role in ["completion", "incompletion", "interception_thrown", "sack_taken"]:
    pb["qb_id"] = pb["qb_id"].fillna(pb[f"{role}_player_id"])
    pb["qb"] = pb["qb"].fillna(pb[f"{role}_player"])

# Fill remaining gaps from other plays in the same game with the same raw passer text.
known = (pb.dropna(subset=["qb_id", "passer_player_name"])
           .drop_duplicates(["game_id", "pos_team", "passer_player_name"])
           .set_index(["game_id", "pos_team", "passer_player_name"])[["qb_id", "qb"]])
miss = pb["qb_id"].isna()
filled = pb.loc[miss, ["game_id", "pos_team", "passer_player_name"]].join(
    known, on=["game_id", "pos_team", "passer_player_name"])
pb.loc[miss, ["qb_id", "qb"]] = filled[["qb_id", "qb"]].values


# Some games have no stat-attribution columns at all. Fall back to matching the
# player named in the play text ("#1 N.Kim pass ...", "Noah Kim run ...") to a
# player credited elsewhere for the same team, keyed on first initial + last name.
SUFFIXES = {"jr", "sr", "ii", "iii", "iv"}


def play_name(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"(?:#\d+\s+)?([A-Z][\w'.\-]*(?:[ .][A-Z][\w'\-]*)*\.?)\s+"
                  r"(?:pass|sacked|run|rush|scramble)", text)
    return m.group(1) if m else None


def short_key(text):
    name = play_name(text)
    if not name:
        return None
    parts = [p for p in re.split(r"[ .]+", name.lower().strip(".")) if p]
    while len(parts) > 2 and parts[-1] in SUFFIXES:
        parts.pop()
    return f"{parts[0][0]}.{parts[-1]}" if len(parts) > 1 else None


def fill_by_name(rows, id_col, name_col, key_text):
    rows[id_col] = rows[id_col].astype(object)
    key = key_text.map(short_key)
    lookup = pd.DataFrame({"team": rows["pos_team"], "key": key,
                           "id": rows[id_col], "name": rows[name_col]}).dropna()
    lookup = lookup.groupby(["team", "key"]).filter(lambda g: g["id"].nunique() == 1)
    lookup = lookup.drop_duplicates(["team", "key"]).set_index(["team", "key"])
    miss = rows[id_col].isna() & key.notna()
    hit = pd.DataFrame({"team": rows.loc[miss, "pos_team"], "key": key[miss]}).join(
        lookup, on=["team", "key"])
    rows.loc[miss, [id_col, name_col]] = hit[["id", "name"]].values
    # Players never credited anywhere: synthetic team+name id, name as in play text.
    rest = rows[id_col].isna() & key.notna()
    rows.loc[rest, id_col] = rows.loc[rest, "pos_team"] + ":" + key[rest]
    rows.loc[rest, name_col] = key_text[rest].map(play_name)


fill_by_name(pb, "qb_id", "qb", pb["play_text"])
unattributed = pb["qb_id"].isna().sum()
pb = pb.dropna(subset=["qb_id"])

# QB rushes (designed runs + scrambles) by anyone who threw a pass.
ru = df[df["rush"] == 1].copy()
fill_by_name(ru, "rush_player_id", "rush_player", ru["play_text"])
ru = ru[ru["rush_player_id"].isin(pb["qb_id"].unique())]
ru["qb_id"] = ru["rush_player_id"]
ru["qb"] = ru["rush_player"]

nongarbage = lambda d: d["wp_before"].between(0.1, 0.9)

def summarize(d, prefix):
    g = d.groupby(["qb_id", "pos_team"])
    return pd.DataFrame({
        f"{prefix}plays": g.size(),
        f"{prefix}epa": g["EPA"].sum(),
        f"{prefix}epa_per": g["EPA"].mean(),
        f"{prefix}success": g["epa_success"].mean(),
    })

names = pd.concat([pb, ru]).groupby(["qb_id", "pos_team"]).agg(
    qb=("qb", "first"), conf=("offense_conference", "first"),
    games=("game_id", "nunique"))
out = names.join([summarize(pb, "db_"), summarize(ru, "rush_"),
                  summarize(pd.concat([pb, ru]), "tot_")])
ng = pd.concat([pb, ru])
ng = ng[nongarbage(ng)].groupby(["qb_id", "pos_team"])
out["ng_plays"] = ng.size()
out["tot_epa_per_nongarbage"] = ng["EPA"].mean()
out["ng_success"] = ng["epa_success"].mean()
out = out.fillna({"rush_plays": 0, "rush_epa": 0, "ng_plays": 0})
out = out[out["db_plays"] >= MIN_DROPBACKS].sort_values("tot_epa_per", ascending=False)
out = out.reset_index().rename(columns={"pos_team": "team"})
out.insert(0, "rank", range(1, len(out) + 1))

cols = ["rank", "qb", "team", "conf", "games", "db_plays", "db_epa_per", "db_success",
        "rush_plays", "rush_epa_per", "tot_plays", "tot_epa", "tot_epa_per",
        "tot_success", "ng_plays", "tot_epa_per_nongarbage", "ng_success"]
out = out[cols].round(3)
out.to_csv("qb_epa_2026.csv", index=False)

# Non-garbage-time ranking (win probability 10-90%), same dropback minimum
# plus enough competitive-game snaps to be meaningful.
ng_out = (out[out["ng_plays"] >= MIN_NG_PLAYS]
          .sort_values("tot_epa_per_nongarbage", ascending=False)
          .rename(columns={"rank": "overall_rank"}))
ng_out.insert(0, "rank", range(1, len(ng_out) + 1))
ng_out.to_csv("qb_epa_2026_nongarbage.csv", index=False)
weeks = sorted(df["week"].unique())
print(f"weeks {weeks}, min {MIN_DROPBACKS} dropbacks, {len(out)} QBs, "
      f"{unattributed} dropbacks unattributed")
print(out.to_string(index=False))
