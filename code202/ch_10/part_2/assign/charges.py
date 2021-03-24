# charges.py

'''
Program asks for user information and send
data to Patient class. Then ask user what procedure
they are going to do. It will then display patient's
information and all procedure charges.
'''
import patient
import procedure

# main function
def main():
    # calling set_procedure
    procedure = set_procedure()

    # calling user_info
    info = user_info()

    # calling display
    display(info, procedure)


# set_procedure function
def set_procedure():
    # create list for patients
    table = []

    # set loop for table
    for x in range(1, 4):
        date = "Today's date"
        if x == 1:
            name = 'Physical Exam'
            practitioner = 'Dr. Irvine'
            charge = 250.00
        elif x == 2:
            name = 'X-ray'
            practitioner = 'Dr. Jamison'
            charge = 500.00
        else:
            name = 'Blood test'
            practitioner = 'Dr. Smith'
            charge = 200.00

        # sends procedure information to procedure class
        proceed = procedure.Procedure(name, date, practitioner, charge)

        # append the table list
        table.append(proceed)

    # return table list
    return table


# user_info function
def user_info():
    # asks for user information
    print("What is your first, middle, and last name?")
    name = input()
    print("What is your full address?")
    address = input()
    print("What is your phone number?")
    phone = int(input())
    print("What is the name of your emergency contact and number?")
    emergency = input()

    # sends user info to the patient class
    info = patient.Patient(name, address, phone, emergency)

    # return info
    return info


# display function
def display(info, table):
    # displays name of user_info
    print()
    print(str(info))

    # set charages accumulator
    charges = 0

    # displays procedures
    for item in table:
        print()
        print(str(item))
        charges += item.get_charge()

    print()
    print("Total charges for all three procedures are: $" + str(charges))


# calling main()
main()
