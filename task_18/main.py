import random as rnd

class NotFourDigitError(Exception):
    pass

def user_input():
    try:
        user_guess = input("Enter a 4-digit number: ").strip()
        if not user_guess.isdigit():
            raise ValueError
        elif len(user_guess) != 4:
            raise NotFourDigitError
    except ValueError:
        print("It's not a number!")
        return user_input()
    except NotFourDigitError:
        print("It's not a 4-digit number!")
        return user_input()
    return user_guess

def check_guess(secret_number, user_guess):
    cows = sum(s == g for s, g in zip(secret_number, user_guess))
    bulls = sum(min(secret_number.count(d), user_guess.count(d)) for d in set(user_guess)) - cows
    return cows, bulls

def main():
    number_to_guess = str(rnd.randint(1000, 9999))
    guess_counter = 0

    while True:
        guess = user_input()
        guess_counter += 1

        cows, bulls = check_guess(number_to_guess, guess)

        if cows == 4:
            print("Congrats, you guessed number in " + str(guess_counter) + " guesses!")
            break
        else:
            print(f"{cows} {'cow' if cows == 1 else 'cows'}, "
                  f"{bulls} {'bull' if cows == 1 else 'bulls'}")


if __name__ == "__main__":
    main()