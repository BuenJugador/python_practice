import random as rnd

def delete_duplicates(lst):
    return list(set(lst).intersection(set(lst)))

def delete_duplicates2(lst):
    result = []
    [result.append(n) for n in lst if n not in result]
    return sorted(result)

mylst = [rnd.randint(1, 5) for i in range(10)]
print(mylst)
print(delete_duplicates(mylst))
print(delete_duplicates2(mylst))