counter = 0
def increment_counter():
    global counter
    counter = counter + 1
    print("Inside function, counter =", counter)


increment_counter()
increment_counter()
increment_counter()

print("Outside function, counter =", counter)
