from tkinter import *
win=Tk()

def check():
    print(g1.get())

g1=StringVar()

rdo1=Radiobutton(win,text='Male',variable=g1,value='M',command=check)
rdo1.pack(side=LEFT)
rdo1.select()
rdo2=Radiobutton(win,text='Female',variable=g1,value='F',command=check)
rdo2.pack(side=LEFT)
