#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 236. SMS With Python

# https://www.twilio.com/
# https://www.twilio.com/docs/sms/quickstart/python?code-sample=code-send-an-sms-using-twilio&code-language=Python&code-sdk-version=6.x

# pip install twilio
from twilio.rest import Client
import time


# twilio-api.keys has the following format
# Phone Number:+11234567890
# Account Sid:ACXXXXXXXXXXXXXXXXXXXXXXXXXX
# Auth Token:xxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_KEYS = '/home/alex/.ssh/twilio-api.keys'

# Replace with the phone number you authorized in Twilio
PHONE_TO='+19876543219'

def api_secret(key):
    """ Return Twilio API secrets. Allowed requests are:
    'Phone Number', 'Account Sid', 'Auth Token'"""
    with open(TWILIO_KEYS, 'r') as reader:
        while (line := reader.readline().strip()) != '':
            api_key, secret = line.split(':')
            if key == api_key:
                return secret
        return None

account_sid = api_secret('Account Sid')
auth_token = api_secret('Auth Token')
phone_from = api_secret('Phone Number')

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi There!\nThis is Hello from Python!",
                     from_=phone_from,
                     to=PHONE_TO
                 )

print(message.sid)
