def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 64, 5))


# this function compares numbers and displays the biggest number out of 3 values
# you can use different data types as well, such as strings, booleans
