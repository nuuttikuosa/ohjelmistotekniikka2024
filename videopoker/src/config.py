import os

dirname = os.path.dirname(__file__)

DATABASE_FILENAME = "game_database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
PICTURES_DIRECTORY = os.path.join(dirname, "card_pictures")
GAME_EVENT_LOG_FILENAME = "game_event_log.log"
GAME_EVENT_LOG_FILE_PATH = os.path.join(
    dirname, "..", "logs", GAME_EVENT_LOG_FILENAME)
