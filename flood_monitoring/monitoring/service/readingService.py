from monitoring.model.readingModel import ReadingModel

readingModel = ReadingModel()
class ReadingService:
    def get_station_readings(self, station_id):
        return readingModel.get_station_readings(station_id)
        
        
        
    