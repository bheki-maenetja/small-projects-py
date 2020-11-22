from tkinter import *
from tkinter import ttk
import re

window = Tk()
window.minsize(300, 300)
window.maxsize(700, 700)
window.aspect(1,1,1,1)
window.rowconfigure(0, weight=1, minsize=100)
window.columnconfigure(0, weight=1, minsize=1)

frame_style = ttk.Style()
frame_style.configure('Danger.TFrame', background='red', relief="raised", borderwidth=10, foreground='yellow')

my_frame = ttk.Frame(style="Danger.TFrame")
my_frame.grid(row=0, column=0, sticky="nesw", padx=10, pady=10)
my_frame.columnconfigure(0, weight=1, minsize=100)
my_frame.rowconfigure(0, weight=1, minsize=10)
my_frame.rowconfigure(1, weight=1, minsize=10)
my_frame.rowconfigure(2, weight=1, minsize=5)

my_label = ttk.Label(my_frame, text="This is some text", anchor="center")
my_label.grid(row=0, column=0, sticky="s", padx=10, pady=10)

my_check = ttk.Checkbutton(my_frame, text="Do you want cake?", onvalue=1, offvalue=0)
my_check.grid(row=1, column=0, sticky="n", padx=10, pady=10)

def call_back(*args):
    print(my_entry.get())

def validate_entry(val):
    return re.match('^[0-9]*$', val) is not None and len(val) < 5

validate_command = (my_frame.register(validate_entry), '%P')

string_var = StringVar()
my_entry = ttk.Entry(my_frame, textvariable=string_var, validate='key', validatecommand=validate_command)

string_var.trace_add("write", call_back)
my_entry.grid(row=2, column=0, sticky='new', padx=10, pady=10)

window.mainloop()