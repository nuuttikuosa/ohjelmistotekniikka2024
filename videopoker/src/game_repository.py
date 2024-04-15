from database_connection import get_database_connection


class GameRepository:

    def __init__(self, connection):

        self.__connection = connection

    def get_games(self):

        cursor = self.__connection.cursor()
        cursor.execute("SELECT name, note FROM games")
        rows = cursor.fetchall()

        return rows

    def get_pay_table(self, name):

        cursor = self.__connection.cursor()
        cursor.execute(
            "SELECT hand_type, pay FROM PayTables WHERE name = ?", (name,))
        rows = cursor.fetchall()

        return rows


game_repository = GameRepository(get_database_connection())
