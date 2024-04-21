class Game:
    def __init__(self, game_id: int, name: str, note: str):
        self.game_id = game_id
        self.name = name
        self.note = note

    def __str__(self):
        return self.name + " - " + self.note
