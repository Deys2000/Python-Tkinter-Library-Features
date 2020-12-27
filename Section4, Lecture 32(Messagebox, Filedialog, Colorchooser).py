
#makes a little message box that delivers message and makes another one that has options in it
from tkinter import messagebox
messagebox.showinfo(title="message", message="Hello tkinter")
print(messagebox.askyesno(title="Open", message="Do you want to Open"))


#opens up the browse file in computer thing
from tkinter import filedialog
filename = filedialog.askopenfile()
print(filename.name)


#opens up the color palette
from tkinter import colorchooser
print(colorchooser.askcolor(initialcolor="#ffffff"))
