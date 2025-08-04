import random as rnd

def generate_number_to_guess(start : int, end: int) -> int:
    return rnd.randint(start, end)

print("Try to guess the number between 1 and 9.(If you want to quit, type 'exit' any time)")

number_to_guess = generate_number_to_guess(1, 9)

tries_counter = 0
while True:
    player_input = input("Enter your guess: ")
    try:
        guess = int(player_input)
    except ValueError:
        if player_input == "exit":
            break
        else:
            print("Invalid input. Type your guess or 'exit' if you want to quit.")
            continue

    if guess == number_to_guess:
        print(f"You guessed right! The number was {number_to_guess}.")
        print(f"Your number of tries was {tries_counter}.")
        tries_counter = 0
        number_to_guess = generate_number_to_guess(1, 9)
    elif guess < number_to_guess:
        print("Too low.")
        tries_counter += 1
    else:
        print("Too high.")
        tries_counter += 1
