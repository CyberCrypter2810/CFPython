# Personal_info.py

'''
Program takes inputted information and assigns them
to a class called Personal_class. After information has
been inputted, the program retrieves the information from
the class.
'''
# import Personal_class module
import Personal_class

# main function
def main():
    # make list to store objects
    info = []

    # loop to input 3 persons info
    for people in range(1, 4):
        name = input("Enter the " + str(people) + " person's name: ")
        address = input("Enter the persons address: ")
        age = int(input("Enter the persons age: "))
        phone_number = input("Enter the persons phone number: ")

        # Send data to Personal class
        person = Personal_class.Personal(name, address, age, phone_number)

        # append list for reading
        info.append(person)

    # display data from Personal class
    for person in info:
        print()
        print("Name: ", person.get_name())
        print("Address: ", person.get_address())
        print("Age: ", person.get_age())
        print("Phone number: ", person.get_phone_number())


# calling main
main()
