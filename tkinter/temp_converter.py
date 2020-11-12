import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
window.title("Temperature Converter")

entry_frame = tk.Frame(master=window)
ent_temperature = tk.Entry(master=entry_frame, borderwidth=3, relief=tk.SUNKEN)
lbl_symbol = tk.Label(master=entry_frame, text="°C")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_symbol.grid(row=0, column=1, sticky="e")

btn_convert = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}", fg="navy")
lbl_result = tk.Label(text="100", fg="black")

entry_frame.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()