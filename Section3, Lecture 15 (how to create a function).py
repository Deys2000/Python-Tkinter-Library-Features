from tkinter import*

window = Tk()

def hello():
    b=a.get()
    mlabel1 = Label(text=b,fg='red',bg='green',font=10).pack()
def delete():
    mlabel1 = Label(text="delete",fg='red',bg='green',font=10).pack()


a = StringVar()
window.geometry('500x400+200+300')
window.title('Hello World')
mbutton1 = Button(text="enter", width = 15, height=6, fg='red', bg='blue',
                  command=hello, font=20).pack()
mbutton2 = Button(text="deleted", width = 15, height=6, fg='red', bg='blue',
                  command=delete, font=20).pack()
text=Entry(textvariable=a).pack()

mlabel = Label(text="Welcome", fg = '#EEF44B', bg='blue').pack()
window.mainloop()
