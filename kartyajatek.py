#!/usr/bin/env python
#-*-coding:utf-8-*-

from random import randrange

class KartyaJatek:
	"""egy kártyajátékot szimuláló osztály"""
	ertek = [2,3,4,5,6,7,8,9,10,11,12,13,14]
	szin = [0,1,2,3]
	
	def __init__(self):
		self.kartyak = []
		for e in KartyaJatek.ertek:
			for s in KartyaJatek.szin:
				self.kartyak.append((e, s))
			
	def kartya_neve(self, t):
		sz = ['kőr', 'káró', 'treff', 'pikk']
		e = [None, None,2,3,4,5,6,7,8,9,10,'bubi', 'dáma', 'király', 'ász']
		return str(sz[t[1]]) + " " + str(e[t[0]])
			
	def kever(self):
		"megkeveri a lista elemeit"
		seged = ""
		for i in range(0, 52):
			j = randrange(52)
			print i, j
			seged = self.kartyak[i]
			self.kartyak[i] = self.kartyak[j]
			self.kartyak[j] = seged
			
	def huz(self):
		"a kártya színét és értékét adja visszatérési értékül"
		if len(self.kartyak) == 0:
			return None
			
		return self.kartyak[0]
		del self.kartyak[0]
		
if __name__ == "__main__":
	jatek = KartyaJatek()
	jatek.kever()
	for n in range(52):
		c = jatek.huz()
		if c == None:
			print "Vége!"
		else:
			print jatek.kartya_neve(c)
