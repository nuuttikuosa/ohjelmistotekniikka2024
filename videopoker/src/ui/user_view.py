from tkinter import ttk, StringVar, constants
from services.videopokerservice import video_poker_service, UserExistsError


class UserView:
    """Käyttäjän kirjautumisesta vastaava näkymä."""

    def __init__(self, root, handle_user):
        """Luokan konstruktori. Luo uuden kirjautumisnäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_login:
                Kutsuttava-arvo, jota kutsutaan kun käyttäjä kirjautuu sisään.
            handle_show_create_user_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään rekisteröitymisnäkymään.
        """

        self._root = root
        self._handle_user = handle_user
        self._frame = None
        self._username_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()

        try:
            video_poker_service.login(username)
            self._handle_user()
        except UserExistsError:
            self._show_error("Problems with finding user database")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="User")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()

        login_button = ttk.Button(
            master=self._frame,
            text="Play",
            command=self._login_handler
        )


        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()