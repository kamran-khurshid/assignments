import random
user_guess=int(input("guess any number: "))
random_number=0
def game(a,b):
    random_number=random.randint(1,50)
    return random_number
print(game(1,50))
if user_guess == random_number:
     print("perfect guess")
else:
     print("try again")
