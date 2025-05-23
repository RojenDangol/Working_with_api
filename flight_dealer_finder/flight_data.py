class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def __str__(self):
        return (f"Price: {self.price} GBP | From: {self.origin_city} ({self.origin_airport}) "
                f"To: {self.destination_city} ({self.destination_airport}) | "
                f"Departure: {self.out_date} | Return: {self.return_date}")