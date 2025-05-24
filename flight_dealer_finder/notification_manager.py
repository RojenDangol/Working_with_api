import smtplib

from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_PASSWORD']


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid ,auth_token)

    def send_msg(self, message):
        message = self.client.messages.create(
            body=message,
            from_=os.environ['TWILIO_NUMBER'],
            to=os.environ['TWILIO_AUTH_NUMBER']
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                                    )