from tkinter import*
from tkinter import ttk


def resize(ev=None):
    label.configure(font = "Aria -%d bold" % scale.get())



window = Tk()
window.geometry("500x500")

label = ttk.Label(window, text="mamood raoof",
                  font = "Aria -12 bold")
label.pack(fill="y", expand=1)

scale = ttk.Scale(window, from_ = 10, to = 40)
scale.set(30)
scale.pack(fill="x", expand=1)

quits = ttk.Button(window, text = 'Quit', command = window.quit )
quits.pack()

window.mainloop()
