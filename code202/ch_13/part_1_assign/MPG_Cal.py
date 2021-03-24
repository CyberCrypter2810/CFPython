# MPG_Cal.py

'''
This program makes a GUI for user to
calculate how much miles they can travel
per gallon (MPG) of gas. The GUI will ask
for distance(miles) and fuel(gallons) from
the user to make the calculation.
'''

import tkinter

# create GUI Class
class MPG_CAL:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()
        
        # create title of window
        self.main_window.title("MPG Calculator")
        
        # Create four frames
        self.distance_frame = tkinter.Frame(self.main_window)
        self.gallons_frame = tkinter.Frame(self.main_window)
        self.result_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        
        # distance frame widgets
        self.distance_label = tkinter.Label(self.distance_frame,
                                          text = 'Distance on full tank (miles): ')
        self.distance_entry = tkinter.Entry(self.distance_frame,
                                            width = 10)
        # pack
        self.distance_label.pack(side = 'left')
        self.distance_entry.pack(side = 'left')
        
        # gallon frame widgets
        self.gallon_label = tkinter.Label(self.gallons_frame,
                                          text = 'Size of tank (Gallons): ')
        self.gallon_entry = tkinter.Entry(self.gallons_frame,
                                          width = 16)
        # pack
        self.gallon_label.pack(side = 'left')
        self.gallon_entry.pack(side = 'left')
        
        # result frame widgets
        self.result_cal = tkinter.StringVar()
        self.result_label1 = tkinter.Label(self.result_frame,
                                          textvariable = self.result_cal)
        self.result_label2 = tkinter.Label(self.result_frame,
                                           text = 'Miles Per Gallon (MPG)')
        # pack
        self.result_label1.pack(side = 'left')
        self.result_label2.pack(side = 'left')
        
        # button frame widgets
        self.cal_button = tkinter.Button(self.button_frame,
                                         text = 'Calculate',
                                         command = self.calculate)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        # pack
        self.cal_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        
        # pack frames
        self.distance_frame.pack()
        self.gallons_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()
        
        # starting main loop
        tkinter.mainloop()
        
    def calculate(self):
        # get variables for distance and gallons
        self.distance = float(self.distance_entry.get())
        self.gallons = float(self.gallon_entry.get())
        
        # calculate mpg
        self.mpg = self.distance / self.gallons
        
        # update result_cal variable
        self.result_cal.set(self.mpg)

mpg_cal = MPG_CAL()