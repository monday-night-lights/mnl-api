from django.db import models
from django.utils.timezone import now

from .utils import season_str


class Season(models.Model):
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)

    def __str__(self):
        return '{str} {year}'.format(str=season_str(self.start_date),
                                     year=self.start_date.year)


# Draft
# season (FK)
# datetime
# venue (FK)
#
# Pick
# draft (FK)
# number
# team (FK=TeamSeason)
# player (FK)
# notes
