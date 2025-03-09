from django.urls import path
from . import views

urlpatterns = [
    path('', views.flood_monitoring, name='flood_monitoring'),  # Main page
    path('readings/<str:station_id>/', views.get_station_readings, name='get_station_readings'),  # API for readings
]