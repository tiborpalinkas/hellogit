#!/usr/bin/env python 
#-*-coding:utf-8-*-

filename = raw_input("Adja meg a file nevét : ")
try:
	f = open(filename, "r")
except:
	print "A fájl", filename, "nem létezik!"
	exit(-1)

szoveg = ""	
while 1:
	txt = f.readline()
	if txt == "":
		break
	szoveg += txt
	
mondat = ""
legn_mondat = ""
legn_hossza = 0
hossz = 0
i = 0
while i < len(szoveg):
	if szoveg[i] == ".":
		if len(mondat) > legn_hossza:
			legn_hossza = len(mondat)
			legn_mondat = mondat
		mondat = ""
	else:
		mondat += szoveg[i]
	i += 1

print legn_mondat, str(legn_hossza)
