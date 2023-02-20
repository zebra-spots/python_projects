#! /usr/bin/python
# Name: string_split_calculator.py
# Author: Chris
# Revision v1.0
# Description: This program takes a string and calculates the simple equation in it.
"""
    Docstring: This program is a calculator. Pass a simple calculation (2+2 or 4/2 etc and it will return the result.
"""

def calc(equation):
    if '+' in equation:
        y = equation.split('+')
        x = int(y[0])+int(y[1])

    elif '-' in equation:
        y = equation.split('-')
        x = int(y[0])-int(y[1])

    elif '*' in equation:
        y = equation.split('*')
        x = int(y[0])*int(y[1])

    elif '/' in equation:
        y = equation.split('/')
        x = int(y[0])/int(y[1])

    return x


num = calc(input("Enter an equation: "))
print(int(num))
