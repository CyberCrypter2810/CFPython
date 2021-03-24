# Name_search.py

'''
Program goes through two text files of popular names and tells 
users if the name they inputted is one of the popular from the
time period.
'''

# main function
def main():
    # Calls list_names function for making lists for names in
    # text files
    Boy_names = list_names("BoyNames.txt")
    Girl_names = list_names("GirlNames.txt")
    
    boy, girl, male, female = name_input()
    
    # search and displays results
    if male == True and female == True:
        # searchs for boy and girl names
        if boy in Boy_names:
            print("This male name is the most popular name in the US " +
                  "from year 2000 through 2009.")
        else:
            print("Male name provided is not a popular name in the US " +
                  "from year 2000 through 2009.")
            
        if girl in Girl_names:
            print("This female name is the most popular name in the US " +
                  "from year 2000 through 2009.")
        else:
            print("Female name provided is not a popular name in the US " +
                  "from year 2000 through 2009.")
        
    elif male == True and female == False:
        if boy in Boy_names:
            print("This male name is popular in the US from year " +
                  "2000 through 2009.")
        else:
            print("This male name is not popular in the US from year " +
                  "2000 through 2009.")
    
    else:
        if girl in Girl_names:
            print("This female name is the most popular name in the US " +
                  "from year 2000 through 2009.")
        else:
            print("This female name is not a popular name in the US " +
                  "from year 2000 through 2009.")
    


# list_names function
def list_names(Name_file):
    # create list
    names = []
    
    # open and read provided file
    file = open(Name_file, 'r')
    name = file.readline()
    
    # takes all names and puts them into list
    while name != '':
        name = name.rstrip('\n')
        names.append(name)
        # read next line
        name = file.readline()
        
    # close the file
    file.close()
    
    # returns list
    return names
        


# name_input function
def name_input():
    # Determine if user wants to search either one gender name
    # or both
    print("1: Male")
    print("2: Female")
    print("3: Both")
    select = int(input("Which gender name are you looking for: "))
    
    # error loop if select is above options field
    while select < 0 or select > 3:
        print("Error, no option exist, please try again.")
        select = int(input("Which gender name are you looking for: "))
    
    # determines the select options and returns said name
    if select == 1:
        boy_name = input("Please enter a male name: ")
        girl_name = ''
        # setting display determinations
        boy = True
        girl = False
    elif select == 2:
        girl_name = input("Please enter a female name: ")
        boy_name = ''
        # setting display determinations
        girl = True
        boy = False
    else:
        boy_name = input("Please enter a male name: ")
        girl_name = input("Please enter a female name: ")
        # setting display determinations
        boy = True
        girl = True
       
    # return boy and girl name
    return boy_name.capitalize(), girl_name.capitalize(), boy, girl


# calling main
main()