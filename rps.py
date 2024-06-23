import sys
import random
from enum import Enum


def rps(name):

    game_count = 0
    player_count = 0
    python_count = 0

    def play_rps():
        nonlocal name #parent function's argument
        nonlocal player_count
        nonlocal python_count

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
            # print(RPS.ROCK)
            # print(RPS(2))
            # print(RPS["PAPER"])
            # print(RPS.PAPER.value)

        playerchoice = input(
            f"\n{name} please enter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors: \n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name} please enter 1,2, or 3.")
            return play_rps()

        # all user input from console is string so, text is needed to cast
        player = int(playerchoice)

        computer = int(random.choice("123"))

        print(f"\n----------\n{name}, you chose {str(RPS(player)).replace("RPS.", "")}\nComputer chose {str(RPS(computer)).replace("RPS.", "")}.")

        def decide_process(player, computer):
            nonlocal player_count
            nonlocal python_count
            if player == 1 and computer == 3:
                player_count += 1
                return f"🎉 {name}, you win!\n"
            elif player == 2 and computer == 1:
                player_count += 1
                return f"🎉 {name}, you win!\n"
            elif player == 3 and computer == 2:
                player_count += 1
                return f"🎉 {name}, you win!\n"
            elif player == computer:
                return "🤝 Tie game!\n"
            else:
                python_count += 1
                return f"🐍 Python wins! Sorry, {name}...\n"

        winner = decide_process(player, computer)
        nonlocal game_count  # it is not global, it is inside the scope opf the parent funct
        game_count += 1
        print(f"{winner} \nGame Count: {game_count}\n{name}'s Count:{player_count} \nPython Count:{python_count}\n----------")  # print how mant times we've played the game
        # eventhough run the function again and again, it wont't lose the count.
        # count's not stroed in the function, stored in the global scope
        print(f"\nPlay again, {name}?")
        while True:
            again = input("\nY for Yes or\nQ for Quit\n\n")
            if again.lower() not in ["y", "q"]:
                continue
            else:
                break
        if again == "y":
            return play_rps()
        else:
            print("Thank you for playing!")
            sys.exit(f"Bye, {name}! 👋")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personal game experience")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person for playing",
    )
    args = parser.parse_args()
    
    play_rpm_now = rps(args.name)
    play_rpm_now()
