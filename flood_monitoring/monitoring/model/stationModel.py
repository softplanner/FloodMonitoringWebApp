from django.db import models
import requests
from monitoring.config import STATIONS_ENDPOINT
import logging

logger = logging.getLogger(__name__) 

class StationModel:
    def get_stations(self):
        try:
            logger.info(STATIONS_ENDPOINT)
            response = requests.get(STATIONS_ENDPOINT)
            response.raise_for_status()  
            return response.json().get('items', [])
        except requests.exceptions.RequestException as e: 
            print(f"Error in fetching stations: {e}")
            return [] 
        except ValueError as e:  
            print(f"Error in parsing JSON: {e}")
            return [] 
        
        
    