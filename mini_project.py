from tkinter import *
from tkinter.ttk import *

from time import strftime

a=Tk()
a.title("Mini Clock")

def time():
	s=strftime('%H:%M:%S %p')
	label.config(text=s)
	label.after(1000,time)
label=Label(a, font=("d=digital",40),background="red",foreground="white")
label.pack(anchor='center')
time()

mainloop()
