import requests
import os
from datetime import datetime, timedelta

KIWI_ENDPOINT = "https://api.tequila.kiwi.com"
API_KEY = os.environ["KIWI_API_KEY"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = KIWI_ENDPOINT
        self.header = {"apikey": API_KEY}

    def get_iata_code(self, city_name):
        endpoint = self.endpoint + "/locations/query"
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=endpoint, params=params, headers=self.header)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def find_cheap_flight(self, city_code):
        endpoint = self.endpoint + "/v2/search"
        start_date = datetime.now() + timedelta(days=1)
        end_date = datetime.now() + timedelta(days=180)
        params = {
            "fly_from": "LON",
            "fly_to": city_code,
            "date_from": start_date.strftime("%d/%m/%Y"),
            "date_to": end_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "one_for_city": 1
        }
        response = requests.get(url=endpoint, params=params, headers=self.header)
        response.raise_for_status()
        return response.json()

