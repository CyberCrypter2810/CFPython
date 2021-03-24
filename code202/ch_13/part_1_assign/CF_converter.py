# CF_converter.py

'''
Program creates a GUI program to
convert the temperature from Celsius
to Fahrenheit.
'''

import tkinter as tk

class Celcius_Converter:
    def __init__(self):
        # Create main window
        self.main_window = tk.Tk()
        
        # create title
        self.main_window.title('Celsius to Fahrenheit Converter')
        
        # create three frames
        self.top_frame = tk.Frame()
        self.middle_frame = tk.Frame()
        self.bottom_frame = tk.Frame()
        
        # widgets for top frame
        self.top_label = tk.Label(self.top_frame,
                                  text = 'Celsius:')
        self.celsius_entry = tk.Entry(self.top_frame,
                                  width = 10)
        # pack top
        self.top_label.pack(side = 'left')
        self.celsius_entry.pack(side = 'left')
        
        # widgets for middle frame
        self.converted = tk.StringVar()
        self.display_converted = tk.Label(self.middle_frame,
                                          textvariable = self.converted)
        self.fahren_label = tk.Label(self.middle_frame,
                                     text = "Fahrenheit:")
        # pack middle
        self.fahren_label.pack(side = 'left')
        self.display_converted.pack(side = 'left')
        
        # widgets for bottom frame
        self.convert_button = tk.Button(self.bottom_frame,
                                        text = 'Convert',
                                        command = self.convert)
        self.quit_button = tk.Button(self.bottom_frame,
                                     text = 'Quit',
                                     command = self.main_window.destroy)
        # pack bottom
        self.convert_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        
        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        
        # tk main loop
        tk.mainloop()
        
    # method for convert button
    def convert(self):
        celsius = float(self.celsius_entry.get())
        
        fahren = (9 / 5) * celsius + 32
        
        # update stringvar with fahren results
        self.converted.set(fahren)

# instance of Celcius Converter class
celcius_converter = Celcius_Converter()