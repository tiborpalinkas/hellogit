#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *

def mutato(event):
	chain.configure(text = "Katintás detektálva: X = " + str(event.x) +\
							", Y = " + str(event.y))

ablak = Tk()
keret = Frame(ablak, width = 200, height = 150, bg = "light yellow")
keret.bind("<Button-1>", mutato)
keret.pack()
chain = Label(ablak)
chain.pack()

ablak.mainloop()
