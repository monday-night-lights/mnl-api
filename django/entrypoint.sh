#!/bin/bash

python manage.py check
python manage.py collectstatic --no-input
python manage.py migrate --no-input
python manage.py loaddata seasons/data/teams.json

/usr/local/bin/gunicorn main.wsgi:application -w 2 -b :8000 --reload
