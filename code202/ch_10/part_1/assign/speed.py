# speed.py

'''
Program creates a speed dial when called appond. It
will then display the current speed of the car.
'''

import car

# main function
def main():
    # create values for car class
    year_model = int(input("Enter the year model: "))
    make = input("What type of car is it? ")
    speed = 0

    # sends data to car class
    design = car.Car(year_model, make, speed)

    # call the accelerate method 5 times and displays results
    print()
    for i in range(5):
        design.accelerate(speed)
        print(design)

    # call the brake method 5 times and displays results
    print()
    for i in range(5):
        design.brake(speed)
        print(design)


# calling main
main()
