# 2026 CFB QB EPA — through Week 5

FBS offenses, games through Oct 3, 2026 (Week 0 games are folded into Week 1).
**Minimum 60 dropbacks**, which leaves 146 QBs. Sorted by EPA/play over all dropbacks + QB rushes.

- **Dropbacks** = pass attempts + sacks. **Rushes** = designed runs + scrambles.
- **Success** = share of plays with positive EPA.
- **EPA/play (WP 10–90%)** leaves out garbage time.
- Not opponent-adjusted, so a team that has played FCS opponents looks better.
- Source: cfbfastR play-by-play (`sportsdataverse/cfbfastR-data`, `data/rds/pbp_players_pos_2026.rds`). Rebuild with `python qb_epa.py <rds> [min_dropbacks]` then `python make_readme.py <week> "<through date>"`.

Full tables: [`qb_epa_2026.csv`](qb_epa_2026.csv), [`qb_epa_2026_nongarbage.csv`](qb_epa_2026_nongarbage.csv)

## Non-garbage time (win probability 10–90%)

Same 60-dropback pool, plus at least 40 plays in competitive game states (136 QBs).

|   # |   Overall # | QB                       | Team                  | Conf              |   Plays (WP 10–90%) |   EPA/play (WP 10–90%) |   Success (WP 10–90%) |   EPA/play (all) |
|----:|------------:|:-------------------------|:----------------------|:------------------|--------------------:|-----------------------:|----------------------:|-----------------:|
|   1 |           4 | Keelon Russell           | Alabama               | SEC               |                  99 |                  0.666 |                 0.586 |            0.472 |
|   2 |           2 | Darian Mensah            | Miami                 | ACC               |                  69 |                  0.664 |                 0.667 |            0.505 |
|   3 |           3 | Julian Sayin             | Ohio State            | Big Ten           |                  93 |                  0.634 |                 0.624 |            0.479 |
|   4 |          16 | Jared Hollins            | South Alabama         | Sun Belt          |                  56 |                  0.553 |                 0.518 |            0.362 |
|   5 |          12 | Marcus Stokes            | Memphis               | American Athletic |                 106 |                  0.544 |                 0.557 |            0.389 |
|   6 |          17 | Gunner Stockton          | Georgia               | SEC               |                  52 |                  0.520 |                 0.558 |            0.360 |
|   7 |          55 | Nathan Hayes             | North Dakota State    | Mountain West     |                  75 |                  0.505 |                 0.533 |            0.189 |
|   8 |           1 | David McComb             | Miami (OH)            | Mid-American      |                  81 |                  0.492 |                 0.519 |            0.570 |
|   9 |          19 | Devon Dampier            | Utah                  | Big 12            |                  55 |                  0.488 |                 0.582 |            0.346 |
|  10 |          14 | Giovanni Lopez           | Wake Forest           | ACC               |                 102 |                  0.481 |                 0.569 |            0.374 |
|  11 |           7 | C.J. Carr                | Notre Dame            | FBS Independents  |                  81 |                  0.470 |                 0.543 |            0.418 |
|  12 |           5 | Austin Simmons           | Missouri              | SEC               |                 118 |                  0.465 |                 0.534 |            0.457 |
|  13 |           6 | Tayven Jackson           | North Texas           | American Athletic |                 125 |                  0.460 |                 0.520 |            0.432 |
|  14 |          27 | Michael Hawkins Jr.      | West Virginia         | Big 12            |                 115 |                  0.454 |                 0.470 |            0.308 |
|  15 |          13 | Avery Johnson            | Kansas State          | Big 12            |                 109 |                  0.433 |                 0.532 |            0.383 |
|  16 |          28 | Bishop Davenport         | South Alabama         | Sun Belt          |                  59 |                  0.413 |                 0.525 |            0.307 |
|  17 |           8 | Josh Hoover              | Indiana               | Big Ten           |                  77 |                  0.408 |                 0.571 |            0.417 |
|  18 |           9 | Jayden Maiava            | USC                   | Big Ten           |                 148 |                  0.406 |                 0.541 |            0.402 |
|  19 |          11 | Aaron Philo              | Florida               | SEC               |                 102 |                  0.394 |                 0.578 |            0.389 |
|  20 |          61 | Camden Coleman           | James Madison         | Sun Belt          |                  77 |                  0.390 |                 0.519 |            0.173 |
|  21 |          21 | Cameran Brown            | Georgia State         | Sun Belt          |                  96 |                  0.374 |                 0.562 |            0.324 |
|  22 |          35 | Trinidad Chambliss       | Ole Miss              | SEC               |                 129 |                  0.368 |                 0.550 |            0.286 |
|  23 |          20 | Kamario Taylor           | Mississippi State     | SEC               |                 120 |                  0.355 |                 0.542 |            0.337 |
|  24 |          33 | William Watson III       | Massachusetts         | Mid-American      |                  77 |                  0.345 |                 0.468 |            0.290 |
|  25 |          68 | Kalieb Osborne           | UConn                 | FBS Independents  |                 103 |                  0.342 |                 0.466 |            0.150 |
|  26 |          18 | Kevin Jennings           | SMU                   | ACC               |                 153 |                  0.340 |                 0.575 |            0.349 |
|  27 |          52 | Matt Vezza               | Ohio                  | Mid-American      |                  82 |                  0.337 |                 0.549 |            0.208 |
|  28 |          24 | John Alan Richter        | Toledo                | Mid-American      |                 110 |                  0.336 |                 0.500 |            0.315 |
|  29 |          22 | Ashton Daniels           | Florida State         | ACC               |                 120 |                  0.331 |                 0.467 |            0.322 |
|  30 |          32 | CJ Bailey                | NC State              | ACC               |                 100 |                  0.329 |                 0.500 |            0.290 |
|  31 |          25 | Ajani Sheppard           | Temple                | American Athletic |                 101 |                  0.313 |                 0.446 |            0.313 |
|  32 |          10 | Anthony Colandrea        | Nebraska              | Big Ten           |                 124 |                  0.286 |                 0.508 |            0.395 |
|  33 |          30 | Mason Heintschel         | Pittsburgh            | ACC               |                 101 |                  0.285 |                 0.446 |            0.299 |
|  34 |          54 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |                 120 |                  0.280 |                 0.533 |            0.196 |
|  35 |          15 | Hauss Hejny              | Colorado State        | Pac-12            |                  56 |                  0.277 |                 0.500 |            0.366 |
|  36 |          82 | Davis Warren             | Stanford              | ACC               |                 119 |                  0.270 |                 0.429 |            0.103 |
|  37 |          43 | Maddux Madsen            | Boise State           | Pac-12            |                 120 |                  0.267 |                 0.542 |            0.249 |
|  38 |          37 | Caden Creel              | Jacksonville State    | Conference USA    |                 134 |                  0.263 |                 0.530 |            0.277 |
|  39 |          57 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |                 107 |                  0.261 |                 0.477 |            0.184 |
|  40 |          67 | Jayden Mandal            | Fresno State          | Pac-12            |                 122 |                  0.254 |                 0.500 |            0.151 |
|  41 |          31 | Malachi Singleton        | App State             | Sun Belt          |                  86 |                  0.253 |                 0.488 |            0.297 |
|  42 |          23 | Lincoln Kienholz         | Louisville            | ACC               |                 158 |                  0.234 |                 0.494 |            0.319 |
|  43 |          41 | Katin Houser             | Illinois              | Big Ten           |                 112 |                  0.227 |                 0.527 |            0.255 |
|  44 |          38 | Bear Bachmeier           | BYU                   | Big 12            |                  82 |                  0.226 |                 0.476 |            0.277 |
|  45 |          34 | Brad Jackson             | Texas State           | Pac-12            |                 137 |                  0.223 |                 0.526 |            0.287 |
|  46 |          36 | Noah Fifita              | Arizona               | Big 12            |                 136 |                  0.221 |                 0.537 |            0.283 |
|  47 |          26 | Conner Weigman           | Houston               | Big 12            |                 135 |                  0.214 |                 0.519 |            0.312 |
|  48 |          49 | Ryan Browne              | Purdue                | Big Ten           |                 133 |                  0.207 |                 0.504 |            0.225 |
|  49 |          60 | Walker Eget              | Duke                  | ACC               |                  76 |                  0.204 |                 0.487 |            0.176 |
|  50 |          83 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |                 136 |                  0.199 |                 0.478 |            0.101 |
|  51 |          66 | Bryce Underwood          | Michigan              | Big Ten           |                 153 |                  0.192 |                 0.510 |            0.154 |
|  52 |          29 | Aidan Chiles             | Northwestern          | Big Ten           |                  88 |                  0.190 |                 0.466 |            0.306 |
|  53 |          86 | Trey Owens               | Arkansas State        | Sun Belt          |                 132 |                  0.189 |                 0.530 |            0.092 |
|  54 |          88 | Beau Pribula             | Virginia              | ACC               |                  93 |                  0.177 |                 0.462 |            0.088 |
|  55 |          53 | Dante Moore              | Oregon                | Big Ten           |                  90 |                  0.173 |                 0.400 |            0.206 |
|  56 |          39 | Caden Veltkamp           | Florida Atlantic      | American Athletic |                 111 |                  0.166 |                 0.450 |            0.274 |
|  57 |          50 | JC French                | Cincinnati            | Big 12            |                 119 |                  0.164 |                 0.513 |            0.213 |
|  58 |          46 | Isaiah Marshall          | Kansas                | Big 12            |                  99 |                  0.163 |                 0.404 |            0.236 |
|  59 |          40 | Braden Atkinson          | Oregon State          | Pac-12            |                 103 |                  0.158 |                 0.417 |            0.255 |
|  60 |          63 | Lanorris Sellers         | South Carolina        | SEC               |                 110 |                  0.158 |                 0.482 |            0.161 |
|  61 |          87 | Will Hammond             | Texas Tech            | Big 12            |                 116 |                  0.156 |                 0.509 |            0.092 |
|  62 |          81 | Jackson Arnold           | UNLV                  | Mountain West     |                 161 |                  0.140 |                 0.422 |            0.105 |
|  63 |          65 | Dylan Lonergan           | Rutgers               | Big Ten           |                  54 |                  0.135 |                 0.444 |            0.155 |
|  64 |          42 | Jared Curtis             | Vanderbilt            | SEC               |                  95 |                  0.130 |                 0.453 |            0.254 |
|  65 |          47 | Colton Joseph            | Wisconsin             | Big Ten           |                  98 |                  0.128 |                 0.429 |            0.231 |
|  66 |          76 | D.J. Lagway              | Baylor                | Big 12            |                 109 |                  0.116 |                 0.440 |            0.120 |
|  67 |         103 | Owen McCown              | UTSA                  | American Athletic |                 136 |                  0.114 |                 0.434 |            0.051 |
|  68 |          58 | Drew Mestemaker          | Oklahoma State        | Big 12            |                 119 |                  0.112 |                 0.496 |            0.179 |
|  69 |         109 | Taron Dickens            | Northern Illinois     | Mountain West     |                  78 |                  0.109 |                 0.513 |            0.035 |
|  70 |          93 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |                 134 |                  0.107 |                 0.478 |            0.081 |
|  71 |          48 | Jacurri Brown            | Rice                  | American Athletic |                 103 |                  0.104 |                 0.466 |            0.226 |
|  72 |          51 | Sam Leavitt              | LSU                   | SEC               |                 106 |                  0.102 |                 0.509 |            0.210 |
|  73 |          95 | Deshawn Purdie           | Liberty               | Conference USA    |                 104 |                  0.097 |                 0.481 |            0.075 |
|  74 |         107 | Roman Gagliano           | Middle Tennessee      | Conference USA    |                 133 |                  0.096 |                 0.444 |            0.047 |
|  75 |         101 | Max Johnson              | Georgia Southern      | Sun Belt          |                 137 |                  0.093 |                 0.445 |            0.058 |
|  76 |          56 | Ryder Burton             | UAB                   | American Athletic |                 103 |                  0.087 |                 0.437 |            0.187 |
|  77 |          64 | Jaylen Raynor            | Iowa State            | Big 12            |                  99 |                  0.087 |                 0.434 |            0.156 |
|  78 |         106 | Steven Angeli            | Syracuse              | ACC               |                  84 |                  0.081 |                 0.381 |            0.048 |
|  79 |          59 | Rocco Becht              | Penn State            | Big Ten           |                  85 |                  0.081 |                 0.365 |            0.179 |
|  80 |         102 | Dru Deshields            | Kent State            | Mid-American      |                 109 |                  0.079 |                 0.404 |            0.053 |
|  81 |         105 | J.J. Kohl                | Florida International | Conference USA    |                 117 |                  0.074 |                 0.453 |            0.048 |
|  82 |         111 | Julian Lewis             | Colorado              | Big 12            |                  70 |                  0.069 |                 0.400 |            0.029 |
|  83 |          91 | Cutter Boley             | Arizona State         | Big 12            |                  90 |                  0.068 |                 0.444 |            0.083 |
|  84 |          94 | Micah Alejado            | Hawai'i               | Mountain West     |                 207 |                  0.067 |                 0.440 |            0.079 |
|  85 |          79 | Hank Brown               | Iowa                  | Big Ten           |                 110 |                  0.066 |                 0.455 |            0.111 |
|  86 |          77 | Luke Weaver              | San José State        | Mountain West     |                 165 |                  0.062 |                 0.473 |            0.117 |
|  87 |          89 | Kenny Minchey            | Kentucky              | SEC               |                 119 |                  0.059 |                 0.479 |            0.084 |
|  88 |          73 | Demond Williams Jr.      | Washington            | Big Ten           |                 165 |                  0.056 |                 0.467 |            0.127 |
|  89 |         104 | Nico Iamaleava           | UCLA                  | Big Ten           |                 109 |                  0.053 |                 0.431 |            0.051 |
|  90 |         124 | Broc Lowry               | Western Michigan      | Mid-American      |                 128 |                  0.052 |                 0.469 |           -0.030 |
|  91 |         131 | Keldric Luster           | Ball State            | Mid-American      |                  62 |                  0.048 |                 0.452 |           -0.061 |
|  92 |          90 | John Mateer              | Oklahoma              | SEC               |                  87 |                  0.047 |                 0.437 |            0.083 |
|  93 |          99 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |                  48 |                  0.042 |                 0.458 |            0.061 |
|  94 |          70 | Arch Manning             | Texas                 | SEC               |                  81 |                  0.040 |                 0.444 |            0.135 |
|  95 |         123 | Isaac Wilson             | Colorado              | Big 12            |                  65 |                  0.037 |                 0.462 |           -0.025 |
|  96 |          84 | Rickie Collins           | Kennesaw State        | Conference USA    |                  66 |                  0.027 |                 0.455 |            0.096 |
|  97 |         110 | Drake Lindsey            | Minnesota             | Big Ten           |                  78 |                  0.024 |                 0.487 |            0.032 |
|  98 |          75 | Jaden Craig              | TCU                   | Big 12            |                 143 |                  0.022 |                 0.434 |            0.124 |
|  99 |         112 | Skyler Locklear          | Missouri State        | Conference USA    |                  81 |                  0.017 |                 0.395 |            0.028 |
| 100 |         125 | Noah Kim                 | Eastern Michigan      | Mid-American      |                 140 |                  0.014 |                 0.414 |           -0.033 |
| 101 |         128 | Mason McKenzie           | Boston College        | ACC               |                 157 |                  0.014 |                 0.433 |           -0.053 |
| 102 |          92 | Cibastian Broughton      | Akron                 | Mid-American      |                  53 |                  0.014 |                 0.472 |            0.082 |
| 103 |          96 | Nick Minicucci           | Delaware              | Conference USA    |                  79 |                  0.012 |                 0.430 |            0.070 |
| 104 |          85 | Landyn Locke             | Sam Houston           | Conference USA    |                 115 |                  0.006 |                 0.452 |            0.094 |
| 105 |         120 | Jay Kastantin            | Bowling Green         | Mid-American      |                 107 |                  0.003 |                 0.411 |           -0.017 |
| 106 |         119 | KJ Jackson               | Arkansas              | SEC               |                  84 |                 -0.010 |                 0.417 |           -0.014 |
| 107 |         129 | Will Crowder             | Troy                  | Sun Belt          |                 110 |                 -0.010 |                 0.418 |           -0.057 |
| 108 |          97 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |                  63 |                 -0.015 |                 0.413 |            0.069 |
| 109 |          98 | Billy Edwards            | North Carolina        | ACC               |                  90 |                 -0.015 |                 0.456 |            0.065 |
| 110 |          80 | Alberto Mendoza          | Georgia Tech          | ACC               |                  95 |                 -0.028 |                 0.463 |            0.108 |
| 111 |          62 | Toa Faavae               | New Mexico            | Mountain West     |                  59 |                 -0.034 |                 0.339 |            0.172 |
| 112 |         113 | Malik Washington         | Maryland              | Big Ten           |                 100 |                 -0.040 |                 0.390 |            0.026 |
| 113 |         130 | Tyler Hughes             | Wyoming               | Mountain West     |                 109 |                 -0.048 |                 0.440 |           -0.060 |
| 114 |         118 | Baylor Hayes             | Tulsa                 | American Athletic |                 109 |                 -0.050 |                 0.349 |           -0.003 |
| 115 |         115 | M.Van Buren Jr.          | South Florida         | American Athletic |                 116 |                 -0.052 |                 0.440 |            0.012 |
| 116 |          72 | Trey Hedden              | New Mexico State      | Conference USA    |                  89 |                 -0.052 |                 0.382 |            0.127 |
| 117 |         117 | Marcel Reed              | Texas A&M             | SEC               |                 113 |                 -0.056 |                 0.389 |            0.004 |
| 118 |         127 | Keyone Jenkins           | UCF                   | Big 12            |                  74 |                 -0.058 |                 0.432 |           -0.049 |
| 119 |         116 | Quinn Henicle            | Old Dominion          | Sun Belt          |                  75 |                 -0.062 |                 0.347 |            0.007 |
| 120 |         121 | Jaron-Keawe Sagapolutele | California            | ACC               |                 141 |                 -0.077 |                 0.411 |           -0.024 |
| 121 |         108 | Byrum Brown              | Auburn                | SEC               |                 152 |                 -0.078 |                 0.401 |            0.039 |
| 122 |          71 | Austin Carlisle          | UL Monroe             | Sun Belt          |                  54 |                 -0.093 |                 0.537 |            0.131 |
| 123 |         137 | Caden Pinnick            | Washington State      | Pac-12            |                 133 |                 -0.099 |                 0.421 |           -0.135 |
| 124 |         139 | Tait Reynolds            | Clemson               | ACC               |                 146 |                 -0.102 |                 0.445 |           -0.150 |
| 125 |         126 | Alessio Milivojevic      | Michigan State        | Big Ten           |                 107 |                 -0.114 |                 0.430 |           -0.046 |
| 126 |         122 | Faizon Brandon           | Tennessee             | SEC               |                  93 |                 -0.136 |                 0.355 |           -0.025 |
| 127 |         135 | Jason Wright             | Buffalo               | Mid-American      |                  76 |                 -0.136 |                 0.421 |           -0.121 |
| 128 |         142 | Kadin Semonza            | Tulane                | American Athletic |                  88 |                 -0.147 |                 0.318 |           -0.167 |
| 129 |         134 | Mitch Griffis            | East Carolina         | American Athletic |                  50 |                 -0.150 |                 0.380 |           -0.098 |
| 130 |         133 | Carter Jones             | Nevada                | Mountain West     |                  72 |                 -0.164 |                 0.389 |           -0.088 |
| 131 |         143 | Elijah Holmes            | Buffalo               | Mid-American      |                  68 |                 -0.174 |                 0.368 |           -0.167 |
| 132 |         136 | Grady Brosterhous        | Utah State            | Pac-12            |                  82 |                 -0.182 |                 0.293 |           -0.126 |
| 133 |         138 | Ethan Hampton            | Southern Miss         | Sun Belt          |                  46 |                 -0.232 |                 0.435 |           -0.142 |
| 134 |         140 | Jayden Denegal           | San Diego State       | Pac-12            |                  82 |                 -0.236 |                 0.329 |           -0.156 |
| 135 |         145 | EJ Colson                | UTEP                  | Mountain West     |                  53 |                 -0.244 |                 0.396 |           -0.192 |
| 136 |         141 | Cole Gonzales            | Charlotte             | American Athletic |                  87 |                 -0.304 |                 0.414 |           -0.166 |

