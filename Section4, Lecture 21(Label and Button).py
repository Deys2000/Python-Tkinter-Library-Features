from tkinter import Tk, Button, Label

class MYGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="GUI")
        self.label.pack()

        self.greet_Button = Button(master, text="Greet", command=self.greet)
        self.greet_Button.pack()

        self.greet_Button = Button(master, text="Quit", command= master.quit)
        self.greet_Button.pack()

    def greet(self):
        print("greetings")


root = Tk()
MY_GUI = MYGUI(root)
root.mainloop()
