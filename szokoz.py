#!/usr/bin/env python
#-*-coding:utf-8-*-

def atalakit(txt):
	"a txt szövegben található szóközök számát megháromszorozza"
	i = 0
	uj_txt = ""
	while i < len(txt):
		if txt[i] == " ":
			uj_txt += "   "
		uj_txt += txt[i]
		i += 1
	return uj_txt

def copyfile_with_spaces(source, destination):
	"átmásol egy fájlt úgy, hogy a szavak között megháromszorozza \
	a szóközök számát"
	try:
		f = open(source, "r")
		fw = open(destination, "w")
	except:
		print "nincs ilyen file"
		exit(-1)
	while 1:
		txt = f.readline()
		if txt == "":
			break
		fw.write(atalakit(txt))
	f.close()
	fw.close()
	
copyfile_with_spaces("kuntakinte", "uj_kuntakinte")	

