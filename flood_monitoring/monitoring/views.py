from django.shortcuts import render
from .models import Stations 
from django.http import JsonResponse
from .utils import Utils 

# view to get the list of stations and return as a JSON response
def get_stations(request):
    try:
        print("in get_stations views")
        stations = Stations.get_stations()

        # Utils.processResponse(stations)

        # print(stations.items)
        response = {"data": {"items": stations}}

        

        return JsonResponse(response)
        # return JsonResponse(stations, safe=False) # safe = False: allow non-dictionary objects to be serialized into JSON
    except Exception as e:
        print(f"Error in get_stations view: {e}")
        return JsonResponse({"An error accured in view get_station(): "}, status = 500)
    
# view to fetch the readings for a specific station using station ID
def get_station_readings(request, station_id):
# def get_station_readings(request):
    try:
        # station_id = request.GET.get('station_id', None)
        print("in get_station_readings views: station id: ", station_id)
        station_readings = Stations.get_station_readings(station_id)
        response = {"data": {"items": station_readings}}
        # return JsonResponse(station_readings, safe=False) # safe = False: allow non-dictionary objects to be serialized into JSON
        return JsonResponse(response)
    except Exception as e:
        print(f"Error in get_station_readings view: {e}")
        return JsonResponse({"An error accured in view get_station_readings(): "}, status = 500)
    
# view to render the main page for flood monitoring web app
def home(request):
    return render(request, 'home.html')   
