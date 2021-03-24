# questions.py

'''
Program holds classes for questions for the
trivia program.
'''

class Question:

    # initiate
    def __init__(self, question, ans1, ans2, ans3, ans4, correct):
        self.__question = question
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__correct = correct

    # accessor
    def get_correct(self):
        return self.__correct
        

    # display questions
    def __str__(self):
        return self.__question +\
        "\nA: " + str(self.__ans1) +\
        "\nB: " + str(self.__ans2) +\
        "\nC: " + str(self.__ans3) +\
        "\nD: " + str(self.__ans4)
