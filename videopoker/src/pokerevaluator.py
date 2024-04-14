from collections import Counter
from enum import IntEnum, unique


@unique
class HandValue(IntEnum):
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

    def basic_evaluation(self, hand: list):

        flush = len(set(suit for _, suit in hand)) == 1
        ranks = sorted('--23456789TJQKA'.find(rank) for rank, _ in hand)
        if ranks == [2, 3, 4, 5, 14]:  # ace-low straight
            ranks = [1, 2, 3, 4, 5]
        straight = ranks == list(range(ranks[0], ranks[0] + 5))
        count = Counter(ranks)
        counts = sorted(count.values())

        if flush and straight:
            q = HandValue.STRAIGHT_FLUSH
        elif counts == [1, 4]:
            q = HandValue.FOUR
        elif counts == [2, 3]:
            q = HandValue.FULL_HOUSE
        elif flush:
            q = HandValue.FLUSH
        elif straight:
            q = HandValue.STRAIGHT
        elif counts == [1, 1, 3]:
            q = HandValue.THREE
        elif counts == [1, 2, 2]:
            q = HandValue.TWO_PAIRS
        elif counts == [1, 1, 1, 2]:
            q = HandValue.PAIR
        else:
            q = HandValue.HIGH_CARD
        return q
