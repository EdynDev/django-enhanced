#!/bin/sh

echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"
echo $SILK

PARAMETER_VALUE=""

if [ "$CPROFILE" = True ]; then
    PARAMETER_VALUE="cprofile"
elif [ "$DEBUG_TOOLBAR" = True ]; then
    PARAMETER_VALUE="toolbar"
elif [ "$SILK" = True ]; then
    PARAMETER_VALUE="silk"
elif [ "$REDIS" = True ]; then
    PARAMETER_VALUE="redis"
else
    echo "---->"
fi

python manage.py $PARAMETER_VALUE makemigrations
python manage.py $PARAMETER_VALUE migrate
python manage.py $PARAMETER_VALUE loaddata apps/weather/data/city.json
python manage.py $PARAMETER_VALUE shell < script.py
python manage.py $PARAMETER_VALUE createsuperuser --noinput

echo "DJANGO EXECUTE: $PARAMETER_VALUE"

exec "$@"