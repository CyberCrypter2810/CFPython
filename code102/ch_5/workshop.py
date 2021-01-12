# workshop.py
# program asks user what
# A: workshop they want to attend
# B: what location to attend the workshop
# C: display the final total of workshop and lodging


# main fuction
def main():
    # calling following functions:

    # workshop menu
    workshop_menu()
    # workshop_selection
    workshop, day = workshop_selection()
    # loation
    location_menu()
    # Lodging_selection
    lodging = lodging_selection()
    # total
    total(workshop, lodging, day)


# menu function
def workshop_menu():
    print ('\t\t\tMENU WORKSHOP SELECTOR')
    print ('\tWORKSHOPS \tRegistration Fee \tDays')
    print ('1) Handling Stress \t$1000 \t\t\t3 ')
    print ('2) Time Management\t$800 \t\t\t3 ')
    print ('3) Supervision Skills\t$1500 \t\t\t3 ')
    print ('4) How to Interview \t$500 \t\t\t1\n')


# workshop function
def workshop_selection():
    # ask user to select workshop
    workshop = int(input("What workshop do you want to attend? \t"))
    print("\n")

    # creating an error loop
    while workshop < 0 or workshop > 4:
        print("Error, no options exist. please try again.")
        workshop = int(input("What workshop do you want to attend? \t"))
        print('\n')

    # Determining workshop price and days
    if workshop == 1:
        price = 1000
        day = 3
    elif workshop == 2:
        price = 800
        day = 3
    elif workshop == 3:
        price = 1500
        day = 3
    else:
        price = 500
        day = 1

    # Returning price and day
    return price, day


# location function
def location_menu():
    print ('\tLOCATION \tLodging Fee per Day')
    print ('1) Austin \t\t$150')
    print ('2) Chicago\t\t$225 ')
    print ('3) Phoenix\t\t$175 ')
    print ('4) Orlando\t\t$300 \n')


# lodging fuction
def lodging_selection():
    # ask user to select location
    location = int(input("Which location do you want to attend? \t"))
    print('\n')

    # creating an error loop
    while location < 0 or location > 4:
        print("Error, no options exist. Please try again.")
        location = int(input("Which location do you want to attend? \t"))
        print('\n')

    # Determining location price
    if location == 1:
        price = 150
    elif location == 2:
        price = 225
    elif location == 3:
        price = 175
    else:
        price = 300

    # returning price
    return price


# total function
def total(workshop, lodging, day):
    # Calculates total of lodging options
    final_lodging = lodging * day
    # calculates final total
    final_total = workshop + final_lodging

    # Displaying final results
    print("Registration: $" + str(workshop))
    print("Lodging: $" + str(lodging) + " x " + str(day) + " days = $" + str(final_lodging))
    print("Total: $" + str(final_total))


# calling main function
main()
