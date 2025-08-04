VALID_INPUT = {"rock", "paper", "scissors"}

class InputError(Exception):
    pass

def player_input(player_number : int) -> str:
    while True:
        try:
            choice = input(f"Player {player_number} please enter your choice between rock, paper, scissors: ").lower()
            if choice not in VALID_INPUT:
                raise InputError("Invalid input! Please enter rock, paper or scissors")
            else:
                return choice
        except InputError as e:
            print(e)


print("Welcome to rock paper scissors game!")
while True:
    first_choice = player_input(1)
    second_choice = player_input(2)

    if first_choice == second_choice:
        print("It's a draw!")
    elif (
        (first_choice == "rock" and second_choice == "scissors") or
        (first_choice == "scissors" and second_choice == "paper") or
        (first_choice == "paper" and second_choice == "rock")
    ):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        continue
    else:
        break


