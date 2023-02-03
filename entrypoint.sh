#!/bin/sh
python manage.py collectstatic --noinput
python manage.py makemigration --noinput
python manage.py migrate
python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@mvfp.com', 'admin')" | python manage.py shell
python manage.py runserver 0.0.0.0:80