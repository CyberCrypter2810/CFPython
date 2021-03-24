# Pig_Latin_translator.py

'''
Program ask user to enter a statement and then translate the
statement into Pig Latin.
'''

# main function
def main():
    # asks user to input a statement
    print("Enter a statement to be translated.")
    statement = input()
    
    # calls translate for user input
    translated = translate(statement)
    
    print()
    print("Here is the translation.")
    print()
    
    # displays the translation into a string
    for words in translated:
        print(words, end=' ')


# translate function
def translate(statement):
    # takes statement and puts its string into a list
    statement_list = statement.split()
    
    # create a translated list
    translated = []
    
    # separate each word in the statment list
    for index in statement_list:
        # create an edit list
        list = []
        
        # separate each letter in the index
        for letter in index:
            list.append(letter)
        
        # Moving the first letter to last to provide translation
        move = list[0]        
        del list[0]        
        list.append(move)        
        list.append('ay')
        
        # Forms the letters into a word
        word = ''
        for letter in list:
            word += letter
        
        # adds word to the translated list
        translated.append(word)
    
    # returns translated
    return translated


# calling main
main()