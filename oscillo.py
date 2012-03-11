#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
from math import sin, pi

class OscilloGraphe(Canvas):
	"kitérés/idő görbe rajzolására szolgáló specializált vászon"
	def __init__(self, boss = None, width_ = 200, height_ = 150):
		"A grafika constructora : tengelyek és vízszintes skála."
		# a szülő widget elkészítése :
		Canvas.__init__(self)
		self.configure(width = width_, height = height_)
		self.width_, self.height_ = width_, height_
		# tengelyek megrajzolása :
		self.create_line(10, height_/2, width_, height_/2, arrow = LAST)
		self.create_line(10, height_-5, 10, 5, arrow = LAST)
		# 8 osztású skála rajzolása :
		step = (width_-25) / 8.
		for t in range(1, 9):
			stx = 10 + t*step
			self.create_line(stx, height_/2 - 4, stx, height_/2 + 4)
			
		step = (height_ - 20) / 10.
		for e in range(1, 11):
			sty = 10 + e * step
			self.create_line(7.5, sty, 13.5, sty)
		self.create_text(20, 10, text = "e", anchor = CENTER)
		self.create_text(width_ - 10, height_ / 2 -10, text = "t", anchor = CENTER)
		
		
			
	def drawCurve(self, freq = 1, phase = 0, ampl = 10, colo = 'red'):
		"1 sec időtartamra eső kitérés/idő görbe rajzolása"
		curve = []
		step = (self.width_ - 25) / 1000.
		for t in range(0, 1001, 5):
			e = ampl * sin(2 * pi * freq * t / 1000 - phase)
			x = 10 + t * step
			y = self.height_ / 2 - e * self.height_ / 25
			curve.append((x,y))
		n = self.create_line(curve, fill = colo, smooth = 1)
		return n
		
### Kód az osztály teszteléséhez ###

if __name__ == "__main__":
	root = Tk()
	gra = OscilloGraphe(root, 250, 180)
	gra.pack()
	gra.configure(bg = 'ivory', bd = 2, relief = SUNKEN)
	gra.drawCurve(2, 1.2, 10, 'purple')
	root.mainloop()

