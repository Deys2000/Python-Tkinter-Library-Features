import tkinter as tk
from tkinter import ttk

window = tk
alabel = ttk.Label(text="A Label")
alabel.grid(row=0, column=0)


def clickme():
    button.configure(text="** I have been Clicked")
    alabel.configure(foreground='red')

button = ttk.Button(text="Click Me", command=clickme)
button.grid(column = 1, row = 1)
window.mainloop()
