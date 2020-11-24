# Rose_Theater.py

# Create a Global Constant for price.
ORCHESTRA = 75
CENTER = 50
OUTER = 25


# main fuction
def main():
    # calls get functions.
    orchestra = get_orchestra()
    center = get_center()
    outer = get_outer()

    # calculates final total.
    final_total = orchestra + center + outer

    # Calculates discount if user is a member.
    answer = input("Are you a local member? (Enter y for yes) ")
    if answer == 'y' or answer == 'Y':
        print("Final Total of seats purchased is: $" + str(final_total))
        print('Discount is 5%')
        discount = final_total * 0.05
        final_total -= discount
        # displays final total with discount
        print("Final Total with discount is: $" + str(final_total))
    else:
        # Prints results without discount.
        print("Final Total of seats purchased is: $" + str(final_total))


# orchestra fuction
def get_orchestra():
    # ask user for input.
    user = int(input("How many Orchestra seats do you want to purchase? "))
    orchestra_final = user * ORCHESTRA
    print("$" + str(orchestra_final))

    # Returning results
    return orchestra_final


# center function
def get_center():
    # ask user for input.
    user = int(input("How many Center Stage seats do you want to purchase? "))
    center_final = user * CENTER
    print("$" + str(center_final))

    # Return results
    return center_final


# outer function
def get_outer():
    user = int(input("How many Outer Stage seats do you want to purchase? "))
    outer_final = user * OUTER
    print("$" + str(outer_final))

    # Return results
    return outer_final


# calling main function
main()
