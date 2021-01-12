# hawn_final.py

'''
Program take user input on the amout of lessons they want
to purchase and calculates the final total.
'''

# Price of each lessons
GUITAR = 29.99
PIANO = 20
FLUTE = 10

# main function
def main():
    try:
        # calling functions
        menu()
        price, number, lesson = select()
        print()
        fee = zoom()
        print()
        total(lesson, number, price, fee)

    except:
        print()

# menu function
def menu():
    print("Lesson Menu")
    print("Number \t Lesson \t Price per lesson")
    print("1: \t Guitar \t $29.99")
    print("2: \t Piano \t\t $20")
    print("3: \t Flute \t\t $10")
    print()
    print("If you decide to receive your lessons over Zoom,")
    print("there will be a $15 fee.")
    print()


# select function
def select():
    try:
        lesson = int(input("Which lesson do you want to take? "))

        # error loop
        while lesson < 1 or lesson > 3:
            print("ERROR, No option exist, please choose again.")
            lesson = int(input("Which lesson do you want to take? "))

        number = int(input("How many are you going to take? "))

        # error loop
        while number < 1:
            print("ERROR, You cannot have no less than 1 lesson.")
            number = int(input("How many are you going to take? "))

        # providing prise for input
        if lesson == 1:
            price = GUITAR * number
        elif lesson == 2:
            price = PIANO * number
        else:
            price = FLUTE * number

        # returns Price, number, and lesson
        return price, number, lesson

    except:
        print("ERROR, number value must be entered. Please try again.")


# zoom function
def zoom():
    # user input
    print("Are you going to take lessons through zoom?")
    zoom = input("(Enter y for Yes, anything else means no): ")

    # determining fee
    if zoom == 'Y' or zoom == 'y':
        fee = 15
    else:
        fee = 0

    # return fee
    return fee


# total function
def total(lesson, number, price, fee):
    # total price calculation
    final = price + fee

    # displaying final results
    if lesson == 1:
        print("$29.99 x", number, "= $" + format(price, ',.2f'))
        print("Fee = $" + str(fee))
        print("Your final total for", number, "Guitar lessons is: ")
        print("$" + format(final, ',.2f'))
    elif lesson == 2:
        print("$20 x", number, "= $" + format(price, ',.2f'))
        print("Fee = $" + str(fee))
        print("Your final total for", number, "Piano lessons is: ")
        print("$" + format(final, ',.2f'))
    else:
        print("$10 x", number, "= $" + format(price, ',.2f'))
        print("Fee = $" + str(fee))
        print("Your final total for", number, "Flute lessons is: ")
        print("$" + format(final, ',.2f'))


# calling main
main()
