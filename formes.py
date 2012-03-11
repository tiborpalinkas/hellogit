#!/usr/bin/env python
#-*-coding:utf-8-*-

from math import pi

class Teglalap:
	"téglalap-osztály"
	def __init__(self, hossz = 30, szelesseg = 15):
		self.L = hossz
		self.l = szelesseg
		self.nev = "teglalap"
		
	def kerulet(self):
		return "(%s + %s) * 2 = %s" % (self.L, self.l, (self.L + self.l) * 2)
		
	def terulet(self):
		return "%s * %s = %s" % (self.L, self.l, self.L * self.l)
		
	def meretek(self):
		print "Egy %s x %s -as %s" % (self.L, self.l, self.nev)
		print "területe %s" % (self.terulet())
		
class Negyzet(Teglalap):
	"Négyzet-osztály"
	def __init__(self, oldal = 10):
		Teglalap.__init__(self, oldal, oldal)
		self.nev = "négyzet"
		
class Kor:
	def __init__(self, sugar):
		self.sugar = sugar
		
	def terulet(self):
		"visszaadja a kör területét"
		return self.sugar**2 * pi
		
class Henger(Kor):
	def __init__(self, sugar, magassag):
		Kor.__init__(self, sugar)
		self.magassag = magassag
		
	def terfogat(self):
		"kiszámítja a henger térfogatát"
		return self.terulet() * self.magassag
		
class Kup(Henger):
	def __init__(self, sugar, magassag):
		Henger.__init__(self, sugar, magassag)
		
	def terfogat(self):
		return Henger.terfogat(self) / 3
	
class KartyaJatek:
	
	ertek
		
	def kartya_neve(self, (x, y)):
		return kartyak(x, y)
		
if __name__ == "__main__":
	kartya = KartyaJatek()
	print kartya.kartya_neve((14, 3))
