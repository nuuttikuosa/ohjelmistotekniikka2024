from entities.card import PlayingCard


class PokerHand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: PlayingCard):
        self.cards.append(card)

    def get_hand_as_string_list(self):
        return [str(c) for c in self.cards]

    def remove_cards(self, card_list: list):
        for i in card_list:
            self.cards.pop(i)

    def replace_card(self, old_card, new_card: PlayingCard):

        item = None
        for card in self.cards:
            if str(card) == str(old_card):
                item = card

        self.cards[self.cards.index(item)] = new_card

    def number_of_cards(self):
        return len(self.cards)

    def get_cards(self):
        return self.cards

    def __str__(self):
        return " ".join([str(c) for c in self.cards])
