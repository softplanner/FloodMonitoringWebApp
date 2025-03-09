from django.db import models
import requests

class Stations(models.Model):
    # Fields to store station information temporarily (used for mimicking real models)
    station_id   = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=255)

    # Prevent Django from creating a database table for this model
    class Meta:
        managed = False  # This tells Django to ignore database management for this model

    # Static method to get all stations from the API
    @staticmethod
    def get_stations():
        try:
            url = "https://environment.data.gov.uk/flood-monitoring/api/stations" # API URL to get all stations
            # Fetch data from the API
            response = requests.get(url)
             # Raise an exception if the status code indicates failure (e.g., 404, 500)
            response.raise_for_status()  
            # Return the list of all stations 
            return response.json().get('items', [])
        except requests.exceptions.RequestException as e: 
            # Handle requests-related exceptions
            print(f"Error in fetching stations: {e}")
            return [] # Return an empty list if somethig wrong
        except ValueError as e:  
            # Handle JSON parsing errors 
            print(f"Error in parsing JSON: {e}")
            return [] # Return an empty list if JSON parsing fails
        
    # static method to fetch readings for a specific station based on its station ID
    @staticmethod
    def get_readings(station_id):
        try:
            url = f"https://environment.data.gov.uk/flood-monitoring/api/readings?stationReference={station_id}"  # API URL to fetch readings
            # Fetch data from the API
            response = requests.get(url)
            # Raise an exception if the status code indicates failure (e.g., 404, 500)
            response.raise_for_status()
            # Return the reading list fetched for the specific station
            return response.json().get('items', []) 
        except requests.exceptions.RequestException as e: # Handle request related exceptions 
            print(f"Error in fetching readings for station {station_id}: {e}")
            return [] # Return an empty list if somethig wrong
        except ValueError as e: # Handle JSON parsing erros
            print(f"Error in parsing JSON: {e}")
            return [] # Return an empty list if JSON parsing fails
        
        
        
        
    