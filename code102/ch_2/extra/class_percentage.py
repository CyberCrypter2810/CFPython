# class_percentages.py

# Asking user how many of each gender are in the class.
male = int(input("How many males are in the class? "))
female = int(input("How many females are in the class? "))

# Calculates total of each gender
Class = male + female

# Calculating male percentage.
male_percent = male / Class

# Preparing # for display
male_percent *= 100
male_percent = int(male_percent)

# Calculating female percentage
female_percent = female / Class

# calculaing # for display
female_percent *= 100
female_percent = int(female_percent)

# displaying total results.
print("\nThe total percent of males in the class is " + str(male_percent) + '%')
print("The total percent of females in the class is " + str(female_percent) + '%')
