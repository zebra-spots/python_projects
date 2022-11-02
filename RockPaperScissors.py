#! /usr/bin/python
# Name: RockPaperScissors.py
# Author: Chris
# Revision v1.0
# Description: This program is a rock paper scissors game.
"""
    Docstring: This program is a rock paper scissors game.
"""
import sys
import random

def main():
    """ Uses random choice to decide computer selection and user inputs their choice """

    def play():
        user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return "Draw"

        if is_win(user, computer):
            return "You won"

        return "You lost"

        # r > s, s > p, p > r

    def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
            return True

    while True:

        print(play())
        userin = input('Press n to quit, Or press any key to play again')
        if userin.lower() == 'n':
            break

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
