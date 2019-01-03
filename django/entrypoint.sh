#!/bin/bash

while ! nc -w 1 -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

python manage.py check
python manage.py collectstatic --no-input
python manage.py migrate --no-input
# python manage.py loaddata data.json

/usr/local/bin/gunicorn main.wsgi:application -w 2 -b :8000 --reload
