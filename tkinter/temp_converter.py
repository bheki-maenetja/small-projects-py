import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
window.title("Temperature Converter")

ent_temperature = tk.Entry(
    borderwidth=2,
    relief=tk.SUNKEN
)

lbl_result = tk.Label(
    text="100",
    fg="black"
)

lbl_symbol = tk.Label(
    text="°C"
)

btn_convert = tk.Button(
    text="Convert",
    height=1,
    width=10,
    fg="navy"
)

ent_temperature.pack(fill=tk.X, expand=1, side=tk.LEFT)
lbl_symbol.pack(fill=tk.X, side=tk.LEFT)
lbl_result.pack(fill=tk.X, side=tk.RIGHT)
btn_convert.pack(fill=tk.X, side=tk.RIGHT)

window.mainloop()