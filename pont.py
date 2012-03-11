#!/usr/bin/env python
#-*-coding:utf-8-*-

################################################
# Python program                 			   #
# Szerző: Pálinkás Tibor, Kunszentmárton, 2012 #
# Licenc: GPL                                  #
################################################

class Pont:
	"""matematikai pont"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
class Teglalap:
	"""téglalap"""
	def __init__(self, sar, ho, sze):
		self.sar = sar
		self.ho = ho
		self.sze = sze
		
	def kozepMeghat(self):
		xc = self.sar.x + self.ho / 2
		yc = self.sar.y + self.sze / 2
		return Pont(xc, yc)
		
class Negyzet(Teglalap):
	"""négyzet = spec. téglalap"""
	def __init__(self, csucs, ol):
		Teglalap.__init__(self, csucs, ol, ol)
		self.ol = ol
		
	def terulet(self):
		return self.ol**2
		
bfsT = Pont(40, 30)
bfsN = Pont(10, 25)

dobozT = Teglalap(bfsT, 100, 50)
dobozN = Negyzet(bfsN, 40)

cT = dobozT.kozepMeghat()
cN = dobozN.kozepMeghat()

print "téglalap közepe: ", cT.x, cT.y
print "négyzet közepe: ", cN.x, cN.y

print "a négyzet területe :",
print dobozN.terulet()
