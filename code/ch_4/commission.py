# commission.py

# This program calculates sales commissions.

# Creating a sentinal variable
keep_going = 'y'

# Calculate the series of commissions.
while keep_going == 'y':
    # Get salesperson's sales and commission rate.
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    # Calculates the commission.
    commission = sales * comm_rate

    # Display the commission.
    print("The commission is $",
        format(commission, ',.2f'), sep='')

    # See if user wants to input another one.
    keep_going = input("Do you want to calculate another " +
        "commission (Enter y for yes): ")
