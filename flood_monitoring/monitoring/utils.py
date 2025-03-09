import json


class Utils:
    @staticmethod
    def processResponse(stations):
        # stations = json.load(response)
        if stations:
            for station in stations:
                print(f"Station ID: {station.get('stationReference', 'N/A')}")
                print(f"Station Name: {station.get('label', 'N/A')}")
                print(f"River Name: {station.get('riverName', 'N/A')}")
                print(f"Longitude: {station.get('long', 'N/A')}, Latitude: {station.get('lat', 'N/A')}")
                print("-" * 40)
        else:
            print("No stations found.")
    
