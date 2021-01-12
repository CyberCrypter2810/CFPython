# tax_calculation.py

# tax percentage of state and county
STATE_TAX = 0.06
COUNTY_TAX = 0.035

# asking user to input product price
price = float(input("Enter price of product: $"))

# calculating input price with tax percentage
state_tax = price * STATE_TAX
county_tax = price * COUNTY_TAX
total_tax = state_tax + county_tax

# final calculation with tax calculation
final_sale = price + total_tax

# outputting input and final calculations
print("Price: $" + format(price, '.2f') + "\n")
print("State Tax: $" + format(state_tax, '.2f'))
print("County Tax: $" + format(county_tax, '.2f') + "\n")
print("Total Tax: $" + format(total_tax, '.2f'))
print("Total: $" + format(final_sale, '.2f'))
