from entities.card import PlayingCard


class Deck:
    """Luokka, jonka avulla ylläpidetään korttipakkaa.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden korttipakan.

        """
        self.cards = []

    def add_card(self, card: PlayingCard):
        """Lisää kortin korttipakkaa.
        Args:
            card: lisättävä kortti
        """

        self.cards.append(card)

    def number_of_cards(self):
        """Palauttaa korttien määrän korttipakassa.
        Returns:
            korttipakan korttien määrä
        """
        return len(self.cards)

    def get_card(self, index):
        """palauttaa pyydetyn kortin korttipakasta.
        Args:
            card: kortin sijainti korttipakassa (0,n-1)
        Returns:
            pelikortti pyydetystä lokaatiosta
        """
        return self.cards.pop(index)

    def __str__(self):
        """palauttaa korttipakan kortin merkkijonona
        Returns:
            Korttipakan pelikortit merkkijonona
        """
        return " ".join([str(c) for c in self.cards])
