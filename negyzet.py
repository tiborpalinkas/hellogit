#!/usr/bin/env python
#-*-coding:utf-8-*-

from math import sin, pi

for i in range(0, 91, 5):
	print "%s fok szinusza: %s" % (i, sin((2*i*pi) / 360))

