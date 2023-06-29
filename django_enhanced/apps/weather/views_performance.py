from rest_framework.views import APIView
from .models import Weather, City
from .serializers import WeatherSerializer, CitySerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.db.models import Prefetch

import time

class PerformanceV1(APIView):
    def get(self, request):
        print("GET>>>>>>>>>>>>>>>>")

        global serializer_time
        global db_time

        db_start = time.time()
        weather = Weather.objects.all()
        db_time = time.time() - db_start

        serializer_start = time.time()
        serializer = WeatherSerializer(instance=weather, many=True)
        data = serializer.data
        serializer_time = time.time() - serializer_start
        return Response(data)

    def dispatch(self, request, *args, **kwargs):
        print("DISPATCH>>>>>>>>>>>>")
        global dispatch_time
        global render_time

        dispatch_start = time.time()
        ret = super(PerformanceV1, self).dispatch(request, *args, **kwargs)

        render_start = time.time()
        ret.render()
        render_time = time.time() - render_start

        dispatch_time = time.time() - dispatch_start
        return ret


class PerformanceV2(APIView):
    def get(self, request):
        print("GET2>>>>>>>>>>>>>>>>")

        global serializer_time
        global db_time

        db_start = time.time()
        data = Weather.objects.values(
            'id', 'formatted_date', 'summary', 'precip_type', 'temperature_c', 'apparent_temperature_c', 'humity', 'wind_speed', 'wind_bearing', \
            'visibility', 'loud_cover', 'pressure', 'daily_summary', 'city'
        )
        db_time = time.time() - db_start
        serializer_time = 0
        return Response(data)

    def dispatch(self, request, *args, **kwargs):
        print("DISPATCH2>>>>>>>>>>>>")
        global dispatch_time
        global render_time

        dispatch_start = time.time()
        ret = super(PerformanceV2, self).dispatch(request, *args, **kwargs)

        render_start = time.time()
        ret.render()
        render_time = time.time() - render_start
        dispatch_time = time.time() - dispatch_start
        return ret

"""
from django.core.signals import request_started, request_finished
from django.dispatch import receiver

@receiver(request_started)
def started(sender, **kwargs):
    print("STARTED>>>>>>>>>>>>>>>>>>>")
    global started_time
    started_time = time.time()

@receiver(request_finished)
def finished(sender, **kwargs):
    print("FINISHED>>>>>>>>>>>>>>>>")
    try:
        total = time.time() - started_time
        api_view_time = dispatch_time - (render_time + serializer_time + db_time)
        request_response_time = total - dispatch_time

        print("Database lookup               | %.10fs" % db_time)
        print("Serialization                 | %.10fs" % serializer_time)
        print("Django request/response       | %.10fs" % request_response_time)
        print("API view                      | %.10fs" % api_view_time)
        print("Response rendering            | %.10fs" % render_time)
        
    except Exception as e:
        # print("exception", e)
        pass
"""
