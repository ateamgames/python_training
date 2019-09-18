employee_file = open("employees.txt", "r")  # this will only allow you to READ from the file (hence the R). Using W = write, a = append, r+ = read&write

print(employee_file.readable())   # checks if the file is readable
print(employee_file.readline())   # reads the first line
print(employee_file.readlines()[1]) # reads the line with index 1
print(employee_file.read())       # reads from the file

for employee in employee_file.readlines():    # for loop for the whole file, reads all lines one by one
    print(employee)



employee_file.close()

