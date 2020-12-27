from tkinter import*
from tkinter import ttk

window = Tk()

def callback(number):
    print(number)


ttk.Button(window, text="Clickme", command=lambda:callback(1)).pack()
ttk.Button(window, text="Clickme", command=lambda:callback(2)).pack()
ttk.Button(window, text="Clickme", command=lambda:callback(3)).pack()
ttk.Button(window, text="Clickme", command=lambda:callback(4)).pack()
ttk.Button(window, text="Clickme", command=lambda:callback(5)).pack()
    


window.mainloop()
