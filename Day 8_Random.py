# Generate a random password of length of min. 24 characters containing lowercase, uppercase, numbers ,special characters(!@#$%^&*()).

l = ['!','@','#','$', '%','^','&','*','(',')']
import random
import string
def random_string(length=24,uppercase=True,lowercase=True,numbers=True):
    randomized_str=""
    i=1

    if uppercase:
        randomized_str+=string.ascii_uppercase
    if lowercase:
        randomized_str += string.ascii_lowercase
    if numbers:
        randomized_str += string.digits
    if l:
        randomized_str += str(l)
    return ''.join(random.choice(randomized_str) for i in range(length))

print("Random Password is : " + random_string())



