import tkinter as tk
import os
from config import PICTURES_DIRECTORY

class ImageRepository:

    def __init__(self, card_picture_directory: str):

        self.__card_picture_directory = card_picture_directory


    def get_card_picture(self, card_name: str):
        print(PICTURES_DIRECTORY)
        picture_path = os.path.join(self.__card_picture_directory , f"{card_name}.png")
        return tk.PhotoImage(file=picture_path)

image_repository = ImageRepository(PICTURES_DIRECTORY)