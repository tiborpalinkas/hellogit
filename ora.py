#!/usr/bin/env python
#-*-coding:utf-8-*-

class Atom:
	"""egyszerűsített atomok, a Per.Rendszer első 10 eleme közül választva"""
	table = [None, ('hidrogén', 0), ('hélium', 2), ('lítium', 4),
				('berilium', 5), ('bór', 6), ('szén', 6), ('nitrogén', 7),
				('oxigén', 8), ('fluor', 10), ('neon', 10)]
				
	def __init__(self, nat):
		"a rendszám meghatározza a protonok, elektronok és neutronok számát"
		self.np, self.ne = nat, nat		# nat = rendszer
		self.nn = Atom.table[nat][1]	# neutronszám a táblázatból
		
	def kiir(self):
		print
		print "Az elem neve :", Atom.table[self.np][0]
		print "%s proton, %s elektron, %s neutron" % \
				(self.np, self.ne, self.nn)
				
class Ion(Atom):
	"""az ionok atomok, amik elektronokat vettek fel vagy vesztettek"""
	
	def __init__(self, nat, toltes):
		"a rendszam és a töltés határozzák meg az iont"
		Atom.__init__(self, nat)
		self.ne = self.ne - toltes
		self.toltes = toltes
		
	def kiir(self):
		"ez a metódus a szülőosztálytól örökölt metódust helyettesíti"
		Atom.kiir(self)		# a szülőosztály metódusát is használja !
		print "Töltött részecske. Töltés =", self.toltes
		
### Főprogram : ###

a1 = Atom(5)
a2 = Ion(3, 1)
a3 = Ion(8, -2)
a1.kiir()
a2.kiir()
a3.kiir()
