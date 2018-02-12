from datetime import date

from django.test import TestCase
from psycopg2.extras import DateRange

from seasons.models import Season


class SeasonsModelsTestCase(TestCase):

    def setUp(self):
        Season.objects.create(duration=DateRange(
            date(year=2016, month=10, day=1),
            date(year=2017, month=3, day=31)))

    def test_season_str(self):
        first_season = Season.objects.first()
        self.assertEqual(str(first_season), 'Fall 2016')
