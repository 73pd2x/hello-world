# 2026 CFB QB EPA — through Week 10

FBS offenses, games through Nov 7, 2026 (Week 0 games are folded into Week 1).
**Minimum 60 dropbacks**, which leaves 187 QBs. Sorted by EPA/play over all dropbacks + QB rushes.

- **Dropbacks** = pass attempts + sacks. **Rushes** = designed runs + scrambles.
- **Success** = share of plays with positive EPA.
- **EPA/play (WP 10–90%)** leaves out garbage time.
- Not opponent-adjusted, so a team that has played FCS opponents looks better.
- Source: cfbfastR play-by-play (`sportsdataverse/cfbfastR-data`, `data/rds/pbp_players_pos_2026.rds`). Rebuild with `python qb_epa.py <rds> [min_dropbacks]` then `python make_readme.py <week> "<through date>"`.

Full tables: [`qb_epa_2026.csv`](qb_epa_2026.csv), [`qb_epa_2026_nongarbage.csv`](qb_epa_2026_nongarbage.csv)

## Non-garbage time (win probability 10–90%)

Same 60-dropback pool, plus at least 40 plays in competitive game states (180 QBs).

|   # |   Overall # | QB                       | Team                  | Conf              |   Plays (WP 10–90%) |   EPA/play (WP 10–90%) |   Success (WP 10–90%) |   EPA/play (all) |
|----:|------------:|:-------------------------|:----------------------|:------------------|--------------------:|-----------------------:|----------------------:|-----------------:|
|   1 |           1 | David McComb             | Miami (OH)            | Mid-American      |                  79 |                  0.611 |                 0.544 |            0.570 |
|   2 |           5 | Giovanni Lopez           | Wake Forest           | ACC               |                 170 |                  0.553 |                 0.565 |            0.429 |
|   3 |           2 | Tayven Jackson           | North Texas           | American Athletic |                 238 |                  0.513 |                 0.571 |            0.468 |
|   4 |           6 | Julian Sayin             | Ohio State            | Big Ten           |                 143 |                  0.504 |                 0.566 |            0.416 |
|   5 |           8 | JC Evans                 | James Madison         | Sun Belt          |                  88 |                  0.494 |                 0.557 |            0.398 |
|   6 |           3 | Darian Mensah            | Miami                 | ACC               |                 182 |                  0.457 |                 0.555 |            0.460 |
|   7 |          11 | Michael Hawkins Jr.      | West Virginia         | Big 12            |                 278 |                  0.438 |                 0.475 |            0.345 |
|   8 |          17 | Bishop Davenport         | South Alabama         | Sun Belt          |                  94 |                  0.392 |                 0.532 |            0.330 |
|   9 |           4 | Hauss Hejny              | Colorado State        | Pac-12            |                 112 |                  0.382 |                 0.554 |            0.444 |
|  10 |           9 | Thomas Castellanos       | Texas Tech            | Big 12            |                  93 |                  0.380 |                 0.516 |            0.360 |
|  11 |          23 | Marcus Stokes            | Memphis               | American Athletic |                 236 |                  0.375 |                 0.525 |            0.291 |
|  12 |          20 | Jayden Maiava            | USC                   | Big Ten           |                 242 |                  0.368 |                 0.545 |            0.325 |
|  13 |           7 | Jackson Gutierrez        | Navy                  | American Athletic |                 207 |                  0.365 |                 0.531 |            0.408 |
|  14 |          13 | Lincoln Kienholz         | Louisville            | ACC               |                 267 |                  0.364 |                 0.536 |            0.339 |
|  15 |          10 | Caden Veltkamp           | Florida Atlantic      | American Athletic |                 244 |                  0.352 |                 0.529 |            0.350 |
|  16 |          29 | Cameran Brown            | Georgia State         | Sun Belt          |                 118 |                  0.340 |                 0.568 |            0.270 |
|  17 |          15 | Avery Johnson            | Kansas State          | Big 12            |                 155 |                  0.339 |                 0.510 |            0.334 |
|  18 |          12 | Aidan Chiles             | Northwestern          | Big Ten           |                 196 |                  0.336 |                 0.515 |            0.344 |
|  19 |          14 | Kevin Jennings           | SMU                   | ACC               |                 283 |                  0.329 |                 0.551 |            0.337 |
|  20 |          34 | Dylan Lonergan           | Rutgers               | Big Ten           |                  96 |                  0.326 |                 0.521 |            0.249 |
|  21 |          37 | Gunner Stockton          | Georgia               | SEC               |                 148 |                  0.323 |                 0.541 |            0.239 |
|  22 |          24 | Keelon Russell           | Alabama               | SEC               |                 237 |                  0.318 |                 0.498 |            0.291 |
|  23 |          18 | C.J. Carr                | Notre Dame            | FBS Independents  |                 203 |                  0.315 |                 0.512 |            0.329 |
|  24 |          19 | Conner Weigman           | Houston               | Big 12            |                 261 |                  0.312 |                 0.544 |            0.329 |
|  25 |          21 | Drew Mestemaker          | Oklahoma State        | Big 12            |                 263 |                  0.305 |                 0.536 |            0.316 |
|  26 |          36 | Devon Dampier            | Utah                  | Big 12            |                 224 |                  0.301 |                 0.545 |            0.240 |
|  27 |          22 | Mason Heintschel         | Pittsburgh            | ACC               |                  89 |                  0.295 |                 0.427 |            0.299 |
|  28 |          40 | John Alan Richter        | Toledo                | Mid-American      |                 212 |                  0.293 |                 0.476 |            0.229 |
|  29 |          33 | Ajani Sheppard           | Temple                | American Athletic |                 179 |                  0.292 |                 0.475 |            0.250 |
|  30 |          78 | Matt Vezza               | Ohio                  | Mid-American      |                  83 |                  0.288 |                 0.542 |            0.139 |
|  31 |          39 | Katin Houser             | Illinois              | Big Ten           |                 212 |                  0.276 |                 0.519 |            0.231 |
|  32 |          68 | Ty Dieffenbach           | UCLA                  | Big Ten           |                 104 |                  0.275 |                 0.413 |            0.151 |
|  33 |          25 | Maddux Madsen            | Boise State           | Pac-12            |                 210 |                  0.271 |                 0.510 |            0.287 |
|  34 |          26 | Noah Fifita              | Arizona               | Big 12            |                 263 |                  0.271 |                 0.510 |            0.278 |
|  35 |          53 | William Watson III       | Massachusetts         | Mid-American      |                 125 |                  0.265 |                 0.456 |            0.200 |
|  36 |          30 | Aaron Philo              | Florida               | SEC               |                 132 |                  0.259 |                 0.553 |            0.269 |
|  37 |          49 | Owen McCown              | UTSA                  | American Athletic |                 248 |                  0.253 |                 0.476 |            0.210 |
|  38 |          56 | Jared Hollins            | South Alabama         | Sun Belt          |                 133 |                  0.252 |                 0.451 |            0.184 |
|  39 |          31 | Nick Minicucci           | Delaware              | Conference USA    |                 185 |                  0.249 |                 0.486 |            0.255 |
|  40 |          48 | Bear Bachmeier           | BYU                   | Big 12            |                 267 |                  0.247 |                 0.509 |            0.210 |
|  41 |          27 | JC French                | Cincinnati            | Big 12            |                 246 |                  0.244 |                 0.528 |            0.275 |
|  42 |          28 | Kamario Taylor           | Mississippi State     | SEC               |                 134 |                  0.241 |                 0.507 |            0.272 |
|  43 |          32 | Ashton Daniels           | Florida State         | ACC               |                 242 |                  0.233 |                 0.467 |            0.252 |
|  44 |          72 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |                 251 |                  0.233 |                 0.502 |            0.146 |
|  45 |         124 | Landon Varnes            | Kennesaw State        | Conference USA    |                  41 |                  0.233 |                 0.463 |            0.044 |
|  46 |          47 | Trey Owens               | Arkansas State        | Sun Belt          |                 266 |                  0.230 |                 0.530 |            0.211 |
|  47 |          45 | Austin Simmons           | Missouri              | SEC               |                 241 |                  0.224 |                 0.465 |            0.221 |
|  48 |          16 | Brad Jackson             | Texas State           | Pac-12            |                 251 |                  0.223 |                 0.490 |            0.332 |
|  49 |          38 | Cale Hellums             | Army                  | American Athletic |                 226 |                  0.222 |                 0.496 |            0.239 |
|  50 |          63 | Trinidad Chambliss       | Ole Miss              | SEC               |                 256 |                  0.217 |                 0.496 |            0.168 |
|  51 |          42 | Caden Creel              | Jacksonville State    | Conference USA    |                 300 |                  0.217 |                 0.483 |            0.225 |
|  52 |          69 | Ryan Browne              | Purdue                | Big Ten           |                 255 |                  0.216 |                 0.490 |            0.148 |
|  53 |          62 | Blake Baker              | Louisiana Tech        | Sun Belt          |                 161 |                  0.208 |                 0.497 |            0.174 |
|  54 |          41 | CJ Bailey                | NC State              | ACC               |                 198 |                  0.208 |                 0.460 |            0.227 |
|  55 |          88 | Davis Warren             | Stanford              | ACC               |                 198 |                  0.205 |                 0.429 |            0.113 |
|  56 |          98 | McCae Hillstead          | Utah State            | Pac-12            |                  68 |                  0.201 |                 0.515 |            0.099 |
|  57 |          43 | Walker Eget              | Duke                  | ACC               |                 222 |                  0.200 |                 0.473 |            0.225 |
|  58 |          92 | Nathan Hayes             | North Dakota State    | Mountain West     |                 207 |                  0.199 |                 0.473 |            0.111 |
|  59 |          65 | Kalieb Osborne           | UConn                 | FBS Independents  |                 224 |                  0.197 |                 0.473 |            0.160 |
|  60 |          46 | Baylor Hayes             | Tulsa                 | American Athletic |                 234 |                  0.195 |                 0.432 |            0.214 |
|  61 |          67 | Billy Edwards            | North Carolina        | ACC               |                 273 |                  0.182 |                 0.542 |            0.155 |
|  62 |          44 | Sam Leavitt              | LSU                   | SEC               |                 244 |                  0.181 |                 0.541 |            0.223 |
|  63 |          51 | Lanorris Sellers         | South Carolina        | SEC               |                 253 |                  0.181 |                 0.470 |            0.209 |
|  64 |          54 | Isaiah Marshall          | Kansas                | Big 12            |                 243 |                  0.178 |                 0.444 |            0.197 |
|  65 |          75 | Max Johnson              | Georgia Southern      | Sun Belt          |                 233 |                  0.174 |                 0.476 |            0.141 |
|  66 |          87 | Will Hammond             | Texas Tech            | Big 12            |                 151 |                  0.173 |                 0.497 |            0.117 |
|  67 |          35 | Braden Atkinson          | Oregon State          | Pac-12            |                 216 |                  0.172 |                 0.486 |            0.243 |
|  68 |          52 | Dante Moore              | Oregon                | Big Ten           |                  89 |                  0.168 |                 0.393 |            0.205 |
|  69 |         146 | Trace Johnson            | Tulane                | American Athletic |                 106 |                  0.165 |                 0.491 |           -0.006 |
|  70 |          95 | Malachi Nelson           | Syracuse              | ACC               |                  72 |                  0.164 |                 0.500 |            0.106 |
|  71 |          89 | Henry Belin IV           | Missouri State        | Conference USA    |                 142 |                  0.163 |                 0.479 |            0.113 |
|  72 |          59 | Jaylen Raynor            | Iowa State            | Big 12            |                 184 |                  0.162 |                 0.440 |            0.176 |
|  73 |         104 | Keldric Luster           | Ball State            | Mid-American      |                 170 |                  0.158 |                 0.453 |            0.081 |
|  74 |          55 | Deshawn Purdie           | Liberty               | Conference USA    |                 178 |                  0.154 |                 0.472 |            0.196 |
|  75 |          83 | Trey Hedden              | New Mexico State      | Conference USA    |                 121 |                  0.146 |                 0.413 |            0.124 |
|  76 |          99 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |                 247 |                  0.143 |                 0.449 |            0.097 |
|  77 |          91 | Jackson Arnold           | UNLV                  | Mountain West     |                 288 |                  0.141 |                 0.444 |            0.112 |
|  78 |         117 | Roman Gagliano           | Middle Tennessee      | Conference USA    |                 296 |                  0.139 |                 0.480 |            0.055 |
|  79 |          93 | Camden Coleman           | James Madison         | Sun Belt          |                 186 |                  0.138 |                 0.452 |            0.107 |
|  80 |          66 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |                  59 |                  0.138 |                 0.492 |            0.158 |
|  81 |          50 | Josh Hoover              | Indiana               | Big Ten           |                 190 |                  0.136 |                 0.453 |            0.209 |
|  82 |          86 | Bryce Underwood          | Michigan              | Big Ten           |                 172 |                  0.136 |                 0.483 |            0.122 |
|  83 |         130 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |                  80 |                  0.123 |                 0.475 |            0.025 |
|  84 |         115 | Jadyn Glasser            | Central Michigan      | Mid-American      |                  60 |                  0.122 |                 0.417 |            0.063 |
|  85 |          71 | Jared Curtis             | Vanderbilt            | SEC               |                 230 |                  0.122 |                 0.457 |            0.146 |
|  86 |          80 | Tommy Carr               | Michigan              | Big Ten           |                 106 |                  0.112 |                 0.481 |            0.129 |
|  87 |          58 | Dylan Raiola             | Oregon                | Big Ten           |                 162 |                  0.111 |                 0.389 |            0.178 |
|  88 |          76 | Rocco Becht              | Penn State            | Big Ten           |                 216 |                  0.108 |                 0.444 |            0.141 |
|  89 |         123 | Mason McKenzie           | Boston College        | ACC               |                 267 |                  0.108 |                 0.427 |            0.049 |
|  90 |         109 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |                 240 |                  0.106 |                 0.471 |            0.074 |
|  91 |          64 | Jayden Mandal            | Fresno State          | Pac-12            |                 222 |                  0.103 |                 0.450 |            0.163 |
|  92 |          90 | Hank Brown               | Iowa                  | Big Ten           |                 167 |                  0.103 |                 0.461 |            0.112 |
|  93 |          96 | Tyler Hughes             | Wyoming               | Mountain West     |                 225 |                  0.100 |                 0.476 |            0.102 |
|  94 |          97 | D.J. Lagway              | Baylor                | Big 12            |                 255 |                  0.097 |                 0.435 |            0.102 |
|  95 |          82 | Malachi Singleton        | App State             | Sun Belt          |                 233 |                  0.092 |                 0.455 |            0.124 |
|  96 |         127 | Alonza Barnett           | UCF                   | Big 12            |                  70 |                  0.091 |                 0.429 |            0.037 |
|  97 |          74 | Nick Poulos              | Ohio                  | Mid-American      |                 126 |                  0.090 |                 0.500 |            0.144 |
|  98 |         107 | Conner Harrell           | Charlotte             | American Athletic |                 120 |                  0.088 |                 0.425 |            0.074 |
|  99 |          85 | Aidan Armenta            | UL Monroe             | Sun Belt          |                 117 |                  0.086 |                 0.402 |            0.122 |
| 100 |         105 | Malik Washington         | Maryland              | Big Ten           |                 226 |                  0.084 |                 0.438 |            0.080 |
| 101 |         147 | Broc Lowry               | Western Michigan      | Mid-American      |                 197 |                  0.083 |                 0.462 |           -0.008 |
| 102 |         116 | Isaac Wilson             | Colorado              | Big 12            |                 161 |                  0.081 |                 0.447 |            0.062 |
| 103 |         119 | Jay Kastantin            | Bowling Green         | Mid-American      |                 240 |                  0.077 |                 0.438 |            0.053 |
| 104 |         110 | Byrum Brown              | Auburn                | SEC               |                 334 |                  0.074 |                 0.428 |            0.073 |
| 105 |         132 | J.J. Kohl                | Florida International | Conference USA    |                 251 |                  0.069 |                 0.438 |            0.017 |
| 106 |         112 | Micah Alejado            | Hawai'i               | Mountain West     |                 363 |                  0.067 |                 0.438 |            0.068 |
| 107 |         142 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |                 162 |                  0.066 |                 0.463 |           -0.002 |
| 108 |         113 | Beau Pribula             | Virginia              | ACC               |                 200 |                  0.061 |                 0.425 |            0.066 |
| 109 |          81 | Colton Joseph            | Wisconsin             | Big Ten           |                 159 |                  0.060 |                 0.415 |            0.124 |
| 110 |         102 | Jaden Craig              | TCU                   | Big 12            |                 333 |                  0.056 |                 0.447 |            0.089 |
| 111 |         128 | Julian Lewis             | Colorado              | Big 12            |                  63 |                  0.052 |                 0.365 |            0.029 |
| 112 |          94 | Demond Williams Jr.      | Washington            | Big Ten           |                 219 |                  0.049 |                 0.461 |            0.106 |
| 113 |         126 | Angel H Flores           | Central Michigan      | Mid-American      |                 121 |                  0.048 |                 0.405 |            0.038 |
| 114 |          77 | Anthony Colandrea        | Nebraska              | Big Ten           |                 304 |                  0.046 |                 0.434 |            0.140 |
| 115 |         103 | Taron Dickens            | Northern Illinois     | Mountain West     |                 196 |                  0.046 |                 0.459 |            0.085 |
| 116 |         143 | Noah Kim                 | Eastern Michigan      | Mid-American      |                 202 |                  0.045 |                 0.441 |           -0.002 |
| 117 |         114 | Rickie Collins           | Kennesaw State        | Conference USA    |                 233 |                  0.044 |                 0.459 |            0.064 |
| 118 |         122 | Kenny Minchey            | Kentucky              | SEC               |                 256 |                  0.040 |                 0.480 |            0.051 |
| 119 |         140 | Tramell Jones Jr.        | Florida               | SEC               |                  65 |                  0.036 |                 0.385 |            0.000 |
| 120 |         137 | Dru Deshields            | Kent State            | Mid-American      |                 225 |                  0.035 |                 0.382 |            0.004 |
| 121 |         125 | Ayden Pereira            | Georgia State         | Sun Belt          |                  61 |                  0.031 |                 0.410 |            0.041 |
| 122 |         139 | Skyler Locklear          | Missouri State        | Conference USA    |                 112 |                  0.026 |                 0.393 |            0.001 |
| 123 |         118 | Keyone Jenkins           | UCF                   | Big 12            |                 187 |                  0.021 |                 0.439 |            0.054 |
| 124 |         100 | Jacurri Brown            | Rice                  | American Athletic |                 147 |                  0.016 |                 0.422 |            0.092 |
| 125 |         108 | John Mateer              | Oklahoma              | SEC               |                 258 |                  0.014 |                 0.442 |            0.074 |
| 126 |         111 | Luke Weaver              | San José State        | Mountain West     |                 243 |                  0.011 |                 0.473 |            0.069 |
| 127 |         148 | Emory Williams           | East Carolina         | American Athletic |                 141 |                  0.007 |                 0.411 |           -0.009 |
| 128 |          61 | Stone Saunders           | San Diego State       | Pac-12            |                  52 |                  0.002 |                 0.365 |            0.175 |
| 129 |         138 | Nico Iamaleava           | UCLA                  | Big Ten           |                 132 |                 -0.006 |                 0.432 |            0.001 |
| 130 |         155 | Zion Turner              | Marshall              | Sun Belt          |                  96 |                 -0.009 |                 0.385 |           -0.031 |
| 131 |         120 | Alberto Mendoza          | Georgia Tech          | ACC               |                 194 |                 -0.012 |                 0.474 |            0.052 |
| 132 |         150 | Brayden Roggow           | Akron                 | Mid-American      |                 132 |                 -0.014 |                 0.386 |           -0.017 |
| 133 |         144 | Arch Manning             | Texas                 | SEC               |                 224 |                 -0.021 |                 0.415 |           -0.004 |
| 134 |         167 | Tait Reynolds            | Clemson               | ACC               |                 279 |                 -0.024 |                 0.441 |           -0.071 |
| 135 |          70 | Owen Eshelman            | Washington State      | Pac-12            |                 104 |                 -0.025 |                 0.471 |            0.147 |
| 136 |         152 | KJ Jackson               | Arkansas              | SEC               |                 217 |                 -0.037 |                 0.410 |           -0.025 |
| 137 |         134 | Raymond Moore III        | UTEP                  | Mountain West     |                  65 |                 -0.041 |                 0.385 |            0.015 |
| 138 |         129 | Brock Glenn              | Western Kentucky      | Conference USA    |                 175 |                 -0.043 |                 0.451 |            0.027 |
| 139 |         131 | Jackson Brousseau        | California            | ACC               |                  72 |                 -0.044 |                 0.403 |            0.019 |
| 140 |         151 | M.Van Buren Jr.          | South Florida         | American Athletic |                 179 |                 -0.048 |                 0.441 |           -0.025 |
| 141 |         153 | Quinn Henicle            | Old Dominion          | Sun Belt          |                 139 |                 -0.050 |                 0.403 |           -0.026 |
| 142 |         121 | Cutter Boley             | Arizona State         | Big 12            |                 126 |                 -0.059 |                 0.421 |            0.052 |
| 143 |         136 | Alessio Milivojevic      | Michigan State        | Big Ten           |                 189 |                 -0.064 |                 0.423 |            0.007 |
| 144 |         133 | Steven Angeli            | Syracuse              | ACC               |                 190 |                 -0.067 |                 0.374 |            0.016 |
| 145 |         156 | Jason Wright             | Buffalo               | Mid-American      |                 190 |                 -0.073 |                 0.405 |           -0.034 |
| 146 |         149 | Will Crowder             | Troy                  | Sun Belt          |                 157 |                 -0.073 |                 0.420 |           -0.011 |
| 147 |         141 | Toa Faavae               | New Mexico            | Mountain West     |                 155 |                 -0.074 |                 0.394 |           -0.001 |
| 148 |         170 | Mitch Griffis            | East Carolina         | American Athletic |                 122 |                 -0.084 |                 0.385 |           -0.115 |
| 149 |         161 | Drake Lindsey            | Minnesota             | Big Ten           |                 199 |                 -0.087 |                 0.392 |           -0.045 |
| 150 |         183 | Jaxon Potter             | Old Dominion          | Sun Belt          |                  65 |                 -0.089 |                 0.400 |           -0.187 |
| 151 |         164 | George MacIntyre         | Tennessee             | SEC               |                 115 |                 -0.091 |                 0.417 |           -0.058 |
| 152 |         159 | Jaron-Keawe Sagapolutele | California            | ACC               |                 200 |                 -0.091 |                 0.395 |           -0.044 |
| 153 |          60 | Elijah Brown             | Washington            | Big Ten           |                  60 |                 -0.095 |                 0.467 |            0.175 |
| 154 |         171 | Caleb Heavner            | Miami (OH)            | Mid-American      |                 165 |                 -0.098 |                 0.406 |           -0.116 |
| 155 |         106 | Austin Carlisle          | UL Monroe             | Sun Belt          |                  96 |                 -0.100 |                 0.500 |            0.078 |
| 156 |         135 | Faizon Brandon           | Tennessee             | SEC               |                  98 |                 -0.111 |                 0.357 |            0.008 |
| 157 |         158 | Marcel Reed              | Texas A&M             | SEC               |                 212 |                 -0.115 |                 0.429 |           -0.039 |
| 158 |         175 | Caden Pinnick            | Washington State      | Pac-12            |                 181 |                 -0.116 |                 0.420 |           -0.134 |
| 159 |         184 | EJ Colson                | UTEP                  | Mountain West     |                  93 |                 -0.120 |                 0.409 |           -0.194 |
| 160 |         172 | Grady Brosterhous        | Utah State            | Pac-12            |                 170 |                 -0.120 |                 0.341 |           -0.116 |
| 161 |         180 | Kadin Semonza            | Tulane                | American Athletic |                 119 |                 -0.131 |                 0.319 |           -0.149 |
| 162 |         166 | Ryder Burton             | UAB                   | American Athletic |                 209 |                 -0.139 |                 0.411 |           -0.069 |
| 163 |         162 | Cibastian Broughton      | Akron                 | Mid-American      |                  92 |                 -0.157 |                 0.467 |           -0.051 |
| 164 |         160 | Landyn Locke             | Sam Houston           | Conference USA    |                 201 |                 -0.163 |                 0.353 |           -0.045 |
| 165 |         168 | Jake Fette               | Arizona State         | Big 12            |                  56 |                 -0.172 |                 0.339 |           -0.092 |
| 166 |         174 | Jayden Denegal           | San Diego State       | Pac-12            |                 104 |                 -0.173 |                 0.346 |           -0.128 |
| 167 |         182 | Elijah Holmes            | Buffalo               | Mid-American      |                  68 |                 -0.174 |                 0.368 |           -0.167 |
| 168 |         145 | AJ Surace                | Rutgers               | Big Ten           |                  67 |                 -0.179 |                 0.388 |           -0.005 |
| 169 |         181 | Cole Gonzales            | Charlotte             | American Athletic |                 100 |                 -0.184 |                 0.420 |           -0.161 |
| 170 |         101 | Luke Fahey               | Ohio State            | Big Ten           |                  47 |                 -0.193 |                 0.404 |            0.091 |
| 171 |         179 | AJ Bianco                | Nevada                | Mountain West     |                  71 |                 -0.195 |                 0.296 |           -0.149 |
| 172 |         165 | Jaxon Smolik             | Temple                | American Athletic |                  48 |                 -0.197 |                 0.375 |           -0.068 |
| 173 |         176 | Carter Jones             | Nevada                | Mountain West     |                  97 |                 -0.205 |                 0.361 |           -0.136 |
| 174 |         169 | Jackson Sharman          | Sacramento State      | Mid-American      |                 157 |                 -0.207 |                 0.369 |           -0.109 |
| 175 |         163 | Landy Lyddy              | Southern Miss         | Sun Belt          |                 144 |                 -0.243 |                 0.333 |           -0.055 |
| 176 |         154 | Holden Geriner           | Pittsburgh            | ACC               |                  87 |                 -0.251 |                 0.356 |           -0.028 |
| 177 |         186 | Tucker Kilcrease         | Troy                  | Sun Belt          |                  62 |                 -0.338 |                 0.339 |           -0.239 |
| 178 |         178 | Ethan Hampton            | Southern Miss         | Sun Belt          |                  44 |                 -0.343 |                 0.409 |           -0.142 |
| 179 |         173 | Adam Damante             | New Mexico State      | Conference USA    |                  73 |                 -0.360 |                 0.260 |           -0.117 |
| 180 |         187 | Brogan McCaughey         | Eastern Michigan      | Mid-American      |                  54 |                 -0.382 |                 0.389 |           -0.244 |

