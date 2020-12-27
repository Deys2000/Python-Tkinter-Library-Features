from tkinter import*
from tkinter import ttk

window = Tk()

panedwindow = ttk.PanedWindow(window, orient=HORIZONTAL)
panedwindow.pack( expand= TRUE)

frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
panedwindow.add(frame1, weight=1)
panedwindow.add(frame2, weight=4)

frame3 = ttk.Frame(window, width = 50, height =50, relief = SUNKEN)

frame3 = ttk.Frame(panedwindow, width = 50, height =50, relief = SUNKEN)
panedwindow.add(frame3)
panedwindow.forget(frame3)

window.mainloop()
