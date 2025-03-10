from monitoring.config import STATIONS_ENDPOINT

class Utils:    
    @staticmethod
    def get_readings_endpoint(station_id):
        return f"{STATIONS_ENDPOINT}/{station_id}/readings?_sorted&_limit=96"