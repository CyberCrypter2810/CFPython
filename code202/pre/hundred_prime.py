# hundred_prime.py

'''
Program displays all prime numbers from
1 to 100.
'''

# main function
def main():
    # prints beginning of final
    print("Prime number from 1 to 100 are: ")

    # count variable
    table = 0

    # range loop
    for num in range(1, 101):
        # calls is_prime function
        prime = is_prime(num)

        # table the results
        if table == 12:
            print()
            table = 0

        if prime == True:
            print(num, end=' ')
            table += 1

    print()


# is_prime function
def is_prime(num):
    # set accumulator
    zero = 0
    # Calculates if num is prime
    if num > 1:
        for count in range(1,num):
            prime = num % count
            if prime == 0:
                zero += 1
        # determines if num is prime
        if zero > 1:
            flag = False
        else:
            flag = True
    else:
        flag = False

    # returns flag
    return flag


# calling main
main()
