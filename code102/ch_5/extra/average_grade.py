# average_grade.py

'''
This program calculates the grade based on the
test scores provided by the user.
'''

# main function
def main():
    # calling functions
    grade = calc_average()
    letter = determine_grade(grade)

    # prints final results
    print()
    print("The students final average grade is: ", format(grade, '.1f'))
    print("This results into an letter grade of: ", letter)


# calc_average function
def calc_average():
    # create variables
    total = 0
    average = 5
    # telling user what to do.
    print("Please enter the five test scores of said student.")
    # create a count loop for user to enter test results
    for count in range(1, average + 1):
        user = int(input("What is the result of test number " + str(count) + ': '))
        total += user
    # calculate final score average
    final = total / average

    # return final
    return final


# determine_grade function
def determine_grade(grade):
    # Determining the grade letter
    if grade <= 100 and grade >= 90:
        letter = 'A'
    elif grade < 90 and grade >= 80:
        letter = 'B'
    elif grade < 80 and grade >= 70:
        letter = 'C'
    elif grade < 70 and grade >= 60:
        letter = 'D'
    else:
        letter = 'F'

    # returning letter results
    return letter


# Calling main function
main()
