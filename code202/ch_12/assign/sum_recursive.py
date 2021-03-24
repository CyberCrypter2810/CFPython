# sum_recursion.py

'''
Program takes a integer argument and
returns the sum of all numbers
from 1 on up to said number.
'''

# main function
def main():

    number = int(input("Enter an integer: "))
    answer = 0
    add(number, answer)


# add function
def add(num, ans):
    if num > 0:
        ans += num
        print(ans, end=" ")
        add(num - 1, ans)


# calling main
main()
