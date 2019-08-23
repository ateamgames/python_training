def cube(num):
    num*num*num

cube(3)
# creates a function called cube that will cube a number
# this will not return anything, because we are missing the return statement

def cube(num):
    return num*num*num


result = cube(4)
print(result)

# the return statement here will return information from the function cube.
