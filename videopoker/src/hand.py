from card import PlayingCard

class PokerHand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: PlayingCard):
        self.cards.append(card)
    
    def number_of_cards(self):
        return self.cards.leght()
    
    def __str__(self):
        return " ".join([str(c)  for c in self.cards])