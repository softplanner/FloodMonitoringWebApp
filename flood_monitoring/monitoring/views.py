from django.shortcuts import render
from monitoring.service.stationService import StationService 
from monitoring.service.readingService import ReadingService 
from django.http import JsonResponse
import logging
from monitoring.constants import GENERIC_ERROR

logger = logging.getLogger(__name__)  # Get a logger for the current module.

stationService = StationService() 
readingService = ReadingService()

def get_stations(request):
    try:
        stations = stationService.get_stations()
        response = {"data": {"items": stations}}      
        return JsonResponse(response, safe=False)
    except Exception as e:
        logger.error(f"{GENERIC_ERROR} : {e}")
        return JsonResponse({"An error accured in view get_station(): "}, status = 500)
    
def get_station_readings(request, station_id):
    try:
        station_readings = readingService.get_station_readings(station_id)
        response = {"data": {"items": station_readings}}
        return JsonResponse(response, safe=False)
    except Exception as e:
        logger.error(f"{GENERIC_ERROR} : {e}")
        return JsonResponse({"An error accured in view get_station_readings(): "}, status = 500)
    
def home(request):
    return render(request, 'home.html')   
