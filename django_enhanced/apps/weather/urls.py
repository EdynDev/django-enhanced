from django.urls import path
from .views import CityListView, CityListView2
from .views_performance import PerformanceV1, PerformanceV2


urlpatterns = [
    path('v1/city/', CityListView.as_view(), name='city'),
    path('v2/city/', CityListView2.as_view(), name='cityv2'),
    path('v1/performance/', PerformanceV1.as_view(), name='performancev1'),
    path('v2/performance/', PerformanceV2.as_view(), name='performancev2'),
]

from decouple import config

if config('REDIS', False):
    from .views_cache import WeatherListView
    urlpatterns += [path('cache/', WeatherListView.as_view(), name='weather-cache'),]
