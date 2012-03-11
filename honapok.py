#!/usr/bin/env python
#-*-coding:utf-8-*-

from random import *

def veletlen_lista(n):
	s = []
	for i in range(n):
		s.append(random())
	return s
	
def lista_nyomtatas(lista):
	"soronként írja ki a lista összes elemét"
	for elem in lista:
		print elem, 
	
lista_nyomtatas(veletlen_lista(10))
