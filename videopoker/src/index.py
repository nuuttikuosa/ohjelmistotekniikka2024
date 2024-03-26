from card import PlayingCard
from hand import PokerHand
from deck import Deck

def main():

    c1 = PlayingCard(0)
    c2 = PlayingCard(13)
    c3 = PlayingCard(26)
    c4 = PlayingCard(39)
    c5 = PlayingCard(51)

    h = PokerHand()
    h.add_card(c1)
    h.add_card(c2)
    h.add_card(c3)
    h.add_card(c4)
    h.add_card(c5)

    print(h)

    d = Deck()
    d.add_card(c1)
    d.add_card(c2)
    d.add_card(c3)
    d.add_card(c4)
    d.add_card(c5)

    print(d)

if __name__ == "__main__":
    main()