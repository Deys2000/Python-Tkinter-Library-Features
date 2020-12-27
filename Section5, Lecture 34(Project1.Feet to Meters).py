from tkinter import*
from tkinter import ttk


def calculate(*args):
    try:
        value=float(feet.get())
        meters.set((0.3048 * value * 10000.0 +0.5)/10000.0)
    except ValueError:
        pass
    
win = Tk()
win.title("Feet to Meters")

window = ttk.Frame(win)
window.grid(column=0,row=0)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(window, width=7, textvariable = feet)
feet_entry.grid(column=2, row=1)

ttk.Label(window, textvariable=meters).grid(column=2, row=2)
ttk.Button(window, text = "Calculate", command=calculate).grid(column=3, row=3)

ttk.Label(window, text="feet").grid(column=3, row=1)
ttk.Label(window, text="is equivalent to").grid(column=1, row=2)
ttk.Label(window, text="meters").grid(column=3, row=2)
for child in window.winfo_children(): child.grid_configure(padx=4, pady=5)

window.mainloop()
