name= str(input("enter any name:"))
greetings= str(input("enter the greetings:"))
def greet(name,greetings):
    grt= name+(",")+greetings
    return grt
result= greet(name , greetings)
print("hello" ,result)