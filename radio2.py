#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *

class RadioDemo(Frame):
	"""Egy rádiógombos példa"""
	def __init__(self, boss = None):
		Frame.__init__(self)
		self.pack()
		self.text = Entry(self, width = 30, font = "Arial 14")
		self.text.insert(END, "A programozás nagyszerű")
		self.text.pack(side = TOP)
		self.fontHu = ["Normál", "Kövér", "Dőlt", "Kövér/Dőlt"]
		self.fontEn = ["normal", "bold", "italic", "bold italic"] 
		self.choiceFont = StringVar()
		self.choiceFont.set(self.fontEn[0])
		for n in range(4):
			bout = Radiobutton(self, text = self.fontHu[n], variable = self.choiceFont, 
					value = self.fontEn[n], command = self.changeFont)
			bout.pack(side = LEFT)
			
	def changeFont(self):
		font_ = "Arial 15 " + self.choiceFont.get()
		self.text.configure(font = font_)
		
if __name__ == "__main__":
	RadioDemo().mainloop()
