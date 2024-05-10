from ui.user_view import UserView
from ui.video_poker_view import VideoPokerView
from services.videopokerservice import video_poker_service

from repositories.image_repository import (
    image_repository as default_image_repository
)


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root, image_repository=default_image_repository):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.

        Args:
            root:
                TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        """
        self._root = root
        self.__image_repository = image_repository
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
            self._show_video_poker_view, video_poker_service
        )

        self._current_view.pack()

    def _show_video_poker_view(self):
        self._hide_current_view()

        self._current_view = VideoPokerView(
            self._root, self._show_user_view, video_poker_service, self.__image_repository)

        self._current_view.pack()
