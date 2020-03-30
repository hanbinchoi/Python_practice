from tkinter import *

win=Tk()

id=Label(win,text='ID')
id.pack(fill=X)

idEntry=Entry(win)
idEntry.pack(fill=X)

pw=Label(win,text='PW')
pw.pack(fill=X)

pwEntry=Entry(win,show='*')
pwEntry.pack(fill=X)


def click1():
    print('ID :',idEntry.get())
    print('PW :',pwEntry.get())
    if var.get() == 1:
        print('You are ADMIN')
    else:
        print('You are USER')

def click2():
    win.destroy()

var=IntVar()

chk=Checkbutton(win,text='Admin',variable=var)
chk.pack(side=LEFT)

btn1=Button(win,text='Login',command=click1)
btn1.pack(side=LEFT)

btn2=Button(win,text='Cancel',command=click2)
btn2.pack(side=LEFT)


