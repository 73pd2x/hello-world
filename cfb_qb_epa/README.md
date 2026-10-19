# 2026 CFB QB EPA — through Week 7

FBS offenses, games through Oct 17, 2026 (Week 0 games are folded into Week 1).
**Minimum 60 dropbacks**, which leaves 163 QBs. Sorted by EPA/play over all dropbacks + QB rushes.

- **Dropbacks** = pass attempts + sacks. **Rushes** = designed runs + scrambles.
- **Success** = share of plays with positive EPA.
- **EPA/play (WP 10–90%)** leaves out garbage time.
- Not opponent-adjusted, so a team that has played FCS opponents looks better.
- Source: cfbfastR play-by-play (`sportsdataverse/cfbfastR-data`, `data/rds/pbp_players_pos_2026.rds`). Rebuild with `python qb_epa.py <rds> [min_dropbacks]` then `python make_readme.py <week> "<through date>"`.

Full tables: [`qb_epa_2026.csv`](qb_epa_2026.csv), [`qb_epa_2026_nongarbage.csv`](qb_epa_2026_nongarbage.csv)

## Non-garbage time (win probability 10–90%)

Same 60-dropback pool, plus at least 40 plays in competitive game states (153 QBs).

|   # |   Overall # | QB                       | Team                  | Conf              |   Plays (WP 10–90%) |   EPA/play (WP 10–90%) |   Success (WP 10–90%) |   EPA/play (all) |
|----:|------------:|:-------------------------|:----------------------|:------------------|--------------------:|-----------------------:|----------------------:|-----------------:|
|   1 |           2 | Darian Mensah            | Miami                 | ACC               |                 105 |                  0.575 |                 0.610 |            0.485 |
|   2 |           5 | Giovanni Lopez           | Wake Forest           | ACC               |                 147 |                  0.569 |                 0.565 |            0.422 |
|   3 |           8 | Jared Hollins            | South Alabama         | Sun Belt          |                  69 |                  0.555 |                 0.536 |            0.389 |
|   4 |           3 | Tayven Jackson           | North Texas           | American Athletic |                 139 |                  0.528 |                 0.554 |            0.465 |
|   5 |           6 | Julian Sayin             | Ohio State            | Big Ten           |                 140 |                  0.511 |                 0.571 |            0.416 |
|   6 |           1 | David McComb             | Miami (OH)            | Mid-American      |                  81 |                  0.492 |                 0.519 |            0.570 |
|   7 |          23 | Michael Hawkins Jr.      | West Virginia         | Big 12            |                 207 |                  0.452 |                 0.488 |            0.321 |
|   8 |           4 | Jayden Maiava            | USC                   | Big Ten           |                 182 |                  0.445 |                 0.549 |            0.425 |
|   9 |          26 | Bishop Davenport         | South Alabama         | Sun Belt          |                  59 |                  0.413 |                 0.525 |            0.307 |
|  10 |          37 | Cameran Brown            | Georgia State         | Sun Belt          |                 104 |                  0.394 |                 0.577 |            0.285 |
|  11 |          16 | Gunner Stockton          | Georgia               | SEC               |                 121 |                  0.392 |                 0.562 |            0.337 |
|  12 |          49 | Devon Dampier            | Utah                  | Big 12            |                 124 |                  0.387 |                 0.556 |            0.209 |
|  13 |          21 | Ajani Sheppard           | Temple                | American Athletic |                 152 |                  0.366 |                 0.487 |            0.331 |
|  14 |          17 | Kamario Taylor           | Mississippi State     | SEC               |                 120 |                  0.355 |                 0.542 |            0.337 |
|  15 |          60 | Kalieb Osborne           | UConn                 | FBS Independents  |                 138 |                  0.355 |                 0.507 |            0.184 |
|  16 |          10 | Conner Weigman           | Houston               | Big 12            |                 192 |                  0.355 |                 0.547 |            0.379 |
|  17 |          39 | Trinidad Chambliss       | Ole Miss              | SEC               |                 165 |                  0.348 |                 0.545 |            0.266 |
|  18 |          36 | Keelon Russell           | Alabama               | SEC               |                 170 |                  0.345 |                 0.512 |            0.285 |
|  19 |          32 | William Watson III       | Massachusetts         | Mid-American      |                  77 |                  0.345 |                 0.468 |            0.290 |
|  20 |          20 | Kevin Jennings           | SMU                   | ACC               |                 188 |                  0.340 |                 0.564 |            0.332 |
|  21 |          19 | Avery Johnson            | Kansas State          | Big 12            |                 155 |                  0.339 |                 0.510 |            0.334 |
|  22 |          71 | Matt Vezza               | Ohio                  | Mid-American      |                  82 |                  0.337 |                 0.549 |            0.139 |
|  23 |          29 | Ashton Daniels           | Florida State         | ACC               |                 172 |                  0.333 |                 0.465 |            0.299 |
|  24 |           7 | Brad Jackson             | Texas State           | Pac-12            |                 141 |                  0.329 |                 0.546 |            0.413 |
|  25 |          27 | John Alan Richter        | Toledo                | Mid-American      |                 147 |                  0.328 |                 0.490 |            0.303 |
|  26 |          33 | Bear Bachmeier           | BYU                   | Big 12            |                 150 |                  0.322 |                 0.527 |            0.289 |
|  27 |          38 | Maddux Madsen            | Boise State           | Pac-12            |                 159 |                  0.320 |                 0.535 |            0.284 |
|  28 |          31 | Austin Simmons           | Missouri              | SEC               |                 162 |                  0.319 |                 0.494 |            0.290 |
|  29 |          13 | C.J. Carr                | Notre Dame            | FBS Independents  |                 145 |                  0.314 |                 0.503 |            0.348 |
|  30 |          24 | Aaron Philo              | Florida               | SEC               |                 129 |                  0.310 |                 0.558 |            0.319 |
|  31 |          12 | Jackson Gutierrez        | Navy                  | American Athletic |                 142 |                  0.309 |                 0.507 |            0.350 |
|  32 |          15 | Lincoln Kienholz         | Louisville            | ACC               |                 211 |                  0.307 |                 0.517 |            0.338 |
|  33 |          25 | Noah Fifita              | Arizona               | Big 12            |                 159 |                  0.306 |                 0.553 |            0.310 |
|  34 |          80 | Nathan Hayes             | North Dakota State    | Mountain West     |                 134 |                  0.299 |                 0.507 |            0.123 |
|  35 |          55 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |                 170 |                  0.292 |                 0.524 |            0.196 |
|  36 |          46 | CJ Bailey                | NC State              | ACC               |                 128 |                  0.292 |                 0.500 |            0.224 |
|  37 |          73 | Conner Harrell           | Charlotte             | American Athletic |                  47 |                  0.288 |                 0.511 |            0.135 |
|  38 |          28 | Mason Heintschel         | Pittsburgh            | ACC               |                 101 |                  0.285 |                 0.446 |            0.299 |
|  39 |          65 | Camden Coleman           | James Madison         | Sun Belt          |                 117 |                  0.284 |                 0.487 |            0.167 |
|  40 |          22 | Aidan Chiles             | Northwestern          | Big Ten           |                 136 |                  0.284 |                 0.507 |            0.330 |
|  41 |          30 | JC French                | Cincinnati            | Big 12            |                 161 |                  0.283 |                 0.540 |            0.293 |
|  42 |          18 | Braden Atkinson          | Oregon State          | Pac-12            |                 149 |                  0.279 |                 0.497 |            0.335 |
|  43 |          42 | Dylan Lonergan           | Rutgers               | Big Ten           |                  90 |                  0.279 |                 0.500 |            0.251 |
|  44 |          11 | Hauss Hejny              | Colorado State        | Pac-12            |                  56 |                  0.277 |                 0.500 |            0.366 |
|  45 |          44 | Katin Houser             | Illinois              | Big Ten           |                 127 |                  0.275 |                 0.535 |            0.237 |
|  46 |          58 | Marcus Stokes            | Memphis               | American Athletic |                 162 |                  0.251 |                 0.488 |            0.194 |
|  47 |          41 | Caden Creel              | Jacksonville State    | Conference USA    |                 227 |                  0.245 |                 0.502 |            0.252 |
|  48 |          14 | Josh Hoover              | Indiana               | Big Ten           |                 144 |                  0.236 |                 0.486 |            0.343 |
|  49 |          63 | Ryan Browne              | Purdue                | Big Ten           |                 187 |                  0.227 |                 0.503 |            0.175 |
|  50 |          50 | Blake Baker              | Louisiana Tech        | Sun Belt          |                  89 |                  0.226 |                 0.449 |            0.206 |
|  51 |          68 | Will Hammond             | Texas Tech            | Big 12            |                 126 |                  0.225 |                 0.532 |            0.152 |
|  52 |          67 | Owen McCown              | UTSA                  | American Athletic |                 220 |                  0.218 |                 0.468 |            0.157 |
|  53 |          53 | Isaiah Marshall          | Kansas                | Big 12            |                 157 |                  0.210 |                 0.420 |            0.199 |
|  54 |          78 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |                 159 |                  0.207 |                 0.440 |            0.124 |
|  55 |          34 | Caden Veltkamp           | Florida Atlantic      | American Athletic |                 128 |                  0.201 |                 0.461 |            0.286 |
|  56 |          72 | Henry Belin IV           | Missouri State        | Conference USA    |                  50 |                  0.193 |                 0.500 |            0.138 |
|  57 |          54 | Walker Eget              | Duke                  | ACC               |                 156 |                  0.186 |                 0.449 |            0.198 |
|  58 |          57 | Lanorris Sellers         | South Carolina        | SEC               |                 146 |                  0.186 |                 0.459 |            0.194 |
|  59 |          35 | Drew Mestemaker          | Oklahoma State        | Big 12            |                 176 |                  0.183 |                 0.506 |            0.286 |
|  60 |          95 | Beau Pribula             | Virginia              | ACC               |                 142 |                  0.179 |                 0.458 |            0.091 |
|  61 |          45 | Sam Leavitt              | LSU                   | SEC               |                 167 |                  0.178 |                 0.533 |            0.236 |
|  62 |          51 | Dante Moore              | Oregon                | Big Ten           |                  90 |                  0.173 |                 0.400 |            0.206 |
|  63 |          62 | Trey Owens               | Arkansas State        | Sun Belt          |                 196 |                  0.165 |                 0.536 |            0.176 |
|  64 |          92 | Davis Warren             | Stanford              | ACC               |                 150 |                  0.165 |                 0.420 |            0.098 |
|  65 |          88 | Malachi Nelson           | Syracuse              | ACC               |                  72 |                  0.164 |                 0.500 |            0.106 |
|  66 |         124 | Broc Lowry               | Western Michigan      | Mid-American      |                 149 |                  0.161 |                 0.503 |            0.024 |
|  67 |          77 | Jayden Mandal            | Fresno State          | Pac-12            |                 179 |                  0.156 |                 0.469 |            0.127 |
|  68 |          82 | Bryce Underwood          | Michigan              | Big Ten           |                 166 |                  0.155 |                 0.494 |            0.122 |
|  69 |         111 | Keldric Luster           | Ball State            | Mid-American      |                 100 |                  0.153 |                 0.470 |            0.061 |
|  70 |          91 | Roman Gagliano           | Middle Tennessee      | Conference USA    |                 171 |                  0.149 |                 0.468 |            0.099 |
|  71 |          81 | Jackson Arnold           | UNLV                  | Mountain West     |                 228 |                  0.147 |                 0.452 |            0.123 |
|  72 |          47 | Anthony Colandrea        | Nebraska              | Big Ten           |                 223 |                  0.124 |                 0.444 |            0.220 |
|  73 |         101 | J.J. Kohl                | Florida International | Conference USA    |                 178 |                  0.124 |                 0.455 |            0.076 |
|  74 |          90 | Max Johnson              | Georgia Southern      | Sun Belt          |                 181 |                  0.123 |                 0.464 |            0.100 |
|  75 |          74 | Baylor Hayes             | Tulsa                 | American Athletic |                 173 |                  0.115 |                 0.393 |            0.134 |
|  76 |          59 | Malachi Singleton        | App State             | Sun Belt          |                 125 |                  0.113 |                 0.432 |            0.192 |
|  77 |         126 | Mason McKenzie           | Boston College        | ACC               |                 188 |                  0.111 |                 0.426 |            0.021 |
|  78 |          84 | Rickie Collins           | Kennesaw State        | Conference USA    |                 161 |                  0.104 |                 0.460 |            0.119 |
|  79 |         100 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |                 180 |                  0.104 |                 0.478 |            0.079 |
|  80 |          52 | Jared Curtis             | Vanderbilt            | SEC               |                 141 |                  0.102 |                 0.447 |            0.204 |
|  81 |         122 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |                 146 |                  0.094 |                 0.473 |            0.026 |
|  82 |          94 | Deshawn Purdie           | Liberty               | Conference USA    |                 113 |                  0.089 |                 0.478 |            0.094 |
|  83 |          61 | Colton Joseph            | Wisconsin             | Big Ten           |                 127 |                  0.085 |                 0.425 |            0.181 |
|  84 |         117 | Steven Angeli            | Syracuse              | ACC               |                  84 |                  0.081 |                 0.381 |            0.048 |
|  85 |          76 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |                  48 |                  0.077 |                 0.458 |            0.128 |
|  86 |          79 | Rocco Becht              | Penn State            | Big Ten           |                 162 |                  0.076 |                 0.420 |            0.123 |
|  87 |          56 | Nick Poulos              | Ohio                  | Mid-American      |                  60 |                  0.073 |                 0.500 |            0.195 |
|  88 |          75 | Jaden Craig              | TCU                   | Big 12            |                 182 |                  0.072 |                 0.445 |            0.131 |
|  89 |         105 | Taron Dickens            | Northern Illinois     | Mountain West     |                 109 |                  0.070 |                 0.495 |            0.070 |
|  90 |         107 | Billy Edwards            | North Carolina        | ACC               |                 151 |                  0.069 |                 0.503 |            0.066 |
|  91 |         121 | Julian Lewis             | Colorado              | Big 12            |                  70 |                  0.069 |                 0.400 |            0.029 |
|  92 |          86 | Hank Brown               | Iowa                  | Big Ten           |                 110 |                  0.066 |                 0.455 |            0.111 |
|  93 |         119 | Angel H Flores           | Central Michigan      | Mid-American      |                 112 |                  0.065 |                 0.393 |            0.038 |
|  94 |          96 | Keyone Jenkins           | UCF                   | Big 12            |                 112 |                  0.062 |                 0.464 |            0.086 |
|  95 |         128 | Dru Deshields            | Kent State            | Mid-American      |                 154 |                  0.060 |                 0.403 |            0.018 |
|  96 |          89 | Luke Weaver              | San José State        | Mountain West     |                 210 |                  0.054 |                 0.481 |            0.101 |
|  97 |         116 | Will Crowder             | Troy                  | Sun Belt          |                 138 |                  0.039 |                 0.442 |            0.048 |
|  98 |         113 | D.J. Lagway              | Baylor                | Big 12            |                 149 |                  0.033 |                 0.396 |            0.057 |
|  99 |          93 | Jacurri Brown            | Rice                  | American Athletic |                 143 |                  0.033 |                 0.427 |            0.094 |
| 100 |         114 | Kenny Minchey            | Kentucky              | SEC               |                 196 |                  0.032 |                 0.474 |            0.054 |
| 101 |         115 | Jay Kastantin            | Bowling Green         | Mid-American      |                 153 |                  0.028 |                 0.431 |            0.050 |
| 102 |          64 | Toa Faavae               | New Mexico            | Mountain West     |                  80 |                  0.027 |                 0.362 |            0.169 |
| 103 |          69 | Alberto Mendoza          | Georgia Tech          | ACC               |                 136 |                  0.023 |                 0.485 |            0.143 |
| 104 |          99 | Jaylen Raynor            | Iowa State            | Big 12            |                 115 |                  0.022 |                 0.409 |            0.081 |
| 105 |         112 | Drake Lindsey            | Minnesota             | Big Ten           |                  89 |                  0.020 |                 0.461 |            0.060 |
| 106 |         136 | Noah Kim                 | Eastern Michigan      | Mid-American      |                 202 |                  0.019 |                 0.426 |           -0.002 |
| 107 |          98 | Cibastian Broughton      | Akron                 | Mid-American      |                  53 |                  0.014 |                 0.472 |            0.082 |
| 108 |          48 | Dylan Raiola             | Oregon                | Big Ten           |                  64 |                  0.014 |                 0.375 |            0.211 |
| 109 |          97 | Demond Williams Jr.      | Washington            | Big Ten           |                 175 |                  0.014 |                 0.463 |            0.082 |
| 110 |         104 | Nick Minicucci           | Delaware              | Conference USA    |                  79 |                  0.012 |                 0.430 |            0.070 |
| 111 |         120 | Tyler Hughes             | Wyoming               | Mountain West     |                 174 |                  0.003 |                 0.443 |            0.030 |
| 112 |         129 | Micah Alejado            | Hawai'i               | Mountain West     |                 291 |                 -0.003 |                 0.416 |            0.016 |
| 113 |         134 | Nico Iamaleava           | UCLA                  | Big Ten           |                 132 |                 -0.006 |                 0.432 |            0.001 |
| 114 |         139 | Brayden Roggow           | Akron                 | Mid-American      |                 101 |                 -0.007 |                 0.366 |           -0.022 |
| 115 |         137 | KJ Jackson               | Arkansas              | SEC               |                 157 |                 -0.009 |                 0.427 |           -0.008 |
| 116 |         135 | Skyler Locklear          | Missouri State        | Conference USA    |                 109 |                 -0.011 |                 0.385 |            0.001 |
| 117 |         132 | George MacIntyre         | Tennessee             | SEC               |                  72 |                 -0.014 |                 0.389 |            0.004 |
| 118 |         125 | Malik Washington         | Maryland              | Big Ten           |                 144 |                 -0.028 |                 0.410 |            0.023 |
| 119 |         102 | Cutter Boley             | Arizona State         | Big 12            |                 125 |                 -0.029 |                 0.448 |            0.075 |
| 120 |         147 | Emory Williams           | East Carolina         | American Athletic |                  92 |                 -0.030 |                 0.424 |           -0.080 |
| 121 |         133 | Isaac Wilson             | Colorado              | Big 12            |                  89 |                 -0.031 |                 0.438 |            0.002 |
| 122 |         109 | Byrum Brown              | Auburn                | SEC               |                 199 |                 -0.031 |                 0.407 |            0.061 |
| 123 |         138 | M.Van Buren Jr.          | South Florida         | American Athletic |                 174 |                 -0.040 |                 0.437 |           -0.013 |
| 124 |         118 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |                  66 |                 -0.049 |                 0.409 |            0.042 |
| 125 |         108 | Trey Hedden              | New Mexico State      | Conference USA    |                  89 |                 -0.052 |                 0.382 |            0.064 |
| 126 |         127 | Jackson Brousseau        | California            | ACC               |                  73 |                 -0.053 |                 0.397 |            0.019 |
| 127 |         130 | Brock Glenn              | Western Kentucky      | Conference USA    |                 115 |                 -0.054 |                 0.435 |            0.008 |
| 128 |         103 | Ryder Burton             | UAB                   | American Athletic |                 152 |                 -0.061 |                 0.414 |            0.070 |
| 129 |         110 | Arch Manning             | Texas                 | SEC               |                 140 |                 -0.072 |                 0.421 |            0.061 |
| 130 |         141 | John Mateer              | Oklahoma              | SEC               |                 171 |                 -0.076 |                 0.444 |           -0.027 |
| 131 |         131 | Jaron-Keawe Sagapolutele | California            | ACC               |                 141 |                 -0.077 |                 0.411 |            0.004 |
| 132 |         148 | Caleb Heavner            | Miami (OH)            | Mid-American      |                  86 |                 -0.078 |                 0.372 |           -0.107 |
| 133 |         145 | Quinn Henicle            | Old Dominion          | Sun Belt          |                 134 |                 -0.081 |                 0.388 |           -0.042 |
| 134 |         154 | Tait Reynolds            | Clemson               | ACC               |                 155 |                 -0.086 |                 0.452 |           -0.129 |
| 135 |         149 | Jackson Sharman          | Sacramento State      | Mid-American      |                  67 |                 -0.086 |                 0.403 |           -0.108 |
| 136 |         123 | Alessio Milivojevic      | Michigan State        | Big Ten           |                 155 |                 -0.090 |                 0.439 |            0.026 |
| 137 |          83 | Austin Carlisle          | UL Monroe             | Sun Belt          |                  54 |                 -0.093 |                 0.537 |            0.119 |
| 138 |         155 | Caden Pinnick            | Washington State      | Pac-12            |                 179 |                 -0.107 |                 0.425 |           -0.134 |
| 139 |          87 | Landy Lyddy              | Southern Miss         | Sun Belt          |                  69 |                 -0.111 |                 0.333 |            0.106 |
| 140 |         158 | Kadin Semonza            | Tulane                | American Athletic |                 119 |                 -0.129 |                 0.319 |           -0.149 |
| 141 |         140 | Faizon Brandon           | Tennessee             | SEC               |                  93 |                 -0.136 |                 0.355 |           -0.025 |
| 142 |         151 | Jason Wright             | Buffalo               | Mid-American      |                 143 |                 -0.140 |                 0.392 |           -0.120 |
| 143 |         144 | Marcel Reed              | Texas A&M             | SEC               |                 142 |                 -0.142 |                 0.387 |           -0.041 |
| 144 |         153 | Jayden Denegal           | San Diego State       | Pac-12            |                  97 |                 -0.144 |                 0.361 |           -0.128 |
| 145 |         146 | Landyn Locke             | Sam Houston           | Conference USA    |                 158 |                 -0.148 |                 0.386 |           -0.059 |
| 146 |         152 | Mitch Griffis            | East Carolina         | American Athletic |                  51 |                 -0.156 |                 0.373 |           -0.126 |
| 147 |         150 | H.Geriner                | Pittsburgh            | ACC               |                  63 |                 -0.171 |                 0.349 |           -0.119 |
| 148 |         162 | EJ Colson                | UTEP                  | Mountain West     |                  72 |                 -0.173 |                 0.417 |           -0.174 |
| 149 |         160 | Elijah Holmes            | Buffalo               | Mid-American      |                  68 |                 -0.174 |                 0.368 |           -0.167 |
| 150 |         156 | Carter Jones             | Nevada                | Mountain West     |                  94 |                 -0.205 |                 0.362 |           -0.136 |
| 151 |         161 | Grady Brosterhous        | Utah State            | Pac-12            |                 123 |                 -0.229 |                 0.276 |           -0.173 |
| 152 |         157 | Ethan Hampton            | Southern Miss         | Sun Belt          |                  46 |                 -0.232 |                 0.435 |           -0.142 |
| 153 |         159 | Cole Gonzales            | Charlotte             | American Athletic |                  88 |                 -0.294 |                 0.420 |           -0.161 |

