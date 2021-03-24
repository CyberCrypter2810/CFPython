# recursive_line.py

'''
Program prints lines of asterisks based on
a certain number. The function will have a recursion
until the certain number has been reached.
'''

# main function
def main():
    # calls line funciton
    line(1)


# line function
def line(n):
    if n < 10:
        lines = '*' * n
        print(lines)
        line(n + 1)


# calling main
main()
