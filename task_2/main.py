number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
elif number % 4 == 0:
    print("Number is multiple of 4")
else:
    print("Odd")

dividend, divisor = int(input("Enter a dividend: ")), int(input("Enter a divisor: "))
if dividend % divisor == 0:
    print(f"{dividend} divides evenly by {divisor}")
else:
    print(f"{dividend} does not divide evenly by {divisor}")
