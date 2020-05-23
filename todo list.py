import tkinter
from tkinter import *

root = Tk()
root.title('HABITIFY')
root.iconbitmap('C:/Users/kaust/Downloads/japan.ico')

e = Entry(root)
e.pack()

#
def comp():
    response = Label(root,text = 'YAYYYYY TASK COMPLETED NOW KILL URSELF U USELESS PIECE OF SHIT').pack()

def shit():
    ting2 = Button(root,text = e.get(),command = comp).pack()

# list
ting = Button(root,text = 'click me after setting ur shit',command=shit).pack()

root.mainloop()