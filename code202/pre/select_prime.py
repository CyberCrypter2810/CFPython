# select_prime.py

'''
This program takes integer input from user
and determins if the integer is a prime number
or not.
'''

# main function
def main():
    # again loop
    again = 'y'
    while again == 'y' or again == 'Y':

        # gets input from user
        num = int(input("Enter a number: "))

        # calling is_prime
        prime = is_prime(num)

        # Displays is_prime findings
        if prime == True:
            print("The number is a prime number.")
        else:
            print("The number is not a prime number.")

        # asking user if they want to input another number
        print("Do you want to input another number?")
        again = input("(Y or y for yes): ")

        # notifying the end of program
        if again != 'y' and again != 'Y':
            print("Ending program.")


# is_prime function
def is_prime(num):
    # setting accumulator
    zero = 0
    # calculating if num is prime
    if num > 1:
        for count in range(1, num):
            prime = num % count
            # determin how many 0 remainders been calculated
            if prime == 0:
                zero += 1
        # determin if number is prime or not
        if zero > 1:
            flag = False
        else:
            flag = True
    else:
        flag = False

    # return flag
    return flag


# Calling main
main()
