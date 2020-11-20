import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
window.resizable(False, False)

top_frame = tk.Frame(height=100, width=100)
top_frame.pack(fill=tk.X, expand=1)

heading_font = tkFont.Font(family="Courier", size=50)
heading = tk.Label(master=top_frame, text="Number Pad", font=heading_font,fg="cyan", bg="navy", borderwidth=5, relief=tk.RAISED)
heading.pack(fill=tk.X)

label_font = tkFont.Font(family="Roboto", size=20)
label_text = tk.Label(master=top_frame, text="", font=label_font, fg="yellow", borderwidth=2, relief=tk.GROOVE, bg="green", justify=tk.LEFT)
label_text.pack(fill=tk.X)

number_font = tkFont.Font(family="Verdana", size=30)

def add_digit(new_string):
    current_text = label_text["text"]
    if current_text == "" or (current_text[0] != "0" and new_string != "0"):
        label_text["text"] += new_string
    print(new_string)

def create_button(digit, button_func):
    new_button = tk.Button(master=body_frame, text=f"{digit}", height=1, width=5, fg="navy", bg="cyan", font=number_font,command=button_func)
    return new_button

symbols = [".", 0, "<-"]

body_frame = tk.Frame(height=100, width=100,bg="purple", borderwidth=5, relief=tk.GROOVE)
for i in range(3):
    body_frame.rowconfigure(i, weight=1, minsize=10)
    body_frame.columnconfigure(i, weight=1, minsize=10)
    for j in range(4):
        if j == 3:
            symbol_button = create_button(symbols[i], None)
            symbol_button.grid(row=j, column=i, padx=5, pady=5, sticky="nesw")
        else:
            new_button = create_button((i + 1) + j * 3, lambda : add_digit(f"{(i + 1) + j * 3}"))
            new_button.grid(row=j, column=i, padx=5, pady=5, sticky="nesw")

body_frame.pack(fill=tk.BOTH, expand=1)
window.mainloop()