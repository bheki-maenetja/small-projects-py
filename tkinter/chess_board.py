import tkinter as tk
from random import choice

window = tk.Tk()
window.aspect(1,1,1,1)
window.minsize(300, 300)
dark_colours = ["black", "brown", "purple","navy","red"]
bright_colours = ["white", "pink", "lime", "cyan", "yellow"]

def make_square(x,y,colour="white", square_size=100):
    new_frame = tk.Frame(master=window, relief=tk.RAISED, height=square_size, width=square_size, borderwidth=2, bg=colour)
    new_frame.grid(row=x, column=y, sticky="nesw")
    # label = tk.Label(master=new_frame, text=colour, fg="black", bg=colour)
    # label.place(x=20, y=30)

def make_board(colour_1, colour_2, square_size=100):
    for i in range(8):
        window.columnconfigure(i, weight=1, minsize=25)
        window.rowconfigure(i, weight=1, minsize=25)
        for j in range(8):
            if (i + j) % 2 == 0:
                make_square(i,j, colour=colour_1, square_size=square_size)
            else:
                make_square(i,j, colour=colour_2, square_size=square_size)


make_board("navy", "cyan")
window.bind("<Return>", lambda e: make_board(choice(dark_colours), choice(bright_colours), 50))
window.mainloop()