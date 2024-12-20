import random
number=0
user_input=int(input("enter any number to check:"))
def random_number(a,b):
    number=tuple(random.randint(1,100) for numbers in range(5))
    return number
print(random_number(1,100))
if user_input==number:
    print(f"{user_input} is present in the tuple")
else:
    print(f"{user_input} is not present in the tuple")