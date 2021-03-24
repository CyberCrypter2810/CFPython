# pet_info.py

'''
Program takes inputted data from user
and stores them in the Pet class.
It will then retrieve the data from the
pet class.
'''

# importing pet.py
import pet

# main function
def main():
    # create a list for pet info
    animal = []

    # ask user how many pets they have
    num = int(input("How many pets do you have? "))

    # loop for creating data for pet class
    for var in range(1, num+1):
        name = input("What is the name of your " + str(var) + " pet? ")
        animal_type = input("What type of pet is it? ")
        age = int(input("How old is your pet? "))

        # sends data to pet class
        pets = pet.Pet(name, animal_type, age)

        # append the pet list
        animal.append(pets)

    # displays data from pet
    for item in animal:
        print()
        print(str(item))


# calling main
main()
