import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "game_database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

PICTURES_DIRECTORY = os.path.join(dirname, "card_pictures")

GAME_EVENT_LOG_FILENAME = os.getenv("GAME_EVENT_LOG_FILENAME") or "game_event_log.log"
GAME_EVENT_LOG_FILE_PATH = os.path.join(
    dirname, "..", "logs", GAME_EVENT_LOG_FILENAME)
