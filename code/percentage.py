# percentage.py

# Ask user to input original price of product with percentage discount
# in whole numbers.
original_price = float(input("Enter the original product price: $"))
percent = float(input("Enter the discount percent: "))

# changes whole percent number to decimal number.
percent = percent * 0.01

# Calculates the discount amount.
discount = original_price * percent

# Calculates the final sales price.
sale_price = original_price - discount
print("The sale price is: $" + format(sale_price, '.2f'))
