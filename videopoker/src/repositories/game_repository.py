from database_connection import get_database_connection
from entities.game import Game
from entities.payout_table import PayoutTable


def get_game_by_row(row):
    return Game(row["id"], row["name"], row["note"]) if row else None


class GameRepository:
    """Peleihin ja niiden sääntöihin vastaavaann Game luokkaan
    liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self.__connection = connection

    def find_games(self):
        """Palauttaa kaikki tietokannassa olevat pelit.

        Returns:
            Palauttaa listan Game-olioita, jotka sisältävät pelin nimen ja
            kuvauksen, mutta ei vielä niiden voitottaulukkoa.
        """

        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM games")
        rows = cursor.fetchall()

        return list(map(get_game_by_row, rows))

    def get_pay_table(self, game_id: int):
        """Palauttaa tietyn pelin voittotaulukon.
        Args:
        game_id: pelin numero tietokannassa
        Returns:
            Palauttaa pelin voittotaulikon PayoutTable oliona.
        """

        cursor = self.__connection.cursor()
        cursor.execute(
            "SELECT hand, payout FROM pay_tables WHERE game_id = ?", (game_id,))
        rows = cursor.fetchall()

        payout_table = PayoutTable()

        for row in rows:
            payout_table.add_payout(row[0], row[1])

        return payout_table

    def get_game(self, game_id: int):
        """Palauttaa tietyn pelin tietokannasta.
        Args:
        game_id: pelin numero tietokannassa
        Returns:
            Palauttaa pelin voittotaulikon PayoutTable oliona.
        """

        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM games WHERE id = ?", (game_id,))
        row = cursor.fetchone()

        game = Game(row["id"], row["name"], row["note"])

        game.set_payout_table(self.get_pay_table(game_id))

        return game

    def delete_all(self):
        """Poistaa kaikki pelikonfiguraatiot tietokannasta.
        """

        cursor = self.__connection.cursor()

        cursor.execute("DELETE FROM pay_tables")
        cursor.execute("DELETE FROM games")

        self.__connection.commit()


game_repository = GameRepository(get_database_connection())