## All plays

|   # | QB                       | Team                  | Conf              |   G |   Dropbacks |   Rushes |   Plays |   EPA/dropback |   EPA/rush |   EPA/play |   Success |   EPA/play (WP 10–90%) |
|----:|:-------------------------|:----------------------|:------------------|----:|------------:|---------:|--------:|---------------:|-----------:|-----------:|----------:|-----------------------:|
|   1 | David McComb             | Miami (OH)            | Mid-American      |   4 |         109 |       11 |     120 |          0.565 |      0.615 |      0.570 |     0.525 |                  0.611 |
|   2 | Tayven Jackson           | North Texas           | American Athletic |   9 |         303 |       27 |     330 |          0.471 |      0.433 |      0.468 |     0.564 |                  0.513 |
|   3 | Darian Mensah            | Miami                 | ACC               |   9 |         284 |       24 |     308 |          0.452 |      0.553 |      0.460 |     0.575 |                  0.457 |
|   4 | Hauss Hejny              | Colorado State        | Pac-12            |   6 |         163 |       34 |     197 |          0.421 |      0.552 |      0.444 |     0.538 |                  0.382 |
|   5 | Giovanni Lopez           | Wake Forest           | ACC               |   8 |         235 |       60 |     295 |          0.375 |      0.640 |      0.429 |     0.539 |                  0.553 |
|   6 | Julian Sayin             | Ohio State            | Big Ten           |   7 |         205 |       23 |     228 |          0.408 |      0.481 |      0.416 |     0.566 |                  0.504 |
|   7 | Jackson Gutierrez        | Navy                  | American Athletic |   9 |          90 |      192 |     282 |          0.387 |      0.418 |      0.408 |     0.528 |                  0.365 |
|   8 | JC Evans                 | James Madison         | Sun Belt          |   6 |          64 |       42 |     106 |          0.385 |      0.417 |      0.398 |     0.538 |                  0.494 |
|   9 | Thomas Castellanos       | Texas Tech            | Big 12            |   6 |          62 |       50 |     112 |          0.409 |      0.300 |      0.360 |     0.509 |                  0.380 |
|  10 | Caden Veltkamp           | Florida Atlantic      | American Athletic |   9 |         357 |       31 |     388 |          0.376 |      0.051 |      0.350 |     0.534 |                  0.352 |
|  11 | Michael Hawkins Jr.      | West Virginia         | Big 12            |   9 |         192 |      163 |     355 |          0.303 |      0.394 |      0.345 |     0.454 |                  0.438 |
|  12 | Aidan Chiles             | Northwestern          | Big Ten           |   8 |         222 |       65 |     287 |          0.286 |      0.544 |      0.344 |     0.533 |                  0.336 |
|  13 | Lincoln Kienholz         | Louisville            | ACC               |   9 |         247 |       74 |     321 |          0.332 |      0.364 |      0.339 |     0.530 |                  0.364 |
|  14 | Kevin Jennings           | SMU                   | ACC               |   9 |         297 |       47 |     344 |          0.388 |      0.020 |      0.337 |     0.541 |                  0.329 |
|  15 | Avery Johnson            | Kansas State          | Big 12            |   6 |         190 |       47 |     237 |          0.259 |      0.638 |      0.334 |     0.511 |                  0.339 |
|  16 | Brad Jackson             | Texas State           | Pac-12            |   9 |         263 |       85 |     348 |          0.326 |      0.352 |      0.332 |     0.517 |                  0.223 |
|  17 | Bishop Davenport         | South Alabama         | Sun Belt          |   3 |          85 |       25 |     110 |          0.290 |      0.465 |      0.330 |     0.500 |                  0.392 |
|  18 | C.J. Carr                | Notre Dame            | FBS Independents  |   9 |         265 |       23 |     288 |          0.336 |      0.254 |      0.329 |     0.514 |                  0.315 |
|  19 | Conner Weigman           | Houston               | Big 12            |   9 |         266 |       63 |     329 |          0.333 |      0.313 |      0.329 |     0.553 |                  0.312 |
|  20 | Jayden Maiava            | USC                   | Big Ten           |   9 |         310 |       13 |     323 |          0.352 |     -0.319 |      0.325 |     0.557 |                  0.368 |
|  21 | Drew Mestemaker          | Oklahoma State        | Big 12            |   9 |         319 |       27 |     346 |          0.288 |      0.638 |      0.316 |     0.546 |                  0.305 |
|  22 | Mason Heintschel         | Pittsburgh            | ACC               |   5 |         153 |       25 |     178 |          0.348 |     -0.003 |      0.299 |     0.466 |                  0.295 |
|  23 | Marcus Stokes            | Memphis               | American Athletic |   9 |         273 |       58 |     331 |          0.308 |      0.214 |      0.291 |     0.529 |                  0.375 |
|  24 | Keelon Russell           | Alabama               | SEC               |   9 |         273 |       50 |     323 |          0.241 |      0.563 |      0.291 |     0.520 |                  0.318 |
|  25 | Maddux Madsen            | Boise State           | Pac-12            |   8 |         230 |       34 |     264 |          0.221 |      0.727 |      0.287 |     0.527 |                  0.271 |
|  26 | Noah Fifita              | Arizona               | Big 12            |   9 |         327 |       46 |     373 |          0.286 |      0.218 |      0.278 |     0.509 |                  0.271 |
|  27 | JC French                | Cincinnati            | Big 12            |   9 |         259 |       74 |     333 |          0.270 |      0.293 |      0.275 |     0.535 |                  0.244 |
|  28 | Kamario Taylor           | Mississippi State     | SEC               |   6 |         175 |       29 |     204 |          0.212 |      0.630 |      0.272 |     0.520 |                  0.241 |
|  29 | Cameran Brown            | Georgia State         | Sun Belt          |   7 |         172 |       34 |     206 |          0.272 |      0.260 |      0.270 |     0.510 |                  0.340 |
|  30 | Aaron Philo              | Florida               | SEC               |   7 |         163 |       35 |     198 |          0.292 |      0.158 |      0.269 |     0.535 |                  0.259 |
|  31 | Nick Minicucci           | Delaware              | Conference USA    |   7 |         234 |       21 |     255 |          0.232 |      0.517 |      0.255 |     0.475 |                  0.249 |
|  32 | Ashton Daniels           | Florida State         | ACC               |   9 |         257 |       81 |     338 |          0.166 |      0.524 |      0.252 |     0.473 |                  0.233 |
|  33 | Ajani Sheppard           | Temple                | American Athletic |   8 |         153 |       64 |     217 |          0.200 |      0.368 |      0.250 |     0.479 |                  0.292 |
|  34 | Dylan Lonergan           | Rutgers               | Big Ten           |   6 |         132 |       16 |     148 |          0.305 |     -0.210 |      0.249 |     0.486 |                  0.326 |
|  35 | Braden Atkinson          | Oregon State          | Pac-12            |   9 |         383 |       20 |     403 |          0.258 |     -0.042 |      0.243 |     0.491 |                  0.172 |
|  36 | Devon Dampier            | Utah                  | Big 12            |   9 |         266 |       88 |     354 |          0.212 |      0.327 |      0.240 |     0.531 |                  0.301 |
|  37 | Gunner Stockton          | Georgia               | SEC               |   9 |         205 |       42 |     247 |          0.236 |      0.258 |      0.239 |     0.530 |                  0.323 |
|  38 | Cale Hellums             | Army                  | American Athletic |   9 |          90 |      181 |     271 |          0.017 |      0.349 |      0.239 |     0.517 |                  0.222 |
|  39 | Katin Houser             | Illinois              | Big Ten           |   8 |         263 |       29 |     292 |          0.212 |      0.403 |      0.231 |     0.507 |                  0.276 |
|  40 | John Alan Richter        | Toledo                | Mid-American      |   9 |         286 |       13 |     299 |          0.256 |     -0.366 |      0.229 |     0.468 |                  0.293 |
|  41 | CJ Bailey                | NC State              | ACC               |   9 |         282 |       48 |     330 |          0.215 |      0.302 |      0.227 |     0.476 |                  0.208 |
|  42 | Caden Creel              | Jacksonville State    | Conference USA    |   9 |         247 |      122 |     369 |          0.222 |      0.232 |      0.225 |     0.501 |                  0.217 |
|  43 | Walker Eget              | Duke                  | ACC               |   9 |         250 |        5 |     255 |          0.227 |      0.129 |      0.225 |     0.478 |                  0.200 |
|  44 | Sam Leavitt              | LSU                   | SEC               |   9 |         316 |       72 |     388 |          0.190 |      0.368 |      0.223 |     0.546 |                  0.181 |
|  45 | Austin Simmons           | Missouri              | SEC               |   9 |         291 |       16 |     307 |          0.238 |     -0.077 |      0.221 |     0.463 |                  0.224 |
|  46 | Baylor Hayes             | Tulsa                 | American Athletic |   7 |         232 |       29 |     261 |          0.223 |      0.143 |      0.214 |     0.448 |                  0.195 |
|  47 | Trey Owens               | Arkansas State        | Sun Belt          |   9 |         280 |       51 |     331 |          0.172 |      0.428 |      0.211 |     0.523 |                  0.230 |
|  48 | Bear Bachmeier           | BYU                   | Big 12            |   9 |         248 |       79 |     327 |          0.139 |      0.432 |      0.210 |     0.508 |                  0.247 |
|  49 | Owen McCown              | UTSA                  | American Athletic |   9 |         291 |       35 |     326 |          0.203 |      0.264 |      0.210 |     0.463 |                  0.253 |
|  50 | Josh Hoover              | Indiana               | Big Ten           |   9 |         216 |       21 |     237 |          0.195 |      0.351 |      0.209 |     0.468 |                  0.136 |
|  51 | Lanorris Sellers         | South Carolina        | SEC               |   9 |         291 |       81 |     372 |          0.079 |      0.675 |      0.209 |     0.481 |                  0.181 |
|  52 | Dante Moore              | Oregon                | Big Ten           |   4 |         106 |        3 |     109 |          0.227 |     -0.567 |      0.205 |     0.459 |                  0.168 |
|  53 | William Watson III       | Massachusetts         | Mid-American      |   7 |         170 |       33 |     203 |          0.140 |      0.510 |      0.200 |     0.443 |                  0.265 |
|  54 | Isaiah Marshall          | Kansas                | Big 12            |   8 |         238 |       88 |     326 |          0.096 |      0.472 |      0.197 |     0.448 |                  0.178 |
|  55 | Deshawn Purdie           | Liberty               | Conference USA    |   9 |         195 |       38 |     233 |          0.204 |      0.159 |      0.196 |     0.498 |                  0.154 |
|  56 | Jared Hollins            | South Alabama         | Sun Belt          |   7 |         163 |       39 |     202 |          0.173 |      0.231 |      0.184 |     0.426 |                  0.252 |
|  57 | Ksaan Farrar             | Colorado State        | Pac-12            |   6 |         156 |       12 |     168 |          0.147 |      0.619 |      0.181 |     0.429 |                 -0.074 |
|  58 | Dylan Raiola             | Oregon                | Big Ten           |   7 |         190 |        4 |     194 |          0.184 |     -0.085 |      0.178 |     0.423 |                  0.111 |
|  59 | Jaylen Raynor            | Iowa State            | Big 12            |   9 |         237 |       63 |     300 |          0.142 |      0.307 |      0.176 |     0.447 |                  0.162 |
|  60 | Elijah Brown             | Washington            | Big Ten           |   4 |         105 |        2 |     107 |          0.236 |     -2.993 |      0.175 |     0.495 |                 -0.095 |
|  61 | Stone Saunders           | San Diego State       | Pac-12            |   4 |          71 |        2 |      73 |          0.186 |     -0.221 |      0.175 |     0.438 |                  0.002 |
|  62 | Blake Baker              | Louisiana Tech        | Sun Belt          |   8 |         188 |       46 |     234 |          0.215 |      0.010 |      0.174 |     0.479 |                  0.208 |
|  63 | Trinidad Chambliss       | Ole Miss              | SEC               |   9 |         342 |       44 |     386 |          0.118 |      0.558 |      0.168 |     0.495 |                  0.217 |
|  64 | Jayden Mandal            | Fresno State          | Pac-12            |   9 |         267 |       46 |     313 |          0.160 |      0.177 |      0.163 |     0.463 |                  0.103 |
|  65 | Kalieb Osborne           | UConn                 | FBS Independents  |   9 |         276 |       70 |     346 |          0.070 |      0.518 |      0.160 |     0.457 |                  0.197 |
|  66 | Rodney Tisdale Jr.       | Western Kentucky      | Conference USA    |   7 |         150 |       24 |     174 |          0.179 |      0.027 |      0.158 |     0.454 |                  0.138 |
|  67 | Billy Edwards            | North Carolina        | ACC               |   9 |         289 |       27 |     316 |          0.156 |      0.146 |      0.155 |     0.525 |                  0.182 |
|  68 | Ty Dieffenbach           | UCLA                  | Big Ten           |   5 |         120 |       21 |     141 |          0.204 |     -0.150 |      0.151 |     0.390 |                  0.275 |
|  69 | Ryan Browne              | Purdue                | Big Ten           |   9 |         302 |       36 |     338 |          0.106 |      0.497 |      0.148 |     0.479 |                  0.216 |
|  70 | Owen Eshelman            | Washington State      | Pac-12            |   3 |         142 |       44 |     186 |          0.027 |      0.537 |      0.147 |     0.489 |                 -0.025 |
|  71 | Jared Curtis             | Vanderbilt            | SEC               |   8 |         238 |       58 |     296 |          0.094 |      0.358 |      0.146 |     0.466 |                  0.122 |
|  72 | Ethan Grunkemeyer        | Virginia Tech         | ACC               |   9 |         326 |       41 |     367 |          0.112 |      0.419 |      0.146 |     0.488 |                  0.233 |
|  73 | Mikey Keene              | Arizona State         | Big 12            |   3 |          66 |        1 |      67 |          0.170 |     -1.529 |      0.145 |     0.448 |                  0.039 |
|  74 | Nick Poulos              | Ohio                  | Mid-American      |   6 |         127 |       43 |     170 |          0.071 |      0.359 |      0.144 |     0.506 |                  0.090 |
|  75 | Max Johnson              | Georgia Southern      | Sun Belt          |   9 |         310 |       22 |     332 |          0.135 |      0.229 |      0.141 |     0.464 |                  0.174 |
|  76 | Rocco Becht              | Penn State            | Big Ten           |   9 |         276 |       49 |     325 |          0.148 |      0.102 |      0.141 |     0.452 |                  0.108 |
|  77 | Anthony Colandrea        | Nebraska              | Big Ten           |   9 |         325 |       63 |     388 |          0.062 |      0.546 |      0.140 |     0.482 |                  0.046 |
|  78 | Matt Vezza               | Ohio                  | Mid-American      |   6 |          70 |       27 |      97 |         -0.091 |      0.736 |      0.139 |     0.515 |                  0.288 |
|  79 | Jeremy Hecklinski        | Iowa                  | Big Ten           |   5 |          68 |        1 |      69 |          0.117 |      1.093 |      0.131 |     0.522 |                 -0.133 |
|  80 | Tommy Carr               | Michigan              | Big Ten           |   5 |         100 |       26 |     126 |         -0.002 |      0.631 |      0.129 |     0.476 |                  0.112 |
|  81 | Colton Joseph            | Wisconsin             | Big Ten           |   8 |         194 |       76 |     270 |          0.061 |      0.287 |      0.124 |     0.437 |                  0.060 |
|  82 | Malachi Singleton        | App State             | Sun Belt          |   9 |         287 |       36 |     323 |          0.153 |     -0.104 |      0.124 |     0.474 |                  0.092 |
|  83 | Trey Hedden              | New Mexico State      | Conference USA    |   6 |         163 |        9 |     172 |          0.120 |      0.183 |      0.124 |     0.413 |                  0.146 |
|  84 | Nate Bennett             | Baylor                | Big 12            |   4 |          67 |        2 |      69 |          0.042 |      2.810 |      0.122 |     0.464 |                  0.710 |
|  85 | Aidan Armenta            | UL Monroe             | Sun Belt          |   8 |         213 |       39 |     252 |          0.088 |      0.310 |      0.122 |     0.452 |                  0.086 |
|  86 | Bryce Underwood          | Michigan              | Big Ten           |   7 |         134 |       51 |     185 |          0.118 |      0.133 |      0.122 |     0.459 |                  0.136 |
|  87 | Will Hammond             | Texas Tech            | Big 12            |   7 |         217 |       28 |     245 |          0.094 |      0.296 |      0.117 |     0.490 |                  0.173 |
|  88 | Davis Warren             | Stanford              | ACC               |   9 |         320 |       11 |     331 |          0.109 |      0.235 |      0.113 |     0.414 |                  0.205 |
|  89 | Henry Belin IV           | Missouri State        | Conference USA    |   8 |         171 |       17 |     188 |          0.074 |      0.506 |      0.113 |     0.452 |                  0.163 |
|  90 | Hank Brown               | Iowa                  | Big Ten           |   8 |         195 |       20 |     215 |          0.099 |      0.239 |      0.112 |     0.470 |                  0.103 |
|  91 | Jackson Arnold           | UNLV                  | Mountain West     |   9 |         254 |      104 |     358 |          0.042 |      0.283 |      0.112 |     0.450 |                  0.141 |
|  92 | Nathan Hayes             | North Dakota State    | Mountain West     |   9 |         238 |       40 |     278 |          0.033 |      0.576 |      0.111 |     0.471 |                  0.199 |
|  93 | Camden Coleman           | James Madison         | Sun Belt          |  10 |         248 |       35 |     283 |          0.105 |      0.123 |      0.107 |     0.442 |                  0.138 |
|  94 | Demond Williams Jr.      | Washington            | Big Ten           |   8 |         239 |       50 |     289 |          0.020 |      0.517 |      0.106 |     0.460 |                  0.049 |
|  95 | Malachi Nelson           | Syracuse              | ACC               |   3 |          74 |        6 |      80 |          0.126 |     -0.146 |      0.106 |     0.475 |                  0.164 |
|  96 | Tyler Hughes             | Wyoming               | Mountain West     |   9 |         197 |       93 |     290 |         -0.114 |      0.559 |      0.102 |     0.483 |                  0.100 |
|  97 | D.J. Lagway              | Baylor                | Big 12            |   7 |         284 |       33 |     317 |          0.073 |      0.347 |      0.102 |     0.426 |                  0.097 |
|  98 | McCae Hillstead          | Utah State            | Pac-12            |   4 |          80 |       31 |     111 |          0.012 |      0.325 |      0.099 |     0.495 |                  0.201 |
|  99 | D'Wayne' Winfield        | Louisiana             | Sun Belt          |   9 |         223 |      113 |     336 |         -0.016 |      0.318 |      0.097 |     0.443 |                  0.143 |
| 100 | Jacurri Brown            | Rice                  | American Athletic |   8 |          92 |      108 |     200 |         -0.208 |      0.347 |      0.092 |     0.435 |                  0.016 |
| 101 | Luke Fahey               | Ohio State            | Big Ten           |   5 |         106 |       11 |     117 |          0.039 |      0.596 |      0.091 |     0.470 |                 -0.193 |
| 102 | Jaden Craig              | TCU                   | Big 12            |   9 |         333 |       50 |     383 |          0.072 |      0.202 |      0.089 |     0.446 |                  0.056 |
| 103 | Taron Dickens            | Northern Illinois     | Mountain West     |   9 |         309 |       43 |     352 |          0.054 |      0.304 |      0.085 |     0.466 |                  0.046 |
| 104 | Keldric Luster           | Ball State            | Mid-American      |   8 |         250 |       63 |     313 |          0.032 |      0.276 |      0.081 |     0.428 |                  0.158 |
| 105 | Malik Washington         | Maryland              | Big Ten           |   9 |         316 |       44 |     360 |          0.043 |      0.346 |      0.080 |     0.433 |                  0.084 |
| 106 | Austin Carlisle          | UL Monroe             | Sun Belt          |   7 |          80 |       55 |     135 |         -0.171 |      0.441 |      0.078 |     0.519 |                 -0.100 |
| 107 | Conner Harrell           | Charlotte             | American Athletic |   6 |         149 |       26 |     175 |          0.076 |      0.067 |      0.074 |     0.371 |                  0.088 |
| 108 | John Mateer              | Oklahoma              | SEC               |   9 |         300 |       79 |     379 |          0.090 |      0.014 |      0.074 |     0.449 |                  0.014 |
| 109 | Deuce Bailey             | Coastal Carolina      | Sun Belt          |   9 |         292 |       64 |     356 |          0.048 |      0.192 |      0.074 |     0.441 |                  0.106 |
| 110 | Byrum Brown              | Auburn                | SEC               |   9 |         314 |      124 |     438 |         -0.015 |      0.295 |      0.073 |     0.434 |                  0.074 |
| 111 | Luke Weaver              | San José State        | Mountain West     |   8 |         257 |       44 |     301 |          0.117 |     -0.211 |      0.069 |     0.475 |                  0.011 |
| 112 | Micah Alejado            | Hawai'i               | Mountain West     |   9 |         401 |       24 |     425 |          0.073 |     -0.018 |      0.068 |     0.449 |                  0.067 |
| 113 | Beau Pribula             | Virginia              | ACC               |   9 |         239 |       69 |     308 |          0.058 |      0.092 |      0.066 |     0.435 |                  0.061 |
| 114 | Rickie Collins           | Kennesaw State        | Conference USA    |   9 |         249 |       76 |     325 |          0.048 |      0.118 |      0.064 |     0.471 |                  0.044 |
| 115 | Jadyn Glasser            | Central Michigan      | Mid-American      |   8 |         100 |       22 |     122 |          0.003 |      0.336 |      0.063 |     0.410 |                  0.122 |
| 116 | Isaac Wilson             | Colorado              | Big 12            |   7 |         189 |       44 |     233 |          0.134 |     -0.248 |      0.062 |     0.455 |                  0.081 |
| 117 | Roman Gagliano           | Middle Tennessee      | Conference USA    |   9 |         313 |       40 |     353 |          0.046 |      0.130 |      0.055 |     0.442 |                  0.139 |
| 118 | Keyone Jenkins           | UCF                   | Big 12            |   8 |         185 |       34 |     219 |          0.079 |     -0.087 |      0.054 |     0.434 |                  0.021 |
| 119 | Jay Kastantin            | Bowling Green         | Mid-American      |   9 |         241 |       46 |     287 |          0.045 |      0.094 |      0.053 |     0.449 |                  0.077 |
| 120 | Alberto Mendoza          | Georgia Tech          | ACC               |   9 |         290 |       20 |     310 |          0.039 |      0.236 |      0.052 |     0.481 |                 -0.012 |
| 121 | Cutter Boley             | Arizona State         | Big 12            |   7 |         184 |       30 |     214 |          0.052 |      0.052 |      0.052 |     0.449 |                 -0.059 |
| 122 | Kenny Minchey            | Kentucky              | SEC               |   9 |         282 |       32 |     314 |          0.038 |      0.166 |      0.051 |     0.468 |                  0.040 |
| 123 | Mason McKenzie           | Boston College        | ACC               |   9 |         250 |      120 |     370 |         -0.064 |      0.284 |      0.049 |     0.438 |                  0.108 |
| 124 | Landon Varnes            | Kennesaw State        | Conference USA    |   3 |          62 |        9 |      71 |          0.083 |     -0.221 |      0.044 |     0.408 |                  0.233 |
| 125 | Ayden Pereira            | Georgia State         | Sun Belt          |   8 |          97 |       32 |     129 |          0.035 |      0.058 |      0.041 |     0.403 |                  0.031 |
| 126 | Angel H Flores           | Central Michigan      | Mid-American      |   7 |         104 |      116 |     220 |         -0.227 |      0.276 |      0.038 |     0.414 |                  0.048 |
| 127 | Alonza Barnett           | UCF                   | Big 12            |   4 |         106 |       23 |     129 |          0.055 |     -0.046 |      0.037 |     0.426 |                  0.091 |
| 128 | Julian Lewis             | Colorado              | Big 12            |   4 |         102 |        6 |     108 |          0.024 |      0.123 |      0.029 |     0.389 |                  0.052 |
| 129 | Brock Glenn              | Western Kentucky      | Conference USA    |   9 |         193 |       89 |     282 |         -0.117 |      0.339 |      0.027 |     0.440 |                 -0.043 |
| 130 | Trey Kukuk               | Louisiana Tech        | Sun Belt          |   8 |          87 |       46 |     133 |         -0.041 |      0.151 |      0.025 |     0.466 |                  0.123 |
| 131 | Jackson Brousseau        | California            | ACC               |   5 |         126 |        7 |     133 |          0.030 |     -0.182 |      0.019 |     0.368 |                 -0.044 |
| 132 | J.J. Kohl                | Florida International | Conference USA    |   9 |         298 |       34 |     332 |          0.029 |     -0.085 |      0.017 |     0.434 |                  0.069 |
| 133 | Steven Angeli            | Syracuse              | ACC               |   6 |         221 |        9 |     230 |          0.005 |      0.289 |      0.016 |     0.417 |                 -0.067 |
| 134 | Raymond Moore III        | UTEP                  | Mountain West     |   9 |         110 |       58 |     168 |         -0.235 |      0.489 |      0.015 |     0.417 |                 -0.041 |
| 135 | Faizon Brandon           | Tennessee             | SEC               |   6 |         117 |       37 |     154 |         -0.161 |      0.543 |      0.008 |     0.416 |                 -0.111 |
| 136 | Alessio Milivojevic      | Michigan State        | Big Ten           |   8 |         235 |       23 |     258 |         -0.021 |      0.289 |      0.007 |     0.465 |                 -0.064 |
| 137 | Dru Deshields            | Kent State            | Mid-American      |   9 |         265 |       59 |     324 |         -0.056 |      0.274 |      0.004 |     0.383 |                  0.035 |
| 138 | Nico Iamaleava           | UCLA                  | Big Ten           |   5 |         124 |       31 |     155 |          0.000 |      0.003 |      0.001 |     0.432 |                 -0.006 |
| 139 | Skyler Locklear          | Missouri State        | Conference USA    |   5 |         117 |       24 |     141 |         -0.034 |      0.169 |      0.001 |     0.376 |                  0.026 |
| 140 | Tramell Jones Jr.        | Florida               | SEC               |   7 |         120 |       25 |     145 |         -0.055 |      0.264 |      0.000 |     0.462 |                  0.036 |
| 141 | Toa Faavae               | New Mexico            | Mountain West     |   9 |         140 |       64 |     204 |         -0.094 |      0.201 |     -0.001 |     0.426 |                 -0.074 |
| 142 | C.Del Rio-Wilson         | Marshall              | Sun Belt          |   7 |         157 |       56 |     213 |          0.002 |     -0.010 |     -0.002 |     0.437 |                  0.066 |
| 143 | Noah Kim                 | Eastern Michigan      | Mid-American      |   8 |         292 |       20 |     312 |         -0.004 |      0.033 |     -0.002 |     0.410 |                  0.045 |
| 144 | Arch Manning             | Texas                 | SEC               |   9 |         284 |       48 |     332 |         -0.019 |      0.086 |     -0.004 |     0.425 |                 -0.021 |
| 145 | AJ Surace                | Rutgers               | Big Ten           |   7 |         126 |       17 |     143 |          0.102 |     -0.795 |     -0.005 |     0.392 |                 -0.179 |
| 146 | Trace Johnson            | Tulane                | American Athletic |   5 |         132 |       18 |     150 |         -0.010 |      0.024 |     -0.006 |     0.427 |                  0.165 |
| 147 | Broc Lowry               | Western Michigan      | Mid-American      |   9 |         208 |       72 |     280 |         -0.061 |      0.146 |     -0.008 |     0.446 |                  0.083 |
| 148 | Emory Williams           | East Carolina         | American Athletic |   7 |         152 |       21 |     173 |         -0.009 |     -0.014 |     -0.009 |     0.434 |                  0.007 |
| 149 | Will Crowder             | Troy                  | Sun Belt          |   7 |         195 |       40 |     235 |         -0.113 |      0.484 |     -0.011 |     0.426 |                 -0.073 |
| 150 | Brayden Roggow           | Akron                 | Mid-American      |   9 |         209 |       19 |     228 |         -0.041 |      0.249 |     -0.017 |     0.408 |                 -0.014 |
| 151 | M.Van Buren Jr.          | South Florida         | American Athletic |   8 |         191 |       39 |     230 |         -0.016 |     -0.068 |     -0.025 |     0.470 |                 -0.048 |
| 152 | KJ Jackson               | Arkansas              | SEC               |   9 |         299 |       60 |     359 |         -0.046 |      0.075 |     -0.025 |     0.440 |                 -0.037 |
| 153 | Quinn Henicle            | Old Dominion          | Sun Belt          |   7 |         120 |       68 |     188 |         -0.220 |      0.317 |     -0.026 |     0.404 |                 -0.050 |
| 154 | Holden Geriner           | Pittsburgh            | ACC               |   6 |         138 |       16 |     154 |         -0.001 |     -0.259 |     -0.028 |     0.390 |                 -0.251 |
| 155 | Zion Turner              | Marshall              | Sun Belt          |   7 |         125 |       21 |     146 |         -0.104 |      0.408 |     -0.031 |     0.425 |                 -0.009 |
| 156 | Jason Wright             | Buffalo               | Mid-American      |   8 |         243 |       46 |     289 |         -0.077 |      0.198 |     -0.034 |     0.391 |                 -0.073 |
| 157 | Dexter Williams II       | Tulsa                 | American Athletic |   6 |          63 |       11 |      74 |         -0.020 |     -0.144 |     -0.038 |     0.419 |                 -0.160 |
| 158 | Marcel Reed              | Texas A&M             | SEC               |   9 |         279 |       61 |     340 |         -0.084 |      0.167 |     -0.039 |     0.429 |                 -0.115 |
| 159 | Jaron-Keawe Sagapolutele | California            | ACC               |   8 |         276 |        9 |     285 |         -0.032 |     -0.420 |     -0.044 |     0.414 |                 -0.091 |
| 160 | Landyn Locke             | Sam Houston           | Conference USA    |   8 |         274 |       24 |     298 |         -0.060 |      0.124 |     -0.045 |     0.379 |                 -0.163 |
| 161 | Drake Lindsey            | Minnesota             | Big Ten           |   9 |         299 |       13 |     312 |         -0.038 |     -0.223 |     -0.045 |     0.410 |                 -0.087 |
| 162 | Cibastian Broughton      | Akron                 | Mid-American      |   5 |         108 |       40 |     148 |         -0.137 |      0.180 |     -0.051 |     0.459 |                 -0.157 |
| 163 | Landy Lyddy              | Southern Miss         | Sun Belt          |   8 |         215 |       21 |     236 |         -0.068 |      0.074 |     -0.055 |     0.381 |                 -0.243 |
| 164 | George MacIntyre         | Tennessee             | SEC               |   7 |         123 |        6 |     129 |         -0.029 |     -0.646 |     -0.058 |     0.434 |                 -0.091 |
| 165 | Jaxon Smolik             | Temple                | American Athletic |   5 |          60 |       18 |      78 |         -0.164 |      0.254 |     -0.068 |     0.359 |                 -0.197 |
| 166 | Ryder Burton             | UAB                   | American Athletic |   9 |         245 |       46 |     291 |         -0.126 |      0.238 |     -0.069 |     0.416 |                 -0.139 |
| 167 | Tait Reynolds            | Clemson               | ACC               |   9 |         268 |       78 |     346 |         -0.149 |      0.199 |     -0.071 |     0.416 |                 -0.024 |
| 168 | Jake Fette               | Arizona State         | Big 12            |   4 |          79 |       15 |      94 |         -0.099 |     -0.055 |     -0.092 |     0.372 |                 -0.172 |
| 169 | Jackson Sharman          | Sacramento State      | Mid-American      |   9 |         275 |       20 |     295 |         -0.114 |     -0.039 |     -0.109 |     0.397 |                 -0.207 |
| 170 | Mitch Griffis            | East Carolina         | American Athletic |   9 |         142 |       32 |     174 |         -0.153 |      0.054 |     -0.115 |     0.385 |                 -0.084 |
| 171 | Caleb Heavner            | Miami (OH)            | Mid-American      |   8 |         143 |       46 |     189 |         -0.224 |      0.221 |     -0.116 |     0.402 |                 -0.098 |
| 172 | Grady Brosterhous        | Utah State            | Pac-12            |   7 |         200 |       80 |     280 |         -0.091 |     -0.179 |     -0.116 |     0.357 |                 -0.120 |
| 173 | Adam Damante             | New Mexico State      | Conference USA    |   6 |         124 |        8 |     132 |         -0.165 |      0.626 |     -0.117 |     0.394 |                 -0.360 |
| 174 | Jayden Denegal           | San Diego State       | Pac-12            |   7 |         157 |       17 |     174 |         -0.117 |     -0.229 |     -0.128 |     0.351 |                 -0.173 |
| 175 | Caden Pinnick            | Washington State      | Pac-12            |   6 |         195 |       53 |     248 |         -0.202 |      0.114 |     -0.134 |     0.403 |                 -0.116 |
| 176 | Carter Jones             | Nevada                | Mountain West     |   4 |          95 |       21 |     116 |         -0.176 |      0.045 |     -0.136 |     0.371 |                 -0.205 |
| 177 | Parker Puckett           | Mississippi State     | SEC               |   5 |          83 |       18 |     101 |         -0.281 |      0.516 |     -0.139 |     0.455 |                 -0.427 |
| 178 | Ethan Hampton            | Southern Miss         | Sun Belt          |   3 |          76 |        6 |      82 |         -0.119 |     -0.437 |     -0.142 |     0.439 |                 -0.343 |
| 179 | AJ Bianco                | Nevada                | Mountain West     |   6 |         109 |       21 |     130 |         -0.203 |      0.133 |     -0.149 |     0.300 |                 -0.195 |
| 180 | Kadin Semonza            | Tulane                | American Athletic |   5 |         132 |       17 |     149 |         -0.126 |     -0.330 |     -0.149 |     0.309 |                 -0.131 |
| 181 | Cole Gonzales            | Charlotte             | American Athletic |   5 |         129 |       11 |     140 |         -0.110 |     -0.756 |     -0.161 |     0.429 |                 -0.184 |
| 182 | Elijah Holmes            | Buffalo               | Mid-American      |   2 |          64 |        7 |      71 |         -0.181 |     -0.044 |     -0.167 |     0.366 |                 -0.174 |
| 183 | Jaxon Potter             | Old Dominion          | Sun Belt          |   4 |         125 |        8 |     133 |         -0.248 |      0.773 |     -0.187 |     0.376 |                 -0.089 |
| 184 | EJ Colson                | UTEP                  | Mountain West     |   7 |         120 |       61 |     181 |         -0.282 |     -0.021 |     -0.194 |     0.425 |                 -0.120 |
| 185 | Ryan Huff                | Old Dominion          | Sun Belt          |   4 |          77 |        6 |      83 |         -0.237 |      0.107 |     -0.212 |     0.289 |                 -0.356 |
| 186 | Tucker Kilcrease         | Troy                  | Sun Belt          |   5 |          86 |       31 |     117 |         -0.280 |     -0.124 |     -0.239 |     0.308 |                 -0.338 |
| 187 | Brogan McCaughey         | Eastern Michigan      | Mid-American      |   3 |          64 |       11 |      75 |         -0.262 |     -0.136 |     -0.244 |     0.400 |                 -0.382 |
