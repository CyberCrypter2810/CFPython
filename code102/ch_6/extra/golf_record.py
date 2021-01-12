# golf_record.py

'''
Program takes user name and score input,
stores the entered data into golf.txt file.
'''

# main function
def main():
    try:
        # open golf.txt file
        golf = open('golf.txt', 'w')

        # getting number of players
        player = int(input("How many players are going to be playing? "))
        # get number of courses players are going to play
        course = int(input("How many courses are you playing today? "))

        # loops for player data
        for play in range(1, player + 1):
            # get player name
            name = input("Enter player #" + str(play) + " name: ")
            # write player name to file
            golf.write(name + "\n")
            # gather and record scoring data
            for hole in range(1, course + 1):
                score = int(input("Enter score for hole #" + str(hole)
                + ": "))
                golf.write(str(score) + " | ")
            golf.write('\n\n')
            print()

    except ValueError:
        print("ERROR: data entered has to be a valid number.")

    finally:
        golf.close()
        print("All data has been save to golf.txt")


# calling main
main()
