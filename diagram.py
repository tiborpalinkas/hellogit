#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
from math import sin, pi

class Diagram(Canvas):
	def __init__(self, boss = None, width_ = 200, height_ = 150):
		Canvas.__init__(self)
		self.configure(width = width_, height = height_)
		self.width_, self.height_ = width_, height_
		# x-tengely felosztása :
		self.step = (width_ - 10) / 8.
		for sx in range(8):
			x = 10 + (sx + 1) * self.step
			self.create_line(x, height_ -4, x, 4, fill = 'grey')
		# y-tengely felosztása :
		self.step = (height_ - 8) / 10.
		for sy in range(10):
			y = (height_ - 4) - sy * self.step
			self.create_line(10, y, width_, y, fill = 'grey')
		# tengelyek megrajzolása :
		self.create_line(10, height_ / 2, width_, height_ / 2, width = 2, arrow = LAST)		# x-tengely
		self.create_line(10, height_ - 4, 10, 4, width = 2, arrow = LAST)					# y-tengely
		
		self.create_text(20, 10, text = "e", anchor = CENTER)
		self.create_text(width_ - 10, height_ / 2 - 10, text = "t", anchor = CENTER)
		
	def drawCurve(self, freq = 1, phase = 0, ampl = 10, colo = 'red'):
		"1 sec időtartamra eső kitérés/idő görbe rajzolása"
		curve = []										# koordináták listája
		step = (self.width_ - 20.5) / 1000.
		for t in range(1, 1001, 5):
			e = ampl * sin(2 * pi * freq * t / 1000 - phase)
			x = 12 + t * step
			y = self.height_ / 2 - e * self.height_ / 20.5
			curve.append((x, y))
		n = self.create_line(curve, fill = colo, smooth = 1)
		return n
		
if __name__ == "__main__":
	ablak = Tk()
	gra = Diagram(ablak, 400, 300)
	gra.pack()
	gra.configure(bg = 'ivory', bd = 2, relief = SUNKEN)
	gra.drawCurve(2, 1.2, 10, 'purple')
	
	ablak.mainloop()
