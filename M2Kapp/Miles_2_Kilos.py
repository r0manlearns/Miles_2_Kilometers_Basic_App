import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import ttkbootstrap as ttk


#window
window = ttk.Window(themename = 'darkly')
window.title("Miles 2 Kilometers")
window.geometry('500x250')

#conver button function
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#font object
title_font = tkFont.Font(family='Times', 
                         size=32, 
                         weight='bold')
output_font = tkFont.Font(family='Times', 
                          size=18, 
                          weight='bold')

#title (1st widget)
title_label = ttk.Label(master = window, 
                        text = 'Miles to Kilometers', 
                        font =title_font)
title_label.pack()

#input field
input_frame = tk.Frame(master = window)
entry_int = tk.IntVar(master = window)
entry = ttk.Entry(master = input_frame, 
                  textvariable = entry_int)
button = ttk.Button(master = input_frame, 
                    text = 'Convert', 
                    command = convert)
entry.pack(side = 'left', 
           padx = 5)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, 
                         text = 'Output', 
                         font = output_font, 
                         textvariable=output_string)
output_label.pack(pady = 10)

#run
window.mainloop()

print('gg')
