# 2026 CFB QB EPA — through Week 3

FBS offenses, games through Sep 20, 2026 (Week 0 games are folded into Week 1).
**Minimum 60 dropbacks** (~20/game), which leaves 115 QBs. Sorted by EPA/play over all dropbacks + QB rushes.

- **Dropbacks** = pass attempts + sacks. **Rushes** = designed runs + scrambles.
- **Success** = share of plays with positive EPA.
- **EPA/play (WP 10–90%)** leaves out garbage time.
- Not opponent-adjusted, so a team that has played FCS opponents looks better.
- Source: cfbfastR play-by-play (`sportsdataverse/cfbfastR-data`, `data/rds/pbp_players_pos_2026.rds`). Rebuild with `python qb_epa.py <rds> [min_dropbacks]`.

Full tables: [`qb_epa_2026.csv`](qb_epa_2026.csv), [`qb_epa_2026_nongarbage.csv`](qb_epa_2026_nongarbage.csv)

## Non-garbage time (win probability 10–90%)

Same 60-dropback pool, plus at least 40 plays in competitive game states (105 QBs).

|   # |   Overall # | QB                       | Team                  | Conf              |   Plays (WP 10–90%) |   EPA/play (WP 10–90%) |   Success (WP 10–90%) |   EPA/play (all) |
|----:|------------:|:-------------------------|:----------------------|:------------------|--------------------:|-----------------------:|----------------------:|-----------------:|
|   1 |           6 | Bear Bachmeier           | BYU                   | Big 12            |                  43 |                  0.688 |                 0.605 |            0.406 |
|   2 |           9 | Keelon Russell           | Alabama               | SEC               |                  62 |                  0.562 |                 0.565 |            0.376 |
|   3 |          44 | Katin Houser             | Illinois              | Big Ten           |                  60 |                  0.527 |                 0.583 |            0.193 |
|   4 |          10 | Tayven Jackson           | North Texas           | American Athletic |                  74 |                  0.508 |                 0.541 |            0.373 |
|   5 |           5 | Kevin Jennings           | SMU                   | ACC               |                  80 |                  0.503 |                 0.600 |            0.409 |
|   6 |          18 | Kamario Taylor           | Mississippi State     | SEC               |                  52 |                  0.503 |                 0.558 |            0.314 |
|   7 |          14 | Aaron Philo              | Florida               | SEC               |                  51 |                  0.468 |                 0.588 |            0.324 |
|   8 |          13 | Avery Johnson            | Kansas State          | Big 12            |                  60 |                  0.430 |                 0.517 |            0.327 |
|   9 |          27 | Marcus Stokes            | Memphis               | American Athletic |                  94 |                  0.421 |                 0.543 |            0.270 |
|  10 |           2 | Lincoln Kienholz         | Louisville            | ACC               |                  79 |                  0.419 |                 0.532 |            0.455 |
|  11 |          16 | Jayden Maiava            | USC                   | Big Ten           |                  72 |                  0.407 |                 0.597 |            0.320 |
|  12 |          17 | Colton Joseph            | Wisconsin             | Big Ten           |                  54 |                  0.406 |                 0.537 |            0.316 |
|  13 |          21 | JC French                | Cincinnati            | Big 12            |                  82 |                  0.400 |                 0.598 |            0.295 |
|  14 |          36 | Trinidad Chambliss       | Ole Miss              | SEC               |                  94 |                  0.386 |                 0.500 |            0.221 |
|  15 |          33 | Austin Simmons           | Missouri              | SEC               |                  52 |                  0.367 |                 0.462 |            0.234 |
|  16 |          67 | Beau Pribula             | Virginia              | ACC               |                  46 |                  0.367 |                 0.500 |            0.104 |
|  17 |          54 | Noah Fifita              | Arizona               | Big 12            |                  70 |                  0.366 |                 0.614 |            0.149 |
|  18 |          35 | William Watson III       | Massachusetts         | Mid-American      |                  40 |                  0.349 |                 0.450 |            0.225 |
|  19 |          47 | Dylan Lonergan           | Rutgers               | Big Ten           |                  43 |                  0.344 |                 0.535 |            0.178 |
|  20 |          11 | Malik Washington         | Maryland              | Big Ten           |                  62 |                  0.344 |                 0.500 |            0.372 |
|  21 |          20 | Anthony Colandrea        | Nebraska              | Big Ten           |                  55 |                  0.333 |                 0.491 |            0.296 |
|  22 |          51 | Malachi Singleton        | App State             | Sun Belt          |                  73 |                  0.326 |                 0.493 |            0.169 |
|  23 |          62 | Cameran Brown            | Georgia State         | Sun Belt          |                  67 |                  0.323 |                 0.627 |            0.120 |
|  24 |           4 | Ryan Browne              | Purdue                | Big Ten           |                  87 |                  0.305 |                 0.540 |            0.422 |
|  25 |          26 | John Alan Richter        | Toledo                | Mid-American      |                  61 |                  0.304 |                 0.492 |            0.280 |
|  26 |          43 | CJ Bailey                | NC State              | ACC               |                  43 |                  0.302 |                 0.535 |            0.194 |
|  27 |           3 | Jared Curtis             | Vanderbilt            | SEC               |                  54 |                  0.300 |                 0.481 |            0.441 |
|  28 |          22 | Bishop Davenport         | South Alabama         | Sun Belt          |                  60 |                  0.293 |                 0.483 |            0.294 |
|  29 |          90 | Nathan Hayes             | North Dakota State    | Mountain West     |                  58 |                  0.292 |                 0.483 |            0.012 |
|  30 |          42 | Bryce Underwood          | Michigan              | Big Ten           |                  85 |                  0.285 |                 0.553 |            0.197 |
|  31 |          30 | Ashton Daniels           | Florida State         | ACC               |                  89 |                  0.284 |                 0.427 |            0.246 |
|  32 |          73 | Taron Dickens            | Northern Illinois     | Mountain West     |                  43 |                  0.279 |                 0.512 |            0.090 |
|  33 |           8 | David McComb             | Miami (OH)            | Mid-American      |                  48 |                  0.277 |                 0.458 |            0.386 |
|  34 |          46 | Faizon Brandon           | Tennessee             | SEC               |                  43 |                  0.264 |                 0.442 |            0.185 |
|  35 |          25 | Giovanni Lopez           | Wake Forest           | ACC               |                  68 |                  0.264 |                 0.544 |            0.282 |
|  36 |          32 | Maddux Madsen            | Boise State           | Pac-12            |                  89 |                  0.252 |                 0.539 |            0.236 |
|  37 |           7 | Hauss Hejny              | Colorado State        | Pac-12            |                  55 |                  0.245 |                 0.491 |            0.395 |
|  38 |          69 | Jayden Mandal            | Fresno State          | Pac-12            |                  55 |                  0.229 |                 0.491 |            0.101 |
|  39 |          23 | Braden Atkinson          | Oregon State          | Pac-12            |                  87 |                  0.227 |                 0.414 |            0.290 |
|  40 |          75 | Skyler Locklear          | Missouri State        | Conference USA    |                  57 |                  0.226 |                 0.474 |            0.077 |
|  41 |          49 | Will Hammond             | Texas Tech            | Big 12            |                  71 |                  0.216 |                 0.493 |            0.176 |
|  42 |          31 | Conner Weigman           | Houston               | Big 12            |                  74 |                  0.215 |                 0.486 |            0.243 |
|  43 |          59 | Isaiah Marshall          | Kansas                | Big 12            |                  76 |                  0.205 |                 0.382 |            0.137 |
|  44 |          55 | Caden Creel              | Jacksonville State    | Conference USA    |                  89 |                  0.200 |                 0.494 |            0.149 |
|  45 |          65 | Cutter Boley             | Arizona State         | Big 12            |                  61 |                  0.196 |                 0.459 |            0.110 |
|  46 |          56 | Demond Williams Jr.      | Washington            | Big Ten           |                 100 |                  0.190 |                 0.530 |            0.140 |
|  47 |          68 | Dante Moore              | Oregon                | Big Ten           |                  73 |                  0.189 |                 0.411 |            0.103 |
|  48 |         100 | Will Crowder             | Troy                  | Sun Belt          |                  71 |                  0.187 |                 0.451 |           -0.028 |
|  49 |          64 | Nick Minicucci           | Delaware              | Conference USA    |                  76 |                  0.181 |                 0.461 |            0.111 |
|  50 |          37 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |                  45 |                  0.177 |                 0.511 |            0.221 |
|  51 |          15 | C.J. Carr                | Notre Dame            | FBS Independents  |                  48 |                  0.166 |                 0.417 |            0.321 |
|  52 |          60 | Micah Alejado            | Hawai'i               | Mountain West     |                 136 |                  0.157 |                 0.463 |            0.133 |
|  53 |          94 | Steven Angeli            | Syracuse              | ACC               |                  81 |                  0.150 |                 0.420 |           -0.005 |
|  54 |          28 | Brad Jackson             | Texas State           | Pac-12            |                  76 |                  0.115 |                 0.474 |            0.261 |
|  55 |          38 | Ryder Burton             | UAB                   | American Athletic |                  67 |                  0.107 |                 0.433 |            0.217 |
|  56 |          52 | Mason Heintschel         | Pittsburgh            | ACC               |                  66 |                  0.102 |                 0.470 |            0.162 |
|  57 |          41 | Trey Hedden              | New Mexico State      | Conference USA    |                  73 |                  0.101 |                 0.411 |            0.203 |
|  58 |          74 | Roman Gagliano           | Middle Tennessee      | Conference USA    |                  93 |                  0.099 |                 0.441 |            0.085 |
|  59 |          39 | Caden Veltkamp           | Florida Atlantic      | American Athletic |                  81 |                  0.092 |                 0.469 |            0.217 |
|  60 |          96 | Kadin Semonza            | Tulane                | American Athletic |                  60 |                  0.084 |                 0.367 |           -0.006 |
|  61 |         105 | Trey Owens               | Arkansas State        | Sun Belt          |                  67 |                  0.075 |                 0.493 |           -0.080 |
|  62 |          29 | Cibastian Broughton      | Akron                 | Mid-American      |                  41 |                  0.070 |                 0.463 |            0.255 |
|  63 |          61 | Hank Brown               | Iowa                  | Big Ten           |                  46 |                  0.066 |                 0.478 |            0.128 |
|  64 |          76 | Alessio Milivojevic      | Michigan State        | Big Ten           |                  78 |                  0.043 |                 0.474 |            0.077 |
|  65 |          24 | Jay Kastantin            | Bowling Green         | Mid-American      |                  41 |                  0.042 |                 0.390 |            0.288 |
|  66 |          79 | J.J. Kohl                | Florida International | Conference USA    |                 108 |                  0.042 |                 0.435 |            0.064 |
|  67 |          63 | Arch Manning             | Texas                 | SEC               |                  58 |                  0.037 |                 0.483 |            0.117 |
|  68 |          57 | Jaden Craig              | TCU                   | Big 12            |                  78 |                  0.035 |                 0.423 |            0.140 |
|  69 |          71 | Sam Leavitt              | LSU                   | SEC               |                  69 |                  0.024 |                 0.507 |            0.095 |
|  70 |          85 | Nico Iamaleava           | UCLA                  | Big Ten           |                  94 |                  0.021 |                 0.415 |            0.026 |
|  71 |          82 | Deshawn Purdie           | Liberty               | Conference USA    |                  67 |                  0.020 |                 0.418 |            0.052 |
|  72 |          81 | Jaron-Keawe Sagapolutele | California            | ACC               |                  82 |                  0.019 |                 0.402 |            0.060 |
|  73 |          80 | Byrum Brown              | Auburn                | SEC               |                  81 |                  0.002 |                 0.420 |            0.062 |
|  74 |         107 | Broc Lowry               | Western Michigan      | Mid-American      |                  79 |                 -0.005 |                 0.443 |           -0.137 |
|  75 |          40 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |                  66 |                 -0.009 |                 0.455 |            0.207 |
|  76 |         102 | Billy Edwards            | North Carolina        | ACC               |                  78 |                 -0.011 |                 0.436 |           -0.043 |
|  77 |          66 | Landyn Locke             | Sam Houston           | Conference USA    |                 102 |                 -0.012 |                 0.441 |            0.108 |
|  78 |          88 | Davis Warren             | Stanford              | ACC               |                  62 |                 -0.014 |                 0.419 |            0.018 |
|  79 |         112 | Owen McCown              | UTSA                  | American Athletic |                  69 |                 -0.015 |                 0.406 |           -0.164 |
|  80 |          87 | Julian Lewis             | Colorado              | Big 12            |                  50 |                 -0.019 |                 0.420 |            0.024 |
|  81 |          84 | Drew Mestemaker          | Oklahoma State        | Big 12            |                  95 |                 -0.025 |                 0.474 |            0.027 |
|  82 |          93 | Caden Pinnick            | Washington State      | Pac-12            |                  72 |                 -0.026 |                 0.472 |           -0.004 |
|  83 |          86 | Jackson Arnold           | UNLV                  | Mountain West     |                 102 |                 -0.029 |                 0.392 |            0.024 |
|  84 |          70 | Luke Weaver              | San José State        | Mountain West     |                 138 |                 -0.048 |                 0.442 |            0.099 |
|  85 |          95 | John Mateer              | Oklahoma              | SEC               |                  75 |                 -0.051 |                 0.440 |           -0.006 |
|  86 |         101 | Mason McKenzie           | Boston College        | ACC               |                  70 |                 -0.069 |                 0.414 |           -0.030 |
|  87 |         103 | Walker Eget              | Duke                  | ACC               |                  63 |                 -0.070 |                 0.492 |           -0.055 |
|  88 |         109 | Tait Reynolds            | Clemson               | ACC               |                  78 |                 -0.072 |                 0.449 |           -0.147 |
|  89 |         104 | Elijah Holmes            | Buffalo               | Mid-American      |                  68 |                 -0.078 |                 0.382 |           -0.076 |
|  90 |          99 | Kenny Minchey            | Kentucky              | SEC               |                  53 |                 -0.088 |                 0.472 |           -0.017 |
|  91 |         108 | Tyler Hughes             | Wyoming               | Mountain West     |                  72 |                 -0.091 |                 0.444 |           -0.138 |
|  92 |          78 | Marcel Reed              | Texas A&M             | SEC               |                  74 |                 -0.097 |                 0.419 |            0.064 |
|  93 |          83 | KJ Jackson               | Arkansas              | SEC               |                  51 |                 -0.102 |                 0.471 |            0.049 |
|  94 |         106 | Keldric Luster           | Ball State            | Mid-American      |                  46 |                 -0.117 |                 0.413 |           -0.137 |
|  95 |          89 | Dru Deshields            | Kent State            | Mid-American      |                  46 |                 -0.120 |                 0.391 |            0.013 |
|  96 |         115 | Max Johnson              | Georgia Southern      | Sun Belt          |                  81 |                 -0.126 |                 0.321 |           -0.319 |
|  97 |          72 | Alberto Mendoza          | Georgia Tech          | ACC               |                  64 |                 -0.129 |                 0.453 |            0.095 |
|  98 |         110 | Ethan Hampton            | Southern Miss         | Sun Belt          |                  42 |                 -0.132 |                 0.500 |           -0.155 |
|  99 |          48 | Austin Carlisle          | UL Monroe             | Sun Belt          |                  54 |                 -0.146 |                 0.481 |            0.177 |
| 100 |          77 | Cole Gonzales            | Charlotte             | American Athletic |                  63 |                 -0.167 |                 0.444 |            0.072 |
| 101 |          92 | Lanorris Sellers         | South Carolina        | SEC               |                  53 |                 -0.168 |                 0.472 |            0.006 |
| 102 |         111 | Mitch Griffis            | East Carolina         | American Athletic |                  52 |                 -0.170 |                 0.385 |           -0.163 |
| 103 |         113 | Jayden Denegal           | San Diego State       | Pac-12            |                  42 |                 -0.301 |                 0.310 |           -0.193 |
| 104 |          97 | Noah Kim                 | Eastern Michigan      | Mid-American      |                  95 |                 -0.332 |                 0.326 |           -0.012 |
| 105 |         114 | Grady Brosterhous        | Utah State            | Pac-12            |                  48 |                 -0.555 |                 0.208 |           -0.267 |

