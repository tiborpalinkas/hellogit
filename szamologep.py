#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
from math import *

def kiertekel(event):
	chain.configure(text = "Eredmény = " + str(eval( mezo.get())))
	
ablak = Tk()
mezo = Entry(ablak)
mezo.bind("<Return>", kiertekel)
mezo.pack()
chain = Label(ablak)
chain.pack()

ablak.mainloop()
