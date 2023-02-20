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
        y = stringin.split("+")
        x = int(y[0])+int(y[1])
        return x
        
    elif "-" in stringin:
        y = stringin.split("-")
        x = int(y[0])-int(y[1])
        return x
        
    elif "*" in stringin:
        y = stringin.split("*")
        x = int(y[0])*int(y[1])
        return x
        
    elif "/" in stringin:
        try:
            y = stringin.split("/")
            x = int(y[0])/int(y[1])
            return int(x)
        except:
            return "Invalid operatin"
        
    else:
        return "Invalid operation"


stringin = input("Enter a simple maths equation: ")        
print(calculator(stringin))
