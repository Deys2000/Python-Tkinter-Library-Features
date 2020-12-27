from tkinter import*
from tkinter import ttk

window = Tk()

month = StringVar()

#making the combobox, putting it in window and giving it values
combox = ttk.Combobox(window, textvariable=month)
combox.pack()
combox.config(values= ("Jan","Feb","Mar","Apr","May","Jun",
                       "Jul","Aug","Sep","Oct","Nov","Dec"))
#print does not do anything for the combobox or spinbox
print(month.get())
month.set('jan')
#setting the default value of the combobox
month.set('Not a month')

year = StringVar()
#making a spinbox and giving it values to hold with limits
Spinbox(window, from_ = 1990, to = 2016, textvariable = year).pack()
print(year.get())


window.mainloop()
