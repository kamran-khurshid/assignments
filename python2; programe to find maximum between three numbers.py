num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))
num3 = int(input("enter number 3:"))
if num1 > num2 > num3 :
    print(f"{num1} is greater than {num2} and {num3}")
elif  num2 > num1 > num3 :
     print(f"{num2} is greater than {num1} and {num3}")
else:
     print(f"{num3} is greater than {num1} and {num2}")

