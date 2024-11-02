import os
import logging

from dotenv import load_dotenv
from twilio.rest import Client

from module.ssm_utils import *

# Initialize Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Set the handler level

# Add the handler to the logger
logger.addHandler(console_handler)

# Load the .env file
load_dotenv()

twilio_account_sid = get_parameter(os.environ['TWILIO_ACCOUNT_SID_SSM_NAME'])
twilio_auth_token = get_parameter(os.environ['TWILIO_AUTH_TOKEN_SSM_NAME'])

if Config.TWILIO_SANDBOX == True:
    twilio_number = get_parameter(os.environ['TWILIO_SANDBOX_NUMBER_SSM_NAME'])
else:
    twilio_number = get_parameter(os.environ['TWILIO_NUMBER_SSM_NAME'])

# Initialize Twilio Client
client = Client(twilio_account_sid, twilio_auth_token)

# Send a WhatsApp message

# Temporary number
jh_number = os.environ['JH_NUMBER']

message = client.messages.create(
    body='Hello, this is a test message from Twilio!',  # The message you want to send
    from_=f'whatsapp:{twilio_number}',  # Your Twilio WhatsApp number
    to=f'whatsapp:{jh_number}'  # The recipient's phone number (must include the 'whatsapp:' prefix)
)
