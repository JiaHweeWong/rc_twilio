import boto3

from config import Config

ssm = boto3.client('ssm', region_name=Config.AWS_REGION)

def get_parameter(name):
    response = ssm.get_parameter(Name=name, WithDecryption=True)
    return response['Parameter']['Value']