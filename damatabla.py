#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
from random import randrange

def create_table():
	"create a chess-table"
	x1, y1, x2, y2 = 0, 0, 20, 20
	i = 0
	j = 0
	while i < 10:
		while j < 10:
			if j % 2 == 0 and i % 2 == 0:
				color = "blue"
			elif j % 2 == 0 and i % 2 != 0:
				color = "white"
			elif j % 2 != 0 and i % 2 == 0:
				color = "white"
			else:
				color = "blue"
				
			can.create_rectangle(x1, y1, x2, y2, fill = color)
			# elmentjük a majdani korongok lehetséges pozícióit
			lista.append([x1 + 10, y1 + 10])
			x1 += 20
			x2 += 20
			j += 1
		x1 = 0
		y1 += 20
		x2 = 20
		y2 += 20
		i += 1
		j = 0
	k = 0

def circle(x, y, r):
	"egy (x,y) középpontú r sugarú, alapértelmezetten vörös kört rajzol"
	can.create_oval(x - r, y - r, x + r, y + r, fill = "red")
	
def circles():
	szam = lista[randrange(100)]
	circle(szam[0], szam[1], 7)
	
##### Main Program #####

lista = []

window = Tk()
can = Canvas(window, width = "200", height = "200", bg = "white")
can.pack(side = TOP, padx = 5, pady = 5)
button1 = Button(window, text = "dámatábla", command = create_table)
button1.pack(side = LEFT, padx = 3, pady = 3)
button2 = Button(window, text = "korongok", command = circles)
button2.pack(side = RIGHT, padx = 2, pady = 3)

window.mainloop()
