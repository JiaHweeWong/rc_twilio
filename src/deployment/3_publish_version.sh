#!/bin/bash

LAMBDA_NAME="rn_twilio_messenger"

echo "Publishing new version for Lambda function: $LAMBDA_NAME"

aws lambda publish-version \
    --function-name "$LAMBDA_NAME"

if [ $? -eq 0 ]; then
    echo "Successfully published a new version of $LAMBDA_NAME"
else
    echo "Failed to publish a new version"
    exit 1
fi