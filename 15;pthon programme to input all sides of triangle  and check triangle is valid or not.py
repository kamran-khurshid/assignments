side1= float(input("enter the lenght of side1:"))
side2= float(input("enter the lenght of side2:"))
side3= float(input("enter the lenght of side3:"))
if side1 + side2 > side3 or side2 + side3 > side1 or side3 + side1> side2:
    print("triangle is valid")
else:
    print("triangle is not valid")