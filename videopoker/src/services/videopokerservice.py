from entities.dealer import Dealer
from entities.deck import Deck
from entities.card import PlayingCard
from entities.user import User
from entities.pokerevaluator import PokerHandEvaluator


from repositories.game_repository import (
    game_repository as default_game_reposotory
)

from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserExistsError(Exception):
    pass


class VideoPokerService:
    def __init__(self,
                 dealer: Dealer,
                 evaluator,
                 game_repository=default_game_reposotory,
                 user_repository=default_user_repository):
        self.dealer = dealer
        self.hand = None
        self.current_player = None
        self.game_repository = game_repository
        self.user_repository = user_repository
        deck = Deck()
        for i in range(52):
            deck.add_card(PlayingCard(i))
        self.deck = deck
        self.evaluator = evaluator
        self.selected_cards = []

    def deal_hand(self, count: int):
        self.hand = self.dealer.deal_hand(count, self.deck)

    def get_hand(self):
        return self.hand

    def replace_cards(self, cards: list):
        self.dealer.replace_cards(cards, self.hand, self.deck)

    def evaluate_hand(self):
        return self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list())

    def get_games(self):
        return self.game_repository.find_games()

    def get_pay_out_table(self, game_id: int):
        return self.game_repository.get_pay_table(game_id)

    def get_pay_out_for_hand(self, pay_table: list):

        pay_out = 0
        hand_value = self.evaluate_hand()
        for pay_row in pay_table:
            if pay_row[0].value == hand_value.value:
                pay_out = pay_row[1]

        self.current_player.balance += pay_out
        self.update_player(self.current_player)

        return pay_out

    def get_players(self):
        return self.user_repository.find_all()

    def create_player(self, player: User):
        return self.user_repository.create(player)

    def update_player(self, player: User):
        self.user_repository.update(player)

    def login(self, user):
        players = self.get_players()

        for player in players:
            if user == player.name:
                self.current_player = player

        if self.current_player is None:
            self.current_player = self.create_player(User(user, 1000))

    def get_current_player(self):
        return self.current_player

    def select_card(self, card_id):
        self.selected_cards.append(card_id)


video_poker_service = VideoPokerService(Dealer(3), PokerHandEvaluator())
