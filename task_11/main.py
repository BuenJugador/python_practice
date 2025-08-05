def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

while True:
    try:
        number = int(input("Enter a number to check if it is prime: "))
        break
    except ValueError:
        print("Sorry, this is not a number")

print(is_prime(number))