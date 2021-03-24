# Magic_square.py

'''
Program takes user input and make a table to
determine if the table context makes up a 
Lo Shu Magic Square.
'''

# Global Variables
ROWS = 3
COLS = 3

# main function
def main():
    # create table list
    table = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    
    # Calling collect
    collection = collect(table)
    
    # calling calculation
    cal = calculation(collection)
    
    # calling results
    results(collection, cal)


# collect function
def collect(table):
    # Create a usable list of numbers that user has and hasn't used
    usable = [1,2,3,4,5,6,7,8,9]
    
    # collect data for table
    for r in range(ROWS):
        for c in range(COLS):
            print("Here is your current table")
            for item in table:
                print(item)
            print("Your available numbers are: ", usable)
            table[r][c] = int(input("Enter a number for row " + str(r+1) +
                                    " column " + str(c+1) + ": "))
            
            # removes number from usable list if it hasn't been inputed
            usable.remove(table[r][c])
    
    # return table
    return table


# calculation function
def calculation(table):
    # calculates total of rows, columns, and diagonals
    row1 = table[0][0] + table[0][1] + table[0][2]    # row 1
    row2 = table[1][0] + table[1][1] + table[1][2]    # row 2
    row3 = table[2][0] + table[2][1] + table[2][2]    # row 3
    dia1 = table[0][0] + table[1][1] + table[2][2]    # diagonal 1
    dia2 = table[2][0] + table[1][1] + table[0][2]    # diagonal 2
    col1 = table[0][0] + table[1][0] + table[2][0]    # column 1
    col2 = table[0][1] + table[1][1] + table[2][1]    # column 2
    col3 = table[0][2] + table[1][2] + table[2][2]    # column 3
    
    # count accumulator
    count = 0
    
    # Determines if table is a Lo Shu Magic Square
    if row1 and row2 and row3 == 15:
        count += 1
    if col1 and col2 and col3 == 15:
        count += 1
    if dia1 and dia2 == 15:
        count += 1
    
    # Sets flag for Magic Square
    if count == 3:
        flag = True
    else:
        flag = False
    
    #print(flag)
    
    # Returns flag
    return flag


# results function
def results(table, flag):
    # Displays final results
    print()
    print("Here is your table")
    
    for item in table:
        print(item)
    
    if flag == True:
        print("This is a Lo Shu Magic Square.")
    else:
        print("This is not a Lo Shu Magic Square.")


# calling main
main()