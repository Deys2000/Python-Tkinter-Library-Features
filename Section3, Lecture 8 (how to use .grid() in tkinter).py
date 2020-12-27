from tkinter import*

window = Tk()

window.geometry('500x400+150+200')
# The first two numbers are height and width,
# the next two added numbers are cordinates of the top
# left corner of the window on the page.

window.title('Hello World')

# pack() is more a centered placement
# place() allows controlled placement
# grid() allows a placement of objects in rows and columns

mbutton = Button(text="mahmoud raouf").grid(row=1,column=1)
mlabel = Label(text="Welcome", fg = '#EEF44B', bg='blue').grid(row=2, column=2, sticky=W) #sticky gives the object gravity


window.mainloop()
