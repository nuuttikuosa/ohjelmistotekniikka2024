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
        saldo integer
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
        'Game1',
        'Note for Game1'
        );
        """)

    cursor.execute("""
        INSERT INTO
        pay_tables (
        hand,
        payout,
        game_id)
        VALUES (
        1, 100, 1
        );
        """)

    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    inser_data(connection)


if __name__ == "__main__":
    initialize_database()
