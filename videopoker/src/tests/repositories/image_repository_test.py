import unittest
import os
import tkinter as tk
from PIL import Image, ImageTk

from repositories.image_repository import image_repository


class TestImageRepository(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        dirname = os.path.dirname(__file__)

        file_path = os.path.join(dirname, "AS.png")
        image_AS = Image.open(file_path)
        self.picture_AS = ImageTk.PhotoImage(image_AS)

        file_path = os.path.join(dirname, "AH.png")
        image_AH = Image.open(file_path)
        self.picture_AH = ImageTk.PhotoImage(image_AH)

    def tearDown(self):
        self.root.destroy()

    def test_get_card_picture(self):
        self.assertEqual(image_repository.get_card_picture(
            "AS").width(), self.picture_AS.width())
        self.assertEqual(image_repository.get_card_picture(
            "AS").height(), self.picture_AS.height())

    def test_get_card_picture2(self):
        self.assertEqual(image_repository.get_card_picture(
            "AH").width(), self.picture_AS.width())
        self.assertEqual(image_repository.get_card_picture(
            "AH").height(), self.picture_AS.height())

    def test_get_card_picture_load_same_picture_again(self):
        self.assertEqual(image_repository.get_card_picture(
            "AS").width(), self.picture_AS.width())
        self.assertEqual(image_repository.get_card_picture(
            "AS").height(), self.picture_AS.height())
