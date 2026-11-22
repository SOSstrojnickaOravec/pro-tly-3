import tkinter
from random import *
canvas = tkinter.Canvas(width=600,height=600, bg="white")
canvas.pack()

def klik(suradnice):
    x = suradnice.x
    y = suradnice.y
    subor = open("kreslenie.txt","a")
    print(f"{x}", file=subor)
    print(f"{y}", file=subor)
    subor.close()
    canvas.create_oval(x-5,y-5,x+5,y+5)


def vymaz(event):
    subor = open("kreslenie.txt", "w")
    subor.close()
    canvas.delete("all")



canvas.bind("<Button-1>",klik)
canvas.bind_all("<space>",vymaz)

canvas.mainloop()
