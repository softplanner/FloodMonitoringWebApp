from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.get_data, name='get_data'),
    path('', views.flood_monitoring, name='flood_monitoring'),  # Main page
    path('stations/', views.get_stations, name='get_stations'),
    path('readings/<str:station_id>/', views.get_station_readings, name='get_station_readings'),  # API for readings
]