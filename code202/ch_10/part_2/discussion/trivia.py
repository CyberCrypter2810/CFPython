# trivia.py

'''
Program asks 2 users to create 5 questions
and answers for the other user. Once all questions
and answers are completed, they will be stored in a tuple
for a class and then the program will challenge the other
user to answer the questions. User with the highest points
wins the game.
'''

import questions

# main funciton
def main():
    # create player variable
    player1 = 'Player 1'
    player2 = 'Player 2'

    # get questions from players
    play1Question = get_questions(player1)
    play2Question = get_questions(player2)

    # play the game
    print("Answer the questions.\n" +
    "The player with the most correct answers wins the game.")
    print()

    play1 = play(player1, play2Question)
    play2 = play(player2, play1Question)

    # determines and displays the results
    display(play1, play2)


# get_questions funciton
def get_questions(players):
    # create list for players questions and answers
    player = []

    # asks player for their questions and answers
    print(players + ": Please enter 5 questions and answers")
    for create in range(1, 6):
        question = input("Question #" + str(create) + ": ")
        ans1 = input("A: ")
        ans2 = input("B: ")
        ans3 = input("C: ")
        ans4 = input("D: ")

        # asks user to input the correct answer
        correct = input("Which letter is the correct answer? ")

        # upper case the letter
        correct = correct.upper()

        # error loop for correct answer
        while correct != 'A' and correct != 'B' and correct != 'C' and correct != 'D':
            print()
            print("Error, Correct answer does not match any \n" +
            "of the assign answers. Please try again.")
            correct = input("Which letter is the correct answer? ")
            correct = correct.upper()
            print()

        # sends question and answers to class
        trivia = questions.Question(question, ans1, ans2, ans3, ans4, correct)

        # append player 1 list
        player.append(trivia)

    # change player1 list to a tuple
    player = tuple(player)

    # clears screen for next player
    for x in range(100):
        print()

    # return player tuple
    return player


# play function
def play(player, question):
    # count variables
    count = 1
    points = 0

    # display the questions for player to answer
    print(player, ": Here are your questions.")
    print()

    for item in question:
        print("Question #" + str(count))
        print()
        print(str(item))
        ans = input("Which is the correct answer: ")
        # upper case the answer letter
        ans = ans.upper()

        # error loop if answer is not one that is provided
        while ans != 'A' and ans != 'B' and ans != 'C' and ans != 'D':
            print()
            print('Error, answer given is not one that is provided. \n' +
            "Please try again.")
            ans = input("Which is the correct answer: ")
            ans = ans.upper()
            print()

        # determine if answer provided is the correct answer.
        if ans == item.get_correct():
            points += 1
            print()
            print("That answer is correct.")
            print()
        else:
            print()
            print("Sorry, that answer is not correct.")
            print()

        # count variable for displaying questions
        count += 1

    # asks player to move controls over to the other player by hitting enter
    input("Press enter when your done seeing this.")

    # clears screen for next player
    for x in range(100):
        print()

    # return players points
    return points


# display function
def display(player1, player2):
    # determine who win the trivia
    print("Player 1 has " + str(player1) + " points.")
    print("Player 2 has " + str(player2) + " points.")
    if player1 > player2:
        print("Player 1 wins the trivia.")
    elif player1 < player2:
        print("Player 2 wins the trivia.")
    else:
        print("The trivia ended in a tie.")


# calling main
main()