## All plays

|   # | QB                       | Team                  | Conf              |   G |   Dropbacks |   Rushes |   Plays |   EPA/dropback |   EPA/rush |   EPA/play |   Success |   EPA/play (WP 10–90%) |
|----:|:-------------------------|:----------------------|:------------------|----:|------------:|---------:|--------:|---------------:|-----------:|-----------:|----------:|-----------------------:|
|   1 | David McComb             | Miami (OH)            | Mid-American      |   4 |         109 |       11 |     120 |          0.565 |      0.615 |      0.570 |     0.525 |                  0.492 |
|   2 | Darian Mensah            | Miami                 | ACC               |   5 |         136 |        7 |     143 |          0.489 |      0.816 |      0.505 |     0.622 |                  0.664 |
|   3 | Julian Sayin             | Ohio State            | Big Ten           |   5 |         151 |       16 |     167 |          0.479 |      0.480 |      0.479 |     0.593 |                  0.634 |
|   4 | Keelon Russell           | Alabama               | SEC               |   5 |         143 |       26 |     169 |          0.443 |      0.633 |      0.472 |     0.574 |                  0.666 |
|   5 | Austin Simmons           | Missouri              | SEC               |   5 |         142 |        7 |     149 |          0.493 |     -0.268 |      0.457 |     0.537 |                  0.465 |
|   6 | Tayven Jackson           | North Texas           | American Athletic |   5 |         168 |       17 |     185 |          0.439 |      0.365 |      0.432 |     0.546 |                  0.460 |
|   7 | C.J. Carr                | Notre Dame            | FBS Independents  |   5 |         127 |       10 |     137 |          0.391 |      0.754 |      0.418 |     0.555 |                  0.470 |
|   8 | Josh Hoover              | Indiana               | Big Ten           |   5 |         113 |       11 |     124 |          0.409 |      0.502 |      0.417 |     0.556 |                  0.408 |
|   9 | Jayden Maiava            | USC                   | Big Ten           |   6 |         197 |       12 |     209 |          0.445 |     -0.296 |      0.402 |     0.569 |                  0.406 |
|  10 | Anthony Colandrea        | Nebraska              | Big Ten           |   5 |         148 |       31 |     179 |          0.308 |      0.807 |      0.395 |     0.547 |                  0.286 |
|  11 | Aaron Philo              | Florida               | SEC               |   5 |         126 |       26 |     152 |          0.420 |      0.240 |      0.389 |     0.553 |                  0.394 |
|  12 | Marcus Stokes            | Memphis               | American Athletic |   5 |         130 |       29 |     159 |          0.421 |      0.241 |      0.389 |     0.541 |                  0.544 |
|  13 | Avery Johnson            | Kansas State          | Big 12            |   4 |         133 |       29 |     162 |          0.318 |      0.683 |      0.383 |     0.531 |                  0.433 |
|  14 | Giovanni Lopez           | Wake Forest           | ACC               |   5 |         154 |       35 |     189 |          0.313 |      0.643 |      0.374 |     0.540 |                  0.481 |
|  15 | Hauss Hejny              | Colorado State        | Pac-12            |   3 |          74 |       12 |      86 |          0.344 |      0.499 |      0.366 |     0.500 |                  0.277 |
|  16 | Jared Hollins            | South Alabama         | Sun Belt          |   4 |          85 |       19 |     104 |          0.392 |      0.226 |      0.362 |     0.471 |                  0.553 |
|  17 | Gunner Stockton          | Georgia               | SEC               |   5 |         106 |       16 |     122 |          0.387 |      0.181 |      0.360 |     0.566 |                  0.520 |
|  18 | Kevin Jennings           | SMU                   | ACC               |   5 |         162 |       25 |     187 |          0.396 |      0.043 |      0.349 |     0.551 |                  0.340 |
|  19 | Devon Dampier            | Utah                  | Big 12            |   4 |         104 |       30 |     134 |          0.378 |      0.235 |      0.346 |     0.567 |                  0.488 |
|  20 | Kamario Taylor           | Mississippi State     | SEC               |   5 |         167 |       29 |     196 |          0.286 |      0.630 |      0.337 |     0.536 |                  0.355 |
|  21 | Cameran Brown            | Georgia State         | Sun Belt          |   5 |         133 |       24 |     157 |          0.360 |      0.119 |      0.324 |     0.529 |                  0.374 |
|  22 | Ashton Daniels           | Florida State         | ACC               |   5 |         127 |       45 |     172 |          0.216 |      0.622 |      0.322 |     0.483 |                  0.331 |
|  23 | Lincoln Kienholz         | Louisville            | ACC               |   5 |         149 |       42 |     191 |          0.321 |      0.313 |      0.319 |     0.518 |                  0.234 |
|  24 | John Alan Richter        | Toledo                | Mid-American      |   5 |         155 |        4 |     159 |          0.339 |     -0.617 |      0.315 |     0.491 |                  0.336 |
|  25 | Ajani Sheppard           | Temple                | American Athletic |   5 |          78 |       39 |     117 |          0.296 |      0.348 |      0.313 |     0.453 |                  0.313 |
|  26 | Conner Weigman           | Houston               | Big 12            |   5 |         140 |       37 |     177 |          0.302 |      0.352 |      0.312 |     0.559 |                  0.214 |
|  27 | Michael Hawkins Jr.      | West Virginia         | Big 12            |   5 |          91 |       83 |     174 |          0.143 |      0.489 |      0.308 |     0.454 |                  0.454 |
|  28 | Bishop Davenport         | South Alabama         | Sun Belt          |   2 |          61 |       16 |      77 |          0.302 |      0.328 |      0.307 |     0.481 |                  0.413 |
|  29 | Aidan Chiles             | Northwestern          | Big Ten           |   4 |          98 |       27 |     125 |          0.288 |      0.373 |      0.306 |     0.512 |                  0.190 |
|  30 | Mason Heintschel         | Pittsburgh            | ACC               |   5 |         153 |       25 |     178 |          0.348 |     -0.003 |      0.299 |     0.466 |                  0.285 |
|  31 | Malachi Singleton        | App State             | Sun Belt          |   4 |         136 |       25 |     161 |          0.390 |     -0.210 |      0.297 |     0.522 |                  0.253 |
|  32 | CJ Bailey                | NC State              | ACC               |   5 |         157 |       26 |     183 |          0.288 |      0.302 |      0.290 |     0.492 |                  0.329 |
|  33 | William Watson III       | Massachusetts         | Mid-American      |   5 |         104 |       25 |     129 |          0.212 |      0.611 |      0.290 |     0.473 |                  0.345 |
|  34 | Brad Jackson             | Texas State           | Pac-12            |   5 |         142 |       45 |     187 |          0.343 |      0.111 |      0.287 |     0.524 |                  0.223 |
|  35 | Trinidad Chambliss       | Ole Miss              | SEC               |   4 |         150 |       22 |     172 |          0.232 |      0.654 |      0.286 |     0.541 |                  0.368 |
|  36 | Noah Fifita              | Arizona               | Big 12            |   5 |         181 |       27 |     208 |          0.270 |      0.369 |      0.283 |     0.529 |                  0.221 |
|  37 | Caden Creel              | Jacksonville State    | Conference USA    |   5 |         131 |       63 |     194 |          0.310 |      0.207 |      0.277 |     0.546 |                  0.263 |
|  38 | Bear Bachmeier           | BYU                   | Big 12            |   4 |          89 |       23 |     112 |          0.151 |      0.763 |      0.277 |     0.527 |                  0.226 |
|  39 | Caden Veltkamp           | Florida Atlantic      | American Athletic |   5 |         184 |       10 |     194 |          0.275 |      0.252 |      0.274 |     0.505 |                  0.166 |
|  40 | Braden Atkinson          | Oregon State          | Pac-12            |   4 |         169 |        7 |     176 |          0.270 |     -0.089 |      0.255 |     0.443 |                  0.158 |
|  41 | Katin Houser             | Illinois              | Big Ten           |   5 |         164 |       19 |     183 |          0.204 |      0.694 |      0.255 |     0.525 |                  0.227 |
|  42 | Jared Curtis             | Vanderbilt            | SEC               |   4 |         104 |       32 |     136 |          0.163 |      0.551 |      0.254 |     0.485 |                  0.130 |
|  43 | Maddux Madsen            | Boise State           | Pac-12            |   5 |         138 |       19 |     157 |          0.163 |      0.867 |      0.249 |     0.541 |                  0.267 |
|  44 | Aidan Armenta            | UL Monroe             | Sun Belt          |   4 |         112 |       17 |     129 |          0.289 |     -0.079 |      0.241 |     0.473 |                 -0.178 |
|  45 | AJ Surace                | Rutgers               | Big Ten           |   4 |          61 |        7 |      68 |          0.424 |     -1.385 |      0.237 |     0.456 |                 -0.437 |
|  46 | Isaiah Marshall          | Kansas                | Big 12            |   4 |         109 |       44 |     153 |          0.159 |      0.428 |      0.236 |     0.444 |                  0.163 |
|  47 | Colton Joseph            | Wisconsin             | Big Ten           |   5 |         145 |       45 |     190 |          0.174 |      0.416 |      0.231 |     0.468 |                  0.128 |
|  48 | Jacurri Brown            | Rice                  | American Athletic |   5 |          73 |       76 |     149 |          0.009 |      0.434 |      0.226 |     0.483 |                  0.104 |
|  49 | Ryan Browne              | Purdue                | Big Ten           |   5 |         159 |       13 |     172 |          0.234 |      0.121 |      0.225 |     0.523 |                  0.207 |
|  50 | JC French                | Cincinnati            | Big 12            |   5 |         131 |       41 |     172 |          0.175 |      0.334 |      0.213 |     0.529 |                  0.164 |
|  51 | Sam Leavitt              | LSU                   | SEC               |   5 |         146 |       39 |     185 |          0.127 |      0.520 |      0.210 |     0.535 |                  0.102 |
|  52 | Matt Vezza               | Ohio                  | Mid-American      |   5 |          66 |       27 |      93 |         -0.007 |      0.736 |      0.208 |     0.538 |                  0.337 |
|  53 | Dante Moore              | Oregon                | Big Ten           |   4 |         106 |        5 |     111 |          0.227 |     -0.230 |      0.206 |     0.459 |                  0.173 |
|  54 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |   5 |         185 |       12 |     197 |          0.168 |      0.630 |      0.196 |     0.508 |                  0.280 |
|  55 | Nathan Hayes             | North Dakota State    | Mountain West     |   5 |         122 |       21 |     143 |          0.114 |      0.626 |      0.189 |     0.517 |                  0.505 |
|  56 | Ryder Burton             | UAB                   | American Athletic |   5 |         123 |       30 |     153 |          0.115 |      0.480 |      0.187 |     0.458 |                  0.087 |
|  57 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |   5 |         116 |       62 |     178 |          0.038 |      0.458 |      0.184 |     0.461 |                  0.261 |
|  58 | Drew Mestemaker          | Oklahoma State        | Big 12            |   4 |         146 |       10 |     156 |          0.134 |      0.830 |      0.179 |     0.526 |                  0.112 |
|  59 | Rocco Becht              | Penn State            | Big Ten           |   5 |         140 |       19 |     159 |          0.205 |     -0.017 |      0.179 |     0.447 |                  0.081 |
|  60 | Walker Eget              | Duke                  | ACC               |   4 |          93 |        3 |      96 |          0.195 |     -0.407 |      0.176 |     0.469 |                  0.204 |
|  61 | Camden Coleman           | James Madison         | Sun Belt          |   5 |         133 |       22 |     155 |          0.183 |      0.113 |      0.173 |     0.465 |                  0.390 |
|  62 | Toa Faavae               | New Mexico            | Mountain West     |   5 |          74 |       29 |     103 |          0.030 |      0.534 |      0.172 |     0.456 |                 -0.034 |
|  63 | Lanorris Sellers         | South Carolina        | SEC               |   5 |         158 |       41 |     199 |          0.011 |      0.739 |      0.161 |     0.477 |                  0.158 |
|  64 | Jaylen Raynor            | Iowa State            | Big 12            |   5 |         125 |       36 |     161 |          0.173 |      0.098 |      0.156 |     0.453 |                  0.087 |
|  65 | Dylan Lonergan           | Rutgers               | Big Ten           |   4 |          96 |       11 |     107 |          0.223 |     -0.435 |      0.155 |     0.449 |                  0.135 |
|  66 | Bryce Underwood          | Michigan              | Big Ten           |   5 |         123 |       47 |     170 |          0.149 |      0.164 |      0.154 |     0.471 |                  0.192 |
|  67 | Jayden Mandal            | Fresno State          | Pac-12            |   5 |         143 |       26 |     169 |          0.154 |      0.133 |      0.151 |     0.491 |                  0.254 |
|  68 | Kalieb Osborne           | UConn                 | FBS Independents  |   5 |         150 |       40 |     190 |          0.034 |      0.584 |      0.150 |     0.437 |                  0.342 |
|  69 | Nate Bennett             | Baylor                | Big 12            |   3 |          66 |        2 |      68 |          0.057 |      2.810 |      0.137 |     0.471 |                  0.986 |
|  70 | Arch Manning             | Texas                 | SEC               |   4 |         127 |       21 |     148 |          0.164 |     -0.035 |      0.135 |     0.466 |                  0.040 |
|  71 | Austin Carlisle          | UL Monroe             | Sun Belt          |   3 |          60 |       30 |      90 |         -0.173 |      0.739 |      0.131 |     0.556 |                 -0.093 |
|  72 | Trey Hedden              | New Mexico State      | Conference USA    |   4 |         123 |        7 |     130 |          0.110 |      0.421 |      0.127 |     0.408 |                 -0.052 |
|  73 | Demond Williams Jr.      | Washington            | Big Ten           |   5 |         176 |       36 |     212 |          0.045 |      0.528 |      0.127 |     0.467 |                  0.056 |
|  74 | Ksaan Farrar             | Colorado State        | Pac-12            |   3 |          77 |        5 |      82 |          0.091 |      0.677 |      0.126 |     0.439 |                 -0.226 |
|  75 | Jaden Craig              | TCU                   | Big 12            |   5 |         169 |       18 |     187 |          0.153 |     -0.142 |      0.124 |     0.449 |                  0.022 |
|  76 | D.J. Lagway              | Baylor                | Big 12            |   3 |         138 |        3 |     141 |          0.111 |      0.537 |      0.120 |     0.418 |                  0.116 |
|  77 | Luke Weaver              | San José State        | Mountain West     |   5 |         181 |       33 |     214 |          0.167 |     -0.155 |      0.117 |     0.467 |                  0.062 |
|  78 | Landy Lyddy              | Southern Miss         | Sun Belt          |   4 |          69 |        6 |      75 |          0.056 |      0.792 |      0.115 |     0.440 |                  0.118 |
|  79 | Hank Brown               | Iowa                  | Big Ten           |   5 |         127 |       13 |     140 |          0.132 |     -0.096 |      0.111 |     0.479 |                  0.066 |
|  80 | Alberto Mendoza          | Georgia Tech          | ACC               |   4 |         133 |        9 |     142 |          0.088 |      0.408 |      0.108 |     0.500 |                 -0.028 |
|  81 | Jackson Arnold           | UNLV                  | Mountain West     |   5 |         148 |       59 |     207 |          0.039 |      0.273 |      0.105 |     0.430 |                  0.140 |
|  82 | Davis Warren             | Stanford              | ACC               |   5 |         182 |        8 |     190 |          0.093 |      0.346 |      0.103 |     0.411 |                  0.270 |
|  83 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |   5 |         142 |       47 |     189 |          0.115 |      0.058 |      0.101 |     0.450 |                  0.199 |
|  84 | Rickie Collins           | Kennesaw State        | Conference USA    |   4 |         120 |       35 |     155 |          0.062 |      0.213 |      0.096 |     0.490 |                  0.027 |
|  85 | Landyn Locke             | Sam Houston           | Conference USA    |   4 |         155 |       16 |     171 |          0.067 |      0.356 |      0.094 |     0.450 |                  0.006 |
|  86 | Trey Owens               | Arkansas State        | Sun Belt          |   5 |         136 |       19 |     155 |          0.033 |      0.518 |      0.092 |     0.516 |                  0.189 |
|  87 | Will Hammond             | Texas Tech            | Big 12            |   5 |         148 |       13 |     161 |          0.076 |      0.278 |      0.092 |     0.472 |                  0.156 |
|  88 | Beau Pribula             | Virginia              | ACC               |   5 |         136 |       32 |     168 |          0.072 |      0.160 |      0.088 |     0.458 |                  0.177 |
|  89 | Kenny Minchey            | Kentucky              | SEC               |   5 |         149 |       13 |     162 |          0.098 |     -0.082 |      0.084 |     0.463 |                  0.059 |
|  90 | John Mateer              | Oklahoma              | SEC               |   4 |         117 |       33 |     150 |          0.123 |     -0.062 |      0.083 |     0.433 |                  0.047 |
|  91 | Cutter Boley             | Arizona State         | Big 12            |   4 |         132 |       19 |     151 |          0.069 |      0.178 |      0.083 |     0.464 |                  0.068 |
|  92 | Cibastian Broughton      | Akron                 | Mid-American      |   4 |          71 |       24 |      95 |         -0.057 |      0.491 |      0.082 |     0.474 |                  0.014 |
|  93 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |   5 |         172 |       37 |     209 |          0.013 |      0.400 |      0.081 |     0.431 |                  0.107 |
|  94 | Micah Alejado            | Hawai'i               | Mountain West     |   5 |         232 |       18 |     250 |          0.086 |     -0.017 |      0.079 |     0.456 |                  0.067 |
|  95 | Deshawn Purdie           | Liberty               | Conference USA    |   5 |         111 |       18 |     129 |          0.071 |      0.102 |      0.075 |     0.457 |                  0.097 |
|  96 | Nick Minicucci           | Delaware              | Conference USA    |   4 |         108 |       12 |     120 |         -0.005 |      0.748 |      0.070 |     0.450 |                  0.012 |
|  97 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |   4 |          74 |       30 |     104 |         -0.029 |      0.310 |      0.069 |     0.471 |                 -0.015 |
|  98 | Billy Edwards            | North Carolina        | ACC               |   4 |         114 |       10 |     124 |          0.038 |      0.368 |      0.065 |     0.468 |                 -0.015 |
|  99 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |   4 |         126 |       19 |     145 |          0.075 |     -0.033 |      0.061 |     0.428 |                  0.042 |
| 100 | Dexter Williams II       | Tulsa                 | American Athletic |   4 |          62 |        7 |      69 |         -0.008 |      0.639 |      0.058 |     0.435 |                  0.075 |
| 101 | Max Johnson              | Georgia Southern      | Sun Belt          |   5 |         192 |       15 |     207 |          0.046 |      0.214 |      0.058 |     0.425 |                  0.093 |
| 102 | Dru Deshields            | Kent State            | Mid-American      |   5 |         125 |       33 |     158 |         -0.070 |      0.520 |      0.053 |     0.380 |                  0.079 |
| 103 | Owen McCown              | UTSA                  | American Athletic |   5 |         154 |       17 |     171 |          0.055 |      0.019 |      0.051 |     0.427 |                  0.114 |
| 104 | Nico Iamaleava           | UCLA                  | Big Ten           |   4 |         106 |       26 |     132 |          0.036 |      0.110 |      0.051 |     0.432 |                  0.053 |
| 105 | J.J. Kohl                | Florida International | Conference USA    |   4 |         144 |       17 |     161 |          0.029 |      0.210 |      0.048 |     0.447 |                  0.074 |
| 106 | Steven Angeli            | Syracuse              | ACC               |   3 |         111 |        5 |     116 |          0.065 |     -0.327 |      0.048 |     0.405 |                  0.081 |
| 107 | Roman Gagliano           | Middle Tennessee      | Conference USA    |   5 |         162 |       13 |     175 |          0.034 |      0.208 |      0.047 |     0.411 |                  0.096 |
| 108 | Byrum Brown              | Auburn                | SEC               |   5 |         176 |       61 |     237 |         -0.083 |      0.391 |      0.039 |     0.439 |                 -0.078 |
| 109 | Taron Dickens            | Northern Illinois     | Mountain West     |   4 |         134 |       11 |     145 |          0.045 |     -0.083 |      0.035 |     0.469 |                  0.109 |
| 110 | Drake Lindsey            | Minnesota             | Big Ten           |   5 |         159 |        8 |     167 |          0.033 |      0.003 |      0.032 |     0.473 |                  0.024 |
| 111 | Julian Lewis             | Colorado              | Big 12            |   4 |         102 |        6 |     108 |          0.024 |      0.123 |      0.029 |     0.389 |                  0.069 |
| 112 | Skyler Locklear          | Missouri State        | Conference USA    |   4 |          92 |       17 |     109 |          0.059 |     -0.141 |      0.028 |     0.385 |                  0.017 |
| 113 | Malik Washington         | Maryland              | Big Ten           |   5 |         203 |       20 |     223 |          0.032 |     -0.028 |      0.026 |     0.426 |                 -0.040 |
| 114 | Brock Glenn              | Western Kentucky      | Conference USA    |   5 |          66 |       33 |      99 |         -0.092 |      0.256 |      0.024 |     0.455 |                 -0.401 |
| 115 | M.Van Buren Jr.          | South Florida         | American Athletic |   5 |         130 |       25 |     155 |         -0.000 |      0.077 |      0.012 |     0.477 |                 -0.052 |
| 116 | Quinn Henicle            | Old Dominion          | Sun Belt          |   4 |          79 |       41 |     120 |         -0.237 |      0.478 |      0.007 |     0.375 |                 -0.062 |
| 117 | Marcel Reed              | Texas A&M             | SEC               |   5 |         156 |       35 |     191 |         -0.068 |      0.329 |      0.004 |     0.403 |                 -0.056 |
| 118 | Baylor Hayes             | Tulsa                 | American Athletic |   3 |          98 |       16 |     114 |         -0.071 |      0.414 |     -0.003 |     0.360 |                 -0.050 |
| 119 | KJ Jackson               | Arkansas              | SEC               |   5 |         168 |       29 |     197 |         -0.024 |      0.049 |     -0.014 |     0.462 |                 -0.010 |
| 120 | Jay Kastantin            | Bowling Green         | Mid-American      |   5 |         132 |       18 |     150 |          0.019 |     -0.285 |     -0.017 |     0.440 |                  0.003 |
| 121 | Jaron-Keawe Sagapolutele | California            | ACC               |   5 |         170 |        6 |     176 |         -0.016 |     -0.252 |     -0.024 |     0.403 |                 -0.077 |
| 122 | Faizon Brandon           | Tennessee             | SEC               |   5 |         116 |       36 |     152 |         -0.184 |      0.488 |     -0.025 |     0.408 |                 -0.136 |
| 123 | Isaac Wilson             | Colorado              | Big 12            |   3 |          74 |       19 |      93 |          0.104 |     -0.525 |     -0.025 |     0.441 |                  0.037 |
| 124 | Broc Lowry               | Western Michigan      | Mid-American      |   5 |         122 |       47 |     169 |         -0.093 |      0.133 |     -0.030 |     0.456 |                  0.052 |
| 125 | Noah Kim                 | Eastern Michigan      | Mid-American      |   6 |         208 |       16 |     224 |         -0.035 |     -0.005 |     -0.033 |     0.406 |                  0.014 |
| 126 | Alessio Milivojevic      | Michigan State        | Big Ten           |   5 |         143 |       16 |     159 |         -0.074 |      0.203 |     -0.046 |     0.465 |                 -0.114 |
| 127 | Keyone Jenkins           | UCF                   | Big 12            |   5 |          77 |       14 |      91 |         -0.089 |      0.168 |     -0.049 |     0.429 |                 -0.058 |
| 128 | Mason McKenzie           | Boston College        | ACC               |   5 |         153 |       79 |     232 |         -0.201 |      0.232 |     -0.053 |     0.431 |                  0.014 |
| 129 | Will Crowder             | Troy                  | Sun Belt          |   4 |         141 |       18 |     159 |         -0.108 |      0.338 |     -0.057 |     0.409 |                 -0.010 |
| 130 | Tyler Hughes             | Wyoming               | Mountain West     |   5 |         120 |       41 |     161 |         -0.208 |      0.376 |     -0.060 |     0.435 |                 -0.048 |
| 131 | Keldric Luster           | Ball State            | Mid-American      |   4 |         126 |       25 |     151 |         -0.103 |      0.149 |     -0.061 |     0.391 |                  0.048 |
| 132 | Jackson Sharman          | Sacramento State      | Mid-American      |   4 |         148 |        8 |     156 |         -0.060 |     -0.533 |     -0.084 |     0.429 |                  0.006 |
| 133 | Carter Jones             | Nevada                | Mountain West     |   3 |          74 |       20 |      94 |         -0.135 |      0.084 |     -0.088 |     0.394 |                 -0.164 |
| 134 | Mitch Griffis            | East Carolina         | American Athletic |   4 |          73 |       17 |      90 |         -0.156 |      0.149 |     -0.098 |     0.411 |                 -0.150 |
| 135 | Jason Wright             | Buffalo               | Mid-American      |   4 |         106 |       22 |     128 |         -0.136 |     -0.048 |     -0.121 |     0.359 |                 -0.136 |
| 136 | Grady Brosterhous        | Utah State            | Pac-12            |   5 |         132 |       59 |     191 |         -0.129 |     -0.121 |     -0.126 |     0.346 |                 -0.182 |
| 137 | Caden Pinnick            | Washington State      | Pac-12            |   5 |         156 |       46 |     202 |         -0.169 |     -0.018 |     -0.135 |     0.396 |                 -0.099 |
| 138 | Ethan Hampton            | Southern Miss         | Sun Belt          |   3 |          76 |        6 |      82 |         -0.119 |     -0.437 |     -0.142 |     0.439 |                 -0.232 |
| 139 | Tait Reynolds            | Clemson               | ACC               |   5 |         145 |       36 |     181 |         -0.137 |     -0.201 |     -0.150 |     0.409 |                 -0.102 |
| 140 | Jayden Denegal           | San Diego State       | Pac-12            |   5 |         128 |       14 |     142 |         -0.144 |     -0.271 |     -0.156 |     0.352 |                 -0.236 |
| 141 | Cole Gonzales            | Charlotte             | American Athletic |   5 |         128 |       11 |     139 |         -0.115 |     -0.756 |     -0.166 |     0.424 |                 -0.304 |
| 142 | Kadin Semonza            | Tulane                | American Athletic |   4 |         105 |       13 |     118 |         -0.146 |     -0.339 |     -0.167 |     0.305 |                 -0.147 |
| 143 | Elijah Holmes            | Buffalo               | Mid-American      |   2 |          64 |        7 |      71 |         -0.181 |     -0.044 |     -0.167 |     0.366 |                 -0.174 |
| 144 | Brayden Roggow           | Akron                 | Mid-American      |   5 |         104 |        8 |     112 |         -0.229 |      0.464 |     -0.180 |     0.393 |                 -0.411 |
| 145 | EJ Colson                | UTEP                  | Mountain West     |   5 |          91 |       50 |     141 |         -0.246 |     -0.093 |     -0.192 |     0.433 |                 -0.244 |
| 146 | Ryan Huff                | Old Dominion          | Sun Belt          |   3 |          61 |        3 |      64 |         -0.269 |      0.594 |     -0.228 |     0.297 |                 -0.253 |
