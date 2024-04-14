from collections import Counter
from enum import IntEnum, unique


@unique
class Quality(IntEnum):
    """Quality of a poker hand. Higher values beat lower values."""
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
        """Return the canonical form of the poker hand as a pair (q, r) where
    q is a value from the Quality enumeration, and r is a list of the
    distinct card ranks in the hand (from 1=low ace to 14=high ace),
    ordered in descreasing order by frequency and then by rank. These
    canonical forms can be compared to see who wins. The hand must be
    a sequence of five cards given as two-character strings in the
    form 2H, TS, JC etc.

    >>> canonical('TD 7H KH TS 7S'.split()) # two pairs (tens and sevens)
    (<Quality.two_pairs: 3>, [10, 7, 13])
    >>> canonical('3C AH 4D 2S 5C'.split()) # ace-low straight
    (<Quality.straight: 5>, [5, 4, 3, 2, 1])
    >>> canonical('JH 2H JC JS 2D'.split()) # full house (twos and jacks)
    (<Quality.full_house: 7>, [11, 2])
    >>> canonical('TS 4S 8S QS 5S'.split()) # queen-high flush
    (<Quality.flush: 6>, [12, 10, 8, 5, 4])

    """
        flush = len(set(suit for _, suit in hand)) == 1
        ranks = sorted('--23456789TJQKA'.find(rank) for rank, _ in hand)
        if ranks == [2, 3, 4, 5, 14]:  # ace-low straight
            ranks = [1, 2, 3, 4, 5]
        straight = ranks == list(range(ranks[0], ranks[0] + 5))
        count = Counter(ranks)
        counts = sorted(count.values())
        # distinct_ranks = sorted(count, reverse=True, key=lambda v:(count[v], v))

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
        # return q, distinct_ranks
