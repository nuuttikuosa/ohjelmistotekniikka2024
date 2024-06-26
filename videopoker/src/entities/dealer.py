from random import choice, seed
import time

from entities.deck import Deck
from entities.hand import PokerHand


class Dealer:
    """Luokka, joka kuvaa pokeripelin jakajaa

    Attributes:
        seed: optionaalinen Kokonaisluku, joka alustaa satunnaislukugeneraattorin.
        Käytetään testauksessa, jotta saadaan aina samat kortit yksikkötesteille.
    """

    def __init__(self, seed_value=None):
        if seed_value is not None:
            seed(seed_value)
        else:
            seed(time.time())

    @staticmethod
    def deal_hand(count: int, card_deck: Deck):
        """Jakaa käden korttipakasta.
        Args:
            count: jaettavien korttien määrä
            card_deck:korttipakka josta kortit jaetaan
        Returns:
                pyydetyn määrän satunnaisia kortteja korttipakasta
        """

        hand = PokerHand()

        for _ in range(count):
            card_number = choice(range(card_deck.number_of_cards()))
            card = card_deck.get_card(card_number)
            hand.add_card(card)

        return hand

    @staticmethod
    def replace_cards(cards_to_keep: list, hand: PokerHand, card_deck: Deck):
        """Korvaa pyydetyt kortit korttipakasta.
        Args:
            cards: Kortit, jotka halutaan pitää
            hand: käsi, josta kortit korvataan
            card_deck:korttipakka josta uudet kortit jaetaan
        Returns:
                Käsi, josta halutut kortit on korvattu uusilla korteilla.
        """

        for card in hand.get_cards():
            if str(card) not in cards_to_keep:
                new_card_number = choice(range(card_deck.number_of_cards()))
                new_card = card_deck.get_card(new_card_number)
                hand.replace_card(card, new_card)

        return hand
