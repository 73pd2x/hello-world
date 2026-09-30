# 2026 CFB QB EPA — through Week 4

FBS offenses, games through Sep 26, 2026 (Week 0 games are folded into Week 1).
**Minimum 60 dropbacks**, which leaves 137 QBs. Sorted by EPA/play over all dropbacks + QB rushes.

- **Dropbacks** = pass attempts + sacks. **Rushes** = designed runs + scrambles.
- **Success** = share of plays with positive EPA.
- **EPA/play (WP 10–90%)** leaves out garbage time.
- Not opponent-adjusted, so a team that has played FCS opponents looks better.
- Source: cfbfastR play-by-play (`sportsdataverse/cfbfastR-data`, `data/rds/pbp_players_pos_2026.rds`). Rebuild with `python qb_epa.py <rds> [min_dropbacks]` then `python make_readme.py <week> "<through date>"`.

Full tables: [`qb_epa_2026.csv`](qb_epa_2026.csv), [`qb_epa_2026_nongarbage.csv`](qb_epa_2026_nongarbage.csv)

## Non-garbage time (win probability 10–90%)

Same 60-dropback pool, plus at least 40 plays in competitive game states (128 QBs).

|   # |   Overall # | QB                       | Team                  | Conf              |   Plays (WP 10–90%) |   EPA/play (WP 10–90%) |   Success (WP 10–90%) |   EPA/play (all) |
|----:|------------:|:-------------------------|:----------------------|:------------------|--------------------:|-----------------------:|----------------------:|-----------------:|
|   1 |           9 | Darian Mensah            | Miami                 | ACC               |                  41 |                  0.721 |                 0.634 |            0.385 |
|   2 |           2 | Bear Bachmeier           | BYU                   | Big 12            |                  43 |                  0.688 |                 0.605 |            0.406 |
|   3 |           3 | Keelon Russell           | Alabama               | SEC               |                  77 |                  0.667 |                 0.610 |            0.402 |
|   4 |          11 | Josh Hoover              | Indiana               | Big Ten           |                  60 |                  0.601 |                 0.633 |            0.348 |
|   5 |           5 | Julian Sayin             | Ohio State            | Big Ten           |                  65 |                  0.518 |                 0.585 |            0.397 |
|   6 |           8 | Tayven Jackson           | North Texas           | American Athletic |                  84 |                  0.484 |                 0.571 |            0.390 |
|   7 |           1 | David McComb             | Miami (OH)            | Mid-American      |                  78 |                  0.470 |                 0.526 |            0.528 |
|   8 |           7 | Kevin Jennings           | SMU                   | ACC               |                 117 |                  0.465 |                 0.632 |            0.390 |
|   9 |          12 | Aaron Philo              | Florida               | SEC               |                  73 |                  0.452 |                 0.589 |            0.342 |
|  10 |          35 | Michael Hawkins Jr.      | West Virginia         | Big 12            |                  83 |                  0.445 |                 0.542 |            0.239 |
|  11 |          14 | Jayden Maiava            | USC                   | Big Ten           |                 110 |                  0.431 |                 0.573 |            0.330 |
|  12 |          26 | Marcus Stokes            | Memphis               | American Athletic |                  94 |                  0.421 |                 0.543 |            0.270 |
|  13 |          85 | Kalieb Osborne           | UConn                 | FBS Independents  |                  62 |                  0.418 |                 0.484 |            0.084 |
|  14 |          18 | JC French                | Cincinnati            | Big 12            |                 103 |                  0.409 |                 0.573 |            0.313 |
|  15 |          37 | William Watson III       | Massachusetts         | Mid-American      |                  58 |                  0.405 |                 0.448 |            0.225 |
|  16 |          50 | Katin Houser             | Illinois              | Big Ten           |                  81 |                  0.389 |                 0.519 |            0.182 |
|  17 |         103 | Drake Lindsey            | Minnesota             | Big Ten           |                  56 |                  0.379 |                 0.518 |            0.007 |
|  18 |          33 | Dylan Lonergan           | Rutgers               | Big Ten           |                  50 |                  0.379 |                 0.560 |            0.249 |
|  19 |          45 | CJ Bailey                | NC State              | ACC               |                  63 |                  0.377 |                 0.556 |            0.195 |
|  20 |          27 | Austin Simmons           | Missouri              | SEC               |                  86 |                  0.371 |                 0.477 |            0.269 |
|  21 |          64 | Beau Pribula             | Virginia              | ACC               |                  61 |                  0.369 |                 0.508 |            0.138 |
|  22 |          36 | Trinidad Chambliss       | Ole Miss              | SEC               |                 125 |                  0.367 |                 0.528 |            0.239 |
|  23 |          97 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |                  76 |                  0.364 |                 0.500 |            0.029 |
|  24 |          20 | John Alan Richter        | Toledo                | Mid-American      |                  76 |                  0.357 |                 0.513 |            0.297 |
|  25 |          22 | Ajani Sheppard           | Temple                | American Athletic |                  76 |                  0.357 |                 0.461 |            0.289 |
|  26 |          17 | Anthony Colandrea        | Nebraska              | Big Ten           |                  84 |                  0.352 |                 0.488 |            0.323 |
|  27 |          29 | Ashton Daniels           | Florida State         | ACC               |                  93 |                  0.343 |                 0.452 |            0.261 |
|  28 |          28 | Kamario Taylor           | Mississippi State     | SEC               |                  99 |                  0.340 |                 0.545 |            0.262 |
|  29 |          10 | Conner Weigman           | Houston               | Big 12            |                  93 |                  0.339 |                 0.538 |            0.362 |
|  30 |          15 | C.J. Carr                | Notre Dame            | FBS Independents  |                  59 |                  0.334 |                 0.475 |            0.330 |
|  31 |          82 | Cameran Brown            | Georgia State         | Sun Belt          |                  83 |                  0.332 |                 0.614 |            0.091 |
|  32 |          52 | Noah Fifita              | Arizona               | Big 12            |                 111 |                  0.311 |                 0.559 |            0.169 |
|  33 |          42 | Davis Warren             | Stanford              | ACC               |                  97 |                  0.305 |                 0.454 |            0.201 |
|  34 |          59 | Devon Dampier            | Utah                  | Big 12            |                  48 |                  0.295 |                 0.542 |            0.154 |
|  35 |          21 | Bishop Davenport         | South Alabama         | Sun Belt          |                  60 |                  0.293 |                 0.483 |            0.294 |
|  36 |         101 | Nathan Hayes             | North Dakota State    | Mountain West     |                  58 |                  0.292 |                 0.483 |            0.012 |
|  37 |          81 | Jared Hollins            | South Alabama         | Sun Belt          |                  54 |                  0.288 |                 0.500 |            0.092 |
|  38 |          13 | Lincoln Kienholz         | Louisville            | ACC               |                 128 |                  0.284 |                 0.492 |            0.331 |
|  39 |          49 | Malachi Singleton        | App State             | Sun Belt          |                  91 |                  0.278 |                 0.484 |            0.192 |
|  40 |          30 | Avery Johnson            | Kansas State          | Big 12            |                 104 |                  0.270 |                 0.490 |            0.260 |
|  41 |          24 | Maddux Madsen            | Boise State           | Pac-12            |                 103 |                  0.268 |                 0.553 |            0.279 |
|  42 |          25 | Giovanni Lopez           | Wake Forest           | ACC               |                  95 |                  0.263 |                 0.526 |            0.278 |
|  43 |          44 | Bryce Underwood          | Michigan              | Big Ten           |                 126 |                  0.259 |                 0.516 |            0.197 |
|  44 |           6 | Brad Jackson             | Texas State           | Pac-12            |                  84 |                  0.256 |                 0.500 |            0.393 |
|  45 |         105 | Camden Coleman           | James Madison         | Sun Belt          |                  55 |                  0.253 |                 0.527 |            0.003 |
|  46 |          41 | Mason Heintschel         | Pittsburgh            | ACC               |                  81 |                  0.247 |                 0.506 |            0.211 |
|  47 |           4 | Hauss Hejny              | Colorado State        | Pac-12            |                  55 |                  0.245 |                 0.491 |            0.400 |
|  48 |          48 | Caden Creel              | Jacksonville State    | Conference USA    |                 127 |                  0.242 |                 0.528 |            0.192 |
|  49 |          57 | Isaiah Marshall          | Kansas                | Big 12            |                  77 |                  0.234 |                 0.390 |            0.156 |
|  50 |          40 | Aidan Chiles             | Northwestern          | Big Ten           |                  74 |                  0.219 |                 0.473 |            0.213 |
|  51 |          23 | Ryan Browne              | Purdue                | Big Ten           |                 101 |                  0.215 |                 0.515 |            0.287 |
|  52 |         104 | Owen McCown              | UTSA                  | American Athletic |                  89 |                  0.207 |                 0.483 |            0.005 |
|  53 |          32 | Braden Atkinson          | Oregon State          | Pac-12            |                  99 |                  0.207 |                 0.434 |            0.255 |
|  54 |          90 | Taron Dickens            | Northern Illinois     | Mountain West     |                  74 |                  0.206 |                 0.527 |            0.065 |
|  55 |          68 | Will Hammond             | Texas Tech            | Big 12            |                  88 |                  0.204 |                 0.523 |            0.119 |
|  56 |          88 | Trey Owens               | Arkansas State        | Sun Belt          |                 102 |                  0.200 |                 0.539 |            0.068 |
|  57 |          72 | Cutter Boley             | Arizona State         | Big 12            |                  61 |                  0.196 |                 0.459 |            0.110 |
|  58 |          70 | Dante Moore              | Oregon                | Big Ten           |                  84 |                  0.193 |                 0.417 |            0.117 |
|  59 |          19 | Jared Curtis             | Vanderbilt            | SEC               |                  98 |                  0.179 |                 0.459 |            0.312 |
|  60 |          69 | Jayden Mandal            | Fresno State          | Pac-12            |                  89 |                  0.170 |                 0.483 |            0.117 |
|  61 |          39 | Caden Veltkamp           | Florida Atlantic      | American Athletic |                 106 |                  0.168 |                 0.491 |            0.220 |
|  62 |          56 | Hank Brown               | Iowa                  | Big Ten           |                  78 |                  0.161 |                 0.462 |            0.157 |
|  63 |          53 | Malik Washington         | Maryland              | Big Ten           |                  75 |                  0.153 |                 0.440 |            0.166 |
|  64 |         109 | Steven Angeli            | Syracuse              | ACC               |                  81 |                  0.150 |                 0.420 |           -0.005 |
|  65 |          65 | Deshawn Purdie           | Liberty               | Conference USA    |                  90 |                  0.140 |                 0.467 |            0.136 |
|  66 |          55 | Rocco Becht              | Penn State            | Big Ten           |                  67 |                  0.130 |                 0.418 |            0.163 |
|  67 |          89 | J.J. Kohl                | Florida International | Conference USA    |                 121 |                  0.130 |                 0.446 |            0.066 |
|  68 |          74 | Dru Deshields            | Kent State            | Mid-American      |                  64 |                  0.129 |                 0.438 |            0.102 |
|  69 |          76 | Nick Minicucci           | Delaware              | Conference USA    |                  81 |                  0.125 |                 0.432 |            0.100 |
|  70 |          58 | Drew Mestemaker          | Oklahoma State        | Big 12            |                 118 |                  0.123 |                 0.492 |            0.155 |
|  71 |          73 | Micah Alejado            | Hawai'i               | Mountain West     |                 168 |                  0.114 |                 0.458 |            0.107 |
|  72 |          60 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |                 104 |                  0.112 |                 0.462 |            0.153 |
|  73 |          47 | Ryder Burton             | UAB                   | American Athletic |                  93 |                  0.107 |                 0.452 |            0.193 |
|  74 |          86 | Roman Gagliano           | Middle Tennessee      | Conference USA    |                 119 |                  0.106 |                 0.437 |            0.084 |
|  75 |          77 | Sam Leavitt              | LSU                   | SEC               |                  86 |                  0.105 |                 0.500 |            0.099 |
|  76 |          80 | Jackson Arnold           | UNLV                  | Mountain West     |                 132 |                  0.104 |                 0.439 |            0.093 |
|  77 |         122 | Will Crowder             | Troy                  | Sun Belt          |                 112 |                  0.092 |                 0.429 |           -0.068 |
|  78 |          61 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |                  76 |                  0.078 |                 0.461 |            0.147 |
|  79 |          84 | Demond Williams Jr.      | Washington            | Big Ten           |                 127 |                  0.078 |                 0.488 |            0.085 |
|  80 |          62 | Colton Joseph            | Wisconsin             | Big Ten           |                  94 |                  0.063 |                 0.436 |            0.143 |
|  81 |          34 | Cibastian Broughton      | Akron                 | Mid-American      |                  42 |                  0.062 |                 0.452 |            0.246 |
|  82 |          94 | KJ Jackson               | Arkansas              | SEC               |                  69 |                  0.058 |                 0.464 |            0.035 |
|  83 |          75 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |                 121 |                  0.052 |                 0.405 |            0.101 |
|  84 |         106 | Skyler Locklear          | Missouri State        | Conference USA    |                  82 |                  0.046 |                 0.415 |            0.001 |
|  85 |          66 | Jaden Craig              | TCU                   | Big 12            |                 116 |                  0.041 |                 0.431 |            0.136 |
|  86 |         115 | Max Johnson              | Georgia Southern      | Sun Belt          |                 106 |                  0.036 |                 0.387 |           -0.036 |
|  87 |          93 | Alessio Milivojevic      | Michigan State        | Big Ten           |                 102 |                 -0.001 |                 0.480 |            0.052 |
|  88 |          99 | John Mateer              | Oklahoma              | SEC               |                  84 |                 -0.007 |                 0.452 |            0.023 |
|  89 |          38 | Trey Hedden              | New Mexico State      | Conference USA    |                  85 |                 -0.008 |                 0.400 |            0.225 |
|  90 |         120 | Tyler Hughes             | Wyoming               | Mountain West     |                 102 |                 -0.010 |                 0.441 |           -0.048 |
|  91 |          98 | Byrum Brown              | Auburn                | SEC               |                 112 |                 -0.024 |                 0.420 |            0.023 |
|  92 |          92 | Arch Manning             | Texas                 | SEC               |                  86 |                 -0.025 |                 0.442 |            0.056 |
|  93 |          54 | Landyn Locke             | Sam Houston           | Conference USA    |                 114 |                 -0.035 |                 0.439 |            0.164 |
|  94 |         135 | Broc Lowry               | Western Michigan      | Mid-American      |                  89 |                 -0.036 |                 0.449 |           -0.209 |
|  95 |          67 | Alberto Mendoza          | Georgia Tech          | ACC               |                  98 |                 -0.037 |                 0.469 |            0.124 |
|  96 |          78 | Luke Weaver              | San José State        | Mountain West     |                 138 |                 -0.048 |                 0.442 |            0.099 |
|  97 |          71 | Jaylen Raynor            | Iowa State            | Big 12            |                  66 |                 -0.049 |                 0.409 |            0.111 |
|  98 |         108 | Julian Lewis             | Colorado              | Big 12            |                  70 |                 -0.050 |                 0.400 |           -0.004 |
|  99 |         130 | Nico Iamaleava           | UCLA                  | Big Ten           |                 104 |                 -0.052 |                 0.385 |           -0.136 |
| 100 |         125 | Billy Edwards            | North Carolina        | ACC               |                  80 |                 -0.057 |                 0.425 |           -0.081 |
| 101 |          87 | Jackson Sharman          | Sacramento State      | Mid-American      |                  41 |                 -0.059 |                 0.439 |            0.083 |
| 102 |         127 | Carter Jones             | Nevada                | Mountain West     |                  74 |                 -0.060 |                 0.405 |           -0.107 |
| 103 |          51 | Rickie Collins           | Kennesaw State        | Conference USA    |                  67 |                 -0.073 |                 0.448 |            0.169 |
| 104 |         116 | D.J. Lagway              | Baylor                | Big 12            |                  83 |                 -0.077 |                 0.386 |           -0.039 |
| 105 |         124 | Elijah Holmes            | Buffalo               | Mid-American      |                  68 |                 -0.078 |                 0.382 |           -0.076 |
| 106 |         118 | Jaron-Keawe Sagapolutele | California            | ACC               |                 110 |                 -0.082 |                 0.400 |           -0.040 |
| 107 |         110 | Faizon Brandon           | Tennessee             | SEC               |                  83 |                 -0.083 |                 0.386 |           -0.011 |
| 108 |         111 | Caden Pinnick            | Washington State      | Pac-12            |                 111 |                 -0.091 |                 0.441 |           -0.025 |
| 109 |         107 | M.Van Buren Jr.          | South Florida         | American Athletic |                  84 |                 -0.091 |                 0.452 |           -0.003 |
| 110 |         121 | Mason McKenzie           | Boston College        | ACC               |                 114 |                 -0.096 |                 0.430 |           -0.062 |
| 111 |          95 | Jay Kastantin            | Bowling Green         | Mid-American      |                  62 |                 -0.104 |                 0.355 |            0.031 |
| 112 |         123 | Walker Eget              | Duke                  | ACC               |                  74 |                 -0.113 |                 0.473 |           -0.070 |
| 113 |         129 | Kadin Semonza            | Tulane                | American Athletic |                  89 |                 -0.114 |                 0.348 |           -0.134 |
| 114 |         126 | Keldric Luster           | Ball State            | Mid-American      |                  46 |                 -0.117 |                 0.413 |           -0.101 |
| 115 |         133 | Ethan Hampton            | Southern Miss         | Sun Belt          |                  43 |                 -0.127 |                 0.512 |           -0.153 |
| 116 |         114 | Kenny Minchey            | Kentucky              | SEC               |                  77 |                 -0.135 |                 0.455 |           -0.035 |
| 117 |          46 | Austin Carlisle          | UL Monroe             | Sun Belt          |                  54 |                 -0.146 |                 0.481 |            0.193 |
| 118 |         136 | Tait Reynolds            | Clemson               | ACC               |                 107 |                 -0.157 |                 0.439 |           -0.213 |
| 119 |         128 | Jason Wright             | Buffalo               | Mid-American      |                  53 |                 -0.163 |                 0.396 |           -0.115 |
| 120 |         119 | Marcel Reed              | Texas A&M             | SEC               |                  98 |                 -0.170 |                 0.378 |           -0.042 |
| 121 |          96 | Lanorris Sellers         | South Carolina        | SEC               |                  69 |                 -0.177 |                 0.464 |            0.031 |
| 122 |         132 | Mitch Griffis            | East Carolina         | American Athletic |                  53 |                 -0.178 |                 0.377 |           -0.152 |
| 123 |         131 | Jayden Denegal           | San Diego State       | Pac-12            |                  66 |                 -0.221 |                 0.348 |           -0.137 |
| 124 |         100 | Quinn Henicle            | Old Dominion          | Sun Belt          |                  56 |                 -0.261 |                 0.286 |            0.017 |
| 125 |         112 | Cole Gonzales            | Charlotte             | American Athletic |                  82 |                 -0.261 |                 0.415 |           -0.026 |
| 126 |         134 | EJ Colson                | UTEP                  | Mountain West     |                  47 |                 -0.270 |                 0.426 |           -0.158 |
| 127 |         137 | Grady Brosterhous        | Utah State            | Pac-12            |                  79 |                 -0.310 |                 0.278 |           -0.224 |
| 128 |         113 | Noah Kim                 | Eastern Michigan      | Mid-American      |                 106 |                 -0.323 |                 0.340 |           -0.035 |

