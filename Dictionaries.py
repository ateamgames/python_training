monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "March": "March",
    "Apr": "April",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])   # prints the value assosiated with the key

print(monthConversions.get("Dec")) # same thing as above, but uses a get function, no need for [ ]
                                   # the get function can replace the none value with a string we choose
                                   # print(monthConversions.get("Dev", "Not a value")) -> this is an example


