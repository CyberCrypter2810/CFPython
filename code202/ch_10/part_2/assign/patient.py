# patient.py

'''
Program create class called patient
for charges program.
'''

class Patient:
    # initiate
    def __init__(self, name, address, phone, emergency):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__emergency = emergency

    # mutator
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_emergency(self, emergency):
        self.__emergency = emergency

    # accessor
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_emergency(self):
        return self.__emergency

    # display patient
    def __str__(self):
        return "Name: " + (self.__name) +\
        "\nAddress: " + str(self.__address) +\
        "\nPhone: " + str(self.__phone) +\
        "\nEmergency Contact: " + str(self.__emergency)
