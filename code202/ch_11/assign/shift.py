# shift.py

'''
Program creates classes Employee, ProductionWorker,
and ShiftSupervisor for program employee_data and supervisor.
'''

class Employee:

    # initiate
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # mutator
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    # accessor
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):

    # initiate
    def __init__(self, name, number, shift, rate):
        # Initiate the Employee class
        Employee.__init__(self, name, number)

        # initate shift and rate
        self.__shift = shift
        self.__rate = rate

    # mutator
    def set_shift(self, shift):
        self.__shift = shift

    def set_rate(self, rate):
        self.__rate = rate

    # accessor
    def get_shift(self):
        return self.__shift

    def get_rate(self):
        return self.__rate

    # display
    def __str__(self):
        return "Name: " + Employee.get_name(self) +\
        "\nNumber: " + Employee.get_number(self) +\
        "\nShift: " + str(self.__shift) +\
        "\nRate: " + str(self.__rate)


class ShiftSupervisor(Employee):

    # initiate
    def __init__(self, name, number, salary, bonus):
        # initiate the employee class
        Employee.__init__(self, name, number)

        # initate salary and bonus
        self.__salary = salary
        self.__bonus = bonus

    # mutator
    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, salary):
        self.__bonus = bonus

    # accessor
    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus

    # display
    def __str__(self):
        return "Name: " + Employee.get_name(self) +\
        "\nNumber: " + Employee.get_number(self) +\
        "\nSalary: $" + str(self.__salary) +\
        "\nBonus: $" + str(self.__bonus)
