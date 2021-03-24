# Books.py

'''
Programs takes data about said book
and stores them into a class and prints
them back out.
'''

import book_info

# main function
def main():
    # get data
    first = input("Authors first name: ")
    last = input("Authors last name: ")
    title = input("Title of Book: ")
    stock = input("Stock of said book: ")
    price = float(input("Price per book: $"))
    collect = input("Collectable series: (YES or NO): ")
    
    if collect == "YES":
        series = input("Which series: ")
    else:
        series = 'None'
    
    info = book_info.BookAuthor(first, last, title, stock, price, collect, series)
    
    # display results
    print()
    print(str(info))
    print()


# calling main
main()