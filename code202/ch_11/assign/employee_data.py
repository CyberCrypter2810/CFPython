# employee_data.py

'''
Program asks for data entered by user
about employee information. The program will
display the results at the very end.
'''

import shift

# main function
def main():
    # collect data about employee
    name = input("Name: ")
    number = input("Number: ")
    print('1: Day')
    print('2: Night')
    time = int(input("Shift: "))
    rate = input("Rate: ")

    # Error loop for time variable
    while time < 1 or time > 2:
        print('Error. Shift entered earlier does not exist.')
        print('Please try again.')
        print()
        print('1: Day')
        print('2: Night')
        time = int(input('Which shift does this worker going to work in: '))

    employee = shift.ProductionWorker(name, number, time, rate)

    # retrieve & display data
    print()
    print(str(employee))
    print()


# calling main
main()
