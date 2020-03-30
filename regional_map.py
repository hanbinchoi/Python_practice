from tkinter import *

win=Tk();
win.title("Map");
win.geometry("300x320");

photo1=PhotoImage(file='africa.png')
photo2=PhotoImage(file='america.jpg')
label1=Label(win,text='MAP',font=('Alial',20))
label1.pack(fill='x')

def check():
    if group.get()==1:
        lbl['image']=photo1
        
    elif group.get()==2:
        lbl['image']=photo2

    elif group.get()==3:
        lbl['image']=photo1

    else:
        lbl['image']=photo2
        
frame1=Frame(win)
group=IntVar()

radio1=Radiobutton(frame1,text='Africa',value=1,variable=group,command=check)
radio1.pack(side=LEFT)

radio2=Radiobutton(frame1,text='America',value=2,variable=group,command=check)
radio2.pack(side=LEFT)

radio3=Radiobutton(frame1,text='Asia',value=3,variable=group,command=check)
radio3.pack(side=LEFT)

radio4=Radiobutton(frame1,text='Europe',value=4,variable=group,command=check)
radio4.pack(side=LEFT)

frame1.pack()



lbl=Label(win,width=300,height=320,bg='gray')
lbl.pack()

win.mainloop()
