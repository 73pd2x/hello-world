# 2026 CFB QB EPA — through Week 9

FBS offenses, games through Oct 31, 2026 (Week 0 games are folded into Week 1).
**Minimum 60 dropbacks**, which leaves 179 QBs. Sorted by EPA/play over all dropbacks + QB rushes.

- **Dropbacks** = pass attempts + sacks. **Rushes** = designed runs + scrambles.
- **Success** = share of plays with positive EPA.
- **EPA/play (WP 10–90%)** leaves out garbage time.
- Not opponent-adjusted, so a team that has played FCS opponents looks better.
- Source: cfbfastR play-by-play (`sportsdataverse/cfbfastR-data`, `data/rds/pbp_players_pos_2026.rds`). Rebuild with `python qb_epa.py <rds> [min_dropbacks]` then `python make_readme.py <week> "<through date>"`.

Full tables: [`qb_epa_2026.csv`](qb_epa_2026.csv), [`qb_epa_2026_nongarbage.csv`](qb_epa_2026_nongarbage.csv)

## Non-garbage time (win probability 10–90%)

Same 60-dropback pool, plus at least 40 plays in competitive game states (169 QBs).

|   # |   Overall # | QB                       | Team                  | Conf              |   Plays (WP 10–90%) |   EPA/play (WP 10–90%) |   Success (WP 10–90%) |   EPA/play (all) |
|----:|------------:|:-------------------------|:----------------------|:------------------|--------------------:|-----------------------:|----------------------:|-----------------:|
|   1 |           1 | David McComb             | Miami (OH)            | Mid-American      |                  73 |                  0.676 |                 0.562 |            0.570 |
|   2 |           4 | Giovanni Lopez           | Wake Forest           | ACC               |                 166 |                  0.572 |                 0.572 |            0.429 |
|   3 |           2 | Darian Mensah            | Miami                 | ACC               |                 157 |                  0.563 |                 0.592 |            0.518 |
|   4 |           5 | Julian Sayin             | Ohio State            | Big Ten           |                 139 |                  0.508 |                 0.568 |            0.416 |
|   5 |           3 | Tayven Jackson           | North Texas           | American Athletic |                 206 |                  0.492 |                 0.568 |            0.459 |
|   6 |          19 | Bishop Davenport         | South Alabama         | Sun Belt          |                  59 |                  0.413 |                 0.525 |            0.307 |
|   7 |          16 | Jayden Maiava            | USC                   | Big Ten           |                 239 |                  0.376 |                 0.548 |            0.325 |
|   8 |          26 | Michael Hawkins Jr.      | West Virginia         | Big 12            |                 240 |                  0.366 |                 0.462 |            0.285 |
|   9 |          43 | Devon Dampier            | Utah                  | Big 12            |                 176 |                  0.363 |                 0.585 |            0.237 |
|  10 |           8 | Hauss Hejny              | Colorado State        | Pac-12            |                  98 |                  0.359 |                 0.561 |            0.366 |
|  11 |          24 | Marcus Stokes            | Memphis               | American Athletic |                 226 |                  0.354 |                 0.527 |            0.290 |
|  12 |           9 | Lincoln Kienholz         | Louisville            | ACC               |                 243 |                  0.342 |                 0.531 |            0.358 |
|  13 |          34 | Cameran Brown            | Georgia State         | Sun Belt          |                 118 |                  0.340 |                 0.568 |            0.270 |
|  14 |          23 | Keelon Russell           | Alabama               | SEC               |                 205 |                  0.339 |                 0.512 |            0.291 |
|  15 |          22 | John Alan Richter        | Toledo                | Mid-American      |                 182 |                  0.339 |                 0.505 |            0.294 |
|  16 |          75 | Matt Vezza               | Ohio                  | Mid-American      |                  82 |                  0.337 |                 0.549 |            0.139 |
|  17 |          13 | Avery Johnson            | Kansas State          | Big 12            |                 153 |                  0.336 |                 0.503 |            0.334 |
|  18 |           6 | Jackson Gutierrez        | Navy                  | American Athletic |                 192 |                  0.317 |                 0.516 |            0.386 |
|  19 |          14 | Kevin Jennings           | SMU                   | ACC               |                 254 |                  0.316 |                 0.543 |            0.333 |
|  20 |          11 | Aidan Chiles             | Northwestern          | Big Ten           |                 193 |                  0.315 |                 0.513 |            0.344 |
|  21 |          10 | Caden Veltkamp           | Florida Atlantic      | American Athletic |                 221 |                  0.312 |                 0.516 |            0.353 |
|  22 |          28 | Cale Hellums             | Army                  | American Athletic |                 192 |                  0.306 |                 0.526 |            0.278 |
|  23 |          20 | Mason Heintschel         | Pittsburgh            | ACC               |                  87 |                  0.305 |                 0.437 |            0.299 |
|  24 |          21 | Noah Fifita              | Arizona               | Big 12            |                 210 |                  0.303 |                 0.529 |            0.296 |
|  25 |          12 | C.J. Carr                | Notre Dame            | FBS Independents  |                 164 |                  0.299 |                 0.506 |            0.340 |
|  26 |          39 | Ajani Sheppard           | Temple                | American Athletic |                 174 |                  0.292 |                 0.471 |            0.250 |
|  27 |          53 | Gunner Stockton          | Georgia               | SEC               |                 140 |                  0.292 |                 0.536 |            0.204 |
|  28 |          45 | Katin Houser             | Illinois              | Big Ten           |                 168 |                  0.288 |                 0.536 |            0.221 |
|  29 |          32 | Austin Simmons           | Missouri              | SEC               |                 190 |                  0.287 |                 0.474 |            0.273 |
|  30 |          61 | Conner Harrell           | Charlotte             | American Athletic |                  86 |                  0.286 |                 0.488 |            0.166 |
|  31 |          42 | Bear Bachmeier           | BYU                   | Big 12            |                 221 |                  0.285 |                 0.520 |            0.245 |
|  32 |          25 | Maddux Madsen            | Boise State           | Pac-12            |                 205 |                  0.284 |                 0.517 |            0.287 |
|  33 |          40 | Dylan Lonergan           | Rutgers               | Big Ten           |                  92 |                  0.284 |                 0.511 |            0.249 |
|  34 |          18 | Conner Weigman           | Houston               | Big 12            |                 226 |                  0.283 |                 0.535 |            0.309 |
|  35 |          57 | Henry Belin IV           | Missouri State        | Conference USA    |                  99 |                  0.281 |                 0.505 |            0.175 |
|  36 |          48 | Trinidad Chambliss       | Ole Miss              | SEC               |                 229 |                  0.276 |                 0.533 |            0.213 |
|  37 |          54 | William Watson III       | Massachusetts         | Mid-American      |                  96 |                  0.275 |                 0.448 |            0.201 |
|  38 |          36 | CJ Bailey                | NC State              | ACC               |                 173 |                  0.273 |                 0.474 |            0.257 |
|  39 |          17 | Drew Mestemaker          | Oklahoma State        | Big 12            |                 238 |                  0.268 |                 0.513 |            0.317 |
|  40 |          59 | Owen McCown              | UTSA                  | American Athletic |                 228 |                  0.264 |                 0.487 |            0.173 |
|  41 |          33 | Kamario Taylor           | Mississippi State     | SEC               |                 132 |                  0.262 |                 0.515 |            0.272 |
|  42 |          35 | Aaron Philo              | Florida               | SEC               |                 132 |                  0.259 |                 0.553 |            0.269 |
|  43 |          31 | Nick Minicucci           | Delaware              | Conference USA    |                 136 |                  0.259 |                 0.493 |            0.273 |
|  44 |          80 | McCae Hillstead          | Utah State            | Pac-12            |                  52 |                  0.256 |                 0.519 |            0.129 |
|  45 |          50 | Blake Baker              | Louisiana Tech        | Sun Belt          |                 129 |                  0.256 |                 0.473 |            0.209 |
|  46 |          44 | Trey Owens               | Arkansas State        | Sun Belt          |                 224 |                  0.252 |                 0.545 |            0.227 |
|  47 |          56 | Jared Hollins            | South Alabama         | Sun Belt          |                 131 |                  0.252 |                 0.443 |            0.182 |
|  48 |          41 | JC French                | Cincinnati            | Big 12            |                 202 |                  0.249 |                 0.535 |            0.249 |
|  49 |          37 | Ashton Daniels           | Florida State         | ACC               |                 194 |                  0.246 |                 0.459 |            0.252 |
|  50 |          27 | Sam Leavitt              | LSU                   | SEC               |                 183 |                  0.245 |                 0.530 |            0.280 |
|  51 |          38 | Caden Creel              | Jacksonville State    | Conference USA    |                 272 |                  0.245 |                 0.496 |            0.251 |
|  52 |          63 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |                 221 |                  0.221 |                 0.498 |            0.163 |
|  53 |          89 | Keldric Luster           | Ball State            | Mid-American      |                 124 |                  0.220 |                 0.476 |            0.107 |
|  54 |          60 | Kalieb Osborne           | UConn                 | FBS Independents  |                 194 |                  0.218 |                 0.479 |            0.169 |
|  55 |          94 | Davis Warren             | Stanford              | ACC               |                 193 |                  0.213 |                 0.430 |            0.096 |
|  56 |          47 | Lanorris Sellers         | South Carolina        | SEC               |                 213 |                  0.207 |                 0.484 |            0.216 |
|  57 |          29 | Braden Atkinson          | Oregon State          | Pac-12            |                 179 |                  0.202 |                 0.497 |            0.277 |
|  58 |          68 | Ryan Browne              | Purdue                | Big Ten           |                 210 |                  0.199 |                 0.500 |            0.154 |
|  59 |          86 | Nathan Hayes             | North Dakota State    | Mountain West     |                 201 |                  0.197 |                 0.468 |            0.111 |
|  60 |          15 | Brad Jackson             | Texas State           | Pac-12            |                 226 |                  0.196 |                 0.478 |            0.328 |
|  61 |          52 | Dante Moore              | Oregon                | Big Ten           |                  87 |                  0.191 |                 0.402 |            0.205 |
|  62 |          65 | Jaylen Raynor            | Iowa State            | Big 12            |                 155 |                  0.182 |                 0.452 |            0.162 |
|  63 |          30 | Tommy Carr               | Michigan              | Big Ten           |                  86 |                  0.180 |                 0.500 |            0.273 |
|  64 |         113 | Ty Dieffenbach           | UCLA                  | Big Ten           |                  81 |                  0.173 |                 0.395 |            0.059 |
|  65 |          67 | Jayden Mandal            | Fresno State          | Pac-12            |                 191 |                  0.170 |                 0.476 |            0.160 |
|  66 |          87 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |                 207 |                  0.170 |                 0.435 |            0.111 |
|  67 |          81 | Jackson Arnold           | UNLV                  | Mountain West     |                 263 |                  0.170 |                 0.471 |            0.128 |
|  68 |          73 | Billy Edwards            | North Carolina        | ACC               |                 237 |                  0.167 |                 0.527 |            0.140 |
|  69 |          84 | Will Hammond             | Texas Tech            | Big 12            |                 149 |                  0.166 |                 0.497 |            0.117 |
|  70 |          90 | Malachi Nelson           | Syracuse              | ACC               |                  72 |                  0.164 |                 0.500 |            0.106 |
|  71 |          51 | Walker Eget              | Duke                  | ACC               |                 193 |                  0.156 |                 0.451 |            0.205 |
|  72 |          83 | Bryce Underwood          | Michigan              | Big Ten           |                 168 |                  0.154 |                 0.494 |            0.122 |
|  73 |          99 | Trace Johnson            | Tulane                | American Athletic |                  89 |                  0.152 |                 0.494 |            0.087 |
|  74 |          88 | Max Johnson              | Georgia Southern      | Sun Belt          |                 210 |                  0.149 |                 0.476 |            0.110 |
|  75 |          66 | Isaiah Marshall          | Kansas                | Big 12            |                 200 |                  0.148 |                 0.430 |            0.161 |
|  76 |          98 | Camden Coleman           | James Madison         | Sun Belt          |                 169 |                  0.144 |                 0.450 |            0.088 |
|  77 |          69 | Baylor Hayes             | Tulsa                 | American Athletic |                 207 |                  0.141 |                 0.411 |            0.151 |
|  78 |         139 | Broc Lowry               | Western Michigan      | Mid-American      |                 187 |                  0.130 |                 0.481 |           -0.008 |
|  79 |          46 | Anthony Colandrea        | Nebraska              | Big Ten           |                 221 |                  0.130 |                 0.448 |            0.220 |
|  80 |         106 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |                 211 |                  0.117 |                 0.483 |            0.079 |
|  81 |          74 | Malachi Singleton        | App State             | Sun Belt          |                 192 |                  0.116 |                 0.453 |            0.139 |
|  82 |          49 | Josh Hoover              | Indiana               | Big Ten           |                 187 |                  0.112 |                 0.449 |            0.209 |
|  83 |          55 | Jared Curtis             | Vanderbilt            | SEC               |                 188 |                  0.111 |                 0.457 |            0.190 |
|  84 |         108 | Isaac Wilson             | Colorado              | Big 12            |                 146 |                  0.108 |                 0.459 |            0.070 |
|  85 |         120 | Mason McKenzie           | Boston College        | ACC               |                 218 |                  0.108 |                 0.427 |            0.044 |
|  86 |          76 | Rocco Becht              | Penn State            | Big Ten           |                 190 |                  0.107 |                 0.442 |            0.133 |
|  87 |         132 | Roman Gagliano           | Middle Tennessee      | Conference USA    |                 246 |                  0.097 |                 0.467 |            0.016 |
|  88 |          85 | Aidan Armenta            | UL Monroe             | Sun Belt          |                  88 |                  0.079 |                 0.375 |            0.113 |
|  89 |          92 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |                  48 |                  0.077 |                 0.458 |            0.103 |
|  90 |          96 | Steven Angeli            | Syracuse              | ACC               |                 154 |                  0.077 |                 0.416 |            0.094 |
|  91 |         118 | Jay Kastantin            | Bowling Green         | Mid-American      |                 215 |                  0.077 |                 0.433 |            0.053 |
|  92 |         121 | Angel H Flores           | Central Michigan      | Mid-American      |                 117 |                  0.076 |                 0.419 |            0.038 |
|  93 |         110 | Beau Pribula             | Virginia              | ACC               |                 197 |                  0.072 |                 0.431 |            0.066 |
|  94 |          97 | Kenny Minchey            | Kentucky              | SEC               |                 219 |                  0.070 |                 0.484 |            0.089 |
|  95 |         123 | Zion Turner              | Marshall              | Sun Belt          |                  72 |                  0.066 |                 0.403 |            0.031 |
|  96 |         137 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |                 161 |                  0.066 |                 0.460 |           -0.002 |
|  97 |          77 | Deshawn Purdie           | Liberty               | Conference USA    |                 137 |                  0.062 |                 0.438 |            0.132 |
|  98 |          62 | Dylan Raiola             | Oregon                | Big Ten           |                 125 |                  0.062 |                 0.384 |            0.165 |
|  99 |          82 | Colton Joseph            | Wisconsin             | Big Ten           |                 155 |                  0.058 |                 0.413 |            0.124 |
| 100 |         117 | Keyone Jenkins           | UCF                   | Big 12            |                 175 |                  0.056 |                 0.457 |            0.054 |
| 101 |         103 | Tyler Hughes             | Wyoming               | Mountain West     |                 198 |                  0.055 |                 0.449 |            0.080 |
| 102 |         111 | Trey Hedden              | New Mexico State      | Conference USA    |                  93 |                  0.053 |                 0.398 |            0.064 |
| 103 |         124 | Julian Lewis             | Colorado              | Big 12            |                  63 |                  0.052 |                 0.365 |            0.029 |
| 104 |          93 | Taron Dickens            | Northern Illinois     | Mountain West     |                 162 |                  0.051 |                 0.469 |            0.103 |
| 105 |         116 | Micah Alejado            | Hawai'i               | Mountain West     |                 315 |                  0.049 |                 0.429 |            0.054 |
| 106 |         112 | Rickie Collins           | Kennesaw State        | Conference USA    |                 220 |                  0.049 |                 0.459 |            0.063 |
| 107 |         101 | Demond Williams Jr.      | Washington            | Big Ten           |                 170 |                  0.048 |                 0.471 |            0.082 |
| 108 |          78 | Nick Poulos              | Ohio                  | Mid-American      |                  99 |                  0.045 |                 0.505 |            0.132 |
| 109 |         107 | D.J. Lagway              | Baylor                | Big 12            |                 213 |                  0.045 |                 0.427 |            0.073 |
| 110 |         102 | Cibastian Broughton      | Akron                 | Mid-American      |                  45 |                  0.044 |                 0.489 |            0.082 |
| 111 |         100 | Jaden Craig              | TCU                   | Big 12            |                 280 |                  0.041 |                 0.443 |            0.087 |
| 112 |          95 | Jacurri Brown            | Rice                  | American Athletic |                 142 |                  0.040 |                 0.430 |            0.094 |
| 113 |         125 | J.J. Kohl                | Florida International | Conference USA    |                 208 |                  0.039 |                 0.418 |            0.027 |
| 114 |         138 | Noah Kim                 | Eastern Michigan      | Mid-American      |                 196 |                  0.038 |                 0.439 |           -0.002 |
| 115 |         134 | Dru Deshields            | Kent State            | Mid-American      |                 222 |                  0.037 |                 0.383 |            0.004 |
| 116 |          91 | Hank Brown               | Iowa                  | Big Ten           |                 146 |                  0.036 |                 0.432 |            0.105 |
| 117 |         114 | Byrum Brown              | Auburn                | SEC               |                 263 |                  0.035 |                 0.407 |            0.058 |
| 118 |         127 | Malik Washington         | Maryland              | Big Ten           |                 189 |                  0.006 |                 0.429 |            0.026 |
| 119 |         126 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |                  67 |                  0.002 |                 0.418 |            0.027 |
| 120 |         144 | AJ Bianco                | Nevada                | Mountain West     |                  43 |                  0.002 |                 0.326 |           -0.024 |
| 121 |          58 | Stone Saunders           | San Diego State       | Pac-12            |                  52 |                  0.002 |                 0.365 |            0.175 |
| 122 |         109 | Luke Weaver              | San José State        | Mountain West     |                 242 |                  0.000 |                 0.467 |            0.069 |
| 123 |         115 | John Mateer              | Oklahoma              | SEC               |                 211 |                 -0.001 |                 0.431 |            0.056 |
| 124 |         135 | Nico Iamaleava           | UCLA                  | Big Ten           |                 132 |                 -0.006 |                 0.432 |            0.001 |
| 125 |         105 | Alberto Mendoza          | Georgia Tech          | ACC               |                 171 |                 -0.009 |                 0.480 |            0.079 |
| 126 |         136 | Skyler Locklear          | Missouri State        | Conference USA    |                 109 |                 -0.011 |                 0.385 |            0.001 |
| 127 |         161 | Tait Reynolds            | Clemson               | ACC               |                 235 |                 -0.014 |                 0.455 |           -0.065 |
| 128 |         143 | Brayden Roggow           | Akron                 | Mid-American      |                 128 |                 -0.014 |                 0.375 |           -0.015 |
| 129 |         140 | KJ Jackson               | Arkansas              | SEC               |                 174 |                 -0.016 |                 0.437 |           -0.008 |
| 130 |          70 | Owen Eshelman            | Washington State      | Pac-12            |                 100 |                 -0.028 |                 0.470 |            0.147 |
| 131 |         153 | Emory Williams           | East Carolina         | American Athletic |                 110 |                 -0.028 |                 0.391 |           -0.041 |
| 132 |         119 | Cutter Boley             | Arizona State         | Big 12            |                 120 |                 -0.033 |                 0.433 |            0.052 |
| 133 |         130 | Jackson Brousseau        | California            | ACC               |                  72 |                 -0.044 |                 0.403 |            0.019 |
| 134 |         159 | George MacIntyre         | Tennessee             | SEC               |                  99 |                 -0.044 |                 0.424 |           -0.065 |
| 135 |         142 | Arch Manning             | Texas                 | SEC               |                 177 |                 -0.047 |                 0.412 |           -0.014 |
| 136 |         133 | Brock Glenn              | Western Kentucky      | Conference USA    |                 143 |                 -0.050 |                 0.455 |            0.009 |
| 137 |         145 | M.Van Buren Jr.          | South Florida         | American Athletic |                 176 |                 -0.051 |                 0.443 |           -0.025 |
| 138 |         128 | Alessio Milivojevic      | Michigan State        | Big Ten           |                 148 |                 -0.058 |                 0.432 |            0.026 |
| 139 |         141 | Will Crowder             | Troy                  | Sun Belt          |                 153 |                 -0.058 |                 0.418 |           -0.011 |
| 140 |         152 | Quinn Henicle            | Old Dominion          | Sun Belt          |                 131 |                 -0.069 |                 0.389 |           -0.039 |
| 141 |         175 | Jaxon Potter             | Old Dominion          | Sun Belt          |                  44 |                 -0.070 |                 0.364 |           -0.161 |
| 142 |         150 | Toa Faavae               | New Mexico            | Mountain West     |                 134 |                 -0.081 |                 0.381 |           -0.033 |
| 143 |         154 | Jaron-Keawe Sagapolutele | California            | ACC               |                 198 |                 -0.086 |                 0.399 |           -0.044 |
| 144 |         163 | Jackson Sharman          | Sacramento State      | Mid-American      |                 129 |                 -0.099 |                 0.372 |           -0.095 |
| 145 |         164 | Mitch Griffis            | East Carolina         | American Athletic |                 104 |                 -0.099 |                 0.375 |           -0.095 |
| 146 |         166 | Grady Brosterhous        | Utah State            | Pac-12            |                 167 |                 -0.099 |                 0.341 |           -0.116 |
| 147 |         147 | Ryder Burton             | UAB                   | American Athletic |                 170 |                 -0.103 |                 0.406 |           -0.028 |
| 148 |         168 | Caleb Heavner            | Miami (OH)            | Mid-American      |                 133 |                 -0.104 |                 0.406 |           -0.121 |
| 149 |         165 | Jason Wright             | Buffalo               | Mid-American      |                 159 |                 -0.107 |                 0.396 |           -0.098 |
| 150 |         173 | Kadin Semonza            | Tulane                | American Athletic |                 117 |                 -0.125 |                 0.325 |           -0.149 |
| 151 |         177 | EJ Colson                | UTEP                  | Mountain West     |                  93 |                 -0.126 |                 0.409 |           -0.198 |
| 152 |         155 | Marcel Reed              | Texas A&M             | SEC               |                 170 |                 -0.127 |                 0.418 |           -0.047 |
| 153 |         170 | Caden Pinnick            | Washington State      | Pac-12            |                 179 |                 -0.130 |                 0.419 |           -0.134 |
| 154 |         156 | Drake Lindsey            | Minnesota             | Big Ten           |                 163 |                 -0.136 |                 0.380 |           -0.050 |
| 155 |         146 | Faizon Brandon           | Tennessee             | SEC               |                  92 |                 -0.144 |                 0.348 |           -0.025 |
| 156 |         151 | Raymond Moore III        | UTEP                  | Mountain West     |                  40 |                 -0.152 |                 0.325 |           -0.038 |
| 157 |         162 | Jadyn Glasser            | Central Michigan      | Mid-American      |                  44 |                 -0.155 |                 0.364 |           -0.069 |
| 158 |         158 | Landyn Locke             | Sam Houston           | Conference USA    |                 183 |                 -0.162 |                 0.366 |           -0.064 |
| 159 |         176 | Elijah Holmes            | Buffalo               | Mid-American      |                  68 |                 -0.174 |                 0.368 |           -0.167 |
| 160 |         148 | Holden Geriner           | Pittsburgh            | ACC               |                  84 |                 -0.181 |                 0.357 |           -0.028 |
| 161 |         129 | Ayden Pereira            | Georgia State         | Sun Belt          |                  41 |                 -0.182 |                 0.366 |            0.025 |
| 162 |         169 | Jayden Denegal           | San Diego State       | Pac-12            |                 100 |                 -0.183 |                 0.330 |           -0.128 |
| 163 |         171 | Carter Jones             | Nevada                | Mountain West     |                  94 |                 -0.205 |                 0.362 |           -0.136 |
| 164 |         131 | Austin Carlisle          | UL Monroe             | Sun Belt          |                  74 |                 -0.240 |                 0.459 |            0.018 |
| 165 |         160 | Landy Lyddy              | Southern Miss         | Sun Belt          |                 141 |                 -0.275 |                 0.326 |           -0.065 |
| 166 |         122 | AJ Surace                | Rutgers               | Big Ten           |                  43 |                 -0.279 |                 0.349 |            0.033 |
| 167 |         174 | Cole Gonzales            | Charlotte             | American Athletic |                  88 |                 -0.294 |                 0.420 |           -0.161 |
| 168 |         172 | Ethan Hampton            | Southern Miss         | Sun Belt          |                  43 |                 -0.325 |                 0.419 |           -0.142 |
| 169 |         167 | Adam Damante             | New Mexico State      | Conference USA    |                  70 |                 -0.347 |                 0.257 |           -0.116 |

