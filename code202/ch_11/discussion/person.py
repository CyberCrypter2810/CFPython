# person.py

class Person:

    # initiate
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # mutator
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    # accessor
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


class Customer(Person):

    # initiate
    def __init__(self, name, address, phone, num, mail):
        super().__init__(name, address, phone)
        self.__num = num
        self.__mail = mail

    # mutator and accessor for num
    def set_num(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

    # Boolean for mail supscription
    def mail_sub(self):
        if self.__mail == 'y':
            return True

    # display
    def __str__(self):
        return "Name: " + Person.get_name(self) +\
        "\nAddress: " + Person.get_address(self) +\
        "\nPhone Number: " + Person.get_phone(self) +\
        "\nId Number: " + str(self.__num)
