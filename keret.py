#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *

ablak = Tk()
ablak.title("Keretekkel létrehozott ablak")
ablak.geometry("300x300")

f1 = Frame(ablak, bg = "#80c0c0")
f1.pack(side = LEFT, padx = 5)
adatok = [(0, 'grey50', RAISED, 'Kiemelkedő felület'),
			(1, 'grey60', SUNKEN, 'Bemélyedő felület'),
			(2, 'grey70', FLAT, 'Sík felület'),
			(3, 'grey80', RIDGE, 'Gerinc'),
			(4, 'grey90', GROOVE, 'Árok'),
			(5, 'grey100', SOLID, 'Szegély')]

fint = [0] * 6
for (n, col, rel, txt) in adatok:
	fint[n] = Frame(f1, bd = 2, relief = rel)
	e = Label(fint[n], text = txt, width = 15, bg = col)
	e.pack(side = LEFT, padx = 5, pady = 5)
	fint[n].pack(side = TOP, padx = 10, pady = 5)
	
f2 = Frame(ablak, bg = '#d0d0b0', bd = 2, relief = GROOVE)
f2.pack(side = RIGHT, padx = 5)

can = Canvas(f2, width = 80, height = 80, bg = 'white', bd = 2, relief = SOLID)
can.pack(padx = 15, pady = 15)
gomb = Button(f2, text = "Gomb")
gomb.pack()
	
ablak.mainloop()
