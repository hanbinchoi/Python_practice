import time
from tkinter import *
win=Tk()

photo1=PhotoImage(file='all.png')
photo2=PhotoImage(file='blue.png')

def click():
    if lbl['image']=='pyimage1':
        lbl['image']=photo2
    else:
        lbl['image']=photo1
        
lbl=Label(win,image=photo1)
lbl.pack()


btn=Button(win,text='click',command=click)
btn.pack()
win.mainloop()
