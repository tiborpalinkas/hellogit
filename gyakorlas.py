#!/usr/bin/env python
#-*-coding:utf-8-*-

def numerikus(sor):
	"igaz a visszatérési értéke, ha a sor tartalmaz numerikus karaktert"
	for c in sor:
		if c in "0123456789":
			return 1
	return 0
	
def szavak_szama(sor):
	"visszaadja a sorban lévő szavak számát"
	return len(sor.split())
	
def atmasol(source, destination):
	"átmásol egy szövegfájlt, úgy, hogy minden sor nagybetűvel kezdődjön"
	try:
		fs = open(source, "r")
	except:
		print "A fájl % nem létezik" % (source)
		quit(-1)
	
	fd = open(destination, "w")
	while 1:
		txt = fs.readline()
		if txt == "":
			break
		fd.write(txt.capitalize())
	
	fs.close()
	fd.close()
		
atmasol("soros_gyorgy.txt", "kuntakinte")
