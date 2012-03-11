#!/usr/bin/env python
#-*-coding:utf-8-*-

def maxElem(lista, kezdo=0, vegso=None):
	"a listából visszaadja a legnagyobb értékű elemet"
	if vegso==None:
		vegso = len(lista)

	legnagyobb = lista[kezdo]
	while vegso > kezdo:
		if lista[kezdo] > legnagyobb:
			legnagyobb = lista[kezdo]
		kezdo = kezdo + 1
	return legnagyobb

serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print maxElem(serie)
print maxElem(serie, 2, 5)
print maxElem(serie, 2)
