import random as rnd

def first_and_last(lst):
    return [lst[0], lst[-1]]

a = [rnd.randint(1, 100) for i in range(10)]
print(a)
print(first_and_last(a))