## All plays

|   # | QB                       | Team                  | Conf              |   G |   Dropbacks |   Rushes |   Plays |   EPA/dropback |   EPA/rush |   EPA/play |   Success |   EPA/play (WP 10–90%) |
|----:|:-------------------------|:----------------------|:------------------|----:|------------:|---------:|--------:|---------------:|-----------:|-----------:|----------:|-----------------------:|
|   1 | David McComb             | Miami (OH)            | Mid-American      |   4 |         109 |       11 |     120 |          0.565 |      0.615 |      0.570 |     0.525 |                  0.492 |
|   2 | Darian Mensah            | Miami                 | ACC               |   6 |         169 |       10 |     179 |          0.468 |      0.772 |      0.485 |     0.598 |                  0.575 |
|   3 | Tayven Jackson           | North Texas           | American Athletic |   6 |         199 |       18 |     217 |          0.474 |      0.362 |      0.465 |     0.558 |                  0.528 |
|   4 | Jayden Maiava            | USC                   | Big Ten           |   7 |         231 |       13 |     244 |          0.467 |     -0.319 |      0.425 |     0.570 |                  0.445 |
|   5 | Giovanni Lopez           | Wake Forest           | ACC               |   7 |         210 |       50 |     260 |          0.376 |      0.615 |      0.422 |     0.538 |                  0.569 |
|   6 | Julian Sayin             | Ohio State            | Big Ten           |   7 |         205 |       23 |     228 |          0.408 |      0.481 |      0.416 |     0.566 |                  0.511 |
|   7 | Brad Jackson             | Texas State           | Pac-12            |   6 |         160 |       59 |     219 |          0.431 |      0.365 |      0.413 |     0.562 |                  0.329 |
|   8 | Jared Hollins            | South Alabama         | Sun Belt          |   5 |          95 |       24 |     119 |          0.416 |      0.285 |      0.389 |     0.487 |                  0.555 |
|   9 | Elijah Brown             | Washington            | Big Ten           |   3 |          73 |        2 |      75 |          0.472 |     -2.993 |      0.380 |     0.560 |                  0.144 |
|  10 | Conner Weigman           | Houston               | Big 12            |   7 |         205 |       51 |     256 |          0.395 |      0.315 |      0.379 |     0.566 |                  0.355 |
|  11 | Hauss Hejny              | Colorado State        | Pac-12            |   3 |          74 |       12 |      86 |          0.344 |      0.499 |      0.366 |     0.500 |                  0.277 |
|  12 | Jackson Gutierrez        | Navy                  | American Athletic |   6 |          61 |      112 |     173 |          0.302 |      0.376 |      0.350 |     0.497 |                  0.309 |
|  13 | C.J. Carr                | Notre Dame            | FBS Independents  |   7 |         196 |       20 |     216 |          0.350 |      0.328 |      0.348 |     0.519 |                  0.314 |
|  14 | Josh Hoover              | Indiana               | Big Ten           |   7 |         178 |       17 |     195 |          0.326 |      0.517 |      0.343 |     0.503 |                  0.236 |
|  15 | Lincoln Kienholz         | Louisville            | ACC               |   7 |         194 |       56 |     250 |          0.313 |      0.425 |      0.338 |     0.524 |                  0.307 |
|  16 | Gunner Stockton          | Georgia               | SEC               |   7 |         165 |       26 |     191 |          0.336 |      0.345 |      0.337 |     0.565 |                  0.392 |
|  17 | Kamario Taylor           | Mississippi State     | SEC               |   5 |         167 |       29 |     196 |          0.286 |      0.630 |      0.337 |     0.536 |                  0.355 |
|  18 | Braden Atkinson          | Oregon State          | Pac-12            |   7 |         283 |       13 |     296 |          0.344 |      0.128 |      0.335 |     0.517 |                  0.279 |
|  19 | Avery Johnson            | Kansas State          | Big 12            |   6 |         190 |       47 |     237 |          0.259 |      0.638 |      0.334 |     0.511 |                  0.339 |
|  20 | Kevin Jennings           | SMU                   | ACC               |   6 |         199 |       28 |     227 |          0.368 |      0.073 |      0.332 |     0.537 |                  0.340 |
|  21 | Ajani Sheppard           | Temple                | American Athletic |   7 |         131 |       52 |     183 |          0.294 |      0.425 |      0.331 |     0.492 |                  0.366 |
|  22 | Aidan Chiles             | Northwestern          | Big Ten           |   6 |         155 |       43 |     198 |          0.319 |      0.371 |      0.330 |     0.515 |                  0.284 |
|  23 | Michael Hawkins Jr.      | West Virginia         | Big 12            |   7 |         156 |      130 |     286 |          0.272 |      0.380 |      0.321 |     0.455 |                  0.452 |
|  24 | Aaron Philo              | Florida               | SEC               |   6 |         157 |       35 |     192 |          0.355 |      0.158 |      0.319 |     0.542 |                  0.310 |
|  25 | Noah Fifita              | Arizona               | Big 12            |   6 |         205 |       29 |     234 |          0.315 |      0.274 |      0.310 |     0.534 |                  0.306 |
|  26 | Bishop Davenport         | South Alabama         | Sun Belt          |   2 |          61 |       16 |      77 |          0.302 |      0.328 |      0.307 |     0.481 |                  0.413 |
|  27 | John Alan Richter        | Toledo                | Mid-American      |   7 |         222 |        9 |     231 |          0.329 |     -0.330 |      0.303 |     0.489 |                  0.328 |
|  28 | Mason Heintschel         | Pittsburgh            | ACC               |   5 |         153 |       25 |     178 |          0.348 |     -0.003 |      0.299 |     0.466 |                  0.285 |
|  29 | Ashton Daniels           | Florida State         | ACC               |   7 |         192 |       61 |     253 |          0.209 |      0.582 |      0.299 |     0.466 |                  0.333 |
|  30 | JC French                | Cincinnati            | Big 12            |   6 |         163 |       51 |     214 |          0.295 |      0.286 |      0.293 |     0.547 |                  0.283 |
|  31 | Austin Simmons           | Missouri              | SEC               |   7 |         216 |       11 |     227 |          0.312 |     -0.125 |      0.290 |     0.493 |                  0.319 |
|  32 | William Watson III       | Massachusetts         | Mid-American      |   5 |         104 |       25 |     129 |          0.212 |      0.611 |      0.290 |     0.473 |                  0.345 |
|  33 | Bear Bachmeier           | BYU                   | Big 12            |   6 |         154 |       45 |     199 |          0.195 |      0.612 |      0.289 |     0.533 |                  0.322 |
|  34 | Caden Veltkamp           | Florida Atlantic      | American Athletic |   6 |         234 |       11 |     245 |          0.291 |      0.197 |      0.286 |     0.498 |                  0.201 |
|  35 | Drew Mestemaker          | Oklahoma State        | Big 12            |   6 |         210 |       15 |     225 |          0.248 |      0.814 |      0.286 |     0.542 |                  0.183 |
|  36 | Keelon Russell           | Alabama               | SEC               |   7 |         214 |       37 |     251 |          0.207 |      0.741 |      0.285 |     0.530 |                  0.345 |
|  37 | Cameran Brown            | Georgia State         | Sun Belt          |   6 |         160 |       31 |     191 |          0.292 |      0.246 |      0.285 |     0.513 |                  0.394 |
|  38 | Maddux Madsen            | Boise State           | Pac-12            |   6 |         172 |       24 |     196 |          0.228 |      0.682 |      0.284 |     0.531 |                  0.320 |
|  39 | Trinidad Chambliss       | Ole Miss              | SEC               |   6 |         217 |       28 |     245 |          0.232 |      0.528 |      0.266 |     0.522 |                  0.348 |
|  40 | Tramell Jones Jr.        | Florida               | SEC               |   5 |          66 |       13 |      79 |          0.242 |      0.348 |      0.260 |     0.494 |                  0.167 |
|  41 | Caden Creel              | Jacksonville State    | Conference USA    |   7 |         199 |       90 |     289 |          0.297 |      0.153 |      0.252 |     0.516 |                  0.245 |
|  42 | Dylan Lonergan           | Rutgers               | Big Ten           |   5 |         132 |       15 |     147 |          0.305 |     -0.227 |      0.251 |     0.483 |                  0.279 |
|  43 | AJ Surace                | Rutgers               | Big Ten           |   4 |          61 |        7 |      68 |          0.424 |     -1.385 |      0.237 |     0.456 |                 -0.437 |
|  44 | Katin Houser             | Illinois              | Big Ten           |   6 |         193 |       24 |     217 |          0.194 |      0.584 |      0.237 |     0.525 |                  0.275 |
|  45 | Sam Leavitt              | LSU                   | SEC               |   7 |         220 |       53 |     273 |          0.202 |      0.377 |      0.236 |     0.549 |                  0.178 |
|  46 | CJ Bailey                | NC State              | ACC               |   6 |         198 |       35 |     233 |          0.219 |      0.254 |      0.224 |     0.489 |                  0.292 |
|  47 | Anthony Colandrea        | Nebraska              | Big Ten           |   7 |         234 |       52 |     286 |          0.130 |      0.625 |      0.220 |     0.479 |                  0.124 |
|  48 | Dylan Raiola             | Oregon                | Big Ten           |   4 |          76 |        3 |      79 |          0.219 |      0.013 |      0.211 |     0.468 |                  0.014 |
|  49 | Devon Dampier            | Utah                  | Big 12            |   6 |         182 |       48 |     230 |          0.220 |      0.167 |      0.209 |     0.526 |                  0.387 |
|  50 | Blake Baker              | Louisiana Tech        | Sun Belt          |   5 |         110 |       19 |     129 |          0.226 |      0.096 |      0.206 |     0.457 |                  0.226 |
|  51 | Dante Moore              | Oregon                | Big Ten           |   4 |         106 |        5 |     111 |          0.227 |     -0.230 |      0.206 |     0.459 |                  0.173 |
|  52 | Jared Curtis             | Vanderbilt            | SEC               |   6 |         170 |       42 |     212 |          0.129 |      0.509 |      0.204 |     0.476 |                  0.102 |
|  53 | Isaiah Marshall          | Kansas                | Big 12            |   6 |         173 |       65 |     238 |          0.164 |      0.291 |      0.199 |     0.424 |                  0.210 |
|  54 | Walker Eget              | Duke                  | ACC               |   6 |         176 |        4 |     180 |          0.199 |      0.138 |      0.198 |     0.450 |                  0.186 |
|  55 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |   7 |         246 |       24 |     270 |          0.176 |      0.398 |      0.196 |     0.496 |                  0.292 |
|  56 | Nick Poulos              | Ohio                  | Mid-American      |   4 |          73 |       29 |     102 |          0.116 |      0.393 |      0.195 |     0.520 |                  0.073 |
|  57 | Lanorris Sellers         | South Carolina        | SEC               |   6 |         196 |       52 |     248 |          0.074 |      0.645 |      0.194 |     0.476 |                  0.186 |
|  58 | Marcus Stokes            | Memphis               | American Athletic |   7 |         195 |       45 |     240 |          0.199 |      0.172 |      0.194 |     0.504 |                  0.251 |
|  59 | Malachi Singleton        | App State             | Sun Belt          |   6 |         175 |       27 |     202 |          0.257 |     -0.231 |      0.192 |     0.475 |                  0.113 |
|  60 | Kalieb Osborne           | UConn                 | FBS Independents  |   6 |         178 |       48 |     226 |          0.084 |      0.554 |      0.184 |     0.465 |                  0.355 |
|  61 | Colton Joseph            | Wisconsin             | Big Ten           |   6 |         163 |       59 |     222 |          0.094 |      0.420 |      0.181 |     0.455 |                  0.085 |
|  62 | Trey Owens               | Arkansas State        | Sun Belt          |   7 |         214 |       38 |     252 |          0.162 |      0.252 |      0.176 |     0.536 |                  0.165 |
|  63 | Ryan Browne              | Purdue                | Big Ten           |   7 |         227 |       26 |     253 |          0.149 |      0.396 |      0.175 |     0.502 |                  0.227 |
|  64 | Toa Faavae               | New Mexico            | Mountain West     |   6 |          87 |       36 |     123 |          0.027 |      0.512 |      0.169 |     0.447 |                  0.027 |
|  65 | Camden Coleman           | James Madison         | Sun Belt          |   7 |         182 |       27 |     209 |          0.163 |      0.199 |      0.167 |     0.459 |                  0.284 |
|  66 | Ksaan Farrar             | Colorado State        | Pac-12            |   5 |         148 |       11 |     159 |          0.123 |      0.705 |      0.163 |     0.428 |                 -0.149 |
|  67 | Owen McCown              | UTSA                  | American Athletic |   7 |         228 |       28 |     256 |          0.155 |      0.179 |      0.157 |     0.457 |                  0.218 |
|  68 | Will Hammond             | Texas Tech            | Big 12            |   6 |         176 |       19 |     195 |          0.138 |      0.287 |      0.152 |     0.492 |                  0.225 |
|  69 | Alberto Mendoza          | Georgia Tech          | ACC               |   6 |         204 |       13 |     217 |          0.145 |      0.126 |      0.143 |     0.521 |                  0.023 |
|  70 | Nate Bennett             | Baylor                | Big 12            |   3 |          66 |        2 |      68 |          0.061 |      2.810 |      0.142 |     0.471 |                  0.986 |
|  71 | Matt Vezza               | Ohio                  | Mid-American      |   6 |          70 |       27 |      97 |         -0.091 |      0.736 |      0.139 |     0.515 |                  0.337 |
|  72 | Henry Belin IV           | Missouri State        | Conference USA    |   5 |          76 |       10 |      86 |          0.107 |      0.372 |      0.138 |     0.453 |                  0.193 |
|  73 | Conner Harrell           | Charlotte             | American Athletic |   4 |          77 |        9 |      86 |          0.118 |      0.282 |      0.135 |     0.395 |                  0.288 |
|  74 | Baylor Hayes             | Tulsa                 | American Athletic |   5 |         163 |       23 |     186 |          0.121 |      0.222 |      0.134 |     0.398 |                  0.115 |
|  75 | Jaden Craig              | TCU                   | Big 12            |   6 |         208 |       23 |     231 |          0.150 |     -0.048 |      0.131 |     0.450 |                  0.072 |
|  76 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |   5 |         131 |       19 |     150 |          0.151 |     -0.033 |      0.128 |     0.447 |                  0.077 |
|  77 | Jayden Mandal            | Fresno State          | Pac-12            |   7 |         209 |       34 |     243 |          0.107 |      0.249 |      0.127 |     0.481 |                  0.156 |
|  78 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |   7 |         163 |       87 |     250 |          0.007 |      0.343 |      0.124 |     0.440 |                  0.207 |
|  79 | Rocco Becht              | Penn State            | Big Ten           |   7 |         220 |       32 |     252 |          0.152 |     -0.075 |      0.123 |     0.444 |                  0.076 |
|  80 | Nathan Hayes             | North Dakota State    | Mountain West     |   7 |         172 |       32 |     204 |          0.043 |      0.552 |      0.123 |     0.500 |                  0.299 |
|  81 | Jackson Arnold           | UNLV                  | Mountain West     |   7 |         201 |       87 |     288 |          0.067 |      0.253 |      0.123 |     0.455 |                  0.147 |
|  82 | Bryce Underwood          | Michigan              | Big Ten           |   6 |         134 |       49 |     183 |          0.118 |      0.134 |      0.122 |     0.459 |                  0.155 |
|  83 | Austin Carlisle          | UL Monroe             | Sun Belt          |   4 |          65 |       32 |      97 |         -0.130 |      0.626 |      0.119 |     0.546 |                 -0.093 |
|  84 | Rickie Collins           | Kennesaw State        | Conference USA    |   6 |         193 |       57 |     250 |          0.126 |      0.096 |      0.119 |     0.480 |                  0.104 |
|  85 | Aidan Armenta            | UL Monroe             | Sun Belt          |   5 |         136 |       19 |     155 |          0.112 |      0.152 |      0.117 |     0.465 |                 -0.164 |
|  86 | Hank Brown               | Iowa                  | Big Ten           |   5 |         127 |       13 |     140 |          0.132 |     -0.096 |      0.111 |     0.479 |                  0.066 |
|  87 | Landy Lyddy              | Southern Miss         | Sun Belt          |   6 |         143 |       14 |     157 |          0.095 |      0.222 |      0.106 |     0.414 |                 -0.111 |
|  88 | Malachi Nelson           | Syracuse              | ACC               |   3 |          74 |        6 |      80 |          0.126 |     -0.146 |      0.106 |     0.475 |                  0.164 |
|  89 | Luke Weaver              | San José State        | Mountain West     |   6 |         221 |       38 |     259 |          0.137 |     -0.109 |      0.101 |     0.475 |                  0.054 |
|  90 | Max Johnson              | Georgia Southern      | Sun Belt          |   7 |         238 |       19 |     257 |          0.090 |      0.230 |      0.100 |     0.444 |                  0.123 |
|  91 | Roman Gagliano           | Middle Tennessee      | Conference USA    |   6 |         197 |       16 |     213 |          0.082 |      0.308 |      0.099 |     0.437 |                  0.149 |
|  92 | Davis Warren             | Stanford              | ACC               |   7 |         243 |       10 |     253 |          0.099 |      0.069 |      0.098 |     0.419 |                  0.165 |
|  93 | Jacurri Brown            | Rice                  | American Athletic |   7 |          92 |      103 |     195 |         -0.208 |      0.365 |      0.094 |     0.436 |                  0.033 |
|  94 | Deshawn Purdie           | Liberty               | Conference USA    |   6 |         127 |       24 |     151 |          0.095 |      0.090 |      0.094 |     0.464 |                  0.089 |
|  95 | Beau Pribula             | Virginia              | ACC               |   7 |         180 |       48 |     228 |          0.064 |      0.196 |      0.091 |     0.447 |                  0.179 |
|  96 | Keyone Jenkins           | UCF                   | Big 12            |   6 |         124 |       23 |     147 |          0.107 |     -0.025 |      0.086 |     0.449 |                  0.062 |
|  97 | Demond Williams Jr.      | Washington            | Big Ten           |   6 |         190 |       44 |     234 |          0.013 |      0.383 |      0.082 |     0.462 |                  0.014 |
|  98 | Cibastian Broughton      | Akron                 | Mid-American      |   4 |          71 |       24 |      95 |         -0.057 |      0.491 |      0.082 |     0.474 |                  0.014 |
|  99 | Jaylen Raynor            | Iowa State            | Big 12            |   6 |         157 |       42 |     199 |          0.073 |      0.107 |      0.081 |     0.417 |                  0.022 |
| 100 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |   7 |         222 |       50 |     272 |          0.026 |      0.310 |      0.079 |     0.434 |                  0.104 |
| 101 | J.J. Kohl                | Florida International | Conference USA    |   6 |         208 |       22 |     230 |          0.067 |      0.164 |      0.076 |     0.452 |                  0.124 |
| 102 | Cutter Boley             | Arizona State         | Big 12            |   6 |         177 |       28 |     205 |          0.076 |      0.071 |      0.075 |     0.459 |                 -0.029 |
| 103 | Ryder Burton             | UAB                   | American Athletic |   7 |         182 |       39 |     221 |          0.015 |      0.328 |      0.070 |     0.443 |                 -0.061 |
| 104 | Nick Minicucci           | Delaware              | Conference USA    |   4 |         108 |       12 |     120 |         -0.005 |      0.748 |      0.070 |     0.450 |                  0.012 |
| 105 | Taron Dickens            | Northern Illinois     | Mountain West     |   6 |         204 |       20 |     224 |          0.053 |      0.233 |      0.070 |     0.464 |                  0.070 |
| 106 | Adam Damante             | New Mexico State      | Conference USA    |   4 |          75 |        7 |      82 |          0.007 |      0.729 |      0.069 |     0.476 |                 -0.470 |
| 107 | Billy Edwards            | North Carolina        | ACC               |   6 |         170 |       18 |     188 |          0.058 |      0.140 |      0.066 |     0.495 |                  0.069 |
| 108 | Trey Hedden              | New Mexico State      | Conference USA    |   5 |         132 |        7 |     139 |          0.045 |      0.421 |      0.064 |     0.396 |                 -0.052 |
| 109 | Byrum Brown              | Auburn                | SEC               |   6 |         207 |       82 |     289 |         -0.055 |      0.354 |      0.061 |     0.443 |                 -0.031 |
| 110 | Arch Manning             | Texas                 | SEC               |   6 |         185 |       31 |     216 |          0.081 |     -0.059 |      0.061 |     0.449 |                 -0.072 |
| 111 | Keldric Luster           | Ball State            | Mid-American      |   6 |         193 |       44 |     237 |          0.010 |      0.282 |      0.061 |     0.418 |                  0.153 |
| 112 | Drake Lindsey            | Minnesota             | Big Ten           |   6 |         198 |        8 |     206 |          0.062 |      0.003 |      0.060 |     0.461 |                  0.020 |
| 113 | D.J. Lagway              | Baylor                | Big 12            |   4 |         193 |        5 |     198 |          0.057 |      0.047 |      0.057 |     0.389 |                  0.033 |
| 114 | Kenny Minchey            | Kentucky              | SEC               |   7 |         217 |       22 |     239 |          0.051 |      0.087 |      0.054 |     0.464 |                  0.032 |
| 115 | Jay Kastantin            | Bowling Green         | Mid-American      |   7 |         177 |       28 |     205 |          0.067 |     -0.058 |      0.050 |     0.463 |                  0.028 |
| 116 | Will Crowder             | Troy                  | Sun Belt          |   6 |         180 |       36 |     216 |         -0.045 |      0.514 |      0.048 |     0.440 |                  0.039 |
| 117 | Steven Angeli            | Syracuse              | ACC               |   3 |         111 |        5 |     116 |          0.065 |     -0.327 |      0.048 |     0.405 |                  0.081 |
| 118 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |   5 |          75 |       34 |     109 |         -0.057 |      0.260 |      0.042 |     0.468 |                 -0.049 |
| 119 | Angel H Flores           | Central Michigan      | Mid-American      |   7 |         104 |      116 |     220 |         -0.227 |      0.276 |      0.038 |     0.414 |                  0.065 |
| 120 | Tyler Hughes             | Wyoming               | Mountain West     |   7 |         169 |       71 |     240 |         -0.171 |      0.507 |      0.030 |     0.458 |                  0.003 |
| 121 | Julian Lewis             | Colorado              | Big 12            |   4 |         102 |        6 |     108 |          0.024 |      0.123 |      0.029 |     0.389 |                  0.069 |
| 122 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |   6 |         147 |       51 |     198 |          0.026 |      0.025 |      0.026 |     0.444 |                  0.094 |
| 123 | Alessio Milivojevic      | Michigan State        | Big Ten           |   7 |         200 |       23 |     223 |         -0.005 |      0.289 |      0.026 |     0.480 |                 -0.090 |
| 124 | Broc Lowry               | Western Michigan      | Mid-American      |   7 |         156 |       62 |     218 |         -0.016 |      0.124 |      0.024 |     0.468 |                  0.161 |
| 125 | Malik Washington         | Maryland              | Big Ten           |   7 |         267 |       33 |     300 |          0.006 |      0.162 |      0.023 |     0.423 |                 -0.028 |
| 126 | Mason McKenzie           | Boston College        | ACC               |   6 |         182 |       85 |     267 |         -0.094 |      0.266 |      0.021 |     0.431 |                  0.111 |
| 127 | Jackson Brousseau        | California            | ACC               |   5 |         126 |        7 |     133 |          0.030 |     -0.182 |      0.019 |     0.368 |                 -0.053 |
| 128 | Dru Deshields            | Kent State            | Mid-American      |   7 |         197 |       44 |     241 |         -0.064 |      0.382 |      0.018 |     0.386 |                  0.060 |
| 129 | Micah Alejado            | Hawai'i               | Mountain West     |   7 |         327 |       23 |     350 |          0.014 |      0.034 |      0.016 |     0.434 |                 -0.003 |
| 130 | Brock Glenn              | Western Kentucky      | Conference USA    |   7 |         129 |       68 |     197 |         -0.095 |      0.203 |      0.008 |     0.431 |                 -0.054 |
| 131 | Jaron-Keawe Sagapolutele | California            | ACC               |   6 |         188 |        6 |     194 |          0.013 |     -0.252 |      0.004 |     0.428 |                 -0.077 |
| 132 | George MacIntyre         | Tennessee             | SEC               |   5 |          83 |        1 |      84 |          0.018 |     -1.129 |      0.004 |     0.417 |                 -0.014 |
| 133 | Isaac Wilson             | Colorado              | Big 12            |   4 |         103 |       26 |     129 |          0.098 |     -0.377 |      0.002 |     0.442 |                 -0.031 |
| 134 | Nico Iamaleava           | UCLA                  | Big Ten           |   5 |         124 |       31 |     155 |          0.000 |      0.003 |      0.001 |     0.432 |                 -0.006 |
| 135 | Skyler Locklear          | Missouri State        | Conference USA    |   5 |         117 |       24 |     141 |         -0.034 |      0.169 |      0.001 |     0.376 |                 -0.011 |
| 136 | Noah Kim                 | Eastern Michigan      | Mid-American      |   8 |         292 |       20 |     312 |         -0.004 |      0.033 |     -0.002 |     0.410 |                  0.019 |
| 137 | KJ Jackson               | Arkansas              | SEC               |   7 |         228 |       47 |     275 |         -0.002 |     -0.040 |     -0.008 |     0.451 |                 -0.009 |
| 138 | M.Van Buren Jr.          | South Florida         | American Athletic |   7 |         189 |       36 |     225 |         -0.001 |     -0.075 |     -0.013 |     0.467 |                 -0.040 |
| 139 | Brayden Roggow           | Akron                 | Mid-American      |   7 |         171 |       19 |     190 |         -0.052 |      0.249 |     -0.022 |     0.405 |                 -0.007 |
| 140 | Faizon Brandon           | Tennessee             | SEC               |   5 |         116 |       36 |     152 |         -0.184 |      0.488 |     -0.025 |     0.408 |                 -0.136 |
| 141 | John Mateer              | Oklahoma              | SEC               |   6 |         191 |       50 |     241 |          0.010 |     -0.168 |     -0.027 |     0.432 |                 -0.076 |
| 142 | Dexter Williams II       | Tulsa                 | American Athletic |   5 |          62 |        9 |      71 |         -0.008 |     -0.176 |     -0.029 |     0.423 |                 -0.132 |
| 143 | Raymond Moore III        | UTEP                  | Mountain West     |   7 |          87 |       49 |     136 |         -0.299 |      0.442 |     -0.032 |     0.390 |                 -0.280 |
| 144 | Marcel Reed              | Texas A&M             | SEC               |   7 |         211 |       43 |     254 |         -0.095 |      0.221 |     -0.041 |     0.406 |                 -0.142 |
| 145 | Quinn Henicle            | Old Dominion          | Sun Belt          |   6 |         115 |       67 |     182 |         -0.229 |      0.278 |     -0.042 |     0.390 |                 -0.081 |
| 146 | Landyn Locke             | Sam Houston           | Conference USA    |   6 |         220 |       22 |     242 |         -0.072 |      0.069 |     -0.059 |     0.393 |                 -0.148 |
| 147 | Emory Williams           | East Carolina         | American Athletic |   5 |         108 |       17 |     125 |         -0.076 |     -0.106 |     -0.080 |     0.440 |                 -0.030 |
| 148 | Caleb Heavner            | Miami (OH)            | Mid-American      |   6 |          79 |       28 |     107 |         -0.266 |      0.338 |     -0.107 |     0.383 |                 -0.078 |
| 149 | Jackson Sharman          | Sacramento State      | Mid-American      |   6 |         201 |       15 |     216 |         -0.113 |     -0.039 |     -0.108 |     0.412 |                 -0.086 |
| 150 | H.Geriner                | Pittsburgh            | ACC               |   4 |          72 |        9 |      81 |         -0.087 |     -0.378 |     -0.119 |     0.370 |                 -0.171 |
| 151 | Jason Wright             | Buffalo               | Mid-American      |   6 |         179 |       37 |     216 |         -0.166 |      0.104 |     -0.120 |     0.366 |                 -0.140 |
| 152 | Mitch Griffis            | East Carolina         | American Athletic |   6 |          76 |       20 |      96 |         -0.187 |      0.107 |     -0.126 |     0.396 |                 -0.156 |
| 153 | Jayden Denegal           | San Diego State       | Pac-12            |   7 |         157 |       17 |     174 |         -0.117 |     -0.229 |     -0.128 |     0.351 |                 -0.144 |
| 154 | Tait Reynolds            | Clemson               | ACC               |   6 |         171 |       42 |     213 |         -0.124 |     -0.149 |     -0.129 |     0.418 |                 -0.086 |
| 155 | Caden Pinnick            | Washington State      | Pac-12            |   6 |         195 |       53 |     248 |         -0.202 |      0.114 |     -0.134 |     0.403 |                 -0.107 |
| 156 | Carter Jones             | Nevada                | Mountain West     |   4 |          95 |       21 |     116 |         -0.176 |      0.045 |     -0.136 |     0.371 |                 -0.205 |
| 157 | Ethan Hampton            | Southern Miss         | Sun Belt          |   3 |          76 |        6 |      82 |         -0.119 |     -0.437 |     -0.142 |     0.439 |                 -0.232 |
| 158 | Kadin Semonza            | Tulane                | American Athletic |   5 |         132 |       17 |     149 |         -0.126 |     -0.330 |     -0.149 |     0.309 |                 -0.129 |
| 159 | Cole Gonzales            | Charlotte             | American Athletic |   5 |         129 |       11 |     140 |         -0.110 |     -0.756 |     -0.161 |     0.429 |                 -0.294 |
| 160 | Elijah Holmes            | Buffalo               | Mid-American      |   2 |          64 |        7 |      71 |         -0.181 |     -0.044 |     -0.167 |     0.366 |                 -0.174 |
| 161 | Grady Brosterhous        | Utah State            | Pac-12            |   6 |         162 |       70 |     232 |         -0.157 |     -0.212 |     -0.173 |     0.328 |                 -0.229 |
| 162 | EJ Colson                | UTEP                  | Mountain West     |   6 |         100 |       55 |     155 |         -0.247 |     -0.041 |     -0.174 |     0.439 |                 -0.173 |
| 163 | Ryan Huff                | Old Dominion          | Sun Belt          |   4 |          77 |        6 |      83 |         -0.237 |      0.107 |     -0.212 |     0.289 |                 -0.395 |
