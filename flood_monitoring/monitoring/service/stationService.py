from monitoring.model.stationModel import StationModel

stationModel = StationModel()
class StationService:
    def get_stations(self):
        return stationModel.get_stations()    
        
        
    