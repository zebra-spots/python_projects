"""Write a program to iterate the first 10 numbers and in each 
iteration, print the sum of the current and previous number."""

previous_num = 0
for num in range (0, 10):
    added = num + previous_num
    print(f'Current Number {num} Previous Number {previous_num} Sum: {added}')
    previous_num = num
