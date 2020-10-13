# Rose_Theater.py

# Setting price tag or various seats.
ORCHESTRA = 75
CENTER = 50
OUTER = 25

# asking user to input how many of each seat they want to purchase.
# calculates final result for each user input.
user = int(input("How many Orchestra seats to you want to purchase? "))
orchestra_final = user * ORCHESTRA
print("$" + str(orchestra_final))

user = int(input("How many Center Stage seats to you want to purchase? "))
center_final = user * CENTER
print("$" + str(center_final))

user = int(input("How many Outer Stage seats to you want to purchase? "))
outer_final = user * OUTER
print("$" + str(outer_final))

# calculates final sale of all purchased seats.
final_total = orchestra_final + center_final + outer_final
print("Final Total of seats purchased is: $" + str(final_total))
