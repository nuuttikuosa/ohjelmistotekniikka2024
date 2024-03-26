from deck import Deck 

class Dealer:
    from random import choise
    
    def __init__(self, seed_value: int):
        self.seed(seed_value)

    def deal_cards(self, count: int, card_deck: Deck):
        cards = []
        
        for i in range(count):
            card = self.choise(card_deck)
            card_deck.remove(card)
            cards.append(card)

        return cards

     