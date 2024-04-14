from card import PlayingCard


class PokerHand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: PlayingCard):
        self.cards.append(card)

    def number_of_cards(self):
        return len(self.cards)

    def get_hand_as_string_list(self):
        return [str(c) for c in self.cards]

    def remove_cards(self, card_list: list):
        for i in card_list:
            self.cards.pop(i)

    def replace_card(self, old_card: int, new_card: PlayingCard):
        self.cards[old_card] = new_card

    def __str__(self):
        return " ".join([str(c) for c in self.cards])
