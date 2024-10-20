a=1
b=-3
c=2
discriminant=b*b-4*a*c
if discriminant> 0:
    root1=(-b + discriminant**0.5)/(2*a)
    root2=(-b-discriminant**0.5)/(2*a)
    print("roots are real and different:",root1, root2)
elif discriminant ==0:
    root = -b(2*a)
    print("roots are real and the same:",root)
else:
    print("roots are complex")
