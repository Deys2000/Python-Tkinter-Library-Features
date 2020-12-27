from tkinter import*

window = Tk()

window.geometry('500x400+200+300')
# The first two numbers are height and width,
# the next two added numbers are cordinates of the top
# left corner of the window on the page.

window.title('Hello World')

# pack() is more a centered placement
# place() allows controlled placement
# grid() allows a placement of objects in rows and columns

mbutton1 = Button(text="mahmoud raouf", relief=SUNKEN).pack()
mbutton2 = Button(text="mahmoud raouf", relief=FLAT).pack()
mbutton3 = Button(text="mahmoud raouf", relief=GROOVE).pack()
mbutton4 = Button(text="mahmoud raouf", relief=RAISED).pack()
mbutton5 = Button(text="mahmoud raouf", relief=RIDGE).pack()



# you can find color hex codes and use them in python
#mlabel = Label(text="Welcome", fg = '#EEF44B', bg='blue').grid(row=3, column=1, sticky=W) #sticky gives the object gravity


window.mainloop()
