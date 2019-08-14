num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)
 # this will print out a wrong result because Python will transform all input from the user into Strings

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)

print(result)

# this will fix the issue however int(num1) will make it integer, so float numbers will not work.

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)

# having float(num) transorm the strings to float, will mostly work in int cases, since all numbers are floats (5 it's 5.0)

