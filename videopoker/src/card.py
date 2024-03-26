# https://codereview.stackexchange.com/questions/95059/project-euler-problem-54-testing-poker-hands/95075#95075
# https://stackoverflow.com/questions/3829457/generating-all-5-card-poker-hands
# https://stackoverflow.com/questions/10363927/the-simplest-algorithm-for-poker-hand-evaluation

class PlayingCard:
    suits_long =  ('Club','Diamond', 'Heart', 'Spade')
    suits_short = ('C','D','H', 'S')
    faces_long = ('2', '3', '4', '5', '6', '7', '8', '9', 'Ten', 'Jack', 'Queen', 'King', 'Ace') 
    faces_short =  ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

    def __init__(self, id_number):
        self.id_number = id_number

    def get_long_suit(self):
        return PlayingCard.suits_long[self.id_number // 13]
    
    def get_short_suit(self):
        return PlayingCard.suits_short[self.id_number // 13]
    
    def get_short_face(self):
        return PlayingCard.faces_short[self.id_number % 13]
    
    def get_long_face(self):
        return PlayingCard.faces_long[self.id_number % 13]
    
    def __str__(self):
        return  self.get_short_face() + self.get_short_suit()

     

