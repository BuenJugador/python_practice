import random as rnd

def generate_random_list():
    generated_list = []
    for i in range(rnd.randint(1,50)):
        generated_list.append(rnd.randint(1,10))
    return generated_list

a = generate_random_list()
b = generate_random_list()
print(f"First list: {a}")
print(f"Second list: {b}")

result = list(set(a).intersection(set(b)))
print(result)