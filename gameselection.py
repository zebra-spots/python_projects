#! /usr/bin/python
# Name: gameselection.py
# Author: Chris
# Revision v1.0
# Description: This is a game program.


import random


def diceplay():
    minimum = 1
    maximum = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dice...")
        print("The values are....")
        print(random.randint(minimum, maximum))
        print(random.randint(minimum, maximum))

        roll_again = input("Press y to roll the dice again, press any other key to quit ").lower()


def playrps():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Draw"

    if is_win(user, computer):
        return "You won"

    return "You lost"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


def playhangman():
    playername = input("What is your name? ")

    words = '''Aragorn Arwen Bilbo Balin Boromir Denethor Elrond Eomer Eowyn Faramir Frodo \
    Galadriel Gandalf Gimli Gollum Isildur Legolas Merry Pippin Sam Saruman Sauron Shelob Treebeard Wormtounge'''
    words = words.split(' ')

    word = random.choice(words)

    guesses_allowed = 6
    guesses = []
    done = False

    print("Hello", playername, "welcome to hangman")
    print("Guess the Lord of the Rings character!")

    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end="")
            else:
                print("_", end=" ")
        print("\n")
        print(guesses)
        print("")

        guess = input(f"Remaining Lives {guesses_allowed}, Next Guess:")
        guesses.append(guess.lower())

        if not guess.isalpha():
            print("Only enter letters")
            continue
        elif len(guess) > 1:
            print("Only enter a single letter")
            continue

        if guess.lower() not in word.lower():
            guesses_allowed -= 1
            if guesses_allowed == 0:
                break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False

    if done:
        print("Well done", playername, "You correctly guessed", word)

    else:
        print("Game over! Unlucky", playername, "The word was:", word)


while True:
    print("Choose a game: \n"
          "1: Roll the dice\n"
          "2: Rock paper scissors\n"
          "3: Hangman\n"
          "q: Quit\n")

    check = input("Choice: \n")

    if check == "1":
        diceplay()

    elif check == "2":
        print(playrps())
        userin = input('Press q to quit, Or press any key to play again ')
        if userin.lower() == "q":
            continue

    elif check == "3":
        playhangman()

    else:
        break
