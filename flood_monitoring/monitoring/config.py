# config.py

# API Configuration
API_BASE_URL      = "https://environment.data.gov.uk"
STATIONS_ENDPOINT = f"{API_BASE_URL}/flood-monitoring/id/stations"

def get_readings_endpoint(station_id):
    return f"{STATIONS_ENDPOINT}/{station_id}/readings?_sorted"