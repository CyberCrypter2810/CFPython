# payroll.py

# Setting control loop
another = 'y'
while (another == 'y' or another == 'Y'):
    # Setting pay for day
    rate = 1

    # receives user input for # of days worked
    pay = int(input("How many days did you work? "))
    # Corrects pay variable for the
    # "for" loop.
    pay += 1
    # Creating Chart
    print("Day\tPay")
    print("------------")

    # create loop for calculating each result
    for day in range (1, pay):
        print(day, '\t', rate)
        # Since rate starts at 1, must reduce by 1
        # for proper results.
        final = rate + rate - 1
        rate *= 2

        # Calculating and displaying final result
    final /= 100
    print("\nTotal pay is: " + format(final, '.2f'))

    # Asking user if they have more payrolls
    another = input("Do you have any more payrolls to enter? (Enter y for yes): ")

    # ending the program.
    if another != 'y':
        print("Ending program.")
