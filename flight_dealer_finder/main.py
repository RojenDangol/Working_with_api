import requests
from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destinaion_data()


for row in sheet_data:
    if row['iataCode'] == "":
        flight_search = FlightSearch()
        row['iataCode'] = flight_search.get_destination_code()

        # data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()


