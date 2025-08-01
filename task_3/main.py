a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Enter a number: "))
print(f"List of elements: {[num for num in a if num < number]} that are less than {number}")