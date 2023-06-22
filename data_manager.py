import requests
import os

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_HEADER = {
    "Authorization": os.environ["SHEETY_TOKEN"]
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = SHEETY_ENDPOINT
        self.header = SHEETY_HEADER

    def get_price_cutoff(self):
        response = requests.get(url=self.endpoint, headers=self.header)
        prices = response.json()["prices"]
        return prices

    def update_sheet(self, data, row_id):
        endpoint = self.endpoint + "/" + str(row_id)
        params = {
            "price": {
                "iataCode": data,
            }
        }
        response = requests.put(url=endpoint, json=params, headers=self.header)

