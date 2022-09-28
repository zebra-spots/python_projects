"""Given two integer numbers return their product only if 
the product is equal to or lower than 1000, 
else return their sum."""

num1 = input()
num2 = input()
num3 = int(num1) * int(num2)

if num3 <= 1000:
    print(f'The result is {num3}')

else:
    num4 = int(num1) + int(num2)
    print(f'The result is {num4}')
