from ui.user_view import UserView
from ui.video_poker_view import VideoPokerView
from services.videopokerservice import video_poker_service


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.

        Args:
            root:
                TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._show_user_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_user_view(self):
        self._hide_current_view()

        self._current_view = UserView(
            self._root,
            self._show_video_poker_view,
        )

        self._current_view.pack()

    def _show_video_poker_view(self):
        self._hide_current_view()

        video_poker_service.deal_hand(5)
        self._current_view = VideoPokerView(self._root, self._show_user_view)

        self._current_view.pack()
