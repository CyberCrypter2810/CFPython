# addition_quiz.py

import random

# main function
def main():
    num1 = random.randint(0, 500)
    num2 = random.randint(0, 500)
    total = num1 + num2

    print('  ', num1, '\n +', num2)
    answer = int(input("What is the answer to the equation above? "))

    if answer == total:
        print("That is the correct answer.")
    else:
        print("Sorry, that isn't the right answer.")
        print("The Correct answer is", total)


# calling main function
main()
