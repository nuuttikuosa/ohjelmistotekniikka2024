# https://codereview.stackexchange.com/questions/95059/project-euler-problem-54-testing-poker-hands/95075#95075
# https://stackoverflow.com/questions/3829457/generating-all-5-card-poker-hands
# https://stackoverflow.com/questions/10363927/the-simplest-algorithm-for-poker-hand-evaluation

class PlayingCard:
    """Luokka, joka kuvaa pelikorttia

    Attributes:
        id: Kokonaisluku, joka toimii kortin id:nä, välillä 0-51.
    """

    suits_long = ('Club', 'Diamond', 'Heart', 'Spade')
    suits_short = ('C', 'D', 'H', 'S')
    faces_long = ('2', '3', '4', '5', '6', '7', '8', '9',
                  'Ten', 'Jack', 'Queen', 'King', 'Ace')
    faces_short = ('2', '3', '4', '5', '6', '7',
                   '8', '9', 'T', 'J', 'Q', 'K', 'A')

    def __init__(self, id_number):
        """Luokan konstruktori, joka luo uuden pelikortin.

        Args:
            id: Kokonaisluku, joka toimii kortin id:nä, välillä 0-51.
        """
        self.id_number = id_number

    def get_long_suit(self):
        """Palauttaa kortin maasta pitkän version stringinä.

            Returns:
               Pitkä versio maasta.
        """
        return PlayingCard.suits_long[self.id_number // 13]

    def get_short_suit(self):
        """Palauttaa kortin maasta lyhyen version yhden kirjaumen mittaisena stringinä.

            Returns:
                Lyhyt versio maan englanninnimisestä termistä
        """

        return PlayingCard.suits_short[self.id_number // 13]

    def get_short_face(self):
        """Palauttaa kortin arvon yhden kirjaimen stringinä.

            Returns:
                kortin arvo yhden kirjaimen stringinä
        """

        return PlayingCard.faces_short[self.id_number % 13]

    def get_long_face(self):
        """Palauttaa kortin arvon pitkässä muodossa englannin kielen sanana stringinä.

            Returns:
                kortin arvo pitkässä muodossa englannin kielen sanana stringinä.
        """

        return PlayingCard.faces_long[self.id_number % 13]

    def __str__(self):
        """Palauttaa kortin tyypin kahden merkin tunnisteena.

            Returns:
                kortin tyyppi kahden merkin tunnisteena.
        """

        return self.get_short_face() + self.get_short_suit()
