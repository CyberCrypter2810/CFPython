# Word_list_analysis.py

'''
Program analyze words from two text files and gives
the results on similarities and differences.
'''

# main function
def main():
    # read files and puts them into sets
    file1 = set(read_files('word_list_1.txt'))
    file2 = set(read_files('word_list_2.txt'))

    # displays each set of words of each file
    display = 'first'
    display_files(file1, display)
    display = 'second'
    display_files(file2, display)

    # displays words that are in both files
    finish = 0
    both = file1.intersection(file2)
    print("Here are the words that are found in both files.")
    finish = results(both, finish)

    # displays words that are in the first but not the second
    both = file1.difference(file2)
    print("Here are the words that are found in the first file " +
    "but not the second.")
    finish = results(both, finish)

    # displays words that are in the second but not the first
    both = file2.difference(file1)
    print("Here are the words that are found in the second file " +
    "but not the first.")
    finish = results(both, finish)

    # displays words that are different in both files
    both = file1.symmetric_difference(file2)
    print("Here are the words that are not shared in both files.")
    results(both, finish)


# read_files function
def read_files(given_file):
    # create a list for the words
    list = []

    # open file to read
    file = open(given_file, 'r')

    # puts all read words into the list
    for line in file:
        list.append(line.rstrip("\n"))

    # returns the list
    return list


def display_files(file, display):
    # set accumulator
    count = 0

    print("Here is the", display, "set of words.")
    for item in file:
        print(item, end=" ")

        # create new line after five words have been printed
        count += 1
        if count == 5:
            print()
            count = 0

    print('\n')
    input("Press any key to continue.")
    print()


def results(data, finish):
    # set accumulator
    count = 0

    for item in data:
        print(item, end=' ')

        # create new line after five words have been printed
        count += 1
        if count == 5:
            print()
            count = 0

    if finish < 3:
        print('\n')
        input("Press any key to continue.")
        print()
        finish += 1
        return finish
    else:
        print('\n')
        print("That is all the data, program had ended.")


# main function
main()
