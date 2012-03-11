#!/usr/bin/env python
#-*-coding:utf-8-*-

from turtle import *

def negyzet(meret, szin):
	"meghatározott méretű és színű négyzetet rajzoló függvény"
	color(szin)
	c = 0
	while c < 4:
		forward(meret)
		right(90)
		c = c + 1
