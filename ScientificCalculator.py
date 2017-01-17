# -*- coding: utf-8 -*-
from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
from datetime import datetime

def buttonpress1():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Here's what you typed", entrytxt)
def clearList(event):
    listbox1.delete(0, END)
   




root = Tk() #gives us a blank canvas object to work with
root.title("Scientific Calculator")

label1 = Label(root, bg="lavender", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=8)

listbox1 = Listbox(root, height=1)
listbox1.grid(row=1, column=0, sticky=EW, columnspan=8)
listbox1.bind("<Button-3>", clearList)

label2 = Label(root, bg="lavender", anchor=W)
label2.grid(row=2, column=0, sticky=EW, columnspan=8)

button7 = Button(root, text="7", bg="light grey")
button7.grid(row=3, column=0, sticky=EW, columnspan=2)

button8 = Button(root, text="8", bg="light grey")
button8.grid(row=3, column=2, sticky=EW, columnspan=2)

button9 = Button(root, text="9", bg="light grey")
button9.grid(row=3, column=4, sticky=EW, columnspan=2)

button00 = Button(root, text="+", bg="light grey")
button00.grid(row=3, column=6, sticky=EW, columnspan=2)

button4 = Button(root, text="4", bg="light grey")
button4.grid(row=4, column=0, sticky=EW, columnspan=2)

button5 = Button(root, text="5", bg="light grey")
button5.grid(row=4, column=2, sticky=EW, columnspan=2)

button6 = Button(root, text="6", bg="light grey")
button6.grid(row=4, column=4, sticky=EW, columnspan=2)

button000 = Button(root, text="-", bg="light grey")
button000.grid(row=4, column=6, sticky=EW, columnspan=2)

button1 = Button(root, text="1", bg="light grey")
button1.grid(row=5, column=0, sticky=EW, columnspan=2)

button2 = Button(root, text="2", bg="light grey")
button2.grid(row=5, column=2, sticky=EW, columnspan=2)

button3 = Button(root, text="3", bg="light grey")
button3.grid(row=5, column=4, sticky=EW, columnspan=2)

button0000 = Button(root, text="x", bg="light grey")
button0000.grid(row=5, column=6, sticky=EW, columnspan=2)

button0 = Button(root, text="0", bg="light grey")
button0.grid(row=6, column=0, sticky=EW, columnspan=2)

button060 = Button(root, text=".", bg="light grey")
button060.grid(row=6, column=2, sticky=EW, columnspan=2)

button061 = Button(root, text=".", bg="light grey")
button061.grid(row=6, column=2, sticky=EW, columnspan=2)

button062 = Button(root, text="=", bg="light grey")
button062.grid(row=6, column=4, sticky=EW, columnspan=2)

button063 = Button(root, text="/", bg="light grey")
button063.grid(row=6, column=6, sticky=EW, columnspan=2)







mainloop() #causes the windows to display on the screen until program closes