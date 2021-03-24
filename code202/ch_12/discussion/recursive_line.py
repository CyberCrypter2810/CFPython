# recursive_line.py

'''
Program prints lines of asterisks based on
a certain number. The function will have a recursion
until the certain number has been reached both up and
down.
'''

# main function
def main():
    # asks user for an input
    n = int(input("Enter a integer number: "))
    
    # calls up_line funciton
    up_line(n)
    
    # calls the down line function
    down_line(n - 1)


# up_line function
def up_line(n):
    if n > 0:
        up_line(n-1)
        lines = '*' * n
        print(lines)


# down_line function
def down_line(n):
    if n > 0:
        lines = '*' * n
        print(lines)
        down_line(n - 1)


# calling main
main()
