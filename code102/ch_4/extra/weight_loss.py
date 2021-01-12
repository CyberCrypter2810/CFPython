# weight_loss.py

# Program will display a chart of six months if the user
# lose 4 pounds a month.

print("This table will show what your weight will be if")
print("you lose 4 pounds a month. \n")

# ask user for their current weight.
weight = int(input("How much do you currently weight? "))
print()

# print top of chart
print("Months \t Weight")
print("-----------------")

# create a loop for chart
for month in range(1,7):
    weight -= 4
    print(month, '\t', weight)

print()
print("At the end of 6 months, your weight will be", weight, 'pounds.')
