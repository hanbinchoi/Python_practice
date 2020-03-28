from tkinter import *

win=Tk()
lbl=Label(win,text='PYTHON',bg='black',fg='white')
lbl.pack()

lbl2=Label(win,text='PYTHON',bg='red',font=('Helvetica',16))
lbl2.pack()

def click():
    btn['text']= "Button Click"

btn=Button(win,text='click',bg='red',fg='white',font=('Arial',14),command=click)
btn.pack()

btn1=Button(win,text='1')
btn1.pack(sied=LEFT)
win.mainloop()
