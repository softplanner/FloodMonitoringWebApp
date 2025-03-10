from monitoring.model.readingModel import ReadingModel

readingModel = ReadingModel()
class ReadingService:
    def get_station_readings(self, station_id):
        response = readingModel.get_station_readings(station_id)
        # TODO: get 24 hour data only
        return response
        
        
        
    