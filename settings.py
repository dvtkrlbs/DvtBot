from dotenv import load_dotenv
from os import getenv

load_dotenv()

DISCORD_TOKEN = getenv('DISCORD_BOT_TOKEN')
LOG_CHANNEL = getenv('LOG_CHANNEL')
