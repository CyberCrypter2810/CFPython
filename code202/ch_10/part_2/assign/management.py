# management.py

'''
Program open file of employees.dat and
provides options to:

look up an employee
add a new employee
change info on said employee
delete an employee
quit the program

When program is done, it then takes said items
and pickles them into a file for storage.
'''

import employee
import pickle

# global variables
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# global name for the file
FILENAME = 'employee.dat'

# main function
def main():
    # load existing employees dictionary
    my_employees = load_employees()

    # set choice value
    choice = 0

    # Process menu selection until user
    # quits the program
    while choice != QUIT:
        # get user's choice
        choice = menu_choice()

        # Process said choice
        if choice == LOOK_UP:
            look_up(my_employees)
        elif choice == ADD:
            add(my_employees)
        elif choice == CHANGE:
            change(my_employees)
        elif choice == DELETE:
            delete(my_employees)

    # save my_employees to employees.dat file
    save(my_employees)


# menu_choice function
def menu_choice():
    # displays menu and asks user
    # what option to choose.
    print()
    print("MENU")
    print('--------------------------')
    print("1: Look up an employee")
    print("2: Add a new employee")
    print("3: Change details on existing employee")
    print("4: Delete an employee")
    print("5: Quit the program")
    print()

    # ask user to input their choice
    choice = int(input("Enter your choice: "))
    print()

    # Validate said choice
    while choice < LOOK_UP or choice > QUIT:
        print("That option is not available. Please try again.")
        print()
        choice = int(input("Enter your choice: "))
        print()

    # return choice
    return choice


# load_employees function
def load_employees():
    try:
        # opens FILENAME
        file = open(FILENAME, 'rb')

        # unpickle dictionary
        employees = pickle.load(file)

        # close FILENAME
        file.close()

    except IOError:
        # If file does not exist,
        # create an empty dictionary
        employees = {}

    # return employees
    return employees


# look_up function
def look_up(employees):
    # ask for a name to look up
    number = int(input("Enter the employee ID Number: "))

    # Look name up in the dictionary
    print(employees.get(number, 'That employee does not exist.'))


# add function
def add(employees):
    # add new data into employee dictionary
    # Get employee info
    name = input("Name: ")
    number = int(input("ID Number: "))
    department = input("Department: ")
    title = input("Job title: ")

    # create object for employee entry
    entry = employee.Employee(name, number, department, title)

    # check to make sure if number is already in the dictionary.
    # If not, add said number as a key
    if number not in employees:
        employees[number] = entry
        print("New employee data has been added.")
    else:
        print("Employee already exist.")


# change function
def change(employees):
    # changes data on existing employee
    # get name
    number = int(input("Enter the employees ID Number: "))

    if number in employees:
        # get new data
        name = input("Enter a new name for existing employee: ")
        department = input("Enter the new department: ")
        title = input("Enter the new job title: ")

        # create object with entry
        entry = employee.Employee(name, number, department, title)

        # update entry to dictionary
        employees[number] = entry
        print("Employees data has been updated.")

    else:
        print("That employee does not exist.")


# delete function
def delete(employees):
    # delete data with said employee
    # get name for deletion
    number = int(input("Enter an employees ID Number: "))

    if number in employees:
        del employees[number]
        print("Employees data has been deleted.")

    else:
        print("That employee does not exist.")


# save function
def save(employees):
    # open file for writing
    file = open(FILENAME, 'wb')

    # pickle dictionary and save data
    pickle.dump(employees, file)

    # close file
    file.close()


# calling main
main()
