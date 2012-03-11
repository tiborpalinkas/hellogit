#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
import Pmw

def changeColo(col):
	ablak.configure(background = col)
	
def changeLabel():
	lab.configure(text = combo.get())
	
colours = ('navy', 'royal blue', 'steelblue1', 'cadet blue',
			'lawn green', 'forest green', 'dark red', 
			'grey80', 'grey60', 'grey40', 'grey20')

ablak = Pmw.initialise()
button_ = Button(ablak, text = "Test", command = changeLabel)
button_.grid(row = 1, column = 0, padx = 8, pady = 6)
lab = Label(ablak, text = 'néant', bg = 'ivory')
lab.grid(row = 1, column = 1, padx = 8)

combo = Pmw.ComboBox(ablak, labelpos = NW, label_text = 'Válasszon színt :',
						scrolledlist_items = colours, listheight = 150,
						selectioncommand = changeColo)
combo.grid(row = 2, columnspan = 2, padx = 10, pady = 10)

ablak.mainloop()
