# Contoso_Widgets.py

# Price of Widgets
WIDGETS = 95

# user input total number of widgets
num = int(input("How many widgets are you purchasing? \t"))

# calculates total price
total = WIDGETS * num

#discount calculator
if num >= 100:
    discount = total * .40
    total = total - discount
elif num <=99 and num >= 50:
    discount = total * .30
    total = total - discount
elif num <= 49 and num >= 20:
    discount = total * .20
    total = total - discount
elif num <= 19 and num >= 10:
    discount = total * .10
    total = total - discount
else:
    total

# Displays final total
print(total)
