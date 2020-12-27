from tkinter import*

master = Tk()

Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

def Show_entry_fields():
    print("First Name: %s \n Last Name: %s" % (e1.get(), e2.get()))
    e1.delete(0,END)
    e2.delete(0,END)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text="Quit", command=master.quit).grid(row=3, column=0)
Button(master, text="Show", command= Show_entry_fields).grid(row=3, column=1)

mainloop()
