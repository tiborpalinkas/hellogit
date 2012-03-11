#!/usr/bin/env python
#-*-coding:utf-8-*-

filename = raw_input("Adja meg a file nevét : ")
try:
	f = open(filename, "r")
except:
	print "A fájl", filename, "nem létezik."
	exit(-1)

ujfile = raw_input("Adja meg az új fájl nevét, amelybe menteni akar : ")
uf = open(ujfile, "w")

while 1:
	num = f.readline()
	if num == "":
		break
	uf.write(str(round(float(num))) + "\n")
	
f.close()
uf.close()
