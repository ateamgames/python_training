lucky_numbers = [4, 8, 15 ,16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Peter"]

friends.extend(lucky_numbers) # it will append the list lucky_numbers to the list Friends

friends.append("Creed") #this appends another item to the list (in this case, appends the name Creed into the friends function
friends.insert(1, "kelly") # this appends Kelly into the friends list on Index number 1. It will shift the rest of the list to the right
friends.remove("Jim") # removes Jim from the list
friends.clear() # clears the list
friends.pop()   # removes the last element from the list
friends.index("Kevin")  # will show the index for Kevin, if not, it fails with an error
friends.count("Jim") # it will tell us how many times Jim shows up in the list
friends.sort() # it sorts from random to alphabetical order
lucky_numbers.sort() # it will sort the list acceding order
lucky_numbers.reverse() # it will reverse the list
friends2 = friends.copy # this is a copy of friends list
