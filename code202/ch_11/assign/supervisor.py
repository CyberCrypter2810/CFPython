# supervisor.py

'''
Program takes input from user about
supervisor information. It will then
determine if said supervisor gets a bonus
if a certain number has been reached.
The program will then display the results as
at the end.
'''
import shift

# main function
def main():
    # collect data about supervisor
    print("Enter information about this supervisor.")
    name = input("Name: ")
    number = input("Number: ")
    print("What is the total salary did " + name + " earned for the company " +
    "during his/her shift?")
    salary = float(input("$"))

    # determine if supervisor gets bonus. Number can be changed
    if salary >= 300:
        bonus = 100
    else:
        bonus = 0

    supervisor = shift.ShiftSupervisor(name, number, salary, bonus)

    # displays supervisor info
    print()
    print(str(supervisor))
    print()


# calling main
main()
