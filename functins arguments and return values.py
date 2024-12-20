num1= float(input("enter num1: "))
num2= float(input("enter num2: "))
operator=str(input("enter the operator:"))
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Divided  by zero"
    else:
        return "Error: Invalid operator"
result= calculate(num1 , num2, operator)
print(result)

