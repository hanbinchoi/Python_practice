from tkinter import *
win=Tk()
win.geometry('200x200+400+200')

lbl=Label(win,text='',font=('Arial',40))
lbl.pack()

def korean():
    lbl['text']='안녕'

def english():
    lbl['text']='hello'

def spanish():
    lbl['text']='hola'


btn1=Button(win,text='한국어',bg='yellow',command=korean)
btn1.pack(fill=BOTH,expand=YES)

btn2=Button(win,text='English',bg='green',command=english)
btn2.pack(fill=BOTH,expand=YES)

btn3=Button(win,text='Spanish',bg='blue',command=spanish)
btn3.pack(fill=BOTH,expand=YES)


win.mainloop()
