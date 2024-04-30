from entities.dealer import Dealer
from entities.deck import Deck
from entities.card import PlayingCard
from entities.user import User
from entities.pokerevaluator import PokerHandEvaluator


from repositories.game_repository import (
    game_repository as default_game_reposotory
)

from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserExistsError(Exception):
    pass


class VideoPokerService:
    """Sovelluslogiikasta vastaa luokka."""
    def __init__(self,
                 dealer: Dealer,
                 evaluator,
                 game_repository=default_game_reposotory,
                 user_repository=default_user_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            dealer:
                Olio dealer luokasta, joka jakaa korttipakasta satunnaisesti halutun määrän kortteja
            game_repository:
                Vapaaehtoinen, oletusarvoltaan GameRepository-olio.
                Olio, jolla on GameRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self.dealer = dealer
        self.hand = None
        self.current_player = None
        self.game_repository = game_repository
        self.user_repository = user_repository
        deck = Deck()
        for i in range(52):
            deck.add_card(PlayingCard(i))
        self.deck = deck
        self.evaluator = evaluator
        self.selected_cards = []

    def deal_hand(self, count: int):
        """Jakaa pokerikäden, pyydetyn määrän kortteja

        Args:
            count: haluttu määrä kortteja
        """

        self.hand = self.dealer.deal_hand(count, self.deck)

    def get_hand(self):
        """Palauttaa aikaisemmin jaetun pokerikäden

        Returns:
            Hand objektin, jossa pelikortit
        """
        return self.hand

    def replace_cards(self, cards: list):
        """Vaihtaa pokerikädestä pyydetyt kortit

        Args:
            vaihdettavien korttien lokaatiot kokonaislukulistassa
        """
        self.dealer.replace_cards(cards, self.hand, self.deck)

    def evaluate_hand(self):
        """Evaluoi tämänhetkisen käden

        Returns:
            pokerikäden arvo HandValue enumeraationa
        """
        return self.evaluator.basic_evaluation(self.hand.get_hand_as_string_list())

    def get_games(self):
        """Palauttaa erilaiset tietokantaan tallennetut videopokerikonfiguraatiot

        Returns:
            Palauttaa kaikki tietokannassa oveta erilaiset pelit
        """
        return self.game_repository.find_games()

    def get_pay_out_table(self, game_id: int):
        """Palauttaa erilaiset tietokantaan tallennetut maksusäännöt, jotka liittyvät annettuun peliin
        Arg:
            game_id: pokeripelin id tietokannassa (int)
        Returns:
            Palauttaa kaikki peliin liittyvät palkintosäännöt
        """

        return self.game_repository.get_pay_table(game_id)

    def get_pay_out_for_hand(self, pay_table: list):
        """Palauttaa käden voiton
        Arg:
            pay_table: lista voittomaksusääntöjä
        Returns:
            palauttaa rahamääräisen voiton
        """
        pay_out = 0
        hand_value = self.evaluate_hand()
        for pay_row in pay_table:
            if pay_row[0].value == hand_value.value:
                pay_out = pay_row[1]

        self.current_player.balance += pay_out
        self.update_player(self.current_player)

        return pay_out

    def get_players(self):
        """Palauttaa erilaiset tietokantaan tallennetut pelaajaprofiilit
        Returns:
            Tietokantaan tallennetut pelaajaprofiit User objektilistana
        """
        return self.user_repository.find_all()

    def create_player(self, player: User):
        """Luo uuden pelaajan tietokantaan
        Args:
            Tietokantaan tallennettava pelaaja User-objektina
        Returns:
            Tietokantaan tallennetun pelaajan User objektina
        """
        return self.user_repository.create(player)

    def update_player(self, player: User):
        """Päivittää pelaajan pelitilin saldon tietokantaan
        Args:
            Tietokantaan päivitettävä pelaaja User-objektina
        """
        self.user_repository.update(player)

    def login(self, user):
        """ Hakee pelaajan tiedot (saldon) tietokannasta tai luo uuden pelaajan
        Args:
            user: pelaajan nimi merkkijonona
        """
        players = self.get_players()

        for player in players:
            if user == player.name:
                self.current_player = player

        if self.current_player is None:
            self.current_player = self.create_player(User(user, 1000))

    def get_current_player(self):
        """Palauttaa peliä tällä hetkellä pelaavan pelaajan
        Return:
            pelaajan tiedot User-obektina
        """
        return self.current_player

    def select_card(self, card_id):
        """Valitsee korti podettäväksi myös pelin toisella kierroksella
        Args:
            kortin id
        """
        self.selected_cards.append(card_id)


video_poker_service = VideoPokerService(Dealer(3), PokerHandEvaluator())
