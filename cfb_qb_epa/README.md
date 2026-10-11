# 2026 CFB QB EPA — through Week 6

FBS offenses, games through Oct 10, 2026 (Week 0 games are folded into Week 1).
**Minimum 60 dropbacks**, which leaves 153 QBs. Sorted by EPA/play over all dropbacks + QB rushes.

- **Dropbacks** = pass attempts + sacks. **Rushes** = designed runs + scrambles.
- **Success** = share of plays with positive EPA.
- **EPA/play (WP 10–90%)** leaves out garbage time.
- Not opponent-adjusted, so a team that has played FCS opponents looks better.
- Source: cfbfastR play-by-play (`sportsdataverse/cfbfastR-data`, `data/rds/pbp_players_pos_2026.rds`). Rebuild with `python qb_epa.py <rds> [min_dropbacks]` then `python make_readme.py <week> "<through date>"`.

Full tables: [`qb_epa_2026.csv`](qb_epa_2026.csv), [`qb_epa_2026_nongarbage.csv`](qb_epa_2026_nongarbage.csv)

## Non-garbage time (win probability 10–90%)

Same 60-dropback pool, plus at least 40 plays in competitive game states (146 QBs).

|   # |   Overall # | QB                       | Team                  | Conf              |   Plays (WP 10–90%) |   EPA/play (WP 10–90%) |   Success (WP 10–90%) |   EPA/play (all) |
|----:|------------:|:-------------------------|:----------------------|:------------------|--------------------:|-----------------------:|----------------------:|-----------------:|
|   1 |           2 | Darian Mensah            | Miami                 | ACC               |                  70 |                  0.698 |                 0.671 |            0.522 |
|   2 |           3 | Julian Sayin             | Ohio State            | Big Ten           |                 106 |                  0.649 |                 0.594 |            0.475 |
|   3 |          10 | Jared Hollins            | South Alabama         | Sun Belt          |                  69 |                  0.555 |                 0.536 |            0.389 |
|   4 |           9 | Gunner Stockton          | Georgia               | SEC               |                  79 |                  0.543 |                 0.557 |            0.401 |
|   5 |          32 | Devon Dampier            | Utah                  | Big 12            |                  81 |                  0.530 |                 0.617 |            0.274 |
|   6 |           4 | Tayven Jackson           | North Texas           | American Athletic |                 139 |                  0.528 |                 0.554 |            0.465 |
|   7 |           7 | Giovanni Lopez           | Wake Forest           | ACC               |                 138 |                  0.515 |                 0.558 |            0.419 |
|   8 |           1 | David McComb             | Miami (OH)            | Mid-American      |                  81 |                  0.492 |                 0.519 |            0.570 |
|   9 |          11 | Keelon Russell           | Alabama               | SEC               |                 140 |                  0.477 |                 0.550 |            0.384 |
|  10 |          14 | Marcus Stokes            | Memphis               | American Athletic |                 131 |                  0.465 |                 0.534 |            0.356 |
|  11 |           6 | Jayden Maiava            | USC                   | Big Ten           |                 182 |                  0.445 |                 0.549 |            0.425 |
|  12 |          38 | Michael Hawkins Jr.      | West Virginia         | Big 12            |                 150 |                  0.430 |                 0.473 |            0.261 |
|  13 |          28 | Bishop Davenport         | South Alabama         | Sun Belt          |                  59 |                  0.413 |                 0.525 |            0.307 |
|  14 |           8 | C.J. Carr                | Notre Dame            | FBS Independents  |                  91 |                  0.398 |                 0.538 |            0.406 |
|  15 |          19 | Avery Johnson            | Kansas State          | Big 12            |                 120 |                  0.377 |                 0.517 |            0.338 |
|  16 |           5 | Josh Hoover              | Indiana               | Big Ten           |                 103 |                  0.376 |                 0.524 |            0.436 |
|  17 |          23 | Cameran Brown            | Georgia State         | Sun Belt          |                  96 |                  0.374 |                 0.562 |            0.324 |
|  18 |          22 | Bear Bachmeier           | BYU                   | Big 12            |                 107 |                  0.373 |                 0.533 |            0.330 |
|  19 |          40 | Trinidad Chambliss       | Ole Miss              | SEC               |                 145 |                  0.363 |                 0.559 |            0.255 |
|  20 |          20 | Kamario Taylor           | Mississippi State     | SEC               |                 120 |                  0.355 |                 0.542 |            0.337 |
|  21 |          58 | Kalieb Osborne           | UConn                 | FBS Independents  |                 138 |                  0.355 |                 0.507 |            0.184 |
|  22 |          30 | William Watson III       | Massachusetts         | Mid-American      |                  77 |                  0.345 |                 0.468 |            0.290 |
|  23 |          16 | Kevin Jennings           | SMU                   | ACC               |                 153 |                  0.340 |                 0.575 |            0.349 |
|  24 |          52 | Matt Vezza               | Ohio                  | Mid-American      |                  82 |                  0.337 |                 0.549 |            0.208 |
|  25 |          18 | Austin Simmons           | Missouri              | SEC               |                 147 |                  0.328 |                 0.503 |            0.340 |
|  26 |          37 | Ashton Daniels           | Florida State         | ACC               |                 142 |                  0.323 |                 0.479 |            0.262 |
|  27 |          31 | Maddux Madsen            | Boise State           | Pac-12            |                 159 |                  0.320 |                 0.535 |            0.284 |
|  28 |          73 | Nathan Hayes             | North Dakota State    | Mountain West     |                 103 |                  0.318 |                 0.505 |            0.128 |
|  29 |          25 | Aaron Philo              | Florida               | SEC               |                 129 |                  0.310 |                 0.558 |            0.319 |
|  30 |          15 | Braden Atkinson          | Oregon State          | Pac-12            |                 133 |                  0.306 |                 0.511 |            0.356 |
|  31 |          27 | Noah Fifita              | Arizona               | Big 12            |                 159 |                  0.306 |                 0.553 |            0.310 |
|  32 |          17 | Brad Jackson             | Texas State           | Pac-12            |                 137 |                  0.297 |                 0.533 |            0.342 |
|  33 |          36 | Ajani Sheppard           | Temple                | American Athletic |                 129 |                  0.296 |                 0.473 |            0.263 |
|  34 |          13 | Aidan Chiles             | Northwestern          | Big Ten           |                  93 |                  0.294 |                 0.505 |            0.362 |
|  35 |          46 | CJ Bailey                | NC State              | ACC               |                 128 |                  0.292 |                 0.500 |            0.224 |
|  36 |          29 | Mason Heintschel         | Pittsburgh            | ACC               |                 101 |                  0.285 |                 0.446 |            0.299 |
|  37 |          12 | Hauss Hejny              | Colorado State        | Pac-12            |                  56 |                  0.277 |                 0.500 |            0.366 |
|  38 |          21 | Conner Weigman           | Houston               | Big 12            |                 152 |                  0.275 |                 0.526 |            0.332 |
|  39 |          43 | Katin Houser             | Illinois              | Big Ten           |                 127 |                  0.275 |                 0.535 |            0.237 |
|  40 |          24 | Lincoln Kienholz         | Louisville            | ACC               |                 178 |                  0.265 |                 0.517 |            0.320 |
|  41 |          34 | John Alan Richter        | Toledo                | Mid-American      |                 129 |                  0.261 |                 0.465 |            0.273 |
|  42 |          71 | Camden Coleman           | James Madison         | Sun Belt          |                 108 |                  0.260 |                 0.491 |            0.134 |
|  43 |          35 | Caden Creel              | Jacksonville State    | Conference USA    |                 188 |                  0.258 |                 0.505 |            0.270 |
|  44 |          62 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |                 141 |                  0.255 |                 0.454 |            0.172 |
|  45 |          56 | Jayden Mandal            | Fresno State          | Pac-12            |                 148 |                  0.249 |                 0.486 |            0.202 |
|  46 |          47 | Ryan Browne              | Purdue                | Big Ten           |                 150 |                  0.244 |                 0.513 |            0.223 |
|  47 |          60 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |                 155 |                  0.225 |                 0.516 |            0.178 |
|  48 |          50 | Isaiah Marshall          | Kansas                | Big 12            |                 122 |                  0.225 |                 0.418 |            0.213 |
|  49 |          51 | Trey Owens               | Arkansas State        | Sun Belt          |                 168 |                  0.224 |                 0.560 |            0.210 |
|  50 |          26 | Anthony Colandrea        | Nebraska              | Big Ten           |                 181 |                  0.222 |                 0.475 |            0.316 |
|  51 |          48 | Walker Eget              | Duke                  | ACC               |                 118 |                  0.220 |                 0.466 |            0.213 |
|  52 |          41 | Drew Mestemaker          | Oklahoma State        | Big 12            |                 146 |                  0.218 |                 0.514 |            0.242 |
|  53 |          63 | Blake Baker              | Louisiana Tech        | Sun Belt          |                  64 |                  0.209 |                 0.484 |            0.171 |
|  54 |          67 | Bryce Underwood          | Michigan              | Big Ten           |                 153 |                  0.192 |                 0.510 |            0.154 |
|  55 |          57 | Lanorris Sellers         | South Carolina        | SEC               |                 146 |                  0.186 |                 0.459 |            0.194 |
|  56 |          84 | Davis Warren             | Stanford              | ACC               |                 127 |                  0.177 |                 0.409 |            0.089 |
|  57 |          80 | Beau Pribula             | Virginia              | ACC               |                 122 |                  0.176 |                 0.467 |            0.101 |
|  58 |          53 | Dante Moore              | Oregon                | Big Ten           |                  90 |                  0.173 |                 0.400 |            0.206 |
|  59 |          59 | Rocco Becht              | Penn State            | Big Ten           |                 122 |                  0.172 |                 0.393 |            0.183 |
|  60 |          33 | Caden Veltkamp           | Florida Atlantic      | American Athletic |                 111 |                  0.166 |                 0.450 |            0.274 |
|  61 |          49 | JC French                | Cincinnati            | Big 12            |                 119 |                  0.164 |                 0.513 |            0.213 |
|  62 |          82 | Will Hammond             | Texas Tech            | Big 12            |                 118 |                  0.160 |                 0.508 |            0.096 |
|  63 |         108 | Broc Lowry               | Western Michigan      | Mid-American      |                 142 |                  0.155 |                 0.500 |            0.043 |
|  64 |         115 | Angel H Flores           | Central Michigan      | Mid-American      |                  97 |                  0.147 |                 0.392 |            0.033 |
|  65 |          39 | Jared Curtis             | Vanderbilt            | SEC               |                 105 |                  0.146 |                 0.448 |            0.257 |
|  66 |          66 | Dylan Lonergan           | Rutgers               | Big Ten           |                  54 |                  0.135 |                 0.444 |            0.155 |
|  67 |          79 | Max Johnson              | Georgia Southern      | Sun Belt          |                 172 |                  0.129 |                 0.465 |            0.104 |
|  68 |          44 | Colton Joseph            | Wisconsin             | Big Ten           |                  98 |                  0.128 |                 0.429 |            0.231 |
|  69 |          54 | Sam Leavitt              | LSU                   | SEC               |                 153 |                  0.127 |                 0.510 |            0.205 |
|  70 |          95 | Owen McCown              | UTSA                  | American Athletic |                 177 |                  0.126 |                 0.463 |            0.074 |
|  71 |         105 | Taron Dickens            | Northern Illinois     | Mountain West     |                  89 |                  0.121 |                 0.528 |            0.049 |
|  72 |          77 | D.J. Lagway              | Baylor                | Big 12            |                 109 |                  0.116 |                 0.440 |            0.120 |
|  73 |          74 | Rickie Collins           | Kennesaw State        | Conference USA    |                 116 |                  0.108 |                 0.440 |            0.125 |
|  74 |         126 | Emory Williams           | East Carolina         | American Athletic |                  61 |                  0.105 |                 0.426 |           -0.001 |
|  75 |          96 | Will Crowder             | Troy                  | Sun Belt          |                 125 |                  0.099 |                 0.464 |            0.071 |
|  76 |          70 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |                  47 |                  0.097 |                 0.468 |            0.134 |
|  77 |         107 | Roman Gagliano           | Middle Tennessee      | Conference USA    |                 133 |                  0.096 |                 0.444 |            0.047 |
|  78 |         118 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |                 146 |                  0.094 |                 0.473 |            0.026 |
|  79 |          83 | Deshawn Purdie           | Liberty               | Conference USA    |                 113 |                  0.089 |                 0.478 |            0.094 |
|  80 |         123 | Keldric Luster           | Ball State            | Mid-American      |                  71 |                  0.083 |                 0.451 |            0.001 |
|  81 |         106 | Steven Angeli            | Syracuse              | ACC               |                  84 |                  0.081 |                 0.381 |            0.048 |
|  82 |         104 | Jackson Arnold           | UNLV                  | Mountain West     |                 196 |                  0.074 |                 0.418 |            0.055 |
|  83 |         111 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |                 147 |                  0.073 |                 0.469 |            0.036 |
|  84 |         109 | Dru Deshields            | Kent State            | Mid-American      |                 125 |                  0.073 |                 0.400 |            0.043 |
|  85 |         116 | Julian Lewis             | Colorado              | Big 12            |                  70 |                  0.069 |                 0.400 |            0.029 |
|  86 |          78 | Hank Brown               | Iowa                  | Big Ten           |                 110 |                  0.066 |                 0.455 |            0.111 |
|  87 |          55 | Jackson Brousseau        | California            | ACC               |                  58 |                  0.065 |                 0.431 |            0.203 |
|  88 |          86 | Keyone Jenkins           | UCF                   | Big 12            |                 112 |                  0.062 |                 0.464 |            0.086 |
|  89 |         131 | Mason McKenzie           | Boston College        | ACC               |                 157 |                  0.057 |                 0.433 |           -0.024 |
|  90 |          81 | Luke Weaver              | San José State        | Mountain West     |                 210 |                  0.054 |                 0.481 |            0.101 |
|  91 |          65 | Malachi Singleton        | App State             | Sun Belt          |                 110 |                  0.052 |                 0.427 |            0.162 |
|  92 |          94 | Cutter Boley             | Arizona State         | Big 12            |                 122 |                  0.050 |                 0.451 |            0.076 |
|  93 |          98 | Kenny Minchey            | Kentucky              | SEC               |                 161 |                  0.047 |                 0.484 |            0.070 |
|  94 |         121 | J.J. Kohl                | Florida International | Conference USA    |                 139 |                  0.043 |                 0.439 |            0.001 |
|  95 |         127 | Noah Kim                 | Eastern Michigan      | Mid-American      |                 189 |                  0.038 |                 0.429 |           -0.007 |
|  96 |         133 | Isaac Wilson             | Colorado              | Big 12            |                  65 |                  0.037 |                 0.477 |           -0.025 |
|  97 |          61 | Toa Faavae               | New Mexico            | Mountain West     |                  61 |                  0.034 |                 0.361 |            0.178 |
|  98 |          87 | Billy Edwards            | North Carolina        | ACC               |                 120 |                  0.030 |                 0.492 |            0.084 |
|  99 |          75 | Alberto Mendoza          | Georgia Tech          | ACC               |                 127 |                  0.029 |                 0.480 |            0.125 |
| 100 |         114 | Jay Kastantin            | Bowling Green         | Mid-American      |                 123 |                  0.024 |                 0.431 |            0.034 |
| 101 |          91 | Jaylen Raynor            | Iowa State            | Big 12            |                 115 |                  0.022 |                 0.409 |            0.081 |
| 102 |          76 | Jaden Craig              | TCU                   | Big 12            |                 143 |                  0.022 |                 0.434 |            0.124 |
| 103 |         102 | Drake Lindsey            | Minnesota             | Big Ten           |                  89 |                  0.020 |                 0.461 |            0.060 |
| 104 |          92 | Brock Glenn              | Western Kentucky      | Conference USA    |                  70 |                  0.016 |                 0.486 |            0.079 |
| 105 |          90 | Cibastian Broughton      | Akron                 | Mid-American      |                  53 |                  0.014 |                 0.472 |            0.082 |
| 106 |          89 | Demond Williams Jr.      | Washington            | Big Ten           |                 175 |                  0.014 |                 0.463 |            0.082 |
| 107 |          97 | Nick Minicucci           | Delaware              | Conference USA    |                  79 |                  0.012 |                 0.430 |            0.070 |
| 108 |         112 | Baylor Hayes             | Tulsa                 | American Athletic |                 144 |                  0.009 |                 0.354 |            0.035 |
| 109 |         113 | Micah Alejado            | Hawai'i               | Mountain West     |                 248 |                  0.003 |                 0.423 |            0.035 |
| 110 |          64 | Landy Lyddy              | Southern Miss         | Sun Belt          |                  41 |                  0.002 |                 0.390 |            0.171 |
| 111 |          85 | Arch Manning             | Texas                 | SEC               |                 119 |                 -0.005 |                 0.412 |            0.087 |
| 112 |         122 | Nico Iamaleava           | UCLA                  | Big Ten           |                 132 |                 -0.006 |                 0.432 |            0.001 |
| 113 |          88 | Ryder Burton             | UAB                   | American Athletic |                 125 |                 -0.010 |                 0.424 |            0.082 |
| 114 |         124 | Skyler Locklear          | Missouri State        | Conference USA    |                 109 |                 -0.011 |                 0.385 |            0.001 |
| 115 |          99 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |                  63 |                 -0.014 |                 0.413 |            0.069 |
| 116 |          93 | Jacurri Brown            | Rice                  | American Athletic |                 129 |                 -0.025 |                 0.411 |            0.077 |
| 117 |         119 | M.Van Buren Jr.          | South Florida         | American Athletic |                 147 |                 -0.027 |                 0.435 |            0.024 |
| 118 |         117 | Landyn Locke             | Sam Houston           | Conference USA    |                 127 |                 -0.044 |                 0.441 |            0.029 |
| 119 |         101 | Trey Hedden              | New Mexico State      | Conference USA    |                  89 |                 -0.052 |                 0.382 |            0.064 |
| 120 |         128 | Malik Washington         | Maryland              | Big Ten           |                 116 |                 -0.058 |                 0.388 |           -0.007 |
| 121 |         136 | Tyler Hughes             | Wyoming               | Mountain West     |                 157 |                 -0.062 |                 0.439 |           -0.068 |
| 122 |         125 | John Mateer              | Oklahoma              | SEC               |                 124 |                 -0.062 |                 0.435 |           -0.001 |
| 123 |         135 | Jackson Sharman          | Sacramento State      | Mid-American      |                  52 |                 -0.063 |                 0.365 |           -0.065 |
| 124 |         134 | KJ Jackson               | Arkansas              | SEC               |                 117 |                 -0.065 |                 0.410 |           -0.049 |
| 125 |         129 | Brayden Roggow           | Akron                 | Mid-American      |                  66 |                 -0.066 |                 0.379 |           -0.016 |
| 126 |         139 | Caleb Heavner            | Miami (OH)            | Mid-American      |                  70 |                 -0.070 |                 0.371 |           -0.095 |
| 127 |         130 | Jaron-Keawe Sagapolutele | California            | ACC               |                 141 |                 -0.077 |                 0.411 |           -0.024 |
| 128 |         110 | Byrum Brown              | Auburn                | SEC               |                 152 |                 -0.078 |                 0.401 |            0.039 |
| 129 |          72 | Austin Carlisle          | UL Monroe             | Sun Belt          |                  54 |                 -0.093 |                 0.537 |            0.131 |
| 130 |         147 | Tait Reynolds            | Clemson               | ACC               |                 146 |                 -0.102 |                 0.445 |           -0.150 |
| 131 |         143 | Caden Pinnick            | Washington State      | Pac-12            |                 179 |                 -0.107 |                 0.425 |           -0.134 |
| 132 |         146 | Kadin Semonza            | Tulane                | American Athletic |                 119 |                 -0.129 |                 0.319 |           -0.149 |
| 133 |         137 | Quinn Henicle            | Old Dominion          | Sun Belt          |                 117 |                 -0.133 |                 0.368 |           -0.076 |
| 134 |         120 | Alessio Milivojevic      | Michigan State        | Big Ten           |                 118 |                 -0.134 |                 0.424 |            0.020 |
| 135 |         140 | Jason Wright             | Buffalo               | Mid-American      |                 104 |                 -0.134 |                 0.404 |           -0.112 |
| 136 |         132 | Faizon Brandon           | Tennessee             | SEC               |                  93 |                 -0.136 |                 0.355 |           -0.025 |
| 137 |         142 | Mitch Griffis            | East Carolina         | American Athletic |                  50 |                 -0.150 |                 0.380 |           -0.123 |
| 138 |         141 | H.Geriner                | Pittsburgh            | ACC               |                  63 |                 -0.171 |                 0.349 |           -0.119 |
| 139 |         149 | Elijah Holmes            | Buffalo               | Mid-American      |                  68 |                 -0.174 |                 0.368 |           -0.167 |
| 140 |         138 | Marcel Reed              | Texas A&M             | SEC               |                 135 |                 -0.179 |                 0.370 |           -0.080 |
| 141 |         144 | Carter Jones             | Nevada                | Mountain West     |                  94 |                 -0.205 |                 0.362 |           -0.136 |
| 142 |         152 | EJ Colson                | UTEP                  | Mountain West     |                  58 |                 -0.226 |                 0.397 |           -0.196 |
| 143 |         150 | Jayden Denegal           | San Diego State       | Pac-12            |                  84 |                 -0.227 |                 0.333 |           -0.170 |
| 144 |         151 | Grady Brosterhous        | Utah State            | Pac-12            |                 123 |                 -0.229 |                 0.276 |           -0.173 |
| 145 |         145 | Ethan Hampton            | Southern Miss         | Sun Belt          |                  46 |                 -0.232 |                 0.435 |           -0.142 |
| 146 |         148 | Cole Gonzales            | Charlotte             | American Athletic |                  88 |                 -0.294 |                 0.420 |           -0.161 |

