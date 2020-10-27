# payroll.py

# Inicial hours and overtime multiplier
BASE_HOURS = 40
OT_MULTIPLIER = 1.5

# Retrieving worked hours and pay rate
hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly pay rate: "))

# Calculating input for overtime
if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS
    overtime_pay = overtime_hours * OT_MULTIPLIER * pay_rate
    gross_pay = BASE_HOURS * pay_rate + overtime_pay

# Calculating input without overtime
else:
    gross_pay = BASE_HOURS * pay_rate

# Displaying calculations
print("The gross pay is: $", format(gross_pay, '.2f'), sep='')
