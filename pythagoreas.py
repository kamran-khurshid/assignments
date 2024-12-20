import math
base= float(input("enter the base:"))
perpendicular= float(input("enter the perpendicular:"))
def pythagoras(base , perpendicular):
    hypotenuse= math.sqrt((base)**2 + (perpendicular)**2)
    return hypotenuse
result= pythagoras(base, perpendicular)
print(result)