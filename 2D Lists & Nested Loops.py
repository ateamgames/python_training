number_grid = [
    [1, 2, 3,], # row 0
    [4, 5, 6],  # row 1
    [7, 8, 9],  # row 2
    [0]
]

print(number_grid[0][0])

# the 2D list acts like a matrix where you can have multiple lists within the list
# you have the same principles as a list, starts with 0 colloms and rows
# to call a specific number, you first need to add the index for the row and then for the collum
# example: printing the number 8 would be: print(number_grid[2][1]) -> row 2 (the 3row, since it starts on 0 and second index list (starts from 0)

for row in number_grid
    for col in row:
        print(col)

# this is an example of nested for loop, where it takes each individual item from the previous grid list
# for each row in the number and for each colloum in the row, it will printout the individual numbers