import smtplib
import os


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.from_email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_PASSWORD"]

    def cheap_flight_notification(self, flight_details, max_price):
        if flight_details["price"] < max_price:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.from_email, password=self.password)
                connection.sendmail(
                    from_addr=self.from_email,
                    to_addrs=self.from_email,
                    msg=f"Subject: Low flight price alert!\n\n"
                        f"Only €{flight_details['price']} to fly from "
                        f"{flight_details['departure city']}-{flight_details['departure airport code']} to "
                        f"{flight_details['destination city']}-{flight_details['destination airport code']} from "
                        f"{flight_details['departure date']} to {flight_details['return date']}".encode("utf-8")
                )
