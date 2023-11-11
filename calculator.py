def addition(x,y):
    return x + y

def substraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    if y == 0:
        return "Syntax Error"
    return x/y

num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
operation = input("Input the type of operation you want to carry out: ")

if operation == "addition":
    print(addition(num1, num2))
    
elif operation == "substraction":
    print(substraction(num1, num2))

elif operation == "multiplication":
    print(multiplication(num1, num2))

elif operation == "division":
    print(division(num1, num2))

else:
    print("Invalid input")
