# SIMPLE CALCULATOR IN PYTHON
import math

num1 = float(input("enter your first number:  "))
num2 = float(input("enter your second number:  "))
operator = input("enter your operator(+ - * /): ")
  
if operator == "+":
    Result = num1 + num2 
    print(Result)  
elif operator == "-":
    Result = num1 - num2
    print(Result)
elif operator == "*":
    Result = num1 * num2
    print(Result)
elif operator == "/": 
    Result = num1 / num2
    print(Result)
   
else:
    print("your operator is not valid please select one of the four (+ - * /). ")
