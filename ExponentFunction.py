print(2**3) # this is 2 at the power of 3

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 5))


# basically this function raises a number to a power
# you can just use the first option from the top to printout the power, but if you do not know on what power you need to raise, a for loop is useful
