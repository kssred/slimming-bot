from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).parent.parent.resolve()

TGBOT_TOKEN = getenv("TGBOT_TOKEN")
