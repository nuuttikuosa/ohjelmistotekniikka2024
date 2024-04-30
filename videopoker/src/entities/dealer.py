from random import choice, seed

from entities.deck import Deck
from entities.hand import PokerHand


class Dealer:

    def __init__(self, seed_value: int):
        seed(seed_value)

    @staticmethod
    def deal_hand(count: int, card_deck: Deck):
        """Jakaa käden korttipakasta.
        Args:
            count: jaettavien korttien määrä
            card_deck:korttipakka josta kortit jaetaan
        Returns:
                pyydetyn määrän satunnaosia kortteja korttipakasta
        """

        hand = PokerHand()

        for _ in range(count):
            card_number = choice(range(card_deck.number_of_cards()))
            card = card_deck.get_card(card_number)
            hand.add_card(card)

        return hand

    @staticmethod
    def replace_cards(cards: list, hand: PokerHand, card_deck: Deck):
        """Korvaa pyydetyn määrän kortteja  korttipakasta.
        Args:
            cards: kokonaislukulista, korttien sijainnit jotka korvataan
            hand: käsi, josta kortit korvataan
            card_deck:korttipakka josta kortit jaetaan
        Returns:
                Käsi, josta kortit on satunnaisesti korvattu.
        """

        cards.sort(reverse=True)
        hand.remove_cards(cards)
        for _ in range(len(cards)):
            card_number = choice(range(card_deck.number_of_cards()))
            card = card_deck.get_card(card_number)
            hand.add_card(card)

        return hand
