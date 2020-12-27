from tkinter import*

window = Tk()

window.geometry('500x400+200+300')
# The first two numbers are height and width,
# the next two added numbers are cordinates of the top
# left corner of the window on the page.

window.title('Hello World')

#some of the diagrams that can be drawn on buttons with bitmap
mbutton1 = Button(text="mahmoud raouf", cursor="circle").pack()
mbutton2 = Button(text="mahmoud raouf", cursor="heart").pack()
mbutton3 = Button(text="mahmoud raouf", cursor="plus").pack()
mbutton4 = Button(text="mahmoud raouf", cursor="clock").pack()
mbutton5 = Button(text="mahmoud raouf", cursor="dotbox").pack()
mbutton6 = Button(text="mahmoud raouf", cursor="man").pack()
mbutton7 = Button(text="mahmoud raouf", cursor="mouse").pack()
mbutton8 = Button(text="mahmoud raouf", cursor="pirate").pack()
mbutton9 = Button(text="mahmoud raouf", cursor="sizing").pack()
mbutton10 = Button(text="mahmoud raouf", cursor="star").pack()



# you can find color hex codes and use them in python
#mlabel = Label(text="Welcome", fg = '#EEF44B', bg='blue').grid(row=3, column=1, sticky=W) #sticky gives the object gravity


window.mainloop()
