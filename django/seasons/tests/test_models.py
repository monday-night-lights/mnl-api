from datetime import date

from django.test import TestCase

from seasons.models import Season


class SeasonsModelsTestCase(TestCase):

    def setUp(self):
        Season.objects.create(start_date=date(year=2016, month=10, day=1),
                              end_date=date(year=2016, month=3, day=31))

    def test_season_str(self):
        first_season = Season.objects.first()
        self.assertEqual(str(first_season), 'Fall 2016')
