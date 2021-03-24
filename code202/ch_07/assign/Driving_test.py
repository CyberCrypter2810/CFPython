# Driving_test.py
'''
Program takes user input and determine whether the input
is correct in the answer tuple.
'''

# main function
def main():
    # answers for test
    answers = ('A', 'C', 'A', 'A', 'D',
              'B', 'C', 'A', 'C', 'B',
              'A', 'D', 'C', 'A', 'D',
              'C', 'B', 'B', 'D', 'A')
    
    print("ALL Answers must be in CAPS.")
    # Calling Test
    user_answers = testing()
    
    # Calling calculation
    right_results, wrong_results = calculation(answers, user_answers)
    
    print()
    
    # Calling display
    display(right_results, wrong_results)


# testing function
def testing():
    # creating user answer list
    answers = []
    
    # accumulator for reading the file and error loop
    read = 0
    
    # opening exam file
    exam = open('Driving_Questions.txt', 'r')
    
    # displaying questions and asking user for answers
    for line in exam:
        line = line.rstrip('\n')
        print(line)
        read += 1
        
        # stops read for user to enter answer
        if read == 5:
            ans = input('Which is the correct answer: ')
            
            # Determins if answer is acceptible (error loop)
            while ans != 'A' and ans != 'B' and ans != 'C' and ans != 'D':
                print("Error, answer inputed is not verifiable.")
                print("Please try again.")
                ans = input("Which is the correct answer: ")
            
            # puts user answer at end of answers list
            answers.append(ans)
            
            # resets read accumulator
            read = 0
        
    # Closes file
    exam.close()
    
    # return answers
    return answers


# calculation function
def calculation(answer, user_answer):
    # Right and Wrong lists
    right = []
    wrong = []
    
    # accumulator
    count = 0
    
    for item in answer:
        if item == user_answer[count]:
            right.append(count)
        else:
            wrong.append(count)
        
        count += 1
    
    # return right and wrong
    return right, wrong
  

# display function
def display(right_results, wrong_results):
    # accumulator
    correct = 0
    wrong = 0
    
    # Calculating the number of correct answers
    for item in right_results:
        correct += 1
        
    for item in wrong_results:
        wrong += 1
    
    # displays final results
    print("The final number of correct answers are: ", correct)
    print("The final number of wrong answers are: ", wrong)
    
    # displays all wrong answers if any
    if wrong > 0:
        print("The wrong answers are: ")
        for item in wrong_results:
            print("Question", item + 1)
        
    # Tells tester if they passed or failed
    if wrong > 5:
        print("You have failed the exam. Better luck next time.")
    else:
        print("You have passed the exam! Congradulations!")


# calling main
main()