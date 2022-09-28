"""Write a program to remove characters from a string 
starting from zero up to n and return a new string."""

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 1))
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
