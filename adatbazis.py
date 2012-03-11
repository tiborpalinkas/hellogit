#!/usr/bin/env python
#-*-coding:utf-8-*-

def feltolt():
	"feltölt egy szótárat, amely kulcsként tartalmazza \
	a felhasználó nevét, értéke pedig egy kételemű tuple \
	amely tartalmazza a felhasználó életkorát és tesmagasságát"
	global adatbazis
	while 1:
		nev = raw_input("Adja meg a nevét : ")
		if nev == "":
			break
		kor = input("Adja meg a korát : ")
		magassag = input("Adja meg a megasságát : ")
		adatbazis[nev] = (kor, magassag)
		
def megjelenit():
	"egy beírt kulcs alapján visszaadja, az ahhoz tartozó \
	kor, és magasság értéket"
	while 1:
		kulcs = raw_input("Adja meg a keresendő nevet : ")
		if adatbazis.has_key(kulcs):
			print "Név: %s - kor : %s éves - magasság : %s m" % (kulcs, adatbazis[kulcs][0], adatbazis[kulcs][1])
		elif kulcs == "":
			break
		else:
			print "Ilyen név nem található az adatbázisban!"
	
def felcserel(szotar):
	"felcseréli az argumentumként átadott szotar kulcsait és értékeit"
	seged_kulcs = ""
	seged_ertek = ""
	for kulcs, ertek in szotar.items():
		seged_kulcs = kulcs
		seged_ertek = ertek
		del szotar[kulcs]
		szotar[seged_ertek] = seged_kulcs
	return szotar
		
pelda = {'yo' : 'én', 'tú' : 'te', 'el' : 'ő', 'nosotros' : 'mi', 'vosotros' : 'ti', 'ellos' : 'ők'}
print felcserel(pelda)
