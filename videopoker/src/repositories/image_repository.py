import os
from PIL import Image, ImageTk

from config import PICTURES_DIRECTORY


class ImageRepository:

    def __init__(self, card_picture_directory: str):

        self.__card_picture_directory = card_picture_directory
        self.__images = {}

    def get_card_picture(self, card_name: str):
        if card_name not in self.__images:
            picture_path = os.path.join(
                self.__card_picture_directory, f"{card_name}.png")
            image = Image.open(picture_path)
            self.__images[card_name] = ImageTk.PhotoImage(image)
        return self.__images[card_name]


image_repository = ImageRepository(PICTURES_DIRECTORY)
