from tkinter import*
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text = "One")
notebook.add(frame2, text = "Two")

ttk.Button(frame1, text="Clickme").pack()

frame3 = ttk.Frame(notebook)
notebook.add(frame3, text = "Three")

notebook.tab(frame3, state="normal")


window.mainloop()
