import unittest
from entities.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.user = Game(1, "Pokeri", "Royal Flush Voitto")

    def test_creation_and_string_conversion (self):
        self.assertEqual(str(self.user), "Pokeri - Royal Flush Voitto")