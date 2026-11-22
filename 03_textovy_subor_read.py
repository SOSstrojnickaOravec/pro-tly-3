import tkinter
from random import *
canvas = tkinter.Canvas(width=600,height=600, bg="white")
canvas.pack()

def citaj():
    riadok = subor.readline()
    if riadok != "":
        x = int(riadok.strip())
        riadok = subor.readline()
        y =int(riadok.strip())
        canvas.create_oval(x-5,y-5,x+5,y+5)
        canvas.after(500,citaj)
    else:
        subor.close()
    


def vymaz(event):
    subor = open("kreslenie.txt", "w")
    subor.close()
    canvas.delete("all")


canvas.bind_all("<space>",vymaz)
subor = open("kreslenie.txt","r")
citaj()

canvas.mainloop()
