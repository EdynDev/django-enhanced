from apps.weather.models import Weather, City
import random

from django.db import connection

with connection.cursor() as cursor:
    copy_sql = """
    COPY weather_weather (formatted_date, summary, precip_type, temperature_c, apparent_temperature_c, humity, wind_speed, wind_bearing, visibility, loud_cover, pressure, daily_summary) 
    FROM '/home/server/backups/weatherHistory2.csv' DELIMITER ',' CSV HEADER;
    """
    print("copy_sql", copy_sql)
    cursor.execute(copy_sql)


list_city = City.objects.all() 

list_weather = Weather.objects.all()[:100]
for i, obj_weather in enumerate(list_weather):
    print(i)
    n = random.randrange(list_city.count() - 1)
    obj_weather.city = list_city[n]
    obj_weather.save()
