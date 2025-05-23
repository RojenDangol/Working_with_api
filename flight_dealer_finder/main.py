import requests
from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destinaion_data()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LON"

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    if flight is not None and float(flight.price) > 0:
        if float(flight.price) < float(destination["lowestPrice"]):
            notification_manager.send_msg(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-"
                        f"{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.out_date} to {flight.return_date}."
            )


