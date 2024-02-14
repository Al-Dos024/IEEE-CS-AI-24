import random
import string

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

random_password = generate_random_password()
print("Random Password :", random_password)