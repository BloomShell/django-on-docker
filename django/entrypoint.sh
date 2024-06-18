#!/bin/sh

# Simple migrations of the /app database
python manage.py migrate --no-input

# Apps migrations
python manage.py makemigrations public --no-input

# run django server using 'gunicorn' instead of 'manage.py runserver'
gunicorn django_website.wsgi:application --bind 0.0.0.0:8000