
employee_file = open("employees.txt", "a")  #apends text at the end of the file
employee_file = open("employees.txt", "w")  # writes over the file, it will replace what is inside with the new info. It can also create a new file, renaming the .txt file
employee_file.write("Toby - Human Resouces") # appends the text at the end of the time (no spacing at all)
employee_file.write("\nKelly - Human Resouces")  # appends the text at the end of the file, on a new line

employee_file.close()