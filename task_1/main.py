from datetime import datetime

name, age = input("Enter your name: "), int(input("Enter your age: "))
current_year = datetime.today().year
result = f"Hello {name}. In {current_year + (100 - age)} you will be 100 years old."
print(result)
number = int(input("Enter a number: "))
print(number * (result + "\n"))