"""Write a program to accept a string from the user and 
display characters that are present at an even index number."""

word = input("Enter a word: ")
print(f"Original word: {word}")

size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2
print("\nPrinting only even index chars:")
for i in range(0, size -1, 2):
    print(f"{i}, {word[i]}")


# using list slicing
# convert string to list
# pick only even index chars
print("\nPrinting only even index chars:")
x = list(word)
for i in x[0::2]:
    print(i)
