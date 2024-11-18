#!/bin/bash

ZIP_FILE="../rn_twilio_messanger.zip"

echo "Deleting existing zip file (if any)..."
if [ -f "$ZIP_FILE" ]; then
    rm "$ZIP_FILE"
    echo "Deleted $ZIP_FILE"
else
    echo "No zip file to delete"
fi

echo "Creating new zip file..."
cd ..
zip -r "$ZIP_FILE" src
echo "Zip file created: $ZIP_FILE"