#! /usr/bin/python
# Name: fileHandling.py
# Author: Chris
# Revision v1.0
# Description: This demonstrates how to do basic file handling.

"""
Docstring:

"""


def main():

    # Open and read a text file
    with open("dog_breeds.txt", "r") as reader:
        dog_breeds = reader.readlines()

    # Open a second text file to write to
    with open("dog_breeds_2.txt", "w") as writer:
        for breed in dog_breeds:
            writer.write(breed)

    # View contents in original file
    with open("dog_breeds.txt", "r") as reader:
        for line in reader:
            print(line, end='')

    print("\n")

    # View contents in new file
    with open("dog_breeds_2.txt", "r") as reader:
        for line in reader:
            print(line, end='')

    print("\n")

    # Append to new file
    with open("dog_breeds_2.txt", "a") as writer:
        writer.write("\nBeagle")

    # See appended file
    with open("dog_breeds_2.txt", "r") as reader:
        for line in reader:
            print(line, end='')

    # Make reverse file
    with open("dog_breeds_reversed.txt", "w") as writer:
        for breed in reversed(dog_breeds):
            writer.write(breed)

    print("\n")

    # Read reversed file
    with open("dog_breeds_reversed.txt", "r") as reader:
        for line in reader:
            print(line, end='')


if __name__ == '__main__':
    main()
