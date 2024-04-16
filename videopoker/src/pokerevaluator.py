from collections import Counter
from hand_value import HandValue


class PokerHandEvaluator:

    def basic_evaluation(self, hand: list):

        flush = len(set(suit for _, suit in hand)) == 1
        ranks = sorted('--23456789TJQKA'.find(rank) for rank, _ in hand)
        if ranks == [2, 3, 4, 5, 14]:  # ace-low straight
            ranks = [1, 2, 3, 4, 5]
        straight = ranks == list(range(ranks[0], ranks[0] + 5))
        count = Counter(ranks)
        counts = sorted(count.values())
        if flush and straight and ranks[4] == 14:
            hand_value = HandValue.ROYAL_FLUSH
        elif flush and straight:
            hand_value = HandValue.STRAIGHT_FLUSH
        elif counts == [1, 4]:
            hand_value = HandValue.FOUR
        elif counts == [2, 3]:
            hand_value = HandValue.FULL_HOUSE
        elif flush:
            hand_value = HandValue.FLUSH
        elif straight:
            hand_value = HandValue.STRAIGHT
        elif counts == [1, 1, 3]:
            hand_value = HandValue.THREE
        elif counts == [1, 2, 2]:
            hand_value = HandValue.TWO_PAIRS
        elif counts == [1, 1, 1, 2]:
            hand_value = HandValue.PAIR
        else:
            hand_value = HandValue.HIGH_CARD
        return hand_value
