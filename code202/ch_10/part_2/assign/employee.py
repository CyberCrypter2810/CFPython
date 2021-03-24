# employee.py

'''
Program create employee class
for program management.
'''

class Employee:

    # initiate
    def __init__(self, name, number, department, title):
        self.__name = name
        self.__number = number
        self.__department = department
        self.__title = title

    # mutator
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    # accessor
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title

    # display
    def __str__(self):
        return "Name: " + (self.__name) +\
        "\nID Number: " + str(self.__number) +\
        "\nDepartment: " + str(self.__department) +\
        "\nJob Title: " + str(self.__title)
