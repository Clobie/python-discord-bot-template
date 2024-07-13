@echo off

REM Load environment variables from .env file if exists
if exist .env (
    for /f "tokens=*" %%i in (.env) do set %%i
)

REM Activate virtual environment if exists
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

REM Run the bot
python bot\main.py
