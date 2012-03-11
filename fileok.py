#!/usr/bin/env python
#-*-coding:utf-8-*-

def existe(fname):
	try:
		f = open(fname, "r")
		f.close()
		return 1
	except:
		return 0
		
filename = raw_input("Irjon be egy filenevet : ")
if existe(filename):
	print "Ez a file létezik."
else:
	print "A file", filename, "nem létezik."
