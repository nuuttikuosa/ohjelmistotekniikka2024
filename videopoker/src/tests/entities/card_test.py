import unittest
from entities.card import PlayingCard


class TestPlayingCard(unittest.TestCase):
    def setUp(self):
        self.AceOfSpades = PlayingCard(51)

    def test_ace_of_spades_short_suit(self):
        self.assertEqual(self.AceOfSpades.get_short_suit(), "S")

    def test_ace_of_spades_long_suit(self):
        self.assertEqual(self.AceOfSpades.get_long_suit(), "Spade")

    def test_ace_of_spades_short_face(self):
        self.assertEqual(self.AceOfSpades.get_short_face(), "A")

    def test_ace_of_spades_long_face(self):
        self.assertEqual(self.AceOfSpades.get_long_face(), "Ace")

    def test_ace_of_spades_to_string(self):
        self.assertEqual(str(self.AceOfSpades), "AS")
