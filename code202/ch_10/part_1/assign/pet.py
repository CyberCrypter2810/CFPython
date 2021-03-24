# pet.py

'''
Pet class attributes data for the
certain type of pet for pet_info.py.
'''

# create Pet class
class Pet:
    # initiate class
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # mutater methods
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # accessor methods
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    # display method
    def __str__(self):
        return 'Name: ' + (self.__name) +\
        '\nAnimal Type: ' + str(self.__animal_type) +\
        '\nAge: ' + str(self.__age)
