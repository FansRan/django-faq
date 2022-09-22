#!/usr/bin/env bash
# start server
(cd faq; python manage.py migrate)
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd faq; python manage.py createsuperuser --no-input)
fi
(cd faq; python manage.py collectstatic)
(cd faq; gunicorn devngo_django.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3) &
nginx -g "daemon off;"