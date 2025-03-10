from django.db import models
import requests
from monitoring.config import STATIONS_ENDPOINT
import logging
from monitoring.constants import JSON_ERROR, SERVICE_RESPONSE_ERROR
logger = logging.getLogger(__name__) 

class StationModel:
    def get_stations(self):
        try:
            logger.info(STATIONS_ENDPOINT)
            response = requests.get(STATIONS_ENDPOINT)
            response.raise_for_status()  
            return response.json().get('items', [])
        except requests.exceptions.RequestException as e: 
            logger.error(f"{SERVICE_RESPONSE_ERROR}: {e}")
            return [] 
        except ValueError as e:  
            logger.error(f"{JSON_ERROR} {e}")
            return [] 
        
        
    