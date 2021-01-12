# Grapevine.py

# Ask the user for input by feet
print("Please input the following in feet please.")
r = float(input("How long is the row? ")) # Row length
e = float(input("How much space is in between each post? ")) # space between post
s = float(input("How much space do you need in between vines? ")) # space between vines

# Calculates the amount of vines to be planted
v = (r - (2 * e)) / s

# displays final result
print("The amount of vines you can plant is: " + format(v, '.0f'))
