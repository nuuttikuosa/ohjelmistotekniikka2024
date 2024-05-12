from loguru import logger

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

from config import GAME_EVENT_LOG_FILE_PATH

NUMBER_OF_CARDS_IN_HAND = 5
NUMBER_OF_CARDS_IN_DECK = 52
PRICE_OF_GAME_ROUND = 1

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
                Olio dealer luokasta, joka jakaa korttipakasta halutun määrän satunnaisia kortteja
            evaluator:
                olio, joka analysoi mitä korttiyhdostelmiä pokerikäsessä on.
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

        self.deck = self.__init_deck()
        self.evaluator = evaluator
        self.selected_cards = []
        self.game = None

        self.set_game(DEFAULT_GAME)
        self.__init_logging(GAME_EVENT_LOG_FILE_PATH)

    def __init_logging(self, log_path):
        logger.add(log_path, rotation="12:00", retention="10 days")

    def __init_deck(self):
        deck = Deck()
        for i in range(NUMBER_OF_CARDS_IN_DECK):
            deck.add_card(PlayingCard(i))
        return deck

    def deal_hand(self, count: int = NUMBER_OF_CARDS_IN_HAND):
        """Jakaa pokerikäden, pyydetyn määrän kortteja

        Args:
            count: haluttu määrä kortteja
        """
        self.selected_cards = []
        self.deck = self.__init_deck()
        self.hand = self.dealer.deal_hand(count, self.deck)
        logger.info(f"Hand dealt successfully: {self.hand}")

        self.current_player.reduce_balance(PRICE_OF_GAME_ROUND)

    def get_hand(self):
        """Palauttaa jaetun pokerikäden. Pokerikäsi on tallennettu videopokerservice luokkaan.

        Returns:
            Hand objektin, jossa pelikortit
        """
        return self.hand

    def replace_cards(self):
        """Vaihtaa pokerikädestä pyydetyt kortit uusiin satunnaisiin kortteihin

        Returns:
            Korttipakka, josta on vaihdettu pyydetyt kortit uusiin.
        """

        self.dealer.replace_cards(self.selected_cards, self.hand, self.deck)
        logger.info(f"Cards changed successfully:{self.selected_cards}")
        logger.info(f"New Hand:{self.hand}")

        self.current_player.add_balance(
            PRICE_OF_GAME_ROUND*self.get_pay_out_for_hand())

    def evaluate_hand(self):
        """Evaluoi tämänhetkisen käden

        Returns:
            pokerikäden arvo HandValue enumeraationa
        """
        return self.evaluator.jacks_or_better_evaluation(self.hand.get_hand_as_string_list())

    def get_hand_value_text(self):
        """Palauttaa tämänhetkisen käden parhaan korttiyhdistelmän nimen stringinä.

        Returns:
            tämänhetkisen pokerikäden arvo HandValue enumeraation nimenä eli stringinä
        """

        return self.evaluate_hand().name

    def get_games(self):
        """Palauttaa erilaiset tietokantaan tallennetut videopokerikonfiguraatiot

        Returns:
            Palauttaa kaikki tietokannassa oveta erilaiset pelit
        """
        return self.game_repository.find_games()

    def get_pay_out_for_hand(self):
        """Palauttaa tämänhetkisen käden voiton
        Returns:
            palauttaa rahamääräisen voiton
        """
        hand_value = self.evaluate_hand()

        payout = self.game.get_payout_for_hand(hand_value)

        logger.info(f"Hand evaluated: {self.hand}")
        logger.success(f"Hand value: {hand_value.name}")
        logger.success(f"Payout: {payout}")

        return payout

    def get_players(self):
        """Palauttaa tietokantaan tallennetut pelaajaprofiilit
        Returns:
            Tietokantaan tallennetut pelaajaprofiit User objektilistana
        """
        return self.user_repository.find_all()

    def create_player(self, player: User):
        """Luo uuden pelaajan tietokantaan
        Args:
            Tietokantaan tallennettava pelaaja User-objektina
        Returns:
            Tietokantaan tallennetun pelaajan User objektin
        """
        return self.user_repository.create(player)

    def update_player(self, player: User):
        """Päivittää pelaajan pelitilin saldon tietokantaan
        Args:
            Tietokantaan päivitettävä pelaaja User-objektina
        """
        self.user_repository.update(player)

    def login(self, user):
        """ Hakee pelaajan tiedot (saldon) tietokannasta tai luo uuden pelaajan.
        Asettaa pelaajan pelin tämänhetkiseksi pelaajaksi.
        Args:
            user: pelaajan nimi merkkijonona
        """
        players = self.get_players()

        for player in players:
            if user == player.name:
                self.current_player = player

        if self.current_player is None:
            self.current_player = self.create_player(User(user, 1000))

    def logout(self):
        """ Tallentaa tämänhetkisen pelaajan saldon tietokantaan ja
        asettaa tämänthetkiseksi pelaajaksi None
        """
        self.update_player(self.current_player)
        self.current_player = None

    def get_current_player(self):
        """Palauttaa peliä tällä hetkellä pelaavan pelaajan
        Return:
            pelaajan tiedot User-obektina
        """
        return self.current_player

    def select_card(self, card_id):
        """Valitsee kortin pidettäväksi myös pelin toisella kierroksella
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
        """Palauttaa tällähetkellä seuraavalle kirrokselle pidettäväksi valitut kortit
        Returns:
            Valittujen korttien id lista
        """
        return self.selected_cards

    def set_game(self, game_id: int = DEFAULT_GAME):
        """Asettaa pelattavan pelin(nimi ja voittotaulukko)
        Args:
            Pelin id tietokannassa
        """
        self.game = self.game_repository.get_game(game_id)

    def get_payout_table_text(self):
        """Palauttaa tämänhetkisen pelin voittotaulukon
        Returns:
            Voittotaulukko string muodossa käyttöliittymää varten
        """
        return str(self.game.get_payout_table())

    def get_player_list_text(self):
        """Palauttaa tietokannassa olevat pelaajaprofiilit
        Returns:
            Lista pelaajaprofiileita string muodossa
        """
        player_str = "\n".join([str(player) for player in self.get_players()])
        return player_str


video_poker_service = VideoPokerService(Dealer(), PokerHandEvaluator())
