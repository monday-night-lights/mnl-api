# from django.db import models

# http://django-organizations.readthedocs.io/en/latest/cookbook.html#custom-org-with-simple-inheritance
# Team
# name
# logo
# goal_horn (FK=Track)
#
# TeamSeason
# season (FK)
# team (FK)
# gm (FK=Player)
# asst_gm (FK=Player)
#
# Player
# user (FK)
# nicknames (array)
# projected_round
# handedness
# phone
# drink_participation (boolean)
# sub_only (boolean)
#
# PlayerStint
# player (FK)
# team (FK=TeamSeason)
# number
# positions (array)
# start_date
# end_date
#
# TradeGroup
# date
# notes
#
# Trade
# group (FK)
# player (FK)
# from (FK=TeamSeason)
# to (FK=TeamSeason)
