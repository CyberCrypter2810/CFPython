# tree_age.py

'''
Program makes 5 GUI Canvas circles
to represent how old a tree is.
'''

import tkinter as tk

class Tree_Age:
    def __init__(self):
        # main window
        self.main_window = tk.Tk()
        
        # main window title
        self.main_window.title("Tree Age")
        
        # Canvas widget
        self.tree = tk.Canvas(self.main_window,
                              width = 350,
                              height = 300)
        
        # circles to represent tree age
        self.tree.create_oval(65, 45, 280, 255, fill = 'orange')
        self.tree.create_oval(85, 65, 260, 235, fill = 'yellow')
        self.tree.create_oval(105, 85, 240, 215, fill = 'cyan')
        self.tree.create_oval(125, 105, 220, 195, fill = 'green')
        self.tree.create_oval(145, 125, 200, 175, fill = 'red')
        
        # text for indecating year
        self.tree.create_text(173, 150, text = "1st year")
        self.tree.create_text(173, 182, text = "2nd year")
        self.tree.create_text(173, 203, text = "3rd year")
        self.tree.create_text(173, 223, text = "4th year")
        self.tree.create_text(173, 245, text = "5th year")
        
        # pack tree
        self.tree.pack()
        
        # tk main loop
        tk.mainloop()

# instance of Tree_Age class
tree_age = Tree_Age()