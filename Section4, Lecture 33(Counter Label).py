from tkinter import*
from tkinter import ttk

counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter +=1
        label.config(text=str(counter))
        label.after(1000, count)
    count()



window= Tk()
window.title("counter")
label = ttk.Label(window, foreground="#000000")
label.pack()

counter_label(label)
button = ttk.Button(window, text = "END", width = 30, command = window.destroy)
button.pack()

window.mainloop()
