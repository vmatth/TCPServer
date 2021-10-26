#!/usr/bin/env python3

from tkinter import *

station = 12
Carrier = 9
Date = "DT#2021-10-26-11:06:47"

window = Tk()
window.geometry('500x500')
window.title("Welcome to LikeGeeks app")

lbl1 = Label(window, text="Station: ", font=("Arial Bold", 50))
lbl2 = Label(window, text=station, font=("Arial Bold", 50))
lbl1.grid(column=0, row=0)
lbl2.grid(column=1, row=0)

lbl3 = Label(window, text="Carrier: ", font=("Arial Bold", 50))
lbl4 = Label(window, text=Carrier, font=("Arial Bold", 50))
lbl3.grid(column=0, row=1)
lbl4.grid(column=1, row=1)

lbl5 = Label(window, text="Date and Time: ", font=("Arial Bold", 50))
lbl6 = Label(window, text=Date, font=("Arial Bold", 50))
lbl5.grid(column=0, row=2)
lbl6.grid(column=1, row=2)

window.mainloop()