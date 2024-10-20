A= int(input("enter length of side A:"))
B= int(input("enter lenght of side B:"))
C= int(input("enter lenght of side C:"))
if A==B==C:
    print("equilateral_triangle")
elif A==B!=C:
    print("isosceles_triangle")
elif A!=B!=C:
    print("scalene_triangle")