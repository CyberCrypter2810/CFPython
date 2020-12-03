# average_temperature.py

'''
Program displays results from temperature.txt file
and then calculates the average of the results.
'''

# main function
def main():
    # Sets up accumulator
    total = 0
    average = 0

    try:
        # Open temperature.txt
        temp = open('temperature.txt', 'r')

        # Displaying and calculating total values from file.
        for line in temp:
            average += 1
            result = int(line)
            print("Day", str(average) + ":", format(result, '.0f'))
            total += result
        print()

    except Exception as error:
        print(error)
        print("An error has occurred because the file doesn't exist.")

    else:
        # Calculates average of total
        final = total / average

        # Display final average results
        print("The average temperature in the 7 recorded days is:",
        format(final, '.0f'), "degress Fahrenheit.")


    # Closes file when program ends.
    finally:
        temp.close()


# calling main
main()
