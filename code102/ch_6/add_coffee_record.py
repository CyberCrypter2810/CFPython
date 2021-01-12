# add_coffee_record.py

'''
Program adds coffee inventory records to
coffee.txt file.
'''

# main function
def main():
    # variable control loop
    another = 'y'

    # Open coffee.txt file in append mode
    coffee_file = open('coffee.txt', 'a')

    # Add records to file
    while another == 'y' or another == 'Y':
        # Get coffee record data
        print("Enter the following coffee data:")
        descr = input("Description: ")
        qty = int(input("Quality (in pounds): "))

        # Append data to file
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Determine if user wants to add more data
        print("Do you want to add another record?")
        another = input("Y = yes, anything else = no: ")

    # Close the file
    coffee_file.close()
    print("Data has been added to coffee.txt")


# calling main function
main()
