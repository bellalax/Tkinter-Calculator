# -*- coding: utf-8 -*-
from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
import parser
from math import *


display=""
firstNum =""
dec=0



class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False


    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):                         # add, minus, multiple, divide
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

                                                                                    #sum1 = Calc()
                                                                                    #root = Tk()
                                                                                    #calc = Frame(root)
                                                                                    #calc.grid()



def clear_all():
    """clears all the content in the Entry widget"""
    label1.config(text="")
    global display
    display=""
def buttonpress1():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Here's what you typed", entrytxt)
def clearList(event):
    listbox1.delete(0, END)    
def openfileR():
    clearList2()
    f=open("ReadMe.txt", 'r')
    for line in f:
        answer=line[0:-1]
        listbox1.insert(END, answer)  
def openfileW():
    f = open("ReadMe.txt", 'w')
    answer = listbox1.get(0, END)
    for i in answer:
        f.write(i+"\n")        
    f.close()    
def clearList2():
    listbox1.delete(0, END)






#types number
def buttonPress0():
    label1.config(text="0")  
    global display
    display += "0"
    label1.config(text=display) 
    global firstNum
    firstNum += "0"
def buttonPress1():
    label1.config(text="1")
    global display
    display += "1"
    label1.config(text=display)
    global firstNum
    firstNum += "1" 
def buttonPress2():
    label1.config(text="2")
    global display
    display += "2"
    label1.config(text=display)
    global firstNum
    firstNum += "2" 
def buttonPress3():
    label1.config(text="3")
    global display
    display += "3"
    label1.config(text=display)
    global firstNum
    firstNum += "3" 
def buttonPress4():
    label1.config(text="4")
    global display
    display += "4"
    label1.config(text=display) 
    global firstNum
    firstNum += "4"
def buttonPress5():
    label1.config(text="5")
    global display
    display += "5"
    label1.config(text=display)
    global firstNum
    firstNum += "5" 
def buttonPress6():
    label1.config(text="6")
    global display
    display += "6"
    label1.config(text=display) 
    global firstNum
    firstNum += "6"
def buttonPress7():
    label1.config(text="7")
    global display
    display += "7"
    label1.config(text=display) 
    global firstNum
    firstNum += "7"
def buttonPress8():
    label1.config(text="8")
    global display
    display += "8"
    label1.config(text=display)
    global firstNum
    firstNum += "8" 
def buttonPress9():
    global display
    display += "9"
    label1.config(text=display)
    global firstNum
    firstNum += "9"
def buttonPress060():
    label1.config(text=".")
    global dec
    global display
    if dec == 0:
        display += "."
        label1.config(text=display) 
        global firstNum
        firstNum += "."
        dec = 1
    

    
       
def buttonPress00():
    label1.config(text="+")
    global display
    listbox1.insert(END, display)                     
    listbox1.insert(END, "+") 
    display += "+"
    label1.config(text=display)
    
    
    
    
    
def buttonPress061():
    label1.config(text="=")
    global display
    display += "="
    label1.config(text=display) 
    listbox1.insert(END, display)      
      
         
def buttonPress000():
    label1.config(text="-")
    global display
    display += "-"
    label1.config(text=display) 
    listbox1.insert(END, display)  
def buttonPress0000():
    label1.config(text="x")
    global display
    display += "x"
    label1.config(text=display) 
    listbox1.insert(END, display) 
def buttonPress062():
    label1.config(text="/")
    global display
    display += "/"
    label1.config(text=display) 
    listbox1.insert(END, display)                     



#design
root = Tk() #gives us a blank canvas object to work with
root.title("Scientific Calculator")

label1 = Label(root, bg="lavender", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=8)

listbox1 = Listbox(root, height=4)
listbox1.grid(row=1, column=0, sticky=EW, columnspan=8) 
listbox1.bind("<Button-3>", clearList)



                                                                                    #scrollbar = Scrollbar(root, orient=VERTICAL)
                                                                                    #listbox1 = Listbox(root, yscrollcommand=scrollbar.set, height=1/3)
                                                                                    #scrollbar.config(command=listbox1.yview)
                                                                                    #scrollbar.grid(row=1, column=2, rowspan=1, sticky=NS)
                                                                                    #listbox1.grid(row=1, column=0, columnspan=8, sticky=EW, rowspan = 10)
                                                                                    #listbox1.bind("<Button-3>", clearList)
    
    

label2 = Label(root, bg="lavender", anchor=W, height=2)
label2.grid(row=2, column=0, sticky=EW, columnspan=8)


#button position
button0 = Button(root, text="0", bg="light grey", command=buttonPress0)
button0.grid(row=6, column=0, sticky=EW, columnspan=2)

button1 = Button(root, text="1", bg="light grey", command=buttonPress1)
button1.grid(row=5, column=0, sticky=EW, columnspan=2)

button2 = Button(root, text="2", bg="light grey", command=buttonPress2)
button2.grid(row=5, column=2, sticky=EW, columnspan=2)

button3 = Button(root, text="3", bg="light grey", command=buttonPress3)
button3.grid(row=5, column=4, sticky=EW, columnspan=2)

button4 = Button(root, text="4", bg="light grey", command=buttonPress4)
button4.grid(row=4, column=0, sticky=EW, columnspan=2)

button5 = Button(root, text="5", bg="light grey", command=buttonPress5)
button5.grid(row=4, column=2, sticky=EW, columnspan=2)

button6 = Button(root, text="6", bg="light grey", command=buttonPress6)
button6.grid(row=4, column=4, sticky=EW, columnspan=2)

button7 = Button(root, text="7", bg="light grey", command=buttonPress7)
button7.grid(row=3, column=0, sticky=EW, columnspan=2)

button8 = Button(root, text="8", bg="light grey", command=buttonPress8)
button8.grid(row=3, column=2, sticky=EW, columnspan=2)

button9 = Button(root, text="9", bg="light grey", command=buttonPress9)
button9.grid(row=3, column=4, sticky=EW, columnspan=2)




button00 = Button(root, text="+", bg="light grey", command=buttonPress00)
button00.grid(row=3, column=6, sticky=EW, columnspan=2)


button000 = Button(root, text="-", bg="light grey", command=buttonPress000)
button000.grid(row=4, column=6, sticky=EW, columnspan=2)

button0000 = Button(root, text="x", bg="light grey", command=buttonPress0000)
button0000.grid(row=5, column=6, sticky=EW, columnspan=2)


button060 = Button(root, text=".", bg="light grey", command=buttonPress060)
button060.grid(row=6, column=2, sticky=EW, columnspan=2)

button061 = Button(root, text="=", bg="light grey", command=buttonPress061)
button061.grid(row=6, column=4, sticky=EW, columnspan=2)

button062 = Button(root, text="/", bg="light grey", command=buttonPress062)
button062.grid(row=6, column=6, sticky=EW, columnspan=2)




menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Clear", command=clear_all)

root.config(menu=menubar)


mainloop() #causes the windows to display on the screen until program closes