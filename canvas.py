#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
import Pmw
from random import randrange

Pmw.initialise()
colo = ["sienna", "maroon", "brown", "pink", "tan", "wheat", "gold", "orange",
		"plum", "red", "khaki", "indian red", "thistle", "firebrick", "salmon", "coral"]
		
class MainWind(Pmw.ScrolledCanvas):
	"""Főablak : nyújtható vászon görgetősávokkal"""
	def __init__(self):
		Pmw.ScrolledCanvas.__init__(self, usehullsize = 1, hull_width = 500, hull_height = 300,
									canvas_bg = "grey40", canvasmargin = 10, labelpos = N,
									label_text = "Kapd el a gombot !",
									borderframe = 1, borderframe_borderwidth = 3)
		# Az alábbi opciókat az inicializálás után meg kell adni :
		self.configure(vscrollmode = "dynamic", hscrollmode = "dynamic")
		self.pack(padx = 5, pady = 5, expand = YES, fill = BOTH)
		
		self.can = self.interior()		# hozzáférés a vászon-komponenshez
		# Dekoráció : véletlen ellipszisek rajzolása :
		for r in range(80):
			x1, y1 = randrange(-800, 800), randrange(-800, 800)
			x2, y2 = x1 + randrange(40, 300), y1 + randrange(40, 300)
			colour = colo[randrange(0, 16)]
			self.can.create_oval(x1, y1, x2, y2, fill = colour, outline = "black")
		# Kisméretű GIF kép hozzáadása :
		self.img = PhotoImage(file = "tux.gif")
		self.can.create_image(50, 20, image = self.img)
		# Annak a gombnak a kirajzolása, amit el kell kapni :
		self.x, self.y = 50, 100
		self.but = Button(self.can, text = "Start", command = self.start)
		self.fb = self.can.create_window(self.x, self.y, window = self.but)
		self.resizescrollregion()
		
	def anim(self):
		if self.run == 0:
			return
		self.x += randrange(-60, 61)
		self.y += randrange(-60, 61)
		self.can.coords(self.fb, self.x, self.y)
		self.configure(label_text = "Keresse %s %s" % (self.x, self.y))
		self.resizescrollregion()
		self.after(250, self.anim)
		
	def stop(self):
		self.run = 0
		self.but.configure(text = "Restart", command = self.start)
		
	def start(self):
		self.but.configure(text = "Kapj el !", command = self.stop)
		self.run = 1
		self.anim()
		
##### Főprogram #####

if __name__ == "__main__":
	MainWind().mainloop()
