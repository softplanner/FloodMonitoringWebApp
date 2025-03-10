from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.home, name='home'),  # Main page
    path('stations/', views.get_stations, name='get_stations'),
    # path('readings/', views.get_station_readings, name='get_station_readings'),
    # re_path(r'^readings/(?P<station_id>\w+)/$', views.get_station_readings, name='get_station_readings'),
    path('readings/<str:station_id>/', views.get_station_readings, name='get_station_readings'),
]