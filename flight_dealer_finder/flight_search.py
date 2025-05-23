import requests
from datetime import datetime, timedelta
import random
from flight_data import FlightData
import json

import os
from dotenv import load_dotenv

load_dotenv()

AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_SEARCH_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
AMADEUS_API_KEY = os.environ['AMADEUS_API_KEY']
AMADEUS_SECRET = os.environ['AMADEUS_SECRET']


class FlightSearch:

    def __init__(self):
        self.token = self.get_access_token()

    def get_access_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_API_KEY,
            "client_secret": AMADEUS_SECRET
        }
        response = requests.post(url=AMADEUS_ENDPOINT, headers=headers, data=data)
        result = response.json()
        return result.get("access_token")

    def get_destination_code(self, city_name):
        location_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations"
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {
            "keyword": city_name,
            "subType": "AIRPORT,CITY"
        }
        response = requests.get(url=location_endpoint, headers=headers, params=params)
        data = response.json()
        try:
            code = data["data"][0]["iataCode"]
            return code
        except (KeyError, IndexError):
            return None

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        departure_date = from_time.strftime("%Y-%m-%d")
        return_date = (from_time + timedelta(days=random.randint(7, 28))).strftime("%Y-%m-%d")
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": 1
        }
        response = requests.get(AMADEUS_SEARCH_URL, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")
            return None

        data = response.json()
        if not data.get("data"):
            print(f"No flights found for {destination_city_code}.")
            return None

        offer = data["data"][0]
        out_segment = offer["itineraries"][0]["segments"][0]
        ret_segment = offer["itineraries"][1]["segments"][0]

        return FlightData(
            price=offer["price"]["total"],
            origin_city=out_segment["departure"]["iataCode"],
            origin_airport=out_segment["departure"]["iataCode"],
            destination_city=out_segment["arrival"]["iataCode"],
            destination_airport=out_segment["arrival"]["iataCode"],
            out_date=out_segment["departure"]["at"][:10],
            return_date=ret_segment["arrival"]["at"][:10]
        )


