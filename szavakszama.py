#!/usr/bin/env python
#-*-coding:utf-8-*-

mondat = "Kuntakinte betekinte, mert ha betekint, az jó"
szo = 0
for e in mondat:
	if e == " ":
		szo += 1
print "szavak száma :", szo + 1
