from tkinter import*

window = Tk()

window.geometry('500x300+200+400')
# The 500 and 300 are width and height,
# the 200 and 400 are cordinates of the top
# left corner of the window on the page.

window.title('Hello World')
mbutton = Button(text="mahmoud raouf").pack()
mlabel = Label(text="Welcome", fg = 'red', bg='blue').pack()
               
window.mainloop()
