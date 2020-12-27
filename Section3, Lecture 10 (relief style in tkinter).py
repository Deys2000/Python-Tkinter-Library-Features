from tkinter import*

window = Tk()

window.geometry('500x400+200+300')
# The first two numbers are height and width,
# the next two added numbers are cordinates of the top
# left corner of the window on the page.

window.title('Hello World')

# five ways to style a button, they MUST be written in capitals
mbutton1 = Button(text="mahmoud raouf", bitmap="error").pack()
mbutton2 = Button(text="mahmoud raouf", bitmap="hourglass").pack()
mbutton3 = Button(text="mahmoud raouf", bitmap="info").pack()
mbutton4 = Button(text="mahmoud raouf", bitmap="gray75").pack()
mbutton5 = Button(text="mahmoud raouf", bitmap="gray50").pack()
mbutton6 = Button(text="mahmoud raouf", bitmap="gray25").pack()
mbutton7 = Button(text="mahmoud raouf", bitmap="gray12").pack()
mbutton8 = Button(text="mahmoud raouf", bitmap="questhead").pack()
mbutton9 = Button(text="mahmoud raouf", bitmap="warning").pack()
mbutton10 = Button(text="mahmoud raouf", bitmap="question").pack()



# you can find color hex codes and use them in python
#mlabel = Label(text="Welcome", fg = '#EEF44B', bg='blue').grid(row=3, column=1, sticky=W) #sticky gives the object gravity


window.mainloop()
