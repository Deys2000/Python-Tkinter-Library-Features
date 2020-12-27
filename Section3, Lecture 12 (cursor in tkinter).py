from tkinter import*

window = Tk()

window.geometry('500x400+200+300')
# The first two numbers are height and width,
# the next two added numbers are cordinates of the top
# left corner of the window on the page.

window.title('Hello World')

#styling a button
mbutton2 = Button(text="mahmoud raouf",width=15,height=6,fg="red",bg="blue",
                 bd=15, activebackground="green", cursor="heart").pack()

# you can find color hex codes and use them in python
#mlabel = Label(text="Welcome", fg = '#EEF44B', bg='blue').grid(row=3, column=1, sticky=W) #sticky gives the object gravity

window.mainloop()
