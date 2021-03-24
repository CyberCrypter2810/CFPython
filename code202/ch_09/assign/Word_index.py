# Word_index.py

'''
Program takes contents of a text file and
assigns them to a dictionary. The dictionary
will then provide which line the certain word
had been mentioned.

'Used the example from the book.'
'''

# main function
def main():
    # accumulator
    count = 0

    # create dictionary
    index = {}

    # open the file
    file = open('Kennedy.txt', 'r')

    # read the file
    for line in file:
        count += 1
        list = line.split()

        # calling filter function
        filter_list = filter(list)

        # calls sort function
        sort(filter_list, index, count)

    # close file
    file.close()

    # takes index and puts findings into a text file
    # in alphabetical order
    file = open('index.txt', 'w')
    for key in sorted (index.keys()):
        file.write(key + index[key] + '\n')
    file.close()

    # reopens index.txt and displays it's contents
    file = open('index.txt', 'r')
    print()
    for line in file:
        line = line.rstrip('\n')
        print(line)

    print()

    file.close()


# filter function
def filter(line_list):
    # create a finished list
    finished = []

    # filters out the periods and commas
    for words in line_list:
        # create a list
        list = []

        # Break word down by the letter and append the letter to list
        for letter in words:
            list.append(letter)

        # Check for any commas or periods
        for index in list:
            if index == '.' or index == ',':
                list.remove(index)

        # Place word back together
        word = ''
        for letter in list:
            word += letter

        # append final word to the finished list
        finished.append(word)

    # checks for any duplicate words in the line
    # and removes them
    finished = dict.fromkeys(finished)

    # returns finished
    return finished


# sort function
def sort(list, index, count):
    # sorts the list of words and to which line they appear
    for item in list:
        if item in index:
            index[item] += ', ' + str(count)
        else:
            index[item] = ': ' + str(count)


# calling main
main()
