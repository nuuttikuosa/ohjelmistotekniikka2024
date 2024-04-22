import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Pelaaja", 1000)

    def test_creation_and_string_conversion(self):
        self.assertEqual(str(self.user), "Pelaaja: 1000")
