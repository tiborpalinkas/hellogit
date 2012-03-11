#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *

def updateLabel(x):
	lab.configure(text = 'Aktuális érték = ' + str(x))
	
root = Tk()
Scale(root, length = 250, orient = HORIZONTAL, label  ='Beállítás :',
		troughcolor = 'dark grey', sliderlength = 20, showvalue = 0,
		from_ = -25, to  =125, tickinterval = 25, command = updateLabel).pack()
		
lab = Label(root)
lab.pack()

root.mainloop()
