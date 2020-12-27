from tkinter import*
from tkinter import ttk

window = Tk()

progressbar = ttk.Progressbar(window, orient=HORIZONTAL, length=200)
progressbar.pack()

progressbar.config(mode = "indeterminate")
progressbar.start()
progressbar.stop()
progressbar.config(mode="determinate", maximum = 11.0, value=4.2)

value = DoubleVar()
progressbar.config(variable = value)

scale = ttk.Scale(window, orient = HORIZONTAL,
                  length = 400, variable = value,
                  from_ = 0.0, to = 11.0)
scale.pack()
scale.set(3.0)

window.mainloop()
