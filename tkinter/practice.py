import tkinter as tk

my_text = "This is just some text"

# Widgets -- Labels, Buttons, Entries & Texts
window = tk.Tk()
"""
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
    width=50,
    relief=tk.RAISED
)
user_text.pack()

text_box = tk.Text()
text_box.pack()
"""
# """
# Widgets -- Frames
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in frame A", relief=tk.SUNKEN)
label_b = tk.Label(master=frame_b, text="I'm in frame B")

label_a.pack()
label_b.pack()

frame_b.pack()
frame_a.pack()
# """
window.mainloop()