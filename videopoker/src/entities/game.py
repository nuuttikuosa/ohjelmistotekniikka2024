class Game:
    """Luokka, jona edustaa pelattavan pelin sääntöjä
    """

    def __init__(self, game_id: int, name: str, note: str):
        """Luokan konstruktori.

        Args:
            game_id: numeerinen PK tietokannasta
            name: Pelin nimi
            note: Tekstikuvaus pelille
        """
        self.__game_id = game_id
        self.__name = name
        self.__note = note
        self.__payout_table = None

    def set_payout_table(self, payout_table):
        """Asettaa voittotaulukon pelille.

        Args:
            Voittotaulukko luokan objekti, joka sisältää rahamääräiset voitot eri
            korttiyhdistelmille.
        """
        self.__payout_table = payout_table

    def get_payout_table(self):
        """Palauttaa voittotaulukon pelille.

        Returns:
            Voittotaulukko luokan objekti, joka sisältää rahamääräiset voitot eri
            korttiyhdistelmille.
        """
        return self.__payout_table

    def get_payout_for_hand(self, hand_value):
        """Palauttaa voiton käden arvolle.
        Args: käden arvo HandValue enumaraationa.
        Returns:
            rahamääräinen voitto.
        """
        return self.__payout_table.get_payout(hand_value)

    def get_game_id(self):
        return self.__game_id

    def get_name(self):
        return self.__name

    def get_note(self):
        return self.__note

    def __str__(self):
        return self.__name + " - " + self.__note
