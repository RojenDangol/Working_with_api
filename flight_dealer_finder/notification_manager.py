from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


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