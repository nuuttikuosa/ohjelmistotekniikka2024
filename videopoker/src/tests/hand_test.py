import unittest
from entities.card import PlayingCard
from entities.hand import PokerHand


class TestPlayingCard(unittest.TestCase):
    def setUp(self):
        self.AceOfClubs = PlayingCard(12)
        self.AceOfDiamonds = PlayingCard(25)
        self.AceOfHearts = PlayingCard(38)
        self.AceOfSpades = PlayingCard(51)
        self.DeuceOfClubs = PlayingCard(0)

        self.hand = PokerHand()
        self.hand.add_card(self.AceOfClubs)
        self.hand.add_card(self.AceOfDiamonds)
        self.hand.add_card(self.AceOfHearts)
        self.hand.add_card(self.AceOfSpades)

    def test_number_of_card_four(self):
        self.assertEqual(self.hand.number_of_cards(), 4)

    def test_hand_as_string_four_aces(self):
        self.assertEqual(str(self.hand), "AC AD AH AS")

    def test_add_card_to_hand(self):
        self.hand.add_card(self.DeuceOfClubs)
        self.assertEqual(str(self.hand), "AC AD AH AS 2C")

    def test_remove_card_from_hand(self):
        self.hand.remove_cards([3])
        self.assertEqual(str(self.hand), "AC AD AH")

    def test_replace_card_in_hand(self):
        self.hand.replace_card(3, self.DeuceOfClubs)
        self.assertEqual(str(self.hand), "AC AD AH 2C")

    def test_get_hand_as_tring_list(self):
        self.assertEqual(self.hand.get_hand_as_string_list(),
                         ["AC", "AD", "AH", "AS"])
