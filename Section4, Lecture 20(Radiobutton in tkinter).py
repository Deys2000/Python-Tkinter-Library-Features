import tkinter as tk
from tkinter import ttk

window = tk.Tk()

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def resCal():
    redSal = redVar.get()
    if redSal == 1: window.configure(background=COLOR1)
    elif redSal == 2: window.configure(background=COLOR2)
    elif redSal == 3: window.configure(background=COLOR3)


redVar = tk.IntVar()

rad1 = tk.Radiobutton(window, text="Rad1", variable=redVar, value=1, command=resCal)
rad1.grid(row=0,column=0)

rad2 = tk.Radiobutton(window, text="Rad2", variable=redVar, value=2, command=resCal)
rad2.grid(row=0,column=1)

rad3 = tk.Radiobutton(window, text="Rad3", variable=redVar, value=3, command=resCal)
rad3.grid(row=0,column=2)

window.mainloop()
