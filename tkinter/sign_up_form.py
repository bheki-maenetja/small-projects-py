from tkinter import *
from tkinter import ttk

window = Tk()
window.rowconfigure(0, weight=1, minsize=50)
window.columnconfigure(0, weight=1, minsize=50)

frame_style = ttk.Style()
frame_style.configure('Danger.TFrame', background='red', relief="raised", borderwidth=10, foreground='yellow')

my_frame = ttk.Frame(style="Danger.TFrame")
my_frame.grid(row=0, column=0, sticky="nesw", padx=10, pady=10)
my_frame.rowconfigure(0, weight=1, minsize=20)
my_frame.columnconfigure(0, weight=1, minsize=20)

my_label = ttk.Label(my_frame, text="This is some text", anchor="center")
my_label.grid(row=0, column=0, sticky="we", padx=10, pady=10)

window.mainloop()