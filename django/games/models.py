# from django.db import models


# Game
#     season (FK)
#     home (FK TeamSeason)
#     away (FK TeamSeason)
#     arena (FK Venue)
#     rink (FK on save ensure rink in arena)
#     lr_home (FK on save ensure locker room in rink)
#     lr_away (FK on save ensure locker room in rink)
#     notes


# GameDuty
#     duty (choices=('Score Keeper', 'DJ', 'Referee', 'Beer'))
#     game (FK)
#     assignee (FK User, on save ensure user has ability e.g. is certified to ref, participates in drinks)


# GameEvent(abstract)
#     game (FK)
#     period (choices=1, 2, 3)
#     time
#     team (FK TeamSeason, on save ensure team in game)
#     player (FK SeasonTeamPlayer, on save ensure player in game)
#     ice_location
#     notes


# Shot(GameEvent)
#     pass


# Goal(Shot)
#     pass


# Assist
#     goal (FK)
#     player (FK SeasonTeamPlayer)


# Penalty(GameEvent)
#     penalty_type
#     length


# GameStar
#     game (FK)
#     star_level (choices=(1, 2, 3))
#     player (FK SeasonTeamPlayer on save ensure player in game)


# GameAttendance
#     game (FK)
#     player (FK SeasonTeamPlayer)
#     attendance (choices=in, tentative, out)


# SubRequest
#     game (FK)
#     team (FK SeasonTeam)
#     player_out (FK SeasonTeamPlayer)
#     player_in (FK SeasonSubstitute)
#     requested_at (datetime)
#     requested_by (FK SeasonTeamPlayer, limit to player out's teammates)
#     decision (choices=null, approved, denied)
#     decision_at (datetime)
#     decision_by (FK SeasonTeamPlayer, limit to player out's opposing team players)
