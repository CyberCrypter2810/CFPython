# customer.py

'''
Program takes user input and provide the input to
classes in person.py. The program will then display
the results at the very end.
'''

import person

# main function
def main():
    print("Enter the following information.")
    name = input("Name: ")
    address = input("Address: ")
    phone = input("Phone Number: ")
    id = input("Customer ID: ")
    print("Does customer want to have an email subscription?")
    mail = input("(Y = yes, N = no): ")
    # lower the letter value in mail
    mail = mail.lower()

    customer_info = person.Customer(name, address, phone, id, mail)

    # display results
    print()
    print("Here is the data the you have entered.")
    print(str(customer_info))
    if customer_info.mail_sub():
        print("Subscription: ON")
    else:
        print("Subscription: OFF")
    print()


# calling main
main()
