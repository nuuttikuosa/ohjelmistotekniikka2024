from entities.card import PlayingCard


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: PlayingCard):
        self.cards.append(card)

    def number_of_cards(self):
        return len(self.cards)

    def get_card(self, index):
        return self.cards.pop(index)

    def __str__(self):
        return " ".join([str(c) for c in self.cards])
