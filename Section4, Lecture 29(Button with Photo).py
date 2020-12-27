from tkinter import*
from tkinter import ttk

window = Tk()

button = ttk.Button(window, text = "Clickme")
button.pack()

def Callback():
    print("Clicked")

button.config(command=Callback)

photo = PhotoImage(file = '*insert name of file here.filetype')
button.config(image=photo, compound=LEFT) #puts picture left of text
small_photo = photo.subsample(5,5) # size of the photo
button.config(image = small_photo) # updates the photo size

window.mainloop()
