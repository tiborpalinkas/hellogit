#!/usr/bin/env python
#-*-coding:utf-8-*-

from Tkinter import *
from math import sqrt, pi
	
def mozgat(x, y):
	"általános mozgatóeljárás"
	global d
	if bolygo == 1:
		global x1, y1
		x1, y1 = x, y
		can.coords(bolygo1, x - r1, y - r1, x + r1, y + r1)	
	elif bolygo == 2:
		global x2, y2
		x2, y2 = x, y
		can.coords(bolygo2, x - r2, y - r2, x + r2, y + r2)
	d = tavolsag()
	cimke.configure(text = "Az égitestek közötti távolság: " + str(d) +\
						", gravitációs erő: " + str(gravitacio()) + " N")	
	
def kiv_kek():
	"a kék bolygó kiválasztása"
	global bolygo
	bolygo = 1
	
def kiv_voros():
	"a voros bolygó kiválasztása"
	global bolygo
	bolygo = 2	
	
def tavolsag():
	"kiszámítja a bolygók közötti távolságot"
	if x1 > x2:
		a = x1 - x2
	elif x2 > x1:
		a = x2 - x1
	else:
		a = 0
		
	if y1 > y2:
		b = y1 - y2
	elif y2 > y1:
		b = y2 - y1
	else:
		b = 0
	
	return sqrt(a**2 + b**2)
	
def tomeg(r, ro = 5510):
	"kiszámíja egy égitest tömegét: m = ró * V, ahol m az égitest tömege\
	ró az égitest sűrűsége, alapértelmezetten 5510 kg/m3 (föld sűrűsége),\
	V pedig a térfogata"
	V = (4 * pi * r**3) / 3
	return (ro * V)
	
def gravitacio():
	"kiszámolja az égitestek közötti gravitációs erőt"
	# gravitációs állandó G :
	G = 6.67428E-11
	return G * (m1 * m2) / d**2

def pozicional(event):
	"odahelyezi az égitestet, ahol az egér van"
	mozgat(event.x, event.y)

##### Főprogram #####
ablak = Tk()

# a "kék" bolygó kezdő koordinátái :
x1, y1, r1 = 100, 200, 20
# a "vörös" bolygó kezdő koordinátái :
x2, y2, r2 = 300, 200, 50
# a bolygo változó mutatja, hogy melyik bolygót lehet mozgatni :
bolygo = 1
# a két bolygó közötti távolság :
d = tavolsag()
# a "kék" bolygó tömege (kg)
m1 = tomeg(r1)
# a "vörös" bolygó tömege (kg)
m2 = tomeg(r2)

Label(ablak, text = "kék bolygó = " + str(m1 / 1000) + " T, vörös bolygó = " \
		+ str(m2 / 1000) + " T, távolságskála: millió km").grid(row = 0, column = 1)
can = Canvas(ablak, width = 400, height = 400, bg = "black")
can.bind("<Button-1>", pozicional)
can.grid(row = 1, rowspan = 30, column = 1)
bolygo1 = can.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill = "blue")
bolygo2 = can.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill =  "red")
cimke = Label(ablak, text = "Az égitestek közötti távolság: " + str(d) +\
				", gravitációs erő: " + str(gravitacio()) + " N")
cimke.grid(row = 31, column = 1)
Button(ablak, text = "kék bolygó", command = kiv_kek).grid(row = 1, column = 2)
Button(ablak, text = "vörös bolygó", command = kiv_voros).grid(row = 2, column = 2)

Button(ablak, text = "Kilépés", command = ablak.quit).grid(row = 31, column = 2)

ablak.mainloop()
