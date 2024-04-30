from enum import IntEnum, unique


@unique
class HandValue(IntEnum):
    """Enumaraatioluokka, jonka avulla ylläpidetään tietoa mahdollista käsien arvoista ja niiden järjestyksestä.
    """

    HIGH_CARD = 10
    PAIR = 20
    PAIR_JACKS_OR_BETTER = 21
    TWO_PAIRS = 30
    THREE = 40
    STRAIGHT = 50
    FLUSH = 60
    FULL_HOUSE = 70
    FOUR = 80
    STRAIGHT_FLUSH = 90
    ROYAL_FLUSH = 100
