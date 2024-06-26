import unittest
from repositories.game_repository import game_repository
from entities.game import Game
from database_connection import get_database_connection


class TestGameRepository(unittest.TestCase):
    def create_test_data(self, connection):
        cursor = connection.cursor()

        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO games (id,
        name,
        note)
        VALUES (
        1,
        'Jacks or Better',
        '800 for Royal Flush'
        );
        """)

        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (100, 800, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (90, 50, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (80, 25, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (70, 9, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (60, 6, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (50, 4, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (40, 3, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (30, 2, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (21, 1, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (20, 0, 1);""")
        cursor.execute(
            """INSERT INTO pay_tables (hand, payout, game_id) VALUES (10, 0, 1);""")

        connection.commit()

    def setUp(self):
        game_repository.delete_all()
        connection = get_database_connection()
        self.create_test_data(connection)
        self.game = Game(1, "Jacks or Better", "800 for Royal Flush")

    def test_find_games(self):
        games = game_repository.find_games()

        self.assertEqual(len(games), 1)
        self.assertEqual(games[0].get_game_id(), self.game.get_game_id())
        self.assertEqual(games[0].get_name(), self.game.get_name())
        self.assertEqual(games[0].get_note(), self.game.get_note())

    def test_get_pay_table(self):
        pay_table = game_repository.get_pay_table(1)

        self.assertEqual(len(str(pay_table)), 208)
        self.assertEqual(pay_table.get_payout(10), 0)
        self.assertEqual(pay_table.get_payout(100), 800)

    def test_get_game(self):
        game = game_repository.get_game(1)

        self.assertEqual(game.get_game_id(), self.game.get_game_id())
        self.assertEqual(game.get_name(), self.game.get_name())
        self.assertEqual(game.get_note(), self.game.get_note())
