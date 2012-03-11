#!/usr/bin/env python
#-*-coding:utf-8-*-

class Application:
	def __init__(self):
		"""A főablak konstruktora"""
		self.root = Tk()
		self.root.title('Színkódok')
		self.drawResistor()
		Label(self.root, text = "Írja be az ellenállás értékét ohm-ban :").grid(row = 2)
		Button(self.root, text = 'Mutat', command = self.changeColours).grid(row = 3, sticky = W)
		Button(self.root, text = 'Kilép', command = self.root.quit).grid(row = 3, sticky = E)
		self.entry = Entry(self.root, width = 14)
		self.entry.grid(row = 3)
		# 0-9 értékek színkódjai
		self.cc = ['black','brown','red','orange','yellow','green','blue','purple','grey','white']
		self.root.mainloop()

	def drawResistor(self):
		"""Vászon ellenállás modellel, amin három szines csík van"""
		self.can = Canvas(self.root, width = 250, height = 100, bg = 'ivory')
		self.can.grid(row = 1, pady = 5, padx = 5)
		self.can.create_line(10, 50, 240, 50, width = 5)
		self.can.create_rectangle(65, 30, 185, 70, fill = 'light grey', width = 2)
		# Három szines csík (induláskor feketék) :
		self.line = []
		for x in range(85, 150, 24):
			self.line.append(self.can.create_rectangle(x, 30, x+12, 70, fill = 'black', width = 0))

	def changeColours(self):
		"""A beírt értéknek megfelelő három szín kiíratása"""
		self.v1ch = self.entry.get()		# get() metódus egy sztringet ad vissza
		try:
			v = float(self.v1ch)			# átalakítás számértékké
		except:
			err = 1
		else:
			err = 0
		if err == 1 or v < 10 or v > 1e11:
			self.reportError()				# inkorrekt vagy tartományon kívüli érték
		else:
			li = [0] * 3					# a 3 kiírandó kód listája
			logv = int(log10(v))			# logaritmus egész része
			ordgr = 10**logv				# nagyságrend
			# az első szignifikáns számjegy előállítása
			li[0] = int(v/ordgr)			# egész rész
			decim = v/ordgr - li[0]			# tizedes rész
			# a második szignifikáns számjegy előállítása
			li[1] = int(decim * 10 + .5)	# +.5 a korrekt kerekítéshez
			# a 2 szignifikáns számjegyhez hozzáteendő nullák száma
			li[2] = logv - 1
			# A 3 szakasz színezése
			for n in range(3):
				self.can.itemconfigure(self.line[n], fill = self.cc[li[n]])

	def reportError(self):
		self.entry.configure(bg = 'red')	# mező hátterének színezése
		self.root.after(1000, self.emptyEntry)	# 1 sec után törölni

	def emptyEntry(self):
		self.entry.configure(bg = 'white')	# fehér háttér visszaállítása
		self.entry.delete(0, len(self.v1ch))	# karakter törlése

from Tkinter import *
from math import log10
f = Application()
