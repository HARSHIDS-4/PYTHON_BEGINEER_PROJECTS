import math
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
operator=input("enter the operator(+,-,*,/):")
match operator:
    case '+':
        print(f"addition of num1 AND NUM2 IS:{num1+num2}")
    case '-':
        print(f"subtraction of num1 and num2 is:{num1-num2}")
    case '*':
        print(f"multiplication of 2 numbers is:{num1*num2}")
    case '/':
        print(f"divison of two numbers is:{num1/num2}") 
    case _:
        print("other")   