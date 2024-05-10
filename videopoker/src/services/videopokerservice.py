from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.game_repository import (
    game_repository as default_game_reposotory
)
from entities.dealer import Dealer
from entities.deck import Deck
from entities.card import PlayingCard
from entities.user import User
from entities.pokerevaluator import PokerHandEvaluator

NUMBER_OF_CARDS_IN_HAND = 5
NUMBER_OF_CARDS_IN_DECK = 52

DEFAULT_GAME = 1


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
        for i in range(NUMBER_OF_CARDS_IN_DECK):
            deck.add_card(PlayingCard(i))
        self.deck = deck
        self.evaluator = evaluator
        self.selected_cards = []
        self.game = None

        self.set_game(DEFAULT_GAME)

    def deal_hand(self, count: int = NUMBER_OF_CARDS_IN_HAND):
        """Jakaa pokerikäden, pyydetyn määrän kortteja

        Args:
            count: haluttu määrä kortteja
        """
        self.selected_cards = []
        self.hand = self.dealer.deal_hand(count, self.deck)

    def get_hand(self):
        """Palauttaa aikaisemmin jaetun pokerikäden

        Returns:
            Hand objektin, jossa pelikortit
        """
        return self.hand

    def replace_cards(self):
        """Vaihtaa pokerikädestä pyydetyt kortit

        Returns:
            Korttipakka, josta on vaihdettu pyydetyt kortit uusiin.
        """

        self.dealer.replace_cards(self.selected_cards, self.hand, self.deck)

    def evaluate_hand(self):
        """Evaluoi tämänhetkisen käden

        Returns:
            pokerikäden arvo HandValue enumeraationa
        """
        return self.evaluator.jacks_or_better_basic_evaluation(self.hand.get_hand_as_string_list())

    def get_hand_value_text(self):
        return self.evaluate_hand().name

    def get_games(self):
        """Palauttaa erilaiset tietokantaan tallennetut videopokerikonfiguraatiot

        Returns:
            Palauttaa kaikki tietokannassa oveta erilaiset pelit
        """
        return self.game_repository.find_games()

    def get_pay_out_table_text(self, game_id: int):
        """Palauttaa erilaiset tietokantaan tallennetut maksusäännöt,
        jotka liittyvät annettuun peliin
        Arg:
            game_id: pokeripelin id tietokannassa (int)
        Returns:
            Palauttaa kaikki peliin liittyvät palkintosäännöt
        """

        return self.game_repository.get_pay_table(game_id)

    def get_pay_out_for_hand(self):
        """Palauttaa käden voiton
        Arg:
            pay_table: lista voittomaksusääntöjä
        Returns:
            palauttaa rahamääräisen voiton
        """
        hand_value = self.evaluate_hand()

        self.game.get_payout_for_hand(hand_value)

        return self.game.get_payout_for_hand(hand_value)

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
        """Valitsee kortti pidettäväksi myös pelin toisella kierroksella
            Tai poistaa kortin valittujen korttien joukosta, jos se on jo valittu.
        Args:
            kortin id
        """
        if card_id in self.selected_cards:
            self.selected_cards = [
                item for item in self.selected_cards if item != card_id]
        else:
            self.selected_cards.append(card_id)

    def get_selected_cards(self):
        return self.selected_cards

    def set_game(self, game_id: int = DEFAULT_GAME):

        self.game = self.game_repository.get_game(game_id)

    def get_payout_table_text(self):
        return str(self.game.get_payout_table())


video_poker_service = VideoPokerService(Dealer(3), PokerHandEvaluator())
