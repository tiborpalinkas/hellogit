#!/usr/bin/env python
#-*-coding:utf-8-*-

def dobozTerfogat(x1=None, x2=None, x3=None):
	"kiszámolja a térfogatot"
	if x1==None and x2==None and x3==None:
		return -1
	if x1!=None and x2==None and x3==None:
		return x1**3
	if x1!=None and x2!=None and x3==None:
		return x1**2*x2
	else:
		return x1*x2*x3

terfogat = dobozTerfogat()
print terfogat
terfogat = dobozTerfogat(5.2)
print terfogat
terfogat = dobozTerfogat(5.2, 3)
print terfogat
terfogat = dobozTerfogat(5.2, 3, 7.4)
print terfogat


