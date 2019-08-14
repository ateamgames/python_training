print(2) # prints the number directly, works with float, negative

print (3+4.5)  # prints also the result of a mathematical operation ( sum, divinion, multiplication, subsctact).
print(3*4 + 5) # also works, as python understand the order of operations
print(10 % 3) # impartire cu rest, remainder of the division

my_num = 5 # assign a variable
print(my_num)  # print the variable (will print the number)
print((str(my_num) + "my fav number"))  # str(my_num) transforms the number into a string so you can work directly with strings

print(abs(my_num)) # this prints the absolut value of the my_num value.
print(pow(3, 2))   # this is 3 la puterea 2 (it allowes you to pass a number and the power you want that number to be raised to)
print(max(4, 6))   #shows which number is higher.
print(min(4, 6))   #prints minimum between the 2 numbers
print(round(5.4))  # rounds the number to the closest integer (example 5,4 = 5  , 5.6 = 6)

# In order to do all the math functions, we need to import the math library

from math import * # this imports the all math functions

my_num1 = 4
print(floor(3.7)) # grabs the lowest number, in this case it's 3
print(ceil(3.7))  # rounds the number to the highest number, in this case 4
print(sqrt(36))   # prints out the square root of the number, in this case 6
#---------------------------------------------------------------------------------------------------------------#

