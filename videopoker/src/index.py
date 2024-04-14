from dealer import Dealer
from videopokerservice import VideoPokerService
from pokerevaluator import PokerHandEvaluator


def main():

    print("Now we play Videopoker!")
    evaluator = PokerHandEvaluator(1)

    user_input = input("Please enter an integer seed: ")
    try:
        integer_seed = int(user_input)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    videopoker = VideoPokerService(Dealer(integer_seed), evaluator)

    more = "y"
    while more == "y":
        videopoker.deal_hand(5)
        print("Here is your hand\n")
        print(videopoker.get_hand())
        print(videopoker.evaluate_hand())
   # print(videopoker.evaluate_hand().value)

    # k = list(map(int, input("Please enter multiple values: ").split()))

        cards_to_replace = list(
            map(int, input("What cards do you want to replace: ").split()))

        videopoker.replace_cards(cards_to_replace)
        print("Here is your new hand:\n")
        print(videopoker.get_hand())
        print(videopoker.evaluate_hand())

        more = input("Do you want to continue? (y/n)")


if __name__ == "__main__":
    main()
