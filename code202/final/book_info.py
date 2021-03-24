# Book_info.py

'''
Program creates three classes for storing various
book data from books.py
'''

class Person:
    # initiate
    def __init__(self, first, last):
        self.__first = first
        self.__last = last
        
    # accessor
    def get_first(self):
        return self.__first
    
    def get_last(self):
        return self.__last
    
class Book(Person):
    # initiate
    def __init__(self, title, stock, price, first, last):
        # initiate Person
        Person.__init__(self, first, last)
        # set values
        self.__title = title
        self.__stock = stock
        self.price = price
    
    # accessors
    def get_title(self):
        return self.__title
    def get_stock(self):
        return self.__stock
    def get_price(self):
        return self.price


class BookAuthor(Book):
    # initiate
    def __init__(self, first, last, title, stock, price, collect, series):
        # initiate Book
        Book.__init__(self, title, stock, price, first, last)
        # set values
        self.__collect = collect
        self.__series = series
    # accessors
    def get_collect(self):
        return self.__collect
    def get_series(self):
        return self.__series
    
    # display
    def __str__(self):
        return "Title: " + Book.get_title(self) +\
            "\nCollectable: " + str(self.__collect) +\
                "\nBook Series: " + str(self.__series) +\
                    "\nAuthor: " + Person.get_first(self) +\
                        Person.get_last(self) +\
                            "\nPrice: " + Book.get_price(self) +\
                                "\nStock: " + Book.get_stock(self)