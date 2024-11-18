import os
import logging

from dotenv import load_dotenv
from module.ssm_utils import *

# Add the 'lib' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from twilio.rest import Client

# Load the .env file
load_dotenv()

# Initialize Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# # Create a console handler
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)  # Set the handler level

# # Add the handler to the logger
# logger.addHandler(console_handler)

twilio_account_sid = get_parameter(os.environ['TWILIO_ACCOUNT_SID_SSM_NAME'])
twilio_auth_token = get_parameter(os.environ['TWILIO_AUTH_TOKEN_SSM_NAME'])

if Config.TWILIO_SANDBOX == True:
    twilio_number = get_parameter(os.environ['TWILIO_SANDBOX_NUMBER_SSM_NAME'])
else:
    twilio_number = get_parameter(os.environ['TWILIO_NUMBER_SSM_NAME'])

# Initialize Twilio Client
client = Client(twilio_account_sid, twilio_auth_token)

logger.info("Lambda Initialized")

# Send a WhatsApp message

def lambda_handler(event, context):

    try:

        # Log incoming event
        logger.info("Received event: %s", json.dumps(event))

        # Temporary number
        jh_number = os.environ['JH_NUMBER']

        logger.info("Sending message via Twilio client")

        message = client.messages.create(
            body='Hello, this is a test message from Twilio!',  # The message you want to send
            from_=f'whatsapp:{twilio_number}',  # Your Twilio WhatsApp number
            to=f'whatsapp:{jh_number}'  # The recipient's phone number (must include the 'whatsapp:' prefix)
        )

        logger.info("Message successfully sent.")

        return {
            "message" : "Invocation Successful",
            "statusCode" : "200"
        }
    
    except Exception as e:
        
        logger.info(e)

        return {
            "message" : str(e),
            "statusCode" : 400
        }


