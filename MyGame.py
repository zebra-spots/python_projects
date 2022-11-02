#! /usr/bin/python
# Name: MyGame.py
# Author: Chris
# Revision v1.0
# Description: This is a testing program.
"""
    Docstring: Use to play games. Import rock paper scissors game.
    TODO: create and import more games
"""
import sys
from rockpaperscissors import *


def main():
    """ Call games here """
    print("Which game?\n"
          "1: rockpaperscissors\n"
          "2: Test statement\n")
    userchoice = input("Make a choice: ")

    if userchoice == "1":

        while True:
            print(play())
            userin = input("Press n to quit, Or press any key to play again ")
            if userin.lower() == "n":
                print("Quitting.......")
                break

    elif userchoice == "2":
        print("Test")

    else:
        print("Quitting.......")

    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
    
