import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Pelaaja", 1000)

    def test_creation_and_string_conversion(self):
        self.assertEqual(str(self.user), "Pelaaja: 1000")

    def test_add_balance(self):
        test_user = User("Pelaaja", 1000)
        test_user.add_balance(10)
        self.assertEqual(test_user.balance, 1010)

    def test_reduce_balance(self):
        test_user = User("Pelaaja", 1000)
        test_user.reduce_balance(10)
        self.assertEqual(test_user.balance, 990)
