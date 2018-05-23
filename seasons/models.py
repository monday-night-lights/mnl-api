from django.contrib.postgres.fields.ranges import DateRangeField#, DateTimeRangeField
from django.db import models
# from django.utils.functional import cached_property
# from django.utils.timezone import now

# from .fields import ChoiceArrayField
from .utils import season_str
# from personnel.models import Player
# from venues.models import Venue

# POSITION_CHOICES = (
#     ('LW', 'Left Wing'),
#     ('C',  'Center'),
#     ('RW', 'Right Wing'),
#     ('LD', 'Left Defenseman'),
#     ('RD', 'Right Defenseman'),
#     ('G',  'Goaltender')
# )


class Season(models.Model):
    duration = DateRangeField()

    def __str__(self):
        return '{str} {year}'.format(str=season_str(self.duration.lower),
                                     year=self.duration.lower.year)

#
# class SeasonPlayer(models.Model):
#     '''Player attributes that change season to season'''
#     season = models.ForeignKey(Season, on_delete=models.PROTECT, related_name='players')
#     player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='seasons')
#     projected_round = models.PositiveSmallIntegerField()
#     participates_in_drinks = models.BooleanField(default=True)
#
#
# class SeasonSubstitute(SeasonPlayer):
#     positions = ChoiceArrayField(
#         models.CharField(max_length=2, choices=POSITION_CHOICES))
#
#
# class Team(models.Model):
#     '''Team attributes that carry over season to season'''
#     name = models.CharField(max_length=20, unique=True)
#     # logo = models.ImageField(upload_to=logo_upload_to)
#     # goal_horn = models.FileField(upload_to=goal_horn_upload_to)
#
#
# class SeasonTeam (models.Model):
#     '''Team attributes that change season to season'''
#     season = models.ForeignKey(Season, on_delete=models.PROTECT, related_name='teams')
#     team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='seasons')
#     gm = models.ForeignKey(SeasonPlayer, on_delete=models.PROTECT, related_name='teams_gmed', )
#     asst_gm = models.ForeignKey(SeasonPlayer, on_delete=models.PROTECT, related_name='teams_asst_gmed', null=True, blank=True)
#     notes = models.TextField(blank=True)
#
#
# class Draft(models.Model):
#     season = models.OneToOneField(Season, on_delete=models.PROTECT)
#     datetime = models.DateTimeField(default=now)
#     # venue = models.ForeignKey(Venue)
#     notes = models.TextField(blank=True)
#
#     @cached_property
#     def team_count(self):
#         self.season.teams.count()
#
#     @cached_property
#     def player_count(self):
#         self.season.players.count()
#
#     @cached_property
#     def rounds(self):
#         return self.player_count() // self.team_count()
#
#
# class DraftPick(models.Model):
#     draft = models.ForeignKey(Draft, on_delete=models.PROTECT, related_name='picks')
#     pick = models.PositiveSmallIntegerField()
#     team = models.ForeignKey(SeasonTeam, on_delete=models.PROTECT, related_name='draft_picks')
#     player = models.ForeignKey(SeasonPlayer, on_delete=models.PROTECT, related_name='drafts')
#     notes = models.TextField(blank=True)
#
#     class Meta:
#         unique_together = (('draft', 'pick'), ('draft', 'player'),)
#
#     @cached_property
#     def round(self):
#         return round((self.pick - 1)/self.draft.rounds) + 1
#
#
# class SeasonTeamPlayer(models.Model):
#     '''Player attributes that change season to season, team to team'''
#     player = models.ForeignKey(SeasonPlayer, on_delete=models.PROTECT, related_name='teams')
#     team = models.ForeignKey(SeasonTeam, on_delete=models.PROTECT, related_name='players')
#     number = models.PositiveSmallIntegerField()
#     positions = ChoiceArrayField(
#         models.CharField(max_length=2, choices=POSITION_CHOICES))
#
#
# TradeGroup
#     date
#     notes
#
#
# Trade
#     group (FK)
#     player (FK SeasonPlayer)
#     from (FK SeasonTeam)
#     to (FK SeasonTeam)
