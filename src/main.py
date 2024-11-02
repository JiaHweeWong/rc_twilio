import os

from dotenv import load_dotenv
from twilio.rest import Client

from module.ssm_utils import *

# Load the .env file
load_dotenv()

twilio_account_sid = get_parameter(os.environ['TWILIO_ACCOUNT_SID_SSM_NAME'])
twilio_auth_token = get_parameter(os.environ['TWILIO_AUTH_TOKEN_SSM_NAME'])

# Initialize Twilio Client
client = Client(twilio_account_sid, twilio_auth_token)