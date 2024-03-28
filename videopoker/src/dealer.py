from deck import Deck 
from hand import PokerHand


class Dealer:
    from random import choice, seed
    
    def __init__(self, seed_value: int):
        self.seed(seed_value)

    def deal_hand(self, count: int, card_deck: Deck):
        hand = PokerHand()
        
        for i in range(count):
            card_number = self.choice(range(card_deck.number_of_cards()))
            card = card_deck.get_card(card_number)
            hand.add_card(card)

        return hand

    def replacde_cards(self, cards: list, hand: PokerHand, card_deck: Deck):
       
        cards.sort(reverse=True)
        hand.remove_cards(cards)
        for i in range(len(cards)):
            card_number = self.choice(range(card_deck.number_of_cards()))
            card = card_deck.get_card(card_number)
            hand.add_card(card)
        
        return hand