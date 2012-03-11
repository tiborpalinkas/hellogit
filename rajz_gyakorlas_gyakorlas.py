#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
from random import randrange

class Draw(Frame):
	"Rajzolást elősegítő osztály"
	def __init__(self):
		Frame.__init__(self)
		self.c = Canvas(self, width = 400, height = 300, bg = 'ivory')
		self.c.pack(padx = 5, pady = 5)
		
		for i in range(9):
			color = ['yellow', 'blue', 'brown', 'cyan', 'grey', 'green',
					'red', 'violet', 'pink'][randrange(9)]
			x1, y1 = randrange(300), randrange(150)
			x2, y2 = x1 + randrange(150), y1 + randrange(150)
			self.c.create_oval(x1, y1, x2, y2, fill = color)
		self.c.bind('<Button-1>', self.mouseDown)
		self.c.bind('<Button1-Motion>', self.mouseMove)
		self.c.bind('<Button1-ButtonRelease>', self.mouseUp)
		b_fin = Button(self, text = "Befejezés", bg = "royal blue", fg = "white",
						command = self.quit)
		b_fin.pack(padx = 5)
		self.pack()
		
	def mouseDown(self, event):
		#self.selObject = None
		self.x1, self.y1 = event.x, event.y
		self.selObject = self.c.find_closest(self.x1, self.y1)
		self.c.itemconfig(self.selObject, width = 3)
		self.c.lift(self.selObject)
		
	def mouseMove(self, event):
		x2, y2 = event.x, event.y
		dx, dy = x2 - self.x1, y2 - self.y1
		if self.selObject:
			self.c.move(self.selObject, dx, dy)
			self.x1, self.y1 = x2, y2
			
	def mouseUp(self, event):
		if self.selObject:
			self.c.itemconfig(self.selObject, width = 1)
			self.selObject = None
		
if __name__ == "__main__":
	Draw().mainloop()
