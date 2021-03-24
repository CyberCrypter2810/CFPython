# Word_separator.py

'''
Program takes an inputted sentence and 
separates the words if some words are fused
together. It also puts makes the letter lower case if
it's not at the beginning of the sentence.
'''

# main function
def main():
    # calls the retrieval function
    user_input = retrieval()
    
    # calls the edit function
    formated = edit(user_input)
    
    # displays final results
    print("Corrected separated version is: ")
    print()
    print(formated)
    

# retrieval function
def retrieval():
    # asks user to input a sentence
    print("Enter a sentence with no spaces.")
    print("Please Capitalize each new word.")
    sentence = input()
    print()
    
    # puts sentence into a list
    sentence_list = list(sentence)
    
    # returns sentence_list
    return sentence_list


# edit function
def edit(user_input):
    # setup of accumulator and sentence
    sentence = ''
    count = 1
    
    # examines each letter to determine it's placement
    for letter in user_input:
        if count == 1:
            if letter.islower():
                sentence += letter.isupper()
            else:
                sentence += letter
        elif letter.isupper():
            sentence += ' ' + letter.lower()
        else:
            sentence += letter
        count += 1
    
    # returns sentence
    return sentence


# calling main
main()