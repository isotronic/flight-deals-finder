import smtplib
import os
import requests



class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.from_email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_PASSWORD"]
        self.sheety_endpoint = os.environ["SHEETY_ENDPOINT"] + "users"
        self.sheety_header = {"Authorization": os.environ["SHEETY_TOKEN"]}

    def cheap_flight_notification(self, flight_details, max_price):
        if flight_details["price"] < max_price:
            response = requests.get(url=self.sheety_endpoint, headers=self.sheety_header)
            all_users = response.json()
            for user in all_users:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=self.from_email, password=self.password)
                    connection.sendmail(
                        from_addr=self.from_email,
                        to_addrs=user["email"],
                        msg=f"Subject: Low flight price alert!\n\n"
                            f"Hi {user['firstName']},\n\n"
                            f"Only €{flight_details['price']} to fly from "
                            f"{flight_details['departure city']}-{flight_details['departure airport code']} to "
                            f"{flight_details['destination city']}-{flight_details['destination airport code']} from "
                            f"{flight_details['departure date']} to {flight_details['return date']}".encode("utf-8")
                    )
