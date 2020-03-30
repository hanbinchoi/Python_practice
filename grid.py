from tkinter import *
win=Tk()

for r in range(2):
    for c in range(3):
        Button(win,text='{},{}'.format(r,c,)).grid(row=r,column=c)

mainloop()
