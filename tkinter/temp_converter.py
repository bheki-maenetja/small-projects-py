import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
window.title("Temperature Converter")

def convert_temp():
    try:
        celsius = float(ent_temperature.get())
        fahrenheit = 9/5 * celsius + 32
        lbl_result["text"] = f"{fahrenheit}\N{DEGREE FAHRENHEIT}"
    except:
        return

entry_frame = tk.Frame(master=window)
ent_temperature = tk.Entry(master=entry_frame, borderwidth=3, relief=tk.SUNKEN)
lbl_symbol = tk.Label(master=entry_frame, text="\N{DEGREE CELSIUS}")

ent_temperature.grid(row=0, column=0, sticky="w")
lbl_symbol.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}", fg="navy", command=convert_temp)
lbl_result = tk.Label(text="\N{DEGREE FAHRENHEIT}", fg="black")

entry_frame.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()