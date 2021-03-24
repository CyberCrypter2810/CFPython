# car.py

'''
Program creates a Car class for speed.py.
'''

class Car:
    # initiate class
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # mutater methods
    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    # create speed
    def accelerate(self, speed):
        self.__speed += 5

    def brake(self, speed):
        if self.__speed >= 0:
            self.__speed -= 5
        else:
            print("Error, the car is not moving.")

    # accessor methods
    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    # display method
    def __str__(self):
        return "Current speed is: " + str(self.__speed)
