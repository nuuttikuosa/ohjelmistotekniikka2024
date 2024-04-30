import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_tero = User('Tero', 1000)
        self.user_taneli = User('Taneli', 2000)

    def test_create(self):
        user_repository.create(self.user_tero)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, self.user_tero.name)
        self.assertEqual(users[0].balance, self.user_tero.balance)

    def test_find_all(self):
        user_repository.create(self.user_tero)
        user_repository.create(self.user_taneli)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, self.user_tero.name)
        self.assertEqual(users[0].balance, self.user_tero.balance)
        self.assertEqual(users[1].name, self.user_taneli.name)
        self.assertEqual(users[1].balance, self.user_taneli.balance)

    def test_update(self):

        self.user_tero_new = User('Tero', 2000)
        user_repository.create(self.user_tero)
        user_repository.update(self.user_tero_new)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, self.user_tero_new.name)
        self.assertEqual(users[0].balance, self.user_tero_new.balance)
