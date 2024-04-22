from database_connection import get_database_connection


def drop_tables(connection):

    cursor = connection.cursor()

    cursor.execute("""
                   DROP TABLE IF EXISTS pay_tables

                   """)
    cursor.execute("""
                   DROP TABLE IF EXISTS games

                   """)
    cursor.execute("""
                   DROP TABLE IF EXISTS users

                   """)

    connection.commit()


def create_tables(connection):

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE users(
        id integer primary key,
        name text,
        balance integer
        );
        """)

    cursor.execute("""
        CREATE TABLE games (
        id INTEGER PRIMARY KEY,
        name TEXT,
        note TEXT
        );
        """)

    cursor.execute("""
        CREATE TABLE pay_tables (
        id INTEGER PRIMARY KEY,
        hand INTEGER,
        payout INTEGER,
        game_id INTEGER,
        FOREIGN KEY (game_id) REFERENCES games(id)
        );
        """)

    connection.commit()


def inser_data(connection):

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO games (id,
        name,
        note)
        VALUES (
        1,
        'Jacks or Better',
        '800 for Royal Flush'
        );
        """)

    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (100, 800, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (90, 50, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (80, 25, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (70, 9, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (60, 6, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (50, 4, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (40, 3, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (30, 2, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (21, 1, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (20, 0, 1);""")
    cursor.execute(
        """INSERT INTO pay_tables (hand, payout, game_id) VALUES (10, 0, 1);""")

    cursor.execute(
        """INSERT INTO users (id, name, balance) VALUES (1, "Peluri", 1000);""")
    cursor.execute(
        """INSERT INTO users (id, name, balance) VALUES (2, "Pro", 1500);""")

    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    inser_data(connection)


if __name__ == "__main__":
    initialize_database()
