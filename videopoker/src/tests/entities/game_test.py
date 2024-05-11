import unittest
from entities.game import Game
from entities.payout_table import PayoutTable


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(1, "Pokeri", "Royal Flush Voitto")
        self.payout_table = PayoutTable()
        self.payout_table.add_payout(100, 800)
        self.payout_table.add_payout(21, 1)
        self.payout_table.add_payout(20, 0)
        self.game.set_payout_table(self.payout_table)

    def test_creation_and_string_conversion(self):
        self.assertEqual(str(self.game), "Pokeri - Royal Flush Voitto")

    def test_get_payout_for_hand(self):
        self.assertEqual(self.game.get_payout_for_hand(100), 800)

    def test_get_payout_table(self):
        self.assertEqual(self.game.get_payout_table(), self.payout_table)
