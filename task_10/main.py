import random as rnd

def generate_random_list():
    generated_list = []
    for i in range(rnd.randint(1,50)):
        generated_list.append(rnd.randint(1,10))
    return generated_list

a = generate_random_list()
b = generate_random_list()
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(f"First list: {a}")
print(f"Second list: {b}")

result = []
[result.append(x) for x in a if x in b and x not in result]
print(result)