#!/bin/sh
python manage.py collectstatic --noinput
python manage.py makemigration --noinput
python manage.py migrate
python manage.py syncdb --noinput
python manage.py runserver 0.0.0.0:80