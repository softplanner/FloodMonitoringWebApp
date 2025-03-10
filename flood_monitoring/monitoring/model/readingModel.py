from django.db import models
import requests
from monitoring.utils import Utils
import logging
from monitoring.constants import JSON_ERROR, SERVICE_RESPONSE_ERROR

logger = logging.getLogger(__name__) 

class ReadingModel:      
    def get_station_readings(self, station_id):
        try:
            logger.info(Utils.get_readings_endpoint(station_id))
            response = requests.get(Utils.get_readings_endpoint(station_id))
            response.raise_for_status()
            return response.json().get('items', []) 
        except requests.exceptions.RequestException as e:
            logger.error(f"{SERVICE_RESPONSE_ERROR}: {e}")
            return [] 
        except ValueError as e:
            logger.error(f"{JSON_ERROR} {e}")
            return [] 
        
        
        
        
    