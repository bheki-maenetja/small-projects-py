import tkinter as tk

window = tk.Tk()

def make_square(x,y,colour="white"):
    new_frame = tk.Frame(master=window, relief=tk.RAISED, height=100, width=100, borderwidth=5, bg=colour)
    new_frame.grid(row=x, column=y, padx=5, pady=5)
    # label = tk.Label(master=new_frame, text=colour, fg="black", bg=colour)
    # label.place(x=20, y=30)

def make_board():
    for i in range(8):
        window.columnconfigure(i, weight=1, minsize=25)
        window.rowconfigure(i, weight=1, minsize=25)
        for j in range(8):
            if (i + j) % 2 == 0:
                make_square(i,j, colour="navy")
            else:
                make_square(i,j, colour="cyan")

make_board()
window.mainloop()