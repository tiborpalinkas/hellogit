#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
from random import randrange

def drawline():
	global x1, y1, x2, y2, color
	can1.create_line(x1, y1, x2, y2, width=2, fill=color)
	
	y1, y2 = y1 + 10, y2 + 10
	
def drawline2():
	can1.create_line(250, 10, 250, 640, width=5, fill='red')
	can1.create_line(10, 325, 490, 325, width=5, fill='red')
	
def drawrectangle(
	
def changecolor():
	global color
	szinek = ['purple', 'red', 'blue', 'orange', 'yellow']
	cc = randrange(5)
	color = szinek[cc]

x1, y1, x2, y2 = 10, 10, 490, 10
color = 'dark green'

abl1 = Tk()
can1 = Canvas(abl1, bg='dark grey', height=650, width=500)
can1.pack(side=LEFT)
gomb1 = Button(abl1, text='Kilép', command=abl1.quit)
gomb1.pack(side=BOTTOM)
gomb2 = Button(abl1, text='Vonalat rajzol', command=drawline)
gomb2.pack()
gomb3 = Button(abl1, text='Más szín', command=changecolor)
gomb3.pack()
gomb4 = Button(abl1, text='Kereső', command=drawline2)
gomb4.pack()

abl1.mainloop()
abl1.destroy()
