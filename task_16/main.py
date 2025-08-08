import random
import string

def password_gen(length: int):
    return ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits,k=length))

pass_length = int(input("Enter a length of password: "))
print(password_gen(pass_length))
