from django.db import models

# Game
# season (FK)
# home (FK=TeamSeason)
# away (FK=TeamSeason)
# arena (FK=Venue)
# rink
# home_lockerroom
# away_lockerroom
# home_drinks
# away_drinks
# notes
#
# Shot
# game (FK)
# period
# time
# team (FK=TeamSeason)
# player (FK)
# ice_location
# notes
#
# Goal
# shot (FK)
# assisted_by_1 (FK=Player)
# assisted_by_2 (FK=Player)
#
# Penalty
# game (FK)
# period
# time
# team (FK=TeamSeason)
# player (FK)
# length
# penalty_type
# ice_location
# notes
#
# GameAttendance
# game (FK)
# player (FK)
# attendance (choices=in,tentative,out)
#
# SubRequest
# game (FK)
# team (FK=TeamSeason)
# player_out (FK=Player)
# player_in (FK=Player)
# requested_at (datetime)
# requested_by (FK=Player)
# decision (choices=null,approved,denied)
# decision_at (datetime)
# decision_by (FK=Player)
