#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file"
    touch .env
    echo "BOT_SECRETS_TOKEN=your_token_here" >> .env
    echo "LOG_FILE=bot.log" >> .env
    echo "LOG_LEVEL=INFO" >> .env
    echo "Please update the .env file with your actual token."
fi