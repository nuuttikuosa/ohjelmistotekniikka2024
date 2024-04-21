from collections import Counter
from entities.hand_value import HandValue


class PokerHandEvaluator:
    def __contains_pair(self, ranks: list, card_rank: int):
        count = ranks.count(card_rank)
        return count == 2


    def __jacks_or_better_pair(self, ranks: list):
        if self.__contains_pair(ranks, 11):
            return True
        elif self.__contains_pair(ranks, 12):
            return True
        elif self.__contains_pair(ranks, 13):
            return True
        elif self.__contains_pair(ranks, 14):
            return True
        else:
            return False


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
            if(self.__jacks_or_better_pair(ranks)):
                hand_value = HandValue.PAIR_JACKS_OR_BETTER
            else:
                hand_value = HandValue.PAIR
        else:
            hand_value = HandValue.HIGH_CARD
        return hand_value
