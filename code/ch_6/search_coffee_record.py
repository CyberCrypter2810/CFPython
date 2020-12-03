# search_coffee_records.py

'''
Program allows user to search the coffee.txt file
for records matching a description.
'''

# main function
def main():
    # create bool variable as a flag
    found = False

    # Get search value
    search = input("Enter a description to search for: ")

    # Open coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    # Read first records description field
    descr = coffee_file.readline()

    # Read rest of file
    while descr != '':
        # Read the quantity field
        qty = float(coffee_file.readline())

        # Strip the \n from description
        descr = descr.rstrip('\n')

        # Determine whether this record matches with search value
        if descr == search:
            # Display record
            print("Description:", descr)
            print("Quantity:", qty)
            print()
            # Set found flag to True
            found = True

        # Read next description
        descr = coffee_file.readline()

    # Close file
    coffee_file.close()

    # If search was not found, display message.
    if not found:
        print("That item was not found in the file.")


# calling main function
main()
