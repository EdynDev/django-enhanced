from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Weather, City
from .serializers import WeatherSerializer, CitySerializer
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from django.db.models import Prefetch

import time


class CityListView(APIView):

    def get(self, request):
        start_time = time.time()
        queryset = City.objects.all()
        serializer = CitySerializer(instance=queryset, many=True)
        duration = time.time() - start_time
        response = Response(serializer.data, status=HTTP_200_OK)
        response["X-total-time-RequestMiddlewareInternal"] = "%.10fs" % duration
        return response


class CityListView2(ListAPIView):

    def get(self, request):
        start_time = time.time()
        queryset = City.objects.all().prefetch_related(Prefetch('weathers'))
        serializer = CitySerializer(instance=queryset, many=True)
        duration = time.time() - start_time
        response = Response(serializer.data, status=HTTP_200_OK)
        response["X-total-time-RequestMiddlewareInternal"] = "%.10fs" % duration
        return response