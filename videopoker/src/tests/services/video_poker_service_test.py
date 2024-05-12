import unittest

from entities.game import Game
from entities.dealer import Dealer
from entities.payout_table import PayoutTable
from entities.pokerevaluator import PokerHandEvaluator
from services.videopokerservice import VideoPokerService


class FakeGameRepository:

    def __init__(self, games=None):
        self.games = games or []

    def get_game(self, game_id):
        return Game(1,"Peli","hyvä peli")

    def get_payout_table(self):
        payout_table = PayoutTable()
        payout_table.add_payout(100,800)

        return payout_table

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

class TestVideoPokerService(unittest.TestCase):
    def setUp(self):
        pass

    def test_login(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        video_poker_service.login("UnitTest")
        current_player = video_poker_service.get_current_player()
        self.assertEqual(current_player.name, "UnitTest")
        self.assertEqual(current_player.balance, 1000)

    def test_deal_hand(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        video_poker_service.login("UnitTest")
        video_poker_service.deal_hand()
        hand = video_poker_service.get_hand()

        self.assertEqual(str(hand), "4D AH JH TC AD")

    def test_select_different_cards(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        video_poker_service.login("UnitTest")
        video_poker_service.deal_hand()
        video_poker_service.select_card("AH")
        video_poker_service.select_card("AD")

        self.assertEqual(
            video_poker_service.get_selected_cards(), ["AH", "AD"])

    def test_select_card_twice(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        video_poker_service.login("UnitTest")
        video_poker_service.deal_hand()
        video_poker_service.select_card("AH")
        video_poker_service.select_card("AH")

        self.assertEqual(video_poker_service.get_selected_cards(), [])

    def test_replace_cards(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        video_poker_service.login("UnitTest")
        video_poker_service.deal_hand()
        video_poker_service.select_card("AH")
        video_poker_service.select_card("AD")
        video_poker_service.replace_cards()
        hand = video_poker_service.get_hand()

        self.assertEqual(str(hand),  "6S AH 9H TS AD")

    def test_get_hand_value_text(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        video_poker_service.login("UnitTest")
        video_poker_service.deal_hand()

        self.assertEqual(
            video_poker_service.get_hand_value_text(),  "PAIR_JACKS_OR_BETTER")

    def test_get_player_list_text(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        video_poker_service.login("UnitTest")
        player_list = f"Tero: 2000\nUnitTest: 1000"

        self.assertEqual(
            video_poker_service.get_player_list_text(), player_list)

    def test_get_payout_table_text(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        payout_text = video_poker_service.get_payout_table_text()
        self.assertEqual(len(payout_text), 208)

    def test_get_games(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        game_list = video_poker_service.get_games()

        self.assertEqual(len(game_list), 1)
        self.assertEqual(str(game_list[0]),
                         "Jacks or Better - 800 for Royal Flush")

    def test_logout(self):
        video_poker_service = VideoPokerService(
            Dealer(3), PokerHandEvaluator())
        video_poker_service.login("UnitTest")
        video_poker_service.logout()

        self.assertEqual(video_poker_service.get_current_player(), None)

