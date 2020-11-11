import tkinter as tk

window = tk.Tk()

top_frame = tk.Frame(height=100, bg="navy", borderwidth=5, relief=tk.RAISED)
heading = tk.Label(master=top_frame, text="Number Pad", fg="cyan", bg="navy")
heading.pack()
top_frame.pack()

body_frame = tk.Frame(height=100, bg="darkgreen", borderwidth=5, relief=tk.GROOVE)
for i in range(3):
    for j in range(3):
        new_button = tk.Button(master=body_frame, text=f"{(i + 1) + j * 3}", height=5, width=10, fg="navy", bg="blue")
        new_button.grid(row=j, column=i, padx=2, pady=2)

body_frame.pack(fill=tk.Y)
window.mainloop()