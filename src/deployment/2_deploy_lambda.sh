#!/bin/bash

LAMBDA_NAME="rn_twilio_messenger"
ZIP_FILE="../rn_twilio_messenger.zip"

echo "Deploying Lambda function: $LAMBDA_NAME"

aws lambda update-function-code \
    --function-name "$LAMBDA_NAME" \
    --zip-file "fileb://$ZIP_FILE"

if [ $? -eq 0 ]; then
    echo "Successfully deployed $LAMBDA_NAME"
else
    echo "Failed to deploy $LAMBDA_NAME"
    exit 1
fi

echo "Deleting existing zip file (if any)..."
if [ -f "$ZIP_FILE" ]; then
    rm "$ZIP_FILE"
    echo "Deleted $ZIP_FILE"
else
    echo "No zip file to delete"
fi