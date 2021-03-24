# house.py

'''
Program will create a GUI Canvas
widget to draw a house.
'''

import tkinter as tk

class House:
    def __init__(self):
        # main window
        self.main_window = tk.Tk()
        
        # main window title
        self.main_window.title("House")
        
        # house widget
        self.house = tk.Canvas(self.main_window,
                                width = 500,
                                height = 500)
        
        # creating picture of house
        # front main
        self.house.create_rectangle(50, 200, 450, 450)
        # roof
        self.house.create_line(50, 200, 250, 40, 450, 200)
        # door
        self.house.create_rectangle(200, 300, 300, 450, fill = 'brown')
        # windows
        self.house.create_rectangle(80, 300, 170, 380, fill = 'cyan')
        self.house.create_rectangle(330, 300, 420, 380, fill = 'cyan')
        self.house.create_oval(190, 80, 307, 190, fill = 'cyan')
        
        # pack house
        self.house.pack()
        
        # tk main loop
        tk.mainloop()
        
# instance of House class
house = House()