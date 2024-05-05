import tkinter as tk
from tkinter import ttk, constants
from services.videopokerservice import video_poker_service
from entities.card import PlayingCard
from entities.hand import PokerHand
from PIL import Image, ImageTk


class VideoPokerHandView:
    """Video pokerin korttien näyttämisestä ja valitsemisesta vastaava näkymä."""

    def __init__(self, root, handle_select_card, card_image_repository):
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
        self._hand = video_poker_service.get_hand()
        self._handle_select_card = handle_select_card
        self.__card_image_repository = card_image_repository
        self._frame = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize_card_item(self, card: PlayingCard, column):
        item_frame = ttk.Frame(master=self._frame)

        # card_image = self.__card_image_repository.get_card_picture(str(card))
        label = ttk.Label(master=item_frame, text=str(card))
        label.configure(image=self.__card_image_repository.get_card_picture(
            str(card)), compound=tk.TOP)

        select_card_button = ttk.Button(
            master=item_frame,
            text="Select",
            command=lambda: self._handle_select_card(str(card))
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.N)

        select_card_button.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.NSEW
        )

        # item_frame.grid_columnconfigure(0, weight=1)
       # item_frame.pack(fill=constants.X)
        item_frame.grid(row=0, column=column, padx=5, pady=5, sticky=tk.NSEW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # lisätty
        self._frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)

        for index, card in enumerate(self._hand.get_cards()):
            self._initialize_card_item(card, index)


class VideoPokerView:
    """Tehtävien listauksesta ja lisäämisestä vastaava näkymä."""

    def __init__(self, root, handle_stop_playing, card_image_repository):
        """Luokan konstruktori. Luo uuden tehtävänäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_logout:
                Kutsuttava-arvo, jota kutsutaan kun käyttäjä kirjautuu ulos.
        """
        self._root = root
        self._handle_stop_playing = handle_stop_playing
        self._user = video_poker_service.get_current_player()
        self._card_image_repository = card_image_repository
        self._frame = None
        # self._create_todo_entry = None
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

    def _handle_select_card(self, card_id):
        video_poker_service.select_card(card_id)
        self._initialize_hand_view()

    def _initialize_hand_view(self):
        if self._hand_view:
            self._hand_view.destroy()

        hand = video_poker_service.get_hand()

        self._todo_list_view = VideoPokerHandView(
            self._hand_frame,
            self._handle_select_card,
            self._card_image_repository
        )

        self._todo_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Playing with {self._user.name}'s balance"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Exit",
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
        # todo_content = self._create_todo_entry.get()
        # pitää kirjoittaa koodia että korttien vaihtaminen  onistuu
        # if todo_content:
        #    todo_service.create_todo(todo_content)
        #    self._initialize_todo_list()
        #    self._create_todo_entry.delete(0, constants.END)
        pass

    def _initialize_footer(self):
        self._create_todo_entry = ttk.Entry(master=self._frame)

        create_deal_button = ttk.Button(
            master=self._frame,
            text="Deal",
            command=self._handle_deal_cards
        )

        self._create_todo_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        create_deal_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._hand_frame = ttk.Frame(master=self._frame)

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
