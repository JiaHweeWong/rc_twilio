#!/bin/bash

ZIP_FILE="deployment/rn_twilio_messenger.zip"

echo "Deleting existing zip file (if any)..."
if [ -f "$ZIP_FILE" ]; then
    rm "$ZIP_FILE"
    echo "Deleted $ZIP_FILE"
else
    echo "No zip file to delete"
fi

echo "Creating new zip file..."
zip -r "$ZIP_FILE" ./*
cd ..
echo "Zip file created: $ZIP_FILE"