from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["name"], row["balance"]) if row else None


class UserRepository:
    """Pelaajiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki käyttäjät.
        Returns:
            Palauttaa listan User-olioita.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def create(self, user):
        """Tallentaa pelaajan tietokantaan.
        Args:
            todo: Tallennettava pelaaja User-oliona.
        Returns:
            Tallennettu pselaaja User-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO users (name, balance) values (?, ?)",
            (user.name, user.balance)
        )

        self._connection.commit()

        return user

    def update(self, user):
        """Päivittää pelaajan pelitilin saldon tietokantaan.
        Args:
            todo: Tallennettava pelaaja User-oliona.
        Returns:
            Päivitetty pelaaja User-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE users SET balance = ? WHERE name = ?",
            (user.balance, user.name)
        )

        self._connection.commit()

        return user

    def delete_all(self):
        """Poistaa kaikki pelaajat.
        """

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
