# average.py

# collects three numbers from users
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# calculate the average/mean of all three numbers
average = (num1 + num2 + num3) / 3.0

# displays final calculation
print("The average of all three numbers is: " + format(average, '.2f'))
