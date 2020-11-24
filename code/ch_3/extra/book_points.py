# Book_Points.py

# asks user how many books they are puchasing
purchase = int(input("How many books have you purchase this month? "))

# create reward points based on purchase of books.
if purchase < 2:
    reward = 0
elif purchase >= 2 and purchase < 4:
    reward = 5
elif purchase >= 4 and purchase < 6:
    reward = 15
elif purchase >= 6 and purchase < 8:
    reward = 30
else:
    reward = 60

# displays results
print("Your amount of award points this month is: ", reward)
