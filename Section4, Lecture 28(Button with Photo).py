from tkinter import*
from tkinter import ttk

window = Tk()

button = ttk.Button(window, text = "Clickme")
button.pack()

def Callback():
    print("Clicked")

button.config(command=Callback)

window.mainloop()
