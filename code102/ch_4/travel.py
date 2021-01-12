# travel.py

# Program calculates that amount of miles
# the employees have driven.

# ask the user how long they driven and
# how fast they were driving.
hour = int(input("How many hours did you drive? "))
speed = int(input("What was your maximum speed? "))

# Displays a table for each hour
print("Hour \t Distance")
print("------------------")
# Prepares the hour loop
hour += 1

for time in range(1, hour):
    # Calculates the distance
    distance = speed * time

    print(str(time), '\t', str(distance))
