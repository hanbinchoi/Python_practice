from tkinter import *
win=Tk()

def check():
    print(var1.get(),var2.get())

var1=IntVar()
var2=IntVar()

chk1=Checkbutton(win,text='Music',variable=var1,command=check)
chk1.select()
chk1.pack(side=LEFT)
chk2=Checkbutton(win,text='Video',variable=var2,command=check)
chk2.select()
chk2.pack(side=LEFT)

win.mainloop()
