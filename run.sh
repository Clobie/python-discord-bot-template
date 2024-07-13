#!/bin/bash

# Load environment variables from .env file if exists
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# Activate virtual environment if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the bot
python bot/main.py