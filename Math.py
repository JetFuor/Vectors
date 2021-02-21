'''from math import *

x = int(input())
y = int(input())

answer = sqrt(x**2+y**2)

print(answer)
'''
'''
from tkinter import *
from math import *

root= Tk()

canvas1 = Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = Entry(root) 
entry2 = Entry(root)
canvas1.create_window(200, 140, window=entry1)
canvas1.create_window(200, 140, window=entry2)

def getSquareRoot ():  
    x1 = int(entry1.get())
    y1 = int(entry2.get())
    
    label1 = Label(root, text= sqrt(x1**2+y1**2)
    #canvas1.create_window(200, 230, window=label1)

    
button1 = Button(text='Get the Square Root', command:lambda = getSquareRoot())
canvas1.create_window(200, 180, window=button1)

root.mainloop()
'''
'''
from tkinter import *
from math import *

root= Tk()

canvas1 = Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = Entry (root)
entry2 = Entry (root) 
canvas1.create_window(200, 140, window=entry1)
canvas1.create_window(200, 200, window=entry2)

def getSquareRoot ():  
    x1 = float(entry1.get())
    y1 = float(entry2.get())
    
    label1 = Label(root, text= sqrt(x1**2 + y1**2))
    canvas1.create_window(200, 230, window=label1)
    
button1 = Button(text='Get the Square Root', command=getSquareRoot)
canvas1.create_window(200, 250, window=button1)

root.mainloop()
'''
def printtext():
    global e
    string = e.get() 
    print(string)   

from tkinter import *
root = Tk()

root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')
root.mainloop()