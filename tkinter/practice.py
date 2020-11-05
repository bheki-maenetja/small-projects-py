import tkinter as tk

my_text = "This is just some text"

# Widgets -- Labels, Buttons, Entries & Texts
window = tk.Tk()
# window_2 = tk.Tk()
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
"""
# Widgets -- Frames
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in frame A", relief=tk.SUNKEN)
label_b = tk.Label(master=frame_b, text="I'm in frame B")

label_a.pack()
label_b.pack()

frame_b.pack()
frame_a.pack()
"""
# my_text_entry = tk.Entry(text="What is your name", width=40)
# my_text_entry.pack()
# my_text_entry.insert(0, "What is your name?")

# Geometry Managers
frame_1 = tk.Frame(width=500, height=25, bg="green")
frame_1.pack(fill=tk.X)

frame_2 = tk.Frame(height=50, bg="cyan")
frame_2.pack(fill=tk.X)

frame_3 = tk.Frame(height=75, bg="yellow")
frame_3.pack(fill=tk.X)

frame_4 = tk.Frame(height=100, bg="orange")
frame_4.pack(fill=tk.X)

window.mainloop()
# window_2.mainloop()