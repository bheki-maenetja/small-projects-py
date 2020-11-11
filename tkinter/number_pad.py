import tkinter as tk

window = tk.Tk()

top_frame = tk.Frame(height=100, bg="navy", borderwidth=5, relief=tk.RAISED)
heading = tk.Label(master=top_frame, text="Number Pad", fg="cyan", bg="navy")
heading.pack()
top_frame.pack()

def print_num(num):
    print(num)

def create_button(digit):
    new_button = tk.Button(master=body_frame, text=f"{digit}", height=5, width=10, fg="navy", bg="blue", command=lambda : print(digit))
    return new_button


body_frame = tk.Frame(height=100, bg="darkgreen", borderwidth=5, relief=tk.GROOVE)
for i in range(3):
    for j in range(3):
        # num_func 
        new_button = create_button((i + 1) + j * 3)
        new_button.grid(row=j, column=i, padx=2, pady=2)
        num_func = None

body_frame.pack(fill=tk.Y)
window.mainloop()