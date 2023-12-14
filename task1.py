#!python3

import tkinter as tk

from tkinter import *

window =tk.Tk()
window.title("Multiplication Calculator")
window.geometry("1280x720")

entry1 = Entry(window,text="Entry widgets can be typed in", width=30)

lable1 = Label(window,text="X", width = 10)

entry2 = Entry(window,text="Entry widgets can be typed in", width=30)

lable2 = Label(window,text="=", width = 10)

entry3 = Entry(window,text="Entry widgets can be typed in", width=30)


entry1.grid(row = 1, column = 1)
lable1.grid(row = 1, column = 2)
entry2.grid(row = 1, column = 3)
lable2.grid(row = 1, column = 4)
entry3.grid(row = 1, column = 5)


window.mainloop()