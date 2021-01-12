# speed_converter.py

# This program converts the speeds 10 kph
# through 210 kph (in 10 kph increments)
# to mph.

START_SPEED = 10            # Starting speed
END_SPEED = 211             # Ending speed
INCREMENT = 10              # Speed increment
CONVERSION_FACTOR = 0.6214  # Conversion factor

# Displaying table headings.
print("KPH \t MPH")
print("--------------")

# Displaying speeds
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t', format(mph, '.1f'))
