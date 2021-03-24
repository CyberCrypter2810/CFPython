# Solar.py

'''
Program create GUI Canvas of
the order of the planets of the
solar system. The Sun will be in the
left corner followed by the planets
in the correct order from their distance
from the sun.
'''

import tkinter as tk

class Solar:
    def __init__(self):
        # main window
        self.main_window = tk.Tk()
        
        # main window title
        self.main_window.title("Solar System")
        
        # solar system canvas
        self.solar = tk.Canvas(self.main_window,
                               width = 1100,
                               height = 500)
        
        # sun
        self.solar.create_oval(10, 10, 200, 200, fill = 'yellow')
        # mercury
        self.solar.create_oval(200, 200, 230, 230, fill = 'grey')
        # venus
        self.solar.create_oval(250, 250, 300, 300, fill = 'red')
        # earth
        self.solar.create_oval(320, 320, 390, 390, fill = 'aqua')
        # mars
        self.solar.create_oval(410, 410, 450, 450, fill = 'darkorange3')
        # Jupiter
        self.solar.create_oval(480, 270, 630, 420, fill = 'tan')
        # Saturn
        self.solar.create_oval(640, 145, 745, 250, fill = 'goldenrod1')
        # Uranus
        self.solar.create_oval(765, 85, 855, 175, fill = 'deepskyblue2')
        # Neptune
        self.solar.create_oval(875, 195, 960, 280, fill = 'dodgerblue3')
        # pluto
        self.solar.create_oval(1000, 350, 1020, 370, fill = 'khaki1')
        
        # Labeling each planet
        self.solar.create_text(105, 210, text = "Sun")
        self.solar.create_text(215, 240, text = "Mercury")
        self.solar.create_text(275, 310, text = "Venus")
        self.solar.create_text(353, 400, text = "Earth")
        self.solar.create_text(430, 460, text = "Mars")
        self.solar.create_text(555, 430, text = "Jupiter")
        self.solar.create_text(692, 260, text = "Saturn")
        self.solar.create_text(810, 185, text = "Uranus")
        self.solar.create_text(918, 290, text = "Neptune")
        self.solar.create_text(1010, 380, text = "Pluto")
        
        # pack
        self.solar.pack()
        
        # tk main loop
        tk.mainloop()
        

# instance of Solar class
solar = Solar()