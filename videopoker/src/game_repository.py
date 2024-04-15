from database_connection import get_database_connection
from game import Game
from hand_value import HandValue


def get_game_by_row(row):
    return Game(row["id"], row["name"], row["note"]) if row else None


def get_pay_out_by_row(row):
    return (HandValue(row["hand"]), row["payout"]) if row else None


class GameRepository:

    def __init__(self, connection):

        self.__connection = connection

    def find_games(self):

        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM games")
        rows = cursor.fetchall()

        return list(map(get_game_by_row, rows))

    def get_pay_table(self, game_id: int):

        cursor = self.__connection.cursor()
        cursor.execute(
            "SELECT hand, payout FROM pay_tables WHERE game_id = ?", (game_id,))
        rows = cursor.fetchall()

        return list(map(get_pay_out_by_row, rows))


game_repository = GameRepository(get_database_connection())
