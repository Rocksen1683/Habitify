import tkinter
from tkinter import *
import sqlite3

root = Tk()

root.iconbitmap('japan.ico')
root.title('Habitify')
root.geometry('400x200')


global txt1
txt1 = Entry(root,width=400)
txt1.insert(0,'pls run list after creating')
txt1.pack()

def create2():
    var = IntVar()

    box = Checkbutton(root2, text=txt2.get(), variable=var,bg='red',fg='black',font='Helvetica 10')
    box.deselect()
    box.pack()
    txt2.delete(0,END)

def open():
    global root2
    global txt2
    root2 = Toplevel()
    root2.title(txt1.get())
    txt1.delete(0,END)
    root2.iconbitmap('japan.ico')
    root2.geometry('400x200')
    root2.configure(background='black')
    txt2 = Entry(root2,width = 400)
    txt2.pack()

    buttonplus2 = Button(root2, text='+', command=create2,bg='red',fg='black',font='Helvetica 10')
    buttonplus2.pack()

def create():
    button = Button(root,text = txt1.get(),command=open,bg='red',fg='black',font='Helvetica 10')
    button.pack()

buttonplus = Button(root,text = '+',command = create,bg='red',fg='black',font='Helvetica 10')
buttonplus.pack()
root.configure(background='black')

mainloop()
