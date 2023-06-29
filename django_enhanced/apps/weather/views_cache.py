from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from .serializers import WeatherSerializer
from .models import Weather
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

class WeatherListView(APIView):

    @method_decorator(cache_page(60*15))
    def get(self, request):
        weather = Weather.objects.all()
        serializer = WeatherSerializer(instance=weather, many=True)
        return Response(serializer.data, HTTP_200_OK)
