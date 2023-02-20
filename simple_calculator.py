#! /usr/bin/python
# Name: simple_calculator.py
# Author: Chris
# Revision v1.0
# Description: This program is a simple calculator.
"""
    Docstring: This program is a simple calculator. Pass a simple calculation (2+2 or 4/2 etc and it will return the result.
"""

def calculator(stringin):
    if "+" in stringin:
        try:
            y = stringin.split("+")
            x = int(y[0])+int(y[1])
            return x
        except:
            return "addition error"
        
    elif "-" in stringin:
        try:
            y = stringin.split("-")
            x = int(y[0])-int(y[1])
            return x
        except:
            return "subtraction error"
        
    elif "*" in stringin:
        try:
            y = stringin.split("*")
            x = int(y[0])*int(y[1])
            return x
        except:
            return "multiplication error"
            
    elif "/" in stringin:
        try:
            y = stringin.split("/")
            x = int(y[0])/int(y[1])
            return int(x)
        except:
            return "division error"
        
    else:
        return "Invalid operation"

while True:
    stringin = input("Enter a simple maths equation between two numbers (e.g: 2+2): ")        
    print(calculator(stringin))
    goagain = input("Do another calculation? Y / N: ")
    if "N" in goagain.upper():
        print("Bye!")
        break
