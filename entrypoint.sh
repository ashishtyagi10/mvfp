#!/bin/sh
python manage.py collectstatic --noinput
python manage.py makemigration --noinput
python manage.py migrate
DJANGO_SUPERUSER_PASSWORD = admin DJANGO_SUPERUSER_EMAIL = admin@admin.com DJANGO_SUPERUSER_USERNAME = admin python manage.py createsuperuser --noinput
python manage.py runserver 0.0.0.0:80