import requests

SHEETY_ENDPOINTS = "https://api.sheety.co/914e5a5a7d2cfc66eaae6dbbe361726f/flightDeals/prices"
GOOGLE_SHEET_NAME = "price"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destinaion_data(self):
        response = requests.get(SHEETY_ENDPOINTS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:

            city_id = city['id']
            sheet_param = {
                GOOGLE_SHEET_NAME: {
                    "iataCode": city['iataCode']
                }
            }

            sheety_response = requests.put(f"{SHEETY_ENDPOINTS}/{city_id}", json=sheet_param)

            print(sheety_response.text)