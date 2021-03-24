# Word_frequency.py

'''
Program reads the contents of a text file
and creates a dictionary to display
the frequency of the mentioned word.
'''

# main function
def main():
    # create dictionary
    frequent = {}

    # opening file
    file = open('frequency.txt', 'r')

    # puts file into list and sorts out all words
    for line in file:
        file_list = line.split()

        # sorts out periods and commas
        list = sort(file_list)

        # sorts words and put them into frequent dictionary
        for index in list:
            if index in frequent:
                frequent[index] += 1
            else:
                frequent[index] = 1

    # closed file
    file.close()

    # displays frequent dictionary
    print()
    print("Here are the list of words that have been mentioned " +
    "in the file in alphabetical order.")
    print()

    for key in sorted (frequent.keys()):
        print(key, frequent[key])

    print()


# sort function
def sort(file_list):
    # create sorted list
    sorted = []

    for words in file_list:

        # create list
        list = []

        for letter in words:
            list.append(letter)
            # checks each index for periods or commas.
            # if any, remove them
            for index in list:
                if index == '.' or index == ',':
                    list.remove(index)

        # recreate word statements
        word = ''
        for letter in list:
            word += letter

        # puts word into sorted list
        sorted.append(word)

    # returns sorted
    return sorted


# calling main
main()
