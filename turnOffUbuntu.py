import os
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("200x100")

def turnOff():
   os.system("shutdown -P 0")

def cans():
   top.destroy()

var = StringVar()
label = Message(top,textvariable=var,relief=FLAT)

var.set("Vil du skru av dataen?")
label.pack()

Ok = Button(top, text = "Ja", command = turnOff)
Ok.place(x = 50,y = 50)
cancel = Button(top, text = "Nei", command = cans)
cancel.place(x = 100,y = 50)

top.mainloop()

#os.system("shutdown -P 0")