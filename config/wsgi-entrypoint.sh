#!/bin/sh

until cd /config
do
  echo 'Waiting'
done

until ./config/manage.py makemigrations
      ./config/manage.py migrate
do
  echo 'Waiting DB'
  sleep 2
done

./config/manage.py collectstatic --noinput

gunicorn config.wsgi --bind 0.0.0.0:8080 --workers 4 --threads 4
