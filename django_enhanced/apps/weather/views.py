from rest_framework.generics import ListAPIView
from .models import Weather, City
from .serializers import WeatherSerializer, CitySerializer

import time


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
