from entities.dealer import Dealer
from entities.pokerevaluator import PokerHandEvaluator
from services.videopokerservice import VideoPokerService


def main():

    print("Now we play Videopoker!")
    evaluator = PokerHandEvaluator()

    user_input = input("Please enter an integer seed: ")
    try:
        integer_seed = int(user_input)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    videopoker = VideoPokerService(Dealer(integer_seed), evaluator)

    games = videopoker.get_games()
    for game in games:
        print(str(game))
    pay_out_table = videopoker.get_pay_out_table(1)

    for payout in pay_out_table:
        print(payout[0].name, payout[1])
    print()
    print("Players:")
    players = videopoker.get_players()
    for player in players:
        print(player)

    print("Select player or give a new name to create player")
    player_name = input("Please enter name: ")

    videopoker.login(player_name)

    current_player = videopoker.get_current_player()
    print(
        f"Terve {current_player.name}, sinulla on {current_player.balance} pelirahaa")

    more = "n"
    more = input("Do you want to Play Video poker? (y/n)")
    while more == "y":
        videopoker.deal_hand(5)
        print("Here is your hand\n")
        print(videopoker.get_hand())
        print(videopoker.evaluate_hand())

        cards_to_replace = list(
            map(int, input("What cards do you want to replace: ").split()))

        videopoker.replace_cards(cards_to_replace)
        print("Here is your new hand:\n")
        print(videopoker.get_hand())
        print(videopoker.evaluate_hand())
        winning = videopoker.get_pay_out_for_hand(pay_out_table)
        print(f"You won {winning }")

        print(f"your balance {videopoker.get_current_player().balance }")
        more = input("Do you want to continue? (y/n)")


if __name__ == "__main__":
    main()
