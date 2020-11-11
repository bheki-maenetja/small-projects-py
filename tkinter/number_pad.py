import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
window.resizable(False, False)

top_frame = tk.Frame(height=100, width=100, borderwidth=5, relief=tk.RAISED)
top_frame.pack(fill=tk.X, expand=1)

heading_font = tkFont.Font(family="Courier", size=50)
heading = tk.Label(master=top_frame, text="Number Pad", font=heading_font,fg="cyan", bg="navy")
heading.pack(fill=tk.X)

label_font = tkFont.Font(family="Times", size=20)
label_text = tk.Label(master=top_frame, text="123", font=label_font, fg="lime", bg="green")
label_text.pack(fill=tk.X, side=tk.LEFT)

def create_button(digit):
    new_button = tk.Button(master=body_frame, text=f"{digit}", height=3, width=15, fg="navy", bg="blue", command=lambda : print(digit))
    return new_button

body_frame = tk.Frame(height=100, width=100,bg="darkgreen", borderwidth=5, relief=tk.GROOVE)
for i in range(3):
    body_frame.rowconfigure(i, weight=1, minsize=10)
    body_frame.columnconfigure(i, weight=1, minsize=10)
    for j in range(3):
        new_button = create_button((i + 1) + j * 3)
        new_button.grid(row=j, column=i, padx=5, pady=5)
        num_func = None

body_frame.pack(fill=tk.BOTH, expand=1)
window.mainloop()