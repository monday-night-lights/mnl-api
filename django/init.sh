#!/bin/bash

while ! nc -w 1 -z postgres 5432
do
  echo 'Waiting for postgres...'
  sleep 1
done

/venv/bin/python manage.py migrate --noinput
/venv/bin/python manage.py create_default_superuser
/venv/bin/python manage.py collectstatic --noinput

/venv/bin/gunicorn main.wsgi:application -w 2 -b :8000 --reload --timeout 20
