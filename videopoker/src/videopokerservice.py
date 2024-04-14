from dealer import Dealer
from deck import Deck
from card import PlayingCard


class VideoPokerService:
    def __init__(self, dealer: Dealer, evaluator):
        self.dealer = dealer
        self.hand = None

        deck = Deck()
        for i in range(52):
            deck.add_card(PlayingCard(i))
        self.deck = deck
        self.evaluator = evaluator

    def deal_hand(self, count: int):
        self.hand = self.dealer.deal_hand(count, self.deck)

    def get_hand(self):
        return self.hand

    def replace_cards(self, cards: list):
        self.dealer.replace_cards(cards, self.hand, self.deck)

    def evaluate_hand(self):
        return self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list())
