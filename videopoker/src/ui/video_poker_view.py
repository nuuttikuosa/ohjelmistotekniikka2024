import tkinter as tk
from tkinter import ttk, constants
from entities.card import PlayingCard
from services.videopokerservice import VideoPokerService
from entities.hand import PokerHand

STATUS_GAME_NOT_STARTED = 0
STATUS_FIRST_ROUND = 1
STATUS_SECOND_ROUND = 2


class VideoPokerHandView:
    """Video pokerin korttien näyttämisestä ja valitsemisesta vastaava näkymä."""

    def __init__(self, root, video_poker_service: VideoPokerService, card_image_repository, status):
        """Luokan konstruktori. Luo uuden korttinäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            todos:
                Lista Card-olioita, jotka näkymässä näytetään
            handle_set_todo_done:
                Kutsuttava-arvo, jota kutsutaan kun kortin alla olevaa valitse bappia painetaan. Saa argumentiksi id-arvon.
        """


        self._root = root

        self._video_poker_service = video_poker_service
        self._hand = self._video_poker_service.get_hand()
        self.__card_image_repository = card_image_repository
        self._frame = None
        self.__status = status
        self.__buttons = {}

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def handle_press_button(self, card_id: str):
        self._video_poker_service.select_card(card_id)

        if card_id in self._video_poker_service.get_selected_cards():
            self.__buttons[card_id].config(text="Vapauta")
        else:
            self.__buttons[card_id].config(text="Valitse")


    def _initialize_card_item(self, card: PlayingCard, column):
        item_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=item_frame, text=str(card))
        label.configure(image=self.__card_image_repository.get_card_picture(
            str(card)), compound=tk.TOP)

        if self.__status == STATUS_FIRST_ROUND:
            select_card_button = ttk.Button(
                master=item_frame,
                text="Select",
                command=lambda: self.handle_press_button(str(card))
            )

            self.__buttons[str(card)]= select_card_button

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.N)

        if self.__status == STATUS_FIRST_ROUND:
            select_card_button.grid(
                row=1,
                column=0,
                padx=5,
                pady=5,
                sticky=constants.NSEW
            )


        item_frame.grid(row=0, column=column, padx=5, pady=5, sticky=tk.NSEW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)

        for index, card in enumerate(self._hand.get_cards()):
            self._initialize_card_item(card, index)


class VideoPokerView:
    """Tehtävien listauksesta ja lisäämisestä vastaava näkymä."""

    def __init__(self, root, handle_stop_playing, video_poker_service, card_image_repository):
        """Luokan konstruktori. Luo uuden tehtävänäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_logout:
                Kutsuttava-arvo, jota kutsutaan kun käyttäjä kirjautuu ulos.
        """
        self._root = root

        self.__status = STATUS_GAME_NOT_STARTED
        self._handle_stop_playing = handle_stop_playing
        self._user = video_poker_service.get_current_player()
        self._card_image_repository = card_image_repository
        self.__video_poker_service = video_poker_service
        self._frame = None
        self._deal_cards_button = None
        self.__hand_value_text = None
        self._hand_frame = None
        self._hand_view = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _user_handler(self):
        # todo_service.logout()
        self._handle_stop_playing()

    def _initialize_hand_view(self):
        if self._hand_view:
            self._hand_view.destroy()

        self._hand_view = VideoPokerHandView(
            self._hand_frame,
            self.__video_poker_service,
            self._card_image_repository, self.__status
        )

        self._hand_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Pelataan pelaajan {self._user.name} saldolla: {self._user.balance}"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Lopeta pelaaminen",
            command=self._user_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _handle_deal_cards(self):

        if self.__status == STATUS_FIRST_ROUND:
            self.__video_poker_service.replace_cards()
            self.__status = STATUS_SECOND_ROUND
            self._deal_cards_button.configure(text="Jaa uusi käsi")

        elif self.__status == STATUS_SECOND_ROUND:
            self.__video_poker_service.deal_hand()
            self.__status =STATUS_FIRST_ROUND
            self._deal_cards_button.configure(text="Vaihda kortteja")

        hand_value_text = f"Korkein yhdistelmä kädessä on {self.__video_poker_service.get_hand_value_text()}."

        if self.__status == STATUS_SECOND_ROUND:
            winning = self.__video_poker_service.get_pay_out_for_hand()
            if winning > 0:
                hand_value_text += f" Voitit {winning} kolikkoa."
            else:
                hand_value_text += f" Ei voittoa."

        self.__hand_value_text.configure(text=hand_value_text)
        self._initialize_hand_view()
        # todo_content = self._create_todo_entry.get()
        # pitää kirjoittaa koodia että korttien vaihtaminen  onistuu
        # if todo_content:
        #    todo_service.create_todo(todo_content)
        #    self._initialize_todo_list()
        #    self._create_todo_entry.delete(0, constants.END)

    def _initialize_footer(self):
        self.__hand_value_text  = ttk.Label(
            master=self._frame,
            text=f"Korkein yhdistelmä kädessä on {self.__video_poker_service.get_hand_value_text()}"
        )
        self._deal_cards_button= ttk.Button(
            master=self._frame,
            text="Vaihda kortteja",
            command=self._handle_deal_cards
        )

        self.__hand_value_text.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        self._deal_cards_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._hand_frame = ttk.Frame(master=self._frame)

        self.__status = STATUS_FIRST_ROUND
        self.__video_poker_service.deal_hand()

        self._initialize_header()
        self._initialize_hand_view()
        self._initialize_footer()

        self._hand_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=800)
        self._frame.grid_columnconfigure(1, weight=0)
