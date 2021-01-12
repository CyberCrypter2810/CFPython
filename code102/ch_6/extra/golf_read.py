# golf_read.py

'''
Program opens the file golf.txt and
displays its contents on the screen.
'''

# main function
def main():
    try:
        # open golf.txt
        golf = open('golf.txt', 'r')

        for line in golf:
            line = line.rstrip('\n')
            print(line)


    except Exception as error:
        print("ERROR: file does not exist.")

    finally:
        golf.close()


# calling main
main()
