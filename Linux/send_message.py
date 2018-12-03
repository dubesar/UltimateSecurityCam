from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
def send message
    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body='Someones Detected',
            from_='+15017122661',
            to='+15558675310'
        )

    print(message.sid)
