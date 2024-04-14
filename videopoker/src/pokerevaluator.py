from collections import Counter
from enum import IntEnum, unique


@unique
class Quality(IntEnum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIRS = 3
    THREE = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR = 8
    STRAIGHT_FLUSH = 9


class PokerHandEvaluator:
    def __init__(self, type: int):

        if type == 1:
            self.evaluator = self.basic_evaluation
        else:
            self.evaluator = None

    def basic_evaluation(self, hand: list):

        flush = len(set(suit for _, suit in hand)) == 1
        ranks = sorted('--23456789TJQKA'.find(rank) for rank, _ in hand)
        if ranks == [2, 3, 4, 5, 14]:  # ace-low straight
            ranks = [1, 2, 3, 4, 5]
        straight = ranks == list(range(ranks[0], ranks[0] + 5))
        count = Counter(ranks)
        counts = sorted(count.values())

        if flush and straight:
            q = Quality.STRAIGHT_FLUSH
        elif counts == [1, 4]:
            q = Quality.FOUR
        elif counts == [2, 3]:
            q = Quality.FULL_HOUSE
        elif flush:
            q = Quality.FLUSH
        elif straight:
            q = Quality.STRAIGHT
        elif counts == [1, 1, 3]:
            q = Quality.THREE
        elif counts == [1, 2, 2]:
            q = Quality.TWO_PAIRS
        elif counts == [1, 1, 1, 2]:
            q = Quality.PAIR
        else:
            q = Quality.HIGH_CARD
        return q
