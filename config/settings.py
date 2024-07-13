import os

# Discord settings
BOT_PREFIX = "!"

# DIrectory structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_LOGS = os.path.join(BASE_DIR, 'logs')
DIR_COGS = os.path.join(BASE_DIR, 'bot', 'cogs')
DIR_UTILS = os.path.join(BASE_DIR, 'bot', 'utils')
DIR_CONFIG = os.path.join(BASE_DIR, 'config')
DIR_TESTS = os.path.join(BASE_DIR, 'tests')