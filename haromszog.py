#!/usr/bin/env python
#-*-coding:utf-8-*-
from turtle import *

def haromszog(szin):
	# különböző színű háromszögeket rajzol
	color(szin)
	forward(100)
	left(120)
	forward(100)
	left(120)
	forward(100)
	up()
	forward(100)
	down()

haromszog('blue')
haromszog('green')
haromszog('red')
