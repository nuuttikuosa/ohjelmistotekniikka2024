import os
from PIL import Image, ImageTk

from config import PICTURES_DIRECTORY


class ImageRepository:
    """Pelikorttien kuvien lukemiseen levyltä / tietokannasta liittyvistä
    operaatiosta vastaava luokka.
    """

    def __init__(self, card_picture_directory: str):
        """Luokan konstruktori.

        Args:
            card_picture_directory: Polku hakemistoon, jossa pelikorttien png muotoiset kuvat ovat.
        """

        self.__card_picture_directory = card_picture_directory
        self.__images = {}

    def get_card_picture(self, card_name: str):
        """Palauttaa pelikortin kuvan. Esim. käyttöliittymää varten.

        Args:
            card_name: pelikorttitiedoston nimi. Pelinkortin kaksimerkkinen string id.

        Returns:
            Palauttaa pelikortin Tkinter PhotoImage muodossa.
        """
        if card_name not in self.__images:
            picture_path = os.path.join(
                self.__card_picture_directory, f"{card_name}.png")
            image = Image.open(picture_path)
            self.__images[card_name] = ImageTk.PhotoImage(image)
        return self.__images[card_name]


image_repository = ImageRepository(PICTURES_DIRECTORY)
