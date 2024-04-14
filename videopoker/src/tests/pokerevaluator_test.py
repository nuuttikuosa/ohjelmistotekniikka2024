import unittest
from card import PlayingCard
from hand import PokerHand
from pokerevaluator import PokerHandEvaluator
from pokerevaluator import HandValue


class TestPlayingCard(unittest.TestCase):
    def setUp(self):
        self.AceOfClubs = PlayingCard(12)
        self.AceOfDiamonds = PlayingCard(25)
        self.AceOfHearts = PlayingCard(38)
        self.AceOfSpades = PlayingCard(51)

        self.DeuceOfClubs = PlayingCard(0)
        self.DeuceOfDiamonds = PlayingCard(13)
        self.DeuceOfHearts = PlayingCard(26)
        self.DeuceOfSpades = PlayingCard(39)

        self.ThreeOfClubs = PlayingCard(1)
        self.FourOfClubs = PlayingCard(2)
        self.FiveOfClubs = PlayingCard(3)
        self.SixOfClubs = PlayingCard(4)
        self.SevenOfClubs = PlayingCard(5)
        self.EightOfClubs = PlayingCard(6)
        self.NineOfClubs = PlayingCard(7)
        self.TenOfClubs = PlayingCard(8)
        self.JackOfClubs = PlayingCard(9)
        self.QueenOfClubs = PlayingCard(10)
        self.KingOfClubs = PlayingCard(11)

        self.hand = PokerHand()

        self.evaluator = PokerHandEvaluator()

    def test_low_straight(self):
        self.hand.add_card(self.AceOfSpades)
        self.hand.add_card(self.DeuceOfClubs)
        self.hand.add_card(self.ThreeOfClubs)
        self.hand.add_card(self.FourOfClubs)
        self.hand.add_card(self.FiveOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.STRAIGHT)


    def test_normal_straight(self):
        self.hand.add_card(self.DeuceOfSpades)
        self.hand.add_card(self.ThreeOfClubs)
        self.hand.add_card(self.FourOfClubs)
        self.hand.add_card(self.FiveOfClubs)
        self.hand.add_card(self.SixOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.STRAIGHT)

    def test_flush(self):
        self.hand.add_card(self.DeuceOfClubs)
        self.hand.add_card(self.ThreeOfClubs)
        self.hand.add_card(self.FourOfClubs)
        self.hand.add_card(self.FiveOfClubs)
        self.hand.add_card(self.EightOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.FLUSH)

    def test_straight_flush(self):
        self.hand.add_card(self.AceOfClubs)
        self.hand.add_card(self.DeuceOfClubs)
        self.hand.add_card(self.ThreeOfClubs)
        self.hand.add_card(self.FourOfClubs)
        self.hand.add_card(self.FiveOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.STRAIGHT_FLUSH)

    def test_four_a_kind(self):
        self.hand.add_card(self.AceOfClubs)
        self.hand.add_card(self.AceOfDiamonds)
        self.hand.add_card(self.AceOfHearts)
        self.hand.add_card(self.AceOfSpades)
        self.hand.add_card(self.TenOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.FOUR)


    def test_full_house(self):
        self.hand.add_card(self.AceOfClubs)
        self.hand.add_card(self.AceOfDiamonds)
        self.hand.add_card(self.AceOfHearts)
        self.hand.add_card(self.DeuceOfSpades)
        self.hand.add_card(self.DeuceOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.FULL_HOUSE)


    def test_three_a_kind(self):
        self.hand.add_card(self.AceOfClubs)
        self.hand.add_card(self.AceOfDiamonds)
        self.hand.add_card(self.AceOfHearts)
        self.hand.add_card(self.DeuceOfSpades)
        self.hand.add_card(self.TenOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.THREE)

    def test_two_pairs(self):
        self.hand.add_card(self.AceOfDiamonds)
        self.hand.add_card(self.AceOfHearts)
        self.hand.add_card(self.DeuceOfSpades)
        self.hand.add_card(self.DeuceOfClubs)
        self.hand.add_card(self.TenOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.TWO_PAIRS)

    def test_one_pair(self):
        self.hand.add_card(self.AceOfDiamonds)
        self.hand.add_card(self.AceOfHearts)
        self.hand.add_card(self.TenOfClubs)
        self.hand.add_card(self.JackOfClubs)
        self.hand.add_card(self.QueenOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.PAIR)

    def test_high_card(self):
        self.hand.add_card(self.AceOfDiamonds)
        self.hand.add_card(self.DeuceOfClubs)
        self.hand.add_card(self.TenOfClubs)
        self.hand.add_card(self.JackOfClubs)
        self.hand.add_card(self.QueenOfClubs)
        self.assertEqual(self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list()), HandValue.HIGH_CARD)