## All plays

|   # | QB                       | Team                  | Conf              |   G |   Dropbacks |   Rushes |   Plays |   EPA/dropback |   EPA/rush |   EPA/play |   Success |   EPA/play (WP 10–90%) |
|----:|:-------------------------|:----------------------|:------------------|----:|------------:|---------:|--------:|---------------:|-----------:|-----------:|----------:|-----------------------:|
|   1 | David McComb             | Miami (OH)            | Mid-American      |   4 |         109 |       11 |     120 |          0.565 |      0.615 |      0.570 |     0.525 |                  0.676 |
|   2 | Darian Mensah            | Miami                 | ACC               |   8 |         239 |       15 |     254 |          0.490 |      0.953 |      0.518 |     0.602 |                  0.563 |
|   3 | Tayven Jackson           | North Texas           | American Athletic |   8 |         269 |       24 |     293 |          0.477 |      0.253 |      0.459 |     0.570 |                  0.492 |
|   4 | Giovanni Lopez           | Wake Forest           | ACC               |   8 |         235 |       60 |     295 |          0.375 |      0.640 |      0.429 |     0.539 |                  0.572 |
|   5 | Julian Sayin             | Ohio State            | Big Ten           |   7 |         205 |       23 |     228 |          0.408 |      0.481 |      0.416 |     0.566 |                  0.508 |
|   6 | Jackson Gutierrez        | Navy                  | American Athletic |   8 |          78 |      165 |     243 |          0.424 |      0.368 |      0.386 |     0.502 |                  0.317 |
|   7 | Elijah Brown             | Washington            | Big Ten           |   3 |          73 |        2 |      75 |          0.472 |     -2.993 |      0.380 |     0.560 |                  0.144 |
|   8 | Hauss Hejny              | Colorado State        | Pac-12            |   5 |         137 |       26 |     163 |          0.341 |      0.494 |      0.366 |     0.534 |                  0.359 |
|   9 | Lincoln Kienholz         | Louisville            | ACC               |   8 |         222 |       65 |     287 |          0.343 |      0.409 |      0.358 |     0.533 |                  0.342 |
|  10 | Caden Veltkamp           | Florida Atlantic      | American Athletic |   8 |         331 |       25 |     356 |          0.379 |      0.012 |      0.353 |     0.528 |                  0.312 |
|  11 | Aidan Chiles             | Northwestern          | Big Ten           |   8 |         222 |       65 |     287 |          0.286 |      0.544 |      0.344 |     0.533 |                  0.315 |
|  12 | C.J. Carr                | Notre Dame            | FBS Independents  |   8 |         225 |       22 |     247 |          0.347 |      0.265 |      0.340 |     0.522 |                  0.299 |
|  13 | Avery Johnson            | Kansas State          | Big 12            |   6 |         190 |       47 |     237 |          0.259 |      0.638 |      0.334 |     0.511 |                  0.336 |
|  14 | Kevin Jennings           | SMU                   | ACC               |   8 |         263 |       42 |     305 |          0.379 |      0.045 |      0.333 |     0.534 |                  0.316 |
|  15 | Brad Jackson             | Texas State           | Pac-12            |   8 |         241 |       75 |     316 |          0.325 |      0.337 |      0.328 |     0.509 |                  0.196 |
|  16 | Jayden Maiava            | USC                   | Big Ten           |   9 |         310 |       13 |     323 |          0.352 |     -0.319 |      0.325 |     0.557 |                  0.376 |
|  17 | Drew Mestemaker          | Oklahoma State        | Big 12            |   8 |         291 |       24 |     315 |          0.288 |      0.669 |      0.317 |     0.530 |                  0.268 |
|  18 | Conner Weigman           | Houston               | Big 12            |   8 |         242 |       57 |     299 |          0.312 |      0.297 |      0.309 |     0.545 |                  0.283 |
|  19 | Bishop Davenport         | South Alabama         | Sun Belt          |   2 |          61 |       16 |      77 |          0.302 |      0.328 |      0.307 |     0.481 |                  0.413 |
|  20 | Mason Heintschel         | Pittsburgh            | ACC               |   5 |         153 |       25 |     178 |          0.348 |     -0.003 |      0.299 |     0.466 |                  0.305 |
|  21 | Noah Fifita              | Arizona               | Big 12            |   8 |         289 |       36 |     325 |          0.308 |      0.199 |      0.296 |     0.520 |                  0.303 |
|  22 | John Alan Richter        | Toledo                | Mid-American      |   8 |         266 |       10 |     276 |          0.313 |     -0.225 |      0.294 |     0.493 |                  0.339 |
|  23 | Keelon Russell           | Alabama               | SEC               |   8 |         247 |       44 |     291 |          0.240 |      0.575 |      0.291 |     0.526 |                  0.339 |
|  24 | Marcus Stokes            | Memphis               | American Athletic |   9 |         273 |       57 |     330 |          0.308 |      0.204 |      0.290 |     0.527 |                  0.354 |
|  25 | Maddux Madsen            | Boise State           | Pac-12            |   8 |         230 |       34 |     264 |          0.221 |      0.727 |      0.287 |     0.527 |                  0.284 |
|  26 | Michael Hawkins Jr.      | West Virginia         | Big 12            |   8 |         174 |      147 |     321 |          0.213 |      0.371 |      0.285 |     0.442 |                  0.366 |
|  27 | Sam Leavitt              | LSU                   | SEC               |   8 |         265 |       61 |     326 |          0.242 |      0.444 |      0.280 |     0.546 |                  0.245 |
|  28 | Cale Hellums             | Army                  | American Athletic |   8 |          80 |      168 |     248 |          0.080 |      0.372 |      0.278 |     0.532 |                  0.306 |
|  29 | Braden Atkinson          | Oregon State          | Pac-12            |   8 |         347 |       17 |     364 |          0.292 |     -0.032 |      0.277 |     0.505 |                  0.202 |
|  30 | Tommy Carr               | Michigan              | Big Ten           |   4 |          69 |       24 |      93 |          0.148 |      0.630 |      0.273 |     0.527 |                  0.180 |
|  31 | Nick Minicucci           | Delaware              | Conference USA    |   6 |         178 |       15 |     193 |          0.219 |      0.914 |      0.273 |     0.487 |                  0.259 |
|  32 | Austin Simmons           | Missouri              | SEC               |   8 |         247 |       14 |     261 |          0.300 |     -0.202 |      0.273 |     0.479 |                  0.287 |
|  33 | Kamario Taylor           | Mississippi State     | SEC               |   6 |         175 |       29 |     204 |          0.212 |      0.630 |      0.272 |     0.520 |                  0.262 |
|  34 | Cameran Brown            | Georgia State         | Sun Belt          |   7 |         172 |       34 |     206 |          0.272 |      0.260 |      0.270 |     0.510 |                  0.340 |
|  35 | Aaron Philo              | Florida               | SEC               |   7 |         163 |       35 |     198 |          0.292 |      0.158 |      0.269 |     0.535 |                  0.259 |
|  36 | CJ Bailey                | NC State              | ACC               |   8 |         257 |       47 |     304 |          0.246 |      0.316 |      0.257 |     0.484 |                  0.273 |
|  37 | Ashton Daniels           | Florida State         | ACC               |   8 |         229 |       71 |     300 |          0.163 |      0.539 |      0.252 |     0.463 |                  0.246 |
|  38 | Caden Creel              | Jacksonville State    | Conference USA    |   8 |         217 |      110 |     327 |          0.263 |      0.227 |      0.251 |     0.514 |                  0.245 |
|  39 | Ajani Sheppard           | Temple                | American Athletic |   8 |         153 |       64 |     217 |          0.200 |      0.368 |      0.250 |     0.479 |                  0.292 |
|  40 | Dylan Lonergan           | Rutgers               | Big Ten           |   6 |         132 |       16 |     148 |          0.305 |     -0.210 |      0.249 |     0.486 |                  0.284 |
|  41 | JC French                | Cincinnati            | Big 12            |   8 |         228 |       63 |     291 |          0.234 |      0.301 |      0.249 |     0.533 |                  0.249 |
|  42 | Bear Bachmeier           | BYU                   | Big 12            |   8 |         212 |       71 |     283 |          0.191 |      0.406 |      0.245 |     0.519 |                  0.285 |
|  43 | Devon Dampier            | Utah                  | Big 12            |   8 |         238 |       71 |     309 |          0.212 |      0.318 |      0.237 |     0.550 |                  0.363 |
|  44 | Trey Owens               | Arkansas State        | Sun Belt          |   8 |         249 |       44 |     293 |          0.197 |      0.402 |      0.227 |     0.532 |                  0.252 |
|  45 | Katin Houser             | Illinois              | Big Ten           |   7 |         225 |       26 |     251 |          0.183 |      0.547 |      0.221 |     0.518 |                  0.288 |
|  46 | Anthony Colandrea        | Nebraska              | Big Ten           |   7 |         234 |       52 |     286 |          0.130 |      0.625 |      0.220 |     0.479 |                  0.130 |
|  47 | Lanorris Sellers         | South Carolina        | SEC               |   8 |         258 |       77 |     335 |          0.080 |      0.670 |      0.216 |     0.490 |                  0.207 |
|  48 | Trinidad Chambliss       | Ole Miss              | SEC               |   8 |         304 |       39 |     343 |          0.164 |      0.601 |      0.213 |     0.507 |                  0.276 |
|  49 | Josh Hoover              | Indiana               | Big Ten           |   9 |         216 |       21 |     237 |          0.195 |      0.351 |      0.209 |     0.468 |                  0.112 |
|  50 | Blake Baker              | Louisiana Tech        | Sun Belt          |   7 |         166 |       39 |     205 |          0.245 |      0.055 |      0.209 |     0.468 |                  0.256 |
|  51 | Walker Eget              | Duke                  | ACC               |   8 |         219 |        5 |     224 |          0.207 |      0.129 |      0.205 |     0.464 |                  0.156 |
|  52 | Dante Moore              | Oregon                | Big Ten           |   4 |         106 |        3 |     109 |          0.227 |     -0.567 |      0.205 |     0.459 |                  0.191 |
|  53 | Gunner Stockton          | Georgia               | SEC               |   8 |         189 |       37 |     226 |          0.204 |      0.203 |      0.204 |     0.531 |                  0.292 |
|  54 | William Watson III       | Massachusetts         | Mid-American      |   6 |         144 |       29 |     173 |          0.135 |      0.530 |      0.201 |     0.439 |                  0.275 |
|  55 | Jared Curtis             | Vanderbilt            | SEC               |   7 |         209 |       47 |     256 |          0.132 |      0.447 |      0.190 |     0.477 |                  0.111 |
|  56 | Jared Hollins            | South Alabama         | Sun Belt          |   7 |         163 |       39 |     202 |          0.170 |      0.231 |      0.182 |     0.426 |                  0.252 |
|  57 | Henry Belin IV           | Missouri State        | Conference USA    |   7 |         133 |       13 |     146 |          0.137 |      0.568 |      0.175 |     0.459 |                  0.281 |
|  58 | Stone Saunders           | San Diego State       | Pac-12            |   4 |          71 |        2 |      73 |          0.186 |     -0.221 |      0.175 |     0.438 |                  0.002 |
|  59 | Owen McCown              | UTSA                  | American Athletic |   8 |         251 |       31 |     282 |          0.163 |      0.253 |      0.173 |     0.465 |                  0.264 |
|  60 | Kalieb Osborne           | UConn                 | FBS Independents  |   8 |         239 |       63 |     302 |          0.086 |      0.484 |      0.169 |     0.457 |                  0.218 |
|  61 | Conner Harrell           | Charlotte             | American Athletic |   5 |         114 |       16 |     130 |          0.164 |      0.179 |      0.166 |     0.408 |                  0.286 |
|  62 | Dylan Raiola             | Oregon                | Big Ten           |   6 |         150 |        4 |     154 |          0.171 |     -0.085 |      0.165 |     0.435 |                  0.062 |
|  63 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |   8 |         284 |       34 |     318 |          0.133 |      0.418 |      0.163 |     0.484 |                  0.221 |
|  64 | Ksaan Farrar             | Colorado State        | Pac-12            |   5 |         148 |       11 |     159 |          0.123 |      0.705 |      0.163 |     0.428 |                 -0.008 |
|  65 | Jaylen Raynor            | Iowa State            | Big 12            |   8 |         197 |       54 |     251 |          0.157 |      0.180 |      0.162 |     0.442 |                  0.182 |
|  66 | Isaiah Marshall          | Kansas                | Big 12            |   7 |         207 |       75 |     282 |          0.095 |      0.346 |      0.161 |     0.433 |                  0.148 |
|  67 | Jayden Mandal            | Fresno State          | Pac-12            |   8 |         226 |       41 |     267 |          0.131 |      0.318 |      0.160 |     0.483 |                  0.170 |
|  68 | Ryan Browne              | Purdue                | Big Ten           |   8 |         257 |       28 |     285 |          0.126 |      0.412 |      0.154 |     0.491 |                  0.199 |
|  69 | Baylor Hayes             | Tulsa                 | American Athletic |   6 |         199 |       27 |     226 |          0.156 |      0.113 |      0.151 |     0.407 |                  0.141 |
|  70 | Owen Eshelman            | Washington State      | Pac-12            |   3 |         142 |       44 |     186 |          0.027 |      0.537 |      0.147 |     0.489 |                 -0.028 |
|  71 | Mikey Keene              | Arizona State         | Big 12            |   3 |          66 |        1 |      67 |          0.170 |     -1.529 |      0.145 |     0.448 |                  0.039 |
|  72 | Nate Bennett             | Baylor                | Big 12            |   3 |          66 |        2 |      68 |          0.061 |      2.810 |      0.142 |     0.471 |                  0.978 |
|  73 | Billy Edwards            | North Carolina        | ACC               |   8 |         250 |       24 |     274 |          0.139 |      0.148 |      0.140 |     0.518 |                  0.167 |
|  74 | Malachi Singleton        | App State             | Sun Belt          |   8 |         248 |       35 |     283 |          0.185 |     -0.184 |      0.139 |     0.473 |                  0.116 |
|  75 | Matt Vezza               | Ohio                  | Mid-American      |   6 |          70 |       27 |      97 |         -0.091 |      0.736 |      0.139 |     0.515 |                  0.337 |
|  76 | Rocco Becht              | Penn State            | Big Ten           |   8 |         246 |       41 |     287 |          0.149 |      0.037 |      0.133 |     0.460 |                  0.107 |
|  77 | Deshawn Purdie           | Liberty               | Conference USA    |   8 |         165 |       31 |     196 |          0.131 |      0.139 |      0.132 |     0.480 |                  0.062 |
|  78 | Nick Poulos              | Ohio                  | Mid-American      |   5 |         105 |       36 |     141 |          0.068 |      0.318 |      0.132 |     0.518 |                  0.045 |
|  79 | Jeremy Hecklinski        | Iowa                  | Big Ten           |   5 |          68 |        1 |      69 |          0.117 |      1.093 |      0.131 |     0.522 |                 -0.133 |
|  80 | McCae Hillstead          | Utah State            | Pac-12            |   3 |          64 |       21 |      85 |          0.050 |      0.368 |      0.129 |     0.506 |                  0.256 |
|  81 | Jackson Arnold           | UNLV                  | Mountain West     |   8 |         232 |       99 |     331 |          0.058 |      0.292 |      0.128 |     0.468 |                  0.170 |
|  82 | Colton Joseph            | Wisconsin             | Big Ten           |   8 |         194 |       76 |     270 |          0.061 |      0.287 |      0.124 |     0.437 |                  0.058 |
|  83 | Bryce Underwood          | Michigan              | Big Ten           |   7 |         134 |       51 |     185 |          0.118 |      0.133 |      0.122 |     0.459 |                  0.154 |
|  84 | Will Hammond             | Texas Tech            | Big 12            |   7 |         217 |       28 |     245 |          0.094 |      0.296 |      0.117 |     0.490 |                  0.166 |
|  85 | Aidan Armenta            | UL Monroe             | Sun Belt          |   7 |         198 |       34 |     232 |          0.110 |      0.129 |      0.113 |     0.444 |                  0.079 |
|  86 | Nathan Hayes             | North Dakota State    | Mountain West     |   9 |         238 |       40 |     278 |          0.033 |      0.576 |      0.111 |     0.471 |                  0.197 |
|  87 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |   8 |         206 |       97 |     303 |          0.028 |      0.288 |      0.111 |     0.439 |                  0.170 |
|  88 | Max Johnson              | Georgia Southern      | Sun Belt          |   8 |         284 |       21 |     305 |          0.106 |      0.166 |      0.110 |     0.452 |                  0.149 |
|  89 | Keldric Luster           | Ball State            | Mid-American      |   7 |         221 |       53 |     274 |          0.056 |      0.318 |      0.107 |     0.438 |                  0.220 |
|  90 | Malachi Nelson           | Syracuse              | ACC               |   3 |          74 |        6 |      80 |          0.126 |     -0.146 |      0.106 |     0.475 |                  0.164 |
|  91 | Hank Brown               | Iowa                  | Big Ten           |   7 |         173 |       18 |     191 |          0.111 |      0.048 |      0.105 |     0.461 |                  0.036 |
|  92 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |   6 |         137 |       19 |     156 |          0.122 |     -0.033 |      0.103 |     0.436 |                  0.077 |
|  93 | Taron Dickens            | Northern Illinois     | Mountain West     |   8 |         267 |       31 |     298 |          0.081 |      0.286 |      0.103 |     0.463 |                  0.051 |
|  94 | Davis Warren             | Stanford              | ACC               |   9 |         321 |       11 |     332 |          0.091 |      0.235 |      0.096 |     0.413 |                  0.213 |
|  95 | Jacurri Brown            | Rice                  | American Athletic |   7 |          92 |      103 |     195 |         -0.208 |      0.365 |      0.094 |     0.436 |                  0.040 |
|  96 | Steven Angeli            | Syracuse              | ACC               |   5 |         179 |        8 |     187 |          0.084 |      0.303 |      0.094 |     0.428 |                  0.077 |
|  97 | Kenny Minchey            | Kentucky              | SEC               |   8 |         244 |       26 |     270 |          0.079 |      0.185 |      0.089 |     0.478 |                  0.070 |
|  98 | Camden Coleman           | James Madison         | Sun Belt          |   9 |         244 |       35 |     279 |          0.083 |      0.123 |      0.088 |     0.434 |                  0.144 |
|  99 | Trace Johnson            | Tulane                | American Athletic |   4 |         107 |       15 |     122 |          0.102 |     -0.024 |      0.087 |     0.451 |                  0.152 |
| 100 | Jaden Craig              | TCU                   | Big 12            |   8 |         289 |       44 |     333 |          0.079 |      0.139 |      0.087 |     0.444 |                  0.041 |
| 101 | Demond Williams Jr.      | Washington            | Big Ten           |   6 |         190 |       44 |     234 |          0.013 |      0.383 |      0.082 |     0.462 |                  0.048 |
| 102 | Cibastian Broughton      | Akron                 | Mid-American      |   4 |          71 |       24 |      95 |         -0.057 |      0.491 |      0.082 |     0.474 |                  0.044 |
| 103 | Tyler Hughes             | Wyoming               | Mountain West     |   8 |         187 |       82 |     269 |         -0.127 |      0.553 |      0.080 |     0.468 |                  0.055 |
| 104 | Tramell Jones Jr.        | Florida               | SEC               |   6 |          95 |       18 |     113 |          0.031 |      0.339 |      0.080 |     0.496 |                  0.132 |
| 105 | Alberto Mendoza          | Georgia Tech          | ACC               |   8 |         261 |       20 |     281 |          0.067 |      0.236 |      0.079 |     0.491 |                 -0.009 |
| 106 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |   8 |         256 |       59 |     315 |          0.042 |      0.241 |      0.079 |     0.444 |                  0.117 |
| 107 | D.J. Lagway              | Baylor                | Big 12            |   6 |         255 |       22 |     277 |          0.066 |      0.165 |      0.073 |     0.415 |                  0.045 |
| 108 | Isaac Wilson             | Colorado              | Big 12            |   6 |         154 |       39 |     193 |          0.143 |     -0.218 |      0.070 |     0.461 |                  0.108 |
| 109 | Luke Weaver              | San José State        | Mountain West     |   8 |         257 |       44 |     301 |          0.117 |     -0.211 |      0.069 |     0.472 |                  0.000 |
| 110 | Beau Pribula             | Virginia              | ACC               |   9 |         239 |       69 |     308 |          0.058 |      0.092 |      0.066 |     0.435 |                  0.072 |
| 111 | Trey Hedden              | New Mexico State      | Conference USA    |   5 |         132 |        7 |     139 |          0.045 |      0.421 |      0.064 |     0.396 |                  0.053 |
| 112 | Rickie Collins           | Kennesaw State        | Conference USA    |   8 |         241 |       74 |     315 |          0.058 |      0.080 |      0.063 |     0.470 |                  0.049 |
| 113 | Ty Dieffenbach           | UCLA                  | Big Ten           |   4 |         103 |       16 |     119 |          0.105 |     -0.237 |      0.059 |     0.378 |                  0.173 |
| 114 | Byrum Brown              | Auburn                | SEC               |   8 |         278 |      103 |     381 |         -0.030 |      0.298 |      0.058 |     0.423 |                  0.035 |
| 115 | John Mateer              | Oklahoma              | SEC               |   8 |         266 |       66 |     332 |          0.072 |     -0.007 |      0.056 |     0.437 |                 -0.001 |
| 116 | Micah Alejado            | Hawai'i               | Mountain West     |   8 |         359 |       23 |     382 |          0.055 |      0.034 |      0.054 |     0.445 |                  0.049 |
| 117 | Keyone Jenkins           | UCF                   | Big 12            |   8 |         185 |       34 |     219 |          0.079 |     -0.087 |      0.054 |     0.434 |                  0.056 |
| 118 | Jay Kastantin            | Bowling Green         | Mid-American      |   9 |         241 |       46 |     287 |          0.045 |      0.094 |      0.053 |     0.449 |                  0.077 |
| 119 | Cutter Boley             | Arizona State         | Big 12            |   7 |         184 |       30 |     214 |          0.052 |      0.052 |      0.052 |     0.449 |                 -0.033 |
| 120 | Mason McKenzie           | Boston College        | ACC               |   8 |         221 |      108 |     329 |         -0.100 |      0.340 |      0.044 |     0.441 |                  0.108 |
| 121 | Angel H Flores           | Central Michigan      | Mid-American      |   7 |         104 |      116 |     220 |         -0.227 |      0.276 |      0.038 |     0.414 |                  0.076 |
| 122 | AJ Surace                | Rutgers               | Big Ten           |   6 |          97 |       13 |     110 |          0.157 |     -0.894 |      0.033 |     0.382 |                 -0.279 |
| 123 | Zion Turner              | Marshall              | Sun Belt          |   6 |         100 |       16 |     116 |         -0.084 |      0.751 |      0.031 |     0.448 |                  0.066 |
| 124 | Julian Lewis             | Colorado              | Big 12            |   4 |         102 |        6 |     108 |          0.024 |      0.123 |      0.029 |     0.389 |                  0.052 |
| 125 | J.J. Kohl                | Florida International | Conference USA    |   8 |         269 |       29 |     298 |          0.048 |     -0.166 |      0.027 |     0.433 |                  0.039 |
| 126 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |   7 |          77 |       41 |     118 |         -0.035 |      0.142 |      0.027 |     0.466 |                  0.002 |
| 127 | Malik Washington         | Maryland              | Big Ten           |   8 |         297 |       37 |     334 |         -0.003 |      0.261 |      0.026 |     0.425 |                  0.006 |
| 128 | Alessio Milivojevic      | Michigan State        | Big Ten           |   7 |         200 |       23 |     223 |         -0.005 |      0.289 |      0.026 |     0.480 |                 -0.058 |
| 129 | Ayden Pereira            | Georgia State         | Sun Belt          |   7 |          77 |       27 |     104 |         -0.036 |      0.199 |      0.025 |     0.413 |                 -0.182 |
| 130 | Jackson Brousseau        | California            | ACC               |   5 |         126 |        7 |     133 |          0.030 |     -0.182 |      0.019 |     0.368 |                 -0.044 |
| 131 | Austin Carlisle          | UL Monroe             | Sun Belt          |   6 |          75 |       38 |     113 |         -0.222 |      0.492 |      0.018 |     0.496 |                 -0.240 |
| 132 | Roman Gagliano           | Middle Tennessee      | Conference USA    |   8 |         270 |       36 |     306 |          0.007 |      0.086 |      0.016 |     0.428 |                  0.097 |
| 133 | Brock Glenn              | Western Kentucky      | Conference USA    |   8 |         169 |       81 |     250 |         -0.131 |      0.299 |      0.009 |     0.440 |                 -0.050 |
| 134 | Dru Deshields            | Kent State            | Mid-American      |   9 |         265 |       59 |     324 |         -0.056 |      0.274 |      0.004 |     0.383 |                  0.037 |
| 135 | Nico Iamaleava           | UCLA                  | Big Ten           |   5 |         124 |       31 |     155 |          0.000 |      0.003 |      0.001 |     0.432 |                 -0.006 |
| 136 | Skyler Locklear          | Missouri State        | Conference USA    |   5 |         117 |       24 |     141 |         -0.034 |      0.169 |      0.001 |     0.376 |                 -0.011 |
| 137 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |   7 |         157 |       55 |     212 |          0.002 |     -0.012 |     -0.002 |     0.434 |                  0.066 |
| 138 | Noah Kim                 | Eastern Michigan      | Mid-American      |   8 |         292 |       20 |     312 |         -0.004 |      0.033 |     -0.002 |     0.410 |                  0.038 |
| 139 | Broc Lowry               | Western Michigan      | Mid-American      |   9 |         208 |       72 |     280 |         -0.061 |      0.146 |     -0.008 |     0.446 |                  0.130 |
| 140 | KJ Jackson               | Arkansas              | SEC               |   8 |         263 |       57 |     320 |         -0.021 |      0.051 |     -0.008 |     0.456 |                 -0.016 |
| 141 | Will Crowder             | Troy                  | Sun Belt          |   7 |         195 |       40 |     235 |         -0.113 |      0.484 |     -0.011 |     0.426 |                 -0.058 |
| 142 | Arch Manning             | Texas                 | SEC               |   8 |         242 |       45 |     287 |         -0.037 |      0.109 |     -0.014 |     0.425 |                 -0.047 |
| 143 | Brayden Roggow           | Akron                 | Mid-American      |   8 |         208 |       19 |     227 |         -0.039 |      0.249 |     -0.015 |     0.410 |                 -0.014 |
| 144 | AJ Bianco                | Nevada                | Mountain West     |   5 |          74 |       18 |      92 |         -0.081 |      0.207 |     -0.024 |     0.337 |                  0.002 |
| 145 | M.Van Buren Jr.          | South Florida         | American Athletic |   8 |         191 |       39 |     230 |         -0.016 |     -0.068 |     -0.025 |     0.470 |                 -0.051 |
| 146 | Faizon Brandon           | Tennessee             | SEC               |   5 |         116 |       36 |     152 |         -0.184 |      0.488 |     -0.025 |     0.408 |                 -0.144 |
| 147 | Ryder Burton             | UAB                   | American Athletic |   8 |         214 |       43 |     257 |         -0.079 |      0.229 |     -0.028 |     0.412 |                 -0.103 |
| 148 | Holden Geriner           | Pittsburgh            | ACC               |   6 |         138 |       16 |     154 |         -0.001 |     -0.259 |     -0.028 |     0.390 |                 -0.181 |
| 149 | Dexter Williams II       | Tulsa                 | American Athletic |   5 |          62 |        9 |      71 |         -0.008 |     -0.176 |     -0.029 |     0.423 |                 -0.152 |
| 150 | Toa Faavae               | New Mexico            | Mountain West     |   8 |         119 |       58 |     177 |         -0.174 |      0.255 |     -0.033 |     0.424 |                 -0.081 |
| 151 | Raymond Moore III        | UTEP                  | Mountain West     |   8 |          93 |       53 |     146 |         -0.351 |      0.512 |     -0.038 |     0.411 |                 -0.152 |
| 152 | Quinn Henicle            | Old Dominion          | Sun Belt          |   6 |         115 |       66 |     181 |         -0.229 |      0.291 |     -0.039 |     0.392 |                 -0.069 |
| 153 | Emory Williams           | East Carolina         | American Athletic |   6 |         122 |       20 |     142 |         -0.035 |     -0.078 |     -0.041 |     0.423 |                 -0.028 |
| 154 | Jaron-Keawe Sagapolutele | California            | ACC               |   8 |         276 |        9 |     285 |         -0.032 |     -0.420 |     -0.044 |     0.414 |                 -0.086 |
| 155 | Marcel Reed              | Texas A&M             | SEC               |   8 |         234 |       55 |     289 |         -0.096 |      0.161 |     -0.047 |     0.419 |                 -0.127 |
| 156 | Drake Lindsey            | Minnesota             | Big Ten           |   8 |         262 |       12 |     274 |         -0.043 |     -0.190 |     -0.050 |     0.412 |                 -0.136 |
| 157 | Alonza Barnett           | UCF                   | Big 12            |   3 |          71 |       15 |      86 |         -0.039 |     -0.118 |     -0.053 |     0.395 |                 -0.218 |
| 158 | Landyn Locke             | Sam Houston           | Conference USA    |   7 |         251 |       24 |     275 |         -0.082 |      0.124 |     -0.064 |     0.382 |                 -0.162 |
| 159 | George MacIntyre         | Tennessee             | SEC               |   6 |         108 |        5 |     113 |         -0.037 |     -0.661 |     -0.065 |     0.434 |                 -0.044 |
| 160 | Landy Lyddy              | Southern Miss         | Sun Belt          |   8 |         214 |       21 |     235 |         -0.079 |      0.074 |     -0.065 |     0.379 |                 -0.275 |
| 161 | Tait Reynolds            | Clemson               | ACC               |   8 |         237 |       66 |     303 |         -0.128 |      0.160 |     -0.065 |     0.426 |                 -0.014 |
| 162 | Jadyn Glasser            | Central Michigan      | Mid-American      |   7 |          80 |       17 |      97 |         -0.102 |      0.088 |     -0.069 |     0.392 |                 -0.155 |
| 163 | Jackson Sharman          | Sacramento State      | Mid-American      |   8 |         258 |       19 |     277 |         -0.100 |     -0.029 |     -0.095 |     0.401 |                 -0.099 |
| 164 | Mitch Griffis            | East Carolina         | American Athletic |   8 |         130 |       31 |     161 |         -0.132 |      0.058 |     -0.095 |     0.385 |                 -0.099 |
| 165 | Jason Wright             | Buffalo               | Mid-American      |   7 |         201 |       40 |     241 |         -0.144 |      0.134 |     -0.098 |     0.369 |                 -0.107 |
| 166 | Grady Brosterhous        | Utah State            | Pac-12            |   7 |         200 |       80 |     280 |         -0.091 |     -0.179 |     -0.116 |     0.357 |                 -0.099 |
| 167 | Adam Damante             | New Mexico State      | Conference USA    |   6 |         124 |        8 |     132 |         -0.164 |      0.626 |     -0.116 |     0.394 |                 -0.347 |
| 168 | Caleb Heavner            | Miami (OH)            | Mid-American      |   7 |         116 |       39 |     155 |         -0.278 |      0.347 |     -0.121 |     0.406 |                 -0.104 |
| 169 | Jayden Denegal           | San Diego State       | Pac-12            |   7 |         157 |       17 |     174 |         -0.117 |     -0.229 |     -0.128 |     0.351 |                 -0.183 |
| 170 | Caden Pinnick            | Washington State      | Pac-12            |   6 |         195 |       53 |     248 |         -0.202 |      0.114 |     -0.134 |     0.403 |                 -0.130 |
| 171 | Carter Jones             | Nevada                | Mountain West     |   4 |          95 |       21 |     116 |         -0.176 |      0.045 |     -0.136 |     0.371 |                 -0.205 |
| 172 | Ethan Hampton            | Southern Miss         | Sun Belt          |   3 |          76 |        6 |      82 |         -0.119 |     -0.437 |     -0.142 |     0.439 |                 -0.325 |
| 173 | Kadin Semonza            | Tulane                | American Athletic |   5 |         132 |       17 |     149 |         -0.126 |     -0.330 |     -0.149 |     0.309 |                 -0.125 |
| 174 | Cole Gonzales            | Charlotte             | American Athletic |   5 |         129 |       11 |     140 |         -0.110 |     -0.756 |     -0.161 |     0.429 |                 -0.294 |
| 175 | Jaxon Potter             | Old Dominion          | Sun Belt          |   3 |          94 |        7 |     101 |         -0.253 |      1.069 |     -0.161 |     0.337 |                 -0.070 |
| 176 | Elijah Holmes            | Buffalo               | Mid-American      |   2 |          64 |        7 |      71 |         -0.181 |     -0.044 |     -0.167 |     0.366 |                 -0.174 |
| 177 | EJ Colson                | UTEP                  | Mountain West     |   7 |         120 |       61 |     181 |         -0.287 |     -0.021 |     -0.198 |     0.425 |                 -0.126 |
| 178 | Parker Puckett           | Mississippi State     | SEC               |   5 |          84 |       18 |     102 |         -0.357 |      0.495 |     -0.206 |     0.451 |                 -0.554 |
| 179 | Ryan Huff                | Old Dominion          | Sun Belt          |   4 |          77 |        6 |      83 |         -0.237 |      0.107 |     -0.212 |     0.289 |                 -0.395 |
