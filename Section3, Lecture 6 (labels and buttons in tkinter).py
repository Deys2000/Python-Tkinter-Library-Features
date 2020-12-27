from tkinter import*

window = Tk()

window.geometry('500x400+200+300')
# The first two numbers are width and height,
# the next two added numbers are cordinates of the top
# left corner of the window on the page.

window.title('Hello World')

mlabel = Label(text="Welcome", fg = 'red', bg='blue').pack()
mbutton = Button(text="mahmoud raouf").place(x=200, y=150)
               
window.mainloop()
