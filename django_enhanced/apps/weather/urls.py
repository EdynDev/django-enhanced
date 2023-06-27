from django.urls import path
from .views import WeatherListView, CityListView, CityListViewV2


urlpatterns = [
    path('v1/city/', CityListView.as_view(), name='city'),
]
