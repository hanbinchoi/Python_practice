from tkinter import *
win=Tk()

def click():
    print(entry.get())

entry=Entry(win,show='*')
entry.pack(fill=X)

btn=Button(win,text='view',command=click)
btn.pack(fill=X)

win.mainloop()
