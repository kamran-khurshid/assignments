physics = int(input("enter marks obtained in physics :"))
chemistry = int(input("enter marks obtained in chemistry :"))
biology = int(input("enter marks obtained in biology :"))
maths = int(input("enter marks obtained in maths :"))
computer = int(input("enter marks obtained in computer :"))
total = physics + chemistry + biology + maths + computer
percentage = total/500*100

if percentage >= 33 :
    print(f"pass with {percentage} %")
    if percentage >= 90 :
        print("Grade A")
    elif percentage >= 80 :
        print("Grade B")
    elif percentage >= 70 :
        print("Grade C")
    elif percentage >= 60 :
        print("Grade D")
    elif percentage >= 40 :
        print("Grade E")
    elif percentage >= 40 :
        print("Grade F")
    else:
        print(f"Failed with {percentage} %")

