class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.all_flight_details = []
        self.stop_overs = 0
        self.via_city = ""

    def structure_data(self, flight):
        departure_date_unformatted = flight["data"][0]["route"][0]["local_departure"].split("T")
        departure_date = departure_date_unformatted[0].split("-")
        return_date_unformatted = flight["data"][0]["route"][1]["local_departure"].split("T")
        return_date = return_date_unformatted[0].split("-")
        flight_details = {
            "departure city": flight["data"][0]["cityFrom"],
            "departure airport code": flight["data"][0]["flyFrom"],
            "destination city": flight["data"][0]["cityTo"],
            "destination airport code": flight["data"][0]["flyTo"],
            "price": flight["data"][0]["price"],
            "departure date": f"{departure_date[2]}/{departure_date[1]}/{departure_date[0]}",
            "return date": f"{return_date[2]}/{return_date[1]}/{return_date[0]}"
        }
        self.all_flight_details.append(flight_details)
        return flight_details

