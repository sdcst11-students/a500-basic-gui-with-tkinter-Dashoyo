import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Client Database")
window.geometry("700x300")

dogphoto = PhotoImage(file="dog.png")
label1 = Label(window, image = dogphoto, borderwidth = 3)
cldb = Label(window, text="Client Database")
search = Button(window, text="Search by Name")
searchbx = Entry(window, borderwidth=3,)

label1.place(x=0, y= 0)
cldb.place(x = 300, y =50)
search.place(x = 500, y =0)
searchbx.place(x = 650, y =0)

window.mainloop()