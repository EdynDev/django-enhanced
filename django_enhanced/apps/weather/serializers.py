from .models import Weather, City
from rest_framework import serializers

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    weathers = WeatherSerializer(many=True)

    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'weathers'
        ) 

