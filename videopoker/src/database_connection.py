import sqlite3
DATABASE_FILE_PATH = "game_database.sqlite"

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
