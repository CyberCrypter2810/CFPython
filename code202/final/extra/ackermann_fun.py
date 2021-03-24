# Ackermann's_fun.py

'''
Program will takes a small number
and does a recursive mathematical algorithm
to test the speed of the program.
'''

# main function
def main():
    # getting values
    m = 3
    n = 2
    
    # start recursive and display results
    print(ackermann(m, n))


# ackermann function
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


# calling main
main()