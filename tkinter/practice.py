import tkinter as tk

my_text = "This is just some text"

window = tk.Tk()

greeting = tk.Label(text=f"Here is some text: {my_text}", fg="white", background="black")
greeting.pack()

button = tk.Button(
    text="Don't Click Me/Click Me",
    width=20,
    height=5,
    fg="red",
    background="blue",
)
button.pack()

user_text = tk.Entry(
    fg="yellow",
    bg="blue",
    width=50
)
user_text.pack()

window.mainloop()