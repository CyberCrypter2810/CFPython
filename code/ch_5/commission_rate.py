# commission_rate.py

# Program calculates salesperson's pay
# at Make Your Own Music
def main():
    # Get amount of sales.
    sales = get_sales()

    # Get amount of advance pay.
    advance_pay = get_advance_pay()

    # Determine commission rate
    comm_rate = determine_comm_rate(sales)

    # Calculate the pay.
    pay = sales * comm_rate - advance_pay

    # Display amount of pay.
    print('The pay is: $', format(pay, ',.2f'), sep='')

    # Determine if pay is negative.
    if pay < 0:
        print('The Salesperson must reimburse')
        print('the company.')


def get_sales():
    # Get monthly sales.
    monthly_sales = float(input("Enter the monthly sales: "))
    # Returning amount entered
    return monthly_sales


def get_advance_pay():
    # Get amount of advance pay.
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advanced pay was given.')
    advanced = float(input("Advance pay: "))

    # Return amount entered
    return advanced


def determine_comm_rate(sales):
    # Determining commission rate
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    # Returning the rate.
    return rate


# Calling main function.
main()
