#!/usr/bin/env python
#-*-coding:utf-8-*-

def cube(n):
	return n**3

def gombTerfogat(r):
	return 4 * 3.1416 * cube(r) / 3

r = input('Írja be a sugár értékét : ')
print 'A gömb térfogata :', gombTerfogat(r)
