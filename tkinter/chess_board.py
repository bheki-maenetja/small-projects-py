import tkinter as tk

window = tk.Tk()

def make_square(x,y,colour="white"):
    new_frame = tk.Frame(master=window, width=100, height=100, bg=colour)
    new_frame.grid(row=x, column=y)
    # label = tk.Label(master=new_frame, text=colour, fg="black", bg=colour)
    # label.place(x=20, y=30)

def make_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                make_square(i,j, colour="cyan")
            else:
                make_square(i,j, colour="navy")

make_board()
window.mainloop()