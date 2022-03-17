#!/bin/sh 
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (ls ; cd Host_Pathogen_Interaction; python manage.py createsuperuser --no-input)
fi
(cd Host_Pathogen_Interaction; gunicorn Host_Pathogen_Interaction.wsgi:application  --bind 0.0.0.0:8000 ) &
nginx -g "daemon off;"