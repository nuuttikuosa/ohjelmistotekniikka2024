from entities.card import PlayingCard


class PokerHand:
    """Luokka, jona edustaa pelattavan pelin pokerikättä
    """

    def __init__(self):
        """Luokan konstruktori."""
        self.cards = []

    def add_card(self, card: PlayingCard):
        """Lisää pelikortin pokerikäteen.
        Args: Lisättävä pelikortti
        """
        self.cards.append(card)

    def get_hand_as_string_list(self):
        """Palauttaa käden kortti id string listana
        Returns: Lisättävä pelikortti
        """
        return [str(c) for c in self.cards]

    def remove_cards(self, card_list: list):
        """Poistaa pyydetyt kortit pokerikädestä.
        Args: poistettevien korttien sijainnit pokerikädessä
        """
        for i in card_list:
            self.cards.pop(i)

    def replace_card(self, old_card, new_card: PlayingCard):
        """Vaihtaa kortin pokerikädessä.
        Args: Vanha (vaihdettava pois)ja uusi kortti (vaihdettava tilalle)
        """
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
