from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name='Ciudad', max_length=60)
    code = models.IntegerField(verbose_name='Código postal')
    population = models.IntegerField(verbose_name='Población')

    def __str__(self):
        return self.name


class Weather(models.Model):
    formatted_date = models.DateTimeField(verbose_name='Formatted Date')
    summary = models.CharField(verbose_name='Summary', max_length=120)
    precip_type = models.CharField(verbose_name='Precip Type', max_length=260)
    temperature_c = models.FloatField(verbose_name='Temperature (C)')
    apparent_temperature_c = models.FloatField(verbose_name='Apparent Temperature (C)')
    humity = models.FloatField(verbose_name='Humity')
    wind_speed = models.FloatField(verbose_name='Wind Speed (km/h)')
    wind_bearing = models.FloatField(verbose_name='Wind Bearing (degrees)')
    visibility = models.FloatField(verbose_name='Visibility')
    loud_cover = models.IntegerField(verbose_name='Loud Cover')
    pressure = models.FloatField(verbose_name='Pressure (millibars)')
    daily_summary = models.CharField(verbose_name='Daily Summary', max_length=260)
    city = models.ForeignKey(City, related_name='weathers', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.daily_summary
