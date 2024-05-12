class User:
    """Luokka, joka kuvaa pokeripelin pelaajaa"""

    def __init__(self, name, balance):
        """Luokan konstruktori.
        Args:
        name : pelaajan nimi
        balance: pelaajan pelitilin saldo, voi olla negatiivinen.
        """
        self.name = name
        self.balance = balance

    def add_balance(self, amount: int):
        self.balance += amount

    def reduce_balance(self, amount: int):
        self.balance -= amount

    def __str__(self):
        return f"{self.name}: {self.balance}"
