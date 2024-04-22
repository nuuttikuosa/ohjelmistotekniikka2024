from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["name"], row["balance"]) if row else None


class UserRepository:

    def __init__(self, connection):

        self._connection = connection

    def find_all(self):

        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def create(self, user):

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO users (name, balance) values (?, ?)",
            (user.name, user.balance)
        )

        self._connection.commit()

        return user

    def update(self, user):

        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE users SET balance = ? WHERE name = ?",
            (user.balance, user.name)
        )

        self._connection.commit()

        return user


user_repository = UserRepository(get_database_connection())