## All plays

|   # | QB                       | Team                  | Conf              |   G |   Dropbacks |   Rushes |   Plays |   EPA/dropback |   EPA/rush |   EPA/play |   Success |   EPA/play (WP 10–90%) |
|----:|:-------------------------|:----------------------|:------------------|----:|------------:|---------:|--------:|---------------:|-----------:|-----------:|----------:|-----------------------:|
|   1 | Rocco Becht              | Penn State            | Big Ten           |   3 |          66 |        4 |      70 |          0.600 |     -1.794 |      0.463 |     0.557 |                  0.694 |
|   2 | Lincoln Kienholz         | Louisville            | ACC               |   3 |          76 |       29 |     105 |          0.512 |      0.307 |      0.455 |     0.543 |                  0.419 |
|   3 | Jared Curtis             | Vanderbilt            | SEC               |   3 |          67 |       18 |      85 |          0.330 |      0.853 |      0.441 |     0.529 |                  0.300 |
|   4 | Ryan Browne              | Purdue                | Big Ten           |   3 |         100 |        6 |     106 |          0.447 |     -0.008 |      0.422 |     0.594 |                  0.305 |
|   5 | Kevin Jennings           | SMU                   | ACC               |   3 |          91 |       13 |     104 |          0.492 |     -0.174 |      0.409 |     0.558 |                  0.503 |
|   6 | Bear Bachmeier           | BYU                   | Big 12            |   3 |          64 |       10 |      74 |          0.351 |      0.761 |      0.406 |     0.581 |                  0.688 |
|   7 | Hauss Hejny              | Colorado State        | Pac-12            |   3 |          74 |       11 |      85 |          0.379 |      0.506 |      0.395 |     0.518 |                  0.245 |
|   8 | David McComb             | Miami (OH)            | Mid-American      |   3 |          79 |        9 |      88 |          0.419 |      0.093 |      0.386 |     0.489 |                  0.277 |
|   9 | Keelon Russell           | Alabama               | SEC               |   3 |          89 |       16 |     105 |          0.281 |      0.901 |      0.376 |     0.543 |                  0.562 |
|  10 | Tayven Jackson           | North Texas           | American Athletic |   3 |         111 |       13 |     124 |          0.360 |      0.487 |      0.373 |     0.540 |                  0.508 |
|  11 | Malik Washington         | Maryland              | Big Ten           |   3 |         119 |        7 |     126 |          0.378 |      0.266 |      0.372 |     0.532 |                  0.344 |
|  12 | Darian Mensah            | Miami                 | ACC               |   3 |          79 |        4 |      83 |          0.344 |      0.297 |      0.342 |     0.554 |                  0.554 |
|  13 | Avery Johnson            | Kansas State          | Big 12            |   3 |          82 |       24 |     106 |          0.248 |      0.599 |      0.327 |     0.547 |                  0.430 |
|  14 | Aaron Philo              | Florida               | SEC               |   3 |          66 |       15 |      81 |          0.367 |      0.135 |      0.324 |     0.543 |                  0.468 |
|  15 | C.J. Carr                | Notre Dame            | FBS Independents  |   3 |          75 |        3 |      78 |          0.336 |     -0.055 |      0.321 |     0.487 |                  0.166 |
|  16 | Jayden Maiava            | USC                   | Big Ten           |   4 |         118 |        6 |     124 |          0.376 |     -0.795 |      0.320 |     0.621 |                  0.407 |
|  17 | Colton Joseph            | Wisconsin             | Big Ten           |   3 |          86 |       22 |     108 |          0.314 |      0.323 |      0.316 |     0.519 |                  0.406 |
|  18 | Kamario Taylor           | Mississippi State     | SEC               |   3 |          86 |       22 |     108 |          0.261 |      0.519 |      0.314 |     0.546 |                  0.503 |
|  19 | Julian Sayin             | Ohio State            | Big Ten           |   3 |          84 |        4 |      88 |          0.267 |      0.908 |      0.297 |     0.545 |                  0.499 |
|  20 | Anthony Colandrea        | Nebraska              | Big Ten           |   3 |          80 |       13 |      93 |          0.276 |      0.421 |      0.296 |     0.505 |                  0.333 |
|  21 | JC French                | Cincinnati            | Big 12            |   3 |          85 |       27 |     112 |          0.259 |      0.408 |      0.295 |     0.580 |                  0.400 |
|  22 | Bishop Davenport         | South Alabama         | Sun Belt          |   2 |          61 |       16 |      77 |          0.291 |      0.303 |      0.294 |     0.468 |                  0.293 |
|  23 | Braden Atkinson          | Oregon State          | Pac-12            |   3 |         135 |        4 |     139 |          0.297 |      0.062 |      0.290 |     0.446 |                  0.227 |
|  24 | Jay Kastantin            | Bowling Green         | Mid-American      |   3 |          64 |       10 |      74 |          0.393 |     -0.382 |      0.288 |     0.514 |                  0.042 |
|  25 | Giovanni Lopez           | Wake Forest           | ACC               |   3 |         104 |       19 |     123 |          0.257 |      0.413 |      0.282 |     0.528 |                  0.264 |
|  26 | John Alan Richter        | Toledo                | Mid-American      |   3 |          98 |        3 |     101 |          0.339 |     -1.670 |      0.280 |     0.485 |                  0.304 |
|  27 | Marcus Stokes            | Memphis               | American Athletic |   4 |         104 |       22 |     126 |          0.319 |      0.036 |      0.270 |     0.492 |                  0.421 |
|  28 | Brad Jackson             | Texas State           | Pac-12            |   3 |          75 |       23 |      98 |          0.348 |     -0.022 |      0.261 |     0.510 |                  0.115 |
|  29 | Cibastian Broughton      | Akron                 | Mid-American      |   3 |          71 |       22 |      93 |          0.135 |      0.642 |      0.255 |     0.505 |                  0.070 |
|  30 | Ashton Daniels           | Florida State         | ACC               |   3 |          86 |       28 |     114 |          0.210 |      0.355 |      0.246 |     0.430 |                  0.284 |
|  31 | Conner Weigman           | Houston               | Big 12            |   3 |          84 |       19 |     103 |          0.250 |      0.211 |      0.243 |     0.524 |                  0.215 |
|  32 | Maddux Madsen            | Boise State           | Pac-12            |   3 |          93 |        7 |     100 |          0.178 |      1.012 |      0.236 |     0.530 |                  0.252 |
|  33 | Austin Simmons           | Missouri              | SEC               |   3 |          68 |        4 |      72 |          0.289 |     -0.696 |      0.234 |     0.431 |                  0.367 |
|  34 | Rickie Collins           | Kennesaw State        | Conference USA    |   3 |          95 |       26 |     121 |          0.167 |      0.449 |      0.228 |     0.529 |                 -0.108 |
|  35 | William Watson III       | Massachusetts         | Mid-American      |   3 |          60 |       14 |      74 |          0.183 |      0.406 |      0.225 |     0.459 |                  0.349 |
|  36 | Trinidad Chambliss       | Ole Miss              | SEC               |   3 |         115 |       16 |     131 |          0.185 |      0.484 |      0.221 |     0.481 |                  0.386 |
|  37 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |   3 |          66 |       39 |     105 |         -0.011 |      0.614 |      0.221 |     0.486 |                  0.177 |
|  38 | Ryder Burton             | UAB                   | American Athletic |   3 |          79 |       20 |      99 |          0.178 |      0.372 |      0.217 |     0.455 |                  0.107 |
|  39 | Caden Veltkamp           | Florida Atlantic      | American Athletic |   3 |         129 |        7 |     136 |          0.198 |      0.561 |      0.217 |     0.522 |                  0.092 |
|  40 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |   3 |          99 |       15 |     114 |          0.108 |      0.863 |      0.207 |     0.447 |                 -0.009 |
|  41 | Trey Hedden              | New Mexico State      | Conference USA    |   3 |         102 |        5 |     107 |          0.199 |      0.276 |      0.203 |     0.430 |                  0.101 |
|  42 | Bryce Underwood          | Michigan              | Big Ten           |   3 |          70 |       27 |      97 |          0.178 |      0.247 |      0.197 |     0.505 |                  0.285 |
|  43 | CJ Bailey                | NC State              | ACC               |   3 |          82 |       19 |     101 |          0.205 |      0.148 |      0.194 |     0.475 |                  0.302 |
|  44 | Katin Houser             | Illinois              | Big Ten           |   3 |          84 |        8 |      92 |          0.181 |      0.318 |      0.193 |     0.533 |                  0.527 |
|  45 | Devon Dampier            | Utah                  | Big 12            |   3 |          76 |       23 |      99 |          0.255 |     -0.026 |      0.190 |     0.576 |                  0.308 |
|  46 | Faizon Brandon           | Tennessee             | SEC               |   3 |          67 |       21 |      88 |          0.035 |      0.664 |      0.185 |     0.489 |                  0.264 |
|  47 | Dylan Lonergan           | Rutgers               | Big Ten           |   2 |          69 |        8 |      77 |          0.224 |     -0.213 |      0.178 |     0.455 |                  0.344 |
|  48 | Austin Carlisle          | UL Monroe             | Sun Belt          |   3 |          60 |       29 |      89 |         -0.087 |      0.724 |      0.177 |     0.528 |                 -0.146 |
|  49 | Will Hammond             | Texas Tech            | Big 12            |   3 |          93 |        8 |     101 |          0.215 |     -0.273 |      0.176 |     0.446 |                  0.216 |
|  50 | Kalieb Osborne           | UConn                 | FBS Independents  |   3 |          76 |       22 |      98 |          0.091 |      0.444 |      0.171 |     0.490 |                  0.602 |
|  51 | Malachi Singleton        | App State             | Sun Belt          |   3 |          96 |       18 |     114 |          0.266 |     -0.345 |      0.169 |     0.509 |                  0.326 |
|  52 | Mason Heintschel         | Pittsburgh            | ACC               |   3 |          98 |       19 |     117 |          0.204 |     -0.056 |      0.162 |     0.462 |                  0.102 |
|  53 | Jackson Sharman          | Sacramento State      | Mid-American      |   3 |         101 |        5 |     106 |          0.227 |     -1.192 |      0.160 |     0.462 |                 -0.257 |
|  54 | Noah Fifita              | Arizona               | Big 12            |   3 |         102 |       14 |     116 |          0.085 |      0.616 |      0.149 |     0.552 |                  0.366 |
|  55 | Caden Creel              | Jacksonville State    | Conference USA    |   4 |         103 |       50 |     153 |          0.152 |      0.143 |      0.149 |     0.503 |                  0.200 |
|  56 | Demond Williams Jr.      | Washington            | Big Ten           |   3 |         111 |       20 |     131 |          0.088 |      0.429 |      0.140 |     0.504 |                  0.190 |
|  57 | Jaden Craig              | TCU                   | Big 12            |   3 |          96 |       11 |     107 |          0.189 |     -0.288 |      0.140 |     0.449 |                  0.035 |
|  58 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |   3 |         105 |        8 |     113 |          0.077 |      0.938 |      0.138 |     0.487 |                  1.024 |
|  59 | Isaiah Marshall          | Kansas                | Big 12            |   3 |          87 |       32 |     119 |          0.117 |      0.192 |      0.137 |     0.395 |                  0.205 |
|  60 | Micah Alejado            | Hawai'i               | Mountain West     |   3 |         144 |        7 |     151 |          0.130 |      0.176 |      0.133 |     0.464 |                  0.157 |
|  61 | Hank Brown               | Iowa                  | Big Ten           |   3 |          62 |       10 |      72 |          0.198 |     -0.305 |      0.128 |     0.486 |                  0.066 |
|  62 | Cameran Brown            | Georgia State         | Sun Belt          |   3 |          92 |       22 |     114 |          0.155 |     -0.023 |      0.120 |     0.526 |                  0.323 |
|  63 | Arch Manning             | Texas                 | SEC               |   3 |         104 |       16 |     120 |          0.157 |     -0.144 |      0.117 |     0.467 |                  0.037 |
|  64 | Nick Minicucci           | Delaware              | Conference USA    |   3 |         100 |       11 |     111 |          0.046 |      0.701 |      0.111 |     0.468 |                  0.181 |
|  65 | Cutter Boley             | Arizona State         | Big 12            |   3 |          87 |       16 |     103 |          0.078 |      0.287 |      0.110 |     0.466 |                  0.196 |
|  66 | Landyn Locke             | Sam Houston           | Conference USA    |   3 |         117 |        9 |     126 |          0.145 |     -0.376 |      0.108 |     0.468 |                 -0.012 |
|  67 | Beau Pribula             | Virginia              | ACC               |   3 |          63 |       20 |      83 |          0.039 |      0.309 |      0.104 |     0.446 |                  0.367 |
|  68 | Dante Moore              | Oregon                | Big Ten           |   3 |          96 |        3 |      99 |          0.125 |     -0.601 |      0.103 |     0.444 |                  0.189 |
|  69 | Jayden Mandal            | Fresno State          | Pac-12            |   3 |          75 |       15 |      90 |          0.120 |      0.006 |      0.101 |     0.489 |                  0.229 |
|  70 | Luke Weaver              | San José State        | Mountain West     |   4 |         151 |       31 |     182 |          0.125 |     -0.027 |      0.099 |     0.456 |                 -0.048 |
|  71 | Sam Leavitt              | LSU                   | SEC               |   3 |         100 |       33 |     133 |         -0.069 |      0.591 |      0.095 |     0.496 |                  0.024 |
|  72 | Alberto Mendoza          | Georgia Tech          | ACC               |   3 |          92 |        3 |      95 |          0.112 |     -0.444 |      0.095 |     0.526 |                 -0.129 |
|  73 | Taron Dickens            | Northern Illinois     | Mountain West     |   3 |          86 |        9 |      95 |          0.114 |     -0.142 |      0.090 |     0.442 |                  0.279 |
|  74 | Roman Gagliano           | Middle Tennessee      | Conference USA    |   3 |         104 |       12 |     116 |          0.071 |      0.207 |      0.085 |     0.431 |                  0.099 |
|  75 | Skyler Locklear          | Missouri State        | Conference USA    |   3 |          67 |       13 |      80 |          0.083 |      0.049 |      0.077 |     0.412 |                  0.226 |
|  76 | Alessio Milivojevic      | Michigan State        | Big Ten           |   3 |          80 |       12 |      92 |          0.103 |     -0.098 |      0.077 |     0.489 |                  0.043 |
|  77 | Cole Gonzales            | Charlotte             | American Athletic |   3 |          96 |        9 |     105 |          0.143 |     -0.680 |      0.072 |     0.486 |                 -0.167 |
|  78 | Marcel Reed              | Texas A&M             | SEC               |   3 |         108 |       20 |     128 |          0.063 |      0.068 |      0.064 |     0.438 |                 -0.097 |
|  79 | J.J. Kohl                | Florida International | Conference USA    |   3 |         132 |       13 |     145 |          0.041 |      0.294 |      0.064 |     0.448 |                  0.042 |
|  80 | Byrum Brown              | Auburn                | SEC               |   3 |         111 |       37 |     148 |          0.001 |      0.244 |      0.062 |     0.446 |                  0.002 |
|  81 | Jaron-Keawe Sagapolutele | California            | ACC               |   3 |         110 |        3 |     113 |          0.064 |     -0.089 |      0.060 |     0.398 |                  0.019 |
|  82 | Deshawn Purdie           | Liberty               | Conference USA    |   3 |          71 |       11 |      82 |          0.055 |      0.029 |      0.052 |     0.427 |                  0.020 |
|  83 | KJ Jackson               | Arkansas              | SEC               |   3 |         102 |       16 |     118 |          0.077 |     -0.134 |      0.049 |     0.500 |                 -0.102 |
|  84 | Drew Mestemaker          | Oklahoma State        | Big 12            |   3 |         119 |        9 |     128 |         -0.042 |      0.936 |      0.027 |     0.492 |                 -0.025 |
|  85 | Nico Iamaleava           | UCLA                  | Big Ten           |   3 |          81 |       21 |     102 |         -0.033 |      0.252 |      0.026 |     0.422 |                  0.021 |
|  86 | Jackson Arnold           | UNLV                  | Mountain West     |   3 |          95 |       39 |     134 |         -0.070 |      0.255 |      0.024 |     0.410 |                 -0.029 |
|  87 | Julian Lewis             | Colorado              | Big 12            |   3 |          83 |        5 |      88 |          0.014 |      0.187 |      0.024 |     0.420 |                 -0.019 |
|  88 | Davis Warren             | Stanford              | ACC               |   3 |         113 |        4 |     117 |          0.021 |     -0.071 |      0.018 |     0.410 |                 -0.014 |
|  89 | Dru Deshields            | Kent State            | Mid-American      |   3 |          61 |       13 |      74 |         -0.157 |      0.814 |      0.013 |     0.405 |                 -0.120 |
|  90 | Nathan Hayes             | North Dakota State    | Mountain West     |   4 |          95 |       13 |     108 |          0.023 |     -0.066 |      0.012 |     0.472 |                  0.292 |
|  91 | Nate Bennett             | Baylor                | Big 12            |   2 |          63 |        2 |      65 |         -0.066 |      2.339 |      0.008 |     0.431 |                  0.373 |
|  92 | Lanorris Sellers         | South Carolina        | SEC               |   3 |          91 |       17 |     108 |         -0.095 |      0.548 |      0.006 |     0.481 |                 -0.168 |
|  93 | Caden Pinnick            | Washington State      | Pac-12            |   3 |          74 |       30 |     104 |         -0.057 |      0.126 |     -0.004 |     0.471 |                 -0.026 |
|  94 | Steven Angeli            | Syracuse              | ACC               |   3 |         111 |        5 |     116 |          0.001 |     -0.151 |     -0.005 |     0.414 |                  0.150 |
|  95 | John Mateer              | Oklahoma              | SEC               |   3 |          81 |       22 |     103 |          0.005 |     -0.048 |     -0.006 |     0.437 |                 -0.051 |
|  96 | Kadin Semonza            | Tulane                | American Athletic |   3 |          78 |       11 |      89 |          0.005 |     -0.085 |     -0.006 |     0.315 |                  0.084 |
|  97 | Noah Kim                 | Eastern Michigan      | Mid-American      |   4 |         140 |       10 |     150 |         -0.048 |      0.491 |     -0.012 |     0.413 |                 -0.332 |
|  98 | Drake Lindsey            | Minnesota             | Big Ten           |   3 |         105 |        4 |     109 |         -0.002 |     -0.290 |     -0.013 |     0.450 |                  0.482 |
|  99 | Kenny Minchey            | Kentucky              | SEC               |   3 |          80 |        8 |      88 |          0.041 |     -0.591 |     -0.017 |     0.455 |                 -0.088 |
| 100 | Will Crowder             | Troy                  | Sun Belt          |   3 |          91 |       12 |     103 |         -0.069 |      0.280 |     -0.028 |     0.408 |                  0.187 |
| 101 | Mason McKenzie           | Boston College        | ACC               |   3 |          91 |       41 |     132 |         -0.148 |      0.233 |     -0.030 |     0.439 |                 -0.069 |
| 102 | Billy Edwards            | North Carolina        | ACC               |   3 |          84 |        7 |      91 |         -0.064 |      0.215 |     -0.043 |     0.429 |                 -0.011 |
| 103 | Walker Eget              | Duke                  | ACC               |   3 |          71 |        3 |      74 |         -0.038 |     -0.456 |     -0.055 |     0.473 |                 -0.070 |
| 104 | Elijah Holmes            | Buffalo               | Mid-American      |   2 |          64 |        7 |      71 |         -0.080 |     -0.041 |     -0.076 |     0.380 |                 -0.078 |
| 105 | Trey Owens               | Arkansas State        | Sun Belt          |   3 |          77 |       11 |      88 |         -0.179 |      0.614 |     -0.080 |     0.489 |                  0.075 |
| 106 | Keldric Luster           | Ball State            | Mid-American      |   3 |          93 |       22 |     115 |         -0.122 |     -0.198 |     -0.137 |     0.374 |                 -0.117 |
| 107 | Broc Lowry               | Western Michigan      | Mid-American      |   3 |          66 |       29 |      95 |         -0.280 |      0.188 |     -0.137 |     0.421 |                 -0.005 |
| 108 | Tyler Hughes             | Wyoming               | Mountain West     |   3 |          77 |       26 |     103 |         -0.292 |      0.319 |     -0.138 |     0.427 |                 -0.091 |
| 109 | Tait Reynolds            | Clemson               | ACC               |   3 |          72 |       21 |      93 |         -0.198 |      0.025 |     -0.147 |     0.409 |                 -0.072 |
| 110 | Ethan Hampton            | Southern Miss         | Sun Belt          |   3 |          76 |        5 |      81 |         -0.131 |     -0.525 |     -0.155 |     0.444 |                 -0.132 |
| 111 | Mitch Griffis            | East Carolina         | American Athletic |   3 |          71 |       16 |      87 |         -0.209 |      0.042 |     -0.163 |     0.414 |                 -0.170 |
| 112 | Owen McCown              | UTSA                  | American Athletic |   3 |          93 |        9 |     102 |         -0.170 |     -0.102 |     -0.164 |     0.392 |                 -0.015 |
| 113 | Jayden Denegal           | San Diego State       | Pac-12            |   3 |          71 |        5 |      76 |         -0.243 |      0.517 |     -0.193 |     0.355 |                 -0.301 |
| 114 | Grady Brosterhous        | Utah State            | Pac-12            |   3 |          79 |       38 |     117 |         -0.221 |     -0.363 |     -0.267 |     0.325 |                 -0.555 |
| 115 | Max Johnson              | Georgia Southern      | Sun Belt          |   3 |         124 |        9 |     133 |         -0.339 |     -0.046 |     -0.319 |     0.308 |                 -0.126 |
