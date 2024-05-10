class Game:
    def __init__(self, game_id: int, name: str, note: str):
        self.__game_id = game_id
        self.__name = name
        self.__note = note
        self.__payout_table = None

    def set_payout_table(self, payout_table):
        self.__payout_table = payout_table

    def get_payout_table(self):
        return self.__payout_table

    def get_payout_for_hand(self, hand_value):
        return self.__payout_table.get_payout(hand_value)

    def get_game_id(self):
        return self.__game_id

    def get_name(self):
        return self.__name

    def get_note(self):
        return self.__note

    def __str__(self):
        return self.__name + " - " + self.__note
