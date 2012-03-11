#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
import Pmw

def cimketModosit():
	cimke.configure(text = combo.get())
	
def changeColor(col):
	ablak.configure(bg = col)
	
szinek = ['red', 'yellow', 'brown', 'blue', 'green', 'ivory']

ablak = Tk()
gomb = Button(ablak, text = "Test", command = cimketModosit)
gomb.grid(row = 1, column = 1, padx = 5, pady = 5)
cimke = Label(ablak, text = "üres")
cimke.grid(row = 1, column = 2, padx = 5, pady = 5)
combo = Pmw.ComboBox(ablak, labelpos = NW, label_text = "valasszon",
						scrolledlist_items = szinek, selectioncommand = changeColor)
combo.grid(row = 2, column = 1, columnspan = 2)
ablak.mainloop()