## All plays

|   # | QB                       | Team                  | Conf              |   G |   Dropbacks |   Rushes |   Plays |   EPA/dropback |   EPA/rush |   EPA/play |   Success |   EPA/play (WP 10–90%) |
|----:|:-------------------------|:----------------------|:------------------|----:|------------:|---------:|--------:|---------------:|-----------:|-----------:|----------:|-----------------------:|
|   1 | David McComb             | Miami (OH)            | Mid-American      |   4 |         109 |       11 |     120 |          0.565 |      0.615 |      0.570 |     0.525 |                  0.492 |
|   2 | Darian Mensah            | Miami                 | ACC               |   5 |         136 |        8 |     144 |          0.489 |      1.091 |      0.522 |     0.625 |                  0.698 |
|   3 | Julian Sayin             | Ohio State            | Big Ten           |   6 |         173 |       21 |     194 |          0.472 |      0.494 |      0.475 |     0.577 |                  0.649 |
|   4 | Tayven Jackson           | North Texas           | American Athletic |   6 |         199 |       18 |     217 |          0.474 |      0.362 |      0.465 |     0.558 |                  0.528 |
|   5 | Josh Hoover              | Indiana               | Big Ten           |   6 |         137 |       14 |     151 |          0.425 |      0.540 |      0.436 |     0.530 |                  0.376 |
|   6 | Jayden Maiava            | USC                   | Big Ten           |   7 |         231 |       13 |     244 |          0.467 |     -0.319 |      0.425 |     0.570 |                  0.445 |
|   7 | Giovanni Lopez           | Wake Forest           | ACC               |   6 |         189 |       42 |     231 |          0.371 |      0.636 |      0.419 |     0.541 |                  0.515 |
|   8 | C.J. Carr                | Notre Dame            | FBS Independents  |   6 |         147 |       15 |     162 |          0.398 |      0.485 |      0.406 |     0.543 |                  0.398 |
|   9 | Gunner Stockton          | Georgia               | SEC               |   6 |         129 |       20 |     149 |          0.421 |      0.270 |      0.401 |     0.564 |                  0.543 |
|  10 | Jared Hollins            | South Alabama         | Sun Belt          |   5 |          95 |       24 |     119 |          0.416 |      0.285 |      0.389 |     0.487 |                  0.555 |
|  11 | Keelon Russell           | Alabama               | SEC               |   6 |         179 |       31 |     210 |          0.312 |      0.798 |      0.384 |     0.552 |                  0.477 |
|  12 | Hauss Hejny              | Colorado State        | Pac-12            |   3 |          74 |       12 |      86 |          0.344 |      0.499 |      0.366 |     0.500 |                  0.277 |
|  13 | Aidan Chiles             | Northwestern          | Big Ten           |   5 |         122 |       32 |     154 |          0.360 |      0.372 |      0.362 |     0.519 |                  0.294 |
|  14 | Marcus Stokes            | Memphis               | American Athletic |   6 |         152 |       37 |     189 |          0.383 |      0.247 |      0.356 |     0.534 |                  0.465 |
|  15 | Braden Atkinson          | Oregon State          | Pac-12            |   6 |         244 |       10 |     254 |          0.368 |      0.050 |      0.356 |     0.539 |                  0.306 |
|  16 | Kevin Jennings           | SMU                   | ACC               |   5 |         162 |       25 |     187 |          0.396 |      0.043 |      0.349 |     0.551 |                  0.340 |
|  17 | Brad Jackson             | Texas State           | Pac-12            |   5 |         141 |       46 |     187 |          0.406 |      0.145 |      0.342 |     0.529 |                  0.297 |
|  18 | Austin Simmons           | Missouri              | SEC               |   6 |         170 |       10 |     180 |          0.367 |     -0.119 |      0.340 |     0.511 |                  0.328 |
|  19 | Avery Johnson            | Kansas State          | Big 12            |   5 |         165 |       36 |     201 |          0.273 |      0.636 |      0.338 |     0.512 |                  0.377 |
|  20 | Kamario Taylor           | Mississippi State     | SEC               |   5 |         167 |       29 |     196 |          0.286 |      0.630 |      0.337 |     0.536 |                  0.355 |
|  21 | Conner Weigman           | Houston               | Big 12            |   6 |         170 |       43 |     213 |          0.349 |      0.267 |      0.332 |     0.554 |                  0.275 |
|  22 | Bear Bachmeier           | BYU                   | Big 12            |   5 |         119 |       32 |     151 |          0.206 |      0.790 |      0.330 |     0.550 |                  0.373 |
|  23 | Cameran Brown            | Georgia State         | Sun Belt          |   5 |         133 |       24 |     157 |          0.360 |      0.119 |      0.324 |     0.529 |                  0.374 |
|  24 | Lincoln Kienholz         | Louisville            | ACC               |   6 |         165 |       50 |     215 |          0.313 |      0.342 |      0.320 |     0.530 |                  0.265 |
|  25 | Aaron Philo              | Florida               | SEC               |   6 |         157 |       35 |     192 |          0.355 |      0.158 |      0.319 |     0.542 |                  0.310 |
|  26 | Anthony Colandrea        | Nebraska              | Big Ten           |   6 |         197 |       42 |     239 |          0.215 |      0.791 |      0.316 |     0.515 |                  0.222 |
|  27 | Noah Fifita              | Arizona               | Big 12            |   6 |         205 |       29 |     234 |          0.315 |      0.274 |      0.310 |     0.534 |                  0.306 |
|  28 | Bishop Davenport         | South Alabama         | Sun Belt          |   2 |          61 |       16 |      77 |          0.302 |      0.328 |      0.307 |     0.481 |                  0.413 |
|  29 | Mason Heintschel         | Pittsburgh            | ACC               |   5 |         153 |       25 |     178 |          0.348 |     -0.003 |      0.299 |     0.466 |                  0.285 |
|  30 | William Watson III       | Massachusetts         | Mid-American      |   5 |         104 |       25 |     129 |          0.212 |      0.611 |      0.290 |     0.473 |                  0.345 |
|  31 | Maddux Madsen            | Boise State           | Pac-12            |   6 |         172 |       24 |     196 |          0.228 |      0.682 |      0.284 |     0.531 |                  0.320 |
|  32 | Devon Dampier            | Utah                  | Big 12            |   5 |         138 |       43 |     181 |          0.289 |      0.229 |      0.274 |     0.558 |                  0.530 |
|  33 | Caden Veltkamp           | Florida Atlantic      | American Athletic |   5 |         184 |       10 |     194 |          0.275 |      0.252 |      0.274 |     0.505 |                  0.166 |
|  34 | John Alan Richter        | Toledo                | Mid-American      |   6 |         192 |        6 |     198 |          0.300 |     -0.589 |      0.273 |     0.465 |                  0.261 |
|  35 | Caden Creel              | Jacksonville State    | Conference USA    |   6 |         176 |       72 |     248 |          0.302 |      0.192 |      0.270 |     0.524 |                  0.258 |
|  36 | Ajani Sheppard           | Temple                | American Athletic |   6 |         107 |       47 |     154 |          0.243 |      0.307 |      0.263 |     0.468 |                  0.296 |
|  37 | Ashton Daniels           | Florida State         | ACC               |   6 |         168 |       54 |     222 |          0.149 |      0.612 |      0.262 |     0.473 |                  0.323 |
|  38 | Michael Hawkins Jr.      | West Virginia         | Big 12            |   6 |         120 |      107 |     227 |          0.098 |      0.444 |      0.261 |     0.436 |                  0.430 |
|  39 | Jared Curtis             | Vanderbilt            | SEC               |   5 |         138 |       35 |     173 |          0.166 |      0.613 |      0.257 |     0.486 |                  0.146 |
|  40 | Trinidad Chambliss       | Ole Miss              | SEC               |   5 |         181 |       25 |     206 |          0.211 |      0.576 |      0.255 |     0.539 |                  0.363 |
|  41 | Drew Mestemaker          | Oklahoma State        | Big 12            |   5 |         175 |       11 |     186 |          0.198 |      0.951 |      0.242 |     0.538 |                  0.218 |
|  42 | AJ Surace                | Rutgers               | Big Ten           |   4 |          61 |        7 |      68 |          0.424 |     -1.385 |      0.237 |     0.456 |                 -0.437 |
|  43 | Katin Houser             | Illinois              | Big Ten           |   6 |         193 |       24 |     217 |          0.194 |      0.584 |      0.237 |     0.525 |                  0.275 |
|  44 | Colton Joseph            | Wisconsin             | Big Ten           |   5 |         145 |       45 |     190 |          0.174 |      0.416 |      0.231 |     0.468 |                  0.128 |
|  45 | Aidan Armenta            | UL Monroe             | Sun Belt          |   4 |         112 |       17 |     129 |          0.273 |     -0.079 |      0.227 |     0.473 |                 -0.178 |
|  46 | CJ Bailey                | NC State              | ACC               |   6 |         198 |       35 |     233 |          0.219 |      0.254 |      0.224 |     0.489 |                  0.292 |
|  47 | Ryan Browne              | Purdue                | Big Ten           |   6 |         183 |       20 |     203 |          0.207 |      0.371 |      0.223 |     0.522 |                  0.244 |
|  48 | Walker Eget              | Duke                  | ACC               |   5 |         135 |        4 |     139 |          0.215 |      0.138 |      0.213 |     0.460 |                  0.220 |
|  49 | JC French                | Cincinnati            | Big 12            |   5 |         131 |       41 |     172 |          0.175 |      0.334 |      0.213 |     0.529 |                  0.164 |
|  50 | Isaiah Marshall          | Kansas                | Big 12            |   5 |         146 |       53 |     199 |          0.207 |      0.229 |      0.213 |     0.427 |                  0.225 |
|  51 | Trey Owens               | Arkansas State        | Sun Belt          |   6 |         184 |       28 |     212 |          0.182 |      0.395 |      0.210 |     0.557 |                  0.224 |
|  52 | Matt Vezza               | Ohio                  | Mid-American      |   5 |          66 |       27 |      93 |         -0.007 |      0.736 |      0.208 |     0.538 |                  0.337 |
|  53 | Dante Moore              | Oregon                | Big Ten           |   4 |         106 |        5 |     111 |          0.227 |     -0.230 |      0.206 |     0.459 |                  0.173 |
|  54 | Sam Leavitt              | LSU                   | SEC               |   6 |         182 |       50 |     232 |          0.141 |      0.436 |      0.205 |     0.530 |                  0.127 |
|  55 | Jackson Brousseau        | California            | ACC               |   4 |          94 |        3 |      97 |          0.199 |      0.334 |      0.203 |     0.423 |                  0.065 |
|  56 | Jayden Mandal            | Fresno State          | Pac-12            |   6 |         178 |       31 |     209 |          0.194 |      0.246 |      0.202 |     0.498 |                  0.249 |
|  57 | Lanorris Sellers         | South Carolina        | SEC               |   6 |         196 |       52 |     248 |          0.074 |      0.645 |      0.194 |     0.476 |                  0.186 |
|  58 | Kalieb Osborne           | UConn                 | FBS Independents  |   6 |         178 |       48 |     226 |          0.084 |      0.554 |      0.184 |     0.465 |                  0.355 |
|  59 | Rocco Becht              | Penn State            | Big Ten           |   6 |         173 |       28 |     201 |          0.221 |     -0.057 |      0.183 |     0.438 |                  0.172 |
|  60 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |   6 |         219 |       17 |     236 |          0.156 |      0.462 |      0.178 |     0.504 |                  0.225 |
|  61 | Toa Faavae               | New Mexico            | Mountain West     |   5 |          74 |       29 |     103 |          0.037 |      0.538 |      0.178 |     0.456 |                  0.034 |
|  62 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |   6 |         142 |       72 |     214 |          0.063 |      0.387 |      0.172 |     0.439 |                  0.255 |
|  63 | Blake Baker              | Louisiana Tech        | Sun Belt          |   4 |          86 |       15 |     101 |          0.168 |      0.186 |      0.171 |     0.465 |                  0.209 |
|  64 | Landy Lyddy              | Southern Miss         | Sun Belt          |   5 |         108 |       13 |     121 |          0.152 |      0.321 |      0.171 |     0.446 |                  0.002 |
|  65 | Malachi Singleton        | App State             | Sun Belt          |   5 |         160 |       27 |     187 |          0.229 |     -0.231 |      0.162 |     0.476 |                  0.052 |
|  66 | Dylan Lonergan           | Rutgers               | Big Ten           |   4 |          96 |       11 |     107 |          0.223 |     -0.435 |      0.155 |     0.449 |                  0.135 |
|  67 | Bryce Underwood          | Michigan              | Big Ten           |   5 |         123 |       47 |     170 |          0.149 |      0.164 |      0.154 |     0.471 |                  0.192 |
|  68 | Ksaan Farrar             | Colorado State        | Pac-12            |   4 |         108 |        6 |     114 |          0.102 |      0.901 |      0.144 |     0.447 |                 -0.037 |
|  69 | Nate Bennett             | Baylor                | Big 12            |   3 |          66 |        2 |      68 |          0.061 |      2.810 |      0.142 |     0.471 |                  0.986 |
|  70 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |   4 |         130 |       19 |     149 |          0.159 |     -0.033 |      0.134 |     0.450 |                  0.097 |
|  71 | Camden Coleman           | James Madison         | Sun Belt          |   6 |         163 |       23 |     186 |          0.140 |      0.088 |      0.134 |     0.457 |                  0.260 |
|  72 | Austin Carlisle          | UL Monroe             | Sun Belt          |   3 |          60 |       30 |      90 |         -0.173 |      0.739 |      0.131 |     0.556 |                 -0.093 |
|  73 | Nathan Hayes             | North Dakota State    | Mountain West     |   6 |         146 |       25 |     171 |          0.050 |      0.584 |      0.128 |     0.503 |                  0.318 |
|  74 | Rickie Collins           | Kennesaw State        | Conference USA    |   5 |         156 |       49 |     205 |          0.104 |      0.191 |      0.125 |     0.473 |                  0.108 |
|  75 | Alberto Mendoza          | Georgia Tech          | ACC               |   5 |         163 |       11 |     174 |          0.109 |      0.357 |      0.125 |     0.506 |                  0.029 |
|  76 | Jaden Craig              | TCU                   | Big 12            |   5 |         169 |       18 |     187 |          0.153 |     -0.142 |      0.124 |     0.449 |                  0.022 |
|  77 | D.J. Lagway              | Baylor                | Big 12            |   3 |         138 |        3 |     141 |          0.111 |      0.537 |      0.120 |     0.418 |                  0.116 |
|  78 | Hank Brown               | Iowa                  | Big Ten           |   5 |         127 |       13 |     140 |          0.132 |     -0.096 |      0.111 |     0.479 |                  0.066 |
|  79 | Max Johnson              | Georgia Southern      | Sun Belt          |   6 |         230 |       18 |     248 |          0.100 |      0.150 |      0.104 |     0.444 |                  0.129 |
|  80 | Beau Pribula             | Virginia              | ACC               |   6 |         157 |       40 |     197 |          0.069 |      0.225 |      0.101 |     0.462 |                  0.176 |
|  81 | Luke Weaver              | San José State        | Mountain West     |   6 |         221 |       38 |     259 |          0.137 |     -0.109 |      0.101 |     0.475 |                  0.054 |
|  82 | Will Hammond             | Texas Tech            | Big 12            |   5 |         150 |       13 |     163 |          0.081 |      0.278 |      0.096 |     0.472 |                  0.160 |
|  83 | Deshawn Purdie           | Liberty               | Conference USA    |   6 |         127 |       24 |     151 |          0.095 |      0.090 |      0.094 |     0.464 |                  0.089 |
|  84 | Davis Warren             | Stanford              | ACC               |   6 |         205 |       10 |     215 |          0.090 |      0.069 |      0.089 |     0.409 |                  0.177 |
|  85 | Arch Manning             | Texas                 | SEC               |   5 |         160 |       26 |     186 |          0.106 |     -0.032 |      0.087 |     0.441 |                 -0.005 |
|  86 | Keyone Jenkins           | UCF                   | Big 12            |   6 |         124 |       23 |     147 |          0.107 |     -0.025 |      0.086 |     0.449 |                  0.062 |
|  87 | Billy Edwards            | North Carolina        | ACC               |   5 |         143 |       11 |     154 |          0.064 |      0.343 |      0.084 |     0.494 |                  0.030 |
|  88 | Ryder Burton             | UAB                   | American Athletic |   6 |         146 |       35 |     181 |          0.020 |      0.344 |      0.082 |     0.442 |                 -0.010 |
|  89 | Demond Williams Jr.      | Washington            | Big Ten           |   6 |         190 |       44 |     234 |          0.013 |      0.383 |      0.082 |     0.462 |                  0.014 |
|  90 | Cibastian Broughton      | Akron                 | Mid-American      |   4 |          71 |       24 |      95 |         -0.057 |      0.491 |      0.082 |     0.474 |                  0.014 |
|  91 | Jaylen Raynor            | Iowa State            | Big 12            |   6 |         157 |       42 |     199 |          0.073 |      0.107 |      0.081 |     0.417 |                  0.022 |
|  92 | Brock Glenn              | Western Kentucky      | Conference USA    |   6 |          97 |       48 |     145 |         -0.059 |      0.358 |      0.079 |     0.462 |                  0.016 |
|  93 | Jacurri Brown            | Rice                  | American Athletic |   6 |          85 |       93 |     178 |         -0.143 |      0.278 |      0.077 |     0.433 |                 -0.025 |
|  94 | Cutter Boley             | Arizona State         | Big 12            |   5 |         165 |       26 |     191 |          0.057 |      0.194 |      0.076 |     0.461 |                  0.050 |
|  95 | Owen McCown              | UTSA                  | American Athletic |   6 |         188 |       24 |     212 |          0.064 |      0.152 |      0.074 |     0.453 |                  0.126 |
|  96 | Will Crowder             | Troy                  | Sun Belt          |   5 |         164 |       33 |     197 |          0.002 |      0.413 |      0.071 |     0.452 |                  0.099 |
|  97 | Nick Minicucci           | Delaware              | Conference USA    |   4 |         108 |       12 |     120 |         -0.005 |      0.748 |      0.070 |     0.450 |                  0.012 |
|  98 | Kenny Minchey            | Kentucky              | SEC               |   6 |         185 |       19 |     204 |          0.069 |      0.073 |      0.070 |     0.471 |                  0.047 |
|  99 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |   4 |          74 |       30 |     104 |         -0.029 |      0.310 |      0.069 |     0.471 |                 -0.014 |
| 100 | Adam Damante             | New Mexico State      | Conference USA    |   4 |          75 |        7 |      82 |          0.007 |      0.729 |      0.069 |     0.476 |                 -0.470 |
| 101 | Trey Hedden              | New Mexico State      | Conference USA    |   5 |         132 |        7 |     139 |          0.045 |      0.421 |      0.064 |     0.396 |                 -0.052 |
| 102 | Drake Lindsey            | Minnesota             | Big Ten           |   6 |         198 |        8 |     206 |          0.062 |      0.003 |      0.060 |     0.461 |                  0.020 |
| 103 | Dexter Williams II       | Tulsa                 | American Athletic |   4 |          62 |        7 |      69 |         -0.008 |      0.639 |      0.058 |     0.435 |                  0.075 |
| 104 | Jackson Arnold           | UNLV                  | Mountain West     |   6 |         167 |       75 |     242 |          0.015 |      0.144 |      0.055 |     0.426 |                  0.074 |
| 105 | Taron Dickens            | Northern Illinois     | Mountain West     |   5 |         155 |       17 |     172 |          0.051 |      0.031 |      0.049 |     0.483 |                  0.121 |
| 106 | Steven Angeli            | Syracuse              | ACC               |   3 |         111 |        5 |     116 |          0.065 |     -0.327 |      0.048 |     0.405 |                  0.081 |
| 107 | Roman Gagliano           | Middle Tennessee      | Conference USA    |   5 |         162 |       13 |     175 |          0.034 |      0.208 |      0.047 |     0.411 |                  0.096 |
| 108 | Broc Lowry               | Western Michigan      | Mid-American      |   6 |         147 |       56 |     203 |          0.004 |      0.147 |      0.043 |     0.478 |                  0.155 |
| 109 | Dru Deshields            | Kent State            | Mid-American      |   6 |         165 |       38 |     203 |         -0.041 |      0.408 |      0.043 |     0.389 |                  0.073 |
| 110 | Byrum Brown              | Auburn                | SEC               |   5 |         176 |       61 |     237 |         -0.083 |      0.391 |      0.039 |     0.439 |                 -0.078 |
| 111 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |   6 |         191 |       45 |     236 |         -0.030 |      0.317 |      0.036 |     0.419 |                  0.073 |
| 112 | Baylor Hayes             | Tulsa                 | American Athletic |   4 |         135 |       19 |     154 |         -0.006 |      0.326 |      0.035 |     0.357 |                  0.009 |
| 113 | Micah Alejado            | Hawai'i               | Mountain West     |   6 |         284 |       20 |     304 |          0.030 |      0.104 |      0.035 |     0.444 |                  0.003 |
| 114 | Jay Kastantin            | Bowling Green         | Mid-American      |   6 |         150 |       24 |     174 |          0.045 |     -0.031 |      0.034 |     0.466 |                  0.024 |
| 115 | Angel H Flores           | Central Michigan      | Mid-American      |   6 |          75 |       88 |     163 |         -0.283 |      0.302 |      0.033 |     0.380 |                  0.147 |
| 116 | Julian Lewis             | Colorado              | Big 12            |   4 |         102 |        6 |     108 |          0.024 |      0.123 |      0.029 |     0.389 |                  0.069 |
| 117 | Landyn Locke             | Sam Houston           | Conference USA    |   5 |         187 |       19 |     206 |          0.008 |      0.238 |      0.029 |     0.432 |                 -0.044 |
| 118 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |   6 |         147 |       51 |     198 |          0.026 |      0.025 |      0.026 |     0.444 |                  0.094 |
| 119 | M.Van Buren Jr.          | South Florida         | American Athletic |   6 |         158 |       30 |     188 |          0.030 |     -0.007 |      0.024 |     0.473 |                 -0.027 |
| 120 | Alessio Milivojevic      | Michigan State        | Big Ten           |   6 |         169 |       17 |     186 |          0.004 |      0.185 |      0.020 |     0.478 |                 -0.134 |
| 121 | J.J. Kohl                | Florida International | Conference USA    |   5 |         168 |       18 |     186 |         -0.017 |      0.172 |      0.001 |     0.430 |                  0.043 |
| 122 | Nico Iamaleava           | UCLA                  | Big Ten           |   5 |         124 |       31 |     155 |          0.000 |      0.003 |      0.001 |     0.432 |                 -0.006 |
| 123 | Keldric Luster           | Ball State            | Mid-American      |   5 |         170 |       30 |     200 |         -0.064 |      0.366 |      0.001 |     0.395 |                  0.083 |
| 124 | Skyler Locklear          | Missouri State        | Conference USA    |   5 |         117 |       24 |     141 |         -0.034 |      0.169 |      0.001 |     0.376 |                 -0.011 |
| 125 | John Mateer              | Oklahoma              | SEC               |   5 |         146 |       42 |     188 |          0.058 |     -0.204 |     -0.001 |     0.431 |                 -0.062 |
| 126 | Emory Williams           | East Carolina         | American Athletic |   4 |          81 |        8 |      89 |         -0.045 |      0.439 |     -0.001 |     0.438 |                  0.105 |
| 127 | Noah Kim                 | Eastern Michigan      | Mid-American      |   7 |         254 |       20 |     274 |         -0.010 |      0.033 |     -0.007 |     0.420 |                  0.038 |
| 128 | Malik Washington         | Maryland              | Big Ten           |   6 |         228 |       25 |     253 |         -0.014 |      0.052 |     -0.007 |     0.415 |                 -0.058 |
| 129 | Brayden Roggow           | Akron                 | Mid-American      |   6 |         130 |       11 |     141 |         -0.051 |      0.402 |     -0.016 |     0.418 |                 -0.066 |
| 130 | Jaron-Keawe Sagapolutele | California            | ACC               |   5 |         170 |        6 |     176 |         -0.016 |     -0.252 |     -0.024 |     0.403 |                 -0.077 |
| 131 | Mason McKenzie           | Boston College        | ACC               |   5 |         153 |       79 |     232 |         -0.201 |      0.318 |     -0.024 |     0.431 |                  0.057 |
| 132 | Faizon Brandon           | Tennessee             | SEC               |   5 |         116 |       36 |     152 |         -0.184 |      0.488 |     -0.025 |     0.408 |                 -0.136 |
| 133 | Isaac Wilson             | Colorado              | Big 12            |   3 |          73 |       19 |      92 |          0.097 |     -0.498 |     -0.025 |     0.446 |                  0.037 |
| 134 | KJ Jackson               | Arkansas              | SEC               |   6 |         197 |       36 |     233 |         -0.049 |     -0.049 |     -0.049 |     0.446 |                 -0.065 |
| 135 | Jackson Sharman          | Sacramento State      | Mid-American      |   5 |         179 |       15 |     194 |         -0.067 |     -0.039 |     -0.065 |     0.418 |                 -0.063 |
| 136 | Tyler Hughes             | Wyoming               | Mountain West     |   6 |         150 |       59 |     209 |         -0.252 |      0.403 |     -0.068 |     0.435 |                 -0.062 |
| 137 | Quinn Henicle            | Old Dominion          | Sun Belt          |   5 |         103 |       62 |     165 |         -0.279 |      0.262 |     -0.076 |     0.376 |                 -0.133 |
| 138 | Marcel Reed              | Texas A&M             | SEC               |   6 |         198 |       39 |     237 |         -0.141 |      0.229 |     -0.080 |     0.388 |                 -0.179 |
| 139 | Caleb Heavner            | Miami (OH)            | Mid-American      |   5 |          61 |       25 |      86 |         -0.204 |      0.171 |     -0.095 |     0.384 |                 -0.070 |
| 140 | Jason Wright             | Buffalo               | Mid-American      |   5 |         143 |       34 |     177 |         -0.165 |      0.109 |     -0.112 |     0.367 |                 -0.134 |
| 141 | H.Geriner                | Pittsburgh            | ACC               |   4 |          72 |        9 |      81 |         -0.087 |     -0.378 |     -0.119 |     0.370 |                 -0.171 |
| 142 | Mitch Griffis            | East Carolina         | American Athletic |   5 |          76 |       19 |      95 |         -0.187 |      0.137 |     -0.123 |     0.400 |                 -0.150 |
| 143 | Caden Pinnick            | Washington State      | Pac-12            |   6 |         195 |       53 |     248 |         -0.202 |      0.114 |     -0.134 |     0.403 |                 -0.107 |
| 144 | Carter Jones             | Nevada                | Mountain West     |   4 |          95 |       21 |     116 |         -0.176 |      0.045 |     -0.136 |     0.371 |                 -0.205 |
| 145 | Ethan Hampton            | Southern Miss         | Sun Belt          |   3 |          76 |        6 |      82 |         -0.119 |     -0.437 |     -0.142 |     0.439 |                 -0.232 |
| 146 | Kadin Semonza            | Tulane                | American Athletic |   5 |         132 |       17 |     149 |         -0.126 |     -0.330 |     -0.149 |     0.309 |                 -0.129 |
| 147 | Tait Reynolds            | Clemson               | ACC               |   5 |         145 |       36 |     181 |         -0.137 |     -0.201 |     -0.150 |     0.409 |                 -0.102 |
| 148 | Cole Gonzales            | Charlotte             | American Athletic |   5 |         129 |       11 |     140 |         -0.110 |     -0.756 |     -0.161 |     0.429 |                 -0.294 |
| 149 | Elijah Holmes            | Buffalo               | Mid-American      |   2 |          64 |        7 |      71 |         -0.181 |     -0.044 |     -0.167 |     0.366 |                 -0.174 |
| 150 | Jayden Denegal           | San Diego State       | Pac-12            |   6 |         146 |       15 |     161 |         -0.159 |     -0.277 |     -0.170 |     0.335 |                 -0.227 |
| 151 | Grady Brosterhous        | Utah State            | Pac-12            |   6 |         162 |       70 |     232 |         -0.157 |     -0.212 |     -0.173 |     0.328 |                 -0.229 |
| 152 | EJ Colson                | UTEP                  | Mountain West     |   5 |          91 |       50 |     141 |         -0.250 |     -0.097 |     -0.196 |     0.433 |                 -0.226 |
| 153 | Ryan Huff                | Old Dominion          | Sun Belt          |   3 |          61 |        3 |      64 |         -0.269 |      0.594 |     -0.228 |     0.297 |                 -0.253 |
