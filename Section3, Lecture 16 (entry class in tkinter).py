from tkinter import*

window = Tk()
Hello = Tk()
def hello():
    b=a.get()
    mlabel1 = Label(Hello, text=b,fg='red',bg='green',font=10).pack()
def delete():
    mlabel1 = Label(text="delete",fg='red',bg='green',font=10).pack()


a = StringVar()
window.geometry('500x400+200+300')
Hello.geometry('500x400+800+300')

window.title('Hello World')
Hello.title('Mahmoud')

mlabel = Label(window,text="Welcome", fg = '#EEF44B', bg='blue').pack()
mbutton1 = Button(window, text="enter", width = 15, height=6, fg='red', bg='blue',
                  command=hello, font=20).pack()
mbutton2 = Button(Hello, text="deleted", width = 15, height=6, fg='red', bg='blue',
                  command=delete, font=20).pack()
text=Entry(window, textvariable=a).pack()

window.mainloop()
