from datetime import date

from django.test import TestCase
from psycopg2.extras import DateRange

from seasons.models import Season, Team


class SeasonModelTestCase(TestCase):

    def setUp(self):
        Season.objects.create(duration=DateRange(
            date(year=2016, month=10, day=1),
            date(year=2017, month=3, day=31)))

    def test_season_str(self):
        first_season = Season.objects.first()
        self.assertEqual(str(first_season), 'Fall 2016')



class TeamModelTestCase(TestCase):

    def test_team_model(self):
        Team.objects.create(name='Americans', color_1='#E03A3E', color_2='#0060A9')
        Team.objects.create(name='Golden Seals', color_1='#FBB838', color_2='#149471')
        Team.objects.create(name='Mighty Ducks', color_1='#006A65', color_2='#FDB827', color_3='#51334B')
        Team.objects.create(name='Nordiques', color_1='#127DB8', color_2='#E11939')
        Team.objects.create(name='North Stars', color_1='#108349', color_2='#FBB838')
        Team.objects.create(name='Whalers', color_1='#0E7B22', color_2='#13207A', color_3='#C8CFC8')
