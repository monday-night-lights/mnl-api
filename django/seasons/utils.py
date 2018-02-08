from datetime import date, datetime

leap_year = 2000
seasons = [('Winter', (date(leap_year,  1,  1),  date(leap_year,  3, 20))),
           ('Spring', (date(leap_year,  3, 21),  date(leap_year,  6, 20))),
           ('Summer', (date(leap_year,  6, 21),  date(leap_year,  9, 22))),
           ('Fall',   (date(leap_year,  9, 23),  date(leap_year, 12, 20))),
           ('Winter', (date(leap_year, 12, 21),  date(leap_year, 12, 31)))]

def season_str(dt):
    if isinstance(dt, datetime):
        dt = dt.date()
    dt = dt.replace(year=leap_year)
    return next(season for season, (start, end) in seasons
                if start <= dt <= end)
