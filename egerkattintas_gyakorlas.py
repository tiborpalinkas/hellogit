#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *

def circle(event):
	"az event.x és event.y középpontú 10 pixel sugarú piros kört jelenít meg"
	can.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fil = "red")

def mutato(event):
	chain.configure(text = "Kattintás detektálva: X = " + str(event.x) +\
							", Y = " + str(event.y))

ablak = Tk()
can = Canvas(ablak, width = 200, height = 200, bg = "ivory")
can.bind("<Button-1>", circle)
can.pack()
chain = Label(ablak)
chain.pack()

ablak.mainloop()

