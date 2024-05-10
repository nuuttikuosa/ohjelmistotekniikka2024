from database_connection import get_database_connection
from entities.game import Game
from entities.hand_value import HandValue
from entities.payout_table import PayoutTable

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

        payout_table = PayoutTable()

        for row in rows:
           payout_table.add_payout(row[0], row[1])

        return payout_table

    def get_game(self, game_id: int):

        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM games WHERE id = ?", (game_id,))
        row = cursor.fetchone()

        game = Game(row["id"], row["name"], row["note"])

        game.set_payout_table(self.get_pay_table(game_id))

        return game


    def delete_all(self):
        """Poistaa kaikki pelikonfiguraatiot.
        """

        cursor = self.__connection.cursor()

        cursor.execute("DELETE FROM pay_tables")
        cursor.execute("DELETE FROM games")

        self.__connection.commit()


game_repository = GameRepository(get_database_connection())
