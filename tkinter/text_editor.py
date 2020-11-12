import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(master=window)
fr_buttons = tk.Frame(master=window)
btn_open = tk.Button(master=fr_buttons, text="Open")
btn_save = tk.Button(master=fr_buttons, text="Save As")

window.mainloop()