import unittest

from entities.dealer import Dealer
from entities.deck import Deck
from entities.card import PlayingCard


class TestDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer(3)

        self.deck = Deck()
        for i in range(52):
            self.deck.add_card(PlayingCard(i))

        self.hand = self.dealer.deal_hand(5, self.deck)

    def test_deal_hand(self):
        self.assertEqual(str(self.hand), "4D AH JH TC AD")

    def test_replace_cards(self):
        new_hand = self.dealer.replace_cards(
            ["AH", "AD"], self.hand, self.deck)
        self.assertEqual(str(new_hand), "6S AH 9H TS AD")
