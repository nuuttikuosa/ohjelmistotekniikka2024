import unittest
from entities.card import PlayingCard
from entities.deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.AceOfClubs = PlayingCard(12)
        self.AceOfDiamonds = PlayingCard(25)
        self.AceOfHearts = PlayingCard(38)
        self.AceOfSpades = PlayingCard(51)
        self.DeuceOfClubs = PlayingCard(0)

        self.deck = Deck()
        self.deck.add_card(self.AceOfClubs)
        self.deck.add_card(self.AceOfDiamonds)
        self.deck.add_card(self.AceOfHearts)
        self.deck.add_card(self.AceOfSpades)

    def test_number_of_cards_in_deck(self):
        self.assertEqual(self.deck.number_of_cards(), 4)

    def test_get_card_from_deck(self):
        self.assertEqual(str(self.deck.get_card(3)), str(self.AceOfSpades))

    def test_ace_of_spades_to_string(self):
        self.assertEqual(str(self.deck), "AC AD AH AS")