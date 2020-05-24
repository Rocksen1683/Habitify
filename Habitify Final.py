import tkinter
from tkinter import *
import sqlite3

root = Tk()
root.iconbitmap('japan.ico')
root.title('Habitify')
root.geometry('400x200')

txt1 = Entry(root)
txt1.pack()

def create2():
    var = IntVar()

    box = Checkbutton(root2, text=txt2.get(), variable=var)
    box.deselect()
    box.pack()

def open():
    global root2
    global txt2
    root2 = Toplevel()
    root2.title(txt1.get())
    root2.iconbitmap('japan.ico')
    root2.geometry('400x200')

    txt2 = Entry(root2)
    txt2.pack()

    buttonplus2 = Button(root2, text='+', command=create2)
    buttonplus2.pack()
    txt2.delete(0,END)

def create():
    button = Button(root,text = txt1.get(),command=open)
    button.pack()
    txt1.delete(0,END)

buttonplus = Button(root,text = '+',command = create)
buttonplus.pack()

mainloop()