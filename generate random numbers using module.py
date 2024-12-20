import random
n=int(input("enter the length of the list: "))
def generate_random_numbers (a,b):
    random_int = [random.randint(1,100) for random_int in range(n)]
    return random_int
print(generate_random_numbers(1,100))