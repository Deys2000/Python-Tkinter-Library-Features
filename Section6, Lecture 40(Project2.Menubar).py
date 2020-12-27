import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

window = tk.Tk()
def _quit():
    window.quit()
    window.destroy()
    exit()
menuBar = Menu(window)
window.config(menu=menuBar)
filemenu = Menu(menuBar)
menuBar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="New")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=_quit)

helpMenu = Menu(menuBar)
menuBar.add_cascade(label="Help", menu=helpMenu)

helpMenu.add_command(label="About")

def clickme():
    button.configure(text="Hello " +name.get())
    button.grid(column=1, row=1)
def clickme():
    button.configure(text="Hello "+ name.get()+" "+numberChoose.get())

ttk.Label(text="choose a number:").grid(column=2, row=0)
number = tk.StringVar()
numberChoose = ttk.Combobox(width=12, textvariable=number)
numberChoose['values']=(1,2,4,50,100)
numberChoose.grid(column=1, row=1)
numberChoose.current(0)

ttk.Label(text="Enter a name:").grid(column=0, row=0)

name= tk.StringVar()
nameEntered = ttk.Entry(width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

button = ttk.Button(text="ClickMe", command=clickme)
button.grid(column=2, row=1)

chDisabled = tk.IntVar()
check1 = tk.Checkbutton(text="Disabled", variable=chDisabled, state="disabled")
check1.select()
check1.grid(column=0, row=4)

chChecked = tk.IntVar()
check2 = tk.Checkbutton(text="UnChecked", variable=chChecked)
check2.deselect()
check2.grid(column=1, row=4)

chEnabled = tk.IntVar()
check3 = tk.Checkbutton(text="Enabled", variable=chEnabled)
check3.select()
check3.grid(column=2, row=4)

scrollW = 30
scrollH = 3
scr = scrolledtext.ScrolledText(window, width=scrollW, height=scrollH)
scr.grid(column=0, columnspan=3)

window = ttk.LabelFrame(window, text="Labels in a Frame")
window.grid(column=0, row=7, padx=20, pady=40)

ttk.Label(window, text="Label in a Frame").grid(column=0,row=0)
ttk.Label(window, text="Label 2").grid(column=0,row=1)
ttk.Label(window, text="Label 3").grid(column=0,row=2)

for child in window.winfo_children():
    child.grid_configure(padx=20, pady=5)



window.mainloop()
