# Frequent_character.py

'''
Program lets user to input a string statement and then
calculates and displays the character that has been used
the most.
'''

# main function
def main():
    # Ask user to input a sentence
    print("Please write a sentence.")
    string = input()
    
    # calling cal function
    char = cal(string)
    
    print()
    
    # displays the most used character
    print("This most frequently used character in this string is " +
          "the letter:", char)
    

# cal function
def cal(string):
    
    # goes through the string and determine
    # which character is mentioned the most
    freq = {} 
    for item in string: 
        if item in freq: 
            freq[item] += 1
        else:
            freq[item] = 1
    character = max(freq, key = freq.get)
    
    # returns character
    return character
        
           
# calling main
main()