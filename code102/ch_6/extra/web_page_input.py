# web_page_input.py

'''
Program does a simple web page layout of what the
user inputs.
'''

# main function
def main():
    # calling user function
    name, describe = user()
    # calling html function
    html(name, describe)


# input function
def user():
    # get input from user
    name = input("Enter your name: ")
    describe = input("Describe yourself: ")

    # returning values
    return name, describe


# html function
def html(name, describe):
    # open html file
    page = open('webpage.html', 'w')
    # writing the displayment of the file
    page.write('<html> \n')
    page.write('<head> \n')
    page.write('</head> \n')
    page.write('<body> \n')
    page.write('<center> \n')
    # inputs name in center of page
    page.write('<h1>' + name + '</h1> \n')
    page.write('</center> \n')
    page.write('<hr /> \n')
    # inputs descrition
    page.write(describe)
    page.write('<hr /> \n')
    page.write('</body> \n')
    page.write('</html> \n')

    # closes the file
    page.close()


# calling main
main()
