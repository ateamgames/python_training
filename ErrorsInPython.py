try:
    number = int(input("Enter a number: "))
print(number)

except:
    print("Invalid Input")

    # Try and Except help you work with python errors
    # using them like this is not the best practice, because the except will allow any error to pass
    # you need to determine what to except when you want to ignore an error