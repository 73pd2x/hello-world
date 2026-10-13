"""Opponent-adjusted team EPA/play (garbage time removed) via ridge regression.

Each competitive play's EPA = intercept + offense[team] + defense[opponent]
+ home-field term. Ridge shrinkage keeps small samples near average. All
teams in the data (FBS, FCS and below) are fit together so games against
lower-division opponents are adjusted rather than dropped; only FBS teams
are written out.

Usage: python opp_adjust.py [path/to/pbp_players_pos_2026.rds] [lambda]
"""
import sys

import numpy as np
import pandas as pd
import pyreadr

PBP = sys.argv[1] if len(sys.argv) > 1 else "pbp_players_pos_2026.rds"
LAMBDA = float(sys.argv[2]) if len(sys.argv) > 2 else 150.0
# Home field is fixed rather than fit: teams host their weakest opponents, so a
# fitted term soaks up schedule strength (conference games alone show ~0).
# 0.02 EPA/play per side is ~2.5-3 points over a game.
HOME_EPA = 0.02
FBS = {"ACC", "Big Ten", "Big 12", "SEC", "Pac-12", "American Athletic",
       "Mountain West", "Sun Belt", "Mid-American", "Conference USA",
       "FBS Independents"}


def fit(df, fbs_teams):
    teams = pd.Index(sorted(set(df["pos_team"]) | set(df["def_pos_team"])))
    n = len(teams)
    off = teams.get_indexer(df["pos_team"])
    dfn = n + teams.get_indexer(df["def_pos_team"])
    home = np.where(df["neutral_site"].fillna(False).astype(bool), 0.0,
                    np.where(df["pos_team"] == df["home"], 1.0, -1.0))
    y = df["EPA"].to_numpy() - HOME_EPA * home
    y = y - y.mean()

    # Dense columns: offense/defense from below FBS. The
    # division terms are unshrunk so a lower-division team with one or two
    # games is pulled toward its division's level, not the overall average
    # (otherwise the FBS/FCS gap is understated).
    dense = np.column_stack([(~df["pos_team"].isin(fbs_teams)).astype(float),
                             (~df["def_pos_team"].isin(fbs_teams)).astype(float)])
    m = dense.shape[1]

    # Normal equations from index arrays: each row has one offense, one
    # defense and the dense terms.
    k = 2 * n + m
    xtx = np.zeros((k, k))
    np.add.at(xtx, (off, off), 1.0)
    np.add.at(xtx, (dfn, dfn), 1.0)
    np.add.at(xtx, (off, dfn), 1.0)
    np.add.at(xtx, (dfn, off), 1.0)
    for j in range(m):
        c = 2 * n + j
        np.add.at(xtx, (off, c), dense[:, j])
        np.add.at(xtx, (dfn, c), dense[:, j])
        xtx[c, :2 * n] = xtx[:2 * n, c]
    xtx[2 * n:, 2 * n:] = dense.T @ dense
    xty = np.zeros(k)
    np.add.at(xty, off, y)
    np.add.at(xty, dfn, y)
    xty[2 * n:] = dense.T @ y

    pen = np.full(k, LAMBDA)
    pen[2 * n:] = 0.0  # division terms are not shrunk
    b = np.linalg.solve(xtx + np.diag(pen), xty)
    return (pd.DataFrame({"adj_off": b[:n], "adj_def": b[n:2 * n]}, index=teams),
            dict(zip(["nonfbs_off", "nonfbs_def"], b[2 * n:])))


raw = next(iter(pyreadr.read_r(PBP).values()))
plays = raw[raw["EPA"].notna() & ((raw["pass"] == 1) | (raw["rush"] == 1))
            & raw["wp_before"].between(0.1, 0.9)]

conf = pd.concat([
    plays[["pos_team", "offense_conference"]].set_axis(["team", "conf"], axis=1),
    plays[["def_pos_team", "defense_conference"]].set_axis(["team", "conf"], axis=1),
]).dropna().groupby("team")["conf"].agg(lambda s: s.mode().iat[0])
fbs_teams = set(conf[conf.isin(FBS)].index)

all_fit, terms = fit(plays, fbs_teams)
pass_fit, _ = fit(plays[plays["pass"] == 1], fbs_teams)
rush_fit, _ = fit(plays[plays["rush"] == 1], fbs_teams)

out = all_fit.join(pass_fit.add_prefix("pass_")).join(rush_fit.add_prefix("rush_"))
out["conf"] = conf
out = out[out["conf"].isin(FBS)].copy()
out["adj_net"] = out["adj_off"] - out["adj_def"]
for c in ["adj_off", "pass_adj_off", "rush_adj_off", "adj_net"]:
    out[c.replace("adj_", "rank_")] = out[c].rank(ascending=False, method="min").astype(int)
for c in ["adj_def", "pass_adj_def", "rush_adj_def"]:
    out[c.replace("adj_", "rank_")] = out[c].rank(method="min").astype(int)
out = out.sort_values("adj_net", ascending=False).round(3)
out.index.name = "team"
out.to_csv("team_adj_epa_2026.csv")
print(f"{len(plays)} plays, lambda {LAMBDA}, " + ", ".join(f"{k} {v:+.3f}" for k, v in terms.items()))
print(out[["conf", "adj_net", "rank_net", "adj_off", "rank_off", "adj_def", "rank_def"]]
      .head(30).to_string())