## All plays

|   # | QB                       | Team                  | Conf              |   G |   Dropbacks |   Rushes |   Plays |   EPA/dropback |   EPA/rush |   EPA/play |   Success |   EPA/play (WP 10–90%) |
|----:|:-------------------------|:----------------------|:------------------|----:|------------:|---------:|--------:|---------------:|-----------:|-----------:|----------:|-----------------------:|
|   1 | David McComb             | Miami (OH)            | Mid-American      |   4 |         109 |       11 |     120 |          0.525 |      0.565 |      0.528 |     0.533 |                  0.470 |
|   2 | Bear Bachmeier           | BYU                   | Big 12            |   3 |          64 |       10 |      74 |          0.351 |      0.761 |      0.406 |     0.581 |                  0.688 |
|   3 | Keelon Russell           | Alabama               | SEC               |   4 |         118 |       24 |     142 |          0.362 |      0.596 |      0.402 |     0.570 |                  0.667 |
|   4 | Hauss Hejny              | Colorado State        | Pac-12            |   3 |          74 |       12 |      86 |          0.379 |      0.533 |      0.400 |     0.523 |                  0.245 |
|   5 | Julian Sayin             | Ohio State            | Big Ten           |   4 |         120 |       11 |     131 |          0.365 |      0.748 |      0.397 |     0.565 |                  0.518 |
|   6 | Brad Jackson             | Texas State           | Pac-12            |   4 |          95 |       27 |     122 |          0.478 |      0.092 |      0.393 |     0.533 |                  0.256 |
|   7 | Kevin Jennings           | SMU                   | ACC               |   4 |         131 |       17 |     148 |          0.459 |     -0.138 |      0.390 |     0.588 |                  0.465 |
|   8 | Tayven Jackson           | North Texas           | American Athletic |   4 |         128 |       13 |     141 |          0.381 |      0.487 |      0.390 |     0.567 |                  0.484 |
|   9 | Darian Mensah            | Miami                 | ACC               |   4 |         107 |        7 |     114 |          0.350 |      0.927 |      0.385 |     0.579 |                  0.721 |
|  10 | Conner Weigman           | Houston               | Big 12            |   4 |         106 |       25 |     131 |          0.374 |      0.312 |      0.362 |     0.565 |                  0.339 |
|  11 | Josh Hoover              | Indiana               | Big Ten           |   4 |          85 |        9 |      94 |          0.329 |      0.528 |      0.348 |     0.553 |                  0.601 |
|  12 | Aaron Philo              | Florida               | SEC               |   4 |          89 |       22 |     111 |          0.399 |      0.111 |      0.342 |     0.550 |                  0.452 |
|  13 | Lincoln Kienholz         | Louisville            | ACC               |   4 |         116 |       38 |     154 |          0.359 |      0.247 |      0.331 |     0.506 |                  0.284 |
|  14 | Jayden Maiava            | USC                   | Big Ten           |   5 |         162 |       10 |     172 |          0.375 |     -0.410 |      0.330 |     0.587 |                  0.431 |
|  15 | C.J. Carr                | Notre Dame            | FBS Independents  |   4 |          97 |        6 |     103 |          0.304 |      0.737 |      0.330 |     0.524 |                  0.334 |
|  16 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |   3 |          83 |       15 |      98 |          0.303 |      0.462 |      0.327 |     0.469 |                  0.295 |
|  17 | Anthony Colandrea        | Nebraska              | Big Ten           |   4 |         107 |       23 |     130 |          0.277 |      0.534 |      0.323 |     0.508 |                  0.352 |
|  18 | JC French                | Cincinnati            | Big 12            |   4 |          99 |       36 |     135 |          0.312 |      0.318 |      0.313 |     0.563 |                  0.409 |
|  19 | Jared Curtis             | Vanderbilt            | SEC               |   4 |         104 |       32 |     136 |          0.204 |      0.663 |      0.312 |     0.493 |                  0.179 |
|  20 | John Alan Richter        | Toledo                | Mid-American      |   4 |         120 |        3 |     123 |          0.346 |     -1.670 |      0.297 |     0.496 |                  0.357 |
|  21 | Bishop Davenport         | South Alabama         | Sun Belt          |   2 |          61 |       16 |      77 |          0.291 |      0.303 |      0.294 |     0.468 |                  0.293 |
|  22 | Ajani Sheppard           | Temple                | American Athletic |   4 |          62 |       28 |      90 |          0.312 |      0.237 |      0.289 |     0.444 |                  0.357 |
|  23 | Ryan Browne              | Purdue                | Big Ten           |   4 |         132 |        9 |     141 |          0.280 |      0.401 |      0.287 |     0.546 |                  0.215 |
|  24 | Maddux Madsen            | Boise State           | Pac-12            |   4 |         115 |       13 |     128 |          0.202 |      0.956 |      0.279 |     0.547 |                  0.268 |
|  25 | Giovanni Lopez           | Wake Forest           | ACC               |   4 |         126 |       24 |     150 |          0.261 |      0.366 |      0.278 |     0.520 |                  0.263 |
|  26 | Marcus Stokes            | Memphis               | American Athletic |   4 |         104 |       22 |     126 |          0.319 |      0.036 |      0.270 |     0.492 |                  0.421 |
|  27 | Austin Simmons           | Missouri              | SEC               |   4 |         110 |        6 |     116 |          0.309 |     -0.449 |      0.269 |     0.457 |                  0.371 |
|  28 | Kamario Taylor           | Mississippi State     | SEC               |   4 |         128 |       28 |     156 |          0.227 |      0.422 |      0.262 |     0.538 |                  0.340 |
|  29 | Ashton Daniels           | Florida State         | ACC               |   4 |         104 |       32 |     136 |          0.228 |      0.367 |      0.261 |     0.456 |                  0.343 |
|  30 | Avery Johnson            | Kansas State          | Big 12            |   4 |         133 |       29 |     162 |          0.189 |      0.586 |      0.260 |     0.512 |                  0.270 |
|  31 | Aidan Armenta            | UL Monroe             | Sun Belt          |   3 |          70 |        9 |      79 |          0.269 |      0.175 |      0.258 |     0.468 |                 -0.226 |
|  32 | Braden Atkinson          | Oregon State          | Pac-12            |   4 |         169 |        7 |     176 |          0.269 |     -0.090 |      0.255 |     0.449 |                  0.207 |
|  33 | Dylan Lonergan           | Rutgers               | Big Ten           |   3 |          86 |       10 |      96 |          0.286 |     -0.066 |      0.249 |     0.490 |                  0.379 |
|  34 | Cibastian Broughton      | Akron                 | Mid-American      |   4 |          71 |       24 |      95 |          0.135 |      0.575 |      0.246 |     0.495 |                  0.062 |
|  35 | Michael Hawkins Jr.      | West Virginia         | Big 12            |   4 |          66 |       65 |     131 |          0.063 |      0.418 |      0.239 |     0.489 |                  0.445 |
|  36 | Trinidad Chambliss       | Ole Miss              | SEC               |   4 |         150 |       22 |     172 |          0.178 |      0.651 |      0.239 |     0.512 |                  0.367 |
|  37 | William Watson III       | Massachusetts         | Mid-American      |   4 |          77 |       21 |      98 |          0.131 |      0.571 |      0.225 |     0.439 |                  0.405 |
|  38 | Trey Hedden              | New Mexico State      | Conference USA    |   4 |         123 |        7 |     130 |          0.199 |      0.683 |      0.225 |     0.431 |                 -0.008 |
|  39 | Caden Veltkamp           | Florida Atlantic      | American Athletic |   4 |         167 |        9 |     176 |          0.217 |      0.292 |      0.220 |     0.517 |                  0.168 |
|  40 | Aidan Chiles             | Northwestern          | Big Ten           |   3 |          83 |       22 |     105 |          0.194 |      0.286 |      0.213 |     0.467 |                  0.219 |
|  41 | Mason Heintschel         | Pittsburgh            | ACC               |   4 |         134 |       22 |     156 |          0.251 |     -0.031 |      0.211 |     0.487 |                  0.247 |
|  42 | Davis Warren             | Stanford              | ACC               |   4 |         149 |        7 |     156 |          0.207 |      0.073 |      0.201 |     0.429 |                  0.305 |
|  43 | Ksaan Farrar             | Colorado State        | Pac-12            |   3 |          77 |        5 |      82 |          0.165 |      0.713 |      0.198 |     0.451 |                 -0.484 |
|  44 | Bryce Underwood          | Michigan              | Big Ten           |   4 |          99 |       40 |     139 |          0.257 |      0.047 |      0.197 |     0.482 |                  0.259 |
|  45 | CJ Bailey                | NC State              | ACC               |   4 |         115 |       21 |     136 |          0.189 |      0.227 |      0.195 |     0.493 |                  0.377 |
|  46 | Austin Carlisle          | UL Monroe             | Sun Belt          |   3 |          60 |       30 |      90 |         -0.087 |      0.752 |      0.193 |     0.533 |                 -0.146 |
|  47 | Ryder Burton             | UAB                   | American Athletic |   4 |         103 |       23 |     126 |          0.170 |      0.294 |      0.193 |     0.468 |                  0.107 |
|  48 | Caden Creel              | Jacksonville State    | Conference USA    |   5 |         131 |       63 |     194 |          0.171 |      0.235 |      0.192 |     0.531 |                  0.242 |
|  49 | Malachi Singleton        | App State             | Sun Belt          |   4 |         136 |       25 |     161 |          0.292 |     -0.353 |      0.192 |     0.503 |                  0.278 |
|  50 | Katin Houser             | Illinois              | Big Ten           |   4 |         125 |       12 |     137 |          0.134 |      0.677 |      0.182 |     0.504 |                  0.389 |
|  51 | Rickie Collins           | Kennesaw State        | Conference USA    |   4 |         120 |       35 |     155 |          0.103 |      0.396 |      0.169 |     0.510 |                 -0.073 |
|  52 | Noah Fifita              | Arizona               | Big 12            |   4 |         141 |       22 |     163 |          0.136 |      0.383 |      0.169 |     0.521 |                  0.311 |
|  53 | Malik Washington         | Maryland              | Big Ten           |   4 |         158 |       11 |     169 |          0.165 |      0.185 |      0.166 |     0.467 |                  0.153 |
|  54 | Landyn Locke             | Sam Houston           | Conference USA    |   4 |         155 |       16 |     171 |          0.090 |      0.879 |      0.164 |     0.456 |                 -0.035 |
|  55 | Rocco Becht              | Penn State            | Big Ten           |   4 |          97 |       13 |     110 |          0.224 |     -0.294 |      0.163 |     0.445 |                  0.130 |
|  56 | Hank Brown               | Iowa                  | Big Ten           |   4 |          98 |       11 |     109 |          0.205 |     -0.271 |      0.157 |     0.459 |                  0.161 |
|  57 | Isaiah Marshall          | Kansas                | Big 12            |   3 |          87 |       33 |     120 |          0.117 |      0.261 |      0.156 |     0.400 |                  0.234 |
|  58 | Drew Mestemaker          | Oklahoma State        | Big 12            |   4 |         146 |       10 |     156 |          0.112 |      0.789 |      0.155 |     0.513 |                  0.123 |
|  59 | Devon Dampier            | Utah                  | Big 12            |   4 |         104 |       30 |     134 |          0.203 |     -0.016 |      0.154 |     0.537 |                  0.295 |
|  60 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |   4 |         136 |       27 |     163 |          0.088 |      0.481 |      0.153 |     0.423 |                  0.112 |
|  61 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |   4 |          95 |       48 |     143 |         -0.007 |      0.451 |      0.147 |     0.455 |                  0.078 |
|  62 | Colton Joseph            | Wisconsin             | Big Ten           |   4 |         125 |       32 |     157 |          0.099 |      0.317 |      0.143 |     0.465 |                  0.063 |
|  63 | Dexter Williams II       | Tulsa                 | American Athletic |   3 |          62 |        6 |      68 |          0.077 |      0.820 |      0.143 |     0.485 |                 -0.251 |
|  64 | Beau Pribula             | Virginia              | ACC               |   4 |          94 |       27 |     121 |          0.110 |      0.237 |      0.138 |     0.463 |                  0.369 |
|  65 | Deshawn Purdie           | Liberty               | Conference USA    |   4 |          90 |       16 |     106 |          0.121 |      0.223 |      0.136 |     0.462 |                  0.140 |
|  66 | Jaden Craig              | TCU                   | Big 12            |   4 |         140 |       15 |     155 |          0.149 |      0.016 |      0.136 |     0.452 |                  0.041 |
|  67 | Alberto Mendoza          | Georgia Tech          | ACC               |   4 |         133 |        9 |     142 |          0.111 |      0.318 |      0.124 |     0.507 |                 -0.037 |
|  68 | Will Hammond             | Texas Tech            | Big 12            |   4 |         122 |       10 |     132 |          0.121 |      0.089 |      0.119 |     0.477 |                  0.204 |
|  69 | Jayden Mandal            | Fresno State          | Pac-12            |   4 |         108 |       19 |     127 |          0.099 |      0.219 |      0.117 |     0.496 |                  0.170 |
|  70 | Dante Moore              | Oregon                | Big Ten           |   4 |         106 |        5 |     111 |          0.134 |     -0.251 |      0.117 |     0.450 |                  0.193 |
|  71 | Jaylen Raynor            | Iowa State            | Big 12            |   4 |          96 |       27 |     123 |          0.081 |      0.216 |      0.111 |     0.463 |                 -0.049 |
|  72 | Cutter Boley             | Arizona State         | Big 12            |   3 |          87 |       16 |     103 |          0.078 |      0.287 |      0.110 |     0.466 |                  0.196 |
|  73 | Micah Alejado            | Hawai'i               | Mountain West     |   4 |         191 |        9 |     200 |          0.099 |      0.271 |      0.107 |     0.465 |                  0.114 |
|  74 | Dru Deshields            | Kent State            | Mid-American      |   4 |          87 |       25 |     112 |         -0.060 |      0.665 |      0.102 |     0.420 |                  0.129 |
|  75 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |   4 |         103 |       42 |     145 |          0.157 |     -0.038 |      0.101 |     0.428 |                  0.052 |
|  76 | Nick Minicucci           | Delaware              | Conference USA    |   4 |         108 |       12 |     120 |          0.040 |      0.634 |      0.100 |     0.458 |                  0.125 |
|  77 | Sam Leavitt              | LSU                   | SEC               |   4 |         123 |       39 |     162 |         -0.020 |      0.475 |      0.099 |     0.488 |                  0.105 |
|  78 | Luke Weaver              | San José State        | Mountain West     |   4 |         151 |       31 |     182 |          0.125 |     -0.027 |      0.099 |     0.456 |                 -0.048 |
|  79 | Gunner Stockton          | Georgia               | SEC               |   4 |          73 |       10 |      83 |          0.115 |     -0.043 |      0.096 |     0.554 |                  0.526 |
|  80 | Jackson Arnold           | UNLV                  | Mountain West     |   4 |         124 |       47 |     171 |          0.060 |      0.182 |      0.093 |     0.433 |                  0.104 |
|  81 | Jared Hollins            | South Alabama         | Sun Belt          |   3 |          65 |       13 |      78 |          0.099 |      0.057 |      0.092 |     0.423 |                  0.288 |
|  82 | Cameran Brown            | Georgia State         | Sun Belt          |   4 |         113 |       24 |     137 |          0.102 |      0.037 |      0.091 |     0.518 |                  0.332 |
|  83 | Landy Lyddy              | Southern Miss         | Sun Belt          |   4 |          69 |        6 |      75 |          0.029 |      0.792 |      0.090 |     0.427 |                  0.022 |
|  84 | Demond Williams Jr.      | Washington            | Big Ten           |   4 |         146 |       29 |     175 |          0.028 |      0.374 |      0.085 |     0.480 |                  0.078 |
|  85 | Kalieb Osborne           | UConn                 | FBS Independents  |   4 |         109 |       33 |     142 |         -0.009 |      0.394 |      0.084 |     0.444 |                  0.418 |
|  86 | Roman Gagliano           | Middle Tennessee      | Conference USA    |   4 |         135 |       13 |     148 |          0.078 |      0.142 |      0.084 |     0.426 |                  0.106 |
|  87 | Jackson Sharman          | Sacramento State      | Mid-American      |   4 |         148 |        8 |     156 |          0.127 |     -0.725 |      0.083 |     0.462 |                 -0.059 |
|  88 | Trey Owens               | Arkansas State        | Sun Belt          |   4 |         108 |       15 |     123 |         -0.005 |      0.593 |      0.068 |     0.528 |                  0.200 |
|  89 | J.J. Kohl                | Florida International | Conference USA    |   4 |         144 |       17 |     161 |          0.039 |      0.293 |      0.066 |     0.447 |                  0.130 |
|  90 | Taron Dickens            | Northern Illinois     | Mountain West     |   4 |         134 |       11 |     145 |          0.069 |      0.017 |      0.065 |     0.462 |                  0.206 |
|  91 | Nate Bennett             | Baylor                | Big 12            |   2 |          64 |        2 |      66 |         -0.014 |      2.339 |      0.058 |     0.439 |                  0.373 |
|  92 | Arch Manning             | Texas                 | SEC               |   4 |         127 |       21 |     148 |          0.100 |     -0.214 |      0.056 |     0.446 |                 -0.025 |
|  93 | Alessio Milivojevic      | Michigan State        | Big Ten           |   4 |         111 |       13 |     124 |          0.054 |      0.033 |      0.052 |     0.500 |                 -0.001 |
|  94 | KJ Jackson               | Arkansas              | SEC               |   4 |         141 |       26 |     167 |          0.073 |     -0.166 |      0.035 |     0.467 |                  0.058 |
|  95 | Jay Kastantin            | Bowling Green         | Mid-American      |   4 |          96 |       14 |     110 |          0.082 |     -0.321 |      0.031 |     0.455 |                 -0.104 |
|  96 | Lanorris Sellers         | South Carolina        | SEC               |   4 |         122 |       29 |     151 |         -0.106 |      0.607 |      0.031 |     0.477 |                 -0.177 |
|  97 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |   4 |         142 |        9 |     151 |         -0.023 |      0.841 |      0.029 |     0.470 |                  0.364 |
|  98 | Byrum Brown              | Auburn                | SEC               |   4 |         139 |       47 |     186 |         -0.043 |      0.218 |      0.023 |     0.435 |                 -0.024 |
|  99 | John Mateer              | Oklahoma              | SEC               |   4 |         117 |       33 |     150 |          0.066 |     -0.130 |      0.023 |     0.447 |                 -0.007 |
| 100 | Quinn Henicle            | Old Dominion          | Sun Belt          |   3 |          60 |       35 |      95 |         -0.230 |      0.442 |      0.017 |     0.379 |                 -0.261 |
| 101 | Nathan Hayes             | North Dakota State    | Mountain West     |   4 |          95 |       13 |     108 |          0.023 |     -0.066 |      0.012 |     0.472 |                  0.292 |
| 102 | Brock Glenn              | Western Kentucky      | Conference USA    |   4 |          60 |       26 |      86 |         -0.156 |      0.397 |      0.011 |     0.465 |                 -0.370 |
| 103 | Drake Lindsey            | Minnesota             | Big Ten           |   4 |         134 |        4 |     138 |          0.016 |     -0.290 |      0.007 |     0.449 |                  0.379 |
| 104 | Owen McCown              | UTSA                  | American Athletic |   4 |         124 |       12 |     136 |          0.022 |     -0.173 |      0.005 |     0.426 |                  0.207 |
| 105 | Camden Coleman           | James Madison         | Sun Belt          |   4 |         102 |       17 |     119 |          0.023 |     -0.115 |      0.003 |     0.437 |                  0.253 |
| 106 | Skyler Locklear          | Missouri State        | Conference USA    |   4 |          92 |       17 |     109 |          0.009 |     -0.038 |      0.001 |     0.385 |                  0.046 |
| 107 | M.Van Buren Jr.          | South Florida         | American Athletic |   4 |          97 |       19 |     116 |         -0.031 |      0.142 |     -0.003 |     0.509 |                 -0.091 |
| 108 | Julian Lewis             | Colorado              | Big 12            |   4 |         102 |        6 |     108 |         -0.014 |      0.160 |     -0.004 |     0.407 |                 -0.050 |
| 109 | Steven Angeli            | Syracuse              | ACC               |   3 |         111 |        5 |     116 |          0.001 |     -0.151 |     -0.005 |     0.414 |                  0.150 |
| 110 | Faizon Brandon           | Tennessee             | SEC               |   4 |         106 |       35 |     141 |         -0.155 |      0.426 |     -0.011 |     0.440 |                 -0.083 |
| 111 | Caden Pinnick            | Washington State      | Pac-12            |   4 |         117 |       41 |     158 |         -0.075 |      0.119 |     -0.025 |     0.449 |                 -0.091 |
| 112 | Cole Gonzales            | Charlotte             | American Athletic |   4 |         113 |       11 |     124 |          0.045 |     -0.756 |     -0.026 |     0.460 |                 -0.261 |
| 113 | Noah Kim                 | Eastern Michigan      | Mid-American      |   5 |         179 |       12 |     191 |         -0.051 |      0.192 |     -0.035 |     0.398 |                 -0.323 |
| 114 | Kenny Minchey            | Kentucky              | SEC               |   4 |         107 |        8 |     115 |          0.006 |     -0.591 |     -0.035 |     0.461 |                 -0.135 |
| 115 | Max Johnson              | Georgia Southern      | Sun Belt          |   4 |         164 |       13 |     177 |         -0.043 |      0.052 |     -0.036 |     0.367 |                  0.036 |
| 116 | D.J. Lagway              | Baylor                | Big 12            |   2 |          95 |        2 |      97 |         -0.034 |     -0.275 |     -0.039 |     0.371 |                 -0.077 |
| 117 | Brayden Roggow           | Akron                 | Mid-American      |   4 |          69 |        3 |      72 |         -0.074 |      0.749 |     -0.040 |     0.458 |                 -0.014 |
| 118 | Jaron-Keawe Sagapolutele | California            | ACC               |   4 |         141 |        4 |     145 |         -0.038 |     -0.093 |     -0.040 |     0.386 |                 -0.082 |
| 119 | Marcel Reed              | Texas A&M             | SEC               |   4 |         137 |       26 |     163 |         -0.083 |      0.175 |     -0.042 |     0.399 |                 -0.170 |
| 120 | Tyler Hughes             | Wyoming               | Mountain West     |   4 |         103 |       32 |     135 |         -0.133 |      0.224 |     -0.048 |     0.437 |                 -0.010 |
| 121 | Mason McKenzie           | Boston College        | ACC               |   4 |         117 |       63 |     180 |         -0.216 |      0.225 |     -0.062 |     0.439 |                 -0.096 |
| 122 | Will Crowder             | Troy                  | Sun Belt          |   4 |         141 |       18 |     159 |         -0.135 |      0.457 |     -0.068 |     0.403 |                  0.092 |
| 123 | Walker Eget              | Duke                  | ACC               |   4 |          93 |        3 |      96 |         -0.058 |     -0.456 |     -0.070 |     0.448 |                 -0.113 |
| 124 | Elijah Holmes            | Buffalo               | Mid-American      |   2 |          64 |        7 |      71 |         -0.080 |     -0.041 |     -0.076 |     0.380 |                 -0.078 |
| 125 | Billy Edwards            | North Carolina        | ACC               |   3 |          85 |        8 |      93 |         -0.086 |     -0.033 |     -0.081 |     0.419 |                 -0.057 |
| 126 | Keldric Luster           | Ball State            | Mid-American      |   3 |          93 |       23 |     116 |         -0.122 |     -0.016 |     -0.101 |     0.379 |                 -0.117 |
| 127 | Carter Jones             | Nevada                | Mountain West     |   3 |          74 |       20 |      94 |         -0.160 |      0.090 |     -0.107 |     0.394 |                 -0.060 |
| 128 | Jason Wright             | Buffalo               | Mid-American      |   3 |          85 |       17 |     102 |         -0.200 |      0.311 |     -0.115 |     0.353 |                 -0.163 |
| 129 | Kadin Semonza            | Tulane                | American Athletic |   4 |         105 |       13 |     118 |         -0.109 |     -0.331 |     -0.134 |     0.314 |                 -0.114 |
| 130 | Nico Iamaleava           | UCLA                  | Big Ten           |   4 |         106 |       26 |     132 |         -0.187 |      0.071 |     -0.136 |     0.379 |                 -0.052 |
| 131 | Jayden Denegal           | San Diego State       | Pac-12            |   4 |         105 |       12 |     117 |         -0.168 |      0.135 |     -0.137 |     0.368 |                 -0.221 |
| 132 | Mitch Griffis            | East Carolina         | American Athletic |   4 |          73 |       17 |      90 |         -0.219 |      0.137 |     -0.152 |     0.411 |                 -0.178 |
| 133 | Ethan Hampton            | Southern Miss         | Sun Belt          |   3 |          76 |        6 |      82 |         -0.131 |     -0.426 |     -0.153 |     0.451 |                 -0.127 |
| 134 | EJ Colson                | UTEP                  | Mountain West     |   4 |          77 |       45 |     122 |         -0.190 |     -0.103 |     -0.158 |     0.434 |                 -0.270 |
| 135 | Broc Lowry               | Western Michigan      | Mid-American      |   4 |          96 |       35 |     131 |         -0.316 |      0.085 |     -0.209 |     0.420 |                 -0.036 |
| 136 | Tait Reynolds            | Clemson               | ACC               |   4 |          95 |       29 |     124 |         -0.255 |     -0.076 |     -0.213 |     0.403 |                 -0.157 |
| 137 | Grady Brosterhous        | Utah State            | Pac-12            |   4 |         109 |       54 |     163 |         -0.190 |     -0.292 |     -0.224 |     0.344 |                 -0.310 |
