# record_temperature.py

'''
Program gathers seven temperature data from user
and stores the data in a file called temperature.txt.
'''

# main function
def main():
    try:
        # create file
        temp = open('temperature.txt', 'w')

        # create loop for seven inputs
        for count in range(1,8):
            data = int(input("Enter temperature for day #" + str(count) +
            " (In Fahrenheit): "))
            temp.write(str(data) + "\n")

    # Error execption protocal if user enters float or letters
    except ValueError:
        print("ERROR: temperature must be in valid numbers.")
        print("Data entered before this ERROR has been saved.")

    # Closes file for data saving also alerting user.
    finally:
        temp.close()
        print("Data has been saved in temperature.txt")


# call main function
main()
